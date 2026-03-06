# Altamira Drones — Site

## What This Is

Corporate website for **Altamira Drones** — a drone services company.
Bilingual (EN/ES), static HTML, deployed to Cloudflare Pages.

- **Live URL**: https://altamiradrones.com
- **ES version**: https://altamiradrones.com/es/
- **Cloudflare Pages**: project name `altamiradrones`
- **Pages domain**: altamiradrones.pages.dev
- **Custom domains**: altamiradrones.com, www.altamiradrones.com

## Structure

```
altamiradrones/
  index.html          # EN homepage (~766 lines, Tailwind CSS via CDN)
  es/index.html       # ES homepage (~676 lines)
  img/
    drone-hero.jpg    # Hero image
    drone-hero.png    # Hero image (PNG variant)
  add_dns.py          # One-off DNS record setup script (already run)
  .wrangler/          # Wrangler local state (gitignored)
  tmp/                # Temp artifacts (gitignored)
```

## Tech Stack

- **HTML + Tailwind CSS** (via CDN `cdn.tailwindcss.com`)
- **Inter font** (Google Fonts)
- **No build step** — static files, deploy the root directory directly
- **No JavaScript framework** — vanilla HTML with Tailwind utility classes
- **Responsive** — mobile-first design

## How to Deploy

Uses channent's Cloudflare dome (`sol_do_cf.py`):

```bash
# Deploy current directory to Cloudflare Pages
cd ~/e/c/channent && python sol_do_cf.py --scenario=cf.deploy \
  --cf_project=altamiradrones --cf_dir=~/e/c/altamiradrones

# Or via unified router
cd ~/e/c/channent && python sol_do_channent.py --scenario=cf.deploy \
  --cf_project=altamiradrones --cf_dir=~/e/c/altamiradrones
```

Manual alternative (wrangler direct):
```bash
~/.npm-global/bin/wrangler pages deploy ~/e/c/altamiradrones --project-name=altamiradrones
```

## How to Edit Content

Both HTML files are self-contained. Edit directly:

- **EN**: `index.html` — English homepage
- **ES**: `es/index.html` — Spanish homepage (manually translated, not auto-generated)

After editing, deploy with the command above.

### Key sections in the HTML

The page is structured with sections (look for `<section` tags):
- Hero with drone image
- Services (urban inspection, agriculture, livestock, R&D)
- About / capabilities
- Contact

### Adding images

Place images in `img/`. Reference them as `img/filename.jpg` from `index.html`
or `../img/filename.jpg` from `es/index.html`.

## DNS

Managed via Cloudflare. Current records:
- `altamiradrones.com` → Cloudflare Pages
- `www.altamiradrones.com` → CNAME to altamiradrones.pages.dev

To manage DNS:
```bash
cd ~/e/c/channent && python sol_do_cf.py --scenario=cf.dns --cf_zone=altamiradrones.com
cd ~/e/c/channent && python sol_do_cf.py --scenario=cf.dns.add --cf_zone=altamiradrones.com \
  --cf_type=CNAME --cf_name=subdomain --cf_content=target.example.com
```

Note: wrangler's OAuth token lacks `dns_records` scope. The dome falls back to
browser automation (AppleScript JS into Cloudflare dashboard) for DNS operations.

## Cache

To purge CDN cache after deploy (usually not needed — Pages auto-purges):
```bash
cd ~/e/c/channent && python sol_do_cf.py --scenario=cf.purge --cf_zone=altamiradrones.com
```

## Wrangler Auth

Wrangler uses OAuth, token at `~/Library/Preferences/.wrangler/config/default.toml`.
If expired:
```bash
cd ~/e/c/channent && python sol_do_cf.py --scenario=cf.login
# or directly: ~/.npm-global/bin/wrangler login
```

## Important

- **No build step** — deploy the directory as-is
- **Wrangler path**: `~/.npm-global/bin/wrangler` (not in default subprocess PATH)
- **Two languages are independent files** — changes to EN must be manually mirrored to ES
- **Tailwind via CDN** — no local install, no purge step, works offline-first
