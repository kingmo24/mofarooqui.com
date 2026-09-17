# mofarooqui.com — Daylight

Static, seven pages, flat file structure (every asset at the root — no /assets/
folder to lose on upload). Warm "daylight" theme with modern motion.

## Deploy (easiest)
Unzip → vercel.com → Add New → Project → drag the folder onto the deploy area.
Live in ~20s. Dragging uploads images correctly (paste corrupts PNGs).

## Domain
Vercel → Settings → Domains → add BOTH mofarooqui.com and www.mofarooqui.com.
Registrar: A @ → 76.76.21.21 ; CNAME www → cname.vercel-dns.com

## Contact form
Vercel → Settings → Environment Variables → RESEND_API_KEY + CONTACT_TO, redeploy.

## The daylight theme
All colours are tokens at the top of styles.css:
  --paper  #FBF9F4  warm background
  --ink    #1A1A17  text + hero/footer panels
  --amber  #C6603D  primary accent
  --sage   #5E7355  secondary
  --gold   #C89B3C  tertiary
Fonts: Fraunces (display), Karla (body), IBM Plex Mono (labels).
Change a token → whole site follows.

## Animations (all GPU-friendly, all respect prefers-reduced-motion)
- Hero headline reveals line by line on load
- Scroll progress bar (sage→gold→amber) at the very top
- Sections + cards fade/stagger in on scroll (IntersectionObserver)
- Magnetic buttons + fill-sweep on hover (pointer devices only)
- Cards: lift, image zoom, and a pointer-tracked warm glow
- Nav gains a shadow once you scroll; animated underline on links
- Drifting gradient orbs in the hero
Anyone with "reduce motion" set in their OS sees a calm static version.

## Editing
Edit .html directly for copy. For shared header/footer/head, edit build.py and
run `python3 build.py`.
