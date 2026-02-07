import streamlit as st
import feedparser
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
JOURNALS = {
    "Nature": "https://www.nature.com/nature.rss",
    "Physical Review Letters": "https://feeds.aps.org/rss/recent/prl.xml",
    "Biophysical Journal": "https://www.cell.com/biophysj/current.rss",
    "arXiv: Quantitative Biology": "https://arxiv.org/rss/q-bio"
}
KEYWORDS = ["TASEP", "Ribosome", "Translation", "Kinetics"]

def clean_text(text):
    if not text: return ""
    return BeautifulSoup(text, "html.parser").get_text()

st.set_page_config(page_title="Biophysics Research Node", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Research Portal")
    page = st.radio("Navigation", ["Overview", "📡 Literature Surf", "Private Lab Notes"])

# --- PAGE 1: OVERVIEW ---
if page == "Overview":
    st.title("Research Framework")
    st.markdown("### Stochastic Dynamics in Protein Synthesis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**TASEP Modeling**")
        st.latex(r"J = \rho(1-\rho)")
    with col2:
        st.write("**Kinetics**")
        st.write("Elongation and Sorting Dynamics")

# --- PAGE 2: LITERATURE SURF ---
elif page == "📡 Literature Surf":
    st.title("Literature Monitor")
    
    col_list, col_viewer = st.columns([1, 2])
    
    with col_list:
        selected_journal = st.selectbox("Source", list(JOURNALS.keys()))
        feed = feedparser.parse(JOURNALS[selected_journal])
        
        for entry in feed.entries[:10]:
            # Clean messy HTML from titles
            ctitle = clean_text(entry.title)
            if st.button(ctitle, key=entry.link, use_container_width=True):
                st.session_state.active_url = entry.link
            st.write("---")

    with col_viewer:
        if 'active_url' in st.session_state:
            st.link_button("Open in New Tab", st.session_state.active_url)
            st.components.v1.iframe(st.session_state.active_url, height=800, scrolling=True)

# --- PAGE 3: NOTES ---
elif page == "Private Lab Notes":
    st.title("Laboratory Notebook")
    password = st.text_input("Password", type="password")
    if password == "physics2026":
        st.text_area("Entry")
