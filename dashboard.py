import streamlit as st
import datetime
import requests
import pandas as pd
import graphviz

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inayat | Theoretical Biophysics",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UTILITY FUNCTIONS ---
def get_weather(city="Basel"):
    """Fetches simple current weather from OpenMeteo (No API Key needed)"""
    try:
        # Coordinates for Basel, Switzerland
        url = "https://api.open-meteo.com/v1/forecast?latitude=47.5584&longitude=7.5733&current_weather=true"
        response = requests.get(url).json()
        temp = response['current_weather']['temperature']
        code = response['current_weather']['weathercode']
        return f"{temp}°C"
    except:
        return "N/A"

# --- CUSTOM CSS: ACADEMIC MINIMALISM & SEGREGATION ---
st.markdown("""
    <style>
    /* TYPOGRAPHY */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif; 
        color: #0f172a;
    }

    /* GLOBAL STYLES */
    .stApp {
        background-color: #ffffff;
        color: #334155;
    }
    
    /* SEGREGATION & ZONES */
    /* Header Zone: Top Title Area */
    .header-zone {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 40px;
        border-radius: 16px;
        border-bottom: 4px solid #3b82f6;
        margin-bottom: 30px;
        text-align: center;
    }

    /* Main Content Areas */
    .research-zone {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 20px -5px rgba(0,0,0,0.05);
        height: 100%;
    }

    .updates-zone {
        background-color: #f1f5f9; /* Distinct light grey/slate for right sidebar */
        border-left: 4px solid #94a3b8;
        border-radius: 8px;
        padding: 20px;
        height: 100%;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }

    /* PUBLICATION LIST */
    .pub-entry {
        padding: 1.5rem 0;
        border-bottom: 1px solid #f1f5f9;
    }
    .pub-year {
        font-weight: 800;
        color: #64748b; /* Darker for better visibility */
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    .pub-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
        line-height: 1.4;
    }
    .pub-journal {
        font-style: italic;
        color: #64748b;
        font-family: 'Playfair Display', serif;
    }

    /* TAB STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
        color: #64748b;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
        color: #0f172a;
        border-bottom: 2px solid #0f172a;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: DASHBOARD CONTROLS ---
with st.sidebar:
    st.markdown("### INAYAT NODE")
    st.caption("Theoretical Biophysics | Postdoc")
    
    # Navigation
    selected_page = st.radio(
        "Navigate", 
        ["Home", "Publications", "Journals & Libraries", "Science Feed", "Planner"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Widget 1: Live Weather (Basel)
    col_w1, col_w2 = st.columns([1, 3])
    with col_w1:
        st.write("☁️")
    with col_w2:
        st.write(f"**Basel:** {get_weather()}")
        st.caption(datetime.datetime.now().strftime("%A, %d %B"))

    st.markdown("---")
    
    # Widget 2: Quick Lab Reminders
    st.markdown("**Lab Reminders**")
    if 'reminders' not in st.session_state:
        st.session_state.reminders = ["Submit grant draft", "Review student paper"]
    
    new_reminder = st.text_input("Add task", placeholder="Type & Enter", label_visibility="collapsed")
    if new_reminder:
        st.session_state.reminders.append(new_reminder)
    
    # Display list with delete capability
    for i, task in enumerate(st.session_state.reminders):
        c1, c2 = st.columns([0.1, 0.9])
        if c1.button("x", key=f"del_{i}", help="Remove"):
            st.session_state.reminders.pop(i)
            st.rerun()
        c2.write(f"• {task}")

# --- PAGE 1: HOME (PERSPECTIVE) ---
if selected_page == "Home":
    # 1. HEADER ZONE (Top)
    st.markdown("""
    <div class="header-zone">
        <h1 style="margin:0; font-size: 3rem;">Biophysics & Computational Biology</h1>
        <p style="margin:10px 0 0; color: #475569; font-weight: 600; letter-spacing: 2px;">NON-EQUILIBRIUM SYSTEMS | STOCHASTIC DYNAMICS</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. SCHEMATIC / EQUATION VISUAL (Middle)
    # Replacing the large image with a scientific schematic and equation
    c_vis1, c_vis2 = st.columns([1, 1])
    
    with c_vis1:
        st.markdown("##### Governing Dynamics")
        # Displaying a generic Fokker-Planck equation as requested (Math instead of Image)
        st.latex(r"""
        \frac{\partial P(x,t)}{\partial t} = -\frac{\partial}{\partial x} \left[ A(x)P(x,t) \right] + \frac{\partial^2}{\partial x^2} \left[ D(x)P(x,t) \right]
        """)
        st.caption("Time-evolution of probability density function in stochastic systems.")

    with c_vis2:
        st.markdown("##### System Schematic")
        # Using Graphviz for a clean, code-generated schematic figure
        st.graphviz_chart("""
            digraph {
                rankdir=LR;
                bgcolor="transparent";
                node [shape=box, style="filled,rounded", fillcolor="#ffffff", color="#cbd5e1", fontname="Inter", fontsize=10];
                edge [color="#64748b", fontname="Inter", fontsize=8];
                
                DNA [label="Chromatin\nConfiguration", fillcolor="#f1f5f9"];
                RNA [label="mRNA\nTranscription"];
                Protein [label="Protein\nTranslation", penwidth=2, color="#3b82f6"];
                
                DNA -> RNA [label="k_tx"];
                RNA -> Protein [label="k_tl"];
                Protein -> Protein [label="Feedback", style=dashed];
            }
        """)

    st.markdown("---")

    # 3. SEGREGATED CONTENT (Bottom: Left & Right)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Research Zone - distinct styling
        st.markdown('<div class="research-zone">', unsafe_allow_html=True)
        st.markdown("### Research Rationale")
        st.markdown("""
        Our work attempts to decipher the stochastic logic governing protein synthesis and gene regulation. 
        Biological systems operate far from equilibrium, necessitating statistical physics frameworks to understand 
        their robustness.
        
        **Key Questions:**
        * How does chromatin conformation influence transcriptional bursting?
        * What are the mechanics of ribosome exchange under stress?
        * Can we predict gene expression from structural modifications?
        
        By bridging fundamental physical laws with complex biological mechanics, we aim to build predictive models
        for cellular behavior.
        """)
        
        st.info("**Current Focus:** Investigating NatA ribosome exchange and translation regulation under stress conditions.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Updates Zone - distinct styling
        st.markdown('<div class="updates-zone">', unsafe_allow_html=True)
        st.markdown("### Latest Preprints")
        st.markdown("""
        **2025 | Molecular Cell** *HYPK promotes N-terminal protein acetylation*
        
        **2025 | npj Systems Bio** *Predicting gene expression from chromatin structure*
        """)
        st.write("")
        st.link_button("→ Google Scholar", "https://scholar.google.com", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: PUBLICATIONS ---
elif selected_page == "Publications":
    st.title("Selected Works")
    st.markdown("A curation of peer-reviewed articles and conference proceedings.")
    
    # Helper to render clean publication entries
    def render_pub(year, title, authors, journal, link="#"):
        st.markdown(f"""
        <div class="pub-entry">
            <div class="pub-year">{year}</div>
            <a href="{link}" style="text-decoration: none;"><div class="pub-title">{title}</div></a>
            <div style="color: #475569; font-size: 0.95rem;">{authors}</div>
            <div class="pub-journal">{journal}</div>
        </div>
        """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Journal Articles", "Conference Proceedings"])
    
    with tab1:
        render_pub("2025", "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA", 
                   "AM Lentzsch, Z Fan, IU Irshad, et al.", "Molecular Cell 85 (24), 4562-4574")
        render_pub("2025", "Predicting gene expression changes from chromatin structure modification", 
                   "S Senapati, IU Irshad, AK Sharma, H Kumar", "npj Systems Biology and Applications 11 (1), 34")
        render_pub("2024", "Understanding the regulation of protein synthesis under stress conditions", 
                   "IU Irshad, AK Sharma", "Biophysical Journal 123 (20), 3627-3639")
        render_pub("2023", "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters", 
                   "IU Irshad, AK Sharma", "Biophysical Reports 3 (4)")
        render_pub("2023", "Fundamental insights into the correlation between chromosome configuration and transcription", 
                   "S Senapati, IU Irshad, et al.", "Physical Biology 20 (5)")
    
    with tab2:
        render_pub("2025", "Understanding the regulation of protein synthesis in stress conditions", 
                   "IU Irshad", "Biophysical Journal 124 (3), 145a-146a")

# --- PAGE 3: JOURNALS & LIBRARIES ---
elif selected_page == "Journals & Libraries":
    st.title("Digital Library")
    
    # -- Search Engines --
    st.markdown("### Database Search")
    c1, c2 = st.columns(2)
    with c1:
        scholar_q = st.text_input("Google Scholar", placeholder="Search keywords...")
        if scholar_q:
            st.link_button("Search Scholar", f"https://scholar.google.com/scholar?q={scholar_q}")
    with c2:
        pubmed_q = st.text_input("PubMed", placeholder="Search biomedical literature...")
        if pubmed_q:
            st.link_button("Search PubMed", f"https://pubmed.ncbi.nlm.nih.gov/?term={pubmed_q}")

    st.write("---")
    
    # -- Segregated Journals --
    st.markdown("### Journal Racks")
    
    # Define journal dictionary structure
    journal_groups = {
        "Nature Portfolio": {
            "Nature": "https://www.nature.com/",
            "Nature Physics": "https://www.nature.com/nphys/",
            "Nature Methods": "https://www.nature.com/nmeth/",
            "Nature Comms": "https://www.nature.com/ncomms/",
            "Sci Reports": "https://www.nature.com/srep/"
        },
        "Science Family": {
            "Science": "https://www.science.org/",
            "Science Advances": "https://www.science.org/journal/sciadv",
            "Science Robotics": "https://www.science.org/journal/scirobotics"
        },
        "Cell Press": {
            "Cell": "https://www.cell.com/cell/home",
            "Molecular Cell": "https://www.cell.com/molecular-cell/home",
            "Biophysical Journal": "https://www.cell.com/biophysj/home",
            "Structure": "https://www.cell.com/structure/home"
        },
        "Physics (APS/IOP)": {
            "Phys. Rev. Lett.": "https://journals.aps.org/prl/",
            "Phys. Rev. E": "https://journals.aps.org/pre/",
            "Physical Biology": "https://iopscience.iop.org/journal/1478-3975",
            "Rev. Mod. Phys.": "https://journals.aps.org/rmp/"
        }
    }
    
    # Create tabs for each publisher group
    tabs = st.tabs(list(journal_groups.keys()))
    
    for tab, (group_name, journals) in zip(tabs, journal_groups.items()):
        with tab:
            cols = st.columns(4)
            for i, (name, url) in enumerate(journals.items()):
                with cols[i % 4]:
                    st.link_button(name, url, use_container_width=True)

# --- PAGE 4: SCIENCE FEED ---
elif selected_page == "Science Feed":
    st.title("Latest Updates in Science")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Curated Feeds")
        # Simulating a feed layout
        feed_items = [
            {"source": "Nature News", "title": "New insights into ribosome heterogeneity", "date": "Today"},
            {"source": "Science Daily", "title": "Physics of chromatin folding revealed by cryo-EM", "date": "Yesterday"},
            {"source": "Phys.org", "title": "Stochastic processes in biological cells: A review", "date": "2 Days ago"},
        ]
        
        for item in feed_items:
            st.markdown(f"""
            <div style="padding: 15px; background: white; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 10px;">
                <div style="font-size: 0.8rem; color: #3b82f6; font-weight: bold; text-transform: uppercase;">{item['source']} • {item['date']}</div>
                <div style="font-size: 1.1rem; font-weight: 600; margin-top: 5px;">{item['title']}</div>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.markdown("### Quick Access")
        st.link_button("bioRxiv (Biophysics)", "https://www.biorxiv.org/collection/biophysics", use_container_width=True)
        st.link_button("arXiv (Quant Bio)", "https://arxiv.org/list/q-bio/new", use_container_width=True)

# --- PAGE 5: PLANNER (Google Calendar) ---
elif selected_page == "Planner":
    st.title("Schedule & Planning")
    st.markdown("Integrate your lab schedule or conference timeline here.")
    
    # Calendar Embed
    # NOTE: Replace 'src=' URL with your specific Google Calendar Embed URL for this to show YOUR events.
    # Go to Google Calendar -> Settings -> Integrate Calendar -> Embed Code
    st.components.v1.iframe(
        src="https://calendar.google.com/calendar/embed?src=en.usa%23holiday%40group.v.calendar.google.com&ctz=Europe%2FZurich",
        height=600,
        scrolling=True
    )
