import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Theoretical Biophysics Hub", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL AESTHETICS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }

    /* Journal Card Styling */
    .journal-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-top: 4px solid #1a73e8;
        height: 100%;
        transition: transform 0.2s ease;
    }
    .journal-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }
    
    .section-title {
        color: #1e3d59;
        font-weight: 600;
        border-bottom: 2px solid #ddd;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    /* Link Styling */
    .journal-link {
        display: block;
        padding: 8px 0;
        color: #2c3e50;
        text-decoration: none;
        font-size: 0.95rem;
        border-bottom: 1px solid #f0f0f0;
    }
    .journal-link:hover {
        color: #1a73e8;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.title("Research Portal")
    st.markdown("---")
    page = st.radio("Navigation", ["🏠 Home", "📚 Journal Portal", "🎓 Scholar & Search"])
    st.markdown("---")
    st.caption("Theoretical Biophysics | Postdoc Node")

# --- PAGE 1: HOME (PROFESSIONAL RESEARCH FRAMEWORK) ---
if page == "🏠 Home":
    st.title("Research Framework")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='background: white; padding: 30px; border-radius: 15px; border-left: 6px solid #1a73e8;'>
            <h2 style='color: #1e3d59;'>Stochastic Modeling of Ribosome Dynamics</h2>
            <p style='color: #555; line-height: 1.6;'>
                I work in the area of theoritical biophysics, wherein I develop the mathematical and biophysical models to adress the questions related to the biological systems. 
               
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.subheader("Key Theoretical Formulations")
        st.latex(r"J_i = \gamma \rho_i (1 - \rho_{i+1})")
        st.info("Current Objective: Mapping the 50% crossover position in ribosome run-off CDFs.")

    with col2:
        st.subheader("Research Keywords")
        st.button("TASEP Modeling", use_container_width=True)
        st.button("Ribosome Profiling", use_container_width=True)
        st.button("Bayesian Inference", use_container_width=True)
        st.button("Theoretical Biophysics", use_container_width=True)

# --- PAGE 2: JOURNAL PORTAL (THE HUB) ---
elif page == "📚 Journal Portal":
    st.title("Academic Journal Hub")
    st.markdown("Click any journal to open its latest articles in a new tab.")

    # Section 1 & 2: Nature and Cell
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.markdown("""<div class="journal-box">
            <h3 class="section-title">Nature Portfolio</h3>
            <a class="journal-link" href="https://www.nature.com/nphys/" target="_blank">🔗 Nature Physics</a>
            <a class="journal-link" href="https://www.nature.com/ncomms/" target="_blank">🔗 Nature Communications</a>
            <a class="journal-link" href="https://www.nature.com/commsbio/" target="_blank">🔗 Communications Biology</a>
            <a class="journal-link" href="https://www.nature.com/nmeth/" target="_blank">🔗 Nature Methods</a>
            <a class="journal-link" href="https://www.nature.com/nstructmb/" target="_blank">🔗 Nature Structural & Molecular Biology</a>
        </div>""", unsafe_allow_html=True)

    with row1_col2:
        st.markdown("""<div class="journal-box" style="border-top-color: #e11d48;">
            <h3 class="section-title">Cell Press</h3>
            <a class="journal-link" href="https://www.cell.com/cell/home" target="_blank">🔗 Cell</a>
            <a class="journal-link" href="https://www.cell.com/molecular-cell/home" target="_blank">🔗 Molecular Cell</a>
            <a class="journal-link" href="https://www.cell.com/cell-reports/home" target="_blank">🔗 Cell Reports</a>
            <a class="journal-link" href="https://www.cell.com/biophysj/home" target="_blank">🔗 Biophysical Journal</a>
            <a class="journal-link" href="https://www.cell.com/structure/home" target="_blank">🔗 Structure</a>
        </div>""", unsafe_allow_html=True)

    st.write("")

    # Section 3 & 4: PNAS and Oxford
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.markdown("""<div class="journal-box" style="border-top-color: #10b981;">
            <h3 class="section-title">National Academy & Multi-Disc</h3>
            <a class="journal-link" href="https://www.pnas.org/" target="_blank">🔗 PNAS (Proceedings of the National Academy of Sciences)</a>
            <a class="journal-link" href="https://elifesciences.org/" target="_blank">🔗 eLife</a>
            <a class="journal-link" href="https://journals.plos.org/ploscompbiol/" target="_blank">🔗 PLOS Computational Biology</a>
        </div>""", unsafe_allow_html=True)

    with row2_col2:
        st.markdown("""<div class="journal-box" style="border-top-color: #8b5cf6;">
            <h3 class="section-title">Oxford Journals</h3>
            <a class="journal-link" href="https://academic.oup.com/nar" target="_blank">🔗 Nucleic Acids Research (NAR)</a>
            <a class="journal-link" href="https://academic.oup.com/bioinformatics" target="_blank">🔗 Bioinformatics</a>
            <a class="journal-link" href="https://academic.oup.com/mbe" target="_blank">🔗 Molecular Biology and Evolution</a>
        </div>""", unsafe_allow_html=True)

    st.write("")

    # Section 5 & 6: Science and APS
    row3_col1, row3_col2 = st.columns(2)

    with row3_col1:
        st.markdown("""<div class="journal-box" style="border-top-color: #f59e0b;">
            <h3 class="section-title">Science Family</h3>
            <a class="journal-link" href="https://www.science.org/journal/science" target="_blank">🔗 Science</a>
            <a class="journal-link" href="https://www.science.org/journal/sciadv" target="_blank">🔗 Science Advances</a>
            <a class="journal-link" href="https://www.science.org/journal/scisignal" target="_blank">🔗 Science Signaling</a>
        </div>""", unsafe_allow_html=True)

    with row3_col2:
        st.markdown("""<div class="journal-box" style="border-top-color: #3b82f6;">
            <h3 class="section-title">APS Journals (Physics)</h3>
            <a class="journal-link" href="https://journals.aps.org/prl/" target="_blank">🔗 Physical Review Letters (PRL)</a>
            <a class="journal-link" href="https://journals.aps.org/pre/" target="_blank">🔗 Physical Review E (PRE)</a>
            <a class="journal-link" href="https://journals.aps.org/prx/" target="_blank">🔗 Physical Review X (PRX)</a>
            <a class="journal-link" href="https://arxiv.org/list/q-bio/new" target="_blank">🔗 arXiv: Quantitative Biology</a>
        </div>""", unsafe_allow_html=True)

# --- PAGE 3: SCHOLAR & SEARCH ---
elif page == "🎓 Scholar & Search":
    st.title("Academic Search")
    
    st.markdown("### Google Scholar Search")
    query = st.text_input("Enter keywords (e.g., 'TASEP ribosome kinetics')")
    if query:
        scholar_url = f"https://scholar.google.com/scholar?q={query.replace(' ', '+')}"
        st.link_button(f"Search Scholar for '{query}'", scholar_url)
    
    st.write("---")
    st.markdown("### Quick Access Tools")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("Go to Google Scholar Profile", "https://scholar.google.com/")
    with c2:
        st.link_button("UniProt Knowledgebase", "https://www.uniprot.org/")
    with c3:
        st.link_button("Protein Data Bank (PDB)", "https://www.rcsb.org/")
