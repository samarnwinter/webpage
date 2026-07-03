import streamlit as st
import style
from data import RESEARCH

style.setup("Research")

st.markdown('<span class="eyebrow">What I work on</span>', unsafe_allow_html=True)
st.markdown("# Research")
st.markdown(
    "I treat protein synthesis as a physics problem: ribosomes are particles "
    "moving on a one-dimensional mRNA lattice, and the observable biology — "
    "rates, noise, stoichiometry — falls out of the stochastic dynamics. The "
    "work moves between three layers: **models**, **data**, and **design**.")

style.codon_strip()

# ---- themes as full-width cards ----------------------------------------- #
for r in RESEARCH:
    st.markdown(f"""
    <div class="card">
      <span class="eyebrow">{r['eyebrow']}</span>
      <h3>{r['title']}</h3>
      <p>{r['body']}</p>
    </div>""", unsafe_allow_html=True)

# ---- approach ------------------------------------------------------------ #
st.markdown("## Approach")
st.markdown("""
<div class="card">
<p><strong>Totally Asymmetric Simple Exclusion Process (TASEP).</strong>
An mRNA is a lattice of codons; a ribosome is an extended particle that initiates
at the start codon, hops codon-to-codon at sequence-dependent rates, and cannot
overtake the ribosome ahead. Simulated with the Gillespie algorithm, this
reproduces polysome profiles, density, and current.</p>
<p><strong>Inference from ribosome profiling.</strong>
Ribo-seq gives a steady-state snapshot of ribosome occupancy. The inverse problem
— recovering absolute initiation and elongation rates from that snapshot — is
where the modeling meets real data.</p>
<p><strong>From mechanism to design.</strong>
Once rates are known, they become knobs: predict initiation rate from sequence,
explain why complex subunits are made in proportion, and optimize genes for a
target expression level.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Tools")
st.markdown("""
<div class="card">
  <span class="eyebrow">Web tool · yeast</span>
  <h3>TIR predictor &amp; optimizer</h3>
  <p>Predicts translation-initiation rate from sequence and optimizes genes for a
  chosen expression level in <em>S. cerevisiae</em> (Chakraborty, Irshad, Mahima
  &amp; Sharma, <em>Biotechnology Journal</em> 2024).</p>
  <p style="margin-top:.5rem"><a class="doi" href="https://doi.org/10.1002/biot.202400081"
  target="_blank">doi:10.1002/biot.202400081 ↗</a></p>
</div>
""", unsafe_allow_html=True)
