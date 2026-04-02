# Tottenham Community Choir Website

A modern Nuxt 4 rebuild of the Tottenham Community Choir website.

## About

This is a complete rebuild of the original Tottenham Community Choir website (https://www.tottenhamcommunitychoir.org/) using Nuxt 4 and Nuxt Content. The original site content has been preserved and migrated to a modern, maintainable framework.

## Features

- ✅ **6 Public Pages**: Home, Joining TCC, About Us, News & Dates, Gallery, How to Find Us
- ✅ **9 Members-Only Pages**: Complete members area with repertoire, practice tracks, and internal resources
- ✅ **70+ Practice Tracks**: MP3 links for all vocal parts across 17 current songs
- ✅ **Responsive Navigation**: Mobile-friendly hamburger menu
- ✅ **Content Management**: Markdown-based content with Nuxt Content

## Project Structure

```
├── app/
│   ├── app.vue              # Main layout with navigation and footer
│   └── components/
│       └── Navigation.vue   # Site navigation component
├── content/
│   ├── *.md                 # Public pages
│   └── members/             # Members-only pages
│       ├── index.md         # Members area landing
│       ├── repertoire.md    # Practice tracks (70+ MP3 links)
│       └── *.md             # Other member resources
├── old-site-archive/
│   ├── html-files/
│   │   ├── public/          # Original public HTML pages
│   │   └── members-only/    # Original members HTML pages
│   ├── ORIGINAL_SITE_REFERENCE.md
│   ├── MEMBERS_AREA_REFERENCE.md
│   ├── ACCESSING_MEMBERS_PAGES.md
│   └── CONTENT_CATEGORIZATION.md
└── public/                  # Static assets
```

## Setup

Install dependencies (using pnpm):

```bash
pnpm install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
pnpm dev
```

## Production

Build the application for production:

```bash
pnpm build
```

Preview production build:

```bash
pnpm preview
```

## Original Site Archive

The original site content is preserved in `old-site-archive/`:

- **HTML Files**: All original public and members-only pages
- **Documentation**: Complete reference documents for content migration
- **Authentication Guide**: Instructions for accessing password-protected pages

## Next Steps

- [ ] Implement authentication for members area
- [ ] Add image galleries (public and members)
- [ ] Embed Google Map on "How to Find Us" page
- [ ] Style refinements to match original site aesthetic
- [ ] Upload practice MP3 files to hosting
- [ ] Add video gallery functionality

## Tech Stack

- **Framework**: Nuxt 4.4.2
- **Content**: Nuxt Content 3.12.0
- **Package Manager**: pnpm
- **Deployment**: TBD

## License

© Tottenham Community Choir 2015
