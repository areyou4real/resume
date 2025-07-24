import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Dheer Doshi | Resume", page_icon="📄", layout="wide")

# Custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("assets/profile.jpg", width=150)
    st.title("Dheer Doshi")
    st.write("📍 Boston, MA / Mumbai, India")
    st.write("📧 dheer@bu.edu")
    st.write("📞 (857) 565 6018")
    st.write("🔗 [LinkedIn](https://www.linkedin.com)")
    st.write("🐙 [GitHub](https://www.github.com)")

# Load animation
lottie_resume = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_cg8ksmnp.json")

# Intro
st.title("👋 Hi, I'm Dheer Doshi")
st.subheader("Aspiring Data Scientist | Developer | Community Builder")

st_lottie(lottie_resume, height=300, key="resume")

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

# Projects / Activities
st.markdown("## 🚀 Projects & Leadership")
st.write("""
- **TEDx Singhania**: Director – Top-tier speaker lineup & record digital reach.  
- **Model UN**: Directed 2000+ delegates using digital tools.  
- **IRIS Magazine**: Editor in Chief – Launched digital edition & global partnerships.  
- **Jupiter Hospital**: Mental health volunteer & inter-hospital outreach.  
- **Concinnity 21**: Head of Technical – $30,000 raised for pediatric cancer.
""")

# Skills
st.markdown("## 🛠 Technical Skills")
st.write("""
**Languages & Tools**: Python, Rust, SQL, HTML5, JavaScript, MongoDB, R, PyTorch, TensorFlow, Docker, GitHub, AWS, Firebase, Tableau, OBS, Final Cut Pro  
**Frameworks**: Streamlit, Firebase, Adobe Suite  
**Languages**: English, Hindi, Marathi, Gujarati, Spanish (Elementary)
""")

# Download Resume
with open("assets/Dheer Doshi Resume.pdf", "rb") as f:
    st.download_button("📥 Download PDF Resume", f, file_name="Dheer_Doshi_Resume.pdf", mime="application/pdf")
