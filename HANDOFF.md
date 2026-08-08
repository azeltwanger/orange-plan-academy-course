# Handoff — Orange Plan Academy

**Written 2026-08-08.** Read this first, then `AUSTIN-AUTHORITY.md`, then
`SOURCE-MATERIAL-POLICY.md`. Those two are rules, not context: they outrank
CLAUDE.md, VOICE-GUIDE.md, and any task brief you are handed.

---

## Where the project is

**Content is film-ready.** Two courses inside one Circle space group:

| | Lessons | Runtime |
|---|---|---|
| **Core** — Build Your Bitcoin Financial Plan (required) | 27 teach + 11 captures | 238 min teaching |
| **Advanced Library** (optional, gated) | 14 teach | 107 min |

Nothing has been filmed. Every change so far has cost zero re-records.

**All gates green as of this writing:**

```
python3 tools/check-crossrefs.py    # 0 problems, 52 lessons, modules 0-9
python3 tools/course-metrics.py --check   # STALE: none
python3 tools/check-visuals.py      # 0 orphans, 0 H1 drift
python3 tools/build-scripts.py      # wrote 0 scripts (all protected)
```

Run all four before and after any content change. They are cheap and they
catch the failure modes this project actually has.

---

## The three rules that matter most

**1. Austin's dictated position is the authority.** Full statement in
`AUSTIN-AUTHORITY.md`. The short version: you may correct math and facts (A),
flag contradictions and propose options (B), and you may **never** rewrite a
planning judgment (C). C arrives disguised as B constantly.

Two violations are recorded in `AUTHORITY-FLAGS.md` as the worked examples:
I deleted Austin's "0.01 to 0.02 Bitcoin per transfer" rule of thumb and
substituted a principle of my own, and I narrowed his 10–20% LTV range to
10–15% and re-derived the arithmetic from my number. Both reverted. **The tell
in both cases: "the number might age" is a reason to review it, not a licence
to replace it.** The evergreen-numbers policy covers *law-set* figures
(brackets, limits, exemptions), not Austin's rules of thumb.

**2. Flags no longer block.** Austin, 2026-08-08: *"I can correct things that I
disagree with during dictation."* So write the flag, note it where he will see
it while reading, and keep moving. **Exception: structural choices still block**
— lesson count, order, which module something lives in, what gets its own
video. Those need a re-shoot, not a re-read.

⚠ **The gates are the hole in that safety net.** The 14 advanced gate
conditions live in the *text* layer. Austin never reads them aloud, so the
dictation booth will not catch them. F7 is the one open item where he has to
look at the words directly.

**3. A change must land in every layer.** The standing hazard, and it has bitten
in both directions this week:

```
MASTER-COURSE.md / MASTER-ADVANCED.md   <- doc layer
scripts/            <- teleprompter, PROTECTED (never regenerated)
lesson-text/        <- student read layer
modules/            <- GENERATED from the masters
visuals/            <- graphics prompts, keyed by lesson number
```

Scripts carrying `AUSTIN DICTATION` or `SPOKEN-PROSE VERSION` are never
regenerated, so a master edit does not reach them. And because `modules/` is
generated *from* the masters, a script-only fix leaves the wrong number in the
layer students actually read. Both happened: the US disclaimer was fixed in the
master and stayed 7× in the scripts; the couple's balances were fixed in the
scripts and stayed backwards in the master, generating "5 years" where the
script said 7.5.

**Generator order matters:** `build-module-gates.py` **before**
`split-modules.py`. Reversed, the module gate blocks go stale silently. I made
this mistake and it left 6 of 14 advanced lessons with no reachable gate.

---

## What Austin has decided (do not re-open)

- **LTV: 10–20% depending on risk tolerance.** Not 10–15%.
- **Bridge rule: the ten-year line stays**, with the *why* taught alongside and
  the Module 6 contradiction handled in one line (whether a **date can force the
  sale**).
- **College is a funding stack** against a defined parental commitment, never a
  sticker price to pre-fund. Full position in `COLLEGE-FUNDING-AUTHORITY.md`.
- **That logic generalises** to cars, weddings, a house, repairs, business,
  family support. Six questions, in lesson 2.3.
- **Dual control is a design choice, not a requirement.** Redundancy is required
  at every level; dual control is not. A sound single-signature household
  answers "yes, the owner can spend alone."
- **The estate gate is trigger-driven, not net-worth-driven.**
- **No new core lessons** for the source-material additions. Better decision
  rules and better artifacts instead.
- **The goal feature is not coming back to the app.** 2.3's answer ("you do the
  division, not the app") is permanent.
- **Uploaded docs are ideas, not curriculum.** Never present an old upload as
  verification of current state.

---

## Open — Austin's call

**Structural (these block filming):**

1. **Split lesson 2.3?** It is 14.5 min doing two jobs: fixed dated costs, and
   college. A student with no kids sits through seven minutes that do not apply,
   which is the "does this apply to me" stall verbatim. Splitting adds a lesson.
2. **The next-dollar lesson (4.3) shape.** It currently reads as a strict
   waterfall. Proposal on the table: a stated default order plus the named
   conditions that override it. Highest-traffic decision in the course.
3. **Module 1 has two walkthroughs** (1.4 onboarding, 1.5 baseline) where every
   other module has one.
4. **A8.1's screen capture.** Its script has a substantial screen-share block
   with no capture sheet — `build-shoot-list.py` now reports it as a missing
   sheet. Give it a sheet, or make it A-roll only and drop the ledger walk.
   Folding it into the core estate walkthrough would put advanced content back
   in the core path.

**Non-blocking (he corrects at dictation):** F1 (spoken qualifier on the
transfer threshold), F4 (November vs. October/November), F6, F11, F12–F19. All
in `AUTHORITY-FLAGS.md`.

**Needs his eyes specifically, because the mic will not catch it:** F7, the 14
gate conditions. Roughly a 15-minute read.

---

## Known gaps, honestly stated

- **`core/verified-numbers.md` in the app repo has zero education entries.** The
  college doctrine routes six kinds of figures there (529 limits, the Roth
  rollover conditions, the qualified-student-loan allowance, federal loan
  limits, parent PLUS, net price) and the file answers none of them. Not a
  filming blocker: no college figure is spoken on camera by design. The failure
  is safe — an assistant says "this number needs verification" — but unhelpful.
  ⚠ When filling it, **net price does not belong there.** It is school-specific,
  and a stored national average invites the assistant to quote an average at a
  household choosing between two named schools, which is what the position
  forbids.
- **8 lessons have no graphic:** core 0.2 and 8.3; advanced A1.1, A4.1, A5.3,
  A7.2, A7.3, A7.4. Lesson 1.2 also gained a second graphic in the script today
  (preview vs. the Plan page) with no prompt file.
- **A "how numbers flow between screens" lesson does not exist.** Austin called
  it important. 1.3 explains where the *confidence number* comes from; A1.1
  explains the Bitcoin return model. Neither maps the data flow. Placement is
  undecided. My read: it belongs near 1.3, where the "where did this number come
  from" stall actually happens, and it should probably be a recurring visual
  brought back per module rather than one lesson — the course already proves
  that pattern with the retirement visual.
- **Historical docs read slightly oddly** after the renumber. Sentences of the
  form "what the course said (4.2, now 5.2)" had their numbers remapped so the
  references still resolve. Git history holds the originals.

---

## What the 24 client calls said, because it drives everything

People were **not** overwhelmed by breadth. They stalled on four things:

| Stall | Where it is answered now |
|---|---|
| "Where did this number come from?" | 1.3 labels the first retirement read a **draft**; the ten-year rule carries its *why*; the LTV range shows what each end buys |
| "Does this apply to me?" | Gate box on every module; *"not applicable is a completed line"* in `MODULE-CHECKPOINTS.md` |
| "Is this my plan or a scenario?" | 1.2's three layers, plus **preview vs. Apply** and the Plan page as plan of record |
| "What do I do next?" | One checkpoint per module; top-unchecked-item rule in every walkthrough |

**The calls do not support cutting more content. They support routing people
through it better.** If you are about to trim a lesson, that is probably the
wrong instinct.

---

## Next moves, in order

1. Austin answers the four structural items above.
2. Austin reads the 14 gate conditions (F7).
3. Voice pass on the ~12 scripts changed since the freeze.
4. Build the Circle structure (paste-ready module overview, lessons,
   walkthrough, checkpoint, advanced links).
5. **Film Wave 1 (Modules 0–4).** Only two of the changed scripts live there.
6. Run `USABILITY-TEST-M1-M3.md` against Wave 1 footage rather than delaying it.

Do not start another review round. The last two both found real defects, but
both were triggered by *new input* — the Austin-Authority rule, then the
source-material dump. There is no new input pending. Another pass would be
re-reading, not reviewing.
