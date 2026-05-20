#!/usr/bin/env python3
"""
Convert repertoire-by-part.md to repertoire.yml YAML config.

Parses the "## Current Repertoire" section only and generates a structured YAML file
with songs, slugs, and local file paths.

Combined-voice parts (e.g., "Bass and Tenor") are split into two entries, one per voice.
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse


def slugify(text):
    """Generate URL-safe slug from text."""
    # Lowercase
    text = text.lower()
    # Replace em-dash, slash with nothing
    text = text.replace('—', '').replace('/', '')
    # Replace spaces with dash
    text = text.replace(' ', '-')
    # Remove apostrophes, commas, parentheses
    text = re.sub(r"[',()]", '', text)
    # Collapse multiple dashes
    text = re.sub(r'-+', '-', text)
    # Strip leading/trailing dashes
    text = text.strip('-')
    return text


def normalize_part_label(identifier):
    """Convert part identifier to normalized slug for localPath."""
    # Lowercase and prepare
    label_lower = identifier.lower()

    # Expand common shorthands
    replacements = {
        'sop1': 'soprano-1',
        'sop2': 'soprano-2',
        'sop': 'soprano',
        'alto1': 'alto-1',
        'alto2': 'alto-2',
        'ten1': 'tenor-1',
        'ten2': 'tenor-2',
        'ten': 'tenor',
    }

    # Try direct replacement first
    if label_lower in replacements:
        return replacements[label_lower]

    # Otherwise, slugify naturally
    result = label_lower.replace(' ', '-').replace('+', '-')
    result = re.sub(r'[^a-z0-9-]', '', result)
    result = re.sub(r'-+', '-', result)
    return result.strip('-')


def get_voice_folder(identifier):
    """Determine voice folder(s) from part identifier."""
    identifier_lower = identifier.lower()
    voices = []

    # Determine which voices this part contains
    if 'sop' in identifier_lower:
        voices.append('Soprano')
    if 'alto' in identifier_lower:
        voices.append('Alto')
    if 'ten' in identifier_lower or 'tenor' in identifier_lower:
        voices.append('Tenor')
    if 'bass' in identifier_lower:
        voices.append('Bass')

    # If no match found, try to infer (shouldn't happen with clean data)
    if not voices:
        voices.append('Soprano')  # Default fallback

    return voices


def extract_filename(url):
    """Extract filename from URL."""
    parsed = urlparse(url)
    # Get the last part of the path
    filename = parsed.path.split('/')[-1]
    # Remove query parameters if any
    filename = filename.split('?')[0]
    return filename


def parse_markdown(filepath):
    """Parse the markdown file and extract Current Repertoire section."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the Current Repertoire section (stop at ## Later or end of file)
    match = re.search(
        r'## Current Repertoire\n(.+?)(?=\n## Later|\Z)',
        content,
        re.DOTALL
    )

    if not match:
        print("ERROR: Could not find '## Current Repertoire' section")
        sys.exit(1)

    repertoire_text = match.group(1)

    # Parse songs: ### Song Name followed by bullet points
    songs = []
    # Updated pattern: song heading + content until next heading or end
    song_pattern = r'### ([^\n]+)\n((?:\n|.)+?)(?=###|\Z)'

    for song_match in re.finditer(song_pattern, repertoire_text, re.MULTILINE | re.DOTALL):
        title = song_match.group(1).strip()
        parts_text = song_match.group(2)

        # Parse parts
        parts = []
        link_pattern = r'- \[([^\]]+)\]\(([^)]+)\)'

        for link_match in re.finditer(link_pattern, parts_text):
            label = link_match.group(1).strip()
            url = link_match.group(2).strip()

            original_filename = extract_filename(url)

            # Determine voice folders for this part
            voices = get_voice_folder(label)
            part_slug = normalize_part_label(label)

            # Create an entry for each voice (handles combined parts)
            for voice in voices:
                part_entry = {
                    'originalIdentifier': label,
                    'originalUrl': url,
                    'originalFilename': original_filename,
                    'voice': voice,
                    'part_slug': part_slug,
                }
                parts.append(part_entry)

        if parts:
            songs.append({
                'title': title,
                'slug': slugify(title),
                'parts': parts,
            })

    return songs


def generate_yaml(songs):
    """Generate YAML string from songs data."""
    lines = ['songs:']

    for song in songs:
        lines.append(f'  - title: {song["title"]}')
        lines.append(f'    slug: {song["slug"]}')
        lines.append('    parts:')

        for part in song['parts']:
            lines.append(f'      - originalIdentifier: {part["originalIdentifier"]}')
            lines.append(f'        originalUrl: {part["originalUrl"]}')
            lines.append(f'        originalFilename: {part["originalFilename"]}')

            local_path = f'{part["voice"]}/{song["slug"]}_{part["part_slug"]}.mp3'
            # Preserve file extension from original
            _, ext = part["originalFilename"].rsplit('.', 1)
            local_path = local_path.rsplit('.', 1)[0] + f'.{ext}'

            lines.append(f'        localPath: {local_path}')

        lines.append('')

    return '\n'.join(lines)


def main():
    # Get paths using __file__ to be explicit
    script_file = Path(__file__).resolve()
    script_dir = script_file.parent  # music/
    repo_root = script_dir.parent     # tcc-website/

    md_file = repo_root / 'content' / 'members' / 'repertoire-by-part.md'
    yaml_file = script_dir / 'repertoire.yml'

    if not md_file.exists():
        print(f"ERROR: Markdown file not found: {md_file}")
        sys.exit(1)

    print(f"Parsing {md_file.name}...")
    songs = parse_markdown(md_file)

    print(f"Found {len(songs)} songs")

    # Count total parts
    total_parts = sum(len(s['parts']) for s in songs)
    print(f"Found {total_parts} total part entries (including duplicates for combined parts)")

    yaml_content = generate_yaml(songs)

    with open(yaml_file, 'w') as f:
        f.write(yaml_content)

    print(f"✓ Generated {yaml_file.name}")


if __name__ == '__main__':
    main()
