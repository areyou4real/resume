import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation from URL with error handling
def load_lottieurl(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            st.warning(f"Lottie animation load failed. Status code: {r.status_code}")
            return None
        return r.json()
    except Exception as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None


# Page config
st.set_page_config(page_title="Dheer Doshi | Resume", page_icon="📄", layout="wide")

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("assets/profile.JPG", width=150)
    st.title("Dheer Doshi")
    st.write("📍 Boston, MA / Mumbai, India")
    st.write("📧 dheer@bu.edu")
    st.write("📞 (857) 565 6018")
    st.write("🔗 [LinkedIn](https://www.linkedin.com)")
    st.write("🐙 [GitHub](https://www.github.com)")

# Load Lottie animation (safe fallback)
lottie_resume = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q5pk6p1k.json")

# Intro
st.title("👋 Hi, I'm Dheer Doshi")
st.subheader("Aspiring Data Scientist | Developer | Community Builder")

if lottie_resume:
    st_lottie(lottie_resume, height=300, key="resume")
else:
    st.info("✨ Interactive animation couldn't be loaded. But here's my resume ↓")

# Experience
st.markdown("## 💼 Experience")
st.write("""
**Ventura Securities** – *Senior Research Intern*  
*Dec 2024 – Present | Mumbai, India*  
- Delivered high-impact equity and macroeconomic research.  
- Synthesized market data into investor-facing insights.  
- Built financial models to forecast earnings and assess risk.
""")

# Education
st.markdown("## 🎓 Education")
st.write("""
**Boston University** – BS in Data Science  
*GPA: 3.43 | May 2027*  
- SMPBED: Predictive models for S&P 500 trends in Python/R, visualized in Tableau.  
- Disease Simulation: SIR model in Rust on synthetic graphs.  
- StreamDash: Live dashboard with Streamlit & Docker.  
- MongoSpread: Backend tracking with MongoDB.  
- GitOps: CI/CD via GitHub.  
- PIT-UN: Managed national tech convening logistics.
""")

# Projects / Leadership
st.markdown("## 🚀 Projects & Leadership")
st.write("""
- **TEDx Singhania**: Director – Curated speaker lineup & led record digital reach.  
- **Model UN**: Directed 2000+ delegates using digital tooling.  
- **IRIS Magazine**: Editor in Chief – Launched digital edition & global collabs.  
- **Jupiter Hospital**: Mental health volunteer, inter-hospital campaigns.  
- **Concinnity 21**: Head of Technical – $30K raised for pediatric cancer patients.
""")

# Skills
st.markdown("## 🛠 Technical Skills")
st.write("""
**Languages & Tools**: Python, Rust, SQL, HTML5, JavaScript, MongoDB, R, PyTorch, TensorFlow, Docker, GitHub, AWS, Firebase, Tableau, OBS, Final Cut Pro  
**Frameworks**: Streamlit, Firebase, Adobe Suite  
**Languages**: English, Hindi, Marathi, Gujarati, Spanish (Elementary)
""")

# Resume Download
try:
    with open("assets/Dheer_Doshi_Resume.pdf", "rb") as f:
        st.download_button("📥 Download PDF Resume", f, file_name="Dheer_Doshi_Resume.pdf", mime="application/pdf")
except FileNotFoundError:
    st.warning("Resume PDF not found. Please add it to assets/ as Dheer_Doshi_Resume.pdf")
