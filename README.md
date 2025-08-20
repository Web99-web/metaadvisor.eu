# News Brief (Hugo + Netlify)

Minimalni Hugo skeleton za automatizirani news sajt (bez osobnih podataka).

## Brzi start
1) Napravi novi **GitHub repo** (prazan).
2) Uploadaj sadržaj ovog foldera u taj repo.
3) Na **Netlify**: "Add new site" → "Import from Git" → odaberi repo.
   - Build command: `hugo`
   - Publish directory: `public`
   - Environment → `HUGO_VERSION = 0.126.1`
4) Nakon deploya, u Netlify → **Domains** → "Add custom domain" i slijedi DNS upute.

## Struktura
- `content/news/` — objave
- `layouts/_default/` — minimalni layout (bez teme)
- `layouts/partials/ads/` — mjesta za reklame
- `layouts/partials/analytics.html` — doda se CF/Plausible skripta
- `static/robots.txt`

## Napomena
Ovaj repo ne sadrži RSS agregator. Njega možeš dodati kasnije (GitHub Actions).
