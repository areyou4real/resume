import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Dheer Doshi — Interactive Resume",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def inject_theme(theme: str):
    if theme == "light":
        bg = "#ffffff"
        text = "#0f172a"
        card = "#f1f5f9"
        accent = "#0ea5e9"
        mute = "#475569"
    else:
        bg = "#0b1020"
        text = "#e2e8f0"
        card = "#111836"
        accent = "#22d3ee"
        mute = "#94a3b8"

    st.markdown(f"""
        <style>
            :root {{
                --bg: {bg};
                --text: {text};
                --card: {card};
                --accent: {accent};
                --mute: {mute};
            }}
            html, body, [class*="css"] {{
                background-color: var(--bg) !important;
                color: var(--text) !important;
                font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial, "Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
            }}
            .hero {{
                padding: 28px 24px;
                border-radius: 16px;
                background: linear-gradient(145deg, var(--card), rgba(34,211,238,0.07));
                border: 1px solid rgba(148,163,184,0.2);
                box-shadow: 0 6px 24px rgba(0,0,0,0.25);
            }}
            .chip {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 6px 12px;
                margin-right: 8px;
                margin-bottom: 8px;
                border-radius: 999px;
                background: rgba(34,211,238,0.12);
                border: 1px solid rgba(34,211,238,0.35);
                color: var(--text);
                font-size: 0.9rem;
                text-decoration: none;
            }}
            .card {{
                background: var(--card);
                border-radius: 16px;
                padding: 16px 18px;
                border: 1px solid rgba(148,163,184,0.18);
            }}
            .muted {{
                color: var(--mute);
                font-size: 0.95rem;
            }}
            .kpi {{
                display: inline-block;
                padding: 8px 10px;
                border-radius: 10px;
                border: 1px dashed rgba(148,163,184,0.4);
                margin-right: 10px;
                margin-bottom: 10px;
                font-size: 0.9rem;
            }}
            .badge {{
                display:inline-block;
                padding:4px 8px;
                font-size:0.8rem;
                border-radius:8px;
                background:rgba(148,163,184,0.2);
                margin-right:8px;
                margin-bottom:8px;
            }}
            .section-title {{
                font-size: 1.3rem;
                font-weight: 700;
                margin: 0 0 6px 0;
            }}
        </style>
    """, unsafe_allow_html=True)

inject_theme(st.session_state.theme)

with st.sidebar:
    st.write("🎨 **Theme**")
    mode = st.toggle("Light mode", value=(st.session_state.theme == "light"))
    st.session_state.theme = "light" if mode else "dark"
    inject_theme(st.session_state.theme)

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

LEADERSHIP = [
    {"role": "Director, Oxford MUN", "impact": "Led 2,000+ delegate sessions; digital briefing innovations."},
    {"role": "Director, TEDx Singhania", "impact": "Exceeded sponsorship targets; record virtual attendance."},
    {"role": "Editor-in-Chief, IRIS Magazine", "impact": "Revamped with digital edition & global partnerships."},
    {"role": "Head of Technical, Concinnity 21", "impact": "Live stream & AV ops for 1,000+ attendees; raised $30k."},
    {"role": "PIT-UN Volunteer", "impact": "Orchestrated logistics enabling cross-sector collaboration."},
]

SKILLS = {
    "Core": ["Python", "PyTorch", "TensorFlow", "Rust", "R", "SQL", "GitHub", "Docker"],
    "Data & Cloud": ["Tableau", "AWS", "Firebase", "MongoDB"],
    "Apps & Video": ["Streamlit", "HTML5", "JavaScript", "OBS Studio", "Adobe Suite", "Final Cut Pro"],
    "Other": ["CPR Certified"]
}

LANGUAGES = ["English", "Hindi", "Marathi", "Gujarati", "Spanish (Elementary)"]
INTERESTS = ["Debate", "History (Greek & Roman)", "Soccer", "Travel", "Event Planning"]

def download_button_from_file(file_path: Path, label: str):
    try:
        bytes_data = file_path.read_bytes()
        st.download_button(label, data=bytes_data, file_name=file_path.name, mime="application/pdf", use_container_width=True)
    except Exception:
        st.info("Resume not bundled yet. Add your PDF to ./assets/resume.pdf")

def mailto_link(to, subject, body):
    import urllib.parse as ul
    href = f"mailto:{to}?subject={ul.quote(subject)}&body={ul.quote(body)}"
    return href

def tag_badges(tags):
    if not tags: return ""
    return " ".join([f"<span class='badge'>{t}</span>" for t in tags])

st.markdown(
    f"""
    <div class="hero">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;">
            <div style="flex:1 1 520px">
                <div style="font-size:2.1rem;font-weight:800;margin-bottom:6px;">{PROFILE['name']}</div>
                <div class="muted" style="margin-bottom:12px;">{PROFILE['role']}</div>
                <div class="muted">📍 {PROFILE['location']}</div>
            </div>
            <div style="flex:0 0 auto;min-width:320px;">
                <a class="chip" href="tel:{PROFILE['phone']}" target="_blank">📞 {PROFILE['phone']}</a>
                <a class="chip" href="mailto:{PROFILE['email']}" target="_blank">✉️ {PROFILE['email']}</a>
                {"".join([f'<a class="chip" href="{url}" target="_blank">🔗 {name}</a>' for name, url in PROFILE["links"].items()])}
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(" ")

tab_about, tab_exp, tab_edu, tab_projects, tab_skills, tab_lead, tab_resume, tab_contact = st.tabs([
    "About", "Experience", "Education", "Projects", "Skills", "Leadership", "Resume", "Contact"
])

with tab_about:
    st.subheader("About")
    st.write(
        "Data science student blending research rigor with product sense. "
        "Comfortable across ML pipelines, deployment, and high-clarity communication."
    )
    st.write("I enjoy building tools that make complex ideas usable for people.")

with tab_exp:
    st.subheader("Experience")
    for exp in EXPERIENCE:
        with st.expander(f"**{exp['title']}** — {exp['company']} ({exp['start']} – {exp['end']}) — {exp['location']}", expanded=False):
            st.markdown(tag_badges(exp.get("tags")), unsafe_allow_html=True)
            for b in exp["bullets"]:
                st.markdown(f"- {b}")
            if exp.get("kpis"):
                st.markdown("**Focus areas:**")
                st.markdown("".join([f"<span class='kpi'>{k}</span>" for k in exp["kpis"]]), unsafe_allow_html=True)

with tab_edu:
    st.subheader("Education")
    for ed in EDUCATION:
        st.markdown(f"**{ed['school']}** — {ed['program']}  •  GPA: {ed['gpa']}  •  Graduation: {ed['grad']}")
        st.markdown("**Highlights:**")
        for h in ed["highlights"]:
            st.markdown(f"- {h}")

with tab_projects:
    left, right = st.columns([2,1])
    with right:
        all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
        sel = st.multiselect("Filter by tags", options=all_tags, default=[])
        q = st.text_input("Search", placeholder="Search projects...").strip().lower()
    with left:
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
            with st.container():
                st.markdown(f"### {p['name']}")
                st.markdown(p["summary"])
                st.markdown(tag_badges(p["tags"]), unsafe_allow_html=True)
                st.divider()

with tab_skills:
    st.subheader("Skills Matrix")
    # If your Streamlit version supports st.pills, this provides a nice multi-select UI.
    # Otherwise, you can replace with st.multiselect.
    selected = st.pills("Highlight", options=[s for grp in SKILLS.values() for s in grp], selection_mode="multi") if hasattr(st, "pills") else st.multiselect("Highlight", [s for grp in SKILLS.values() for s in grp])
    cols = st.columns(2)
    groups = list(SKILLS.items())
    for i, (grp, items) in enumerate(groups):
        with cols[i % 2]:
            st.markdown(f"<div class='section-title'>{grp}</div>", unsafe_allow_html=True)
            line = []
            for s in items:
                if selected and s in selected:
                    line.append(f"<span class='badge' style='border:1px solid var(--accent);background:rgba(34,211,238,0.18)'>{s}</span>")
                else:
                    line.append(f"<span class='badge'>{s}</span>")
            st.markdown(" ".join(line), unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown("**Languages**")
    st.markdown(" ".join([f"<span class='badge'>{l}</span>" for l in LANGUAGES]), unsafe_allow_html=True)
    st.markdown("**Interests**")
    st.markdown(" ".join([f"<span class='badge'>{i}</span>" for i in INTERESTS]), unsafe_allow_html=True)

with tab_lead:
    st.subheader("Leadership & Engagement")
    for item in LEADERSHIP:
        with st.expander(item["role"], expanded=False):
            st.write(item["impact"])

with tab_resume:
    st.subheader("Resume")
    pdf_path = Path(__file__).parent / "assets" / "resume.pdf"
    st.write("Download a copy of my resume:")
    download_button_from_file(pdf_path, "📄 Download resume (PDF)")
    if pdf_path.exists():
        base64_pdf = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.info("Embed will appear once resume.pdf is placed in assets.")

with tab_contact:
    st.subheader("Contact")
    with st.form("contact_form", clear_on_submit=False):
        name = st.text_input("Your name")
        sender = st.text_input("Your email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Draft Email")
        if submitted:
            subject = f"Hello from {name or 'a visitor'} — Interactive Resume"
            body = f"From: {name}\nEmail: {sender}\n\n{message}"
            import urllib.parse as ul
            href = f"mailto:{PROFILE['email']}?subject={ul.quote(subject)}&body={ul.quote(body)}"
            st.markdown(f"[Open email draft]({href})")

st.caption("Built with ❤️ in Streamlit")
