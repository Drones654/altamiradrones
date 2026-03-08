# Altamira Drones — Website

## Quick Commands

When the user asks to update the site, use these commands:

```bash
# After editing files, deploy:
git add -A && git commit -m "description" && git push

# Check status:
git status

# See recent changes:
git log --oneline -5
```

## What This Is

Corporate website for **Altamira Drones** — a drone services company.
Bilingual (EN/ES), static HTML, hosted on Cloudflare Pages.

- **Live URL**: https://altamiradrones.com
- **ES version**: https://altamiradrones.com/es/
- **GitHub**: https://github.com/Drones654/altamiradrones
- **Hosting**: Cloudflare Pages (auto-deploys when you push to GitHub)
- **Cloudflare Project**: altamiradrones.carlosgzmarcos.workers.dev

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

## Page Sections

Both pages have these sections (edit in order):
1. **Navigation** — logo, menu links, language switcher
2. **Hero** — main headline, subtitle, CTA buttons, drone image
3. **Intro** — "What we do" overview
4. **Sector Cards** — Urban, Agriculture, Innovation links
5. **Urban Services** — inspection, photogrammetry, etc.
6. **Agriculture & Livestock** — crops, animals, monitoring
7. **Innovation / R&D** — focus areas
8. **About** — company info, locations (Madrid, Europe, USA)
9. **Contact** — email, phone, address, social links
10. **Footer** — logo, nav links, copyright

## Contact Info (current)

- **Email**: altamiradronesrrss@gmail.com
- **Phone**: +34 638 099 208, +34 610 485 116
- **Address**: Calle Hermosilla 48, Piso 1, Puerta DC, 28001 Madrid
- **Instagram**: @altamira_drones
- **YouTube**: @AltamiraDrones
- **LinkedIn**: https://www.linkedin.com/company/altamira-drones

## Common Tasks

### Change text content
1. Edit `index.html` (English) and `es/index.html` (Spanish)
2. Both files must be updated separately — they are NOT synced
3. Run: `git add -A && git commit -m "update text" && git push`

### Add a social media link
1. Find the "Social" card in the Contact section (~line 668 in index.html)
2. Add a new `<a>` tag following the existing pattern
3. Update both EN and ES files
4. Commit and push

### Add an image
1. Put image in `img/` folder
2. Reference in HTML:
   - From `index.html`: `src="img/photo.jpg"`
   - From `es/index.html`: `src="../img/photo.jpg"`
3. Commit and push

### Change contact info
1. Search for the current value (email, phone, etc.)
2. Replace in both `index.html` and `es/index.html`
3. Commit and push

## Tech Stack

- **HTML + Tailwind CSS** (loaded from CDN — no install needed)
- **Inter font** (Google Fonts)
- **No build step** — plain HTML files
- **No frameworks** — vanilla HTML with Tailwind utility classes
- **Responsive** — works on mobile and desktop

## Two Languages

English and Spanish are **separate HTML files**. They are NOT auto-synced.
If you change content in `index.html`, manually update `es/index.html` too.

**Important for Spanish**: Use proper accents (á, é, í, ó, ú, ñ, ü)

## Deploy Process

Push to GitHub — Cloudflare auto-deploys within ~30 seconds:

```bash
git add -A
git commit -m "describe your change"
git push
```

## Troubleshooting

**Site not updating after push?**
- Cloudflare Pages typically deploys in 30 seconds
- Hard-refresh browser: Ctrl+Shift+R (Windows) / Cmd+Shift+R (Mac)

**Git push rejected?**
- Run: `git pull --rebase && git push`

**Need to check what changed?**
- Run: `git diff`
