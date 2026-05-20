#!/usr/bin/env python3
"""Update repertoire markdown links using files from a Google Drive folder.

This script traverses a Google Drive folder recursively and rewrites markdown links
whose current URL filenames match files found in Drive.

Requirements:
- The Drive folder must be shared so files are visible to your API key.
- Set GOOGLE_API_KEY in your environment or pass --api-key.

Example:
  python music/update_links_from_google_drive.py \
    --folder-link "https://drive.google.com/drive/folders/<FOLDER_ID>" \
    --write
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import urlopen
import json


DRIVE_FOLDER_ID_RE = re.compile(r"(?:/folders/|id=)([a-zA-Z0-9_-]{10,})")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class DriveFile:
    file_id: str
    name: str
    web_view_link: str


def extract_folder_id(folder_link: str) -> str:
    match = DRIVE_FOLDER_ID_RE.search(folder_link)
    if not match:
        raise ValueError("Could not extract Google Drive folder ID from link")
    return match.group(1)


def extract_filename_from_url(url: str) -> str:
    parsed = urlparse(url)

    # Common direct-drive form: ...?id=<file_id> (no filename present)
    if parsed.path.endswith("/uc"):
        return ""

    path_name = Path(parsed.path).name
    if path_name and "." in path_name:
        return path_name

    # Fallback for query parameter driven URLs
    query_name = parse_qs(parsed.query).get("filename", [""])[0]
    return query_name


def drive_api_get(url: str) -> dict:
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def list_drive_files_recursive(folder_id: str, api_key: str) -> List[DriveFile]:
    files: List[DriveFile] = []
    queue = [folder_id]

    while queue:
        current_folder = queue.pop(0)
        page_token = ""

        while True:
            params = {
                "q": f"'{current_folder}' in parents and trashed = false",
                "fields": "nextPageToken,files(id,name,mimeType,webViewLink)",
                "pageSize": "1000",
                "includeItemsFromAllDrives": "true",
                "supportsAllDrives": "true",
                "key": api_key,
            }
            if page_token:
                params["pageToken"] = page_token

            url = "https://www.googleapis.com/drive/v3/files?" + urlencode(params)
            payload = drive_api_get(url)

            if "error" in payload:
                message = payload["error"].get("message", "Unknown Google Drive API error")
                raise RuntimeError(message)

            for entry in payload.get("files", []):
                mime = entry.get("mimeType", "")
                if mime == "application/vnd.google-apps.folder":
                    queue.append(entry["id"])
                    continue

                files.append(
                    DriveFile(
                        file_id=entry["id"],
                        name=entry.get("name", ""),
                        web_view_link=entry.get("webViewLink")
                        or f"https://drive.google.com/file/d/{entry['id']}/view",
                    )
                )

            page_token = payload.get("nextPageToken", "")
            if not page_token:
                break

    return files


def build_name_index(files: List[DriveFile]) -> Dict[str, List[DriveFile]]:
    index: Dict[str, List[DriveFile]] = {}
    for item in files:
        key = item.name.strip().lower()
        if not key:
            continue
        index.setdefault(key, []).append(item)
    return index


def rewrite_links(text: str, drive_index: Dict[str, List[DriveFile]]) -> Tuple[str, dict]:
    stats = {
        "updated": 0,
        "unchanged": 0,
        "missing": 0,
        "ambiguous": 0,
    }

    def replacement(match: re.Match[str]) -> str:
        label = match.group(1)
        url = match.group(2)

        filename = extract_filename_from_url(url)
        if not filename:
            stats["unchanged"] += 1
            return match.group(0)

        candidates = drive_index.get(filename.lower(), [])
        if not candidates:
            stats["missing"] += 1
            return match.group(0)

        if len(candidates) > 1:
            stats["ambiguous"] += 1
            return match.group(0)

        chosen = candidates[0]
        if url == chosen.web_view_link:
            stats["unchanged"] += 1
            return match.group(0)

        stats["updated"] += 1
        return f"[{label}]({chosen.web_view_link})"

    new_text = MARKDOWN_LINK_RE.sub(replacement, text)
    return new_text, stats


def update_file(path: Path, drive_index: Dict[str, List[DriveFile]], write: bool) -> dict:
    original = path.read_text(encoding="utf-8")
    updated, stats = rewrite_links(original, drive_index)

    if write and updated != original:
        path.write_text(updated, encoding="utf-8")

    return stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update repertoire markdown links from Google Drive")
    parser.add_argument("--folder-link", required=True, help="Google Drive folder link")
    parser.add_argument("--api-key", default=os.environ.get("GOOGLE_API_KEY", ""), help="Google API key")
    parser.add_argument(
        "--files",
        nargs="+",
        default=[
            "content/members/repertoire-by-part.md",
            "content/members/repertoire-special-cases.md",
        ],
        help="Markdown files to process",
    )
    parser.add_argument("--write", action="store_true", help="Write changes to disk")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.api_key:
        print("ERROR: Missing Google API key. Pass --api-key or set GOOGLE_API_KEY.")
        return 1

    try:
        folder_id = extract_folder_id(args.folder_link)
    except ValueError as err:
        print(f"ERROR: {err}")
        return 1

    try:
        drive_files = list_drive_files_recursive(folder_id, args.api_key)
    except RuntimeError as err:
        print(f"ERROR: Google Drive API: {err}")
        return 1

    drive_index = build_name_index(drive_files)
    print(f"Indexed {len(drive_files)} files from Google Drive")

    totals = {"updated": 0, "unchanged": 0, "missing": 0, "ambiguous": 0}
    repo_root = Path(__file__).resolve().parent.parent

    for relative in args.files:
        target = repo_root / relative
        if not target.exists():
            print(f"WARN: File not found, skipping: {relative}")
            continue

        stats = update_file(target, drive_index, args.write)
        for key in totals:
            totals[key] += stats[key]

        mode = "updated" if args.write else "dry-run"
        print(
            f"{relative} ({mode}) -> "
            f"updated={stats['updated']} unchanged={stats['unchanged']} "
            f"missing={stats['missing']} ambiguous={stats['ambiguous']}"
        )

    if not args.write:
        print("Dry-run complete. Re-run with --write to apply changes.")

    print(
        "Totals -> "
        f"updated={totals['updated']} unchanged={totals['unchanged']} "
        f"missing={totals['missing']} ambiguous={totals['ambiguous']}"
    )

    if totals["ambiguous"] > 0:
        print("NOTE: Ambiguous filenames were left unchanged. Rename duplicates in Drive or adjust manually.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
