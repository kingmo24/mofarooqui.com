# mofarooqui.com — v4

Seven pages, static HTML, no build step required to deploy. Hosted on Vercel.

```
index.html        home
diligence.html    QoE, EBITDA, underwriting, consulting  → /diligence
legal.html        paralegal practice                     → /legal
marketing.html    Sound Marketing Canada                 → /marketing
work.html         companies, positions, registrations    → /work
about.html        story, education, licensing            → /about
contact.html      form + direct lines                    → /contact
404.html          not-found page

styles.css        all design tokens live in :root at the top
main.js           reveals, nav state, contact form
build.py          optional generator (see below)
api/contact.js    serverless function that emails the form
assets/           artwork, portrait, icons, social card
```

Clean URLs are on, so `diligence.html` is served at `/diligence`. Keep the links
without the `.html` extension.

## Editing

For copy changes, **edit the `.html` files directly** — they are plain HTML and
that is the simplest path.

The header and footer are repeated in every page. If you change something shared
(a nav link, the footer, the disclaimer), edit `build.py` and run:

```bash
python3 build.py
```

That regenerates all pages and the sitemap. If you have edited the HTML by hand
since the last build, your changes will be overwritten — so pick one approach and
stay with it. For most updates, editing the HTML is fine.

## Design tokens

Everything visual comes from the variables at the top of `styles.css`:

| Token | Value | Used for |
|---|---|---|
| `--ink` | `#0B1110` | dark sections, footer |
| `--bone` | `#EDEBE4` | light sections |
| `--brass` | `#A97F45` | accents, prices, links |
| `--display` | Cormorant Garamond | headings |
| `--body` | Karla | body text |
| `--mono` | IBM Plex Mono | labels, figures |

Change a value there and the whole site follows.

## Deploy

```bash
npm i -g vercel
vercel --prod
```

Or push to GitHub and import the repo at vercel.com. Framework preset: **Other**.
Build command and output directory: leave empty.

Domain: Vercel → Settings → Domains → add `mofarooqui.com`. At your registrar,
A record `@` → `76.76.21.21`, CNAME `www` → `cname.vercel-dns.com`.

## Contact form

Set two environment variables in Vercel, then redeploy:

- `RESEND_API_KEY` — from resend.com
- `CONTACT_TO` — `marfarooqui@gmail.com`

Without them the form shows the "email me directly" fallback. Never commit the key.

## The headshot

`assets/portrait.png` is your photo upscaled 2× from a 92px original, cut to a
transparent circle. It is displayed at 84px, which is as large as it can go while
staying sharp. Send a full-resolution photo and it can be used much bigger —
including a proper portrait on the About page.

Regenerate `assets/og.png` (the social preview) if the photo changes.

## Local preview

```bash
npx serve .        # static only
vercel dev         # includes the contact form function
```
