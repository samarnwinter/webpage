import streamlit as st
import datetime
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inayat | Theoretical Biophysics Node",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LUXURY THEMING & UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    :root {
        --primary-accent: #3b82f6;
        --text-main: #0f172a;
        --text-sub: #64748b;
        --card-bg: #ffffff;
        --sidebar-bg: #f8fafc;
    }

    .stApp { background-color: #ffffff; color: var(--text-main); }
    [data-testid="stSidebar"] { background-color: var(--sidebar-bg) !important; border-right: 1px solid #e2e8f0; }

    /* Typography */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; font-weight: 800; color: var(--text-main); letter-spacing: -0.05em; }
    .hero-title { font-family: 'Playfair Display', serif; font-size: 3.8rem; line-height: 1.1; margin-bottom: 0.5rem; }
    .hero-subtitle { font-family: 'Outfit', sans-serif; font-weight: 300; font-size: 1rem; color: var(--text-sub); letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 3rem; }

    /* Custom Containers */
    .glass-card {
        background: var(--card-bg);
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08);
        border-color: var(--primary-accent);
    }

    /* Publication Styling */
    .pub-row { padding: 1.5rem 0; border-bottom: 1px solid #f1f5f9; }
    .pub-year { font-weight: 800; color: var(--primary-accent); font-size: 0.85rem; margin-bottom: 0.5rem; }
    .pub-title { font-size: 1.15rem; font-weight: 600; color: #1e293b; line-height: 1.4; }
    .pub-meta { font-size: 0.9rem; color: #64748b; margin-top: 0.4rem; font-family: 'Outfit', sans-serif; }

    /* Sidebar Improvements */
    .sidebar-header { font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.2rem; color: #0f172a; margin-bottom: 2rem; }
    
    /* Utility */
    .stButton>button { border-radius: 12px; font-weight: 600; transition: all 0.3s; border: 1px solid #e2e8f0; }
    .stButton>button:hover { background: #0f172a; color: white; border-color: #0f172a; }
    
    header { visibility: hidden; }
    footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<div class='sidebar-header'>INAYAT LAB 01</div>", unsafe_allow_html=True)
    page = st.radio("NAVIGATION", ["Executive Summary", "Journal Repository", "Scientific Bibliography", "Intelligence Terminal"])
    
    st.markdown("---")
    # Interactive Reminders
    st.subheader("📌 Task Monitor")
    st.checkbox("Review NatA Ribosome Draft", value=True)
    st.checkbox("Analyze Chromatin Data")
    st.checkbox("Submit Biophysical Journal Rev.")
    
    st.markdown("---")
    # Quick Weather Widget (Clean Iframe)
    st.markdown("### 🌤 Local Climate")
    weather_html = """<a class="weatherwidget-io" href="https://forecast7.com/en/40k71n74k01/new-york/" data-label_1="LAB LOCATION" data-label_2="WEATHER" data-theme="pure" >LAB WEATHER</a>
    <script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    </script>"""
    st.components.v1.html(weather_html, height=100)

# --- PAGE 1: EXECUTIVE SUMMARY ---
if page == "Executive Summary":
    st.markdown("<h1 class='hero-title'>Theoretical <br>Biophysics Node</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Interdisciplinary Research in Stochastic Dynamics</p>", unsafe_allow_html=True)
    
    l_col, r_col = st.columns([2, 1])
    
    with l_col:
        st.markdown(f"""
        <div class="glass-card">
            <h3>Research Methodology</h3>
            <p style='font-size: 1.1rem; line-height: 1.7; color: #334155;'>
                Our research framework centers on the <strong>rational explanation</strong> of biological phenomena through 
                physical principles. We focus on the stochastic logic of protein synthesis, analyzing how ribosome 
                exchange dynamics and chromatin conformation dictate cellular outcomes. 
            </p>
            <p style='font-size: 1.1rem; line-height: 1.7; color: #334155;'>
                By bridging fundamental physics with molecular biology, we seek to decode the mechanics of 
                gene regulation and translation initiation under various stress landscapes.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Physics Formulation
        st.markdown("### Governing Dynamics")
        st.latex(r"\frac{dP_n(t)}{dt} = \sum_{m} [W_{nm}P_m(t) - W_{mn}P_n(t)]")
        
        st.info("**Current Active Focus:** Investigating the role of HYPK in ribosome exchange of NatA during stress-induced translational reprogramming.")

    with r_col:
        # Mini Google Calendar Integration
        st.markdown("### 📅 Lab Calendar")
        # Note: Replace URL with your actual public calendar link if available
        st.markdown("""<iframe src="https://calendar.google.com/calendar/embed?src=en.usa%23holiday%40group.v.calendar.google.com&ctz=America%2FNew_York" style="border: 0" width="100%" height="300" frameborder="0" scrolling="no"></iframe>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card" style="padding: 1.5rem;">
            <h4>Lab Updates</h4>
            <small style="color: #64748b;">Feb 08, 2026</small>
            <p style="font-size: 0.9rem; margin-top: 0.5rem;">New publication accepted in <i>Molecular Cell</i> regarding NatA acetylation dynamics.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: JOURNAL REPOSITORY ---
elif page == "Journal Repository":
    st.title("Academic Intelligence")
    st.markdown("---")
    
    # Global Search Tools
    c1, c2 = st.columns(2)
    with c1: st.link_button("🌐 Open Google Scholar Profile", "https://scholar.google.com", use_container_width=True)
    with c2: st.link_button("🧬 Search PubMed Database", "https://pubmed.ncbi.nlm.nih.gov/", use_container_width=True)

    def journal_section(title, journals):
        st.subheader(title)
        cols = st.columns(4)
        for i, (name, url) in enumerate(journals.items()):
            cols[i % 4].link_button(name, url, use_container_width=True)
        st.write("")

    # Segregated by Publisher
    journal_section("Nature Portfolio", {
        "Nature": "https://www.nature.com/",
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Methods": "https://www.nature.com/nmeth/",
        "Nature Communications": "https://www.nature.com/ncomms/",
        "Nature Cell Biology": "https://www.nature.com/ncb/",
        "Scientific Reports": "https://www.nature.com/srep/"
    })

    journal_section("Science / AAAS", {
        "Science": "https://www.science.org/journal/science",
        "Science Advances": "https://www.science.org/journal/sciadv",
        "Science Signaling": "https://www.science.org/journal/stke",
        "Science Immunology": "https://www.science.org/journal/sciimmunol"
    })

    journal_section("Cell Press", {
        "Cell": "https://www.cell.com/cell/home",
        "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home",
        "Cell Reports": "https://www.cell.com/cell-reports/home",
        "Structure": "https://www.cell.com/structure/home"
    })

    journal_section("APS & AIP (Physics)", {
        "Physical Review Letters": "https://journals.aps.org/prl/",
        "Physical Review E": "https://journals.aps.org/pre/",
        "J. Chem. Phys.": "https://aip.scitation.org/journal/jcp",
        "Physics Today": "https://physicstoday.scitation.org/journal/pto"
    })

# --- PAGE 3: SCIENTIFIC BIBLIOGRAPHY ---
elif page == "Scientific Bibliography":
    st.title("Peer-Reviewed Works")
    
    publications = [
        {"year": "2025", "title": "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", "authors": "AM Lentzsch, Z Fan, IU Irshad, et al.", "journal": "Molecular Cell 85 (24), 4562-4574"},
        {"year": "2025", "title": "Predicting gene expression changes from chromatin structure modification", "authors": "S Senapati, IU Irshad, AK Sharma, H Kumar", "journal": "npj Systems Biology and Applications 11 (1), 34"},
        {"year": "2024", "title": "Understanding the regulation of protein synthesis under stress conditions", "authors": "IU Irshad, AK Sharma", "journal": "Biophysical Journal 123 (20), 3627-3639"},
        {"year": "2023", "title": "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters", "authors": "IU Irshad, AK Sharma", "journal": "Biophysical Reports 3 (4)"},
        {"year": "2021", "title": "Quantitative modeling of protein synthesis using ribosome profiling data", "authors": "V Yadav, I Ullah Irshad, et al.", "journal": "Frontiers in Molecular Biosciences 8"}
    ]

    for pub in publications:
        st.markdown(f"""
        <div class="pub-row">
            <div class="pub-year">{pub['year']}</div>
            <div class="pub-title">{pub['title']}</div>
            <div class="pub-meta">{pub['authors']} | <em>{pub['journal']}</em></div>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 4: INTELLIGENCE TERMINAL ---
elif page == "Intelligence Terminal":
    st.title("Scientific Discovery Terminal")
    
    st.markdown("""
    <div class="glass-card">
        <h3>Repository Search</h3>
        <p>Cross-reference theoretical models with experimental datasets across open-access repositories.</p>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("ENTER SEARCH PARAMETERS:", placeholder="e.g. 'Ribosome profiling stress response'")
    
    if query:
        st.info(f"Initiating decentralized search for: {query}")
        c1, c2, c3 = st.columns(3)
        with c1: st.link_button("Search arXiv", f"https://arxiv.org/search/?query={query}&searchtype=all")
        with c2: st.link_button("Search bioRxiv", f"https://www.biorxiv.org/search/{query}")
        with c3: st.link_button("Google Scholar", f"https://scholar.google.com/scholar?q={query}")

    st.markdown("---")
    st.subheader("Global Data Access")
    d1, d2, d3 = st.columns(3)
    d1.link_button("RCSB Protein Data Bank", "https://www.rcsb.org/")
    d2.link_button("NCBI Gene Database", "https://www.ncbi.nlm.nih.gov/gene")
    d3.link_button("UniProt Knowledgebase", "https://www.uniprot.org/")

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© 2026 Inayat Lab | Theoretical Biophysics Node | Built with Streamlit</div>", unsafe_allow_html=True)
