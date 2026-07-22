#!/usr/bin/env python3
"""
Builds the static pages for mofarooqui.com.

You can edit the generated .html files directly — they are plain HTML and that is
fine for copy changes. Use this script instead when you change something shared
(the nav, the footer, the head tags), so all pages stay in sync:

    python3 build.py
"""

import pathlib

SITE = "https://mofarooqui.com"
NAV = [
    ("Diligence", "/diligence"),
    ("Legal", "/legal"),
    ("Marketing", "/marketing"),
    ("Work", "/work"),
    ("About", "/about"),
    ("Contact", "/contact"),
]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400"
         "&family=Karla:wght@400;500"
         "&family=IBM+Plex+Mono:wght@400"
         "&display=swap")


def nav(active):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{name}</a>'
        for name, href in NAV
    )
    return f"""<nav class="nav">
  <div class="wrap">
    <a class="logo" href="/"><img src="/assets/mark.svg" alt="" width="34" height="34"><span>M. A. R. Farooqui</span></a>
    <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
      <span class="bars" aria-hidden="true"><i></i><i></i></span>
      <span class="sr">Menu</span>
    </button>
    <div class="nav-links" id="nav-menu">{links}<a class="menu-cta" href="/contact">Book a call</a></div>
    <a class="cta" href="/contact">Book a call</a>
  </div>
</nav>
<div class="nav-scrim" id="nav-scrim" hidden></div>"""


FOOTER = """<footer class="foot">
  <div class="wrap pad-sm">
    <div class="foot-grid">
      <div>
        <h4>Mohammed A. R. Farooqui</h4>
        <p class="prose prose-dark" style="font-size:.9375rem">Quality of Earnings, underwriting, and licensed paralegal work. Pickering and Toronto, serving Ontario and remote engagements across Canada and the United States.</p>
      </div>
      <div>
        <h4>Practices</h4>
        <ul>
          <li><a href="/diligence">Diligence &amp; underwriting</a></li>
          <li><a href="/legal">Paralegal services</a></li>
          <li><a href="/marketing">Marketing &amp; growth</a></li>
          <li><a href="/work">Work &amp; record</a></li>
        </ul>
      </div>
      <div>
        <h4>Direct</h4>
        <ul>
          <li><a href="mailto:marfarooqui@gmail.com">marfarooqui@gmail.com</a></li>
          <li><a href="tel:+16472003526">+1 (647) 200-3526</a></li>
          <li><a href="https://www.linkedin.com/in/kingmo24" rel="me noopener">LinkedIn</a></li>
          <li><a href="/mo-farooqui.vcf" download>Save contact card</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">
      This site is general information, not legal or financial advice. Sending a message does not create a paralegal&ndash;client relationship, and nothing here should be relied on until an engagement letter is signed. Paralegal services are provided within the scope of practice permitted in Ontario by the Law Society of Ontario. Fees shown are starting points and depend on scope.<br><br>
      &copy; 2017&ndash;<span id="yr">2026</span> Mohammed A. R. Farooqui &middot; Sound Marketing Canada Inc.
    </p>
  </div>
</footer>"""


def shell(*, path, title, description, body, active, schema=""):
    canonical = SITE + ("/" if path == "index" else f"/{path}")
    schema_block = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1110">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{schema_block}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav(active)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="/main.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# shared blocks
# --------------------------------------------------------------------------

def cta_band(heading, sub, primary=("Book a call", "/contact"), secondary=None):
    second = f'<a class="btn btn-line" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    return f"""<section class="dark grain pad">
  <div class="wrap band">
    <h2 class="h-lg rise">{heading}</h2>
    <p class="lead rise">{sub}</p>
    <div class="actions rise">
      <a class="btn btn-brass" href="{primary[1]}">{primary[0]}</a>
      {second}
    </div>
  </div>
</section>"""


STEPS = """<ol class="steps">
  <li class="rise"><span class="n">Step 01</span><h3>Scoping call</h3><p>What the deal is, what is at stake, and what records exist. If I am not the right person for it, you will hear that on this call.</p><span class="dur">30 minutes &middot; no charge</span></li>
  <li class="rise"><span class="n">Step 02</span><h3>Document request</h3><p>A specific list, not a fishing expedition: statements, general ledger, bank reconciliations, tax filings, payroll, material contracts.</p><span class="dur">Fixed quote &middot; retainer</span></li>
  <li class="rise"><span class="n">Step 03</span><h3>Analysis</h3><p>Normalize the statements, test every add-back against evidence, prove out cash, and work through working capital, margin, and concentration.</p><span class="dur">Two to four weeks</span></li>
  <li class="rise"><span class="n">Step 04</span><h3>Report and debrief</h3><p>Written findings with adjustments laid out line by line, then a call to walk through where the number moves and what it gives you to negotiate.</p><span class="dur">Report plus one hour</span></li>
</ol>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

PAGES = {}

PAGES["index"] = dict(
    title="Mohammed A. R. Farooqui — Quality of Earnings, Underwriting &amp; Paralegal Services | Ontario",
    description="Quality of Earnings and EBITDA analysis, mortgage and credit underwriting, licensed paralegal representation, and growth marketing. Pickering and Toronto, Ontario.",
    active="/",
    schema="""{"@context":"https://schema.org","@type":"Person","name":"Mohammed A. R. Farooqui","url":"https://mofarooqui.com/","image":"https://mofarooqui.com/assets/portrait-card.png","jobTitle":"Licensed Paralegal & Financial Analyst","email":"mailto:marfarooqui@gmail.com","telephone":"+1-647-200-3526","address":{"@type":"PostalAddress","addressLocality":"Pickering","addressRegion":"ON","addressCountry":"CA"},"sameAs":["https://www.linkedin.com/in/kingmo24"],"worksFor":{"@type":"Organization","name":"Sound Marketing Canada Inc."},"knowsAbout":["Quality of Earnings","EBITDA analysis","Mortgage underwriting","Paralegal services","Digital marketing"]}""",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">Pickering &middot; Toronto &middot; Ontario</span>
    <h1 class="h-xl rise" style="--i:1">Read the numbers<br>as closely as the <span class="italic brass">contract</span>.</h1>
    <p class="lead rise" style="--i:2">I am a licensed Ontario paralegal and financial analyst. I test the earnings behind a deal, underwrite the credit behind a loan, and represent clients when the file turns into a dispute.</p>
    <div class="actions rise" style="--i:3">
      <a class="btn btn-brass" href="/contact">Book a scoping call</a>
      <a class="btn btn-line" href="/diligence">See how diligence runs</a>
    </div>
    <dl class="hero-meta rise" style="--i:4">
      <div><dt>Practice</dt><dd>Diligence &amp; underwriting</dd></div>
      <div><dt>Licensed</dt><dd>Ontario</dd></div>
      <div><dt>Engagements</dt><dd>GTA &amp; remote</dd></div>
      <div><dt>Response</dt><dd>One business day</dd></div>
    </dl>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Three practices, one discipline</h2><span class="eyebrow eyebrow-mute">Where to start</span></div>
    <div class="cards">
      <a class="card rise" href="/diligence">
        <img src="/assets/art-diligence.svg" alt="Reported earnings adjusted down to a normalized figure" width="600" height="380" loading="lazy">
        <div class="card-body"><span class="eyebrow">For buyers &amp; lenders</span><h3>Diligence &amp; underwriting</h3><p>Quality of Earnings, EBITDA normalization, and mortgage or credit underwriting. The work that decides whether a price is defensible.</p><span class="more">Explore &rarr;</span></div>
      </a>
      <a class="card rise" href="/legal">
        <img src="/assets/art-legal.svg" alt="A filed record with an official seal" width="600" height="380" loading="lazy">
        <div class="card-body"><span class="eyebrow">For claimants &amp; respondents</span><h3>Paralegal services</h3><p>Representation within the scope permitted to Ontario paralegals, from the first demand letter through to hearing.</p><span class="more">Explore &rarr;</span></div>
      </a>
      <a class="card rise" href="/marketing">
        <img src="/assets/art-marketing.svg" alt="A funnel narrowing from reach to closed clients" width="600" height="380" loading="lazy">
        <div class="card-body"><span class="eyebrow">For operators</span><h3>Marketing &amp; growth</h3><p>Campaigns, lead generation, and analytics through Sound Marketing Canada, built on what the numbers say rather than what looks busy.</p><span class="more">Explore &rarr;</span></div>
      </a>
    </div>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="split split-wide">
      <div class="rise">
        <span class="eyebrow">The through-line</span>
        <h2 class="h-lg mt-1">Complexity is where most people lose money.</h2>
      </div>
      <div class="rise">
        <p class="lead">I started by building a marketing and technology firm, which pulled me into the financial side of every deal it touched. That led to underwriting, then to Quality of Earnings work, then to a paralegal licence when the same clients kept running into disputes.</p>
        <p class="prose prose-dark">Three regulated worlds &mdash; finance, law, and technology &mdash; and one job in all of them: work out what is actually true before someone signs, and say it plainly.</p>
        <div class="portrait-block">
          <img src="/assets/portrait.png" alt="Mohammed A. R. Farooqui" width="184" height="184">
          <span><span class="sig">Mohammed A. R. Farooqui</span><span class="cap">Licensed paralegal &amp; financial analyst</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">How an engagement runs</h2><span class="eyebrow eyebrow-mute">Four steps</span></div>
    {STEPS}
  </div>
</section>

<section class="dark grain pad-sm">
  <div class="wrap">
    <div class="pull rise">
      <blockquote>His analysis caught what we would have missed, and gave us the terms to negotiate with.</blockquote>
      <cite>Private equity investor</cite>
    </div>
  </div>
</section>

{cta_band("Bring me the file before you sign it.", "Thirty minutes, no charge, and a straight answer on whether the work is worth doing.", secondary=("See fees", "/diligence#fees"))}""",
)

PAGES["diligence"] = dict(
    title="Quality of Earnings &amp; Underwriting — Mohammed A. R. Farooqui",
    description="Quality of Earnings reports, EBITDA normalization, and mortgage and credit underwriting for buyers, lenders, and owners in Ontario and remote.",
    active="/diligence",
    schema="""{"@context":"https://schema.org","@type":"Service","serviceType":"Quality of Earnings and financial due diligence","provider":{"@type":"Person","name":"Mohammed A. R. Farooqui"},"areaServed":"CA","url":"https://mofarooqui.com/diligence"}""",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">Practice 01</span>
    <h1 class="h-lg rise" style="--i:1">Quality of Earnings<br>&amp; <span class="italic brass">underwriting</span></h1>
    <p class="lead rise" style="--i:2">A stated EBITDA figure is an argument, not a fact. My job is to test it &mdash; and to tell you what the business actually earns before the price is fixed.</p>
    <div class="actions rise" style="--i:3"><a class="btn btn-brass" href="/contact">Book a scoping call</a><a class="btn btn-line" href="#fees">See fees</a></div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div class="rise">
        <span class="eyebrow eyebrow-mute">What it is</span>
        <h2 class="h-md mt-1">Not an audit. A different question.</h2>
      </div>
      <div class="rise prose">
        <p>An audit asks whether the financial statements comply with the accounting standards. A Quality of Earnings analysis asks something narrower and far more useful to a buyer: how much of the reported profit is real, repeatable, and still going to be there after closing.</p>
        <p>That means going behind the add-backs. Owner compensation, one-time revenue, related-party arrangements, deferred maintenance, capitalized costs that should have hit the income statement &mdash; each one either survives evidence or comes out of the number.</p>
      </div>
    </div>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">What you receive</h2><span class="eyebrow">Deliverables</span></div>
    <ul class="checks">
      <li>Normalized EBITDA with every adjustment itemized and sourced</li>
      <li>Add-back schedule showing what survived testing and what did not</li>
      <li>Working capital analysis and a peg recommendation</li>
      <li>Proof of cash and revenue reconciliation to bank</li>
      <li>Customer and supplier concentration</li>
      <li>Margin walk by period and by line</li>
      <li>Quality of revenue: recurring versus one-time</li>
      <li>A findings memo written for a decision, not a file</li>
    </ul>
    <p class="lead mt-3 rise">Underwriting engagements follow the same discipline applied to credit: capacity, collateral, structure, and the scenarios where the loan stops performing.</p>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">How it runs</h2><span class="eyebrow eyebrow-mute">Four steps</span></div>
    {STEPS}
  </div>
</section>

<section class="dark grain pad" id="fees">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Fees</h2><span class="eyebrow">All amounts CAD</span></div>
    <div class="fees">
      <div class="fee rise"><div><h3>Quality of Earnings</h3><p>Full diligence engagement including the report, the adjustment schedules, and the debrief call. Priced on deal size, entities and periods in scope, and the state of the records.</p></div><span class="amt">$73,589<small>Engagement, from</small></span></div>
      <div class="fee rise"><div><h3>Underwriting review</h3><p>Credit and mortgage underwriting, risk assessment, and scenario modelling on a single facility or a portfolio.</p></div><span class="amt">On request<small>Scoped per file</small></span></div>
      <div class="fee rise"><div><h3>Consulting</h3><p>Strategy, capital allocation, operations, and go-to-market advisory where you need a second set of eyes on a decision rather than a full report.</p></div><span class="amt">$7,359<small>Engagement, from</small></span></div>
    </div>
    <p class="prose prose-dark mt-2">You get a fixed quote after the scoping call, before any work begins. Compressed timelines are possible and are priced accordingly.</p>
  </div>
</section>

<section class="pad">
  <div class="wrap narrow">
    <div class="rule-head"><h2 class="h-md">Questions</h2><span class="eyebrow eyebrow-mute">Before you call</span></div>
    <div class="faq">
      <details><summary>How long does it take?</summary><div class="answer"><p>Two to four weeks from the day the document request is filled. The clock is usually set by how fast the target produces records, not by the analysis itself.</p></div></details>
      <details><summary>Can you work from incomplete books?</summary><div class="answer"><p>Often, yes &mdash; reconstructed statements are common in owner-operated businesses. It takes longer and it costs more, and I will tell you at the scoping call whether the records can support a defensible number at all.</p></div></details>
      <details><summary>Do you work sell-side?</summary><div class="answer"><p>Yes. A sell-side QoE run before you go to market finds the adjustments a buyer would have used against you, which is generally cheaper than finding them during the buyer's diligence.</p></div></details>
      <details><summary>Do you work outside Ontario?</summary><div class="answer"><p>Financial analysis, underwriting, and consulting are handled remotely anywhere in Canada and the United States. Paralegal representation is limited to Ontario.</p></div></details>
    </div>
  </div>
</section>

{cta_band("Test the number before you pay for it.", "Thirty minutes on the phone will tell us both whether this engagement is worth running.")}""",
)

PAGES["legal"] = dict(
    title="Paralegal Services in Ontario — Mohammed A. R. Farooqui",
    description="Licensed Ontario paralegal. Small Claims Court, provincial offences, Landlord and Tenant Board, and administrative tribunals. Pickering and the Greater Toronto Area.",
    active="/legal",
    schema="""{"@context":"https://schema.org","@type":"LegalService","name":"Mohammed A. R. Farooqui, Paralegal","areaServed":{"@type":"State","name":"Ontario"},"url":"https://mofarooqui.com/legal","telephone":"+1-647-200-3526"}""",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">Practice 02</span>
    <h1 class="h-lg rise" style="--i:1">Paralegal representation,<br><span class="italic brass">Ontario</span></h1>
    <p class="lead rise" style="--i:2">Most disputes are lost on preparation rather than argument. I take the file seriously from the first letter, and I tell you early when the case is not worth what it will cost to run.</p>
    <div class="actions rise" style="--i:3"><a class="btn btn-brass" href="/contact">Describe your matter</a><a class="btn btn-line" href="#scope">What I can act on</a></div>
  </div>
</section>

<section class="pad" id="scope">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">What I can act on</h2><span class="eyebrow eyebrow-mute">Scope of practice</span></div>
    <div class="ledger">
      <div class="ledger-row rise"><span class="k">Claims</span><span class="v">Small Claims Court</span><span class="n">Debt recovery, contract disputes, unpaid invoices, property damage, and defence of the same.</span></div>
      <div class="ledger-row rise"><span class="k">Offences</span><span class="v">Provincial offences</span><span class="n">Matters under the Provincial Offences Act, including traffic and regulatory charges.</span></div>
      <div class="ledger-row rise"><span class="k">Housing</span><span class="v">Landlord and Tenant Board</span><span class="n">Applications and hearings for landlords and tenants.</span></div>
      <div class="ledger-row rise"><span class="k">Tribunals</span><span class="v">Administrative tribunals</span><span class="n">Boards and tribunals where paralegal representation is permitted in Ontario.</span></div>
      <div class="ledger-row rise"><span class="k">Advisory</span><span class="v">Commercial disputes</span><span class="n">Demand letters, settlement negotiation, and document preparation ahead of a claim.</span></div>
    </div>
    <p class="prose mt-2" style="color:var(--mute)">Paralegal licensure in Ontario does not cover every matter. Family law, criminal indictable matters, real estate conveyancing, wills and estates, and Superior Court proceedings fall outside my scope. If your matter sits there, I will tell you at the first call and point you toward a lawyer rather than take a retainer I should not take.</p>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="split">
      <div class="rise"><span class="eyebrow">The advantage</span><h2 class="h-lg mt-1">A file that is also a financial file.</h2></div>
      <div class="rise prose">
        <p>Commercial disputes turn on numbers as often as they turn on law. Quantum of damages, the accounting behind a broken contract, whether the other side can actually satisfy a judgment &mdash; these are financial questions attached to a legal proceeding.</p>
        <p>That combination is unusual and it is the reason most of my legal work is commercial. The analysis and the representation happen in one place instead of being handed between two firms.</p>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">How a matter runs</h2><span class="eyebrow eyebrow-mute">Four steps</span></div>
    <ol class="steps">
      <li class="rise"><span class="n">Step 01</span><h3>Intake</h3><p>What happened, what you want, and what documents exist. Conflicts are checked before anything else.</p><span class="dur">30 minutes &middot; no charge</span></li>
      <li class="rise"><span class="n">Step 02</span><h3>Assessment</h3><p>An honest read on merits, likely cost, and whether the amount at stake justifies the fight.</p><span class="dur">Written where useful</span></li>
      <li class="rise"><span class="n">Step 03</span><h3>Retainer and filing</h3><p>Engagement terms in writing, then demand, claim, or defence, with settlement pursued wherever it beats a hearing.</p><span class="dur">Fees agreed up front</span></li>
      <li class="rise"><span class="n">Step 04</span><h3>Hearing</h3><p>Preparation of evidence and submissions, and representation on the day.</p><span class="dur">Timeline set by the tribunal</span></li>
    </ol>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap narrow">
    <div class="rule-head"><h2 class="h-md">Questions</h2><span class="eyebrow">Before you call</span></div>
    <div class="faq">
      <details><summary>What does it cost?</summary><div class="answer"><p>Quoted per matter after intake, either as a flat fee for defined work or hourly where the scope cannot be fixed in advance. You will have the terms in writing before I start.</p></div></details>
      <details><summary>Is a paralegal different from a lawyer?</summary><div class="answer"><p>Yes. Paralegals are licensed and regulated by the Law Society of Ontario, and can represent clients in a defined set of forums &mdash; Small Claims Court, provincial offences, and certain tribunals. Lawyers have a wider scope. For matters inside paralegal scope, the cost is usually materially lower.</p></div></details>
      <details><summary>Can you act for me if you did the financial analysis?</summary><div class="answer"><p>Sometimes, and it has to be assessed file by file. The roles carry different duties and a conflict can arise. I will raise it at intake rather than after a retainer is signed.</p></div></details>
    </div>
  </div>
</section>

{cta_band("Tell me what happened.", "Bring the documents you have. Thirty minutes will usually tell you whether you have a matter worth running.")}""",
)

PAGES["marketing"] = dict(
    title="Marketing &amp; Growth — Sound Marketing Canada | Mohammed A. R. Farooqui",
    description="Campaigns, lead generation, analytics, and online profile management for small businesses, real estate, and government procurement. Sound Marketing Canada Inc.",
    active="/marketing",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">Practice 03</span>
    <h1 class="h-lg rise" style="--i:1">Marketing judged<br>by <span class="italic brass">qualified leads</span></h1>
    <p class="lead rise" style="--i:2">Sound Marketing Canada Inc. builds campaigns, funnels, and analytics for small businesses, real estate, and firms bidding on government work. The reporting is built to be read by someone who understands a P&amp;L.</p>
    <div class="actions rise" style="--i:3"><a class="btn btn-brass" href="/contact">Request a plan</a><a class="btn btn-line" href="#fees">See fees</a></div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">What we run</h2><span class="eyebrow eyebrow-mute">Services</span></div>
    <div class="ledger">
      <div class="ledger-row rise"><span class="k">Acquisition</span><span class="v">Lead generation</span><span class="n">Multi-channel campaigns with tracking that ties spend to closed business rather than to impressions.</span></div>
      <div class="ledger-row rise"><span class="k">Search</span><span class="v">SEO &amp; content</span><span class="n">Technical fixes, local search, and content built around what buyers actually search for.</span></div>
      <div class="ledger-row rise"><span class="k">Measurement</span><span class="v">Analytics &amp; dashboards</span><span class="n">Attribution set up properly once, so the monthly report answers whether it worked.</span></div>
      <div class="ledger-row rise"><span class="k">Reputation</span><span class="v">Online profile management</span><span class="n">Audit and cleanup across search, directories, reviews, and the profiles a prospect checks before calling.</span></div>
      <div class="ledger-row rise"><span class="k">Procurement</span><span class="v">Bid readiness</span><span class="n">Registration and classification support for public sector work: SAM, CAGE, UEI, NAICS, and UNSPSC coding.</span></div>
    </div>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="split">
      <div class="rise">
        <span class="eyebrow">In development</span>
        <h2 class="h-lg mt-1">Sound AI</h2>
        <p class="lead mt-1">A predictive marketing tool that forecasts revenue and surfaces trends, built on Google Cloud with iOS and Android front ends and chatbot features.</p>
      </div>
      <div class="rise"><img src="/assets/art-marketing.svg" alt="A funnel narrowing from reach to closed clients" width="600" height="380" loading="lazy" style="border:1px solid var(--rule-d)"></div>
    </div>
  </div>
</section>

<section class="pad" id="fees">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Fees</h2><span class="eyebrow eyebrow-mute">All amounts CAD</span></div>
    <div class="fees">
      <div class="fee rise"><div><h3>Digital marketing</h3><p>Campaign build and management, lead generation, funnel work, and analytics setup with monthly reporting.</p></div><span class="amt">$221<small>Per month, from</small></span></div>
      <div class="fee rise"><div><h3>Online profile management</h3><p>Audit, optimize, and protect your presence across search, directories, and review platforms.</p></div><span class="amt">$588<small>Per engagement</small></span></div>
      <div class="fee rise"><div><h3>Procurement readiness</h3><p>Registrations, classification coding, and bid documentation for public sector opportunities.</p></div><span class="amt">On request<small>Scoped per client</small></span></div>
    </div>
  </div>
</section>

{cta_band("Tell me what you are selling.", "A short call and a look at your current numbers is enough to say whether marketing is your constraint.", primary=("Request a plan", "/contact"))}""",
)

PAGES["work"] = dict(
    title="Work &amp; Record — Mohammed A. R. Farooqui",
    description="Selected positions, companies, projects, and registrations. Sound Marketing Canada, LendX Financial Technologies, NEO Legal Services, CIBC, and government procurement work.",
    active="/work",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">The record</span>
    <h1 class="h-lg rise" style="--i:1">What I have built<br>and <span class="italic brass">where I have worked</span></h1>
    <p class="lead rise" style="--i:2">A selected record rather than a complete one. The full history is on LinkedIn.</p>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Companies &amp; projects</h2><span class="eyebrow eyebrow-mute">Founded or co-founded</span></div>
    <div class="cards">
      <div class="card rise"><img src="/assets/art-marketing.svg" alt="" width="600" height="380" loading="lazy"><div class="card-body"><span class="eyebrow">2017 &mdash;</span><h3>Sound Marketing Canada</h3><p>Marketing and technology firm serving small business, real estate, and government procurement. Platform partnerships across Shopify, Google, Meta, BBB, and Ariba SAP.</p></div></div>
      <div class="card rise"><img src="/assets/art-diligence.svg" alt="" width="600" height="380" loading="lazy"><div class="card-body"><span class="eyebrow">2026 &mdash;</span><h3>LendX Financial Technologies</h3><p>Co-founded to take the underwriting and diligence work that runs on spreadsheets today and turn it into a product.</p></div></div>
      <div class="card rise"><img src="/assets/art-legal.svg" alt="" width="600" height="380" loading="lazy"><div class="card-body"><span class="eyebrow">2023 &mdash;</span><h3>NEO Legal Services</h3><p>Professional corporation through which the Ontario paralegal practice runs.</p></div></div>
    </div>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Selected positions</h2><span class="eyebrow">2017 &rarr; today</span></div>
    <div class="ledger">
      <div class="ledger-row rise"><span class="k">2023 &mdash;</span><span class="v">NEO Legal Services</span><span class="n">In-house counsel</span></div>
      <div class="ledger-row rise"><span class="k">2026 &mdash;</span><span class="v">LendX Financial Technologies</span><span class="n">Co-founder</span></div>
      <div class="ledger-row rise"><span class="k">2017 &mdash;</span><span class="v">Sound Marketing Canada</span><span class="n">Founder &amp; project development manager</span></div>
      <div class="ledger-row rise"><span class="k">2024 &ndash; 2026</span><span class="v">Sound Hedge Fund Corporation</span><span class="n">Financial analyst</span></div>
      <div class="ledger-row rise"><span class="k">2025 &ndash; 2026</span><span class="v">PFSL Investments Canada</span><span class="n">Financial advisor</span></div>
      <div class="ledger-row rise"><span class="k">2023 &ndash; 2024</span><span class="v">CIBC</span><span class="n">Mortgage advisor</span></div>
      <div class="ledger-row rise"><span class="k">2021 &ndash; 2024</span><span class="v">AR Technologies &amp; Data</span><span class="n">Portfolio specialist, government procurement</span></div>
      <div class="ledger-row rise"><span class="k">2020 &ndash; 2024</span><span class="v">Century 21 &amp; eXp Realty</span><span class="n">Realtor, then associate broker</span></div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap narrow">
    <div class="rule-head"><h2 class="h-md">Registrations</h2><span class="eyebrow eyebrow-mute">Sound Marketing Canada Inc.</span></div>
    <div class="ledger">
      <div class="ledger-row rise two-col"><span class="k">CAGE</span><span class="v">L0S95</span></div>
      <div class="ledger-row rise two-col"><span class="k">UEI</span><span class="v">P297PSMMSUG7</span></div>
      <div class="ledger-row rise two-col"><span class="k">NAICS</span><span class="v">Coverage across 21 sectors</span></div>
    </div>
  </div>
</section>

{cta_band("Working on something that needs this?", "Tell me what it is and I will tell you whether I am the right person for it.")}""",
)

PAGES["about"] = dict(
    title="About — Mohammed A. R. Farooqui",
    description="Licensed Ontario paralegal and financial analyst. Honours B.Com from Telfer, paralegal at triOS College, urban land economics at UBC Sauder, and postgraduate AI at Durham College.",
    active="/about",
    body=f"""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">About</span>
    <h1 class="h-lg rise" style="--i:1">Finance, law,<br>and the space <span class="italic brass">between them</span></h1>
    <div class="portrait-block rise" style="--i:2;max-width:30rem">
      <img src="/assets/portrait.png" alt="Mohammed A. R. Farooqui" width="184" height="184">
      <span><span class="sig">Mohammed A. R. Farooqui</span><span class="cap">Pickering, Ontario</span></span>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div class="rise"><span class="eyebrow eyebrow-mute">The path</span><h2 class="h-md mt-1">It started with building something.</h2></div>
      <div class="rise prose">
        <p>Sound Marketing Canada came first &mdash; a marketing and technology firm for small businesses and real estate, built while I was finishing an Honours Bachelor of Commerce at the Telfer School of Management.</p>
        <p>Running it meant looking closely at other people's businesses, and the financial side turned out to be the part I was best at and most interested in. That took me into underwriting at CIBC, then into analysis and Quality of Earnings work, then to a paralegal licence when it became clear how often the same clients were ending up in disputes they were not prepared for.</p>
        <p>Setbacks are part of the record too. Losing the family home in 2021 taught me more about credit, structure, and how quickly a plan can come apart than anything I studied. It is a large part of why I am blunt with clients about downside.</p>
      </div>
    </div>
  </div>
</section>

<section class="dark grain pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">Education</h2><span class="eyebrow">Qualifications</span></div>
    <div class="ledger">
      <div class="ledger-row rise"><span class="k">2020</span><span class="v">Honours Bachelor of Commerce</span><span class="n">International Management &middot; Telfer School of Management, University of Ottawa</span></div>
      <div class="ledger-row rise"><span class="k">2025</span><span class="v">Paralegal, Law</span><span class="n">triOS College Business Technology Healthcare</span></div>
      <div class="ledger-row rise"><span class="k">2023</span><span class="v">Urban Land Economics</span><span class="n">Diploma Program &middot; UBC Sauder School of Business, Real Estate Division</span></div>
      <div class="ledger-row rise"><span class="k">2027</span><span class="v">Artificial Intelligence, Analysis &amp; Design</span><span class="n">Postgraduate &middot; Durham College &middot; in progress</span></div>
    </div>
    <div class="rule-head mt-3"><h2 class="h-md">Licensing &amp; certification</h2><span class="eyebrow">Current</span></div>
    <div class="ledger">
      <div class="ledger-row rise"><span class="k">LSO</span><span class="v">Licensed paralegal</span><span class="n">Law Society of Ontario</span></div>
      <div class="ledger-row rise"><span class="k">CSI</span><span class="v">Canadian Securities Course &amp; IFC</span><span class="n">Canadian Securities Institute</span></div>
      <div class="ledger-row rise"><span class="k">LLQP</span><span class="v">Life Licence Qualification Program</span><span class="n">Harmonized</span></div>
      <div class="ledger-row rise"><span class="k">AML</span><span class="v">Anti-Money Laundering</span><span class="n">Certification</span></div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="rule-head"><h2 class="h-md">How I work</h2><span class="eyebrow eyebrow-mute">What to expect</span></div>
    <ul class="checks">
      <li>You get the downside first, then the upside</li>
      <li>Fixed quote before work starts, not after</li>
      <li>If I am the wrong person for it, I say so on the first call</li>
      <li>Findings written for a decision, not for a file</li>
      <li>Conflicts raised at intake, not after a retainer</li>
      <li>Replies inside one business day</li>
    </ul>
  </div>
</section>

{cta_band("Start with a conversation.", "Thirty minutes, no charge, and a straight answer on whether I can help.")}""",
)

PAGES["contact"] = dict(
    title="Contact — Mohammed A. R. Farooqui",
    description="Book a scoping call for Quality of Earnings, underwriting, paralegal matters, or marketing. Pickering and Toronto, Ontario. Replies within one business day.",
    active="/contact",
    body="""<section class="dark grain hero">
  <div class="wrap inner">
    <span class="eyebrow rise" style="--i:0">Contact</span>
    <h1 class="h-lg rise" style="--i:1">Start a <span class="italic brass">file</span></h1>
    <p class="lead rise" style="--i:2">Tell me what the matter is and what is at stake. The more specific you are, the more useful the first call will be. I reply within one business day.</p>
  </div>
</section>

<section class="dark pad" style="background:var(--ink-2)">
  <div class="wrap">
    <div class="split">
      <form class="form rise" id="contact-form" novalidate>
        <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="topic">What do you need</label>
          <select id="topic" name="topic">
            <option>Quality of Earnings / EBITDA</option>
            <option>Mortgage or credit underwriting</option>
            <option>Paralegal matter</option>
            <option>Consulting</option>
            <option>Marketing</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="field"><label for="message">Details</label><textarea id="message" name="message" required></textarea></div>
        <input class="hp" type="text" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div><button class="btn btn-brass" type="submit">Send message</button></div>
        <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      </form>

      <div class="rise">
        <span class="eyebrow">Direct</span>
        <div class="contact-lines mt-1">
          <a href="mailto:marfarooqui@gmail.com"><span>Email</span><strong>marfarooqui@gmail.com</strong></a>
          <a href="tel:+16472003526"><span>Phone</span><strong>+1 (647) 200-3526</strong></a>
          <a href="https://www.linkedin.com/in/kingmo24" rel="me noopener"><span>LinkedIn</span><strong>linkedin.com/in/kingmo24</strong></a>
          <a href="/mo-farooqui.vcf" download><span>Contact card</span><strong>Save to your phone</strong></a>
        </div>
        <p class="prose prose-dark mt-2" style="font-size:.9375rem">Sending a message does not create a paralegal&ndash;client relationship. Please do not send confidential documents until an engagement is agreed.</p>
      </div>
    </div>
  </div>
</section>""",
)

PAGES["404"] = dict(
    title="Page not found — Mohammed A. R. Farooqui",
    description="That page does not exist.",
    active="",
    body="""<section class="dark grain" style="min-height:70vh;display:grid;align-content:center">
  <div class="wrap void">
    <span class="eyebrow">Error 404</span>
    <h1 class="h-lg">This page is not<br>in the <span class="italic brass">file</span>.</h1>
    <p class="lead" style="margin-inline:auto;max-width:44ch">The address is wrong or the page has moved.</p>
    <div class="actions" style="justify-content:center"><a class="btn btn-brass" href="/">Back to the site</a><a class="btn btn-line" href="/contact">Contact</a></div>
  </div>
</section>""",
)


def main():
    out = pathlib.Path(__file__).parent
    for name, page in PAGES.items():
        html = shell(
            path=name,
            title=page["title"],
            description=page["description"],
            body=page["body"],
            active=page["active"],
            schema=page.get("schema", ""),
        )
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        print(f"wrote {name}.html")

    # sitemap
    urls = "".join(
        f"<url><loc>{SITE}/{'' if n == 'index' else n}</loc></url>"
        for n in PAGES if n != "404"
    )
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
