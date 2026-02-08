import streamlit as st
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inayat | Research Node",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LUXURY DESIGN SYSTEM ---
# We use raw strings r""" for all CSS and HTML blocks. 
# This prevents Python from interpreting backslashes as escape sequences.
st.markdown(r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');

    :root {
        --bg-primary: #F8F9FA;
        --accent-gold: #B89150;
        --text-main: #0F172A;
        --text-muted: #475569;
        --card-bg: #FFFFFF;
        --border-subtle: #EDF2F7;
    }

    .stApp { background-color: var(--bg-primary); color: var(--text-main); font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Hero Section */
    .hero-container {
        padding: 6rem 3rem;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.8) 100%),
                    url('https://images.unsplash.com/photo-1501166617713-78894c7482d9?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border-radius: 40px;
        margin-bottom: 2.5rem;
        color: white;
        text-align: left;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .hero-title {
        font-family: 'Instrument Serif', serif;
        font-size: clamp(3rem, 7vw, 5rem);
        line-height: 1.1;
        margin-bottom: 1.5rem;
        color: #FFFFFF;
    }

    .hero-tagline {
        font-size: 0.9rem;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        color: var(--accent-gold);
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Bento Grid Elements */
    .bento-card {
        background: var(--card-bg);
        padding: 2.5rem;
        border-radius: 32px;
        border: 1px solid var(--border-subtle);
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        height: 100%;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .bento-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
        border-color: var(--accent-gold);
    }

    .card-label {
        font-size: 0.7rem;
        font-weight: 700;
        color: var(--accent-gold);
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 1.2rem;
        display: block;
    }

    /* Sidebar Navigation */
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid var(--border-subtle); }
    .sidebar-brand { font-family: 'Instrument Serif', serif; font-size: 2.2rem; padding: 2rem 0; text-align: center; color: var(--text-main); }

    header, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & UTILITIES ---
with st.sidebar:
    st.markdown(r"<div class='sidebar-brand'>Inayat</div>", unsafe_allow_html=True)
    
    # Navigation logic with exact matching strings for the if/elif blocks below
    page = st.selectbox(
        "NAVIGATION", 
        ["Home: Perspective", "Archive: Repository", "Bibliography: Selected", "Terminal: Workspace"],
        index=0
    )
    
    st.markdown("---")
    
    # High-End Weather Integration
    st.markdown(r"### 🌤 Climate Metrics")
    weather_html = r"""
    <div style="background: #F8FAFC; padding: 15px; border-radius: 24px; border: 1px solid #E2E8F0;">
    <a class="weatherwidget-io" href="https://forecast7.com/en/40k71n74k01/new-york/" data-label_1="LAB LOCALE" data-label_2="ATMOSPHERICS" data-font="Open Sans" data-icons="Climacons Animated" data-theme="pure" >WEATHER DATA</a>
    <script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    </script>
    </div>
    """
    st.components.v1.html(weather_html, height=140)
    
    st.markdown("---")
    st.caption("Postdoc Researcher | Theoretical Biophysics")

# --- MAIN CONTENT LOGIC ---
if page == "Home: Perspective":
    # Hero Visual Partition
    st.markdown(r"""
        <div class="hero-container">
            <div class="hero-tagline">Theoretical Biophysics Node</div>
            <div class="hero-title">Nonequilibrium<br>Statistical Physics</div>
        </div>
    """, unsafe_allow_html=True)

    # Main Bento Grid
    c1, c2 = st.columns([1.8, 1], gap="large")

    with c1:
        st.markdown(r"""
            <div class="bento-card">
                <span class="card-label">Research Rationale</span>
                <h2 style="margin-top:0; font-family: 'Instrument Serif', serif; font-size: 2.5rem;">Rationalizing Biological Complexity</h2>
                <p style="color: var(--text-muted); line-height: 1.8; font-size: 1.1rem;">
                    Biological systems are fundamentally dissipative structures maintained far from thermal equilibrium. 
                    Our methodology involves treating intracellular processes—such as translation and chromatin dynamics—as 
                    stochastic trajectories through a complex state-space. By deriving analytical solutions to Master Equations 
                    and utilizing stochastic modeling, we aim to transform qualitative observations of cellular regulation 
                    into a predictive physical framework.
                </p>
                <p style="color: var(--text-muted); line-height: 1.8; font-size: 1.1rem;">
                    The rationale behind this approach is that the seemingly chaotic nature of protein synthesis is actually 
                    governed by rigorous energetic and kinetic constraints. Understanding these constraints allows us to 
                    decode how cells maintain robustness in fluctuating environments.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(r"""
            <div class="bento-card" style="background: #0F172A; color: white;">
                <span class="card-label" style="color: var(--accent-gold);">Operational Focus</span>
                <h3 style="margin-top:0; color: white;">Molecular Architecture</h3>
                <p style="font-size: 0.95rem; color: #94A3B8; line-height: 1.6;">
                    Currently investigating the kinetic barriers of ribosome exchange within the NatA complex. 
                    Analyzing how proteotoxic stress alters the landscape of N-terminal acetylation.
                </p>
                <div style="margin-top: 2rem; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 16px;">
                    <code style="color: var(--accent-gold);">Branch: main/manuscript-v2</code>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(r"<br>", unsafe_allow_html=True)

    # Sub Grid
    g1, g2, g3 = st.columns(3, gap="medium")
    with g1:
        st.markdown(r"""<div class="bento-card">
            <span class="card-label">Foundational Equation</span>
            <div style="padding: 1rem 0; text-align: center;">""", unsafe_allow_html=True)
        st.latex(r"\frac{\partial P}{\partial t} = \mathbb{W} P")
        st.markdown(r"""<small style="color: var(--text-muted);">Probability evolution in discrete state-space.</small></div>""", unsafe_allow_html=True)
    
    with g2:
        st.markdown(r"""<div class="bento-card">
            <span class="card-label">Node Status</span>
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <div style="width: 10px; height: 10px; background: #10B981; border-radius: 50%; margin-right: 10px;"></div>
                <span>Computational Cluster Active</span>
            </div>
            <div style="display: flex; align-items: center;">
                <div style="width: 10px; height: 10px; background: var(--accent-gold); border-radius: 50%; margin-right: 10px;"></div>
                <span>Data Synthesis Pending</span>
            </div>
        </div>""", unsafe_allow_html=True)
        
    with g3:
        st.markdown(r"""<div class="bento-card">
            <span class="card-label">Academic Identity</span>
            <div style="display: grid; gap: 10px;">
                <a href="#" style="text-decoration:none; color: var(--text-main); font-weight:600;">ORCID: Registered</a>
                <a href="#" style="text-decoration:none; color: var(--text-main); font-weight:600;">ResearchGate Profile</a>
            </div>
        </div>""", unsafe_allow_html=True)

elif page == "Archive: Repository":
    st.markdown(r"<h1 style='font-family: Instrument Serif, serif; font-size: 3.5rem;'>Repository Archive</h1>", unsafe_allow_html=True)
    
    def journal_section(title, journals):
        st.markdown(fr"""<div style='background: white; border-radius: 32px; padding: 2.5rem; border: 1px solid var(--border-subtle); margin-bottom: 2rem;'>
            <h3 style='font-family: Instrument Serif, serif; color: var(--text-main); margin-bottom: 2rem;'>{title}</h3>""", unsafe_allow_html=True)
        cols = st.columns(4)
        for i, (name, url) in enumerate(journals.items()):
            cols[i%4].link_button(name, url, use_container_width=True)
        st.markdown(r"</div>", unsafe_allow_html=True)

    journal_section("Nature & Science Portfolios", {
        "Nature": "https://nature.com", "Nature Physics": "https://nature.com/nphys",
        "Nature Comms": "https://nature.com/ncomms", "Science": "https://science.org",
        "Science Adv": "https://science.org/sciadv", "Scientific Reports": "https://nature.com/srep"
    })

    journal_section("Cell Press & Biophysics", {
        "Cell": "https://cell.com", "Molecular Cell": "https://cell.com/molecular-cell",
        "Biophysical Journal": "https://cell.com/biophysj", "Structure": "https://cell.com/structure",
        "Cell Reports": "https://cell.com/cell-reports"
    })

    journal_section("Meta-Intelligence Search", {
        "Google Scholar": "https://scholar.google.com", "PubMed Central": "https://pubmed.ncbi.nlm.nih.gov",
        "arXiv: q-bio": "https://arxiv.org", "bioRxiv": "https://biorxiv.org"
    })

elif page == "Bibliography: Selected":
    st.markdown(r"<h1 style='font-family: Instrument Serif, serif; font-size: 3.5rem;'>Curated Bibliography</h1>", unsafe_allow_html=True)
    
    publications = [
        {"y": "2025", "t": "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", "j": "Molecular Cell 85 (24)"},
        {"y": "2024", "t": "Understanding the regulation of protein synthesis under stress conditions", "j": "Biophysical Journal 123 (20)"},
        {"y": "2023", "t": "Decoding stoichiometric protein synthesis through translation rate parameters", "j": "Biophysical Reports 3 (4)"}
    ]

    for p in publications:
        st.markdown(rf"""
            <div style="background: white; padding: 2.5rem; border-radius: 32px; margin-bottom: 1.5rem; border: 1px solid var(--border-subtle);">
                <span style="color: var(--accent-gold); font-weight: 800; font-size: 0.8rem; letter-spacing: 0.1em;">{p['y']}</span>
                <h3 style="margin: 0.5rem 0; font-weight: 700; color: var(--text-main);">{p['t']}</h3>
                <p style="color: var(--text-muted); margin:0;">Archived in <span style="font-weight: 600; color: var(--text-main);">{p['j']}</span></p>
            </div>
        """, unsafe_allow_html=True)

elif page == "Terminal: Workspace":
    st.markdown(r"<h1 style='font-family: Instrument Serif, serif; font-size: 3.5rem;'>Discovery Terminal</h1>", unsafe_allow_html=True)
    
    st.markdown(r"""<div class="bento-card">
        <span class="card-label">Unified Query Matrix</span>
        <h3>Distributed Repository Search</h3>
        <p style="color: var(--text-muted);">Access open-source datasets and pre-print servers globally.</p>
    </div>""", unsafe_allow_html=True)
    
    st.markdown(r"<br>", unsafe_allow_html=True)
    query = st.text_input("ENTER SEARCH PARAMETERS", placeholder="e.g. 'Stochastic translation initiation'")
    
    if query:
        st.link_button(f"Initiate Search for: {query}", f"https://scholar.google.com/scholar?q={query}")

# --- GLOBAL FOOTER ---
st.markdown(r"""
    <div style="text-align: center; padding: 5rem 0; color: #94A3B8; font-size: 0.75rem; letter-spacing: 0.05em;">
        &copy; 2026 INAYAT NODE | THEORETICAL BIOPHYSICS | OPERATIONAL DEPLOYMENT V.3.2
    </div>
""", unsafe_allow_html=True)
