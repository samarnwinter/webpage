# Inayat Ullah Irshad — academic website

A multi-page Streamlit site:

| Page | What it does |
|------|--------------|
| **Home** | Intro, research focus, featured paper, the ribosome-lattice signature |
| **Publications** | Your papers with summaries, topic filters, and DOI links |
| **Research** | Themes, the TASEP approach, and your web tools |
| **Literature Feed** | Newest translation papers from top journals (live, Europe PMC) + optional AI summaries |
| **Scheduler** | Meetings, deadlines, and reminders with backup/restore |

Entry point is **`Home.py`**. Your content lives in **`data.py`** — edit that
file to change your bio, links, or publications; you never touch the layout.

---

## How to put this online (start to finish)

You have a repo at `https://github.com/samarnwinter/webpage`. These files
replace what's in it.

### Step 1 — get the files into the repo

**Easiest (no command line):**
1. Go to your repo on github.com.
2. If old files like `dashboard.py` / `app.py` / `older_web` are there and you
   don't need them, open each and delete it (⋯ menu → Delete file → Commit).
3. Click **Add file → Upload files**. Drag in everything from this folder —
   `Home.py`, `data.py`, `style.py`, `requirements.txt`, the `pages` folder,
   the `.streamlit` folder, and `assets`. *(If GitHub won't let you drag the
   folders, create them with **Add file → Create new file** and type e.g.
   `pages/1_Publications.py` as the name — the slash makes the folder.)*
4. Scroll down, write a short message like "new site", click **Commit changes**.

**Or with git on your computer:**
```bash
git clone https://github.com/samarnwinter/webpage.git
cd webpage
# copy all the new files in here, remove the old ones (dashboard.py, app.py, older_web)
git add -A
git commit -m "New multi-page site"
git push
```

### Step 2 — deploy on Streamlit Community Cloud

1. Go to **https://share.streamlit.io** and sign in with GitHub.
2. **Create app** → **Deploy a public app from GitHub**.
3. Fill in:
   - **Repository:** `samarnwinter/webpage`
   - **Branch:** `main`
   - **Main file path:** `Home.py`   ← important: it's `Home.py`, not `dashboard.py`
4. Click **Deploy**. First build takes a minute; then you get a public URL.

That URL *is* your website. Every time you push a change to GitHub, the app
redeploys automatically — no need to redeploy by hand.

> **If you had an app deployed before** and it's stuck on the broken
> `dashboard.py`: open it from your Streamlit workspace, go to
> **Settings → General**, set the main file to `Home.py`, and reboot. Or just
> delete the old app and deploy a fresh one as above.

### Step 3 (optional) — turn on AI summaries

The Literature Feed can add a two-sentence TL;DR under each paper.
1. In Streamlit Cloud: your app → **Settings → Secrets**.
2. Add:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-key"
   ```
3. Save. The **AI TL;DRs** checkbox in the feed's sidebar unlocks.

---

## Editing your content

- **Bio, links, email, publications, research themes** → `data.py` (all in one
  place, with comments). Your email is a placeholder — put your real one in.
- **Colors / fonts / spacing** → `style.py` (the `_CSS` block near the top).
- **Which journals the feed watches** → the `JOURNALS` dict at the top of
  `pages/3_Literature_Feed.py`.
- **Your photo** → see `assets/README.txt`.

## Run it locally first (optional)
```bash
pip install -r requirements.txt
streamlit run Home.py
```
It opens at http://localhost:8501.

## Notes
- The Literature Feed uses the free Europe PMC API (no key). Journal filtering is
  by ISSN, so "Science" and "Science Advances" never collide.
- The Scheduler saves to `data/schedule.json`. On free hosting that file resets
  when the app restarts, so use **Backup & restore** in that page to keep a copy.
