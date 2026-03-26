# Downloaded Content Categorization

**Download Date:** 26 March 2026  
**Source:** https://www.tottenhamcommunitychoir.org/

---

## Downloaded Files Summary

All HTML files have been organized into two directories based on access level.

### 🌐 Public Pages (6 files)

**Location:** `public/` directory

Publicly accessible pages (no authentication required):

1. **index.html** (40 KB) - Home page
2. **joining-tcc.html** (38 KB) - How to join the choir
3. **about-us.html** (38 KB) - About the choir
4. **news-and-dates.html** (38 KB) - News and upcoming events
5. **gallery.html** (76 KB) - Public photo gallery
6. **how-to-find-us.html** (39 KB) - Location and directions

### 🔒 Members-Only Pages (9 files)

**Location:** `members-only/` directory

Password-protected content accessible only to current choir members:

1. **members-area.html** (36 KB) - Members area landing page
2. **repertoire.html** (68 KB) - Current & past repertoire with 70+ MP3 practice tracks
3. **comments-and-chat.html** (36 KB) - Member discussion/communication
4. **contact.html** (41 KB) - Members-only contact form and information
5. **dress-code.html** (39 KB) - Performance attire guidelines
6. **feedback.html** (87 KB) - Member feedback system
7. **members-gallery.html** (41 KB) - Private member photos
8. **serving-refreshments.html** (39 KB) - Refreshment duty rota/instructions
9. **video-gallery.html** (96 KB) - Performance videos

---

## Reference Documentation

- **ORIGINAL_SITE_REFERENCE.md** - Complete documentation of all public pages and site structure
- **MEMBERS_AREA_REFERENCE.md** - Detailed documentation of the 9 members-only pages
- **public/** - Directory containing 6 public HTML pages (no authentication required)
- **members-only/** - Directory containing 9 password-protected HTML pages

---

## Notes for Nuxt Migration

1. **Public pages** (`public/` folder): Can be accessed directly without authentication
2. **Members-only pages** (`members-only/` folder): Require password authentication (Password: Copland0!)
3. The contact.html in members-only is different from any public contact information
4. All content needed for the rebuild is now available in these two folders

---

## Total Content

- **15 HTML pages** downloaded
- **269 KB** of public content
- **484 KB** of members-only content
- **Total: 753 KB** of HTML content ready for Nuxt migration
