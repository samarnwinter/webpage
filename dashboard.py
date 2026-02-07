import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Inayat | Theoretical Biophysics Node", layout="wide")

# --- CUSTOM CSS: THE "STUNNING" OVERHAUL ---
st.markdown("""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Global Transitions */
    * { transition: all 0.3s ease-in-out; }

    /* Main Background: Subtle Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #f8fafc, #f1f5f9);
    }

    /* Sidebar Styling: Minimalist */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Typography */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        color: #0f172a;
        letter-spacing: -0.02em;
    }
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #1e293b;
    }

    /* Custom Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(226, 232, 240, 0.8);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        border: 1px solid #3b82f6;
    }

    /* Publication Box */
    .pub-entry {
        padding: 1.5rem;
        border-bottom: 1px solid #f1f5f9;
    }
    .pub-entry:last-child { border-bottom: none; }
    .pub-tag {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        color: #3b82f6;
        letter-spacing: 0.05em;
    }

    /* Professional Button Styling */
    div.stButton > button {
        background-color: #ffffff;
        color: #1e293b;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        font-weight: 500;
        height: 3.5rem;
    }
    div.stButton > button:hover {
        background-color: #0f172a;
        color: #ffffff;
        border: 1px solid #0f172a;
    }
    
    /* Remove default Streamlit header for cleaner look */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>INAYAT</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>THEORETICAL BIOPHYSICS</p>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("EXPLORE", ["Perspective", "Journal Archive", "Publications", "Discovery Tool"])
    st.markdown("---")
    st.caption("Postdoc Research Node • 2026")

# --- PAGE 1: HOME (PERSPECTIVE) ---
if page == "Perspective":
    st.markdown("<h1 class='main-title'>Theoretical Research <br>In Systems Biology</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.6, 1])
    
    with col1:
        st.markdown("""
        <div class='glass-card'>
            <p style='font-size: 1.2rem; line-height: 1.8; color: #475569;'>
                My research program focuses on the <strong>stochastic thermodynamics of protein synthesis</strong>. 
                By utilizing the Totally Asymmetric Simple Exclusion Process (TASEP), we bridge the gap between 
                fundamental physics and the complex regulatory landscape of the cell.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Current Theoretical Focus")
        st.write("Quantitative mapping of ribosome density and flux-limitations in the cytoplasm.")
        st.latex(r"J(\rho) = v_{max} \cdot \rho(1 - \rho)")
        
    with col2:
        st.markdown("<div style='margin-top: 1rem;'>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png", 
                 caption="Non-equilibrium steady state density profiles.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: JOURNAL ARCHIVE ---
elif page == "Journal Archive":
    st.markdown("<h1 class='main-title'>Journal Archive</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; margin-bottom: 2rem;'>Global literature portal for rapid journal access.</p>", unsafe_allow_html=True)

    def journal_grid(title, icon, journals):
        st.markdown(f"### {icon} {title}")
        cols = st.columns(len(journals))
        for i, (name, url) in enumerate(journals.items()):
            cols[i].link_button(name, url)
        st.markdown("<br>", unsafe_allow_html=True)

    journal_grid("Nature Portfolio", "🧬", {
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Comms": "https://www.nature.com/ncomms/",
        "Comms Biology": "https://www.nature.com/commsbio/"
    })

    journal_grid("Cell Press", "🧫", {
        "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home",
        "Cell Reports": "https://www.cell.com/cell-reports/home"
    })

    journal_grid("Physics & Science", "⚛️", {
        "PRL": "https://journals.aps.org/prl/",
        "PRE": "https://journals.aps.org/pre/",
        "Science Adv": "https://www.science.org/journal/sciadv"
    })

# --- PAGE 3: PUBLICATIONS ---
elif page == "Publications":
    st.markdown("<h1 class='main-title'>Selected Works</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    def render_paper(tag, title, info, link):
        st.markdown(f"""
        <div class='pub-entry'>
            <span class='pub-tag'>{tag}</span>
            <h4 style='margin: 0.5rem 0;'>{title}</h4>
            <p style='color: #64748b; font-size: 0.9rem;'>{info}</p>
            <a href='{link}' style='color: #3b82f6; text-decoration: none; font-size: 0.8rem; font-weight: 600;'>DOI ACCESS →</a>
        </div>
        """, unsafe_allow_html=True)

    render_paper("Physics of Life", "Stochastic Modeling of Ribosome Run-off Dynamics", "Biophysical Journal (2025) • Lead Researcher", "#")
    render_paper("Theoretical Physics", "Non-equilibrium Phase Transitions in Protein Synthesis", "Physical Review Letters (2024)", "#")
    render_paper("Methodology", "Bayesian Parameter Estimation for Elongation Rates", "Nature Methods (2023)", "#")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 4: DISCOVERY TOOL ---
elif page == "Discovery Tool":
    st.markdown("<h1 class='main-title'>Search Engine</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        query = st.text_input("Enter Research Keywords:", placeholder="e.g. TASEP Protein Sorting")
        if query:
            st.link_button("Search Google Scholar", f"https://scholar.google.com/scholar?q={query}")
        st.markdown("</div>", unsafe_allow_html=True)
