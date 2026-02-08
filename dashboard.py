import streamlit as st
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inayat | Theoretical Biophysics",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Playfair+Display:wght@400;600;700&display=swap');

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
    
    # Simple Todo/Reminder System using Session State
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
    # Header Section
    col_hero, col_widgets = st.columns([2, 1])
    
    with col_hero:
        st.markdown(f"""
        <div style="padding-top: 10px;">
            <h1 style="font-size: 3.5rem; margin-bottom: 10px;">Research Node</h1>
            <p style="font-size: 1.2rem; color: #718096;">
                Specializing in Non-Equilibrium Systems & Stochastic Dynamics of Gene Regulation.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧬 Current Research Focus")
        st.markdown("""
        <div class="feature-card">
            <p><strong>Deciphering the stochastic logic of protein synthesis.</strong></p>
            <p>My work utilizes refined TASEP models and polymer physics frameworks to understand:</p>
            <ul>
                <li>The mechanics of ribosome exchange (NatA).</li>
                <li>Chromatin conformation dynamics.</li>
                <li>Translation regulation under stress conditions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_widgets:
        # Date & Time Widget
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %d %B %Y")
        
        # Weather Widget (Using wttr.in as an image to avoid iframe conflicts)
        # Note: 'format=3' gives a concise output. Change 'Basel' to your city if needed.
        st.markdown(f"""
        <div class="weather-widget">
            <h3 style="color: white; margin:0;">{date_str}</h3>
            <div style="margin-top: 15px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px;">
                <img src="https://wttr.in/?format=3&m" style="filter: invert(1); width: 100%; object-fit: contain;">
            </div>
            <p style="margin-top: 10px; font-size: 0.8rem; opacity: 0.8;">Daily Research Planner</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3 style="margin-top:0;">Quick Access</h3>
            <a href="https://scholar.google.com" target="_blank" style="text-decoration: none; color: #3b82f6; display: block; margin: 5px 0;">Google Scholar</a>
            <a href="https://calendar.google.com" target="_blank" style="text-decoration: none; color: #3b82f6; display: block; margin: 5px 0;">Google Calendar</a>
            <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" style="text-decoration: none; color: #3b82f6; display: block; margin: 5px 0;">PubMed</a>
        </div>
        """, unsafe_allow_html=True)

    # Visualization / Math Section
    st.markdown("### 📐 Theoretical Framework")
    c1, c2 = st.columns(2)
    with c1:
        st.latex(r"\frac{\partial \rho(x,t)}{\partial t} = -\frac{\partial J(x,t)}{\partial x} + \text{source} - \text{sink}")
    with c2:
        st.info("Mathematical modeling of ribosome traffic utilizing totally asymmetric simple exclusion processes.")

# --- TAB 2: PUBLICATIONS ---
elif selected_tab == "Publications":
    st.title("Selected Bibliography")
    st.markdown("A curated list of peer-reviewed articles and conference proceedings.")
    st.divider()

    def render_publication(year, title, authors, journal, link="#"):
        st.markdown(f"""
        <div class="feature-card pub-entry">
            <div class="pub-year">{year}</div>
            <div class="pub-title"><a href="{link}" style="text-decoration: none; color: inherit;">{title}</a></div>
            <div style="color: #4a5568;">{authors}</div>
            <div class="pub-journal">{journal}</div>
        </div>
        """, unsafe_allow_html=True)

    # 2025
    st.markdown("## 2025")
    render_publication(
        "2025", 
        "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA",
        "AM Lentzsch, Z Fan, IU Irshad, et al.",
        "Molecular Cell 85 (24), 4562-4574"
    )
    render_publication(
        "2025", 
        "Predicting gene expression changes from chromatin structure modification",
        "S Senapati, IU Irshad, AK Sharma, H Kumar",
        "npj Systems Biology and Applications 11 (1), 34"
    )

    # 2024
    st.markdown("## 2024")
    render_publication(
        "2024", 
        "Understanding the regulation of protein synthesis under stress conditions",
        "IU Irshad, AK Sharma",
        "Biophysical Journal 123 (20), 3627-3639"
    )
    render_publication(
        "2024", 
        "TIR predictor and optimizer: Web-tools for accurate prediction of translation initiation rate",
        "S Chakarborty, IU Irshad, et al.",
        "Biotechnology Journal 19 (5)"
    )

    # 2023 & Prior
    st.markdown("## 2023 & Selected Prior")
    render_publication(
        "2023", 
        "Decoding stoichiometric protein synthesis in E. coli through translation rate parameters",
        "IU Irshad, AK Sharma",
        "Biophysical Reports 3 (4)"
    )
    render_publication(
        "2023", 
        "Fundamental insights into the correlation between chromosome configuration and transcription",
        "S Senapati, IU Irshad, et al.",
        "Physical Biology 20 (5)"
    )
    render_publication(
        "2021", 
        "Quantitative modeling of protein synthesis using ribosome profiling data",
        "V Yadav, I Ullah Irshad, et al.",
        "Frontiers in Molecular Biosciences 8"
    )

# --- TAB 3: JOURNAL LIBRARY ---
elif selected_tab == "Journal Library":
    st.title("Journal Archive")
    st.markdown("Direct access to high-impact publishing venues.")
    
    # Search Bar
    c_search, c_ext = st.columns([3, 1])
    with c_search:
        q = st.text_input("Search Library Database", placeholder="Quick search...")
    with c_ext:
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("🔎 Open Google Scholar", "https://scholar.google.com")

    st.divider()

    def journal_section(header, journals):
        st.markdown(f"### {header}")
        cols = st.columns(4)
        for i, (name, link) in enumerate(journals.items()):
            with cols[i % 4]:
                st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="feature-card" style="padding: 15px; text-align: center; height: 100px; display: flex; align-items: center; justify-content: center;">
                        <span style="font-weight: 700; color: #2d3748;">{name}</span>
                    </div>
                </a>
                """, unsafe_allow_html=True)

    # 1. Nature Portfolio
    journal_section("Nature Portfolio", {
        "Nature": "https://www.nature.com/",
        "Nature Physics": "https://www.nature.com/nphys/",
        "Nature Methods": "https://www.nature.com/nmeth/",
        "Nature Comms": "https://www.nature.com/ncomms/",
        "Sci. Reports": "https://www.nature.com/srep/",
        "Comms Biology": "https://www.nature.com/commsbio/"
    })

    # 2. Science / AAAS
    journal_section("Science (AAAS)", {
        "Science": "https://www.science.org/",
        "Science Advances": "https://www.science.org/journal/sciadv",
        "Science Signaling": "https://www.science.org/journal/signaling",
        "Science Robotics": "https://www.science.org/journal/scirobotics"
    })

    # 3. Cell Press
    journal_section("Cell Press", {
        "Cell": "https://www.cell.com/cell/home",
        "Molecular Cell": "https://www.cell.com/molecular-cell/home",
        "Biophysical J.": "https://www.cell.com/biophysj/home",
        "Cell Reports": "https://www.cell.com/cell-reports/home",
        "Structure": "https://www.cell.com/structure/home",
        "Trends Biochem": "https://www.cell.com/trends/biochemical-sciences/home"
    })

    # 4. Physics & General
    journal_section("Physics & Computational Bio", {
        "Phys. Rev. Lett.": "https://journals.aps.org/prl/",
        "Phys. Rev. E": "https://journals.aps.org/pre/",
        "PNAS": "https://www.pnas.org/",
        "Nucleic Acids Res.": "https://academic.oup.com/nar",
        "Bioinformatics": "https://academic.oup.com/bioinformatics",
        "Physical Biology": "https://iopscience.iop.org/journal/1478-3975"
    })

# --- TAB 4: SCIENCE MONITOR ---
elif selected_tab == "Science Monitor":
    st.title("Latest Updates in Science")
    st.markdown("Real-time aggregator links for scientific breakthroughs.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📰 News Feeds")
        st.markdown("""
        <div class="feature-card">
            <ul style="list-style-type: none; padding: 0;">
                <li style="margin-bottom: 15px;">
                    <a href="https://www.nature.com/latest-news" target="_blank" style="text-decoration: none; font-weight: bold; color: #1a202c;">Nature News & Comment</a><br>
                    <span style="font-size: 0.85rem; color: #718096;">Global science news and analysis.</span>
                </li>
                <li style="margin-bottom: 15px;">
                    <a href="https://www.science.org/news" target="_blank" style="text-decoration: none; font-weight: bold; color: #1a202c;">ScienceDaily: Biophysics</a><br>
                    <span style="font-size: 0.85rem; color: #718096;">Latest research news in biophysics.</span>
                </li>
                 <li style="margin-bottom: 15px;">
                    <a href="https://phys.org/biology-news/biophysics/" target="_blank" style="text-decoration: none; font-weight: bold; color: #1a202c;">Phys.org: Biophysics</a><br>
                    <span style="font-size: 0.85rem; color: #718096;">Physics and Tech news.</span>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 🗓️ Conference Radar")
        st.markdown("""
        <div class="feature-card">
            <p><strong>Upcoming Events (2025-2026)</strong></p>
            <hr style="margin: 10px 0;">
            <p><strong>Biophysical Society Annual Meeting</strong><br><span style="color: #718096; font-size: 0.9rem;">Los Angeles, CA | Feb 2026</span></p>
            <p><strong>APS March Meeting</strong><br><span style="color: #718096; font-size: 0.9rem;">Anaheim, CA | Mar 2026</span></p>
        </div>
        """, unsafe_allow_html=True)
