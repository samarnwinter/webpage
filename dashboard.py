import streamlit as st
import feedparser
import pandas as pd

# --- CONFIGURATION & SESSION STATE ---
JOURNALS = {
    "Nature": "https://www.nature.com/nature.rss",
    "Physical Review Letters": "https://feeds.aps.org/rss/recent/prl.xml",
    "Biophysical Journal": "https://www.cell.com/biophysj/current.rss",
    "arXiv: Quantitative Biology": "https://arxiv.org/rss/q-bio"
}

# Keywords to highlight in your field
KEYWORDS = ["TASEP", "Ribosome", "Translation", "Biophysics", "Kinetics"]

st.set_page_config(page_title="Theoretical Biophysics Research Hub", layout="wide")

# --- CUSTOM THEMING ---
st.markdown("""
    <style>
    .reportview-container { background: #f0f2f6; }
    .main { font-family: 'Times New Roman', Times, serif; }
    .highlight { background-color: #fff3cd; padding: 2px 5px; border-radius: 3px; border: 1px solid #ffeeba; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.title("Research Portal")
    page = st.radio("Navigation", ["Overview", "Journal Dashboard", "Private Lab Notes"])
    st.markdown("---")
    st.caption("Status: Active")

# --- PAGE 1: OVERVIEW (The 'Book' Introduction) ---
if page == "Overview":
    st.title("Research Framework")
    st.subheader("Theoretical Modeling of Protein Synthesis")
    
    st.markdown("""
    This platform serves as a centralized node for investigating the stochastic processes 
    governing mRNA translation. Current theoretical efforts focus on:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**1. Ribosome Dynamics (TASEP)**")
        st.latex(r"J = \rho(1-\rho)")
        st.write("Modeling the totally asymmetric simple exclusion process to determine per-gene elongation rates.")
    
    with col2:
        st.write("**2. Co-translational Sorting**")
        st.write("Integrating binding/unbinding kinetics with elongation rates.")

# --- PAGE 2: JOURNAL DASHBOARD ---
elif page == "Journal Dashboard":
    st.title("Literature Monitor")
    
    col_list, col_viewer = st.columns([1, 2])
    
    with col_list:
        st.info("Consolidated Feed")
        selected_journal = st.selectbox("Select Journal Source", list(JOURNALS.keys()))
        feed = feedparser.parse(JOURNALS[selected_journal])
        
        for entry in feed.entries[:12]:
            # Highlight logic
            is_relevant = any(kw.lower() in entry.title.lower() for kw in KEYWORDS)
            label = f"⭐ {entry.title}" if is_relevant else entry.title
            
            if st.button(label, key=entry.link, use_container_width=True):
                st.session_state.active_url = entry.link
            st.write("---")

    with col_viewer:
        if 'active_url' in st.session_state:
            st.markdown(f"**Current Article:** {st.session_state.active_url}")
            st.components.v1.iframe(st.session_state.active_url, height=1000, scrolling=True)
        else:
            st.write("Select a publication from the list to initiate the reader.")

# --- PAGE 3: PRIVATE LAB NOTES (Password Protected) ---
elif page == "Private Lab Notes":
    password = st.text_input("Enter Research Credential", type="password")
    if password == "physics2026": # Change this to your preferred password
        st.title("Laboratory Notebook")
        note_entry = st.text_area("Record new derivation or observation:", height=200)
        if st.button("Commit to Log"):
            st.success("Entry logged successfully.")
    elif password:
        st.error("Credential rejected.")