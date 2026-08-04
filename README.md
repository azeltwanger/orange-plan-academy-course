# Orange Plan Course — production repo

Source of truth for **"Financial Planning for Bitcoin Holders"**: scripts, filming plan, and the decision log. Course *content* never lives in the orange-plan app repo (Austin's rule) — it lives here and mirrors to two places:

| Copy | Purpose | Update flow |
|---|---|---|
| **This repo** | Canonical. Fast edits, history, review. | Claude commits here first. |
| **Google Drive → "Orange Plan Course"** | Austin's reading/editing copy, final versions. | Refreshed from here (`tools/split-modules.py` regenerates `modules/`). Austin's Drive edits get pulled back into the repo by Claude. |
| **Honen draft** | What students eventually see. | Claude syncs content changes via the Honen MCP; publishing is manual in the Honen dashboard. |

## Files

- `MASTER-COURSE.md` — **the canonical script.** All 50 lessons, 11 modules, verified against the Honen draft (byte-hash) and the live app code (string audit, last run 2026-07-31). 🎥 markers show every screen-share boundary; `>` flag lines are production notes, never read on camera.
- `SCREEN-SHOOT-LIST.md` — the 19-segment screen-capture run sheet (beats + app-state prep).
- `FILMING-CHECKLIST.md` — production plan: phases, shooting order, per-lesson table.
- `COURSE-IMPROVEMENT-ANALYSIS.md` — decision log; 33 tracked items with full audit history.
- `modules/` — the master split per module (what Drive holds). Generated — edit the master, then run `python3 tools/split-modules.py`.
- `lessons/` — byte-verified verbatim exports of restructured Honen lessons (Modules 4, 8 + major walkthroughs), in Honen's own format. Used for pushing edits back to the Honen draft.
- `tools/fp.py` — Honen-sandbox hash mirror (its md5 hashes UTF-16 code units mod 256); proves local ↔ Honen parity.

## Working rules

1. Edit `MASTER-COURSE.md` (or have Claude do it), commit, then propagate: split → Drive, content → Honen.
2. The couple's canonical numbers (income $190k, surplus $48k/$4k-mo, DTA 40%, DTI ~12%…) are load-bearing across ~15 lessons — change them nowhere without changing them everywhere. See item 29 in the analysis log.
3. Re-run the app-string verification sweep before filming each module (item 32 documents the method).
