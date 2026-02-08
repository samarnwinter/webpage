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

# --- ADVANCED UI ARCHITECTURE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');

    :root {
        --primary-accent: #6366f1;
        --secondary-accent: #a855f7;
        --bg-main: #ffffff;
        --bg-sidebar: #fcfcfd;
        --glass-bg: rgba(255, 255, 255, 0.7);
        --text-heading: #0f172a;
        --text-body: #334155;
        --text-muted: #64748b;
        --border-color: #f1f5f9;
    }

    /* Base Styling */
    .stApp { background-color: var(--bg-main); color: var(--text-body); }
    [data-testid="stSidebar"] { 
        background-color: var(--bg-sidebar) !important; 
        border-right: 1px solid var(--border-color); 
    }

    /* Sophisticated Typography */
    h1, h2, h3 { 
        font-family: 'Plus Jakarta Sans', sans-serif; 
        font-weight: 800; 
        color: var(--text-heading); 
        letter-spacing: -0.04em; 
    }
    
    .hero-title { 
        font-family: 'Instrument Serif', serif; 
        font-size: clamp(3rem, 8vw, 5.5rem); 
        line-height: 0.95; 
        margin-bottom: 0.75rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle { 
        font-family: 'Plus Jakarta Sans', sans-serif; 
        font-weight: 500; 
        font-size: 0.9rem; 
        color: var(--text-muted); 
        letter-spacing: 0.4em; 
        text-transform: uppercase; 
        margin-bottom: 4rem; 
        display: block;
    }

    /* Glassmorphism Containers */
    .premium-card {
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border-color);
        border-radius: 32px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.03);
        transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    
    .premium-card:hover {
        transform: translateY(-8px) scale(1.005);
        box-shadow: 0 30px 60px -12px rgba(15, 23, 42, 0.12);
        border-color: #e2e8f0;
    }

    /* Bibliography Refinement */
    .pub-entry { 
        padding: 2rem 0; 
        border-bottom: 1px solid var(--border-color);
        display: flex;
        gap: 2rem;
    }
    
    .pub-year-badge {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        color: var(--primary-accent);
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        background: #f5f3ff;
        padding: 4px 12px;
        border-radius: 100px;
        height: fit-content;
    }
    
    .pub-content { flex: 1; }
    .pub-title { font-size: 1.25rem; font-weight: 700; color: var(--text-heading); line-height: 1.3; margin-bottom: 0.5rem; }
    .pub-authors { font-size: 0.95rem; color: var(--text-body); margin-bottom: 0.2rem; }
    .pub-journal { font-size: 0.9rem; color: var(--text-muted); font-style: italic; }

    /* Navigation Styling */
    .nav-header { 
        padding: 2rem 1rem; 
        font-weight: 800; 
        letter-spacing: -0.02em; 
        font-size: 1.4rem;
        background: linear-gradient(to right, var(--primary-accent), var(--secondary-accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 16px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        border: 1px solid var(--border-color);
        background: white;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: var(--text-heading);
        color: white !important;
        transform: translateY(-2px);
    }
    
    /* Clean Up Streamlit Defaults */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ARCHITECTURE ---
with st.sidebar:
    st.markdown("<div class='nav-header'>NODE.INAYAT.01</div>", unsafe_allow_html=True)
    page = st.radio("ARCHIVE SECTIONS", 
                    ["Summary & Outlook", "Publication Repositories", "Selected Bibliography", "Research Terminal"],
                    label_visibility="collapsed")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Lab Logistics
    st.markdown("### ⚡ Operational Focus")
    with st.expander("Active Protocols", expanded=True):
        st.checkbox("Analyze HYPK/NatA Cross-link", value=True)
        st.checkbox("Chromatin Modification Synthesis")
        st.checkbox("Peer Review - Biophysics")
    
    st.markdown("---")
    
    # Environmental Context
    st.markdown("### 📍 Node Environment")
    weather_html = """<a class="weatherwidget-io" href="https://forecast7.com/en/40k71n74k01/new-york/" data-label_1="LAB COORDINATES" data-label_2="LOCAL CLIMATE" data-theme="pure" >LAB WEATHER</a>
    <script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    </script>"""
    st.components.v1.html(weather_html, height=120)

# --- PAGE 1: EXECUTIVE SUMMARY ---
if page == "Summary & Outlook":
    st.markdown("<h1 class='hero-title'>Theoretical <br>Biophysics Node</h1>", unsafe_allow_html=True)
    st.markdown("<span class='hero-subtitle'>Interdisciplinary Research in Stochastic Dynamics</span>", unsafe_allow_html=True)
    
    l_col, r_col = st.columns([2, 1], gap="large")
    
    with l_col:
        st.markdown(f"""
        <div class="premium-card">
            <h3 style="margin-top:0;">Theoretical Framework</h3>
            <p style='font-size: 1.15rem; line-height: 1.8; color: var(--text-body);'>
                Our node operates at the nexus of <strong>statistical physics</strong> and <strong>molecular architecture</strong>. 
                We pursue a rational derivation of biological function by modeling cellular processes as complex 
                non-equilibrium systems. Our primary investigative thrust involves the stochastic nature of translation 
                machinery and the spatial logic governing chromatin organization.
            </p>
            <p style='font-size: 1.15rem; line-height: 1.8; color: var(--text-body);'>
                By utilizing rigorous mathematical modeling, we aim to uncover the fundamental rulesets that 
                govern how molecular interactions translate into phenotypic expression under fluctuating 
                environmental stressors.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Master Dynamic Equation")
        st.latex(r"\frac{\partial P(\mathbf{x},t)}{\partial t} = -\sum_i \frac{\partial}{\partial x_i} [A_i(\mathbf{x},t)P(\mathbf{x},t)] + \frac{1}{2} \sum_{i,j} \frac{\partial^2}{\partial x_i \partial x_j} [B_{ij}(\mathbf{x},t)P(\mathbf{x},t)]")
        
        st.info("💡 **Key Insight:** Current investigations suggest that ribosome exchange rates are a critical bottleneck in protein acetylation efficiency.")

    with r_col:
        st.markdown("### 📅 Scheduling")
        st.markdown("""<iframe src="https://calendar.google.com/calendar/embed?src=en.usa%23holiday%40group.v.calendar.google.com&ctz=America%2FNew_York" style="border: 1px solid #f1f5f9; border-radius:24px;" width="100%" height="320" frameborder="0" scrolling="no"></iframe>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="premium-card" style="padding: 1.5rem; border-left: 4px solid var(--primary-accent);">
            <h4 style="margin:0;">Node Dispatch</h4>
            <small style="color: var(--text-muted);">REF: FEB-2026-08</small>
            <p style="font-size: 0.95rem; margin-top: 0.8rem; line-height: 1.5;">
                <strong>Accepted:</strong> "Molecular Cell" publication regarding NatA dynamics. Preparing supplementary data for the archival repository.
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: PUBLICATION REPOSITORIES ---
elif page == "Publication Repositories":
    st.markdown("<h1 style='font-size: 3rem;'>Intelligence Repositories</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Global Access Points
    c1, c2 = st.columns(2)
    with c1: st.link_button("📜 Google Scholar Dashboard", "https://scholar.google.com", use_container_width=True)
    with c2: st.link_button("🧪 PubMed Intelligence", "https://pubmed.ncbi.nlm.nih.gov/", use_container_width=True)

    def journal_grid(title, icon, journals):
        st.markdown(f"### {icon} {title}")
        cols = st.columns(4)
        for i, (name, url) in enumerate(journals.items()):
            cols[i % 4].link_button(name, url, use_container_width=True)
        st.write("<br>", unsafe_allow_html=True)

    journal_grid("Nature Portfolio", "⚛️", {
        "Nature": "https://www.nature.com/", "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Methods": "https://www.nature.com/nmeth/", "Nature Communications": "https://www.nature.com/ncomms/",
        "Scientific Reports": "https://www.nature.com/srep/", "Nat. Struct. Mol. Biol.": "https://www.nature.com/nsmb/"
    })

    journal_grid("Science / AAAS", "🔬", {
        "Science": "https://www.science.org/journal/science", "Science Advances": "https://www.science.org/journal/sciadv",
        "Science Signaling": "https://www.science.org/journal/stke", "Science Immunology": "https://www.science.org/journal/sciimmunol"
    })

    journal_grid("Cell Press", "🧬", {
        "Cell": "https://www.cell.com/cell/home", "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical Journal": "https://www.cell.com/biophysj/home", "Structure": "https://www.cell.com/structure/home"
    })

    journal_grid("Physics & Mathematics", "📐", {
        "Phys. Rev. Lett.": "https://journals.aps.org/prl/", "Phys. Rev. E": "https://journals.aps.org/pre/",
        "J. Chem. Phys.": "https://aip.scitation.org/journal/jcp", "SIAM Review": "https://www.siam.org/publications/journals/siam-review"
    })

# --- PAGE 3: SELECTED BIBLIOGRAPHY ---
elif page == "Selected Bibliography":
    st.markdown("<h1 style='font-size: 3rem;'>Peer-Reviewed Bibliography</h1>", unsafe_allow_html=True)
    
    pubs = [
        {"y": "2025", "t": "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", "a": "AM Lentzsch, Z Fan, IU Irshad, et al.", "j": "Molecular Cell 85 (24), 4562-4574"},
        {"y": "2025", "t": "Predicting gene expression changes from chromatin structure modification", "a": "S Senapati, IU Irshad, AK Sharma, H Kumar", "j": "npj Systems Biology and Applications 11 (1), 34"},
        {"y": "2024", "t": "Understanding the regulation of protein synthesis under stress conditions", "a": "IU Irshad, AK Sharma", "j": "Biophysical Journal 123 (20), 3627-3639"},
        {"y": "2023", "t": "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters", "a": "IU Irshad, AK Sharma", "j": "Biophysical Reports 3 (4)"},
        {"y": "2021", "t": "Quantitative modeling of protein synthesis using ribosome profiling data", "a": "V Yadav, I Ullah Irshad, et al.", "j": "Frontiers in Molecular Biosciences 8"}
    ]

    st.markdown("<div class='premium-card' style='padding-top: 1rem;'>", unsafe_allow_html=True)
    for p in pubs:
        st.markdown(f"""
        <div class="pub-entry">
            <div class="pub-year-badge">{p['y']}</div>
            <div class="pub-content">
                <div class="pub-title">{p['t']}</div>
                <div class="pub-authors">{p['a']}</div>
                <div class="pub-journal">Published in <strong>{p['j']}</strong></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 4: RESEARCH TERMINAL ---
elif page == "Research Terminal":
    st.markdown("<h1 style='font-size: 3rem;'>Research Intelligence</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <h3>Meta-Search Matrix</h3>
        <p>A unified interface for searching quantitative biology and physics repositories.</p>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("QUERY PARAMETERS", placeholder="e.g. 'Chromatin dynamics non-equilibrium physics'")
    
    if query:
        st.write(f"Searching distributed databases for: `{query}`")
        col_a, col_b, col_c = st.columns(3)
        with col_a: st.link_button("arXiv: q-bio", f"https://arxiv.org/search/?query={query}&searchtype=all")
        with col_b: st.link_button("bioRxiv", f"https://www.biorxiv.org/search/{query}")
        with col_c: st.link_button("Scholar Meta", f"https://scholar.google.com/scholar?q={query}")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Data Access Portals")
    d1, d2, d3 = st.columns(3)
    d1.link_button("PDB: Structure Search", "https://www.rcsb.org/", use_container_width=True)
    d2.link_button("NCBI: Genetic Data", "https://www.ncbi.nlm.nih.gov/", use_container_width=True)
    d3.link_button("UniProt: Proteomics", "https://www.uniprot.org/", use_container_width=True)

# --- GLOBAL FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: var(--text-muted); font-size: 0.8rem; border-top: 1px solid var(--border-color); padding-top: 2rem;'>
        INAYAT RESEARCH NODE | THEORETICAL BIOPHYSICS | V.2.5.0
    </div>
""", unsafe_allow_html=True)
