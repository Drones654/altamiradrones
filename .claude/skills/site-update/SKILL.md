---
name: site-update
description: Update the Altamira Drones website. Use this when the user wants to change content, add links, update contact info, or modify any part of the website.
allowed-tools: Read, Edit, Write, Bash, Grep, Glob
argument-hint: [what to change]
---

# Altamira Drones Website Update

You are updating the **Altamira Drones** corporate website.

## Quick Reference

| Item | Value |
|------|-------|
| **Live Site** | https://altamiradrones.com |
| **Spanish** | https://altamiradrones.com/es/ |
| **GitHub** | https://github.com/Drones654/altamiradrones |
| **Deploy** | Auto-deploys on `git push` (~30 seconds) |

## Files to Edit

- `index.html` — English homepage
- `es/index.html` — Spanish homepage (use proper accents: á, é, í, ó, ú, ñ)

**IMPORTANT**: Always update BOTH files when changing content.

## Page Structure

1. Navigation (logo, menu, language switcher)
2. Hero (headline, subtitle, CTA buttons)
3. Intro ("What we do")
4. Sector Cards (Urban, Agriculture, Innovation)
5. Urban Services section
6. Agriculture & Livestock section
7. Innovation / R&D section
8. About section
9. Contact section (email, phone, address, social links)
10. Footer

## Current Contact Info

- **Email**: altamiradronesrrss@gmail.com
- **Phone**: +34 638 099 208, +34 610 485 116
- **Address**: Calle Hermosilla 48, Piso 1, Puerta DC, 28001 Madrid
- **Instagram**: @altamira_drones
- **YouTube**: @AltamiraDrones
- **LinkedIn**: https://www.linkedin.com/company/altamira-drones

## How to Complete the Update

1. Read both HTML files to find the relevant section
2. Make the requested change in `index.html`
3. Make the equivalent change in `es/index.html` (translate if needed)
4. Commit and push:

```bash
git add -A && git commit -m "description of change

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>" && git push
```

5. Confirm the change is live (wait ~30 seconds)

## Common Tasks

### Add Social Link
Find the Social card in Contact section (~line 668) and add:
```html
<a href="URL" target="_blank" class="text-white text-sm hover:text-cyan-400 active:text-cyan-300 transition-colors block py-2 touch-link">LinkName</a>
```

### Add Image
1. Place image in `img/` folder
2. Reference: `src="img/name.jpg"` (EN) or `src="../img/name.jpg"` (ES)

### Change Text
Search for existing text, replace in both files.

## User Request

$ARGUMENTS
