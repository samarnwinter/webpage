import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime

# --- SETTINGS & THEME ---
st.set_page_config(page_title="Biophysics Research Node", layout="wide", initial_sidebar_state="expanded")

# --- ADVANCED CSS CUSTOMIZATION ---
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0,0,0,0.1);
    }

    /* Card Styling for Articles */
    .article-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #2e5cb8;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        transition: transform 0.2s ease;
    }
    .article-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Metrics / Badge Styling */
    .badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .badge-relevant { background-color: #ffd700; color: #000; }
    .badge-physics { background-color: #e1f5fe; color: #01579b; }

    /* Remove default button styling for cards */
    div.stButton > button {
        width: 100%;
        background-color: transparent;
        border: none;
        padding: 0;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA CONFIG ---
JOURNALS = {
    "Nature": "https://www.nature.com/nature.rss",
    "Physical Review Letters": "https://feeds.aps.org/rss/recent/prl.xml",
    "Biophysical Journal": "https://www.cell.com/biophysj/current.rss",
    "arXiv: Quantitative Biology": "https://arxiv.org/rss/q-bio"
}
KEYWORDS = ["TASEP", "Ribosome", "Translation", "Stochastic", "Kinetics"]

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2950/2950155.png", width=80)
    st.title("Research Node")
    st.markdown("---")
    page = st.radio("MAIN MENU", ["✧ Overview", "📡 Literature Surf", "📓 Theory Log"])
    st.markdown("---")
    st.caption("Theoretical Biophysics | v2.0")

# --- PAGE 1: RESEARCH OVERVIEW ---
if page == "✧ Overview":
    st.title("Research Framework")
    
    # Hero Section
    with st.container():
        st.markdown("""
        <div style='background: white; padding: 30px; border-radius: 15px; margin-bottom: 25px;'>
            <h2 style='color: #1e3d59;'>Stochastic Dynamics in Protein Biosynthesis</h2>
            <p style='color: #555; font-size: 1.1rem;'>Investigating the non-equilibrium statistical mechanics of 
            ribosomal movement and mRNA translation efficiency.</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Current Modeling: TASEP")
        st.latex(r"P(\tau) = \omega e^{-\omega \tau}")
        st.info("Focusing on the exclusion process and site-dependent hopping rates to predict experimental run-off profiles.")
    
    with col2:
        st.subheader("Co-translational Kinetics")
        st.markdown("* Binding/Unbinding flux ($\phi$)\n* Elongation velocity ($v$)\n* Ribosome density ($\rho$)")
        st.success("Theoretical Goal: Link mRNA sequence features to protein sorting efficiency.")

# --- PAGE 2: LITERATURE SURF ---
elif page == "📡 Literature Surf":
    st.title("Active Literature Monitor")
    
    col_list, col_viewer = st.columns([1, 1.5])
    
    with col_list:
        selected_journal = st.selectbox("Journal Source", list(JOURNALS.keys()))
        feed = feedparser.parse(JOURNALS[selected_journal])
        
        st.write(f"Displaying latest from **{selected_journal}**")
        
        for entry in feed.entries[:10]:
            is_relevant = any(kw.lower() in (entry.title + entry.get('summary', '')).lower() for kw in KEYWORDS)
            
            # Custom Article Card with HTML
            badge_html = '<span class="badge badge-relevant">Field Match</span>' if is_relevant else ''
            card_html = f"""
            <div class="article-card">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <small style="color: #666;">{entry.get('published', 'Recent')}</small>
                    {badge_html}
                </div>
                <h4 style="margin: 10px 0; color: #2e5cb8;">{entry.title}</h4>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Invisible button over the card to handle selection
            if st.button("Read Full Article", key=entry.link):
                st.session_state.active_url = entry.link
            st.write("") # Spacer

    with col_viewer:
        if 'active_url' in st.session_state:
            st.subheader("Interactive Viewer")
            st.components.v1.iframe(st.session_state.active_url, height=900, scrolling=True)
        else:
            st.markdown("""
            <div style="height: 600px; display: flex; align-items: center; justify-content: center; border: 2px dashed #ccc; border-radius: 15px;">
                <p style="color: #999;">Select an article card to begin deep-reading.</p>
            </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: THEORY LOG ---
elif page == "📓 Theory Log":
    st.title("Theoretical Journal")
    password = st.sidebar.text_input("Access Key", type="password")
    
    if password == "physics2026":
        st.markdown("### Private Derivations & Lab Log")
        log_col, tool_col = st.columns([2, 1])
        
        with log_col:
            st.text_area("Daily Research Entry:", placeholder="Derived new steady-state flux for TASEP with k_deg...", height=300)
            st.button("Archive to GitHub")
            
        with tool_col:
            st.write("**Quick Constants**")
            st.code("k_on = 0.1 s^-1\nv_avg = 5 aa/s", language="python")
    else:
        st.warning("Please enter your access key in the sidebar to view private logs.")
