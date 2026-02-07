import streamlit as st
import feedparser
from bs4 import BeautifulSoup # Ensure you added this to requirements.txt

# --- LOGIC TO CLEAN RSS CONTENT ---
def clean_text(raw_html):
    """Removes HTML tags and returns clean text."""
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

# ... (Previous Configuration & CSS) ...

# --- UPDATED JOURNAL DASHBOARD PAGE ---
elif page == "📡 Literature Surf":
    st.title("Academic Literature Station")
    
    col_list, col_viewer = st.columns([1, 1.8])
    
    with col_list:
        selected_journal = st.selectbox("Journal Source", list(JOURNALS.keys()))
        feed = feedparser.parse(JOURNALS[selected_journal])
        
        st.write(f"Showing last **{len(feed.entries)}** papers")
        
        for entry in feed.entries:
            # Clean the title of any stray HTML
            clean_title = clean_text(entry.title)
            
            # Identify high-relevance papers
            is_relevant = any(kw.lower() in clean_title.lower() for kw in KEYWORDS)
            
            # Styled Card Selection
            with st.container():
                label = f"⭐ {clean_title}" if is_relevant else clean_title
                if st.button(label, key=entry.link, use_container_width=True):
                    # Store both link and summary in session state
                    st.session_state.active_article = {
                        "title": clean_title,
                        "link": entry.link,
                        "summary": entry.get('summary', 'No abstract available.'),
                        "published": entry.get('published', 'N/A')
                    }
                st.write("---")

    with col_viewer:
        if 'active_article' in st.session_state:
            art = st.session_state.active_article
            
            # --- THE ARTICLE ABSTRACT PANE ---
            st.markdown(f"""
            <div style='background: white; padding: 25px; border-radius: 10px; border: 1px solid #ddd;'>
                <h2 style='color: #1e3d59;'>{art['title']}</h2>
                <p style='color: #666;'>Published: {art['published']}</p>
                <hr>
                <div style='font-size: 1.1rem; line-height: 1.6; color: #333;'>
                    <strong>Abstract / Summary:</strong><br>
                    {clean_text(art['summary'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("") # Spacer
            
            # --- FULL WEBSITE VIEWER ---
            with st.expander("View Full Journal Interface", expanded=True):
                st.link_button("Open Article in New Tab", art['link'])
                st.components.v1.iframe(art['link'], height=800, scrolling=True)
        else:
            st.info("Select a title from the list to view the summary and interface.")
