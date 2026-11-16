import sys, os
OUT = sys.argv[1]

LOGO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 3h14l-3.2 5H4.8z"/><path d="M5 9.5h17l-3.2 5H1.8z"/><path d="M5.2 16h14l-3.2 5H2z"/></svg>'
ARROW_NE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
ARROW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12H4M10 6l-6 6 6 6"/></svg>'
ARROW_D = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v16M6 14l6 6 6-6"/></svg>'
LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.06c.53-1 1.83-1.9 3.76-1.9 4 0 4.88 2.4 4.88 5.9V21h-4v-5c0-1.3-.03-2.9-1.9-2.9s-2.1 1.4-2.1 2.8V21h-4z"/></svg>'
GH = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.420-3.580-8-8-8z"/></svg>'

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body id="top">
'''

def nav(cur=''):
    def a(href, label, key):
        c = ' aria-current="page"' if cur == key else ''
        return f'<a href="{href}"{c}>{label}</a>'
    return f'''<header class="nav">
  <a class="brand" href="index.html" aria-label="Saira Garg — home">{LOGO}<span>Saira Garg</span></a>
  <nav class="nav-links" aria-label="Primary">
    {a("index.html#work", "Work", "work")}
    {a("about.html", "About", "about")}
    {a("about.html#experience", "Resume", "resume")}
  </nav>
</header>
'''

FOOTER = f'''<footer class="footer">
  <div class="footer-top">
    <div>
      <h2>From concepts to creation, let’s make it happen</h2>
      <p>I’d love to tell you more about my projects and how I build. So, connect with me today and let’s start a conversation about what matters the most.</p>
    </div>
    <div class="badge" aria-hidden="true">
      <svg class="ring" viewBox="0 0 120 120">
        <defs><path id="circ" d="M60,60 m-47,0 a47,47 0 1,1 94,0 a47,47 0 1,1 -94,0"/></defs>
        <circle cx="60" cy="60" r="58" fill="none" stroke="#6b6b6b" stroke-width="1"/>
        <text font-family="Noto Sans, sans-serif" font-size="9" fill="#e8e8e8"><textPath href="#circ" textLength="288" lengthAdjust="spacing">SAIRA GARG • PRODUCT MANAGER •</textPath></text>
      </svg>
      <svg class="mark" viewBox="0 0 24 24" fill="#e8e8e8"><path d="M8 3h14l-3.2 5H4.8z"/><path d="M5 9.500h17l-3.200 5H1.800z"/><path d="M5.200 16h14l-3.200 5H2z"/></svg>
    </div>
  </div>
  <hr class="footer-rule">
  <div class="footer-bottom">
    <div>
      <div class="mail-label">My mail id</div>
      <a class="mail" href="mailto:sairagarg11@gmail.com">sairagarg11@gmail.com</a>
      <div class="socials">
        <a href="https://www.linkedin.com/in/saira-garg" target="_blank" rel="noopener" aria-label="LinkedIn">{LI}</a>
        <a href="https://github.com/SAIRAGARG" target="_blank" rel="noopener" aria-label="GitHub">{GH}</a>
      </div>
    </div>
    <a class="totop" href="#top">{ARROW_L}<span>GO TO TOP</span></a>
  </div>
</footer>
</body>
</html>
'''

def card(title, desc, href, pill_label, pill_href, img, alt, cls='', ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'''    <article class="card">
      <div class="card-body">
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="card-actions">
          <a class="round" href="{href}" aria-label="Open {alt}">{ARROW_NE}</a>
          <a class="pill" href="{pill_href}"{t}>{pill_label}</a>
        </div>
      </div>
      <a class="card-media {cls}" href="{href}" tabindex="-1" aria-hidden="true"><img src="{img}" alt=""></a>
    </article>
'''

def tile(big, tag, title, text):
    return f'''      <div class="tile"><div class="tile-top"><span class="tag">{tag}</span><span class="big">{big}</span></div><div class="tile-body"><b>{title}</b><span>{text}</span></div></div>
'''

# ------------------------------------------------------------------ HOME
home = head("Saira Garg — Product Manager", "Portfolio of Saira Garg — co-founder of TRACKR and software engineer at Cisco, building products from user research to launch.") + nav('work') + f'''
<section class="hero">
  <span class="glow l1"></span><span class="glow l2"></span><span class="glow r1"></span><span class="glow r2"></span>
  <h1>Hi, I’m Saira Garg<br>a Product Manager</h1>
  <p>who turns user and market insight into products, and takes them from problem to launch with engineering, design and business teams</p>
</section>

<main>
  <section class="wrap" id="work">
    <h2 class="section-title">Projects &amp; Case studies</h2>
    <p class="section-sub">A glimpse of my recent work</p>
    <div class="cards">
{card("TRACKR : Fitness Coaching Platform", "Co-founded a coaching platform for coaches and gyms, from 8 coach interviews to a live product with 30+ coaches in early access in under 1 month. Owned the PRD, pricing, metrics and the AI insights roadmap.", "trackr.html", "Live Product", "https://trackrdaily.com", "assets/trackr/product.jpg", "the TRACKR case study", "trackr", True)}
    <article class="card">
      <div class="card-body">
        <h3>MainStreet : AI Local Discovery</h3>
        <p>An AI-powered, route-aware discovery app for expats in Swiss cities. Defined the problem, AI matching model, scope, metrics and experiment plan. It began with my sister’s move to Zürich.</p>
        <div class="card-actions">
          <a class="round" href="mainstreet.html" aria-label="Open the MainStreet case study">{ARROW_NE}</a>
          <a class="pill" href="mainstreet.html">Case Study</a>
        </div>
      </div>
      <a class="card-media ms" href="mainstreet.html" tabindex="-1" aria-hidden="true"><img src="assets/mainstreet/hifi-new-1.jpeg" alt=""><img src="assets/mainstreet/hifi-new-2.jpeg" alt=""></a>
    </article>
{card("YouTube Video-to-Article AI", "Built a tool that turns any YouTube video into a skimmable, screenshot-rich article, processing 2-hour videos in under 5 minutes with Whisper, GPT-4 Vision and LLM writing.", "video-to-article.html", "See Examples", "video-to-article.html#examples", "assets/video-article/shark-tank.jpg", "the Video-to-Article case study", "va")}
{card("Settle : Relocation &amp; Travel Planner", "Sized a 281M-person market, ran interviews and a survey, mapped 8 competitors and prioritised a 4-feature, AI-assisted MVP for people moving abroad.", "settle.html", "Case Study", "settle.html", "assets/home/settle-card.jpg", "the Settle case study")}
    </div>
  </section>

  <section class="lower">
    <div class="wrap">
      <h2 class="section-title">Where I’ve Worked &amp; Led</h2>
      <div class="tiles">
{tile("Cisco", "Jul 2026 – Present", "Software Engineer", "Building cloud management for campus switches on the Meraki Dashboard.")}
{tile("Snapdeal", "Jan – Apr 2025", "Software Engineering Intern", "Built in-house seller advertising tools with the product and marketing teams.")}
{tile("100+", "Founder", "Run Club, Bathinda", "Started a local running community from zero, organising bi-weekly group runs.")}
{tile("Myntra", "HackerRamp 2024", "Shared Carts", "Designed, prototyped and presented a social shopping feature that lets friends build and check out one cart together.")}
      </div>
    </div>
  </section>
</main>
''' + FOOTER

# ------------------------------------------------------------------ CASE STUDY HELPERS (PM framing)
def h2(num, title, sub=''):
    t = f'<h2 class="tight"><span class="num">{num}</span>{title}</h2>' if sub else f'<h2><span class="num">{num}</span>{title}</h2>'
    return t + (f'<p class="sub">{sub}</p>' if sub else '')
def stats(items):
    return '<div class="stats">' + ''.join(f'<div class="stat"><b>{b}</b><span>{s}</span></div>' for b, s in items) + '</div>'
def meta(items):
    return '<div class="meta">' + ''.join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in items) + '</div>'
def table(head, rows):
    h = ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table class="table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'
def pillars(items, cls='pillars'):
    return f'<div class="{cls}">' + ''.join(f'<div class="pillar"><i>{i}</i><b>{b}</b>{t}</div>' if i else f'<div class="pillar"><b>{b}</b>{t}</div>' for i, b, t in items) + '</div>'
def why(items):
    return '<div class="why">' + ''.join(f'<div><b>{b}</b><span>{t}</span></div>' for b, t in items) + '</div>'
def tldr(items):
    return '<div class="tldr">' + ''.join(f'<div><span>{k}</span><p>{v}</p></div>' for k, v in items) + '</div>'
def img(path, alt, cap=''):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure><img src="assets/{path}" alt="{alt}" loading="lazy">{c}</figure>'
def label(t):
    return f'<p class="flag">{t}</p>'

# ------------------------------------------------------------------ SETTLE
def chart(q, vals, mx):
    bars = ''.join(f'<i data-v="{v}" style="height:{v/mx*100:.1f}%"></i>' for v in vals)
    return f'<div class="chart"><h4>{q}</h4><div class="plot"><div class="bars">{bars}</div><div class="x"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></div><small>Increasing order of difficulty →</small></div>'
SURVEY = ('<div class="survey" role="img" aria-label="Survey results: number of people per difficulty rating from 1 to 5, for four questions">'
    + chart("How challenging was it to manage and keep track of relocation-related tasks?", [0, 18, 8, 34, 20], 36)
    + chart("How challenging was it to find reliable and trustworthy information?", [0, 8, 22, 28, 22], 32)
    + chart("To what extent did you feel lonely or isolated after the move?", [0, 2, 10, 30, 38], 42)
    + chart("How stressful did you find the overall relocation process?", [2, 4, 16, 18, 30], 32) + '</div>')

settle = head("Settle — Relocation & Travel Partner · Saira Garg", "Product case study: Settle, an AI-assisted relocation app, from market sizing and user research to a prioritised MVP.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <div class="eyebrow">Product case study · Discovery to MVP · 8 weeks</div>
    <h1>Settle | Relocation &amp; Travel Partner</h1>
    <p class="lede">A personal relocation assistant that turns the chaos of moving to a new country into a clear, guided, and manageable process.</p>
    <figure class="cover sharp"><img src="assets/settle/hero.avif" alt="Settle app screens: sign-up, relocation task plan, documents, community and AI assistant"></figure>
    {meta([("ROLE", "Product owner, end to end"), ("TIMELINE", "8-week sprint"), ("SCOPE", "Research · Strategy · MVP")])}
    {tldr([("Problem", "Moving abroad means hundreds of fragmented tasks spread across government sites, forums and chats, and no single place tells you what to do next."), ("What I did", "Sized the market, ran interviews and a survey, mapped 8 competitors, prioritised a 4-feature MVP and took it to a clickable prototype."), ("Outcome", "A phased, AI-assisted relocation plan that fills a gap none of the 8 competitors covered: one personal journey from visa to feeling at home.")])}

    {h2("01", "The Problem")}
    <p>International relocation is rarely a seamless transition. It is a complex web of hundreds of fragmented tasks, and the order matters: you often need a bank account to rent a flat, but an address to open the bank account.</p>
    <p>Existing tools solve isolated pieces (task lists, document storage, B2B relocation services) and leave the individual mover to stitch them together.</p>

    {h2("02", "Market Opportunity")}
    <p>Migration is no longer a niche event. According to the 2024 UN World Migration Report there are roughly 281 million international migrants, a number that has doubled since 1990, and the OECD reports over 6 million people move permanently to developed countries every year, before counting students and digital nomads.</p>
    {stats([("281M", "international migrants worldwide"), ("2×", "growth since 1990"), ("6M+", "permanent moves to OECD countries a year"), ("70%", "move for economic opportunity")])}
    <h3>Segment choice</h3>
    {table(["Segment", "Share of movers", "Decision"], [["Skilled workers moving for a job (e.g. Berlin, London, SF)", "~70%", "<b>Primary.</b> Largest segment, hard deadlines, high willingness to pay for certainty."], ["International students", "~20%", "Secondary. Visa and housing needs overlap with the core plan."], ["Family and lifestyle moves", "~10%", "Later. Needs vary too much for a v1 plan."]])}

    {h2("03", "User Research")}
    <p>Three questions drove the research: what makes relocation hard, which tasks are time-critical, and how people organise a move today. I ran 4 in-depth interviews to find the pain points, then a survey to size them.</p>
    {SURVEY}
    <p class="caption">Survey responses: tracking tasks, finding trustworthy information and isolation after the move all skewed to the hardest end of the scale.</p>
    <h3>Key insights</h3>
    <div class="notes">
      <div class="note blue"><b>Cognitive Overload</b>Users are drowning in unverified information from scattered sources.</div>
      <div class="note red"><b>The Verification Loop</b>70% of users waste 5+ hours/week cross-referencing data, with no 24/7 way to check what they found.</div>
      <div class="note green"><b>Task Sequencing</b>Users can’t see which tasks block others, which leads to deadlocks.</div>
      <div class="note purple"><b>Asset Management</b>Critical documents (visas, deeds, contracts) are scattered, causing panic before high-stakes appointments.</div>
      <div class="note orange"><b>Social Displacement</b>Beyond logistics, loneliness and the lack of a local network are real costs of moving.</div>
    </div>

    {h2("04", "Competitive Landscape")}
    <p>I reviewed 8 products across four categories: relocation services (Deel, Localyze), productivity tools (Notion, Todoist), community platforms (Reddit, Facebook Groups) and document storage (Google Drive, Dropbox). Each solves one slice; none offers a personal, end-to-end journey.</p>
    {table(["Competitor insight", "Gap for the user", "Opportunity for Settle"], [["Relocation tools are B2B, sold to employers", "Individual movers feel lost", "A personal relocation platform"], ["Task apps are generic", "No relocation context or ordering", "Phase-based task plan"], ["Document tools lack guidance", "Users don’t know what’s required", "“Documents you might need”"], ["Communities are scattered", "Advice is hard to trust", "Location-based discussions in-app"], ["No real-time help", "Users search externally", "Embedded AI assistant"]])}

    {h2("05", "Target User")}
    <div class="persona">
      <div class="id"><img src="assets/settle/persona-photo.avif" alt="Portrait of the persona, Priya Sharma" loading="lazy">
        <dl><dt>NAME :</dt><dd>Priya Sharma, 27</dd><dt>ROLE :</dt><dd>Software Engineer</dd><dt>CONTEXT :</dt><dd>Moving from Bangalore, India → Berlin, Germany for a full-time job</dd><dt>DEVICE :</dt><dd>Mobile-first, expects quick, clear actions</dd></dl></div>
      <div class="traits">
        <div class="trait"><b>Goals</b><ul><li>Complete every relocation task correctly and on time.</li><li>Avoid fines, legal trouble or missed mandatory steps.</li><li>Settle into life in Germany quickly.</li></ul></div>
        <div class="trait"><b>Pain Points</b><ul><li>Doesn’t know what to do first.</li><li>Overwhelmed by unfamiliar bureaucracy and terminology.</li><li>Information is fragmented across blogs, forums and government sites.</li><li>Unsure which documents are critical vs optional.</li></ul></div>
      </div>
    </div>

    {h2("06", "Prioritisation &amp; MVP Scope", "Each MVP feature maps to a validated pain point.")}
    {table(["Feature", "Pain point it solves", "Priority", "Rationale"], [["Personalised, phased task plan", "Task sequencing, cognitive overload", "P0", "The core job: tell the user what to do next, in the right order."], ["Document hub with review", "Asset management", "P0", "Missing documents cause the costliest failures (missed appointments, rejected visas)."], ["AI assistant (Sia)", "The verification loop", "P0", "Directly attacks the 5+ hours/week spent cross-checking information."], ["Community hub", "Social displacement", "P1", "Real need, but the logistics must work first; ships as a lighter v1."]])}
    {label("Priority labels are my ranking of the four MVP features; all four are in the MVP.")}
    <h3>Product requirements</h3>
    <ul>
      <li>Generate a relocation task list with timelines automatically from a short onboarding questionnaire, and let users edit, delete and track tasks.</li>
      <li>Let users upload required documents, review them, and clearly flag anything missing.</li>
      <li>Give users a 24/7 way to clear doubts, reachable from anywhere in the app.</li>
      <li>Build a sense of belonging with local event listings and discussions, so users feel at home before they arrive.</li>
    </ul>

    {h2("07", "Where AI Fits", "Two AI features, each aimed at a measured pain point.")}
    {pillars([("01", "Personalised plan generation", "Answers to a few onboarding questions (origin, destination, move date, purpose) are turned into a tailored, phased roadmap of actionable tasks, instead of a generic checklist."), ("02", "Sia, the AI relocation assistant", "Explains document requirements and bureaucratic terms in plain language, in context, to cut the time users spend verifying information across sites."), ("!", "Guardrails", "Uploaded documents are reviewed and missing items flagged, so users aren’t relying on AI alone for high-stakes, legal steps.")])}

    {h2("08", "The Product")}
    <p>The roadmap is split into phases so users only see the next actionable items, with a secure document hub, a community space and a calendar that keeps them aligned to their move date.</p>
    {img("settle/onboarding.avif", "Onboarding: welcome, account creation and a short questionnaire that generates the plan", "Onboarding: a three-question flow generates the personalised plan.")}
    {img("settle/app-experience.avif", "Core screens: phased task list, create task, documents hub, community, calendar and the AI assistant", "Core MVP: phased tasks, documents, community, calendar and Sia.")}
    {img("settle/journey-40.avif", "The app when the user is 40% through: phase 2 tasks, documents and journey timeline", "Mid-move: progress, outstanding documents and the timeline when a user is 40% through.")}
    <a class="jump" href="https://www.figma.com/proto/tPsz1kYWrE2gMf47X8u1kt/Portfolio?node-id=61-44" target="_blank" rel="noopener"><span>Open the clickable prototype</span>{ARROW_NE}</a>

    {h2("09", "Success Metrics")}
    {label("Proposed metrics for a launch; Settle has not launched.")}
    {table(["Type", "Metric", "Why it matters"], [["North star", "Relocation tasks completed on time per active mover", "Captures the core promise: a move that happens in the right order, on time."], ["Activation", "Plan generated in the first session", "Users only get value once they have their own roadmap."], ["Engagement", "Weekly active movers; documents uploaded per mover", "Shows Settle has become the place the move is managed."], ["Problem metric", "Self-reported hours a week spent verifying information", "Directly tracks the 5+ hours/week pain found in research."], ["Counter-metric", "Questions escalated or answered wrongly by Sia", "Speed must not come at the cost of trust on legal steps."]])}

    {h2("10", "Key Takeaways")}
    <ul>
      <li>Design for the journey, not features. Organising the product around relocation phases mattered more than any single feature, because it answered the user’s real question: what do I do next?</li>
      <li>Quantify the pain before prioritising. The survey turned “relocation is stressful” into a measurable problem (5+ hours a week verifying information) that the AI assistant could be held to.</li>
      <li>Find the gap in the market map. Laying out 8 competitors by category made the opportunity obvious: everyone solved a slice, nobody owned the journey.</li>
      <li>AI needs guardrails in high-stakes flows. For legal and visa steps, AI speeds people up, but review and clear flags keep their trust.</li>
    </ul>
  </div>
</main>
''' + FOOTER

# ------------------------------------------------------------------ TRACKR
trackr = head("TRACKR — Coaching platform for fitness coaches · Saira Garg", "Product case study: TRACKR, a coaching platform taken from coach interviews and a PRD to a working product and beta.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <div class="eyebrow">Product case study · Co-founder · 0 → 1</div>
    <h1>TRACKR | Coaching Platform for Fitness Coaches</h1>
    <p class="lede">A shared place for coaches and clients to plan workouts, log sessions and meals, and follow progress, replacing the spreadsheet, form and chat stack most coaches run today.</p>
    <figure class="cover"><div class="browser"><img src="assets/trackr/product.jpg" alt="TRACKR coach overview with client follow-ups, sessions logged and adherence, next to the client app logging a bench press set"></div></figure>
    {meta([("ROLE", "Co-Founder · Product"), ("TIMELINE", "Aug 2026 – Present"), ("STATUS", "Free early access")])}
    {tldr([("Problem", "Online coaches are capped by admin, not demand: every new client adds hours of formatting plans, chasing check-ins and digging through chats."), ("What I did", "Interviewed 8 coaches, wrote the PRD (positioning, pricing, metrics, launch gates), benchmarked competitors and built the coach web app and client mobile app with AI tools."), ("Outcome", "Live at trackrdaily.com in under 1 month, with 30+ coaches and 7+ gyms in free early access. Next: AI insights across workouts and meals.")])}
    <a class="jump" href="https://trackrdaily.com" target="_blank" rel="noopener"><span>Visit trackrdaily.com</span>{ARROW_NE}</a>

    {stats([("8", "fitness coaches interviewed"), ("&lt;1 mo", "from idea to working product"), ("30+", "coaches in early access"), ("870+", "exercises in the library")])}

    {h2("01", "The Problem")}
    <p>A typical online coach runs their business across four disconnected tools. Nothing connects them, so the coach becomes the integration layer, and that work grows with every client.</p>
    {table(["Job", "Tool today", "Where it fails"], [["Deliver the plan", "Spreadsheet", "Unreadable on a phone mid-set; no logging"], ["Collect check-ins", "Online form", "Responses sit in a sheet nobody opens"], ["Communicate", "Chat app", "Coaching decisions buried in chat history"], ["Track progress", "Manual notes", "No trend view; rebuilt from memory"]])}
    <p class="caption">On the other side, the client can’t reliably answer two questions: what am I doing today, and am I making progress?</p>

    {h2("02", "User Research")}
    <p>I interviewed 8 fitness coaches about how they plan, deliver and review training. The clearest finding: scattered tools cap how many clients a coach can take on. That reframed the product from “an app for coaches” to a measurable goal: raise the number of clients a coach can handle without lowering quality.</p>
    <div class="notes">
      <div class="note sage"><b>No Unified View</b>Coaches react to whoever messages loudest, not whoever needs help most.</div>
      <div class="note slate"><b>Silent Churn</b>A disengaged client stays invisible until they quit.</div>
      <div class="note sage"><b>Two Ways to Get Paid</b>Coaches with clients in India and abroad need both UPI and international payments.</div>
      <div class="note clay"><b>Manual Plan Updates</b>One programming change across a roster costs hours.</div>
      <div class="note plum"><b>No Trend View</b>Progression decisions are made on recall, not data.</div>
      <div class="note gold"><b>Admin Crowds Out Coaching</b>Quality slips once a roster outgrows what one person can track.</div>
    </div>

    {h2("03", "Positioning")}
    <p>Incumbent coaching platforms compete on breadth (payments, video, white-labelling) and mostly price in USD. TRACKR competes on depth in the loop coach and client repeat every day, and on India-first pricing.</p>
    {table(["", "Kahunas", "FITR", "TRACKR"], [["Core pitch", "All-in-one coaching suite", "Business builder for coaches", "Daily training and nutrition loop"], ["Pricing", "Per client, in USD", "Subscription, in USD", "Per active client, in INR (₹300 → ₹100)"], ["AI", "Insights, client triage, AI assistants", "None advertised", "Insights across logged sets and meals (next)"], ["Breadth", "Payments, courses, communities, branded app", "Payments, storefront, branded app", "Deliberately narrow; see scope"]])}
    <p class="caption">Competitor details from their public websites, November 2026.</p>
    {pillars([("01", "Client-side speed", "Open, see today’s session, log, done. Target: today’s workout on screen in under 2 seconds."), ("02", "One coaching workspace", "Plan training, manage clients and review progress in one place; reuse programs across clients."), ("03", "Built for teams from day one", "Every workspace is an org, from one independent coach to a coaching business with several.")])}

    {h2("04", "Scope: What We Said No To")}
    <p>A small team ships by choosing. These were explicitly left out of v1, each with a reason, so the core loop could be excellent.</p>
    {table(["Out of scope for v1", "Why"], [["Sales CRM and discovery calls", "A different buyer moment; TRACKR starts after coach and client agree to work together."], ["Video calling", "Meet and Zoom work fine; no way to differentiate."], ["Open-ended chat inbox", "Rebuilding WhatsApp with fewer features; feedback is tied to sessions instead."], ["White-labelling", "The incumbents’ battleground; expensive and not our edge."]])}

    {h2("05", "The Solution")}
    <p>Write the plan once, and every client gets their own copy.</p>
    {pillars([("Plan", "Program builder", "Exercises, sets, reps and rest; reusable templates and a start date per client."), ("Train", "Client app", "Today’s session first, exercise demos, set-by-set logging and an AI calorie tracker for meals."), ("Review", "Follow-ups and nutrition", "Training history, meal diaries logged by photo or search, and a list of the clients who need attention first.")])}
    <h3>What it replaces</h3>
    <div class="replace">
      <div><s>Copying last week’s spreadsheet for every client</s><i>→</i><span>Assign a program once; each client gets their own copy.</span></div>
      <div><s>Asking “did you train today?” in a chat</s><i>→</i><span>Clients log every set, and the coach sees it the same day.</span></div>
      <div><s>Scrolling threads to find who’s slipping</s><i>→</i><span>A follow-up list puts the clients who need you first.</span></div>
      <div><s>Asking clients to send photos of their meals</s><i>→</i><span>Clients log meals in the app and the coach reviews each diary.</span></div>
    </div>

    {h2("06", "Pricing &amp; Business Model")}
    <p>Coaches already price per client, so TRACKR does too, and it gets cheaper per client as the roster grows. That rewards exactly the behaviour we want: coaches taking on more clients.</p>
    {table(["Roster size", "Price per active client / month"], [["Up to 25 clients", "₹300"], ["Up to 50 clients", "₹200"], ["Up to 100 clients", "₹150"], ["Up to 250 clients", "₹100"], ["250+", "Custom"]])}
    <p class="caption">Free during early access; billed monthly in rupees with GST invoices once billing launches. Only active clients count toward the bill.</p>

    {h2("07", "Success Metrics")}
    <p>North-star metric: <b>weekly logged sessions per active client</b>. It captures both sides: the coach published something worth doing, and the client did it.</p>
    {table(["Layer", "Metric", "How it’s measured"], [["Activation", "Workspace activated", "At least one client logs at least one session"], ["Engagement", "Weekly adherence", "Sessions logged ÷ sessions assigned"], ["Retention", "Coach week-4 retention", "Coach still active in week 4"], ["Leverage", "Clients per coach", "Median, month 3 vs month 1"], ["Performance", "Time to today’s workout", "Under 2 seconds on a cold start"]])}

    {h2("08", "Next: AI Insights", "Scoped from the competitor review. Not live yet.")}
    <p>Once clients log every set and every meal, TRACKR has the data to do the review work for the coach. Kahunas already sells AI triage, so the bar is set. TRACKR’s edge is using set-level workout logs and meal diaries together, not only check-in forms.</p>
    {table(["Insight", "What the coach sees", "Built from"], [["Weekly client summary", "A short note per client on what changed this week", "Sets, sessions and meal diaries"], ["Progression signals", "Lifts that have stalled or are ready to load up", "Set-by-set history"], ["Nutrition flags", "Low-protein days or missed logging, with the pattern behind it", "Meal diaries"], ["Smarter follow-ups", "The follow-up list ranked with a reason for each client", "Adherence, workouts and meals together"]])}
    <p class="caption">Success measure: coach time spent on weekly reviews goes down while adherence holds at 65% or above.</p>

    {h2("09", "Launch Plan", "Each phase has a gate it must pass before the next one starts.")}
    {table(["Phase", "Scope", "Gate to move on"], [["Alpha", "5 design-partner coaches; programs, assignment, logging, history", "5 coaches run real clients for 2 weeks with no spreadsheet"], ["Beta (next)", "25 workspaces; check-ins, feedback, follow-ups, notifications, team directories", "≥65% adherence sustained for 4 weeks; ≥50% coach week-4 retention"], ["General availability", "Bulk import, team analytics, billing", "50 paying workspaces"]])}

    {h2("10", "Building with AI")}
    <p>I own the product and build it with AI coding tools: writing requirements, reviewing flows in the running product, and directing Google’s Antigravity and Claude Code across the coach web app and the client mobile app. That compressed idea-to-working-product into under 1 month.</p>

    {h2("11", "Key Takeaways")}
    <ul>
      <li>Interviews should change the plan. Coach conversations moved the problem from “coaches need an app” to “scattered tools cap client capacity”, which has a measurable outcome.</li>
      <li>Depth beats breadth early on. Saying no to payments, video and chat kept the product small enough to ship and sharp enough to explain.</li>
      <li>Write the metric and the gate before the feature. Adherence and retention targets make it easy to decide what not to build next.</li>
      <li>When building is fast, product judgement is the bottleneck. AI tools shift the hard part to knowing exactly what to ask for and noticing when the result is wrong.</li>
    </ul>
  </div>
</main>
''' + FOOTER

# ------------------------------------------------------------------ MAINSTREET
mainstreet = head("MainStreet — AI-curated local discovery · Saira Garg", "Product case study: MainStreet, an AI-curated, route-aware local discovery app for busy people in Swiss cities.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <div class="eyebrow">Product case study · AI/ML · Two-sided marketplace</div>
    <h1>MainStreet. AI-curated local discovery for busy people in Swiss cities.</h1>
    <p class="lede">A predictive, route-aware discovery feed that replaces the ritual of checking Google Maps for ratings, Instagram for vibe, TikTok for food and friends for a sanity check.</p>
    <div class="grid4 cover4"><img src="assets/mainstreet/hifi-new-1.jpeg" alt="Discovery screen with a map and match scores"><img src="assets/mainstreet/hifi-new-2.jpeg" alt="Pattern detected on a repeated route"><img src="assets/mainstreet/hifi-new-4.jpeg" alt="Single location menu with learned routes"><img src="assets/mainstreet/hifi-new-5.jpeg" alt="List view of top matches nearby"></div>
    {meta([("ROLE", "Product Manager · Personal project"), ("MARKET", "Zürich, Geneva and similar cities"), ("PLATFORM", "iOS · Android")])}
    {tldr([("Problem", "Finding a good local spot takes four apps and still often ends in a mediocre experience, while independent businesses can’t reach the people walking past them."), ("What I did", "Defined the problem, users and scope, designed an AI matching model around daily routes, tested 3 concepts quickly with AI prototyping tools, and set success metrics and an experiment plan."), ("Outcome", "A mobile MVP concept with route-aware AI recommendations, separate flows for users and businesses, and a plan to test it.")])}

    {h2("01", "Why I Built This")}
    <div class="origin">My sister recently moved to Zürich. When she told me how hard it was to find places that actually suited her in a new city, hopping between four apps and still ending up somewhere average, I came forward with this idea: an app that learns the routes you already take and curates local spots along them.</div>

    {h2("02", "The Problem")}
    {pillars([("U", "For users", "People bounce between Google Maps for ratings, Instagram for the vibe, TikTok for the food and friends for recommendations, and still end up at places that don’t match what they want."), ("B", "For local businesses", "Independent owners struggle to reach their ideal customers and rarely connect with the audience they were built for."), ("?", "The gap", "Generic review platforms rank by average stars, not by fit for this person, at this moment, on this route.")])}

    {h2("03", "Target Users")}
    <div class="grid3">
      <div class="pillar"><b>WHO</b>Young professionals, expats and students aged 22–36 in urban Swiss areas such as Zürich and Geneva.</div>
      <div class="pillar"><b>WHAT THEY VALUE</b>Supporting local, independent businesses over chains; specific tastes such as vegan food, specialty coffee or vintage fashion.</div>
      <div class="pillar"><b>CORE PAIN</b>Limited free time. They hate losing a weekend meal to a place a generic platform rated 4.5 stars, and won’t spend an hour researching.</div>
    </div>

    {h2("04", "Product Hypothesis")}
    <div class="origin">If MainStreet learns where users already go and what they like, it can surface one place that fits along their route faster and more reliably than four apps, and give local businesses a direct line to the people walking past their door.</div>
    {label("Monetisation to test: businesses already join through their own onboarding flow, so a paid visibility tier for local businesses is the first pricing hypothesis.")}

    {h2("05", "Scope Decisions")}
    {table(["Decision", "In / out", "Reasoning"], [["Native mobile apps (iOS &amp; Android)", "In", "The value depends on live location and passive route learning."], ["Web app", "Out", "No live location or route learning; a phone in hand is the real context of use."], ["Separate user and business onboarding", "In", "Both sides of the marketplace need to be onboarded from day one."], ["Pre-permission location screen", "In", "Route learning needs location access, so the value exchange is explained before the OS prompt to protect opt-in rates."]])}

    {h2("06", "How the AI Works", "Ranking places by fit for this person, on this route, right now.")}
    {pillars([("in", "Signals", "Taste picks from onboarding, current location, repeated routes, implicit feedback (taps, saves, visits) and explicit feedback (ratings, “not my vibe”)."), ("ml", "Model output", "A per-user match score (e.g. “95% Match”), walk time, and short vibe tags such as “Cozy · Fine dine” that explain why a place was picked."), ("↻", "Route detection", "After repeated trips, e.g. Wiedikon → Zürich HB, the app detects the pattern and curates matches along that path without the user configuring anything.")], 'pillars')}
    <p>Trust is a product requirement, not a nice-to-have: the “Pattern detected” banner appears once, then the app curates quietly. A utility that gets noisy about tracking loses users.</p>

    {h2("07", "Testing Concepts Fast with AI Tools")}
    <p>Instead of weeks of manual mock-ups, I generated three concepts with AI prototyping tools in days, then used their gaps to make the key product calls.</p>
    {table(["Tool tested", "What it showed", "Decision it led to"], [["Lovable", "Match scores alongside the map work; splitting Home and Map into two tabs adds friction", "One map-first home screen, no separate map tab"], ["Figma Make", "No list to browse suggestions and no signal of where the search is happening", "Always show location context; add a list alternative"], ["Google Stitch", "One question per onboarding screen keeps effort low; no way to apply or see learned routes", "Single-question onboarding; one menu for current location and learned routes"]])}

    {h2("08", "The Product")}
    <div class="grid4 cover4">
      <figure><img src="assets/mainstreet/hifi-new-1.jpeg" alt="Discovery near current location" loading="lazy"><figcaption>Discover nearby, with quick filters</figcaption></figure>
      <figure><img src="assets/mainstreet/hifi-new-2.jpeg" alt="Pattern detected on a new route" loading="lazy"><figcaption>Route pattern detected</figcaption></figure>
      <figure><img src="assets/mainstreet/hifi-new-3.jpeg" alt="Learned commute with no banner" loading="lazy"><figcaption>Learned commute, quiet curation</figcaption></figure>
      <figure><img src="assets/mainstreet/hifi-new-4.jpeg" alt="Single location menu" loading="lazy"><figcaption>One menu for location and routes</figcaption></figure>
    </div>

    {h2("09", "Experiment Plan", "Does knowing your route beat knowing where you are?")}
    {label("Planned experiment; not yet run.")}
    {table(["", "Variant A: route-aware", "Variant B: nearby-only"], [["Idea", "Recommend spots along the routes the user already takes", "Recommend spots near the user’s current location, as map apps do"], ["Hypothesis", "Picks that fit the day’s path convert better", "Proximity alone is enough (the null: no edge for MainStreet)"], ["Primary metric", "Feed conversion rate", "Feed conversion rate"], ["Guardrail", "Time-to-value", "Time-to-value"]])}
    <p class="caption">This is the test that decides whether the product has an edge: if route-awareness doesn’t win, MainStreet is just another map.</p>

    {h2("10", "Success Metrics")}
    {table(["Metric", "Definition", "Why"], [["Time-to-value (TTV)", "Time from install to the first saved or visited place", "Proves the app delivers before users give up"], ["Feed conversion rate (FCR)", "Share of feed sessions that lead to directions, a save or a visit", "The core test of recommendation quality"], ["Implicit feedback", "Taps, saves, dwell and visits per user", "Trains the model and shows real interest"], ["Explicit feedback", "Ratings and “not my vibe” dismissals", "Fast correction signal for bad matches"], ["Weekly active users (WAU)", "Users opening the app at least once a week", "Habit: MainStreet becomes the default way to choose"]])}

    {h2("11", "Key Product Decisions")}
    {why([("One control for “where”", "Current location, learned routes and route editing live in one top-left menu. Where the app looks is always one tap away, and the feed stays focused on what is there."), ("Show the pattern once", "The route banner appears only on first detection. Proving the intelligence once builds trust; repeating it erodes it."), ("Lead with “why this is for me”", "Cards open with the match percentage and vibe tags before distance, because fit is the reason to trust a recommendation."), ("Two sides from day one", "Businesses get their own onboarding (“Reach commuters near my door”) so supply grows alongside demand.")])}

    {h2("12", "Next Steps")}
    <ul>
      <li>Usability-test the MVP with expats and students in Zürich, starting with people like my sister who moved recently.</li>
      <li>Run the route-aware vs nearby-only experiment to test the core hypothesis on feed conversion.</li>
      <li>Onboard independent businesses in one neighbourhood to test the business side and the paid visibility hypothesis.</li>
    </ul>

    <a class="next" href="video-to-article.html"><div><span>NEXT</span><b>YouTube Video-to-Article AI</b></div>{ARROW_L}</a>
  </div>
</main>
''' + FOOTER

# ------------------------------------------------------------------ VIDEO-TO-ARTICLE
video = head("YouTube Video-to-Article AI · Saira Garg", "AI project: a multimodal pipeline that turns any YouTube video into a skimmable, screenshot-rich article, processing 2-hour videos in under 5 minutes.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <div class="eyebrow">AI project · Generative AI · Multimodal LLMs</div>
    <h1>YouTube Video-to-Article AI</h1>
    <p class="lede">A tool that turns any YouTube video into a skimmable article, with screenshots placed next to the words that explain them. Built for Andrej Karpathy’s LLM Challenge.</p>
    <div class="shots3" id="examples">
      <figure><a href="https://github.com/lordgavy01/Karpathy-LLM-Challenge/blob/main/Sample%20Outputs/Nana%20Hats%20Pitch%20on%20Shark%20Tank.pdf" target="_blank" rel="noopener"><img src="assets/video-article/shark-tank.jpg" alt="Generated article: a deep dive into the Nana Hats pitch on Shark Tank, with a table of contents and an on-stage screenshot"></a><figcaption>SHARK TANK PITCH</figcaption></figure>
      <figure><a href="https://github.com/lordgavy01/Karpathy-LLM-Challenge/blob/main/Sample%20Outputs/NBA%20Lakers%20vs.%20Pelicans.pdf" target="_blank" rel="noopener"><img src="assets/video-article/nba.jpg" alt="Generated article: Lakers vs Pelicans in the NBA Play-In Tournament, with an aerial screenshot of the arena" loading="lazy"></a><figcaption>NBA GAME</figcaption></figure>
      <figure><a href="https://github.com/lordgavy01/Karpathy-LLM-Challenge/blob/main/Sample%20Outputs/Man%20vs%20Wild%20Episode.pdf" target="_blank" rel="noopener"><img src="assets/video-article/man-vs-wild.jpg" alt="Generated article: a visual journey through a survival documentary, with a screenshot of a climber on a cliff" loading="lazy"></a><figcaption>SURVIVAL DOCUMENTARY</figcaption></figure>
    </div>
    <p class="caption">First pages of three generated articles. Each was written and illustrated by the pipeline from the video alone. Click one to open the full article.</p>
    {meta([("ROLE", "Built end to end"), ("CONTEXT", "Andrej Karpathy’s LLM Challenge"), ("STACK", "Python · OpenAI · Streamlit")])}
    {tldr([("Problem", "Long videos are hard to skim, search or quote. A transcript alone loses the slides, code and scenes that carry half the meaning."), ("What I did", "Designed and built a pipeline that transcribes the video, picks the frames that matter, describes them with a vision model and writes an illustrated article."), ("Outcome", "2-hour videos become finished, screenshot-rich articles in under 5 minutes, tested on sports, TV, chess and documentary footage.")])}
    <a class="jump" href="https://github.com/lordgavy01/Karpathy-LLM-Challenge" target="_blank" rel="noopener"><span>View the code on GitHub</span>{ARROW_NE}</a>

    {stats([("2 hr", "of video in"), ("&lt;5 min", "to a finished article"), ("&lt;1 min", "gap between text and its visual"), ("5", "video genres tested")])}

    {h2("01", "The Problem")}
    <p>In early 2024 Andrej Karpathy challenged builders to turn his 2-hour lecture into a book chapter automatically: readable text, with the right screenshots in the right places. Video is linear. You can’t skim it, search it or pick up where an idea starts, and the transcript misses whatever was shown on screen.</p>
    <p>The bar was an article a person would actually choose to read instead of watching, produced fast enough to be worth it.</p>

    {h2("02", "How It Works", "Four stages, from raw video to a finished article.")}
    {table(["Stage", "What happens", "Model or method"], [["Listen", "The video is split into 5-minute chunks, each transcribed at the same time, then stitched back with corrected timestamps.", "OpenAI Whisper"], ["Look", "A frame is sampled every 5 seconds and near-duplicates are dropped, so only frames that show something new survive.", "SSIM image similarity"], ["Understand", "Each kept frame is described using the transcript of the same section, so the description matches what is being said. Code on screen is written out.", "GPT-4 Vision"], ["Write", "Transcript and frame notes become one article with a title, table of contents, headings and screenshots in place.", "GPT-4 Turbo"]])}

    {h2("03", "Key Trade-offs")}
    {why([("Fewer frames, lower cost", "Every frame sent to the vision model costs time and money. Dropping frames that look almost the same as the last one (similarity above 0.9) removes most of a talking-head video before any model call."), ("Chunk for speed", "Transcribing one long file is slow. Splitting into 5-minute chunks and processing them in parallel is what gets a 2-hour video under 5 minutes."), ("Context in, accuracy out", "A screenshot on its own is ambiguous. Giving the vision model the transcript from the same moment keeps each caption tied to what the speaker is explaining."), ("Simple beats clever", "I also tried ranking frames by sharpness and contrast. It failed on shorter videos, so I shipped the similarity filter alone.")])}

    {h2("04", "What I’d Do Next")}
    <ul>
      <li>Cut the cost per video further by sending only the most informative frame from each section to the vision model.</li>
      <li>Run more model calls in parallel to bring long videos down further.</li>
      <li>Test open-source models in place of GPT and compare article quality against cost.</li>
    </ul>

    {h2("05", "Key Takeaways")}
    <ul>
      <li>In an AI product, the cheapest model call is the one you don’t make. Filtering the input mattered more than tuning the prompt.</li>
      <li>Multimodal output is only as good as its alignment. Text and image have to describe the same moment, or the article falls apart.</li>
      <li>Test outside the brief. Running it on sports, TV and documentaries, not just lectures, showed it worked for any video.</li>
    </ul>

    <a class="next" href="settle.html"><div><span>NEXT</span><b>Settle — Relocation &amp; travel planner</b></div>{ARROW_L}</a>
  </div>
</main>
''' + FOOTER

# ------------------------------------------------------------------ ABOUT
def xp(when, org, role, text):
    return f'<div class="xp"><div class="when">{when}</div><div><h3>{org}<span>{role}</span></h3><p>{text}</p></div></div>'
def chips(label, items):
    return f'<div class="skillrow"><div class="when">{label}</div><div class="chips">' + ''.join(f'<span>{i}</span>' for i in items) + '</div></div>'

about = head("About — Saira Garg", "About Saira Garg — co-founder of TRACKR, software engineer at Cisco, and founder of a 100+ member run club.") + nav('about') + f'''
<main>
  <section class="about-top">
    <div class="portrait"><img src="assets/saira-portrait.jpg" alt="Saira Garg standing in a garden, smiling"></div>
    <div>
      <h1>Hey, I’m Saira!</h1>
      <p>A product manager who loves turning messy problems into simple products. I start with the people who have the problem, write down what would actually help, and then build it.</p>
      <p>Right now I’m co-founding TRACKR, a platform for fitness coaches and their clients, while working as a Software Engineer at Cisco on cloud management for campus switches.</p>
      <p>Outside work, I run. I started a run club in Bathinda that has grown to 100+ members.</p>
    </div>
  </section>

  <section class="approach">
    <div class="wrap">
      <h2>My Approach</h2>
      <div class="split">80% Problem Solver<br>10% Builder - 10% Runner</div>
      <p>I don’t think of myself as just an engineer or just a product person; I’m a problem solver with a versatile toolkit. I talk to users, size the market, write the PRD, prioritise hard, and work with engineering to ship, measure and iterate. With AI tools I can also build and test ideas myself. Wearing several hats lets me look at a problem from every angle and bring value to both the business and the user.</p>
    </div>
  </section>

  <section class="about-block" id="experience">
    <h2>Experience</h2>
    {xp("Aug 2026 – Present", "TRACKR", "Co-Founder", "Co-founded a platform where fitness coaches plan workouts, assign them to clients and review training and meal diaries. Interviewed 8 coaches, wrote the PRD covering positioning, pricing and success metrics, and built the coach web app and client mobile app with AI tools in under 1 month. Now in free early access with 30+ coaches, and scoping AI insights across workouts and meals.")}
    {xp("Jul 2026 – Present", "Cisco", "Software Engineer", "Building cloud management for Cisco campus switches with cross-functional teams, so enterprise customers can onboard, monitor and automate switches from the Meraki Dashboard.")}
    {xp("May – Jul 2025, Jan – Jun 2026", "Cisco", "Software Engineering Intern", "Took a pre-release contact-center (UCCE) routing feature from specs to launch with engineering, validation and UX, letting live calls query external systems at 1,000 queries per second. Cut processing latency 12%, prioritised the backlog and presented progress and risks to leadership. Earlier, moved a legacy diagnostics tool into the CCE Admin console across 20+ views with 88%+ test coverage.")}
    {xp("Jan 2025 – Apr 2025", "Snapdeal", "Software Engineering Intern", "Built in-house seller advertising tools with product and marketing teams, replacing third-party software and saving up to ₹50 Lakhs a month.")}
  </section>

  <section class="about-block">
    <h2>More Projects</h2>
    {xp("AI/ML", "NutriScan", "AI Dietitian", "Built an AI calorie and macro tracker that reads food labels from a photo with Google Gemini’s image model, reaching 92% accuracy and removing manual data entry. <a class=\"t\" href=\"https://github.com/SAIRAGARG/NutriScan\" target=\"_blank\" rel=\"noopener\">GitHub →</a>")}
  </section>

  <section class="about-block">
    <h2>Leadership &amp; Achievements</h2>
    {xp("Founder", "Run Club, Bathinda", "100+ members", "Started a local running community from zero, organising bi-weekly group runs.")}
    {xp("2024", "Myntra HackerRamp WeForShe", "Shared Carts", "Designed, prototyped and presented a social shopping feature that lets friends build and check out one cart together.")}
    {xp("2025 – 26", "PECFEST", "Head of Publicity", "Led a 100-person team working with design, sponsorship and tech to run the campaigns for the college’s annual fest.")}
    {xp("2022 – 2026", "Punjab Engineering College", "B.Tech, Computer Science", "Chandigarh, India. CGPA 8.0. AWS AI Scholarship recipient (AI Programming Nanodegree).")}
  </section>

  <section class="about-block">
    <h2>Skills</h2>
    {chips("Product", ["Product Strategy", "User Research", "Market Sizing", "PRDs", "Roadmapping", "Prioritization", "Competitive Analysis", "Go-to-Market", "Agile / Scrum"])}
    {chips("Data &amp; Business", ["Data Analysis", "SQL", "KPIs &amp; North-Star Metrics", "A/B Testing", "Business Case", "Pricing Models"])}
    {chips("AI / ML", ["LLM Applications", "Multimodal Pipelines", "Prompt Engineering", "Ranking &amp; Recommendation", "Gemini API", "Google Antigravity", "Claude Code"])}
    {chips("Technical", ["Java", "Python", "JavaScript", "C++", "React", "Node.js", "Spring Boot", "REST APIs", "Git"])}
    {chips("Design", ["Figma", "AI Prototyping"])}
  </section>
</main>
''' + FOOTER

for name, html in [("index.html", home), ("settle.html", settle), ("trackr.html", trackr), ("mainstreet.html", mainstreet), ("video-to-article.html", video), ("about.html", about)]:
    with open(os.path.join(OUT, name), "w") as f: f.write(html)
    print(name, len(html))
