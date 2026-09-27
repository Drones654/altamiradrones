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
  es/index.html       # Spanish homepage
  golf/index.html     # News: aerial coverage of the architects' golf tournament (ES)
  privacidad/, terminos/   # Legal pages (ES)
  css/altamira.css    # Shared stylesheet for every page
  img/web/            # Optimised images used by the pages (toro.png = logo)
  img/torre-san-leonardo-crop.glb   # 3D model shown in "Projects"
  _redirects          # Cloudflare Pages redirects (/golf/gracias/ -> /golf/)
  CLAUDE.md
```

## Design system (Sep 2026 redesign)

Same look as the Arquivir portfolio and the Geoxa dossier: white background,
Segoe UI Light / Semibold (Open Sans fallback), rust red `#8C2418`, greys
`#6E6E6E` / `#9B9B9B`, thin rules, numbered services (01, 02...) and large photos.
All tokens live at the top of `css/altamira.css`.

Image captions state where each image comes from:
- `Trabajo realizado por Altamira Drones` / `Work by Altamira Drones` for our own work
- `Esquema ilustrativo` / `Illustrative diagram` for the thermal diagrams
- Pexels stock photos carry only a descriptive caption
Do NOT use Víctor de la Fuente's photos on the website.

## Page Sections (homepages)

1. **Navigation** — logo, anchors, ES/EN switch (white over the hero, solid on scroll)
2. **Hero** — full-bleed photo, headline, CTA
3. **Intro** — what we do + how we work
4. **Services index** — numbered list 01–12
5. **Services 01–11** — each: number, title, text, "what's included", fact sheet, images
6. **12 Agriculture & livestock**
7. **Featured project** — San Leonardo 3D viewer (`orientation="0deg -90deg 0deg"`: the model is Z-up)
8. **News** — links to /golf/
9. **About**
10. **Contact** — FormSubmit form (`formsubmit.co/ajax/altamiradronesrrss@gmail.com`)
11. **Footer**

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
1. Find the "Redes" / "Social" row in the Contact section
2. Add a new `<a>` tag following the existing pattern
3. Update both EN and ES files
4. Commit and push

### Add an image
1. Resize (max ~1800 px wide, JPEG quality ~80) and put it in `img/web/`
2. Reference in HTML:
   - From `index.html`: `src="img/web/photo.jpg"`
   - From `es/index.html`: `src="../img/web/photo.jpg"`
3. Commit and push

### Change contact info
1. Search for the current value (email, phone, etc.)
2. Replace in both `index.html` and `es/index.html`
3. Commit and push

## Tech Stack

- **Plain HTML + one stylesheet** (`css/altamira.css`) — no Tailwind any more
- **Segoe UI** (Windows) with **Open Sans** fallback (Google Fonts)
- **model-viewer** from jsDelivr for the 3D model
- **No build step** — plain HTML files
- **No frameworks** — vanilla HTML and a few lines of JS
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
