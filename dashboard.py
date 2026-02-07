import streamlit as st

# --- ULTIMATE PAGE CONFIG ---
st.set_page_config(page_title="Dr. Inayat | Research Hub", layout="wide")

# --- HIGH-END CSS INJECTION ---
st.markdown("""
    <style>
    /* Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

    /* Global Transitions */
    .main { background-color: #0a0e14; color: #e2e8f0; }
    
    /* Navigation Bar Replacement */
    .nav-container {
        display: flex;
        justify-content: space-around;
        background: #111827;
        padding: 1rem;
        border-bottom: 2px solid #b59410;
        margin-bottom: 2rem;
        border-radius: 0 0 15px 15px;
    }

    /* Executive Cards */
    .exec-card {
        background: #1f2937;
        border: 1px solid #374151;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .exec-card:hover {
        border: 1px solid #b59410;
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    /* Typography */
    .hero-text {
        font-family: 'Cinzel', serif;
        color: #b59410;
        font-size: 3.5rem;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-hero {
        font-family: 'Montserrat', sans-serif;
        text-align: center;
        color: #9ca3af;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-size: 0.9rem;
        margin-bottom: 3rem;
    }

    /* Journal Links Styling */
    .journal-btn {
        display: block;
        text-align: center;
        background: #111827;
        color: #b59410 !important;
        border: 1px solid #b59410;
        padding: 12px;
        margin: 10px 0;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .journal-btn:hover {
        background: #b59410;
        color: #111827 !important;
    }

    /* Remove Streamlit default elements */
    header {visibility: hidden;}
    [data-testid="stSidebar"] {background-color: #0a0e14 !important;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAV ---
with st.sidebar:
    st.markdown("<h1 style='color: #b59410; font-family: Cinzel;'>NODE V3</h1>", unsafe_allow_html=True)
    page = st.radio("SELECT DOMAIN", ["Research Overview", "Journal Suites", "Publications", "Scholar Terminal"])
    st.markdown("---")
    st.markdown("### Theoretical Biophysics")

# --- PAGE 1: RESEARCH OVERVIEW ---
if page == "Research Overview":
    st.markdown("<h1 class='hero-text'>DR. INAYAT</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-hero'>Theoretical Biophysics & Stochastic Dynamics</p>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.5, 1])
    
    with col_l:
        st.markdown("""
        <div class='exec-card'>
            <h3 style='color: #b59410;'>Research Framework</h3>
            <p style='line-height: 1.8; color: #d1d5db;'>
                Our research integrates non-equilibrium statistical mechanics with protein synthesis kinetics. 
                By refining the <strong>Totally Asymmetric Simple Exclusion Process (TASEP)</strong>, we bridge 
                the gap between theoretical physics and ribosomal dynamics.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \sigma")
        st.info("Current Milestone: Quantifying elongation rates through ribosome run-off CDF analysis.")

    with col_r:
        st.markdown("""
        <div class='exec-card' style='text-align: center;'>
            <h3 style='color: #b59410;'>Model Visualization</h3>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png' width='100%' style='border-radius: 10px; margin-top: 10px;'>
            <p style='font-size: 0.8rem; margin-top: 10px; color: #9ca3af;'>Particle Exclusion & Hopping Probabilities</p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: JOURNAL SUITES ---
elif page == "Journal Suites":
    st.markdown("<h1 class='hero-text'>JOURNAL SUITES</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-hero'>Global Academic Monitoring</p>", unsafe_allow_html=True)

    def journal_suite(title, links):
        with st.container():
            st.markdown(f"<div class='exec-card'><h3 style='color: #b59410;'>{title}</h3>", unsafe_allow_html=True)
            cols = st.columns(len(links))
            for i, (name, url) in enumerate(links.items()):
                cols[i].markdown(f"<a href='{url}' target='_blank' class='journal-btn'>{name}</a>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    journal_suite("Nature Portfolio", {
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Comms": "https://www.nature.com/ncomms/",
        "Comms Biology": "https://www.nature.com/commsbio/"
    })

    journal_suite("Cell Press & Biophysics", {
        "Cell": "https://www.cell.com/cell/home",
        "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home"
    })

    journal_suite("Physics Excellence", {
        "PRL": "https://journals.aps.org/prl/",
        "PRE": "https://journals.aps.org/pre/",
        "Science": "https://www.science.org/journal/science"
    })

    journal_suite("PNAS & Oxford", {
        "PNAS": "https://www.pnas.org/",
        "Nucleic Acid Res": "https://academic.oup.com/nar",
        "Bioinformatics": "https://academic.oup.com/bioinformatics"
    })

# --- PAGE 3: PUBLICATIONS ---
elif page == "Publications":
    st.markdown("<h1 class='hero-text'>PUBLICATIONS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-hero'>Intellectual Contributions</p>", unsafe_allow_html=True)
    
    papers = [
        ("Modeling Ribosome Run-off via TASEP Dynamics", "Biophysical Journal (2026)", "#"),
        ("Phase Transitions in Co-translational Transport", "Physical Review Letters (2025)", "#"),
        ("Stochastic Flux in Protein Synthesis", "Nature Communications (2024)", "#")
    ]

    for title, cite, link in papers:
        st.markdown(f"""
        <div class='exec-card'>
            <h4 style='margin: 0;'>{title}</h4>
            <p style='color: #b59410; margin: 5px 0;'>{cite}</p>
            <a href='{link}' style='color: #60a5fa; text-decoration: none;'>View DOI Structure →</a>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 4: SCHOLAR TERMINAL ---
elif page == "Scholar Terminal":
    st.markdown("<h1 class='hero-text'>SEARCH TERMINAL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-hero'>Data & Literature Query</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='exec-card'>", unsafe_allow_html=True)
    q = st.text_input("QUERY DATABASE", placeholder="e.g., TASEP KINETICS")
    if q:
        st.link_button(f"EXECUTE SEARCH FOR: {q}", f"https://scholar.google.com/scholar?q={q}")
    st.markdown("</div>", unsafe_allow_html=True)
