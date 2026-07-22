# mofarooqui.com

Static site, one page, no build step. Deployed on Vercel.

```
index.html          the whole page
styles.css          design tokens at the top — change colours/type once, everywhere updates
main.js             scroll reveals + contact form submit
api/contact.js      Vercel serverless function that emails the form
assets/             original artwork (SVG) + social card + headshot placeholder
mo-farooqui.vcf     the "save my contact" e-business card
vercel.json         caching + security headers
```

## Deploy

```bash
npm i -g vercel
cd path/to/this/folder
vercel            # first run: links the project, gives you a preview URL
vercel --prod     # ships it live
```

Or push the folder to GitHub and click **Add New → Project** at vercel.com. Vercel
detects it as a static site with no framework — leave build settings empty.

## Point mofarooqui.com at it

Vercel dashboard → your project → **Settings → Domains** → add `mofarooqui.com`
and `www.mofarooqui.com`. Vercel prints the exact records; at your registrar set:

| Type  | Name | Value                  |
|-------|------|------------------------|
| A     | @    | `76.76.21.21`          |
| CNAME | www  | `cname.vercel-dns.com` |

TLS is issued automatically once DNS propagates (usually minutes, up to 48h).

## Turn on the contact form

The form posts to `/api/contact`. Without keys it will fail and show the
"email me directly" fallback, so set this up before launch:

1. Sign up at **resend.com**, create an API key.
2. Vercel → Settings → **Environment Variables**:
   - `RESEND_API_KEY` = your key
   - `CONTACT_TO` = `marfarooqui@gmail.com`
3. Redeploy.

To send from `mo@mofarooqui.com` instead of the shared test address, verify the
domain in Resend (it gives you DKIM records), then change the `from:` line in
`api/contact.js`.

Simpler alternative: make a form at **formspree.io**, and in `index.html` change
the form to `<form action="https://formspree.io/f/YOURID" method="POST">` and
delete the fetch block in `main.js`. No environment variables needed.

## The headshot

`assets/portrait.png` is your photo, upscaled 2x from the 92px original and cut to a
circle with a transparent background. It is displayed at 88px, which is the largest
size that still looks sharp. **Send a full-resolution version and this can get bigger.**
To swap it: replace `assets/portrait.png` (square, transparent circle) and
`assets/portrait-card.png` (square, on `#DEE7DB`, used for the social preview).

`assets/og.png` is the social card that renders when the link is shared. Regenerate it
if the photo changes.

## Editing content

Everything is plain HTML in `index.html`, in the order it appears on the page.
Prices live in the `<span class="price">` elements. Timeline entries are `<li>`
items. Colours and fonts are the `:root` variables at the top of `styles.css`.

## Local preview

```bash
npx serve .
```
