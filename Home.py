"""Home — run with:  streamlit run Home.py"""
import streamlit as st
import style
from data import PROFILE, METRICS, RESEARCH, PUBLICATIONS

style.setup("Home")
p = PROFILE

# ---- hero ---------------------------------------------------------------- #
# To use a real photo instead of the monogram: put assets/profile.jpg in the
# repo and replace the <div class="medallion">…</div> with:
#   <div class="medallion"><img src="app/static/profile.jpg"></div>
st.markdown(f"""
<div class="hero">
  <div class="hero-text">
    <span class="eyebrow">{p['role']} · {p['affiliation']}</span>
    <h1>{p['name']}</h1>
    <p class="lede">{p['tagline']}</p>
    <p class="sub">{p['position']} · {p['group']}</p>
  </div>
  <div class="medallion">{p['initials']}</div>
</div>
""", unsafe_allow_html=True)

style.codon_strip()

# ---- metrics ------------------------------------------------------------- #
st.markdown(
    '<div class="metrics">'
    + "".join(f'<div class="metric"><div class="n">{n}</div>'
              f'<div class="k">{k}</div></div>' for n, k in METRICS)
    + "</div>", unsafe_allow_html=True)

# ---- about --------------------------------------------------------------- #
st.markdown(f"<p style='font-size:1.08rem;max-width:70ch'>{p['lede']}</p>",
            unsafe_allow_html=True)
st.markdown(f"<p class='sub' style='margin-top:-.4rem'>{p['background']}</p>",
            unsafe_allow_html=True)

# ---- research focus ------------------------------------------------------ #
st.markdown("## Research focus")
cols = st.columns(2)
for i, r in enumerate(RESEARCH):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
          <span class="eyebrow">{r['eyebrow']}</span>
          <h3>{r['title']}</h3>
          <p>{r['body']}</p>
        </div>""", unsafe_allow_html=True)

# ---- featured publication ------------------------------------------------ #
feat = PUBLICATIONS[0]
st.markdown("## Featured work")
st.markdown(f"""
<div class="card">
  <span class="eyebrow">{feat['venue']} · {feat['year']}</span>
  <h3>{feat['title']}</h3>
  <p class="a" style="color:var(--muted);font-size:.92rem">{feat['authors']}</p>
  <p style="margin-top:.5rem">{feat['summary']}</p>
  <p style="margin-top:.6rem"><a class="doi" href="https://doi.org/{feat['doi']}"
     target="_blank">doi:{feat['doi']} ↗</a></p>
</div>""", unsafe_allow_html=True)

st.caption("Browse the full list under **Publications**, or track the newest "
           "translation papers from top journals under **Literature Feed**.")
