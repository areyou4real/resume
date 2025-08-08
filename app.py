import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# -----------------------------
# Page Config (Light-first)
# -----------------------------
st.set_page_config(
    page_title="Dheer Doshi — Interactive Resume",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Global CSS + Animations + Scroll UX
# -----------------------------
st.markdown("""
<style>
/* Light theme tokens */
:root{
  --bg:#ffffff;
  --text:#0b1220;
  --muted:#475569;
  --card:#f7fafc;
  --border:rgba(2,6,23,0.08);
  --accent:#0ea5e9;
  --accent-soft:#e0f2fe;
  --chip-bg:#eef6ff;
  --chip-br:#bfe0ff;
}

/* Base */
html, body, [class*="css"] {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
  scroll-behavior:smooth;
}

/* Scroll progress bar */
#scroll-progress {
  position: fixed; top: 0; left: 0; height: 4px; width: 0%;
  background: linear-gradient(90deg, #22c55e, #0ea5e9, #a855f7);
  z-index: 10000; border-radius:0 4px 4px 0;
}

/* Top Nav */
.navbar {
  position: sticky; top: 0; z-index: 9999;
  backdrop-filter: saturate(1.2) blur(10px);
  background: rgba(255,255,255,0.75);
  border-bottom:1px solid var(--border);
  padding: 10px 8px; border-radius: 0 0 12px 12px;
}
.nav-grid { display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:space-between; }
.nav-links { display:flex; gap:10px; flex-wrap:wrap; }
.nav-btn {
  border:1px solid var(--border); background:#fff; color:var(--text);
  padding:8px 12px; border-radius:10px; font-weight:600; text-decoration:none; transition: all .2s ease;
}
.nav-btn:hover { transform: translateY(-1px); box-shadow: 0 4px 14px rgba(2,6,23,0.08); border-color:#bae6fd; }

/* Hero */
.hero {
  padding: 28px 24px; margin: 8px 0 16px 0;
  border-radius: 20px; position: relative; overflow:hidden;
  background: radial-gradient(1200px 600px at 5% -10%, #e7f7ff 0%, transparent 50%), 
              radial-gradient(900px 500px at 95% 10%, #f6e8ff 0%, transparent 55%),
              var(--card);
  border: 1px solid var(--border);
  box-shadow: 0 10px 30px rgba(2,6,23,0.06);
  animation: floatIn .6s ease-out both;
}
@keyframes floatIn { from {opacity:0; transform: translateY(10px)} to {opacity:1; transform: translateY(0)} }

.hero h1 { font-size:2.15rem; margin:0 0 6px 0; line-height:1.1; }
.hero .sub { color: var(--muted); margin-bottom:10px; }
.hero .meta { color: var(--muted); }

/* Chips */
.chip {
  display:inline-flex; align-items:center; gap:8px;
  padding:6px 12px; margin:6px 6px 0 0; border-radius:999px;
  background: var(--chip-bg); border:1px solid var(--chip-br);
  font-size:0.92rem; text-decoration:none; color:var(--text);
  transition: transform .18s ease, box-shadow .18s ease;
}
.chip:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(2,6,23,0.08); }

/* Cards */
.card {
  background:#fff; border:1px solid var(--border); border-radius:18px;
  padding:16px 18px; box-shadow: 0 10px 24px rgba(2,6,23,0.05);
}
.section-title { font-weight:800; font-size:1.1rem; letter-spacing:.2px; margin:0 0 8px 0; }
.muted { color: var(--muted); }

/* Badges / KPIs */
.badge {
  display:inline-block; padding:5px 10px; border-radius:999px;
  background: var(--accent-soft); color:#075985; font-weight:600; font-size:.82rem;
  margin:0 8px 8px 0; border:1px solid #bae6fd;
}
.kpi { display:inline-block; padding:6px 10px; border-radius:10px; border:1px dashed #cbd5e1; margin:0 10px 10px 0; }

/* Reveal on scroll */
.reveal { opacity:0; transform: translateY(12px); transition: all .6s ease; }
.reveal.visible { opacity:1; transform: translateY(0); }

/* Floating Back-To-Top */
#backToTop {
  position: fixed; right: 18px; bottom: 24px; z-index: 9999;
  border: none; background: #111827; color: #fff; border-radius: 999px;
  padding: 12px 14px; cursor: pointer; box-shadow: 0 8px 24px rgba(17,24,39,.25);
  display:none; transition: transform .2s ease, opacity .2s ease;
}
#backToTop:hover { transform: translateY(-2px); }

/* Section anchor spacing */
.section { scroll-margin-top: 90px; }
hr { border:none; border-top:1px solid var(--border); margin: 8px 0 16px 0; }
</style>
<div id="scroll-progress"></div>
""", unsafe_allow_html=True)

# Inject the JS with components.html (so it actually runs)
components.html("""
<script>
(function(){
  const progress = document.getElementById('scroll-progress') || (function(){
    const p = document.createElement('div'); p.id='scroll-progress'; document.body.appendChild(p); return p;
  })();
  const backBtn = document.createElement('button');
  backBtn.id = 'backToTop';
  backBtn.innerText = '↑';
  document.body.appendChild(backBtn);

  function onScroll(){
    const h = document.documentElement;
    const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
    progress.style.width = scrolled + '%';
    backBtn.style.display = h.scrollTop > 300 ? 'block' : 'none';
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  backBtn.addEventListener('click', () => window.scrollTo({top:0, behavior:'smooth'}));

  // Reveal on scroll
  const obs = new IntersectionObserver((entries)=>{
    entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, {threshold: 0.08});
  setTimeout(()=>{ document.querySelectorAll('.reveal').forEach(el=>obs.observe(el)); }, 100);
})();
</script>
""", height=0)

# -----------------------------
# Data (edit to personalize)
# -----------------------------
PROFILE = {
    "name": "Dheer Doshi",
    "role": "Data Science @ Boston University • Research & Product-minded",
    "location": "Boston, MA • Open to remote/hybrid",
    "email": "dheer@bu.edu",
    "phone": "(857) 565 6018",
    "links": {
        "LinkedIn": "https://www.linkedin.com/",
        "GitHub": "https://github.com/",
        "Portfolio": "https://example.com/"
    }
}

EXPERIENCE = [
    {
        "company": "Ventura Securities",
        "location": "Mumbai, India",
        "title": "Senior Research Intern",
        "start": "Dec 2024",
        "end": "Present",
        "bullets": [
            "Delivered equity & macro research informing portfolio strategy and executive decisions.",
            "Synthesized complex market data into investor-facing insights & thought leadership.",
            "Built financial models to forecast earnings, assess risk, and source opportunities."
        ],
        "tags": ["Finance Research", "Modeling", "Macro", "Python"],
        "kpis": ["Earnings models", "Risk frameworks", "Sector deep dives"]
    },
]

EDUCATION = [
    {
        "school": "Boston University",
        "program": "BS in Data Science",
        "gpa": "3.43",
        "grad": "May 2027",
        "highlights": [
            "GenomeSage: sequence modeling in PyTorch to predict mutations; Tableau viz for interpretability.",
            "SMPBED: Python/R models for S&P 500 trend forecasting using macro indicators; Tableau viz.",
            "Disease Simulation (Rust): SIR model on synthetic graphs; centrality-based risk analysis.",
            "Vision: Real-time image classification web app (TensorFlow, Streamlit, Docker).",
            "GitOps & CI with GitHub; streamlined deployment across projects."
        ]
    }
]

PROJECTS = [
    {"name": "GenomeSage", "summary": "Sequence modeling to predict genetic mutations; model explainability dashboards.", "tags": ["PyTorch", "Bioinformatics", "Tableau", "Data Viz"]},
    {"name": "SMPBED", "summary": "Macroeconomic indicators → predictive models for S&P 500 trends.", "tags": ["Python", "R", "Finance", "Time Series"]},
    {"name": "Disease Simulation", "summary": "Rust-based SIR simulations on synthetic graphs; centrality analysis for risk.", "tags": ["Rust", "Graphs", "Simulation"]},
    {"name": "Vision Web App", "summary": "Real-time image classification with TensorFlow + Streamlit; Dockerized.", "tags": ["TensorFlow", "Streamlit", "Docker", "MLOps"]},
]

SKILLS = {
    "Core": ["Python", "PyTorch", "TensorFlow", "Rust", "R", "SQL", "GitHub", "Docker"],
    "Data & Cloud": ["Tableau", "AWS", "Firebase", "MongoDB"],
    "Apps & Video": ["Streamlit", "HTML5", "JavaScript", "OBS Studio", "Adobe Suite", "Final Cut Pro"],
    "Other": ["CPR Certified"]
}

LEADERSHIP = [
    {"role": "Director, Oxford MUN", "impact": "Led 2,000+ delegate sessions; digital briefing innovations."},
    {"role": "Director, TEDx Singhania", "impact": "Exceeded sponsorship targets; record virtual attendance."},
    {"role": "Editor-in-Chief, IRIS Magazine", "impact": "Revamped with digital edition & global partnerships."},
    {"role": "Head of Technical, Concinnity 21", "impact": "Live stream & AV ops for 1,000+ attendees; raised $30k."},
    {"role": "PIT-UN Volunteer", "impact": "Orchestrated logistics enabling cross-sector collaboration."},
]

LANGUAGES = ["English", "Hindi", "Marathi", "Gujarati", "Spanish (Elementary)"]
INTERESTS = ["Debate", "History (Greek & Roman)", "Soccer", "Travel", "Event Planning"]

# -----------------------------
# Helpers
# -----------------------------
def tag_badges(tags):
    if not tags: return ""
    return " ".join([f"<span class='badge'>{t}</span>" for t in tags])

def mailto_link(to, subject, body):
    import urllib.parse as ul
    return f"mailto:{to}?subject={ul.quote(subject)}&body={ul.quote(body)}"

def download_button_from_file(file_path: Path, label: str):
    try:
        bytes_data = file_path.read_bytes()
        st.download_button(label, data=bytes_data, file_name=file_path.name, mime="application/pdf", use_container_width=True)
    except Exception:
        st.info("Resume not bundled yet. Add your PDF to ./assets/resume.pdf")

# -----------------------------
# Sticky Top Nav
# -----------------------------
st.markdown("""
<div class="navbar">
  <div class="nav-grid">
    <div><strong>💼 Dheer Doshi</strong></div>
    <div class="nav-links">
      <a class="nav-btn" href="#about">About</a>
      <a class="nav-btn" href="#experience">Experience</a>
      <a class="nav-btn" href="#education">Education</a>
      <a class="nav-btn" href="#projects">Projects</a>
      <a class="nav-btn" href="#skills">Skills</a>
      <a class="nav-btn" href="#leadership">Leadership</a>
      <a class="nav-btn" href="#resume">Resume</a>
      <a class="nav-btn" href="#contact">Contact</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Hero + About
# -----------------------------
st.markdown(f"""
<div class="hero reveal section" id="about">
  <h1>{PROFILE['name']}</h1>
  <div class="sub">{PROFILE['role']}</div>
  <div class="meta">📍 {PROFILE['location']}</div>
  <div style="margin-top:12px;">
    <a class="chip" href="tel:{PROFILE['phone']}" target="_blank">📞 {PROFILE['phone']}</a>
    <a class="chip" href="mailto:{PROFILE['email']}" target="_blank">✉️ {PROFILE['email']}</a>
    {"".join([f'<a class="chip" href="{url}" target="_blank">🔗 {name}</a>' for name, url in PROFILE["links"].items()])}
  </div>
</div>
<div class="reveal" style="margin-top:6px;"><div class="card">
  <div class="section-title">About</div>
  <div class="muted">Data science student blending research rigor with product sense. Comfortable across ML pipelines, deployment, and high-clarity communication. I enjoy building tools that make complex ideas usable for people.</div>
</div></div>
""", unsafe_allow_html=True)

# -----------------------------
# Experience
# -----------------------------
st.markdown("<div id='experience' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card'><div class='section-title'>Experience</div></div>", unsafe_allow_html=True)
for exp in EXPERIENCE:
    st.markdown(f"""
    <div class="reveal card" style="margin-top:10px;">
        <div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <div><strong>{exp['title']}</strong> — {exp['company']}</div>
            <div class="muted">{exp['start']} – {exp['end']} • {exp['location']}</div>
        </div>
        <div style="margin:8px 0 4px 0;">{tag_badges(exp.get('tags'))}</div>
        <ul style="margin:6px 0 0 18px;">
          {''.join([f'<li>{b}</li>' for b in exp['bullets']])}
        </ul>
        <div style="margin-top:10px;">{"".join([f"<span class='kpi'>{k}</span>" for k in exp.get("kpis", [])])}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Education
# -----------------------------
st.markdown("<div id='education' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card' style='margin-top:14px;'><div class='section-title'>Education</div>", unsafe_allow_html=True)
for ed in EDUCATION:
    st.markdown(f"""
    <div class="muted"><strong>{ed['school']}</strong> — {ed['program']} • GPA: {ed['gpa']} • Graduation: {ed['grad']}</div>
    <div style="height:6px;"></div>
    <div><strong>Highlights:</strong></div>
    <ul style="margin:6px 0 0 18px;">{''.join([f'<li>{h}</li>' for h in ed['highlights']])}</ul>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Projects (search + tags)
# -----------------------------
st.markdown("<div id='projects' class='section'></div>", unsafe_allow_html=True)
left, right = st.columns([2,1])  # removed vertical_alignment for compatibility
with right:
    all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    sel = st.multiselect("🔎 Filter by tags", options=all_tags, placeholder="Select tags...")
    q = st.text_input("Search projects", placeholder="Type to filter...").strip().lower()

with left:
    st.markdown("<div class='reveal card'><div class='section-title'>Projects</div></div>", unsafe_allow_html=True)
    visible = []
    for p in PROJECTS:
        if sel and not any(t in p["tags"] for t in sel):
            continue
        if q and q not in (p["name"] + " " + p["summary"]).lower():
            continue
        visible.append(p)

    if not visible:
        st.info("No projects match your current filters.")
    for p in visible:
        st.markdown(f"""
        <div class="reveal card" style="margin-top:10px;">
            <div style="font-weight:700; font-size:1.05rem;">{p['name']}</div>
            <div class="muted" style="margin:4px 0 8px 0;">{p['summary']}</div>
            {tag_badges(p['tags'])}
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# Skills
# -----------------------------
st.markdown("<div id='skills' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card' style='margin-top:14px;'><div class='section-title'>Skills Matrix</div>", unsafe_allow_html=True)

all_skills = [s for grp in SKILLS.values() for s in grp]
if hasattr(st, "pills"):
    selected = st.pills("Highlight", options=all_skills, selection_mode="multi")
else:
    selected = st.multiselect("Highlight", options=all_skills, placeholder="Pick skills to highlight")

c1, c2 = st.columns(2)
groups = list(SKILLS.items())
for i, (grp, items) in enumerate(groups):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(f"<div class='section-title' style='margin-top:6px;'>{grp}</div>", unsafe_allow_html=True)
        chips = []
        for s in items:
            if selected and s in selected:
                chips.append(f"<span class='badge' style='box-shadow:0 0 0 2px #bae6fd inset'>{s}</span>")
            else:
                chips.append(f"<span class='badge'>{s}</span>")
        st.markdown(" ".join(chips), unsafe_allow_html=True)

st.markdown("""
<hr/>
<div class="muted"><strong>Languages:</strong> English • Hindi • Marathi • Gujarati • Spanish (Elementary)</div>
<div class="muted" style="margin-top:4px;"><strong>Interests:</strong> Debate • History (Greek & Roman) • Soccer • Travel • Event Planning</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Leadership
# -----------------------------
st.markdown("<div id='leadership' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card' style='margin-top:14px;'><div class='section-title'>Leadership & Engagement</div>", unsafe_allow_html=True)
for item in LEADERSHIP:
    with st.expander(item["role"], expanded=False):
        st.write(item["impact"])
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Resume (Download + Embed)
# -----------------------------
st.markdown("<div id='resume' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card' style='margin-top:14px;'><div class='section-title'>Resume</div>", unsafe_allow_html=True)

def download_button_from_file(file_path: Path, label: str):
    try:
        bytes_data = file_path.read_bytes()
        st.download_button(label, data=bytes_data, file_name=file_path.name, mime="application/pdf", use_container_width=True)
    except Exception:
        st.info("Resume not bundled yet. Add your PDF to ./assets/resume.pdf")

pdf_path = Path(__file__).parent / "assets" / "resume.pdf"
st.write("Download a copy of my resume:")
download_button_from_file(pdf_path, "📄 Download resume (PDF)")

if pdf_path.exists():
    base64_pdf = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
    st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>', unsafe_allow_html=True)
else:
    st.info("Embed will appear once resume.pdf is placed in assets.")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Contact
# -----------------------------
st.markdown("<div id='contact' class='section'></div>", unsafe_allow_html=True)
st.markdown("<div class='reveal card' style='margin-top:14px;'><div class='section-title'>Contact</div>", unsafe_allow_html=True)
with st.form("contact_form", clear_on_submit=False):
    name = st.text_input("Your name")
    sender = st.text_input("Your email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Draft Email")
    if submitted:
        subject = f"Hello from {name or 'a visitor'} — Interactive Resume"
        body = f"From: {name}\nEmail: {sender}\n\n{message}"
        st.markdown(f"[Open email draft]({mailto_link(PROFILE['email'], subject, body)})")
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.caption("Made with 🤍 — Light theme, animations, smooth scroll, and interactive filters.")
