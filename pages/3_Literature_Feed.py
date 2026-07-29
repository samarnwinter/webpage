import datetime as dt
import re
import requests
import pandas as pd
import streamlit as st
import style

style.setup("Literature Feed")

# --------------------------------------------------------------------------- #
# CONFIG — edit freely
# --------------------------------------------------------------------------- #
JOURNALS = {
    "Science":                     ["0036-8075", "1095-9203"],
    "Science Advances":            ["2375-2548"],
    "Nature":                      ["0028-0836", "1476-4687"],
    "Nature Communications":       ["2041-1723"],
    "Nature Struct. & Mol. Biol.": ["1545-9993", "1545-9985"],
    "Cell":                        ["0092-8674", "1097-4172"],
    "Molecular Cell":              ["1097-2765", "1097-4164"],
    "Cell Reports":                ["2211-1247"],
    "PNAS":                        ["0027-8424", "1091-6490"],
    "eLife":                       ["2050-084X"],
    "Nucleic Acids Research":      ["0305-1048", "1362-4962"],
    "EMBO Journal":                ["0261-4189", "1460-2075"],
    "Biophysical Journal":         ["0006-3495", "1542-0086"],
    "RNA":                         ["1355-8382", "1469-9001"],
}
DEFAULT_QUERY = (
    '"protein synthesis" OR "mRNA translation" OR "translational control" '
    'OR "translation elongation" OR "translation initiation" '
    'OR "ribosome profiling" OR "Ribo-seq" OR "elongation rate" '
    'OR "ribosome" OR "codon usage" OR "tRNA"'
    'OR "TASEP" OR "protein synthesis modelling" OR "codon adaptation"'
    'OR "codon usage bias" OR "uORF translation" OR "UTR"'
    'OR "mRNA stability" OR "cotranslation process" OR "cotranslation folding"'
)
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
SUMMARY_MODEL = "claude-haiku-4-5-20251001"
CACHE_TTL = 60 * 60 * 6
ISSN2NAME = {i: n for n, xs in JOURNALS.items() for i in xs}
_TAG = re.compile(r"<[^>]+>")


@st.cache_data(ttl=CACHE_TTL, show_spinner=False)
def fetch_papers(topic, issns, since, sort, limit):
    jc = "(" + " OR ".join(f'ISSN:"{i}"' for i in issns) + ")"
    query = f"({topic}) AND {jc} AND FIRST_PDATE:[{since} TO 3000]"
    if sort == "Newest":
        query += " sort_date:y"
    elif sort == "Most cited":
        query += " sort_cited:y"
    r = requests.get(EPMC, timeout=30,
                     headers={"User-Agent": "iui-site/1.0"},
                     params={"query": query, "resultType": "core",
                             "format": "json", "pageSize": min(limit, 1000),
                             "synonym": "false"})
    r.raise_for_status()
    res = r.json().get("resultList", {}).get("result", [])
    return [_norm(x) for x in res][:limit]


def _clean(t):
    return _TAG.sub("", t or "").strip()


def _norm(x):
    j = (x.get("journalInfo", {}) or {}).get("journal", {}) or {}
    name = (ISSN2NAME.get(j.get("issn", "")) or ISSN2NAME.get(j.get("essn", ""))
            or j.get("title", "—"))
    doi = x.get("doi", "")
    url = (f"https://doi.org/{doi}" if doi else
           f"https://europepmc.org/article/{x.get('source','MED')}/{x.get('id','')}")
    return {"title": _clean(x.get("title", "Untitled")).rstrip("."),
            "journal": name, "date": x.get("firstPublicationDate", ""),
            "authors": x.get("authorString", ""),
            "abstract": _clean(x.get("abstractText", "")) or "No abstract available.",
            "doi": doi, "url": url}


@st.cache_data(ttl=CACHE_TTL, show_spinner=False)
def ai_tldr(title, abstract):
    import anthropic
    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    m = client.messages.create(
        model=SUMMARY_MODEL, max_tokens=220,
        messages=[{"role": "user", "content":
            "In two plain sentences, summarise the key finding and method of this "
            f"paper for a translation-biology researcher.\n\nTitle: {title}\n\n"
            f"Abstract: {abstract}"}])
    return "".join(b.text for b in m.content if b.type == "text").strip()


# --------------------------------------------------------------------------- #
# UI
# --------------------------------------------------------------------------- #
st.markdown('<span class="eyebrow">Live from Europe PMC</span>', unsafe_allow_html=True)
st.markdown("# Literature Feed")
st.markdown("The newest protein-synthesis / translation papers from top journals, "
            "refreshed on load. Abstracts are the quick summary.")

try:
    has_key = "ANTHROPIC_API_KEY" in st.secrets
except Exception:
    has_key = False

with st.sidebar:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("**Feed filters**")
    topic = st.text_area("Topic query", DEFAULT_QUERY, height=140)
    days = st.slider("Last … days", 7, 365, 60, step=7)
    sort = st.radio("Sort", ["Newest", "Most cited", "Relevance"])
    limit = st.slider("Max papers", 10, 150, 50, step=10)
    picked = st.multiselect("Journals", list(JOURNALS), default=list(JOURNALS))
    want_ai = st.checkbox("AI TL;DRs", value=False, disabled=not has_key,
                          help=None if has_key else
                          "Add ANTHROPIC_API_KEY in app secrets to enable.")
    if st.button("Refresh now"):
        st.cache_data.clear()

since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
issns = tuple(i for n in picked for i in JOURNALS[n])
if not issns:
    st.warning("Pick at least one journal in the sidebar.")
    st.stop()

try:
    papers = fetch_papers(topic.strip(), issns, since, sort, limit)
except Exception as e:
    st.error(f"Couldn't reach Europe PMC: {e}")
    st.stop()

st.caption(f"{len(papers)} papers · since {since} · "
           f"updated {dt.datetime.now():%Y-%m-%d %H:%M}")
if papers:
    df = pd.DataFrame(papers)[["date", "journal", "title", "authors", "doi", "url"]]
    st.download_button("Download CSV", df.to_csv(index=False).encode(),
                       "translation_papers.csv", "text/csv")
st.markdown("<hr>", unsafe_allow_html=True)

for p in papers:
    tldr = ""
    if want_ai:
        try:
            tldr = f'<div class="s"><strong>TL;DR</strong> — {ai_tldr(p["title"], p["abstract"])}</div>'
        except Exception as e:
            tldr = f'<div class="s" style="color:var(--muted)">AI summary unavailable: {e}</div>'
    st.markdown(f"""
    <div class="pub">
      <div class="yr">{p['journal']} · {p['date']}</div>
      <div class="t"><a href="{p['url']}" target="_blank">{p['title']}</a></div>
      <div class="a">{p['authors']}</div>
      {tldr}
    </div>""", unsafe_allow_html=True)
    with st.expander("Abstract"):
        st.write(p["abstract"])

if not papers:
    st.info("No papers matched. Widen the date window or loosen the topic query "
            "in the sidebar.")
