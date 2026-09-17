# mofarooqui.com

Static, seven pages, no build step needed to deploy. SEO and icons are complete.

## Deploy (easiest — no GitHub)
Unzip, then vercel.com → Add New → Project → drag the folder onto the deploy area.
Live in ~20s. Dragging uploads binary images correctly (paste corrupts PNGs).

## Deploy (GitHub)
Push the folder, import at vercel.com, framework preset "Other", build/output empty.
Upload — never paste — the .png/.ico files.

## Domain
Vercel → Settings → Domains → add mofarooqui.com.
Registrar: A @ → 76.76.21.21 ; CNAME www → cname.vercel-dns.com

## Contact form
Vercel → Settings → Environment Variables:
  RESEND_API_KEY = (from resend.com)
  CONTACT_TO     = marfarooqui@gmail.com
Redeploy. Without them the form shows an "email me directly" fallback.

## SEO included
- Unique title + meta description + keywords per page
- Open Graph + Twitter card (1200x630 image) per page
- Canonical URL per page; en-CA locale
- JSON-LD graph: WebSite + Person + WebPage + BreadcrumbList on every page;
  Service (diligence), LegalService (legal), and FAQPage where FAQs are shown
- sitemap.xml (lastmod/priority) + robots.txt + site.webmanifest
- 404 set to noindex
Submit the sitemap in Google Search Console after launch: https://mofarooqui.com/sitemap.xml

## Favicons included
favicon.ico (16/32/48), favicon.svg, 16 + 32 PNG, apple-touch-icon (180),
maskable 192 + 512 for Android/PWA, safari-pinned-tab.svg.

## Editing
Edit the .html directly for copy. For shared header/footer/head changes edit
build.py and run `python3 build.py` (regenerates pages + sitemap + manifest).

## To opt out of AI crawlers
Uncomment the GPTBot / CCBot blocks in robots.txt.
