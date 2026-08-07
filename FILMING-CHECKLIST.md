# Orange Plan Course — Filming Checklist & Production Plan

**Source of truth: `MASTER-COURSE.md` (core) and `MASTER-ADVANCED.md` (library).**

| | Teach lessons | Runtime |
|---|---|---|
| **Core** — Build Your Bitcoin Financial Plan | 27 | ~246 min |
| **Advanced Library** — optional, gated | 10 | ~91 min |

Plus 9 core walkthroughs and 1 external demo, narrated off the DO/SEE/⚠ sheets rather than read.

⚠ Recording order lives in `DICTATION-ORDER.md`, which is **generated**. Run `python3 tools/build-dictation-order.py` before filming so you are not recording from an obsolete order.

Lesson types — this drives the whole shooting plan:

| Type | Count | What it means on set |
|---|---|---|
| 🎙 Talking head (teleprompter) | 27 core + 8 advanced | Camera only. Batch these. |
| 🖥 Screen share (walkthrough) | 9 core + 1 external demo | Screen recording with live narration. App state must be seeded first. **Film one continuous capture per module and decide the cut in the edit** — `✂ CUT POINT` markers on the sheets show where a split is safe. |
| 🎙+🖥 Hybrid | 2, both in the Advanced Library | Teach section on camera, then an app section on screen. The cut point is the 🎥 marker in the master. The core course has no hybrids left; Modules 4 and 8's were retired in favour of whole-module walkthroughs. |

---

## Phase 0 — Before you film anything (one-time prep)

- [ ] **Seed the demo account with the couple's canonical numbers.** Every worked example on camera must match the app on screen. The fact sheet (all re-derived and verified 2026-07-30):
  - Income $190,000/yr · taxes $40,000 · living $80,000 · debt service $22,000 ($1,850/mo)
  - **Surplus $48,000/yr = $4,000/mo** (pre-routing — contributions are NOT subtracted)
  - Waterfall: 401(k) $1,000 + HSA $300 + Roth $583 + Bitcoin/taxable **$2,117/mo**
  - Debt: $280,000 mortgage @3.25% + $18,000 car @7% → DTA 40%, DTI ~12%
  - Assets: $175k BTC (1.75 BTC) + $90k funds + $30k cash + $450k house = $745,000
  - Retirement-era demo (Modules 6+): $80,000 spending · $120,000 reserve (18 mo) · **$600K taxable BTC · $400K traditional** · $200K Roth · SS $51,600/yr ($4,300/mo). ⚠ Taxable BTC is $600K, not $400K — 7.3 divides it by $80,000 to get ~7.5 years, and it must match the seeded demo on screen.
- [x] **Evergreen numbers policy (replaces the old item 11).** The course must outlive the tax year, so: (1) never speak a law-set number (bracket, limit, exemption, RMD age) as a fact — the scripts are already written this way; (2) worked-example figures are tilde-marked snapshots with a "these move every year" frame — leave them, say the frame; (3) when a law number is on screen during capture, don't zoom or dwell, and refer to it as "the current number the app shows." The app updates with the law; the video doesn't have to.
- [ ] **Decide the lesson renames** (item 20 — plain-language v2 titles are drafted and awaiting your go). Film with FINAL titles; renaming after filming means re-recording intros.
- [ ] **Decide the 3.3 rebuild** (item 18 — Life-Events checklist redesign is spec'd, 3 questions open). If you're rebuilding it, do it before filming Module 2.
- [x] **Retirement Income page push** — LANDED (commit 073fdf0, 2026-07-29). Walkthrough 7.7 Step 5 and lesson 7.4's app pointer rewritten against the new UI and re-verified.
- [ ] Set the app to a clean browser profile: no extensions, no bookmarks bar, notifications off, 1080p+ window.
- [ ] Print the three toolkit PDFs (06 Heir Letter, 07 Family Custody Map, 08 Executor Packet) — they appear on camera in 8.5, 9.1, 9.3.

## Phase 1 — Teleprompter prep (per lesson, ~10 min each)

The master file is written to be read aloud, but strip these before loading the prompter:

- [ ] Delete everything that isn't spoken: the `**By the end of this lesson**` outcomes block, all `⚠` production notes (those are FOR you, not BY you), tables, and the `*`TYPE`*` metadata line.
- [ ] Tables become spoken lines. Rule of thumb: read the pattern, not the cells ("under 36 percent is healthy, over 43 is high-risk") and let the screen carry the full table.
- [ ] Mark the hybrid cut point: everything after **"Now put it in the app"** moves to the screen-capture script.
- [ ] Numbers: write them out the way you say them ("forty-eight thousand a year — four grand a month").
- [ ] Keep the hand-off sentence at the end of each lesson — they're the course's connective tissue.

## Phase 2 — Shooting order

**Batch by setup, not by course order.** Same outfit + lighting within a module so hybrid A-roll cuts match.

1. **Talking-head batches (camera days).** Film in course order within each day for narrative momentum — the couple's story builds. Suggested days:
   - Day 1: Modules 0–2 talk lessons (1.1 → 3.3) — ~6,300 words ≈ 40 min narration
   - Day 2: Modules 3–5 talk + hybrid A-roll (4.1 → 6.4) — ~9,700 words ≈ 63 min
   - Day 3: Modules 6–7 (7.1 → 8.3) — ~7,600 words ≈ 49 min
   - Day 4: Modules 8–10 talk + hybrid A-roll (9.1 → 11.1) — ~10,100 words ≈ 65 min
2. **Screen-capture batches (app days).** App state carries forward lesson to lesson — capture in course order: 2.4 → 3.4 → 4.6 → 5.x app segments → 6.5 → 7.7 → 8.4/8.5 → 9.x app segments → 10.4 → 11.2.
3. **8.4 External demo** needs physical props (hardware wallet) — its own mini-shoot.

## Phase 3 — Per-lesson checklist

Runtime = words ÷ 155 wpm (spoken), low end. Screen lessons run longer than their word count (clicking, waiting, reading the UI) — the high end is closer.


### Module 0 — Start Here

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 1.1 | How to use this course | 🎙 Talk | 1,012 | 7–10 min |  |

### Module 1 — Foundation

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 2.1 | What to gather before you build the plan | 🎙 Talk | 484 | 3–5 min |  |
| ☐ | 2.2 | Set your growth and inflation assumptions | 🎙 Talk | 638 | 4–7 min |  |
| ☐ | 2.3 | Read your retirement date and confidence number | 🎙 Talk | 937 | 6–10 min |  |
| ☐ | 2.4 | Walkthrough: set up your plan and build your baseline in Orange Plan | 🖥 Screen | 3,432 | 22–35 min | Longest in course. Two sessions: Part A (onboarding) + Part B (baseline lap). Fresh demo account required. |

### Module 2 — Cash Flow + Reserve

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 3.1 | Find your surplus and your two spending numbers | 🎙 Talk | 824 | 5–9 min |  |
| ☐ | 3.2 | Size your cash reserve in months of spending | 🎙 Talk | 711 | 5–7 min |  |
| ☐ | 3.3 | Fund known future costs: college, cars, a house, repairs | 🎙 Talk | 648 | 4–7 min | ⚠ Hold until item 18 decision (rebuild spec drafted). |
| ☐ | 3.4 | Walkthrough: build cash flow and reserve in Orange Plan | 🖥 Screen | 1,752 | 11–18 min |  |

### Module 3 — Allocation & Next-Dollar

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 4.1 | Pick your Bitcoin allocation tier | 🎙 Talk | 720 | 5–7 min |  |
| ☐ | 4.2 | Stress-test the allocation you can actually hold | 🎙 Talk | 550 | 4–6 min |  |
| ☐ | 4.3 | Split your money into Reserve, Bridge, and Legacy | 🎙 Talk | 612 | 4–6 min | Sidebar in app may still read Reserve/Bridge/Forever — verify "Legacy" rename landed before capture. |
| ☐ | 4.4 | Order your contributions: which account gets funded first | 🎙 Talk | 615 | 4–6 min |  |
| ☐ | 4.5 | Asset location: which account each holding belongs in | 🎙 Talk | 687 | 4–7 min |  |
| ☐ | 4.6 | Walkthrough: route it in Orange Plan | 🖥 Screen | 1,881 | 12–19 min |  |

### Module 4 — Debt Strategy

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 5.1 | Set your debt ceiling: debt-to-income and debt-to-assets | 🎙+🖥 Hybrid | 1,121 | 7–12 min | Cut at "Now put it in the app". Demo account needs both debts entered for Step 2–3 reads. |
| ☐ | 5.2 | Size the LTV cushion on a Bitcoin-backed loan | 🎙+🖥 Hybrid | 864 | 6–9 min |  |
| ☐ | 5.3 | The four ways debt can build wealth | 🎙+🖥 Hybrid | 931 | 6–10 min |  |
| ☐ | 5.4 | Give every debt a payoff decision | 🎙+🖥 Hybrid | 1,133 | 7–12 min |  |
| ☐ | 5.5 | Check your work | 🖥 Screen | 418 | 3–4 min | Nav title in Honen still reads "Walkthrough:" — cosmetic, rename in UI. |

### Module 5 — Tax Strategy

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 6.1 | Cost basis: what you paid, and how to reconstruct it | 🎙 Talk | 718 | 5–7 min |  |
| ☐ | 6.2 | Taxable, tax-deferred, and Roth: bracket windows and state taxes | 🎙 Talk | 1,425 | 9–15 min |  |
| ☐ | 6.3 | RMD risk and Roth conversions | 🎙 Talk | 957 | 6–10 min |  |
| ☐ | 6.4 | Harvesting losses and gains | 🎙 Talk | 1,115 | 7–12 min |  |
| ☐ | 6.5 | Walkthrough: model it in Orange Plan | 🖥 Screen | 1,622 | 10–17 min | Run transaction import FIRST or harvest rows render empty (its own pre-flight says so). Includes new "Fixing a lot that came in wrong" section. |

### Module 6 — Retirement Income

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 7.1 | Spending, floor, and the gap | 🎙 Talk | 586 | 4–6 min |  |
| ☐ | 7.2 | The bridge years | 🎙 Talk | 550 | 4–6 min |  |
| ☐ | 7.3 | Health insurance between retiring and Medicare | 🎙 Talk | 767 | 5–8 min |  |
| ☐ | 7.4 | Set your withdrawal order and refill rule | 🎙 Talk | 891 | 6–9 min |  |
| ☐ | 7.5 | Sell, borrow, or hold: funding a year of spending | 🎙 Talk | 733 | 5–8 min |  |
| ☐ | 7.6 | Guardrails: how much you can spend each year | 🎙 Talk | 837 | 5–9 min |  |
| ☐ | 7.7 | Walkthrough: build the paycheck in Orange Plan | 🖥 Screen | 1,901 | 12–20 min | Gated on retirement phase: demo account age ≥ retirement age. Run Monte Carlo before capture. ✅ Retirement Income push landed (073fdf0) — Step 5 rewritten for the new Withdrawal order section 2026-07-31. |

### Module 7 — Custody

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 8.1 | Custody: the five questions and choosing your level | 🎙 Talk | 1,796 | 12–19 min |  |
| ☐ | 8.2 | Set up a hardware wallet and test recovery | 🎙 Talk | 658 | 4–7 min |  |
| ☐ | 8.3 | Single points of failure, account hardening, and scams | 🎙 Talk | 757 | 5–8 min |  |
| ☐ | 8.4 | External demo: hardware wallet setup + exchange hardening | 🖥 Screen | 837 | 5–9 min | Physical hardware wallet on camera. No app. |
| ☐ | 8.5 | Walkthrough: document your custody map in Orange Plan | 🖥 Screen | 1,816 | 12–19 min |  |

### Module 8 — Estate & Inheritance

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 9.1 | The executor, the four legal documents, and choosing an estate attorney | 🎙+🖥 Hybrid | 2,139 | 14–22 min | Longest talk section (2,139 w). Strongest split candidate if it drags on the prompter. |
| ☐ | 9.2 | Split access so no one person holds everything | 🎙 Talk | 888 | 6–9 min |  |
| ☐ | 9.3 | The heir letter | 🎙+🖥 Hybrid | 1,397 | 9–14 min | Cloud mode + 1 email contact required BEFORE capture (pre-flight). |
| ☐ | 9.4 | The 90-day dead man's switch | 🎙+🖥 Hybrid | 728 | 5–8 min |  |
| ☐ | 9.5 | Insurance: term life, disability, umbrella, and when to stop | 🎙 Talk | 1,106 | 7–11 min |  |
| ☐ | 9.6 | Advanced: do you need a trust, and which one? | 🎙+🖥 Hybrid | 1,887 | 12–19 min | Advanced/skimmable lesson — consider a visual "optional" badge on the thumbnail. |
| ☐ | 9.7 | Check your work | 🖥 Screen | 685 | 4–7 min | Nav title still reads "Walkthrough:" in Honen UI. |

### Module 9 — Maintenance (Capstone)

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 10.1 | A review is not a rebuild: the two rhythms | 🎙 Talk | 546 | 4–6 min |  |
| ☐ | 10.2 | The monthly pass | 🎙 Talk | 725 | 5–7 min |  |
| ☐ | 10.3 | The annual review: six areas to check | 🎙 Talk | 918 | 6–9 min |  |
| ☐ | 10.4 | Walkthrough: run the annual review in Orange Plan | 🖥 Screen | 1,800 | 12–19 min | Needs: a flagged review item on a linked account, transactions ready to enter, visible timer. |

### Module 10 — Your Financial Plan Review

| ☐ | # | Lesson | Type | Words | Est. runtime | Notes |
|---|---|---|---|---|---|---|
| ☐ | 11.1 | How to read a financial plan | 🎙 Talk | 1,081 | 7–11 min |  |
| ☐ | 11.2 | Walkthrough: walk your report in Orange Plan | 🖥 Screen | 1,552 | 10–16 min | Needs: 1 saved scenario + fresh confidence check, or 3 report sections won't render. |

---

## Recording hygiene

- **File naming:** `M04-L2-A-take3.mp4` (module, lesson, A=camera/B=screen, take). Future-you in the edit bay will thank you.
- **Teleprompter pace:** your natural ~155 wpm. If a lesson runs past ~8 prompter minutes, break at a `##` section heading and treat it as two segments.
- **Flub protocol:** clap, 2-second pause, restart the paragraph. Never restart the lesson.
- **Screen capture:** record at least 5 seconds of stillness before the first click and after the last — edit handles.
- **Never on camera:** real account balances, real seed words (obviously), the plaintext backup-passphrase prompt (10.4 and 8.5 scripts already call this out — type it off-camera or use a visible throwaway).
- **Don't speak numbers that age:** the estate exemption, current tax brackets, today's BTC price. The scripts are already written to point at the screen instead — trust them.

## After each module is filmed

- [ ] Check the box in Phase 3 above.
- [ ] Note any place you deviated from the script — those edits go back into MASTER-COURSE.md so the doc stays the source of truth.
- [ ] If the app UI changed since the script was audited (2026-07-30), flag it rather than improvising labels on camera — every UI string in the walkthroughs was verified against the codebase.
