import streamlit as st
import datetime
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inayat | Theoretical Biophysics",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CACHED PUBMED FETCHING FUNCTION ---
@st.cache_data(ttl=43200) # Caches data for 12 hours so it loads instantly
def fetch_recent_papers():
    # Calculate date range (Look back 7 days to catch all new entries without gaps)
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)
    
    date_str = f'"{start_date.strftime("%Y/%m/%d")}"[PDAT] : "{end_date.strftime("%Y/%m/%d")}"[PDAT]'
    
    # Target high-impact journals and specific translation/ribosome keywords
    journals = '("Nature"[Journal] OR "Science"[Journal] OR "Cell"[Journal])'
    keywords = '("protein synthesis"[TIAB] OR "translation"[TIAB] OR "ribosome"[TIAB] OR "mRNA translation"[TIAB])'
    query = urllib.parse.quote(f"{journals} AND {keywords} AND {date_str}")
    
    search_url = f"https://nih.gov{query}&retmode=json"
    
    try:
        with urllib.request.urlopen(search_url) as response:
            search_data = json.loads(response.read().decode())
            id_list = search_data.get("esearchresult", {}).get("idlist", [])
            
        if not id_list:
            return []
            
        ids_str = ",".join(id_list)
        fetch_url = f"https://nih.gov{ids_str}&retmode=xml"
        
        with urllib.request.urlopen(fetch_url) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        papers = []
        
        for article in root.findall(".//PubmedArticle"):
            title = article.find(".//ArticleTitle").text
            journal = article.find(".//Journal/Title").text
            pub_date = article.find(".//JournalIssue/PubDate")
            
            year = pub_date.find("Year").text if pub_date.find("Year") is not None else ""
            month = pub_date.find("Month").text if pub_date.find("Month") is not None else ""
            
            abstract_elements = article.findall(".//AbstractText")
            abstract = " ".join([elem.text for elem in abstract_elements if elem.text])
            
            doi = ""
            for el in article.findall(".//ArticleId"):
                if el.attrib.get("IdType") == "doi":
                    doi = el.text
            
            link = f"https://doi.org{doi}" if doi else f"https://nih.gov{article.find('.//PMID').text}"

            papers.append({
                "title": title,
                "journal": journal,
                "date": f"{month} {year}".strip(),
                "abstract": abstract if abstract else "Abstract text not indexed on PubMed yet.",
                "link": link
            })
        return papers
    except Exception as e:
        return []

# --- SESSION STATE INITIALIZATION (For Reminders) ---
if 'reminders' not in st.session_state:
    st.session_state.reminders = [
        {"task": "Submit manuscript revision", "done": False},
        {"task": "Review lab meeting notes", "done": True},
        {"task": "Check simulation logs", "done": False}
    ]

# --- ADVANCED CUSTOM CSS ---
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://googleapis.com');

    /* GLOBAL RESET & VARIABLES */
    :root {
        --primary-color: #1a202c;
        --accent-color: #3b82f6;
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --text-color: #2d3748;
        --subtext-color: #718096;
    }

    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: 'Lato', sans-serif;
    }

    /* TYPOGRAPHY */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: var(--primary-color);
    }
    
    h1 { letter-spacing: -0.5px; font-weight: 700; }
    h2 { font-weight: 600; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 30px; }
    p, li { font-size: 1.05rem; line-height: 1.6; color: #4a5568; }

    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    .sidebar-profile {
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid #edf2f7;
        margin-bottom: 20px;
    }
    
    .sidebar-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 5px;
    }
    
    .sidebar-role {
        font-family: 'Lato', sans-serif;
        font-size: 0.9rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* CARDS & CONTAINERS */
    .feature-card {
        background: var(--card-bg);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 20px;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #cbd5e0;
    }

    /* PUBLICATION STYLING */
    .pub-entry {
        border-left: 3px solid var(--accent-color);
        padding-left: 20px;
        margin-bottom: 25px;
    }
    .pub-year { font-weight: 700; color: var(--accent-color); font-size: 0.9rem; }
    .pub-title { font-weight: 700; font-size: 1.2rem; color: #2d3748; margin: 5px 0; }
    .pub-journal { font-style: italic; color: #718096; }

    /* WIDGET STYLING */
    .weather-widget {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }

    /* BUTTONS */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #cbd5e0;
        background-color: white;
        color: #2d3748;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        border-color: var(--primary-color);
        background-color: #f7fafc;
        color: var(--primary-color);
    }
    
    /* HIDE STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-profile">
            <div class="sidebar-name">INAYAT</div>
            <div class="sidebar-role">Theoretical Biophysics</div>
        </div>
    """, unsafe_allow_html=True)
    
    selected_tab = st.radio(
        "NAVIGATION", 
        ["Dashboard", "Publications", "Journal Library", "Science Monitor"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("**QUICK TOOLS**")
    
    new_task = st.text_input("Add Reminder", placeholder="e.g., Read Nature paper...")
    if st.button("Add Task") and new_task:
        st.session_state.reminders.append({"task": new_task, "done": False})
        st.rerun()

    st.write("")
    for i, item in enumerate(st.session_state.reminders):
        col1, col2 = st.columns([0.15, 0.85])
        with col1:
            if st.button("✖", key=f"del_{i}", help="Remove task"):
                st.session_state.reminders.pop(i)
                st.rerun()
        with col2:
            st.caption(f"• {item['task']}")

# --- TAB 1: DASHBOARD (HOME) ---
if selected_tab == "Dashboard":
    
    # --- SCHEMATIC FIGURE HEADER ---
    st.markdown("""
        <div style="width:100%; height:240px; overflow:hidden; border-radius:12px; margin-bottom: 25px; position: relative; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=2670&auto=format&fit=crop" 
                 style="width:100%; height:100%; object-fit:cover; opacity: 0.85; filter: contrast(1.2) brightness(0.8);" 
                 alt="Biophysics Schematic">
            <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0) 100%);"></div>
            
            <!-- OVERLAY EQUATIONS -->
            <div style="position:absolute; top: 20%; left: 10%; color: rgba(255,255,255,0.8); font-family: 'Times New Roman', serif; font-size: 1.5rem; font-style: italic;">
                iℏ ∂Ψ/∂t = ĤΨ
            </div>
            <div style="position:absolute; bottom: 30%; right: 15%; color: rgba(255,255,255,0.6); font-family: 'Times New Roman', serif; font-size: 1.2rem;">
                (iγ<sup>μ</sup>∂<sub>μ</sub> - m)ψ = 0
            </div>
             <div style="position:absolute; top: 30%; right: 35%; color: rgba(255,255,255,0.5); font-family: 'Times New Roman', serif; font-size: 1.4rem;">
                ∂ρ/∂t + ∇⋅J = σ
            </div>
            <div style="position:absolute; bottom: 20%; left: 30%; color: rgba(255,255,255,0.7); font-family: 'Times New Roman', serif; font-size: 1.3rem;">
                dP<sub>n</sub>/dt = ∑ (W<sub>nm</sub>P<sub>m</sub> - W<sub>mn</sub>P<sub>n</sub>)
            </div>

            <div style="position:absolute; bottom: 10px; left: 20px; color: white; background: rgba(0,0,0,0.5); padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; backdrop-filter: blur(4px);">
                Schematic: Stochastic Dynamics & Quantum Transport
            </div>
        </div>
