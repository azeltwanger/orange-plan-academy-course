# Handoff — Orange Plan Academy

**Rewritten 2026-08-08** after the repo-parity + client-call pass. Read this
first, then `AUSTIN-AUTHORITY.md`, then `SOURCE-MATERIAL-POLICY.md`. Those two
are rules, not context: they outrank CLAUDE.md, VOICE-GUIDE.md, and any task
brief you are handed.

---

## Where the project is

**Content is structurally settled. It is NOT all cleared for filming** — the
production checklist generates its own blocker list and currently refuses to say
FINAL.

> ⚠ **No counts, runtimes or command lists live in this file, deliberately.**
> This is the first document every new session reads, and a hand-typed copy here
> is the next stale copy. It said 242 core minutes while the generated README
> block said 244, and it listed four gate commands after there were five. Both
> within a day of being written.
>
> | You want | Read |
> |---|---|
> | Current lesson counts, runtimes, capture counts | the **metrics block in `README.md`** (generated) |
> | The commands to run before and after a change | **Working rules** in `README.md` |
> | What is filmable today and what is blocked | **`PRODUCTION-CHECKLIST.md`** (generated) |
> | What to record, in order | **`DICTATION-ORDER.md`** (generated) |
> | What to capture on screen | **`SCREEN-SHOOT-LIST.md`** (generated) |
> | The paste-ready Circle build | **`CIRCLE-STRUCTURE.md`** (generated) |

**This file holds decisions and unresolved issues. Nothing else.** If you find
yourself typing a number into it, that number belongs in a generated block.

Nothing has been filmed. Every change so far has cost zero re-records.

## The three rules that matter most

**1. Austin's dictated position is the authority.** Full statement in
`AUSTIN-AUTHORITY.md`. The short version: you may correct math and facts (A),
flag contradictions and propose options (B), and you may **never** rewrite a
planning judgment (C). C arrives disguised as B constantly.

Two violations are recorded in `AUTHORITY-FLAGS.md` as the worked examples: I
deleted Austin's "0.01 to 0.02 Bitcoin per transfer" rule of thumb and
substituted a principle of my own, and I narrowed his 10–20% LTV range to 10–15%
and re-derived the arithmetic from my number. Both reverted. **The tell in both
cases: "the number might age" is a reason to review it, not a licence to replace
it.** The evergreen-numbers policy covers *law-set* figures (brackets, limits,
exemptions), not Austin's rules of thumb.

**2. Flags no longer block.** Austin, 2026-08-08: *"I can correct things that I
disagree with during dictation."* So write the flag, note it where he will see it
while reading, and keep moving. **Exception: structural choices still block** —
lesson count, order, which module something lives in, what gets its own video.
Those need a re-shoot, not a re-read.

⚠ **The gates are the hole in that safety net.** The 14 advanced gate conditions
live in the *text* layer. Austin never reads them aloud, so the dictation booth
will not catch them. F7 is the one open item where he has to look at the words
directly.

**3. A change must land in every layer.** The standing hazard:

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
layer students actually read. **Both directions have bitten, twice each.** The
2026-08-08 pass found two more: 2.3's master and lesson text still taught the
position the script had replaced, and A7.4's master still refused to give the
number the script gives.

**Generator order matters:** `build-module-gates.py` **before**
`split-modules.py`. Reversed, the module gate blocks go stale silently.

**Every generator is now idempotent.** Running the full pipeline twice produces a
zero-byte diff across the masters, `modules/`, `scripts/` and all six generated
documents. It was not: `build-production-checklist.py` preserved its own warning
block as "head" and appended a fresh one every run, which is why seven identical
warnings had stacked up in the file.

---

## What Austin has decided (do not re-open)

- **LTV: 10–20% depending on risk tolerance.** Not 10–15%.
- **Transfer threshold: about 0.01 to 0.02 BTC minimum per transfer**, bounded by
  current fees and exchange exposure. Restored in every layer 2026-08-08.
- **Bridge rule: the ten-year line stays**, with the *why* taught alongside and
  the Module 6 contradiction handled in one line (whether a **date can force the
  sale**).
- **College is a funding stack** against a defined parental commitment, never a
  sticker price to pre-fund. Full position in `COLLEGE-FUNDING-AUTHORITY.md`.
- **That logic generalises** to cars, weddings, a house, repairs, business, family
  support. Six questions, now in lesson 2.3.
- **College is optional and stays inside Module 2** as lesson 2.4. Not the
  Advanced Library — it is conditional, not advanced.
- **Dual control is a design choice, not a requirement.** Redundancy is required
  at every level; dual control is not.
- **The estate gate is trigger-driven, not net-worth-driven** — and there is now
  exactly **one** gate, the nine triggers and four levels in the core walkthrough.
- **No new core lessons** for the source-material additions.
- **The goal feature is not coming back to the app.** 2.3's answer ("you do the
  division, not the app") is permanent.
- **Uploaded docs are ideas, not curriculum.**

---

## Resolved by the 2026-08-08 pass (was "open — Austin's call")

All four structural blockers from the previous handoff are closed:

1. **Split 2.3?** Done. 2.3 is the required six-questions lesson (~10 min); **2.4
   is an optional college lesson** (~7 min); the walkthrough moved to 2.5. Both
   are recorded in **one sitting**, cut immediately before *"College is a funding
   stack, not a bill you prepay"* — so the split costs no extra production.
2. **The next-dollar lesson (4.3).** Not resolved by rewriting — **marked HOLD FOR
   REDICTATION (F22)**. The strict-waterfall text is preserved verbatim; the
   intended shape is written down; the order and wording are Austin's to give.
3. **Module 1's two walkthroughs.** Merged into one capture sheet with a cut point
   after onboarding. Still two published lessons, filmed once.
4. **A8.1's screen capture.** Removed. The lesson is **text-only for v1**, its
   embedded screen-share block is gone (so the phantom capture no longer shows as
   a missing sheet), and its legal claims are **blocked pending estate-attorney
   review** — see Part 4b of `LEGAL-REVIEW-PACKET.md`.

---

## Open — Austin's call

**Blocking (a re-shoot, not a re-read):**

1. **F22 · 4.3, the next-dollar lesson.** Highest-traffic decision in the course.
   Needs his dictation: the default order, the presumptions, the overriding
   conditions. Everything downstream of it — the proposed title, the completion
   line, two Module 4 checkpoint lines — is deliberately left alone until then.
2. **F20 · the 7-to-10-year funding lane.** The 2.3 dictation names 0–1, 1–3, 3–7
   and 10+. Nothing covers 7 to 10. One sentence at the mic settles it; guessing
   would either re-impose the table he replaced or loosen a rule he kept.
3. **F23 · Module 2's ordering.** College sits at 2.4, walkthrough at 2.5, and the
   walkthrough hand-off is on 2.3 (the last *required* lesson) worded to work on
   both paths. The alternative — college last at 2.5 — is cheap to switch now.

**Needs his eyes specifically, because the mic will not catch it:** F7, the 14
gate conditions. Roughly a 15-minute read.

**Non-blocking (he corrects at dictation):** F21 (the inserted number-flow section
in 1.3 — keep, rewrite, or cut), F1, F4, F6, F11, F13–F19. All in
`AUTHORITY-FLAGS.md`.

**Not Austin's call, but blocking publication:** the A8.1 estate-attorney review.

---

## Known gaps, honestly stated

- **`core/verified-numbers.md` in the app repo has zero education entries.** The
  college doctrine routes six kinds of figures there and the file answers none.
  Not a filming blocker: no college figure is spoken on camera by design. ⚠ When
  filling it, **net price does not belong there** — it is school-specific, and a
  stored national average invites the assistant to quote an average at a household
  choosing between two named schools.
- **A known layer-parity gap, unfixed on purpose.** The *"which modules are
  US-shaped"* breakdown exists only in the 0.1 **script**, not in
  `MASTER-COURSE.md`. `build-dictation-order.py` prints a `!! PARITY` warning on
  every run rather than hiding it. Fixing it means moving dictated prose into the
  master, which is a content decision, not a mechanical one.
- **8 lessons have no graphic:** core 0.2 and 8.3; advanced A1.1, A4.1, A5.3,
  A7.2, A7.3, A7.4. Lesson 1.2 also has a second graphic in the script (preview
  vs. the Plan page) with no prompt file.
- **`AI-FACTS.md` was remapped 2026-08-08.** Nine of its fifteen lesson pointers
  were wrong; three pointed at a module that no longer exists and six resolved to
  a *different* lesson, which `check-crossrefs.py` cannot catch because the number
  was valid. If you touch that file, verify every row against the master titles.
- **Historical docs read slightly oddly** after the renumbers. That is deliberate.
  `COURSE-IMPROVEMENT-ANALYSIS.md` and the archived `FILMING-CHECKLIST.md` are
  excluded from `check-crossrefs.py` because their references to retired numbers
  are correct in their own context.

---

## Production sources: three, and only three

`FILMING-CHECKLIST.md` was **retired 2026-08-08** and carries a banner saying so.
It was the most dangerous file in the repo: it disagreed with the measured capture
count, seeded a stale contribution breakdown, referred to a module that no longer
existed, and still told you to "decide the 2.3 rebuild" after 2.3 had been rebuilt.

| Use | File | Regenerate with |
|---|---|---|
| What to film, in what order, what is blocked | `PRODUCTION-CHECKLIST.md` | `tools/build-production-checklist.py` |
| What to dictate, in what order, with runtimes | `DICTATION-ORDER.md` | `tools/build-dictation-order.py` |
| What to capture on screen, and the app state each needs | `SCREEN-SHOOT-LIST.md` | `tools/build-shoot-list.py` |

All three build from the same lesson manifest — the masters plus the capture
sheets. `FILM-ORDER.md` still exists as a flat index and stamps a banner saying it
is not a production source.

**The production checklist cannot lie about readiness any more.** Its status block
is generated: it prints FINAL only when no layer carries a do-not-film, rebuild,
redictation or legal-review marker. Today it prints **NOT CLEARED — 5 open
blockers** across 4.3 and A8.1.

---

## What the 24 client calls said, because it drives everything

People were **not** overwhelmed by breadth. They stalled on four things:

| Stall | Where it is answered now |
|---|---|
| "Where did this number come from?" | **1.3's number-flow frame** — CALCULATED FROM · EDIT SOURCE · THIS AFFECTS — recalled in all eight remaining walkthroughs. Plus 1.3 labelling the first retirement read a **draft** |
| "Does this apply to me?" | Gate box on every module; *"not applicable is a completed line"*; **college is now genuinely skippable**; Module 7 and 8 completion paths are conditional on setup |
| "Is this my plan or a scenario?" | 1.2's three layers, plus **preview vs. Apply** and the Plan page as plan of record |
| "What do I do next?" | One checkpoint per module; top-unchecked-item rule in every walkthrough |

**The calls do not support cutting more content. They support routing people
through it better.** If you are about to trim a lesson, that is probably the wrong
instinct.

---

## Next moves, in order

1. **Austin dictates 4.3** (F22). It is the only content blocker left.
2. Austin settles F20 (the 7–10 band) and F23 (Module 2 ordering) — one sentence
   each.
3. Austin reads the 14 gate conditions (F7).
4. Send A8.1 to an estate attorney (`LEGAL-REVIEW-PACKET.md`, Part 4b).
5. Voice pass on the scripts changed since the freeze.
6. Build the Circle structure. **Module 2 needs the optional-lesson framing:**
   *"Optional: College funding stack — complete this when you have children or
   another education goal. Otherwise your Module 2 plan is complete without it."*
7. **Film Wave 1 (Modules 0–4)** — everything except 4.3, which is blocked.
8. Run `USABILITY-TEST-M1-M3.md` against Wave 1 footage rather than delaying it.

Do not start another review round. The last three all found real defects, but all
three were triggered by *new input* — the Austin-Authority rule, then the
source-material dump, then the repo audit. There is no new input pending. Another
pass would be re-reading, not reviewing.
