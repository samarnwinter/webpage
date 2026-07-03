"""Home — run with:  streamlit run Home.py"""
import streamlit as st
import style
from data import PROFILE, RESEARCH, PUBLICATIONS, SCIENCE

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

# ---- protein synthesis explainer ----------------------------------------- #
st.markdown("## Protein synthesis, quantitatively")
st.markdown(f"<p style='text-align:justify;font-size:1.06rem'>{SCIENCE['intro']}</p>",
            unsafe_allow_html=True)
st.markdown(f"<p style='text-align:justify'>{SCIENCE['bridge']}</p>",
            unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    items = "".join(
        f"<p style='margin:.2rem 0 .8rem'><strong>{t}</strong><br>"
        f"<span style='color:var(--muted);font-size:.94rem'>{d}</span></p>"
        for t, d in SCIENCE["measured"])
    st.markdown(f'<div class="card"><span class="eyebrow">Measured</span>'
                f'<h3>Experiments</h3>{items}</div>', unsafe_allow_html=True)
with c2:
    lis = "".join(f"<li style='margin:.3rem 0'>{x}</li>" for x in SCIENCE["inferred"])
    st.markdown(
        f'<div class="card"><span class="eyebrow">Inferred</span>'
        f'<h3>What the models recover</h3>'
        f'<ul style="margin:.3rem 0 0;padding-left:1.1rem">{lis}</ul>'
        f'<p style="margin-top:.7rem;color:var(--muted);font-size:.92rem">'
        f'via TASEP lattices &amp; master equations</p></div>',
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
