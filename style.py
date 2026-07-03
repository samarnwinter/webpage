"""
Shared visual identity for the site.

Design brief: a theoretical biophysicist who models translation as particles
hopping on an mRNA lattice. The signature motif is a codon strip — monospaced
triplets with two ribosome markers — echoing the TASEP models the work is built
on. Palette is cool "ink + viridian" with a warm amber particle accent, chosen
to avoid the usual cream/terracotta template look.

    Display   Spectral        (editorial serif, screen-tuned)
    Body      Inter
    Data      IBM Plex Mono   (codons, eyebrows, metrics)
"""
import streamlit as st
from data import PROFILE

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root{
  --ink:#16223b;          /* headings / primary text        */
  --ink-soft:#3d4a63;     /* body                            */
  --muted:#727b8f;        /* captions                        */
  --paper:#f6f7f9;        /* app background (cool paper)      */
  --surface:#ffffff;      /* cards                           */
  --line:#e6e9ef;         /* hairlines                       */
  --teal:#0f766e;         /* primary accent (viridian)       */
  --teal-deep:#0b5c55;
  --teal-tint:#e9f2f0;
  --amber:#c98a2b;        /* ribosome particle micro-accent  */
  --amber-tint:#f7ecd9;
}

/* ---- base --------------------------------------------------------------- */
.stApp{ background:var(--paper); }
html, body, [class*="css"]{ font-family:'Inter',sans-serif; color:var(--ink-soft); }
.block-container{ max-width:1080px; padding-top:2.2rem; padding-bottom:4rem; }

h1,h2,h3,h4{ font-family:'Spectral',serif; color:var(--ink); letter-spacing:-.01em; }
h1{ font-weight:700; }
h2{ font-weight:600; font-size:1.7rem; margin-top:.2rem; }
h3{ font-weight:600; }
p,li{ font-size:1.03rem; line-height:1.62; color:var(--ink-soft); }
a{ color:var(--teal-deep); text-decoration:none; }
a:hover{ text-decoration:underline; }

/* ---- eyebrow / labels --------------------------------------------------- */
.eyebrow{
  font-family:'IBM Plex Mono',monospace; font-size:.72rem; font-weight:500;
  letter-spacing:.22em; text-transform:uppercase; color:var(--teal);
}

/* ---- hero --------------------------------------------------------------- */
.hero{ display:flex; align-items:center; gap:32px; margin:.2rem 0 1.4rem; }
.hero-text{ flex:1; }
.hero h1{ font-size:3.2rem; line-height:1.02; margin:.35rem 0 .5rem; }
.hero .lede{ font-size:1.12rem; color:var(--ink-soft); max-width:46ch; }
.hero .sub{ color:var(--muted); font-size:.98rem; margin-top:.4rem; }

/* medallion (swap for a real photo — see README) */
.medallion{
  width:132px; height:132px; border-radius:50%; flex:0 0 auto;
  display:grid; place-items:center;
  background:radial-gradient(120% 120% at 30% 25%, #1c2c4a 0%, #0f766e 130%);
  color:#fff; font-family:'Spectral',serif; font-weight:600; font-size:2.5rem;
  letter-spacing:.02em; box-shadow:0 12px 30px -12px rgba(15,118,110,.55);
  border:3px solid #fff;
}
.medallion img{ width:100%; height:100%; object-fit:cover; border-radius:50%; }

/* ---- codon strip (signature motif) ------------------------------------- */
.codon-strip{
  display:flex; gap:6px; flex-wrap:wrap; align-items:center;
  padding:14px 16px; background:var(--surface); border:1px solid var(--line);
  border-radius:12px; margin:1.1rem 0 1.6rem;
  box-shadow:0 1px 2px rgba(22,34,59,.04);
}
.codon{
  font-family:'IBM Plex Mono',monospace; font-size:.82rem; font-weight:500;
  color:var(--muted); background:#f4f6f8; border:1px solid var(--line);
  border-radius:6px; padding:5px 9px; letter-spacing:.04em;
}
.codon.start{ color:var(--teal-deep); border-color:var(--teal); }
.codon.ribo{                                   /* the "ribosome" particle */
  color:#fff; background:var(--teal); border-color:var(--teal-deep);
  box-shadow:0 0 0 2px var(--amber-tint), 0 4px 10px -4px rgba(15,118,110,.6);
}
.codon.stop{ color:var(--amber); border-color:var(--amber); background:var(--amber-tint); }
@keyframes glide{ 0%,100%{ transform:translateY(0);} 50%{ transform:translateY(-3px);} }
@media (prefers-reduced-motion:no-preference){ .codon.ribo{ animation:glide 2.4s ease-in-out infinite; } }

/* ---- metric row --------------------------------------------------------- */
.metrics{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin:.4rem 0 1.2rem; }
.metric{
  background:var(--surface); border:1px solid var(--line); border-radius:12px;
  padding:18px 20px;
}
.metric .n{ font-family:'Spectral',serif; font-size:1.9rem; font-weight:700; color:var(--ink); line-height:1; }
.metric .k{ font-family:'IBM Plex Mono',monospace; font-size:.68rem; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); margin-top:8px; }

/* ---- generic card ------------------------------------------------------- */
.card{
  background:var(--surface); border:1px solid var(--line); border-radius:14px;
  padding:22px 24px; margin-bottom:16px; transition:transform .18s ease, box-shadow .18s ease;
}
.card:hover{ transform:translateY(-2px); box-shadow:0 14px 30px -18px rgba(22,34,59,.35); }
.card h3{ margin:.1rem 0 .4rem; font-size:1.22rem; }
.card .eyebrow{ display:block; margin-bottom:.3rem; }
.card p{ margin:0; color:var(--ink-soft); }

/* ---- publication entry -------------------------------------------------- */
.pub{ border-left:2px solid var(--line); padding:2px 0 2px 22px; margin:0 0 26px; position:relative; }
.pub::before{ content:''; position:absolute; left:-5px; top:6px; width:8px; height:8px;
  border-radius:50%; background:var(--teal); }
.pub .yr{ font-family:'IBM Plex Mono',monospace; font-size:.78rem; color:var(--teal); letter-spacing:.08em; }
.pub .t{ font-family:'Spectral',serif; font-size:1.2rem; font-weight:600; color:var(--ink); margin:.25rem 0; line-height:1.32; }
.pub .a{ font-size:.92rem; color:var(--muted); }
.pub .v{ font-size:.95rem; color:var(--ink-soft); font-style:italic; margin-top:2px; }
.pub .s{ font-size:.98rem; color:var(--ink-soft); margin:.55rem 0 .5rem; }
.tag{ display:inline-block; font-family:'IBM Plex Mono',monospace; font-size:.68rem;
  letter-spacing:.06em; color:var(--teal-deep); background:var(--teal-tint);
  border-radius:20px; padding:3px 10px; margin:0 6px 6px 0; }
.doi{ font-family:'IBM Plex Mono',monospace; font-size:.82rem; }

/* ---- sidebar ------------------------------------------------------------ */
[data-testid="stSidebar"]{ background:#fff; border-right:1px solid var(--line); }
.side-id{ text-align:center; padding:6px 0 14px; border-bottom:1px solid var(--line); margin-bottom:12px; }
.side-mono{
  width:64px; height:64px; border-radius:50%; margin:0 auto 10px; display:grid; place-items:center;
  background:radial-gradient(120% 120% at 30% 25%, #1c2c4a 0%, #0f766e 130%);
  color:#fff; font-family:'Spectral',serif; font-weight:600; font-size:1.35rem; border:2px solid #fff;
  box-shadow:0 8px 20px -10px rgba(15,118,110,.6);
}
.side-name{ font-family:'Spectral',serif; font-weight:600; color:var(--ink); font-size:1.05rem; }
.side-role{ font-family:'IBM Plex Mono',monospace; font-size:.6rem; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); margin-top:3px; }
.side-links{ font-size:.9rem; }
.side-links a{ display:block; padding:3px 0; color:var(--ink-soft); }
.side-links a:hover{ color:var(--teal-deep); text-decoration:none; }

/* ---- buttons ------------------------------------------------------------ */
.stButton>button{
  border-radius:9px; border:1px solid var(--line); background:#fff; color:var(--ink);
  font-weight:600; transition:all .15s;
}
.stButton>button:hover{ border-color:var(--teal); color:var(--teal-deep); background:var(--teal-tint); }

/* ---- misc --------------------------------------------------------------- */
hr{ border:none; border-top:1px solid var(--line); margin:1.6rem 0; }
#MainMenu,footer,header{ visibility:hidden; }
@media (max-width:760px){
  .hero{ flex-direction:column-reverse; align-items:flex-start; }
  .hero h1{ font-size:2.3rem; }
  .metrics{ grid-template-columns:1fr; }
}
</style>
"""


def setup(page_title: str):
    """Call at the very top of every page (after imports)."""
    st.set_page_config(page_title=f"{page_title} · {PROFILE['name']}",
                       page_icon="🧬", layout="wide",
                       initial_sidebar_state="expanded")
    st.markdown(_CSS, unsafe_allow_html=True)
    _sidebar()


def _sidebar():
    p = PROFILE
    links = [("Google Scholar", p["scholar"]),
             ("Biozentrum", p["profile_page"]),
             ("LinkedIn", p["linkedin"]),
             ("GitHub", p["github"]),
             ("Email", f"mailto:{p['email']}")]
    link_html = "".join(f'<a href="{u}" target="_blank">{t} ↗</a>' for t, u in links)
    with st.sidebar:
        st.markdown(f"""
        <div class="side-id">
          <div class="side-mono">{p['initials']}</div>
          <div class="side-name">{p['name']}</div>
          <div class="side-role">{p['role']}</div>
        </div>
        <div class="side-links">{link_html}</div>
        """, unsafe_allow_html=True)


def codon_strip():
    """The signature translation-lattice motif."""
    cells = [("AUG", "start"), ("GCU", ""), ("CUG", ""), ("AAA", ""),
             ("UUC", "ribo"), ("GGC", ""), ("ACC", ""), ("GAU", "ribo"),
             ("CGU", ""), ("UAC", ""), ("CCA", ""), ("GAG", ""),
             ("UCG", ""), ("UAA", "stop")]
    html = '<div class="codon-strip">'
    html += '<span class="eyebrow" style="margin-right:6px">5′</span>'
    html += "".join(f'<span class="codon {c}">{t}</span>' for t, c in cells)
    html += '<span class="eyebrow" style="margin-left:6px">3′</span></div>'
    st.markdown(html, unsafe_allow_html=True)
