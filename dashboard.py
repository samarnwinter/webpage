import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Inayat | Theoretical Biophysics ", layout="wide")

# --- CUSTOM CSS: MINIMALIST LUXURY ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    .stApp { background-color: #ffffff; color: #1e293b; }
    [data-testid="stSidebar"] { background-color: #f8fafc !important; border-right: 1px solid #e2e8f0; }

    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 900; color: #0f172a; letter-spacing: -1.5px; }
    .hero-title { font-family: 'Playfair Display', serif; font-size: 4.5rem; margin-bottom: 0px; text-align: center; }
    .hero-subtitle { font-family: 'Inter', sans-serif; font-weight: 300; font-size: 1.1rem; color: #64748b; text-align: center; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 4rem; }

    .content-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 40px; margin-bottom: 30px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.03); transition: transform 0.3s ease; }
    .content-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.08); border-color: #3b82f6; }
    
    .pub-box { padding: 25px; border-bottom: 1px solid #f1f5f9; transition: background 0.2s; }
    .pub-box:hover { background-color: #f8fafc; }
    .pub-year { font-size: 0.85rem; font-weight: 800; color: #3b82f6; margin-bottom: 8px; }
    .pub-title { font-size: 1.2rem; font-weight: 700; color: #0f172a; line-height: 1.4; }
    .pub-authors { font-size: 0.95rem; color: #475569; margin-top: 5px; }
    .pub-journal { font-size: 0.95rem; color: #64748b; font-style: italic; margin-top: 3px; }

    .stButton>button { background-color: #ffffff; color: #0f172a; border: 1px solid #e2e8f0; border-radius: 8px; font-weight: 600; }
    .stButton>button:hover { background-color: #0f172a; color: #ffffff; border-color: #0f172a; }
    
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("<br><br><h1 style='font-size: 1.5rem;'>INAYAT NODE</h1>", unsafe_allow_html=True)
    page = st.radio("SELECT DOMAIN", ["Perspective", "Journal Archive", "Selected Works", "Discovery Terminal"])
    st.markdown("---")
    st.caption("Theoretical Biophysics | Postdoc")

# --- PAGE 1: PERSPECTIVE (HOME) ---
if page == "Perspective":
    st.markdown("<h1 class='hero-title'>Biophysics and Computational Biology</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Non-Equilibrium Systems & Stochastic Dynamics</p>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.6, 1])
    with col_l:
        st.markdown("""<div class="content-card"><h3>Research Framework</h3><p style='font-size: 1.15rem; line-height: 1.8;'>
            Our work deciphers the stochastic logic of protein synthesis and gene regulation. 
            By refining <strong>TASEP</strong> models and polymer physics frameworks, we bridge 
            fundamental physics with the mechanics of ribosome exchange and chromatin conformation. 
            </p></div>""", unsafe_allow_html=True)
        st.latex(r"\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \sigma")
        st.markdown("""<div style='background: #f1f5f9; padding: 20px; border-radius: 12px; border-left: 5px solid #0f172a;'>
            <strong>Current Focus:</strong> Investigating NatA ribosome exchange and translation regulation under stress.
            </div>""", unsafe_allow_html=True)
    with col_r:
        st.markdown("<div class='content-card'><h3>Visualization</h3>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png", caption="Stochastic Transport Model")
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: JOURNAL ARCHIVE ---
elif page == "Journal Archive":
    st.title("Academic Archive")
    
    def journal_grid(title, journals):
        st.markdown(f"### {title}")
        cols = st.columns(3)
        for i, (name, url) in enumerate(journals.items()):
            cols[i % 3].link_button(name, url, use_container_width=True)
        st.write("")

    journal_grid("Nature & Science Portfolio", {
        "Nature Physics": "https://www.nature.com/nphys/", "Nature Comms": "https://www.nature.com/ncomms/",
        "Nature Methods": "https://www.nature.com/nmeth/", "Science Advances": "https://www.science.org/journal/sciadv",
        "Scientific Reports": "https://www.nature.com/srep/", "Communications Biology": "https://www.nature.com/commsbio/"
    })

    journal_grid("Cell Press & Biophysics", {
        "Molecular Cell": "https://www.cell.com/molecular-cell/home", "Cell": "https://www.cell.com/cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home", "Biophysical Reports": "https://www.cell.com/biophysical-reports/home",
        "Cell Reports": "https://www.cell.com/cell-reports/home", "Structure": "https://www.cell.com/structure/home"
    })

    journal_grid("Physical Societies & Life Science", {
        "PRL": "https://journals.aps.org/prl/", "PRE": "https://journals.aps.org/pre/",
        "Physical Biology": "https://iopscience.iop.org/journal/1478-3975", "PNAS": "https://www.pnas.org/",
        "Nucleic Acids Research": "https://academic.oup.com/nar", "Bioinformatics": "https://academic.oup.com/bioinformatics"
    })

# --- PAGE 3: SELECTED WORKS ---
elif page == "Selected Works":
    st.title("Selected Bibliography")
    
    def render_pub(year, title, authors, journal):
        st.markdown(f"""
        <div class='pub-box'>
            <div class='pub-year'>{year}</div>
            <div class='pub-title'>{title}</div>
            <div class='pub-authors'>{authors}</div>
            <div class='pub-journal'>{journal}</div>
        </div>
        """, unsafe_allow_html=True)

    render_pub("2025", "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", "AM Lentzsch, Z Fan, IU Irshad, et al.", "Molecular Cell 85 (24), 4562-4574")
    render_pub("2025", "Predicting gene expression changes from chromatin structure modification", "S Senapati, IU Irshad, AK Sharma, H Kumar", "npj Systems Biology and Applications 11 (1), 34")
    render_pub("2025", "Understanding the regulation of protein synthesis in stress conditions", "IU Irshad", "Biophysical Journal 124 (3), 145a-146a")
    render_pub("2024", "Understanding the regulation of protein synthesis under stress conditions", "IU Irshad, AK Sharma", "Biophysical Journal 123 (20), 3627-3639")
    render_pub("2024", "TIR predictor and optimizer: Web-tools for accurate prediction of translation initiation rate", "S Chakarborty, IU Irshad, et al.", "Biotechnology Journal 19 (5)")
    render_pub("2023", "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters", "IU Irshad, AK Sharma", "Biophysical Reports 3 (4)")
    render_pub("2023", "Fundamental insights into the correlation between chromosome configuration and transcription", "S Senapati, IU Irshad, et al.", "Physical Biology 20 (5)")
    render_pub("2021", "Quantitative modeling of protein synthesis using ribosome profiling data", "V Yadav, I Ullah Irshad, et al.", "Frontiers in Molecular Biosciences 8")

# --- PAGE 4: DISCOVERY TERMINAL ---
elif page == "Discovery Terminal":
    st.title("Discovery Terminal")
    st.markdown("""<div class="content-card"><h3>Technical Deep Dive</h3>
        Search across curated physics and biology repositories to bridge theoretical gaps.</div>""", unsafe_allow_html=True)
    
    query = st.text_input("QUERY SCHOLAR DATABASE:", placeholder="e.g. 'ribosome exchange factor NatA'")
    if query:
        st.link_button(f"Search Scholar for: {query}", f"https://scholar.google.com/scholar?q={query}")
    
    st.write("---")
    st.subheader("Specialized Repositories")
    c1, c2, c3 = st.columns(3)
    with c1: st.link_button("arXiv: Quantitative Biology", "https://arxiv.org/list/q-bio/new")
    with c2: st.link_button("bioRxiv: Biophysics", "https://www.biorxiv.org/collection/biophysics")
    with c3: st.link_button("UniProt: Protein Sequences", "https://www.uniprot.org/")
