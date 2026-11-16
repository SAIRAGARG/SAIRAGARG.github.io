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
  <p>focused on turning user research into simple products people actually use, from first interview to launch</p>
</section>

<main>
  <section class="wrap" id="work">
    <h2 class="section-title">Projects &amp; Case studies</h2>
    <p class="section-sub">A glimpse of my recent work</p>
    <div class="cards">
{card("TRACKR : Fitness Coaching Platform", "A shared place for coaches and clients to plan workouts, record sessions and follow progress. Co-founded and built with AI tools, from idea to working product in under 3 months.", "trackr.html", "Live Product", "https://trackrdaily.com", "assets/trackr/product.jpg", "the TRACKR case study", "trackr", True)}
    <article class="card">
      <div class="card-body">
        <h3>MainStreet : AI Local Discovery</h3>
        <p>A journey-based discovery feed that learns your daily routes and surfaces local spots that match your vibe. It began with my sister’s move to Zürich.</p>
        <div class="card-actions">
          <a class="round" href="mainstreet.html" aria-label="Open the MainStreet case study">{ARROW_NE}</a>
          <a class="pill" href="mainstreet.html">Case Study</a>
        </div>
      </div>
      <a class="card-media ms" href="mainstreet.html" tabindex="-1" aria-hidden="true"><img src="assets/mainstreet/hifi-new-1.jpeg" alt=""><img src="assets/mainstreet/hifi-new-2.jpeg" alt=""></a>
    </article>
{card("Settle : Relocation &amp; Travel Planner", "Settle is a personal relocation assistant that turns the chaos of moving to a new country into a clear, guided, and manageable process", "settle.html", "Case Study", "settle.html", "assets/home/settle-card.jpg", "the Settle case study")}
    </div>
  </section>

  <section class="lower">
    <div class="wrap">
      <h2 class="section-title">Where I’ve Worked &amp; Led</h2>
      <div class="tiles">
{tile("Cisco", "Jul 2026 – Present", "Software Engineer", "Building cloud management for campus switches on the Meraki Dashboard.")}
{tile("Snapdeal", "Jan – Apr 2025", "Software Engineering Intern", "Built in-house seller advertising tools with the product and marketing teams.")}
{tile("70+", "Founder", "Run Club, Bathinda", "Started a community run club and grew it through outreach and group runs.")}
{tile("Finalist", "Myntra HackerRamp 2024", "Shared Carts", "A social shopping feature that lets friends build and shop one cart together.")}
      </div>
    </div>
  </section>
</main>
''' + FOOTER

# ------------------------------------------------------------------ SETTLE
def fig(src, alt, cls='', cap=''):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="{cls}"><img src="assets/settle/{src}" alt="{alt}" loading="lazy">{c}</figure>'

settle = head("Settle — Relocation & Travel Partner · Saira Garg", "Case study: Settle, a personal relocation assistant that turns the chaos of moving to a new country into a clear, guided process.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <h1>Settle | Relocation &amp; Travel Partner</h1>
    <p class="lede">A personal relocation assistant that turns the chaos of moving to a new country into a clear, guided, and manageable process.</p>
    <figure class="cover sharp"><img width="2280" height="1400" src="assets/settle/hero.avif" alt="Settle app screens: sign-up, relocation task plan, documents, community and AI assistant"></figure>

    <h2>Project Overview</h2>
    <p>Problem: International relocation is rarely a seamless transition. It is a complex web of hundreds of fragmented tasks.</p>
    <p>Role: To address this, I led an 8-week end-to-end design sprint to create Settle, a mobile relocation partner. Grounded in comprehensive user research, the app bridges the gap between travel and residency, organizing the chaos of moving into a clear, manageable roadmap that prioritizes users peace of mind.</p>
    <a class="jump" href="#hifi"><span>Jump to hi-fi designs</span>{ARROW_D}</a>

    <h2>Relocation Market</h2>
    <p>Migration is no longer a niche event; it is a global mega trend. According to the 2024 UN World Migration Report, there are approximately 281 million international migrants globally. This number has doubled since 1990 <a class="t" href="https://worldmigrationreport.iom.int/" target="_blank" rel="noopener">[source]</a>. The Organisation for Economic Co-operation and Development reports that over 6 million people <a class="t" href="https://www.oecd.org/en/topics/migration.html" target="_blank" rel="noopener">[source]</a> move permanently to developed countries every year. This excludes the millions of students and temporary "Digital Nomads". People move due to variety of reasons:</p>
    <ul>
      <li>70% Economic Opportunity: Skilled workers moving for higher wages in example tech hubs (Berlin, London, SF).</li>
      <li>20% Education: International students who need visa/housing support before they even graduate.</li>
      <li>10% Family/Lifestyle: Joining a partner or seeking a better quality of life.</li>
    </ul>

    <h2>User Research</h2>
    <p>Our comprehensive research phase was driven by three key objectives: understand relocation challenges, Identify time-sensitive tasks, and learn how people currently organize moves.</p>
    <h3>Qualitative Research</h3>
    <p>We conducted 4 user interviews to learn about users’ pain points and preferences and understand their needs and expectations.</p>
    <h3>Quantitative Research</h3>
    <div class="survey" role="img" aria-label="Survey results, number of people per difficulty rating from 1 to 5, for four questions"><div class="chart"><h4>How challenging was it to manage and keep track of relocation-related tasks?</h4><div class="plot"><div class="bars"><i data-v="0" style="height:0.0%"></i><i data-v="18" style="height:50.0%"></i><i data-v="8" style="height:22.2%"></i><i data-v="34" style="height:94.4%"></i><i data-v="20" style="height:55.6%"></i></div><div class="x"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></div><small>Increasing order of difficulty →</small></div><div class="chart"><h4>How challenging was it to find reliable and trustworthy information?</h4><div class="plot"><div class="bars"><i data-v="0" style="height:0.0%"></i><i data-v="8" style="height:25.0%"></i><i data-v="22" style="height:68.8%"></i><i data-v="28" style="height:87.5%"></i><i data-v="22" style="height:68.8%"></i></div><div class="x"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></div><small>Increasing order of difficulty →</small></div><div class="chart"><h4>To what extent did you feel lonely or isolated after the move?</h4><div class="plot"><div class="bars"><i data-v="0" style="height:0.0%"></i><i data-v="2" style="height:4.8%"></i><i data-v="10" style="height:23.8%"></i><i data-v="30" style="height:71.4%"></i><i data-v="38" style="height:90.5%"></i></div><div class="x"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></div><small>Increasing order of difficulty →</small></div><div class="chart"><h4>How stressful did you find the overall relocation process?</h4><div class="plot"><div class="bars"><i data-v="2" style="height:6.2%"></i><i data-v="4" style="height:12.5%"></i><i data-v="16" style="height:50.0%"></i><i data-v="18" style="height:56.2%"></i><i data-v="30" style="height:93.8%"></i></div><div class="x"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></div><small>Increasing order of difficulty →</small></div></div>
    <p class="caption">A survey was created to gather insights into users’ preferences on feature prioritization to find the common segment and validate our hypothesis.</p>

    <h2>Competitive Analysis</h2>
    <p>A competitive analysis revealed that existing solutions focus on isolated problems — such as task management, document storage, or relocation services — but fail to offer a unified, user-centric journey.</p>
    <div class="boxes">
      <div class="box"><b>Relocation Services</b><ul><li>Deel</li><li>Localyze</li></ul></div>
      <div class="box"><b>Productivity Tools</b><ul><li>Notion</li><li>Todoist</li></ul></div>
      <div class="box"><b>Community Platforms</b><ul><li>Reddit</li><li>Facebook Groups</li></ul></div>
      <div class="box"><b>Document Storage</b><ul><li>Google Drive</li><li>Dropbox</li></ul></div>
    </div>
    <p>A comparison of relocation, productivity, and support platforms</p>
    <table class="table">
      <thead><tr><th>Competitor insight</th><th>UX Gap Identified</th><th>Opportunity</th></tr></thead>
      <tbody>
        <tr><td>Relocation tools are B2B focused</td><td>Individual users feel lost</td><td>Create a personal relocation platform</td></tr>
        <tr><td>Task apps are generic</td><td>No relocation context</td><td>Phase based task structure</td></tr>
        <tr><td>Document tools lack guidance</td><td>Users don’t know what’s required</td><td>“Documents you might need” section</td></tr>
        <tr><td>Communities are scattered</td><td>Advice is hard to trust</td><td>In-app, location based discussions</td></tr>
        <tr><td>No real time help</td><td>Users search externally</td><td>Embedded AI assistant</td></tr>
      </tbody>
    </table>

    <h2>Key Insights &amp; Opportunity Areas</h2>
    <div class="notes">
      <div class="note blue"><b>Cognitive Overload</b>Users are drowning in unverified information from scattered sources</div>
      <div class="note red"><b>The Verification Loop</b>70% of users waste 5+ hours/week cross-referencing data, lacking a 24/7 support system to validate their findings.</div>
      <div class="note green"><b>Task Sequencing</b>Users fail to identify which tasks block others (e.g., "I need a bank account to rent, but an address to bank"), leading to operational deadlocks.</div>
      <div class="note purple"><b>Asset Management</b>Critical documents (Visas, Deeds, Contracts) are often disorganized, causing panic during high-stakes appointments.</div>
      <div class="note orange"><b>Social Displacement</b>Beyond logistics, users struggle with the "soft" challenges of relocation: loneliness and the lack of a local support network.</div>
    </div>

    <h2>The Solution</h2>
    <p>While brainstorming the best approach for the project, I empathised with the user's problems and made conceptions based on research and available data upon which I implemented the designs.</p>
    <p>Listed below are some major product requirements that I considered the most important to drive the overall user experience.</p>
    <ul>
      <li>Automatically generate a comprehensive relocation task list with clear timelines, allowing users to fully manage their journey by editing, deleting, or tracking progress in real-time.</li>
      <li>Add a feature that allows users to upload the required documents. The documents should be reviewed internally by us and anything missing should be clearly flagged.</li>
      <li>Add a support system where users can clear any doubt 24 X 7. The user journey to reach out to the support should be intuitive.</li>
      <li>Foster a sense of belonging by integrating community features, such as local event listings and discussion hubs, to help users feel 'at home' even before they arrive.</li>
    </ul>

    <h2>User Persona : Primary user</h2>
    <div class="persona">
      <div class="id"><img src="assets/settle/persona-photo.avif" alt="Portrait of the persona, Priya Sharma" loading="lazy">
        <dl><dt>NAME :</dt><dd>Priya Sharma</dd><dt>AGE :</dt><dd>27</dd><dt>ROLE :</dt><dd>Software Engineer</dd><dt>CONTEXT :</dt><dd>Moving from Bangalore, India → Berlin, Germany for a full-time job</dd><dt>DEVICE BEHAVIOUR :</dt><dd>Mobile-first, expects quick, clear actions</dd></dl></div>
      <div class="traits">
        <div class="trait"><b>Behaviours</b><ul><li>Researches heavily but gets overwhelmed quickly.</li><li>Saves links, screenshots, and PDFs across devices.</li><li>Relies on WhatsApp groups / Reddit / friends for reassurance.</li><li>Checks tasks multiple times due to fear of mistakes.</li></ul></div>
        <div class="trait"><b>Feelings</b><ul><li>Excited about career growth and living abroad.</li><li>Anxious, uncertain, mentally overloaded.</li><li>Wants reassurance that she’s “doing things right”.</li></ul></div>
        <div class="trait"><b>Goals</b><ul><li>Complete all relocation tasks correctly and on time.</li><li>Avoid fines, legal trouble, or missing mandatory steps.</li><li>Feel in control instead of anxious during the move.</li><li>Settle into life in Germany as quickly as possible.</li></ul></div>
        <div class="trait"><b>Pain Points</b><ul><li>Doesn’t know what to do first.</li><li>Overwhelmed by German bureaucracy &amp; unfamiliar terminology.</li><li>Information is fragmented across blogs, expat forums, and government sites</li><li>Afraid of missing time-sensitive legal steps.</li><li>Unsure which documents are critical vs optional.</li></ul></div>
      </div>
    </div>

    <h2>Information Architecture</h2>
    <p>The information architecture is designed to reduce cognitive overload by organizing relocation tasks into clear phases, while supporting users with documents, community knowledge, and contextual AI assistance.</p>
    {fig("ia.avif", "Settle sitemap: Onboarding, Home, Documents, Overflow Menu, Community, Calendar and AI Assistant with their sub-screens")}

    <h2>Design &amp; Prototyping</h2>
    <h3>Lo-Fi Ideation</h3>
    <p>The lo-fi ideation phase for Settle focused on defining a core structure that reduces cognitive load during the stressful relocation process. By mapping out a 'milestone-based' architecture, I visualized how to break down a complex international move into manageable, bite-sized steps before moving into high-fidelity details</p>
    {fig("lofi-ideation.avif", "Ideation board: reference imagery, grey-box wireframes, logo sketches and paper sketches of the main screens", "sharp")}
    <h3>Lo-Fi Designs</h3>
    {fig("lofi-designs.avif", "Low-fidelity wireframes and annotated paper sketches of onboarding, tasks, documents and community screens", "sharp")}
    <h3>Mood-board</h3>
    <div class="mood"><img src="assets/settle/moodboard.avif" alt="Mood-board collage of moving boxes, a house mark, a map pin, a visa form and greens" loading="lazy"><p>I chose a cohesive palette of ombre and layered greens—ranging from deep forest to light sage—to transform the high-stress, "red-alert" chaos of relocation into a guided journey of growth and stability. By blending these tones, the UI moves away from the clinical feel of a standard checklist and instead mimics the natural transition of "planting roots" in a new home.</p></div>

    <h2 id="hifi">Design System &amp; Hi-Fi Designs</h2>
    {fig("hifi.avif", "Design system: colour palette of layered greens, SF Pro typography, an eight-step grey scale, and the component library of buttons, inputs, cards, chips, menus and navigation", "sharp")}

    <h3 class="band-title">Easy Onboarding</h3>
    <p>The sign-up process is frictionless, allowing entry via email or phone. Immediately after, users complete a targeted questionnaire to capture essential move details. This input is instantly processed to generate a personalized relocation roadmap, converting all the requirements into a tailored set of actionable tasks.</p>
    {fig("onboarding.avif", "Onboarding flow: welcome screen, account creation, and a short questionnaire about location, move date and purpose")}

    <h3 class="band-title">The App Experience</h3>
    <p>To prevent cognitive overload, the roadmap is divided into logical phases. Users see only immediate, actionable items rather than a daunting long list, while retaining the flexibility to add or edit tasks. We also have a dedicated, encrypted hub that allows users to upload, review, and store sensitive paperwork, ensuring critical documents are always accessible. Additionally, we addressed social isolation through a Community Hub—a space to connect with peers. Finally, an integrated Calendar visualizes the timeline, keeping users aligned with their move date.</p>
    {fig("app-experience.avif", "Six core screens: phased task list, create new task, documents hub, community, empty calendar and the Sia AI assistant")}

    <h3 class="band-title">The UX through the journey</h3>
    <p>To prevent cognitive overload, the roadmap is divided into logical phases. Users see only immediate, actionable items rather than a daunting long list, while retaining the flexibility to add or edit tasks. We also have a dedicated, encrypted hub allows users to upload, review, and store sensitive paperwork, ensuring critical documents are always accessible. Additionally, we addressed social isolation through a Community Hub—a space to connect with peers. Finally, an integrated Calendar visualizes the timeline, keeping users aligned with their move date.</p>
    {fig("journey-40.avif", "App experience when the user is 40% through: phase 2 tasks, uploaded and pending documents, and the journey timeline")}

    <h3 class="band-title">Feedback &amp; Error states</h3>
    {fig("feedback.avif", "Profile, offline status, loading state and error state screens")}

    <h2>Accessibility Considerations</h2>
    <div class="a11y">
      <div><h4>Cognitive &amp; Visual Accessibility</h4><div class="panel">
        <p><em>Contrast &amp; Color:</em> The primary brand palette maintains a contrast ratio of 3.7:1. This specifically meets WCAG standards for large text and graphical components, ensuring key UI elements remain legible.</p>
        <p><em>Readability:</em> Used high-legibility sans-serif fonts with generous line spacing to prevent "visual noise" during high-stress relocation tasks.</p></div></div>
      <div><h4>Interactive &amp; Motor Accessibility</h4><div class="panel">
        <p><em>Touch Targets:</em> All interactive elements (buttons, checkboxes, and tabs) maintain a minimum size of 44x44 dp for easy tapping while on the move.</p>
        <p><em>Error Recovery:</em> Error states provide explicit instructions on how to fix issues, reducing frustration for users with motor or cognitive impairments.</p></div></div>
      <div><h4>Assistive Technology (Screen Readers)</h4><div class="panel">
        <p><em>Semantic Hierarchy:</em> Organized the app's hierarchy with clear headings so screen readers can easily phrase the relocation roadmap by milestones.</p>
        <p><em>Live Regions:</em> Progress bars and document icons include descriptive labels (e.g., "Relocation 40% Complete") to provide context to visually impaired users beyond just the visual graphics.</p></div></div>
      <div><h4>Linguistic &amp; Inclusive Design</h4><div class="panel">
        <p><em>Plain Language:</em> Translated complex legal and bureaucratic terms into simple, actionable language to support non-native speakers and users under high stress.</p>
        <p><em>Contextual Help:</em> Integrated an AI assistant (Sia) to provide immediate, simplified explanations for difficult document requirements, ensuring the app is accessible to all digital literacy levels.</p></div></div>
    </div>

    <h2>Prototypes</h2>
    <div class="protos">
      <img src="assets/settle/proto-tasks.jpg" alt="Settle home screen with the phased relocation task list" loading="lazy">
      <div class="bubbles"><div class="bubble l">Settle: Reimagining the International Relocation Experience.</div><div class="bubble r">UX for Momentum: Visualizing the "Mid-Move" State.</div></div>
      <img src="assets/settle/proto-community.jpg" alt="Settle community screen with dining, events and discussions" loading="lazy">
    </div>
    <a class="jump" href="https://www.figma.com/proto/tPsz1kYWrE2gMf47X8u1kt/Portfolio?node-id=61-44" target="_blank" rel="noopener"><span>Open the Figma prototype</span>{ARROW_NE}</a>

    <h2>Key Takeaways</h2>
    <ul>
      <li>Designing for journeys is more effective than designing for features. This project reinforced the importance of structuring products around user progress and mental models, rather than isolated features. Organizing the app into relocation phases significantly reduced cognitive load and improved clarity.</li>
      <li>Information architecture plays a critical role in reducing anxiety. Relocation is an emotionally stressful experience. A well-thought-out IA can act as a reassurance mechanism, showing users what to focus on now and what can wait.</li>
      <li>Contextual visibility improves decision-making. Surfacing tasks, documents, and guidance based on the user’s current phase made the experience feel personalized and intentional, rather than overwhelming.</li>
      <li>Support systems are as important as functional tools. Integrating community discussions and an AI assistant highlighted that users need emotional and informational support, not just checklists, during major life transitions.</li>
      <li>Simplification is a design skill. One of the biggest challenges was distilling a complex system into a clear, high-level IA suitable for a portfolio, without losing the product’s depth or intent.</li>
    </ul>
  </div>
</main>
''' + FOOTER

# ------------------------------------------------------------------ TRACKR
trackr = head("TRACKR — Coaching platform for fitness coaches · Saira Garg", "Case study: TRACKR, a platform where fitness coaches plan workouts, assign them to clients and track progress.") + nav('work') + f'''
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <h1>TRACKR | Coaching Platform for Fitness Coaches</h1>
    <p class="lede">A shared place for coaches and clients to plan workouts, record sessions and follow progress, replacing the spreadsheet, form and chat stack most coaches run today.</p>
    <figure class="cover"><div class="browser"><img src="assets/trackr/product.jpg" alt="TRACKR coach overview showing active clients, client follow-ups, sessions logged and adherence, next to the client app logging a bench press set"></div></figure>

    <h2>Project Overview</h2>
    <p>Problem: Online coaches are capped not by demand but by admin. Every additional client adds hours of formatting plans, chasing check-ins and reconstructing context from chat threads.</p>
    <p>Role: Co-Founder, Aug 2026 – Present. I defined the product from coach interviews through to a PRD covering positioning, pricing and success metrics, then built the coach web app and the client mobile app using AI tools (Claude Code, OpenAI Codex), going from idea to working product in under 3 months. TRACKR is now being prepared for a beta launch to test and iterate.</p>
    <a class="jump" href="https://trackrdaily.com" target="_blank" rel="noopener"><span>Visit trackrdaily.com</span>{ARROW_NE}</a>

    <h2>At a Glance</h2>
    <div class="stats">
      <div class="stat"><b>8</b><span>fitness coaches interviewed to define requirements</span></div>
      <div class="stat"><b>&lt;3 mo</b><span>from idea to a working product</span></div>
      <div class="stat"><b>2</b><span>surfaces: coach web workspace and client mobile app</span></div>
      <div class="stat"><b>870+</b><span>exercises in the built-in library</span></div>
    </div>

    <h2>The Problem</h2>
    <p>A typical online coach operates across four disconnected tools. Nothing connects them, so the coach becomes the integration layer, and that work grows with every client added.</p>
    <table class="table">
      <thead><tr><th>Job</th><th>Tool today</th><th>Where it fails</th></tr></thead>
      <tbody>
        <tr><td>Deliver the plan</td><td>Spreadsheet</td><td>Unreadable on a phone mid-set; no logging</td></tr>
        <tr><td>Collect intake and check-ins</td><td>Online form</td><td>Responses sit in a sheet nobody opens</td></tr>
        <tr><td>Communicate</td><td>Chat app</td><td>Coaching decisions buried in chat history</td></tr>
        <tr><td>Track progress</td><td>Manual notes</td><td>No trend view; reconstructed from memory</td></tr>
      </tbody>
    </table>
    <p class="caption">On the other side, the client cannot reliably answer two questions: what am I doing today, and am I making progress?</p>

    <h2>User Research</h2>
    <p>I interviewed 8 fitness coaches to understand how they plan, deliver and review training today. The clearest finding was that scattered tools cap how many clients a coach can take on. That finding became the spine of the PRD.</p>
    <h3>Key Insights &amp; Opportunity Areas</h3>
    <div class="notes">
      <div class="note sage"><b>No Unified View</b>Coaches react to whoever messages loudest, not to whoever needs help most.</div>
      <div class="note slate"><b>Silent Churn</b>A disengaged client stays invisible until they quit, and the coach finds out weeks late.</div>
      <div class="note clay"><b>Manual Plan Updates</b>One programming change repeated across a full roster costs hours of copy and paste.</div>
      <div class="note plum"><b>No Trend View</b>Progression decisions are made on recall instead of the client’s logged history.</div>
      <div class="note gold"><b>Admin Crowds Out Coaching</b>Quality starts to slip once a roster grows past what one person can track by hand.</div>
    </div>

    <h2>Positioning</h2>
    <p>Most coaching platforms compete on breadth: nutrition, payments, video, wearables, white-labelling. TRACKR competes on depth in the loop a coach and client repeat every single day.</p>
    <div class="pillars">
      <div class="pillar"><i>01</i><b>Client-side speed</b>Open, see today’s session, log, done. The client should understand today’s workout in under two seconds.</div>
      <div class="pillar"><i>02</i><b>One coaching workspace</b>Plan training, manage clients and review progress in one place. Reuse programs across clients.</div>
      <div class="pillar"><i>03</i><b>Built for teams from day one</b>Every workspace is an org, whether it is one independent coach or a coaching business with several.</div>
    </div>

    <h2>The Solution</h2>
    <p>Write the plan once, and every client gets their own copy. The coach creates a plan, shares it and sees how training is going; the client opens the app and knows exactly what to do next.</p>
    <ul>
      <li>Plan training: build programs with exercises, sets, reps and rest times, reuse templates and choose a start date for each client.</li>
      <li>Follow each workout: clients see their assigned sessions, view exercise demonstrations and record their sets in the client app.</li>
      <li>Review progress: completed sessions and workout history help the coach decide what comes next.</li>
      <li>Know who needs you: a follow-up list puts the clients who need attention first.</li>
    </ul>
    <h3>What it replaces</h3>
    <div class="replace">
      <div><s>Copying last week’s spreadsheet for every client</s><i>→</i><span>Assign a program once. Each client gets their own copy, week after week.</span></div>
      <div><s>Asking “did you train today?” in a chat</s><i>→</i><span>Clients log every set as they go, and the coach sees it the same day.</span></div>
      <div><s>Scrolling threads to find who’s slipping</s><i>→</i><span>A follow-up list puts the clients who need you first.</span></div>
    </div>

    <h2>Product Architecture</h2>
    <p>Two surfaces share one backend. Coaches work on the web, where program building and roster review are comfortable at a desk and still usable on a phone browser between sessions. Clients train in a mobile app built for the gym floor, where speed matters more than features.</p>
    <div class="pillars">
      <div class="pillar"><i>Coach</i><b>Web workspace</b>Overview, clients, programs and the exercise library. One coach surface instead of two.</div>
      <div class="pillar"><i>Client</i><b>Mobile app</b>Today’s session first, set-by-set logging and workout history.</div>
      <div class="pillar"><i>Org</i><b>Roles and access</b>Coach, Admin and Super-user roles, with each coach seeing only their own clients.</div>
    </div>

    <h2>Success Metrics</h2>
    <p>The north-star metric is weekly logged sessions per active client. It captures both sides of the product: the coach published something worth doing, and the client did it.</p>
    <table class="table">
      <thead><tr><th>Layer</th><th>Metric</th><th>How it is measured</th></tr></thead>
      <tbody>
        <tr><td>Activation</td><td>Workspace activated</td><td>At least one client logs at least one session</td></tr>
        <tr><td>Engagement</td><td>Weekly adherence</td><td>Sessions logged ÷ sessions assigned</td></tr>
        <tr><td>Retention</td><td>Coach week-4 retention</td><td>Coach still active in week 4</td></tr>
        <tr><td>Leverage</td><td>Clients per coach</td><td>Median, month 3 vs month 1</td></tr>
        <tr><td>Performance</td><td>Time to today’s workout</td><td>Under 2 seconds on a cold start</td></tr>
      </tbody>
    </table>

    <h2>Building with AI</h2>
    <p>TRACKR is built with AI coding tools. I work as the product owner: writing the requirements, reviewing flows in the running product, and directing Claude Code and OpenAI Codex through the coach web app and the client mobile app. That took TRACKR from idea to a working product in under 3 months.</p>

    <h2>Key Takeaways</h2>
    <ul>
      <li>Depth beats breadth early on. Choosing the daily coach and client loop over a long feature list kept the product small enough to finish and sharp enough to explain.</li>
      <li>Interviews should change the plan. Talking to coaches moved the problem statement from "coaches need an app" to "scattered tools cap client capacity", which is a problem with a measurable outcome.</li>
      <li>Write the metric before the feature. Defining adherence and retention up front made it easier to say no to work that would not move them.</li>
      <li>AI tools shift the bottleneck to product judgement. When building is fast, the hard part becomes knowing precisely what to ask for and noticing when the result is wrong.</li>
    </ul>
  </div>
</main>
''' + FOOTER


# ------------------------------------------------------------------ MAINSTREET
def mimg(src, alt):
    return f'<img src="assets/mainstreet/{src}" alt="{alt}" loading="lazy">'
def hifi(k, title, text, src):
    return f'<div class="hifi"><div class="shot">{mimg(src, title)}</div><div><div class="k">{k} · HI-FI</div><h3>{title}</h3><p>{text}</p></div></div>'
def tool(name, kind, worked, gaps, shots):
    w=''.join(f'<li>{x}</li>' for x in worked); g=''.join(f'<li>{x}</li>' for x in gaps)
    im=''.join(mimg(a,b) for a,b in shots)
    return f'<div class="tool"><div><h3>{name}</h3><div class="kind">{kind}</div><h5>WHAT WORKED</h5><ul>{w}</ul><h5 class="gap">GAPS</h5><ul>{g}</ul></div><div class="shots">{im}</div></div>'
def h2(num, title, sub=''):
    t = f'<h2 class="tight"><span class="num">{num}</span>{title}</h2>' if sub else f'<h2><span class="num">{num}</span>{title}</h2>'
    return t + (f'<p class="sub">{sub}</p>' if sub else '')

mainstreet = head("MainStreet — AI-curated local discovery · Saira Garg", "Case study: MainStreet, an AI-curated, journey-based local discovery app for busy people in Swiss cities.") + nav('work') + f"""
<main class="case">
  <a class="goback" href="index.html#work">{ARROW_L}<span>GO BACK</span></a>
  <div class="col">
    <div class="eyebrow">Case study · Personal project · Built with AI workflows</div>
    <h1>MainStreet. AI-curated local discovery, designed with AI workflows.</h1>
    <p class="lede">A product design project exploring how AI can turn the scattered ritual of finding a good local spot — Google Maps for ratings, Instagram for vibe, TikTok for food, friends for a sanity check — into a single, predictive, journey-based discovery feed for busy people in Swiss cities.</p>
    <div class="grid4 cover4">{mimg("hifi-new-1.jpeg","Discovery screen")}{mimg("hifi-new-2.jpeg","Pattern detected screen")}{mimg("hifi-new-4.jpeg","Unified location dropdown")}{mimg("hifi-new-5.jpeg","Bottom sheet list view")}</div>
    <div class="origin">MainStreet started close to home. My sister recently moved to Zürich, and when she told me how hard it was to find places that actually suited her in a new city, hopping between four apps and still ending up somewhere average, I came forward with this idea: an app that learns the routes you already take and curates local spots along them.</div>
    <a class="jump" href="#hifi-mocks"><span>Jump to hi-fi mocks</span>{ARROW_D}</a>
    <div class="meta"><div><span>ROLE</span><b>Product &amp; Design</b></div><div><span>TYPE</span><b>Consumer · Discovery</b></div><div><span>PLATFORM</span><b>iOS · Android</b></div></div>

    {h2("01", "Design Foundations")}
    <p>Before starting any design, I focus on four things that keep the work honest and directional:</p>
    <div class="grid4">
      <div class="pillar"><i>a</i><b>Problem Statement</b>The reason we're building — the friction we're removing from real people's days.</div>
      <div class="pillar"><i>b</i><b>Target Audience</b>Who we're building for, in enough detail to make real trade-offs.</div>
      <div class="pillar"><i>c</i><b>Surface</b>Where the experience lives, and where it explicitly does not.</div>
      <div class="pillar"><i>d</i><b>Success Metrics</b>How we'll know it's working — for users and for the business.</div>
    </div>

    {h2("02", "Problem Statement")}
    <p>Finding the right local business is currently a mess — or doesn't happen at all. People bounce between Google Maps for ratings, Instagram to check the vibe, TikTok to see if the food looks good, and friends for recommendations — and still end up at places that don't match what they actually want. On the other side, local business owners struggle to reach their ideal customers and rarely connect with the audience they were built for.</p>

    {h2("03", "Target Audience")}
    <div class="grid3">
      <div class="pillar"><b>DEMOGRAPHICS</b>Young professionals, expats and students (Ages 22–36) living in urban Swiss areas — Zürich, Geneva, and similar.</div>
      <div class="pillar"><b>CHARACTERISTICS</b>Tech-savvy, values supporting local and independent businesses over major chains, has specific dietary or lifestyle preferences (vegan, specialty coffee, vintage fashion, etc.).</div>
      <div class="pillar"><b>PAIN POINTS</b>Limited free time. They hate wasting a weekend meal or an afternoon off on a mediocre experience because a generic review platform gave it 4.5 stars. They want a curated ‘vibe' that aligns with their lifestyle without spending an hour researching it.</div>
    </div>

    {h2("04", "Surface")}
    <p>Mobile apps (iOS &amp; Android) are in scope. Web is explicitly out of scope — the core value depends on live location, passive route learning and glanceable, thumb-first interactions that only make sense on a phone in the user's hand.</p>

    {h2("05", "Success Metrics")}
    <div class="grid5">
      <div class="stat"><b>TTV</b><span>Time-to-Value</span></div><div class="stat"><b>FCR</b><span>Feed Conversion Rate</span></div><div class="stat"><b>IMP</b><span>Implicit Feedback</span></div><div class="stat"><b>EXP</b><span>Explicit Feedback</span></div><div class="stat"><b>WAU</b><span>Weekly Active Users</span></div>
    </div>

    {h2("06", "AI Tools · Prototyping", "Where AI accelerated the visual head start, and where it fell short.")}
    <p>To kick off the visual process, I used AI generation tools to get a rapid head start. They provided a great baseline and surfaced ideas much faster than manual competitive analysis. But they couldn't be used as-is — each had core UX gaps that shaped the direction of the real design.</p>
    {tool("Lovable", "MAP + CAROUSEL EXPLORATION", ["Decent carousel showing matching scores alongside the map"], ["Splits ‘Home' and ‘Map' into two tabs — introduces unnecessary friction", "Routing logic is flawed; unclear how the UI handles a plain ‘current location' state with no route", "Bright red on the map reads as traffic / warning — wrong signal for a premium, curated vibe"], [("ai-lovable.png", "Lovable exploration for MainStreet")])}
    {tool("Figma Make", "RAPID LAYOUT EXPLORATION", ["Fast baseline styling", "Surfaces card and grid ideas quickly"], ["No dedicated list view to actually browse personalized suggestions", "Context is broken — no clear signal of where the search is happening", "No way to add a route or differentiate it from a standard neighborhood search"], [("ai-figma-make.png", "Figma Make exploration for MainStreet")])}
    {tool("Google Stitch", "ONBOARDING &amp; DISCOVERY STRUCTURE", ["Strong onboarding baseline — pictorial choices, one question per page", "Confirms the low-cognitive-load direction I was already thinking about"], ["‘location_on' header is vague and unhelpful", "No system for manually applying routes or surfacing learned ones", "Separates ‘Matches for You' from the Map — the exact split I chose to solve"], [("ai-google-stitch.png", "Google Stitch exploration 1 for MainStreet"), ("ai-google-stitch-2.png", "Google Stitch exploration 2 for MainStreet")])}

    {h2("07", "Wireframing", "Back to paper, to solve the structural flaws.")}
    <p>After identifying the structural flaws in the AI explorations, I stepped back and moved to paper. Onboarding was designed around a single question per screen with heavy use of visual graphics to drastically reduce cognitive load.</p>
    <p>I also prioritised a dedicated ‘pre-permission' location screen. Because the app's value depends on tracking daily routes, it's critical to set the right tone and clearly explain the value exchange before triggering the OS-level permission prompt.</p>
    <p>For the home screen, the challenge was seamlessly combining four complex elements: map interactions, routing logic, current location, and a personalised list of places with matching scores. I mapped out how users would intuitively add routes or apply quick filters like ‘Coffee' or ‘Dinner' without losing context.</p>
    <div class="shots3">
      <figure>{mimg("wireframe-onboarding.png", "Paper wireframe — Splash, onboarding and pre-permission")}<figcaption>SPLASH · ONBOARDING · PRE-PERMISSION</figcaption></figure>
      <figure>{mimg("wireframe-home.png", "Paper wireframe — Home screen trials")}<figcaption>HOME SCREEN TRIALS</figcaption></figure>
      <figure>{mimg("wireframe-location.png", "Paper wireframe — Location sheet, nearby and nav")}<figcaption>LOCATION SHEET · NEARBY · NAV</figcaption></figure>
    </div>

    {h2("08", "Mocks for Onboarding", "One question per screen, for both user and business flows.")}
    <p>The onboarding screens are designed to hold one question per page — decreasing cognitive load and minimising time spent on any single screen. Separate onboarding flows exist for the business owner and the everyday user.</p>
    <div class="shots2">
      <figure>{mimg("onboarding-1.png", "Splash screen")}<figcaption>SPLASH SCREEN</figcaption></figure>
      <figure>{mimg("onboarding-2.png", "Onboarding — user and business")}<figcaption>ONBOARDING — USER &amp; BUSINESS</figcaption></figure>
      <figure>{mimg("onboarding-3.png", "Business onboarding")}<figcaption>BUSINESS ONBOARDING</figcaption></figure>
      <figure>{mimg("onboarding-4.png", "User onboarding")}<figcaption>USER ONBOARDING</figcaption></figure>
    </div>

    <div id="hifi-mocks"></div>
    {h2("09", "Hi-fi Mocks", "The active ‘Exploring' state — before routing is applied.")}
    <p>From the wireframes, I developed a set of high-fidelity screens that walk through the core loop — from a plain ‘Exploring' state, to passive route detection, to the unified spatial controls that hold it all together.</p>
    {hifi("01", "Discovery — current location", "The default ‘Exploring' state stays fundamentally map-centric to preserve context, paired with low-friction quick-filter pills — ‘Open Now', ‘Coffee', ‘Dinner' — so users can rapidly narrow criteria without ever opening a separate search menu. The wheel carousel maximises each venue's visual aesthetic: walk time, a Smart Matching Score, and vibe tags like ‘opulent' or ‘cozy' answer <em>is this my vibe?</em> at a single glance.", "hifi-new-1.jpeg")}
    {hifi("02", "Pattern detected — new route", "MainStreet's true differentiator: predictive, journey-based curation. The system passively recognises a repeated route — Wiedikon → Zurich HB — and surfaces a subtle ‘Pattern Detected' banner, curating the sheet to matches along that path. It proves the intelligence without ever asking the user to configure it.", "hifi-new-2.jpeg")}
    {hifi("03", "No banner — learned commute", "Once acknowledged, the banner is dismissed and stays hidden for subsequent trips on the same route. Utility apps lose trust the moment they become noisy — showing the pattern once, then quietly curating in the background, is the detail that earns the second visit.", "hifi-new-3.jpeg")}
    {hifi("04", "Unified location dropdown", "The most important structural decision: all spatial controls live inside a single top-left menu — switching to a learned ‘Morning Commute', editing a saved route, or jumping to a new neighborhood. The top-left universally controls <em>where</em> the app is looking, so the bottom sheet is free to focus purely on <em>what</em> is there.", "hifi-new-4.jpeg")}

    {h2("10", "Alternative — Bottom Sheet List", "Optimised for rapid scanning, closer to established habits.")}
    <div class="hifi"><div class="shot">{mimg("hifi-new-5.jpeg", "Alternative — bottom sheet list view")}</div><div><p>I also built an alternative mock using a standard bottom-sheet list. The wheel is optimised for a ‘focused decision' model — one premium recommendation at a time.</p><p>This alternative is designed for users who prioritise rapid scanning: it lets them cross-compare 4–5 highly-rated places simultaneously and leans on established mental models from apps like Google Maps.</p></div></div>

    {h2("11", "Design Decisions — the Whys", "Each decision maps back to trust, focus or premium feel.")}
    <div class="why">
      <div><b>The Unified Location Dropdown</b><span>All spatial controls — current location, learned routes, route editing — live inside a single top-left menu. The top-left corner dictates where the app is looking; the feed dictates what is there. It prevents routing features from getting buried in a Settings or Profile tab and keeps the mental model perfectly clean.</span></div>
      <div><b>Contextual Header &amp; One-Time Banner</b><span>The ‘Pattern Detected' banner appears only once, on initial route discovery, then hides for subsequent trips. Utility apps lose trust when they get noisy. Showing it once proves the intelligence without becoming annoying.</span></div>
      <div><b>The Focused Immersive Wheel</b><span>Instead of a dense bottom-sheet list, a rotating wheel elevates one premium recommendation at a time. Highly tactile, differentiated from utilitarian map interfaces, and better suited to a time-poor user making a focused decision. Users swipe to spin and explore other curated options.</span></div>
      <div><b>The Floating Navigation Bar</b><span>A decoupled, dark floating bar — not an edge-to-edge system tab bar. Maximises immersive map visibility when the sheet is closed, and anchors primary buttons within the thumb zone per Fitts's Law.</span></div>
      <div><b>Matching Scores &amp; Vibe Tags</b><span>Discovery cards lead with a specific match percentage (e.g. ‘95% Match'), walk time (‘4 mins') and short vibe tags (‘Fine Dine · Cozy', ‘Exclusive · Buffet'). The UI answers ‘Why is this for me?' before ‘How far is it?'.</span></div>
      <div><b>Color Psychology — Indigo Ascent</b><span>Deliberately avoided red and green. Red reads as traffic / warning on a map; green makes it feel like a GPS clone. A deep blue-purple (indigo) is subtle but instantly signals a premium, curated matchmaking tool.</span></div>
      <div><b>Accessibility</b><span>48×48px minimum tap targets, WCAG AA contrast, dynamic text sizing, VoiceOver support and color-independent affordances — built in, not bolted on.</span></div>
    </div>

    <a class="next" href="settle.html"><div><span>NEXT</span><b>Settle — Relocation &amp; travel planner</b></div>{ARROW_L}</a>
  </div>
</main>
""" + FOOTER

# ------------------------------------------------------------------ ABOUT
def xp(when, org, role, text):
    return f'<div class="xp"><div class="when">{when}</div><div><h3>{org}<span>{role}</span></h3><p>{text}</p></div></div>'
def chips(label, items):
    return f'<div class="skillrow"><div class="when">{label}</div><div class="chips">' + ''.join(f'<span>{i}</span>' for i in items) + '</div></div>'

about = head("About — Saira Garg", "About Saira Garg — co-founder of TRACKR, software engineer at Cisco, and founder of a 70+ member run club.") + nav('about') + f'''
<main>
  <section class="about-top">
    <div class="portrait"><img src="assets/saira-portrait.jpg" alt="Saira Garg standing in a garden, smiling"></div>
    <div>
      <h1>Hey, I’m Saira!</h1>
      <p>A product manager who loves turning messy problems into simple products. I start with the people who have the problem, write down what would actually help, and then build it.</p>
      <p>Right now I’m co-founding TRACKR, a platform for fitness coaches and their clients, while working as a Software Engineer at Cisco on cloud management for campus switches.</p>
      <p>Outside work, I run. I started a run club in Bathinda that has grown to 70+ members.</p>
    </div>
  </section>

  <section class="approach">
    <div class="wrap">
      <h2>My Approach</h2>
      <div class="split">80% Problem Solver<br>10% Builder - 10% Runner</div>
      <p>I don’t think of myself as just an engineer or just a product person; I’m a problem solver with a versatile toolkit. I interview users, write the PRD, design the flow in Figma and build the thing with AI tools. Wearing several hats lets me look at a problem from every angle and bring value to both the business and the user.</p>
    </div>
  </section>

  <section class="about-block" id="experience">
    <h2>Experience</h2>
    {xp("Aug 2026 – Present", "TRACKR", "Co-Founder", "Co-founded a platform where fitness coaches plan workouts, assign them to clients and track progress. Interviewed 8 coaches, wrote the PRD covering positioning, pricing and success metrics, and built the coach web app and client mobile app with AI tools in under 3 months.")}
    {xp("Jul 2026 – Present", "Cisco", "Software Engineer", "Building cloud management for Cisco campus switches with cross-functional teams, so enterprise customers can onboard, monitor and automate switches from the Meraki Dashboard.")}
    {xp("Jan 2026 – Jun 2026", "Cisco", "Software Engineering / Program Management Intern", "Led a new UCCE router feature from requirements to launch across engineering, validation and UX, supporting up to 1000 queries per second. Wrote functional specs, prioritised the Agile backlog and cut data processing time by 12%.")}
    {xp("Jan 2025 – Apr 2025", "Snapdeal", "Software Engineering Intern", "Built in-house seller advertising tools with product and marketing teams, replacing third-party software and saving up to ₹50 Lakhs a month.")}
  </section>

  <section class="about-block">
    <h2>Leadership &amp; Achievements</h2>
    {xp("Founder", "Run Club, Bathinda", "70+ members", "Founded a community run club and grew it through social media outreach and regular group runs into an active local fitness community.")}
    {xp("Finalist · 2024", "Myntra HackerRamp WeForShe", "Shared Carts", "Designed and prototyped a social shopping feature that lets friends build and shop from one cart together, reaching the finals among thousands of teams.")}
    {xp("2025 – 26", "PECFEST", "Head of Publicity", "Led publicity for the college’s annual cultural fest through social media and campus campaigns, driving record participation.")}
    {xp("Education", "Punjab Engineering College", "B.Tech, Computer Science", "Chandigarh, India. CGPA 8.0. AWS AI Scholarship recipient (AI Programming Nanodegree).")}
  </section>

  <section class="about-block">
    <h2>Skills</h2>
    {chips("Product", ["Product Strategy", "User Research", "Market Research", "PRDs", "Roadmapping", "Prioritization", "Competitive Analysis", "Pricing", "Go-to-Market", "KPIs", "Agile / Scrum"])}
    {chips("AI Tools", ["Claude Code", "OpenAI Codex", "Google Gemini API"])}
    {chips("Design", ["Figma", "Wireframing", "Prototyping", "Usability Testing", "Journey Mapping"])}
    {chips("Technical", ["Java", "Python", "JavaScript", "React.js", "Spring", "REST APIs", "Git", "JIRA", "Postman"])}
  </section>
</main>
''' + FOOTER

for name, html in [("index.html", home), ("settle.html", settle), ("trackr.html", trackr), ("mainstreet.html", mainstreet), ("about.html", about)]:
    with open(os.path.join(OUT, name), "w") as f: f.write(html)
    print(name, len(html))
