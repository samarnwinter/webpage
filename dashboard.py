import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dr. Inayat | Research Hub", layout="wide")

# --- CUSTOM CSS: HIGH-CONTRAST ELITE THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital@1&family=Montserrat:wght@300;600;800&display=swap');

    /* Global Foundation */
    .stApp {
        background-color: #0f172a; /* Deep Navy/Slate Background for the whole page */
        color: #f1f5f9;
    }

    /* Sidebar - High Contrast Black */
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1e293b;
    }

    /* Typography Overhaul */
    h1, h2, h3 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .hero-title {
        font-size: 4rem;
        color: #f8fafc;
        margin-bottom: 0px;
        text-align: center;
    }
    .hero-subtitle {
        font-family: 'Libre+Baskerville', serif;
        font-style: italic;
        font-size: 1.2rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 3rem;
    }

    /* Content Cards - Glassmorphism */
    .content-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 25px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    
    .card-title {
        color: #fbbf24; /* Gold accent */
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(251, 191, 36, 0.3);
        padding-bottom: 10px;
    }

    .card-text {
        color: #e2e8f0; /* Ultra-clear light grey for readability */
        line-height: 1.8;
        font-size: 1.1rem;
    }

    /* Status Bar Styling */
    .status-bar {
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.3);
        color: #7dd3fc;
        padding: 15px 25px;
        border-radius: 12px;
        font-weight: 600;
        margin-top: 20px;
    }

    /* Hide Streamlit infantile elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {
        background-color: transparent;
        color: #fbbf24;
        border: 2px solid #fbbf24;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #fbbf24;
        color: #0f172a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #fbbf24; font-size: 2rem;'>NODE V3</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b;'>Theoretical Biophysics</p>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("SELECT DOMAIN", ["Research Overview", "Journal Suites", "Publications", "Scholar Terminal"])

# --- PAGE 1: RESEARCH OVERVIEW ---
if page == "Research Overview":
    st.markdown("<h1 class='hero-title'>DR. INAYAT</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Theoretical Biophysics & Stochastic Dynamics</p>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.5, 1])
    
    with col_l:
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">Research Framework</div>
            <div class="card-text">
                Our research integrates non-equilibrium statistical mechanics with protein synthesis kinetics. 
                By refining the <strong>Totally Asymmetric Simple Exclusion Process (TASEP)</strong>, we bridge the gap 
                between theoretical physics and ribosomal dynamics. We specialize in mapping 
                stochastic flux and particle density within constrained biological topologies.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \sigma")
        
        st.markdown(f"""
        <div class="status-bar">
            Current Milestone: Quantifying elongation rates through ribosome run-off CDF analysis.
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">Model Visualization</div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png" width="100%" style="border-radius: 12px; opacity: 0.9;">
            <p style="color: #64748b; font-size: 0.8rem; margin-top: 15px; text-align: center;">
                TASEP: Particle Exclusion & Hopping Probabilities
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: JOURNAL SUITES ---
elif page == "Journal Suites":
    st.markdown("<h1 class='hero-title'>LITERATURE PORTAL</h1>", unsafe_allow_html=True)
    
    def journal_section(title, journals):
        st.markdown(f"""<div class='content-card'><div class='card-title'>{title}</div>""", unsafe_allow_html=True)
        cols = st.columns(len(journals))
        for i, (name, url) in enumerate(journals.items()):
            cols[i].link_button(name, url, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    journal_section("Nature Portfolio", {
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Comms": "https://www.nature.com/ncomms/",
        "Comms Biology": "https://www.nature.com/commsbio/"
    })

    journal_section("Cell Press", {
        "Cell": "https://www.cell.com/cell/home",
        "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home"
    })
    
    journal_section("The Physical Societies", {
        "PRL": "https://journals.aps.org/prl/",
        "PRE": "https://journals.aps.org/pre/",
        "Science": "https://www.science.org/journal/science"
    })
