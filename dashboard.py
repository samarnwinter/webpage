import streamlit as st

# --- SETTINGS ---
st.set_page_config(page_title="Inayat | Research Node", layout="wide")

# --- ADVANCED UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: white; border: 1px solid #ddd; }
    .stButton>button:hover { border: 1px solid #1a73e8; color: #1a73e8; }
    
    .publication-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1a73e8;
        margin-bottom: 15px;
    }
    .journal-section {
        background: rgba(255, 255, 255, 0.7);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Main Menu")
    page = st.radio("Navigate", ["🏠 Home & Research", "📚 Journal Portal", "🎓 Publications", "🎓 Scholar Search"])
    st.markdown("---")
    st.info("Theoretical Biophysics Node v2.1")

# --- PAGE 1: HOME ---
if page == "🏠 Home & Research":
    st.title("Theoretical Biophysics Framework")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Stochastic Modeling of Ribosome Dynamics")
        st.write("""
        This research node integrates non-equilibrium statistical mechanics with 
        high-throughput sequencing data. We utilize **TASEP** models to decode the 
        relationship between mRNA sequence features and translation efficiency.
        """)
        st.latex(r"J_i = k_{on} \rho_0(1-\rho_1)")
        
        st.subheader("Current Project: Ribosome Run-off")
        st.write("Measuring per-gene elongation rates by calculating the CDF of ribosome footprints.")

    with col2:
        st.markdown("### Visual Gallery")
        # Placeholder for your simulation plot
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png", 
                 caption="TASEP Simulation: Particle Density Flow")

# --- PAGE 2: JOURNAL PORTAL ---
elif page == "📚 Journal Portal":
    st.title("Global Journal Directory")
    
    # Using the Section approach we discussed
    def journal_card(title, links, color):
        st.markdown(f"### {title}")
        with st.container():
            for name, url in links.items():
                st.link_button(f"🔗 {name}", url)
            st.write("")

    col_a, col_b = st.columns(2)
    
    with col_a:
        journal_card("Nature Portfolio", {
            "Nature Physics": "https://www.nature.com/nphys/",
            "Nature Communications": "https://www.nature.com/ncomms/",
            "Communications Biology": "https://www.nature.com/commsbio/"
        }, "#1a73e8")
        
        journal_card("Cell Press", {
            "Molecular Cell": "https://www.cell.com/molecular-cell/home",
            "Biophysical Journal": "https://www.cell.com/biophysj/home",
            "Cell Reports": "https://www.cell.com/cell-reports/home"
        }, "#e11d48")

    with col_b:
        journal_card("Physics & Science", {
            "Physical Review Letters (PRL)": "https://journals.aps.org/prl/",
            "Physical Review E (PRE)": "https://journals.aps.org/pre/",
            "Science Advances": "https://www.science.org/journal/sciadv"
        }, "#3b82f6")
        
        journal_card("Oxford & PNAS", {
            "Nucleic Acids Research (NAR)": "https://academic.oup.com/nar",
            "PNAS": "https://www.pnas.org/",
            "Bioinformatics": "https://academic.oup.com/bioinformatics"
        }, "#8b5cf6")

# --- PAGE 3: PUBLICATIONS ---
elif page == "🎓 Publications":
    st.title("Selected Publications")
    
    # Template for your papers
    def paper_entry(title, journal, year, link):
        st.markdown(f"""
        <div class="publication-box">
            <strong>{title}</strong><br>
            <em style='color: #666;'>{journal} ({year})</em><br>
            <a href="{link}" target="_blank" style='color: #1a73e8; text-decoration: none;'>View Publication →</a>
        </div>
        """, unsafe_allow_html=True)

    paper_entry("Modeling Ribosome Run-off via TASEP Dynamics", "Biophysical Journal", "2025", "#")
    paper_entry("Stochastic Sorting of Proteins during Co-translational Transport", "Physical Review Letters", "2024", "#")

# --- PAGE 4: SCHOLAR SEARCH ---
elif page == "🎓 Scholar Search":
    st.title("Search & Discovery")
    query = st.text_input("Search Google Scholar for papers:")
    if query:
        st.link_button("Launch Scholar Search", f"https://scholar.google.com/scholar?q={query}")
