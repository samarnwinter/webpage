import json
import datetime as dt
from pathlib import Path
import streamlit as st
import style

style.setup("Scheduler")

DATA = Path("data/schedule.json")
KINDS = {"Meeting": "🟢", "Deadline": "🔴", "Reminder": "🟡", "Seminar": "🔵"}


# --------------------------------------------------------------------------- #
# storage  (JSON file + session mirror; export/import for durable backup)
# --------------------------------------------------------------------------- #
def load():
    try:
        return json.loads(DATA.read_text())
    except Exception:
        return []


def save(items):
    try:
        DATA.parent.mkdir(exist_ok=True)
        DATA.write_text(json.dumps(items, indent=2))
    except Exception:
        pass  # read-only filesystem; session state still holds the data


if "events" not in st.session_state:
    st.session_state.events = load()


def commit():
    st.session_state.events.sort(key=lambda e: e["when"])
    save(st.session_state.events)


# --------------------------------------------------------------------------- #
# header
# --------------------------------------------------------------------------- #
st.markdown('<span class="eyebrow">Stay on top of it</span>', unsafe_allow_html=True)
st.markdown("# Scheduler")
st.markdown("Track meetings, deadlines, and reminders. Everything is private to "
            "this app.")

# ---- add form ------------------------------------------------------------ #
with st.form("add", clear_on_submit=True):
    st.markdown("**Add an entry**")
    c1, c2, c3 = st.columns([3, 1.2, 1.2])
    title = c1.text_input("What", placeholder="e.g. Group meeting with Prof. Sharma")
    date = c2.date_input("Date", dt.date.today())
    time = c3.time_input("Time", dt.time(10, 0))
    c4, c5 = st.columns([1.2, 3])
    kind = c4.selectbox("Type", list(KINDS))
    note = c5.text_input("Note (optional)", placeholder="Agenda, location, link…")
    if st.form_submit_button("Add to schedule") and title:
        st.session_state.events.append({
            "title": title, "kind": kind, "note": note,
            "when": dt.datetime.combine(date, time).isoformat(), "done": False})
        commit()
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------------------------------- #
# grouped list
# --------------------------------------------------------------------------- #
now = dt.datetime.now()
today = now.date()
week_end = today + dt.timedelta(days=7 - today.weekday())


def bucket(when: dt.datetime):
    d = when.date()
    if when < now and not d == today:
        return "Past"
    if d == today:
        return "Today"
    if d <= week_end:
        return "This week"
    return "Later"


ORDER = ["Today", "This week", "Later", "Past"]
groups: dict[str, list] = {k: [] for k in ORDER}
for i, e in enumerate(st.session_state.events):
    groups[bucket(dt.datetime.fromisoformat(e["when"]))].append((i, e))

if not st.session_state.events:
    st.info("Nothing scheduled yet. Add your first meeting or deadline above.")

for g in ORDER:
    if not groups[g]:
        continue
    st.markdown(f"### {g}")
    for i, e in groups[g]:
        when = dt.datetime.fromisoformat(e["when"])
        c1, c2, c3 = st.columns([0.08, 0.77, 0.15])
        with c1:
            if st.checkbox("Mark done", value=e["done"], key=f"chk{i}",
                           label_visibility="collapsed"):
                if not e["done"]:
                    st.session_state.events[i]["done"] = True
                    commit(); st.rerun()
            elif e["done"]:
                st.session_state.events[i]["done"] = False
                commit(); st.rerun()
        with c2:
            strike = "text-decoration:line-through;opacity:.5" if e["done"] else ""
            note = f' · <span style="color:var(--muted)">{e["note"]}</span>' if e["note"] else ""
            st.markdown(
                f'<div style="{strike}">{KINDS[e["kind"]]} '
                f'<strong>{e["title"]}</strong>{note}<br>'
                f'<span class="doi" style="color:var(--muted)">'
                f'{when:%a %d %b · %H:%M}</span></div>', unsafe_allow_html=True)
        with c3:
            if st.button("Remove", key=f"del{i}"):
                st.session_state.events.pop(i)
                commit(); st.rerun()
    st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------------------------------- #
# backup  (durable across restarts — download here, re-upload anytime)
# --------------------------------------------------------------------------- #
with st.expander("Backup & restore"):
    st.caption("On free hosting the app's storage resets when it restarts, so "
               "download a copy to keep your schedule safe. Re-upload it here to "
               "restore.")
    if st.session_state.events:
        st.download_button("Download schedule (.json)",
                           json.dumps(st.session_state.events, indent=2),
                           "schedule.json", "application/json")
    up = st.file_uploader("Restore from a .json backup", type="json")
    if up and st.button("Load this backup"):
        try:
            st.session_state.events = json.loads(up.read())
            commit(); st.success("Schedule restored."); st.rerun()
        except Exception as e:
            st.error(f"Couldn't read that file: {e}")
