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
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;700&family=Inter:wght@300;400;600;800&display=swap');

    :root {
        --bg-primary: #FAFAFA;
        --accent-gold: #C5A059;
        --text-deep: #1A202C;
        --text-slate: #4A5568;
        --glass-white: rgba(255, 255, 255, 0.95);
        --card-shadow: 0 10px 30px rgba(0,0,0,0.04);
    }

    /* Main Container Cleanup */
    .stApp { background-color: var(--bg-primary); }
    [data-testid="stHeader"] { background: transparent; }
    
    /* Hero Section */
    .hero-container {
        position: relative;
        padding: 8rem 2rem;
        background-image: linear-gradient(rgba(250, 250, 250, 0.1), rgba(250, 250, 250, 0.9)), 
                          url('https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border-radius: 40px;
        text-align: center;
        margin-bottom: 3rem;
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 4.5rem;
        color: var(--text-deep);
        letter-spacing: -0.04em;
        line-height: 1;
        margin-bottom: 1rem;
    }

    .hero-sub {
        font-family: 'DM Sans', sans-serif;
        color: var(--accent-gold);
        letter-spacing: 0.3em;
        text-transform: uppercase;
        font-weight: 600;
        font-size: 0.9rem;
    }

    /* Bento Grid Card */
    .bento-card {
        background: white;
        padding: 2.5rem;
        border-radius: 32px;
        box-shadow: var(--card-shadow);
        border: 1px solid #F1F1F1;
        height: 100%;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    
    .bento-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.06);
        border-color: var(--accent-gold);
    }

    /* Partitions & Labels */
    .section-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: var(--accent-gold);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
        display: block;
    }

    /* Sidebar and Navigation */
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF !important; 
        border-right: 1px solid #EEE; 
    }
    
    /* Custom Sidebar Title */
    .sidebar-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 800; 
        font-size: 1.5rem; 
        padding: 1.5rem 0; 
        color: var(--text-deep); 
        text-align: center;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Publication Styling */
    .pub-box {
        background: white; 
        padding: 2.5rem; 
        border-radius: 28px; 
        margin-bottom: 1.5rem; 
        border: 1px solid #F1F1F1; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.02);
        transition: border-color 0.3s ease;
    }
    .pub-box:hover {
        border-color: var(--accent-gold);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & UTILITIES ---
with st.sidebar:
    st.markdown("<div class='sidebar-title'>INAYAT NODE</div>", unsafe_allow_html=True)
    
    # Navigation Tabs via selectbox
    page = st.selectbox(
        "WORKSPACE NAVIGATION", 
        ["Home: Identity", "Archive: Literature", "Selected Works", "Terminal: Tools"],
        index=0
    )
    
    st.markdown("---")
    
    # Premium Weather Widget
    st.markdown("### 🌤 Environmental Data")
    weather_code = """
    <div style="background: white; padding: 15px; border-radius: 20px; border: 1px solid #EEE;">
    <a class="weatherwidget-io" href="https://forecast7.com/en/40k71n74k01/new-york/" data-label_1="LAB LOCALE" data-label_2="METRICS" data-font="Roboto" data-icons="Climacons Animated" data-theme="pure" >METEOROLOGICAL DATA</a>
    <script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    </script>
    </div>
    """
    st.components.v1.html(weather_code, height=150)
    
    st.markdown("---")
    st.caption("Theoretical Biophysics | Postdoc")

# --- PAGE 1: HOME ---
if page == "Home: Identity":
    # Hero Partition
    st.markdown("""
        <div class="hero-container">
            <span class="hero-sub">The Interface of Physics & Biology</span>
            <div class="hero-title">Theoretical<br>Biophysics</div>
        </div>
    """, unsafe_allow_html=True)

    # Bento Grid Layout
    col1, col2 = st.columns([2, 1], gap="medium")

    with col1:
        st.markdown("""
            <div class="bento-card">
                <span class="section-label">Philosophical Framework</span>
                <h2 style="margin-top:0;">Rational Derivation of Biological Function</h2>
                <p style="color: var(--text-slate); line-height: 1.8; font-size: 1.1rem;">
                    Biology often presents as a series of disparate phenomena; our work seeks the underlying physical ruleset 
                    that unifies these observations. We treat the cellular environment as a non-equilibrium system where 
                    stochasticity is not merely noise, but a fundamental driver of regulatory logic. 
                    By applying rigorous statistical mechanics to translation machinery and chromatin structure, 
                    we move from descriptive observation to predictive theory.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="bento-card">
                <span class="section-label">Active Research</span>
                <h3 style="margin-top:0;">Molecular Transport</h3>
                <p style="font-size: 0.95rem; color: var(--text-slate);">
                    Investigation into how protein synthesis parameters dictate the efficiency of ribosome exchange 
                    factors, specifically focusing on the NatA complex under proteotoxic stress.
                </p>
                <hr style="border: 0; border-top: 1px solid #EEE; margin: 1.5rem 0;">
                <code style="color: var(--accent-gold); font-weight: 700;">STATUS: PRE-PRINT PHASE</code>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4, col5 = st.columns([1, 1, 1], gap="medium")
    
    with col3:
        st.markdown("""<div class="bento-card">
            <span class="section-label">Core Equation</span>
            <div style="padding: 1rem 0;">""" , unsafe_allow_html=True)
        st.latex(r"\dot{P} = \mathbb{L}P")
        st.markdown("""<p style="font-size: 0.8rem; color: #999; margin-top:10px;">Operator dynamics for stochastic state transitions.</p></div>""", unsafe_allow_html=True)
        
    with col4:
        st.markdown("""<div class="bento-card">
            <span class="section-label">Lab Schedule</span>
            <p style="font-size: 0.9rem; margin-bottom: 5px;"><strong>Mon:</strong> Data Synthesis</p>
            <p style="font-size: 0.9rem; margin-bottom: 5px;"><strong>Wed:</strong> Collaborative Sync</p>
            <p style="font-size: 0.9rem;"><strong>Fri:</strong> Manuscript Review</p>
        </div>""", unsafe_allow_html=True)
        
    with col5:
        st.markdown("""<div class="bento-card">
            <span class="section-label">Connectivity</span>
            <a href="#" style="text-decoration:none; color: var(--text-deep); font-weight:600; display:block; margin-bottom:10px;">→ ResearchGate Profile</a>
            <a href="#" style="text-decoration:none; color: var(--text-deep); font-weight:600; display:block;">→ ORCID Identity</a>
        </div>""", unsafe_allow_html=True)

# --- PAGE 2: LITERATURE ---
elif page == "Archive: Literature":
    st.markdown("<h1 style='font-size: 3rem; font-weight: 800;'>Archive Repository</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--text-slate); margin-bottom: 3rem;'>Segregated intelligence from top-tier scientific publishers.</p>", unsafe_allow_html=True)

    def journal_box(title, items):
        st.markdown(f"""<div style='background: white; border-radius: 24px; padding: 2rem; border: 1px solid #EEE; margin-bottom: 2rem;'>
            <h4 style='color: var(--accent-gold); margin-bottom: 1.5rem;'>{title}</h4>""", unsafe_allow_html=True)
        cols = st.columns(4)
        for i, (name, url) in enumerate(items.items()):
            cols[i%4].link_button(name, url, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    journal_box("Nature & Science Portfolios", {
        "Nature": "https://nature.com", "Nature Physics": "https://nature.com/nphys",
        "Nature Comms": "https://nature.com/ncomms", "Science": "https://science.org",
        "Science Adv": "https://science.org/sciadv", "Scientific Reports": "https://nature.com/srep"
    })

    journal_box("Cell Press & Biophysics", {
        "Cell": "https://cell.com", "Molecular Cell": "https://cell.com/molecular-cell",
        "Biophysical Journal": "https://cell.com/biophysj", "Structure": "https://cell.com/structure"
    })
    
    journal_box("Meta Search Platforms", {
        "Google Scholar": "https://scholar.google.com", "PubMed": "https://pubmed.ncbi.nlm.nih.gov",
        "ArXiv (q-bio)": "https://arxiv.org", "BioRxiv": "https://biorxiv.org"
    })

# --- PAGE 3: BIBLIOGRAPHY ---
elif page == "Selected Works":
    st.markdown("<h1 style='font-size: 3rem; font-weight: 800;'>Selected Works</h1>", unsafe_allow_html=True)
    
    publications = [
        {"y": "2025", "t": "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", "j": "Molecular Cell 85 (24), 4562-4574"},
        {"y": "2024", "t": "Understanding the regulation of protein synthesis under stress conditions", "j": "Biophysical Journal 123 (20), 3627-3639"},
        {"y": "2023", "t": "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters", "j": "Biophysical Reports 3 (4)"}
    ]

    for p in publications:
        st.markdown(f"""
            <div class="pub-box">
                <span style="color: var(--accent-gold); font-weight: 800; font-size: 0.8rem;">{p['y']}</span>
                <h3 style="margin: 0.5rem 0; font-weight: 700;">{p['t']}</h3>
                <p style="color: var(--text-slate); margin:0;">Published in <span style="font-weight: 600;">{p['j']}</span></p>
            </div>
        """, unsafe_allow_html=True)

# --- PAGE 4: TERMINAL ---
elif page == "Terminal: Tools":
    st.markdown("<h1 style='font-size: 3rem; font-weight: 800;'>Discovery Terminal</h1>", unsafe_allow_html=True)
    
    st.markdown("""<div class="bento-card">
        <h3>Repository Query</h3>
        <p>A unified interface for searching quantitative biology and physics repositories.</p>
    </div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    query = st.text_input("ENTER SEARCH PARAMETERS", placeholder="e.g. 'Ribosome dynamics'")
    
    if query:
        st.link_button(f"Search Scholar for: {query}", f"https://scholar.google.com/scholar?q={query}")

# --- GLOBAL FOOTER ---
st.markdown("""
    <div style="text-align: center; padding: 4rem 0; color: #BBB; font-size: 0.8rem;">
        &copy; 2026 INAYAT LAB | THEORETICAL BIOPHYSICS | NODE 01
    </div>
""", unsafe_allow_html=True)
