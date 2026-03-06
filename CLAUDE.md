# Altamira Drones — Website

## What This Is

Corporate website for **Altamira Drones** — a drone services company.
Bilingual (EN/ES), static HTML, hosted on Cloudflare Pages.

- **Live URL**: https://altamiradrones.com
- **ES version**: https://altamiradrones.com/es/
- **Hosting**: Cloudflare Pages (auto-deploys when you push to GitHub)

## Structure

```
altamiradrones/
  index.html          # English homepage
  es/
    index.html        # Spanish homepage
  img/
    drone-hero.jpg    # Hero image
    drone-hero.png    # Hero image (PNG variant)
  CLAUDE.md           # This file
  .gitignore          # Git ignore rules
```

## Tech Stack

- **HTML + Tailwind CSS** (loaded from CDN — no install needed)
- **Inter font** (Google Fonts)
- **No build step** — these are plain HTML files, nothing to compile
- **No frameworks** — vanilla HTML with Tailwind utility classes
- **Responsive** — works on mobile and desktop

## How to Make Changes

### 1. Edit the files

Open `index.html` (English) or `es/index.html` (Spanish) in any text editor.

The pages are organized in `<section>` blocks:
- Hero banner with drone image
- Services (urban inspection, agriculture, livestock, R&D)
- About / capabilities
- Contact information

### 2. Preview locally

Just open `index.html` in your browser — it works as a local file.
No server needed.

### 3. Deploy

Push to GitHub — Cloudflare auto-deploys within ~30 seconds:

```bash
git add -A
git commit -m "describe your change"
git push
```

That's it. The site updates automatically.

## How to Add Images

1. Put the image in the `img/` folder
2. Reference it in HTML:
   - From `index.html`: `<img src="img/photo.jpg">`
   - From `es/index.html`: `<img src="../img/photo.jpg">` (note the `../`)
3. Commit and push

## Two Languages

English and Spanish are **separate HTML files**. They are NOT auto-synced.
If you change content in `index.html`, manually update `es/index.html` too.

The language switcher links between them:
- EN page links to `/es/` for Spanish
- ES page links to `/` for English

## DNS & Domain

The domain `altamiradrones.com` is managed through Cloudflare.
DNS changes are done in the Cloudflare dashboard (not in this repo).

Current setup:
- `altamiradrones.com` → Cloudflare Pages
- `www.altamiradrones.com` → redirects to main domain

## Troubleshooting

**Site not updating after push?**
- Cloudflare Pages typically deploys in 30 seconds
- Check the Cloudflare Pages dashboard for build status
- Try hard-refresh in browser (Ctrl+Shift+R / Cmd+Shift+R)

**Tailwind styles not working locally?**
- The page needs internet to load Tailwind from CDN
- If offline, styles won't render (but the content is still there)

**Want to test on your phone?**
- Push to GitHub, wait 30 seconds, open altamiradrones.com on your phone
