# Protein Synthesis Paper Tracker

A Streamlit dashboard that shows the latest **protein-synthesis / translation**
papers from top journals, pulled live from the **Europe PMC** REST API
(free, no API key). Abstracts serve as the quick summary; an optional AI TL;DR
is available if you add an Anthropic API key.

## Deploy on Streamlit Community Cloud

1. Put `app.py`, `requirements.txt`, and this `README.md` in your GitHub repo.
2. Go to https://share.streamlit.io → **New app** → point it at your repo and
   `app.py`. It builds and gives you a public URL.
3. Every time you `git push`, the app redeploys automatically.

## How "latest" works

The app queries Europe PMC on page load and caches results for 6 hours
(`CACHE_TTL`), so visitors always see recent papers without hammering the API.
The **🔄 Refresh now** button forces an immediate re-query. No cron/scheduler
needed for a webpage; the on-load fetch is the refresh.

## Customizing

All knobs are at the top of `app.py`:

- **`JOURNALS`** — add/remove journals. Each is a display name mapped to its
  ISSNs (print + electronic). Filtering is by ISSN so titles like "Science" vs
  "Science Advances" never collide. To add a journal, search "<name> ISSN".
- **`DEFAULT_QUERY`** — the topic search in Europe PMC boolean syntax. Edit it
  in the file or live in the sidebar. Supports `AND`, `OR`, `NOT`, quoted
  phrases, and field tags like `TITLE:"..."` or `ABSTRACT:"..."`.
- Sidebar controls date window, sort (newest / most cited / relevance),
  max papers, and journal subset.

## Optional: AI TL;DRs

1. `pip`/deploy already includes `anthropic`.
2. In Streamlit Cloud: **App → Settings → Secrets**, add:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
3. The "Add AI TL;DRs" checkbox unlocks; each paper gets a 2-sentence summary
   (model set by `SUMMARY_MODEL`, default a cheap/fast Haiku). Check current
   model strings at https://docs.claude.com.

## Notes / extensions

- **Preprints:** Europe PMC also indexes bioRxiv/medRxiv. Add
  `src:PPR` handling or a bioRxiv toggle if you want preprints alongside
  published papers.
- **Email digest:** for a scheduled push (not just a webpage), a GitHub Actions
  cron job can run the same query and email/Slack new hits.
- Data source contract verified against the Europe PMC RESTful Web Service docs;
  the search endpoint, `resultType=core` (returns `abstractText`), `sort_date:y`,
  and `FIRST_PDATE:[... TO 3000]` filters are all documented and stable.
