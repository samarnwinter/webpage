import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dr. Inayat | Research Hub", layout="wide")

# --- CUSTOM CSS: MINIMALIST GALLERY THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital@1&family=Inter:wght@300;400;700;900&display=swap');

    /* Global Foundation - Clean Studio White */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
    }

    /* Sidebar - Soft Slate for Contrast */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Typography Overhaul - High Contrast */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        color: #0f172a;
        letter-spacing: -1.5px;
    }
    .hero-title {
        font-size: 4.5rem;
        margin-bottom: 0px;
        text-align: center;
    }
    .hero-subtitle {
        font-family: 'Libre Baskerville', serif;
        font-style: italic;
        font-size: 1.3rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 4rem;
    }

    /* Floating Content Cards */
    .content-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease;
    }
    .content-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.1);
        border-color: #1e293b;
    }
    
    .card-title {
        color: #0f172a;
        font-size: 1.6rem;
        font-weight: 800;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }
    .card-title::before {
        content: "";
        width: 12px;
        height: 12px;
        background-color: #3b82f6; /* Blue accent dot */
        border-radius: 50%;
        margin-right: 15px;
    }

    .card-text {
        color: #334155;
        line-height: 1.8;
        font-size: 1.15rem;
    }

    /* Professional Accents */
    .status-highlight {
        background: #f1f5f9;
        border-left: 5px solid #0f172a;
        padding: 20px 30px;
        border-radius: 0 12px 12px 0;
        font-weight: 500;
        font-size: 1.1rem;
        color: #1e293b;
    }

    /* Hide default Streamlit clutter */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Clean Link Buttons */
    .stButton>button {
        background-color: #ffffff;
        color: #0f172a;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #0f172a;
        color: #ffffff;
        border-color: #0f172a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 1.8rem; color: #0f172a;'>NODE V3</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-weight: 500;'>Theoretical Biophysics</p>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("EXPLORE", ["Perspective", "Journal Archive", "Publications", "Discovery"])

# --- PAGE 1: HOME (PERSPECTIVE) ---
if page == "Perspective":
    st.markdown("<h1 class='hero-title'>DR. INAYAT</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Theoretical Biophysics & Stochastic Dynamics</p>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.6, 1])
    
    with col_l:
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">Research Framework</div>
            <div class="card-text">
                Our research program investigates the non-equilibrium statistical mechanics of 
                protein synthesis. By utilizing <strong>Totally Asymmetric Simple Exclusion Process (TASEP)</strong> 
                modeling, we bridge the gap between theoretical physics and ribosomal dynamics. 
                Our current focus is mapping stochastic flux and particle density within 
                the constrained topologies of the cell.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \sigma")
        
        st.markdown(f"""
        <div class="status-highlight">
            Current Focus: Quantifying per-gene elongation rates through ribosome run-off analysis.
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">Visualization</div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png" width="100%" style="border-radius: 8px; filter: grayscale(100%) contrast(1.2);">
            <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 15px; text-align: center; font-style: italic;">
                TASEP: Stochastic particle-hopping dynamics.
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: JOURNAL ARCHIVE ---
elif page == "Journal Archive":
    st.markdown("<h1 class='hero-title' style='font-size: 3rem;'>LITERATURE</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Global Research Monitor</p>", unsafe_allow_html=True)
    
    def journal_set(title, journals):
        st.markdown(f"""<div class='content-card'><div class='card-title'>{title}</div>""", unsafe_allow_html=True)
        cols = st.columns(len(journals))
        for i, (name, url) in enumerate(journals.items()):
            cols[i].link_button(name, url, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    journal_set("Nature Portfolio", {
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Comms": "https://www.nature.com/ncomms/",
        "Comms Biology": "https://www.nature.com/commsbio/"
    })

    journal_set("The Physical Societies", {
        "PRL": "https://journals.aps.org/prl/",
        "PRE": "https://journals.aps.org/pre/",
        "Science": "https://www.science.org/journal/science"
    })
