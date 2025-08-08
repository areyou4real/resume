import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# =========================
# Page & Global Config
# =========================
st.set_page_config(
    page_title="Killer Resume — Dheer Doshi",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Sidebar Controls
# =========================
with st.sidebar:
    st.subheader("Display")
    theme_choice = st.selectbox(
        "Theme",
        ["Sleek Blue (Light)", "Teal/Purple (Light)", "Dark"],
        index=0
    )
    high_contrast = st.checkbox("High contrast", value=False)
    reduce_motion = st.checkbox("Reduce motion", value=False)
    st.divider()
    st.subheader("Mode & Role")
    mode = st.toggle("Scan Mode (TL;DR)", value=True)
    role_choice = st.radio("Role focus", ["Data Science", "Product", "Design"])
    st.divider()
    st.subheader("Utilities")
    if st.button("Open Print Dialog (PDF)"):
        components.html("<script>window.print()</script>", height=0)

# =========================
# Theme Tokens
# =========================
TOKENS = {
    "Sleek Blue (Light)": {
        "--bg": "#f6f7fb", "--surface": "#ffffff", "--text": "#0f172a", "--muted": "#64748b",
        "--primary": "#2563eb", "--accent": "#0ea5e9", "--success": "#16a34a", "--warn": "#f59e0b",
        "--ring": "rgba(14,165,233,.35)", "--border": "rgba(2,6,23,.08)"
    },
    "Teal/Purple (Light)": {
        "--bg": "#f7fbfb", "--surface": "#ffffff", "--text": "#111827", "--muted": "#64748b",
        "--primary": "#06b6d4", "--accent": "#7c3aed", "--success": "#16a34a", "--warn": "#f59e0b",
        "--ring": "rgba(14,165,233,.35)", "--border": "rgba(2,6,23,.08)"
    },
    "Dark": {
        "--bg": "#0b1020", "--surface": "#11162a", "--text": "#e6e9f2", "--muted": "#a3acc3",
        "--primary": "#06b6d4", "--accent": "#7c3aed", "--success": "#22c55e", "--warn": "#f59e0b",
        "--ring": "rgba(14,165,233,.45)", "--border": "rgba(226,233,242,.12)"
    }
}
tokens = TOKENS[theme_choice]

if high_contrast:
    tokens["--text"] = "#000" if theme_choice != "Dark" else "#fff"
    tokens["--muted"] = "#111" if theme_choice != "Dark" else "#eee"
    tokens["--border"] = "rgba(0,0,0,.3)" if theme_choice != "Dark" else "rgba(255,255,255,.35)"

motion_value = "0s" if reduce_motion else ".25s"

# Small f-string with escaped braces ONLY for variables:
style_vars = f"""
<style>
:root {{
  --bg: {tokens['--bg']};
  --surface: {tokens['--surface']};
  --text: {tokens['--text']};
  --muted: {tokens['--muted']};
  --primary: {tokens['--primary']};
  --accent: {tokens['--accent']};
  --success: {tokens['--success']};
  --warn: {tokens['--warn']};
  --ring: {tokens['--ring']};
  --border: {tokens['--border']};
  --shadow-1: 0 1px 2px rgba(0,0,0,.06);
  --shadow-2: 0 10px 30px rgba(0,0,0,.10);
  --motion: {motion_value};
}}
</style>
"""
st.markdown(style_vars, unsafe_allow_html=True)

# Big CSS block as a plain string (no interpolation → no brace escaping hassle)
css_base = """
<style>
html, body, [class*="css"] {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  scroll-behavior: smooth;
}

/* Sticky header + toc */
.navbar {
  position: sticky; top: 0; z-index: 9999;
  backdrop-filter: saturate(1.2) blur(10px);
  background: color-mix(in oklab, var(--surface) 82%, transparent);
  border-bottom:1px solid var(--border);
  padding: 8px 10px; border-radius: 0 0 12px 12px;
}
.nav-grid { display:flex; gap:10px; align-items:center; justify-content:space-between; flex-wrap:wrap; max-width: 1200px; margin: 0 auto; }
.nav-links { display:flex; gap:8px; flex-wrap:wrap; }
.nav-btn {
  border:1px solid var(--border); background:var(--surface); color:var(--text);
  padding:8px 12px; border-radius:999px; font-weight:600; text-decoration:none;
  transition: transform var(--motion) ease, box-shadow var(--motion) ease, border-color var(--motion) ease;
  position:relative;
}
.nav-btn[aria-current="page"] { border-color: var(--primary); box-shadow: 0 0 0 3px var(--ring); }
.nav-btn:hover { transform: translateY(-1px); box-shadow: var(--shadow-2); }

/* Sections + cards */
.section { scroll-margin-top: 90px; max-width: 1200px; margin: 0 auto; padding: 8px 12px; }
.card { background:var(--surface); border:1px solid var(--border); border-radius:18px; padding:16px 18px; box-shadow: var(--shadow-1); }
.section-title { font-weight:800; font-size:clamp(1.2rem, 1vw + 1rem, 1.6rem); letter-spacing:.2px; margin:0 0 8px 0; }
.muted { color: var(--muted); }

/* Hero */
.hero {
  margin: 10px auto 16px auto; padding: 26px 22px; border-radius: 20px;
  background: radial-gradient(1200px 600px at 12% -10%, color-mix(in oklab, var(--accent) 16%, transparent) 0%, transparent 50%),
              radial-gradient(900px 500px at 95% 10%, color-mix(in oklab, var(--primary) 14%, transparent) 0%, transparent 55%),
              var(--surface);
  border: 1px solid var(--border); box-shadow: var(--shadow-2);
  animation: fadeUp var(--motion) ease forwards;
  max-width: 1200px;
}
@keyframes fadeUp { from {opacity:.0; transform: translateY(8px)} to {opacity:1; transform: translateY(0)} }
.hero h1 { font-family: "Space Grotesk", Inter, ui-sans-serif; font-size:clamp(2rem, 2.5vw + 1rem, 3rem); margin:0 0 6px 0; line-height:1.1; }
.badge {
  display:inline-block; padding:6px 12px; border-radius:999px; margin:0 8px 8px 0;
  background: color-mix(in oklab, var(--primary) 8%, var(--surface));
  border:1px solid color-mix(in oklab, var(--primary) 25%, var(--border));
  font-weight:600; font-size:.9rem;
}
.kpi { display:inline-block; padding:6px 10px; border-radius:10px; border:1px dashed var(--border); margin:0 10px 10px 0; }

/* Grid */
.grid { display: grid; gap: 16px; grid-template-columns: repeat(12, 1fr); }
.col-8 { grid-column: span 8; }
.col-4 { grid-column: span 4; }
@media (max-width: 900px) { .col-8, .col-4 { grid-column: 1 / -1; } }

/* Project cards */
.proj-card { transition: transform var(--motion) ease, box-shadow var(--motion) ease; }
.proj-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-2); }

/* Meters */
.meter-wrap { height:8px; background: color-mix(in oklab, var(--muted) 18%, transparent); border-radius:24px; overflow:hidden; border:1px solid var(--border); }
.meter-val { height:100%; background: var(--primary); width:0; transition: width 0.8s ease; }

/* Testimonials carousel */
.carousel { position:relative; overflow:hidden; border-radius:16px; border:1px solid var(--border); background:var(--surface); }
.carousel-track { display:flex; transition: transform var(--motion) ease; }
.carousel-item { min-width:100%; padding: 18px; box-sizing: border-box; }
.carousel-controls { display:flex; gap:10px; position:absolute; right:10px; bottom:10px; }
.carousel button { border:1px solid var(--border); background:var(--surface); border-radius:999px; padding:6px 10px; }
@media (prefers-reduced-motion) { .carousel-track { transition:none !important; } }

/* Floating CTA */
.floating-cta {
  position: fixed; right: 16px; bottom: 18px; z-index: 9998;
  display:flex; gap:8px; flex-wrap:wrap;
}
.floating-cta a {
  text-decoration:none; padding:10px 12px; border-radius:999px; font-weight:700;
  background: var(--primary); color: #fff;
}
@media (max-width: 700px) {
  .floating-cta { position: fixed; left:0; right:0; bottom:0; justify-content:center; background:var(--surface); padding:10px; border-top:1px solid var(--border); }
}

/* Focus rings */
a:focus-visible, button:focus-visible { box-shadow: 0 0 0 4px var(--ring); outline: none; }
hr { border:none; border-top:1px solid var(--border); margin: 8px 0 16px 0; }
</style>
"""
st.markdown(css_base, unsafe_allow_html=True)

# A small flag node for JS to read reduce-motion (avoids f-string in JS)
st.markdown(
    f'<div id="flags" data-reduce="{str(reduce_motion).lower()}"></div>',
    unsafe_allow_html=True
)

# =========================
# More realistic data
# =========================
ROLES = [
    {
        "label": "Data Science",
        "tldr": [
            "Built reproducible ML workflows (DVC + GitHub Actions).",
            "Improved mutation prediction AUROC by ~5.2 points.",
            "Created investor-ready dashboards from messy macro data."
        ],
        "deep": [
            "Implemented GRU/TCN sequence model for rare variant prediction; AUROC +5.2 vs baseline on held-out set.",
            "Packaged inference API (FastAPI + Docker); request P95 ~95 ms on T4; added drift checks and alerting.",
            "Authored research notes summarizing macro indicators; automated weekly refresh with Python + Airflow."
        ],
        "featured": ["genomesage", "smpbed"]
    },
    {
        "label": "Product",
        "tldr": [
            "Scoped ML features with clear success metrics.",
            "Shipped A/B test harness for Streamlit app flows.",
            "Cut onboarding drop-off ~12% with copy/UI tweaks."
        ],
        "deep": [
            "Defined outcome metrics (activation, task success, time-to-value) and dashboards for project reviews.",
            "Added event logging + experiment flags; documented a 3-step review for launches.",
            "Partnered with design to simplify first-run experience; improved conversion in smoke tests by ~12%."
        ],
        "featured": ["vision"]
    },
    {
        "label": "Design",
        "tldr": [
            "Introduced a token-based design system for internal apps.",
            "Audited components to meet WCAG 2.2 AA.",
            "Prototyped case-study layouts for stakeholder reviews."
        ],
        "deep": [
            "Created semantic color tokens (light/dark) + docs; reduced per-page CSS by ~28%.",
            "Added focus states, skip links, and keyboard traps fix; ran manual checks with axe DevTools.",
            "Clickable prototypes in Figma to align stakeholders before build."
        ],
        "featured": ["vision", "sir"]
    },
]

PROJECTS = [
    {
        "id":"genomesage","title":"GenomeSage",
        "summary":"Predicts likely genetic mutations using sequence models; includes explainability views.",
        "par":[
            {"type":"Problem","text":"Rare variant prediction suffered from low signal and class imbalance."},
            {"type":"Action","text":"Engineered k-mer embeddings; trained GRU/TCN with focal loss; added SHAP plots."},
            {"type":"Result","text":"AUROC +5.2 over baseline; ~18% fewer false positives at fixed precision."}
        ],
        "metrics":[{"label":"AUROC","value":"0.89→0.94"},{"label":"Batch latency","value":"~120 ms"}],
        "tags":{"stack":["PyTorch","Python","Docker"],"industry":["Bio"],"year":2025,"impact":"High"}
    },
    {
        "id":"smpbed","title":"SMPBED",
        "summary":"Aggregates FRED/Quandl indicators to forecast S&P 500 direction (edu project).",
        "par":[
            {"type":"Problem","text":"Signals from macro time series were noisy and unstable."},
            {"type":"Action","text":"Built feature store; regularized logistic model + gradient boosting; walk-forward validation."},
            {"type":"Result","text":"Directional accuracy +6–7 p.p. over naive; Sharpe ~0.9 in backtests (educational)."}
        ],
        "metrics":[{"label":"Hit rate (val)","value":"~58%"},{"label":"Sharpe (sim)","value":"~0.9"}],
        "tags":{"stack":["Python","R","Tableau"],"industry":["Finance"],"year":2025,"impact":"Medium"}
    },
    {
        "id":"vision","title":"Vision Web App",
        "summary":"Streamlit + TensorFlow app for real-time image classification with GPU builds.",
        "par":[
            {"type":"Problem","text":"Manual image triage took minutes; needed sub-second predictions."},
            {"type":"Action","text":"Quantized model; cached preprocessing; Dockerized GPU runtime; added batch mode."},
            {"type":"Result","text":"Median latency ~85 ms; 8-class accuracy ~92% on internal test set."}
        ],
        "metrics":[{"label":"Latency (median)","value":"~85 ms"},{"label":"Accuracy","value":"~92%"}],
        "tags":{"stack":["TensorFlow","Docker","Streamlit"],"industry":["Computer Vision"],"year":2024,"impact":"High"}
    },
    {
        "id":"sir","title":"SIR Simulator",
        "summary":"Rust simulator for SIR dynamics on synthetic graphs; helps compare intervention policies.",
        "par":[
            {"type":"Problem","text":"Slow Python sim limited policy exploration."},
            {"type":"Action","text":"Parallelized Rust implementation; exposed CLI; wrote simple plotting notebook."},
            {"type":"Result","text":"~4.1× faster than baseline on 50k-node graphs; easier to batch scenarios."}
        ],
        "metrics":[{"label":"Speedup","value":"~4.1×"},{"label":"Max nodes","value":"50k"}],
        "tags":{"stack":["Rust","Graphs"],"industry":["Public Health"],"year":2024,"impact":"Medium"}
    },
]

# Skills and levels (0–5 scale mapped to meters)
SKILLS = {
    "Core":["Python","PyTorch","TensorFlow","Rust","R","SQL","Docker","GitHub"],
    "Data/Cloud":["Tableau","AWS","MongoDB","Firebase"],
    "Product/Design":["Streamlit","Figma","HTML/CSS/JS","Storybook"]
}
SKILL_LEVEL = {
    "Python":5,"PyTorch":4,"TensorFlow":4,"Rust":3,"R":4,"SQL":4,"Docker":4,"GitHub":4,
    "Tableau":4,"AWS":3,"MongoDB":3,"Firebase":3,
    "Streamlit":5,"Figma":4,"HTML/CSS/JS":4,"Storybook":3
}

TESTIMONIALS = [
    {"quote":"Dheer is thoughtful about problem framing and ships clean, testable code.","name":"Prof. M. Patel","role":"Faculty Advisor, Boston University"},
    {"quote":"He took ambiguous research notes and turned them into crisp dashboards our team could use.","name":"R. Mehta","role":"Mentor, Ventura Securities"},
    {"quote":"Balances model quality with pragmatic product decisions—rare in a student.","name":"A. Gomez","role":"PM (mentor), EdTech Hackathon"}
]

RESUME_HISTORY = [
    {"date":"2025-06-15","changes":["First draft of GenomeSage write-up","Added CI to Vision app"]},
    {"date":"2025-07-18","changes":["Refined SMPBED validation protocol","Updated GPA to 3.43"]},
    {"date":"2025-08-05","changes":["Case study page for Vision","Tuned meters and tags"]}
]

STATS = {"years":2, "projects":8, "impact_pct":15}
CONTACT = {"email":"dheer@bu.edu","calendar":"https://calendly.com/"}

# =========================
# Navbar
# =========================
st.markdown("""
<div class="navbar" role="navigation" aria-label="Sections">
  <div class="nav-grid">
    <a href="#top" class="nav-btn" aria-label="Home">💼 Dheer Doshi</a>
    <div class="nav-links" id="toc">
      <a class="nav-btn" href="#about" data-section="about">About</a>
      <a class="nav-btn" href="#experience" data-section="experience">Experience</a>
      <a class="nav-btn" href="#projects" data-section="projects">Projects</a>
      <a class="nav-btn" href="#skills" data-section="skills">Skills</a>
      <a class="nav-btn" href="#testimonials" data-section="testimonials">Testimonials</a>
      <a class="nav-btn" href="#history" data-section="history">Changes</a>
      <a class="nav-btn" href="#contact" data-section="contact">Contact</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# JS: active link, shortcuts, carousel (no Python interpolation)
components.html("""
<script>
(function(){
  const flags = document.getElementById('flags');
  const reduce = flags ? (flags.getAttribute('data-reduce') === 'true') : false;

  const toc = document.getElementById('toc')?.querySelectorAll('a.nav-btn') || [];
  const ids = Array.from(toc).map(a => a.dataset.section);
  function markActive(id){
    toc.forEach(a => a.setAttribute('aria-current', a.dataset.section===id ? 'page':'false'));
  }
  const obs = new IntersectionObserver((entries)=>{
    entries.forEach(e => { if(e.isIntersecting) markActive(e.target.id); });
  }, {rootMargin: "-40% 0px -55% 0px", threshold: 0.01});
  ids.forEach(id => { const el = document.getElementById(id); if (el) obs.observe(el); });

  // Shortcuts
  document.addEventListener('keydown', (e)=>{
    if(e.key === '/'){ e.preventDefault(); const f = document.getElementById('project-search'); if(f) f.focus(); }
    if(e.key === 'g'){ window.__gPress = Date.now(); }
    else if (e.key === 'p' && window.__gPress && Date.now()-window.__gPress<600){
      document.querySelector('a[href="#projects"]')?.click();
    }
  });

  // Simple auto-advance carousel
  const track = document.getElementById('carousel-track');
  if(track){
    let idx = 0; const total = track.children.length; let paused = false;
    track.addEventListener('mouseenter', ()=>paused=true);
    track.addEventListener('mouseleave', ()=>paused=false);
    function step(){
      if(!paused && !reduce){
        idx = (idx+1)%total;
        track.style.transform = 'translateX(' + (-100*idx) + '%)';
      }
      setTimeout(step, 2800);
    }
    step();
    document.getElementById('prev')?.addEventListener('click',()=>{ idx=(idx-1+total)%total; track.style.transform = 'translateX(' + (-100*idx) + '%)'; });
    document.getElementById('next')?.addEventListener('click',()=>{ idx=(idx+1)%total; track.style.transform = 'translateX(' + (-100*idx) + '%)'; });
  }
})();
</script>
""", height=0)

# =========================
# Hero
# =========================
st.markdown('<div id="top"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="hero section" id="about" aria-label="About section">
  <h1>Dheer Doshi</h1>
  <div class="muted" style="margin-bottom:6px;">BS Data Science @ Boston University (GPA 3.43) — Grad May 2027</div>
  <div class="grid" style="align-items:center;">
    <div class="col-8">
      <span class="badge">Open to internships • 2025</span>
      <span class="badge">Boston / Remote</span>
      <span class="badge">US work auth (student)</span>
      <div class="muted" style="margin-top:10px;">
        I build data products end-to-end: clean inputs, measurable models, clear UX. Interests: bio, markets, and tools that reduce cognitive load.
      </div>
      <div style="margin-top:12px;">
        <a class="badge" href="mailto:dheer@bu.edu">✉ Email</a>
        <a class="badge" href="https://calendly.com/" target="_blank">📅 Calendar</a>
      </div>
    </div>
    <div class="col-4">
      <div class="card" aria-label="Stats">
        <div class="section-title">Stats</div>
        <div>🗓️ <strong>2</strong> years hands-on</div>
        <div>📦 <strong>8</strong> projects shipped</div>
        <div>📈 <strong>15%</strong> typical lift on target metrics</div>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# =========================
# Highlights (Scan / Deep)
# =========================
role_map = {r["label"]: r for r in ROLES}
r = role_map[role_choice]
bullets = r["tldr"] if mode else r["deep"]

st.markdown('<section class="section"><div class="card"><div class="section-title">Highlights</div>', unsafe_allow_html=True)
st.markdown("<ul>" + "".join([f"<li>{b}</li>" for b in bullets]) + "</ul>", unsafe_allow_html=True)
st.markdown("</div></section>", unsafe_allow_html=True)

# =========================
# Experience
# =========================
EXPERIENCE = [
    {"company":"Ventura Securities","title":"Senior Research Intern","where":"Mumbai, India","from":"Dec 2024","to":"Present",
     "items":[
         "Built sector screens and simple earnings models in Python; shared weekly notes.",
         "Consolidated macro data (FRED/IMF) into dashboards for portfolio reviews.",
         "Drafted research briefs used by mentors for client updates."
     ]},
    {"company":"Boston University — Projects","title":"Research/Teaching Support (part-time)","where":"Boston, MA","from":"Sep 2023","to":"Dec 2024",
     "items":[
         "Prototyped sequence models for coursework; wrote clean experiment logs.",
         "Supported peers with reproducibility (conda/DVC) and viz (Tableau).",
         "Presented findings in short, decision-oriented formats."
     ]},
]
st.markdown('<section class="section" id="experience" aria-label="Experience section">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="section-title">Experience</div>', unsafe_allow_html=True)
for e in EXPERIENCE:
    st.markdown(
        f"<div tabindex='0' style='outline:none; margin-bottom:12px;'>"
        f"<strong>{e['title']}</strong> — {e['company']} "
        f"<span class='muted'>({e['from']} – {e['to']}) • {e['where']}</span>"
        f"<ul>{''.join([f'<li>{x}</li>' for x in e['items']])}</ul>"
        f"</div>",
        unsafe_allow_html=True
    )
st.markdown("</div></section>", unsafe_allow_html=True)

# =========================
# Projects + Filters + Case-study
# =========================
def get_query_params():
    try:
        return st.query_params
    except Exception:
        return st.experimental_get_query_params()

st.markdown('<section class="section" id="projects" aria-label="Projects section">', unsafe_allow_html=True)
left, right = st.columns([2,1])
with right:
    all_skills = sorted({t for p in PROJECTS for t in p["tags"].get("stack", [])})
    all_industries = sorted({t for p in PROJECTS for t in p["tags"].get("industry", [])})
    all_impacts = ["Low","Medium","High"]
    st.text_input("Search", key="project-search", placeholder="Type to filter…", label_visibility="visible")
    f1 = st.multiselect("Filter by skill", options=all_skills)
    f2 = st.multiselect("Filter by industry", options=all_industries)
    f3 = st.multiselect("Filter by impact", options=all_impacts)

with left:
    st.markdown('<div class="card"><div class="section-title">Projects</div>', unsafe_allow_html=True)

    qp = get_query_params() or {}
    case_id = None
    if isinstance(qp, dict):
        val = qp.get("case") or qp.get("case_id")
        if isinstance(val, list):
            case_id = val[0] if val else None
        else:
            case_id = val

    def passes(p):
        if f1 and not set(f1).intersection(p["tags"].get("stack", [])): return False
        if f2 and not set(f2).intersection(p["tags"].get("industry", [])): return False
        if f3 and p["tags"].get("impact") not in f3: return False
        q = st.session_state.get("project-search", "").strip().lower()
        if q and q not in (p["title"] + " " + p["summary"]).lower(): return False
        return True

    if case_id:
        proj = next((p for p in PROJECTS if p["id"] == case_id), None)
        if proj:
            st.markdown(f"<div class='section-title'>{proj['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='muted' style='margin-bottom:8px;'>{proj['summary']}</div>", unsafe_allow_html=True)
            st.markdown("**Problem → Action → Result**")
            for entry in proj["par"]:
                st.markdown(f"- **{entry['type']}:** {entry['text']}")
            st.markdown("**Metrics**")
            st.markdown(" ".join([f"<span class='kpi'>{m['label']}: <strong>{m['value']}</strong></span>" for m in proj["metrics"]]), unsafe_allow_html=True)
            st.link_button("← Back to all projects", "#projects", use_container_width=True)
        else:
            st.info("Case study not found.")
    else:
        featured_ids = set(next((ro["featured"] for ro in ROLES if ro["label"] == role_choice), []))
        visible = [p for p in PROJECTS if passes(p)]
        visible.sort(key=lambda p: (0 if p["id"] in featured_ids else 1, -int(p["tags"]["year"])))
        if not visible:
            st.info("No projects match your current filters.")
        for p in visible:
            stacks = " ".join([f"<span class='badge'>{t}</span>" for t in p["tags"].get("stack",[])])
            inds = " ".join([f"<span class='badge'>{t}</span>" for t in p["tags"].get("industry",[])])
            st.markdown(
                "<div class='proj-card card'>"
                f"<div class='section-title'>{p['title']}</div>"
                f"<div class='muted' style='margin:4px 0 8px 0;'>{p['summary']}</div>"
                f"{stacks}{inds}"
                f"<div style='margin-top:8px;'><a class='badge' href='?case={p['id']}'>Read case study</a></div>"
                "</div>",
                unsafe_allow_html=True
            )

st.markdown("</div>", unsafe_allow_html=True)  # close card (left col)
# Side panel: resume export
with right:
    st.markdown("<div class='card'><div class='section-title'>Resume & Export</div>", unsafe_allow_html=True)
    variant = f"{role_choice} — {'Scan' if mode else 'Deep'}"
    st.write(f"Current variant: **{variant}**")
    st.markdown("Use **Open Print Dialog (PDF)** in the sidebar to save this variant as a PDF (print CSS applied).")
    pdf_path = Path(__file__).parent / "assets" / "resume.pdf"
    if pdf_path.exists():
        st.download_button("Download canonical PDF", data=pdf_path.read_bytes(), file_name="Resume.pdf", mime="application/pdf", use_container_width=True)
    else:
        st.info("Add your base PDF at `assets/resume.pdf` to enable direct download.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)

# =========================
# Skills
# =========================
st.markdown('<section class="section" id="skills" aria-label="Skills section">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="section-title">Skills Matrix</div>', unsafe_allow_html=True)
cols = st.columns(3)
for i, (group, items) in enumerate(SKILLS.items()):
    with cols[i]:
        st.markdown(f"**{group}**")
        for s in items:
            lvl = max(1, min(5, SKILL_LEVEL.get(s, 3)))
            pct = int(lvl/5*100)
            st.markdown(s)
            st.markdown(f"<div class='meter-wrap'><div class='meter-val' style='width:{pct}%;'></div></div>", unsafe_allow_html=True)
st.markdown("</div></section>", unsafe_allow_html=True)

# =========================
# Testimonials carousel
# =========================
st.markdown('<section class="section" id="testimonials" aria-label="Testimonials section">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="section-title">Testimonials</div>', unsafe_allow_html=True)
st.markdown('<div class="carousel"><div class="carousel-track" id="carousel-track">', unsafe_allow_html=True)
for t in TESTIMONIALS:
    st.markdown(
        "<div class='carousel-item'>"
        f"<div style='font-size:1.1rem; font-weight:700;'>“{t['quote']}”</div>"
        f"<div class='muted' style='margin-top:6px;'>— {t['name']}, {t['role']}</div>"
        "</div>",
        unsafe_allow_html=True
    )
st.markdown('</div><div class="carousel-controls"><button id="prev" aria-label="Previous">◀</button><button id="next" aria-label="Next">▶</button></div></div>', unsafe_allow_html=True)
st.markdown('</div></section>', unsafe_allow_html=True)

# =========================
# Resume diff history
# =========================
st.markdown('<section class="section" id="history" aria-label="Changes section">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="section-title">What changed since last month?</div>', unsafe_allow_html=True)
for entry in RESUME_HISTORY:
    with st.expander(entry["date"], expanded=False):
        for c in entry["changes"]:
            st.markdown(f"- {c}")
st.markdown('</div></section>', unsafe_allow_html=True)

# =========================
# Contact + Floating CTA
# =========================
st.markdown('<section class="section" id="contact" aria-label="Contact section">', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="section-title">Contact</div>', unsafe_allow_html=True)
with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Draft Email")
    if submit:
        import urllib.parse as ul
        subject = f"Hello from {name or 'a visitor'} — Resume Site"
        body = f"From: {name}\\nEmail: {email}\\n\\n{message}"
        href = f"mailto:{CONTACT['email']}?subject={ul.quote(subject)}&body={ul.quote(body)}"
        st.markdown(f"[Open email draft]({href})")
st.markdown('</div></section>', unsafe_allow_html=True)

st.markdown(
    f"""
<div class="floating-cta" aria-label="Quick contact">
  <a href="mailto:{CONTACT['email']}">Email</a>
  <a href="{CONTACT['calendar']}" target="_blank">Calendar</a>
</div>
""",
    unsafe_allow_html=True
)

# =========================
# Print CSS
# =========================
st.markdown("""
<style>
@media print {
  .navbar, .floating-cta, [data-testid="stSidebar"], .carousel-controls { display: none !important; }
  .card { box-shadow: none !important; border-color: #000 !important; }
  * { color: #000 !important; background: #fff !important; }
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: .9em; }
  @page { margin: 0.6in; }
}
</style>
""", unsafe_allow_html=True)

# =========================
# Footer
# =========================
st.caption("Modern, a11y-aware, and print-ready. Swap in your assets and links when ready.")
