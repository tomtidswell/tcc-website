# TCC Website — Claude Guidelines

## Stack

- **Nuxt 4** with `compatibilityVersion: 4`
- **@nuxt/content** for markdown-driven pages
- **SCSS** for all styles, with global variables auto-imported via Vite
- **pnpm** as the package manager

## Project Structure

- `app/` — Nuxt app source (pages, components, styles)
- `content/` — Markdown content, organised into collections: `home/`, `events/`, `members/`
- `public/` — Static assets
- `app/assets/styles/_variables.scss` — All colour and design tokens
- `app/assets/styles/content.scss` — Prose/markdown styles, globally loaded

## Colours

**Always use SCSS variables from `_variables.scss`.** Never write hardcoded colour values (`#aaa`, `white`, `rgba(255,255,255,...)`, etc.) in any `.vue` or `.scss` file. If a new colour is needed, add a variable first then use it.

## Styles

- All component styles use `<style scoped lang="scss">`
- SCSS variables from `_variables.scss` are available everywhere via `additionalData` in `nuxt.config.ts` — no need to import them manually
- Mobile breakpoint is `768px`; content sections use `600px` for footer columns
- Content section horizontal padding is handled at the `.content-section` level in `content.scss`

## Content

- Pages are built from markdown collections queried with `useAsyncData` + `queryCollection`
- Custom components available in markdown: `::Alert{type="..."}`, `::Accordion{title="..."}`
- No blockquotes, code blocks, ordered lists, or inline code are used in content — don't add styles for these

## Members Area Auth

- Client-side password protection using SHA-256 hashing via Web Crypto API
- `app/composables/useAuth.ts` — `login()`, `logout()`, `checkSession()`; auth state in `sessionStorage`
- `app/middleware/auth.ts` — guards all `/members/**` routes; skips on server so `nuxt generate` works
- `app/pages/members/login.vue` — explicit route, takes priority over the `[...slug]` catch-all
- To change the password: generate a new SHA-256 hash and update `PASSWORD_HASH` in `useAuth.ts`
    ```
    node -e "const {subtle}=require('crypto').webcrypto,enc=new TextEncoder();subtle.digest('SHA-256',enc.encode('your-password')).then(h=>console.log(Array.from(new Uint8Array(h)).map(b=>b.toString(16).padStart(2,'0')).join('')))"
    ```

## Deployment

- Deployed to GitHub Pages at `www.tomtidswell.co.uk/tcc-website/`
- Uses `nuxt generate` (static output to `.output/public/`)
- `app.baseURL` is set to `/tcc-website/` in `nuxt.config.ts`
- GitHub Actions workflow at `.github/workflows/deploy.yml` deploys on push to `main`
