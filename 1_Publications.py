import streamlit as st
import style
from data import PUBLICATIONS, PROFILE

style.setup("Publications")

st.markdown('<span class="eyebrow">Peer-reviewed</span>', unsafe_allow_html=True)
st.markdown("# Publications")
st.markdown(
    f"Full list also on "
    f"[Google Scholar]({PROFILE['scholar']}). Newest first.")

# ---- controls ------------------------------------------------------------ #
all_tags = sorted({t for pub in PUBLICATIONS for t in pub["tags"]})
c1, c2 = st.columns([2, 1])
with c1:
    picked = st.multiselect("Filter by topic", all_tags, default=[])
with c2:
    query = st.text_input("Search title / author", "")

def keep(pub):
    if picked and not set(picked) & set(pub["tags"]):
        return False
    if query and query.lower() not in (pub["title"] + pub["authors"]).lower():
        return False
    return True

shown = [p for p in PUBLICATIONS if keep(p)]
st.caption(f"{len(shown)} of {len(PUBLICATIONS)} papers")
st.markdown("<hr>", unsafe_allow_html=True)

# ---- list ---------------------------------------------------------------- #
for pub in shown:
    tags = "".join(f'<span class="tag">{t}</span>' for t in pub["tags"])
    st.markdown(f"""
    <div class="pub">
      <div class="yr">{pub['year']}</div>
      <div class="t">{pub['title']}</div>
      <div class="a">{pub['authors']}</div>
      <div class="v">{pub['venue']} · {pub['detail']}</div>
      <div class="s">{pub['summary']}</div>
      <div>{tags}</div>
      <div style="margin-top:.4rem">
        <a class="doi" href="https://doi.org/{pub['doi']}" target="_blank">doi:{pub['doi']} ↗</a>
      </div>
    </div>""", unsafe_allow_html=True)

if not shown:
    st.info("No papers match those filters. Clear the topic or search box.")
