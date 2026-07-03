"""
Protein Synthesis Paper Tracker
--------------------------------
Streamlit dashboard that pulls the latest protein-synthesis / translation
papers from top journals via the Europe PMC REST API (free, no key needed)
and shows title, journal, date, authors, abstract, and an optional AI TL;DR.

Deploy on Streamlit Community Cloud straight from GitHub. See README.md.
"""

from __future__ import annotations
import datetime as dt
import re
import requests
import pandas as pd
import streamlit as st

# --------------------------------------------------------------------------- #
# CONFIG — edit these freely
# --------------------------------------------------------------------------- #

# Journals to track: display name -> list of ISSNs (print + electronic).
# Filtering is done by ISSN (unambiguous, avoids the "Science" substring trap).
# If a journal ever goes missing, double-check/add its ISSNs (search "<name> ISSN").
JOURNALS: dict[str, list[str]] = {
    "Science":                        ["0036-8075", "1095-9203"],
    "Science Advances":               ["2375-2548"],
    "Science Transl. Medicine":       ["1946-6234", "1946-6242"],
    "Nature":                         ["0028-0836", "1476-4687"],
    "Nature Communications":          ["2041-1723"],
    "Nature Methods":                 ["1548-7091", "1548-7105"],
    "Nature Struct. & Mol. Biol.":    ["1545-9993", "1545-9985"],
    "Nature Cell Biology":            ["1465-7392", "1476-4679"],
    "Nature Chemical Biology":        ["1552-4450", "1552-4469"],
    "Cell":                           ["0092-8674", "1097-4172"],
    "Molecular Cell":                 ["1097-2765", "1097-4164"],
    "Cell Reports":                   ["2211-1247"],
    "PNAS":                           ["0027-8424", "1091-6490"],
    "eLife":                          ["2050-084X"],
    "Nucleic Acids Research":         ["0305-1048", "1362-4962"],
    "EMBO Journal":                   ["0261-4189", "1460-2075"],
    "Genes & Development":            ["0890-9369", "1549-5477"],
    "RNA":                            ["1355-8382", "1469-9001"],
}

# Default topic query (Europe PMC boolean syntax). Editable in the sidebar.
# Covers both modelling and experimental translation biology.
DEFAULT_QUERY = (
    '"protein synthesis" OR "mRNA translation" OR "translational control" '
    'OR "translation elongation" OR "translation initiation" '
    'OR "ribosome profiling" OR "Ribo-seq" OR "elongation rate" '
    'OR "ribosome" OR "codon usage" OR "tRNA"'
)

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
SUMMARY_MODEL = "claude-haiku-4-5-20251001"  # used only if an API key is set
CACHE_TTL = 60 * 60 * 6  # re-query Europe PMC at most every 6 hours

ISSN2NAME = {issn: name for name, issns in JOURNALS.items() for issn in issns}
_TAG = re.compile(r"<[^>]+>")


# --------------------------------------------------------------------------- #
# DATA
# --------------------------------------------------------------------------- #

@st.cache_data(ttl=CACHE_TTL, show_spinner=False)
def fetch_papers(topic: str, issns: tuple[str, ...], since: str,
                 sort: str, limit: int) -> list[dict]:
    """Query Europe PMC and return a list of normalised paper dicts."""
    journal_clause = "(" + " OR ".join(f'ISSN:"{i}"' for i in issns) + ")"
    query = f"({topic}) AND {journal_clause} AND FIRST_PDATE:[{since} TO 3000]"
    if sort == "Newest":
        query += " sort_date:y"
    elif sort == "Most cited":
        query += " sort_cited:y"
    params = {
        "query": query, "resultType": "core", "format": "json",
        "pageSize": min(limit, 1000), "synonym": "false",
    }
    r = requests.get(EPMC, params=params,
                     headers={"User-Agent": "protein-synth-tracker/1.0"},
                     timeout=30)
    r.raise_for_status()
    results = r.json().get("resultList", {}).get("result", [])
    return [_normalise(x) for x in results][:limit]


def _clean(text: str) -> str:
    return _TAG.sub("", text or "").strip()


def _normalise(x: dict) -> dict:
    j = (x.get("journalInfo", {}) or {}).get("journal", {}) or {}
    issn, essn = j.get("issn", ""), j.get("essn", "")
    name = ISSN2NAME.get(issn) or ISSN2NAME.get(essn) or j.get("title", "—")
    doi = x.get("doi", "")
    url = (f"https://doi.org/{doi}" if doi else
           f"https://europepmc.org/article/{x.get('source', 'MED')}/{x.get('id', '')}")
    return {
        "title": _clean(x.get("title", "Untitled")).rstrip("."),
        "journal": name,
        "date": x.get("firstPublicationDate", ""),
        "authors": x.get("authorString", ""),
        "abstract": _clean(x.get("abstractText", "")) or "No abstract available.",
        "doi": doi, "url": url,
    }


@st.cache_data(ttl=CACHE_TTL, show_spinner=False)
def ai_tldr(title: str, abstract: str) -> str:
    """Optional 2-sentence TL;DR via the Anthropic API (needs a key in secrets)."""
    import anthropic
    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model=SUMMARY_MODEL, max_tokens=220,
        messages=[{"role": "user", "content":
            "In two plain sentences, summarise the key finding and the method of "
            "this paper for a translation-biology researcher. Be specific.\n\n"
            f"Title: {title}\n\nAbstract: {abstract}"}],
    )
    return "".join(b.text for b in msg.content if b.type == "text").strip()


# --------------------------------------------------------------------------- #
# UI
# --------------------------------------------------------------------------- #

st.set_page_config(page_title="Protein Synthesis Paper Tracker",
                   page_icon="🧬", layout="wide")
st.title("🧬 Protein Synthesis Paper Tracker")
st.caption("Latest translation / protein-synthesis papers from top journals · "
           "source: Europe PMC")

try:
    has_key = "ANTHROPIC_API_KEY" in st.secrets
except Exception:
    has_key = False

with st.sidebar:
    st.header("Filters")
    topic = st.text_area("Topic query (Europe PMC syntax)", DEFAULT_QUERY, height=150)
    days = st.slider("Published in the last … days", 7, 365, 60, step=7)
    sort = st.radio("Sort by", ["Newest", "Most cited", "Relevance"], index=0)
    limit = st.slider("Max papers", 10, 200, 60, step=10)
    picked = st.multiselect("Journals", list(JOURNALS), default=list(JOURNALS))
    want_ai = st.checkbox(
        "Add AI TL;DRs", value=False, disabled=not has_key,
        help=None if has_key else "Add ANTHROPIC_API_KEY in app secrets to enable.")
    if st.button("🔄 Refresh now"):
        st.cache_data.clear()

since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
issns = tuple(i for name in picked for i in JOURNALS[name])

if not issns:
    st.warning("Select at least one journal.")
    st.stop()

try:
    papers = fetch_papers(topic.strip(), issns, since, sort, limit)
except Exception as e:
    st.error(f"Could not reach Europe PMC: {e}")
    st.stop()

st.write(f"**{len(papers)}** papers · since {since} · "
         f"updated {dt.datetime.now():%Y-%m-%d %H:%M}")

if papers:
    df = pd.DataFrame(papers)[["date", "journal", "title", "authors", "doi", "url"]]
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(),
                       "protein_synthesis_papers.csv", "text/csv")

for p in papers:
    st.markdown(f"### [{p['title']}]({p['url']})")
    st.markdown(f"**{p['journal']}** · {p['date']}  \n*{p['authors']}*")
    if want_ai:
        with st.spinner("Summarising…"):
            try:
                st.info("**TL;DR** — " + ai_tldr(p["title"], p["abstract"]))
            except Exception as e:
                st.caption(f"(AI summary unavailable: {e})")
    with st.expander("Abstract"):
        st.write(p["abstract"])
    st.divider()

if not papers:
    st.info("No papers matched. Widen the date window or loosen the topic query.")
