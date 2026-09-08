# Course analysis: claim sourcing + simplification

Course: **Financial Planning for Bitcoin Holders** (Honen `6a64e9bb11e32569d5e8a337`)
Measured 2026-07-29 against the live course revision: 11 modules, 50 lessons,
52,634 words, 5,924 sentences.

**This is the one working file.** All findings live here. The other files in this
directory are tooling, not findings: `build-export.sh` (rebuilds the export),
`audit-ui-labels.sh` + `walkthrough-ui-labels.txt` (re-runs the app audit),
`README.md` (export mechanics and why the file can't be moved automatically).

---

## Action list

Status as of 2026-07-29. Update this table as things land — everything below it
is the supporting evidence.

**Standing policy (Austin, 2026-07-29): minor problems get fixed directly in
the course as they're found.** Minor = mechanical, factual, or consistency
fixes — broken escapes, stale hand-offs, wrong labels, missing one-line
clarifications Austin already asked for. Not minor = anything touching voice,
worked-example numbers, lesson structure, or naming systems; those still land
here as flagged items. Every direct fix is recorded in the master file at the
lesson it touched.

| # | Action | Where | Status |
| --- | --- | --- | --- |
| 1 | ~~Normalise Save as PDF → Download PDF~~ | walkthroughs | ❌ **WITHDRAWN — false positive.** "Save as PDF" is the browser print dialog, not an app button. Course is correct. |
| 2 | ~~Normalise Spending & Reserve → Cash Flow & Reserve~~ | walkthroughs | ❌ **WITHDRAWN — false positive.** It's a course section heading, already paired with the real nav path. |
| 3 | Fix **"Bitcoin at 40% forever (its historical rate)"** | Module 1 | ✅ **DONE 2026-07-29** — now reads "(a deliberately conservative number, well under what Bitcoin has actually done)" |
| 4 | ~~Add "where this lives" lines~~ | ~~Modules 4, 5, 8~~ | ✅ **Fully withdrawn** — Module 8's walkthroughs name **Protect** throughout, same filename-vs-nav artifact — walkthroughs name real nav paths (Strategy → Debt, Strategy → Tax) throughout; my reverse audit matched component *filenames* (Liabilities.jsx, TaxCenter.jsx), not UI. Only Module 8 still unverified. |
| 5 | Split the 3,172-word estate walkthrough in two | Module 8 | ☐ ready |
| 6 | Add drawdown-trend data (−93/−86/−84/−77) | Module 1 or 3 | ☐ ready |
| 7 | ~~Eyeball the Tax funding control~~ | app + Module 5 | ✅ **resolved** — walkthrough 5.3 names the picker and both options; matches engine behavior |
| 8 | Add "How to read the app" lesson (tooltips, gear, where numbers live) | Module 0/1 | ☐ needs decision |
| 9 | Re-run `audit-ui-labels.sh`; re-check the ⚠ income-floor note | Module 6 | ☐ **blocked** — Retirement Income change in flight |
| 10 | Add "where this lives" for Module 6 | Module 6 walkthrough | ☐ **blocked** — same |
| 11 | Verify tax specifics (brackets, RMD ages, estate exemptions) vs 2026 tables | Modules 5, 8 | ☐ not started |
| 12 | Send 3–5 YouTube transcripts for voice matching | — | ☐ Austin |
| 13 | ~~Decide whether the 11 module checks ship~~ | all modules | ☑ **closed** — Austin removed quizzes/flashcards by design (2026-07-29) |
| 14 | Triage planned-but-unbuilt lessons — **count is lower than 23**, several exist under different nav titles | outline vs. course | ☐ needs decision |
| 15 | Confirm templates **01–05**; the **Coverage Audit worksheet** (8.5, 9.7) is referenced with **no Materials location** — unlike 06/07/08 | Honen Materials | ☐ needs Austin |
| 16 | **Fix 10 empty outcomes checklists** | 10 lessons | ✅ **DONE 2026-07-29** — `'"'"'` → `&#39;` in all 10; 0 of 50 malformed |
| 17 | **Fix currency rendering as LaTeX math** — `$…$` pairs typeset as equations | up to 33 lessons | ☐ **ready — highest severity** |
| 26 | **Toolkit PDF footers over-claim app features** — reminders/surfaces the course says don't exist | PDFs 07, 08 | ☐ **needs Austin — PDF edit** |
| 25 | **Worked-example inconsistency:** couple's DTI is $1,850/~12% in 4.1 but $1,600/~10% in 9.3 | Modules 4, 9 | ☐ fold into item 22's arithmetic pass |
| 24 | **Decide 7.4's read text** — it's a shooting script (producer-facing), fine until the video exists, then needs a learner rewrite or a deliberate keep | Module 7 | ☐ needs decision |
| 23 | ~~Fix stale hand-off in 6.4~~ | Module 5 | ✅ **DONE 2026-07-29** — now points at the walkthrough |
| 22 | **🔴 MATH ERROR: the couple's $19,000 is spent twice** across 2.1 and 4.4 | Modules 2 and 3 | ☐ **ready — highest priority** |
| 21 | **Resolve the bucket/wrapper/Legacy terminology tangle** — 4 overlapping naming systems | Modules 3, 4, 5 + app | ☐ **ready** |
| 20 | **Rename all lessons descriptively; one name per lesson (nav = H1)** | all 50 | ☐ **Austin's call — full pass drafted** |
| 19 | ~~State that retirement spending excludes debt payments~~ | 1.4, 7.7 | ✅ **DONE 2026-07-29** — one line each at both entry points |
| 18 | **Rebuild lesson 2.3** around Life Events + funding sources; drop the "don't hold Bitcoin under 7 years" table | Module 2 | ☐ **Austin's call — spec drafted** |

Items 1 and 2 are withdrawn — see the audit-correction note below. Items 3–6 are
independent of the Retirement Income change and safe to do now.
Items 9–10 wait for that push. Item 11 should happen before filming, since
wrong tax numbers are expensive to fix on video.

---

## Headline: the readability problem is not the writing

Measured across all 50 lessons:

| Metric | Value |
| --- | --- |
| Average sentence length | **8.9 words** |
| Sentences over 30 words | 38 in the entire course |
| Longest paragraph | 84 words |

For comparison, general-audience business writing typically runs 15–20 words per
sentence. **The prose is already far simpler than the target.** Shortening
sentences would be optimising something that isn't broken, and would likely make
the voice choppier without helping comprehension.

The comprehension load is coming from two other places: **term density** and
**lesson length**. Both are measurable, and both have specific fixes.

### Term density

Occurrences across the course:

```
trust        82     drawdown   43     cost basis    18
Roth         78     LTV        36     collateral    16
bracket      78     RMD        32     liquidation   15
passphrase   50     waterfall  28     probate       14
                    multisig   25     capital gains  9
                    guardrail  22     power law      6
                    beneficiary 22    Monte Carlo    5
```

Every one of these is a term a smart newcomer does not arrive knowing. The issue
isn't that they appear — it's a financial planning course, they have to — it's
that several carry heavy conceptual weight and are introduced inside lessons
already doing other work.

**Module 8 (Estate & Inheritance) is the density hotspot**: `trust` (82),
`beneficiary` (22), `probate` (14), plus executor and the four legal documents,
all concentrated in one module. It also contains the longest lesson in the course.

### Lesson length

The five longest lessons, by word count:

| Words | Lesson |
| --- | --- |
| **3,172** | Walkthrough: set the backstop + read the estate-tax number in Orange Plan |
| 1,743 | Walkthrough: document your custody map in Orange Plan |
| 1,721 | Walkthrough: build cash flow and reserve in Orange Plan |
| 1,720 | Walkthrough: run the annual review in Orange Plan |
| 1,659 | The executor, the four legal documents, and choosing an estate attorney |

The estate walkthrough is **1.8× the next longest lesson** and roughly 3× the
course median. It is doing at least two jobs (set the backstop; read the
estate-tax number) and the title admits it with a `+`.

---

## Claims: what checks out

I pulled all 318 percentage claims and verified the load-bearing ones. **The
factual accuracy is good** — these are all correct as stated:

| Claim in course | Verified |
| --- | --- |
| "62 Early (~30% less)" | Correct. FRA 67 (born 1960+) → 30% reduction at 62. |
| "70 Max (~24% more)" | Correct. Delayed retirement credits total 24% from 67→70. |
| "67 Full (100% benefit)" | Correct for anyone born 1960 or later. |
| "2018: dropped 84%, from ~$20k to ~$3k" | Correct. |
| "2022: dropped 77%, from $69k to just under $16k" | Correct ($69,000 → $15,476). |
| "an asset that can fall 80%" | Consistent with both cycles above. |

This is worth saying plainly: the numbers in this course are not sloppy. Adding
citations here is about **credibility**, not correction.

## Claims: one that needs fixing

> **"Bitcoin at 40% forever** (its historical rate)."

**The parenthetical is wrong**, and it's the single most attackable line in the
course. Bitcoin's realised historical CAGR is materially *higher* than 40% over
most measurement windows — roughly 70% for the decade to 2023, ~60% blended
across timeframes. So 40% is a defensible *forward assumption*, but it is not
"its historical rate."

The fix is small and makes the course stronger, not weaker:

- Keep 40% as the assumption. Relabel it as what it is — a deliberately
  conservative forward number, **well below** what Bitcoin has actually done.
- That reframing is more persuasive anyway: "we're projecting at little more
  than half the historical rate" is a much better position to defend than a
  claim a critic can falsify in one search.
- The adjacent scenario ("Bitcoin at 20% now, declining as adoption grows") is
  already framed correctly as an assumption. Match that pattern.

**Compliance angle** (per `CLAUDE.md`: educational, not advisory): labelling a
number "its historical rate" edges toward a performance representation. Framing
it as a chosen, conservative assumption is both more accurate and safer.

## Data worth adding

The strongest available data point isn't in the course yet — Bitcoin's
**declining drawdown severity across cycles**:

```
2011:  -93%
2015:  -86%
2018:  -84%
2022:  -77%
```

This directly supports the course's core thesis (Bitcoin drops hard and
recovers, plan for it) while showing maturation over time. It turns
"Bitcoin can fall 80%" from a scary assertion into an evidence-backed trend
with a direction. It belongs in Module 1 (assumptions) or Module 3 (the
stress-test emotion gate).

Two more with solid literature behind them:

- **Guardrails** — ✅ **already satisfied**: lesson 6.4 cites the source
  directly ("These bands come out of Guyton and Klinger's withdrawal research,
  sized for Bitcoin's volatility") and correctly frames the 60/80/95 stops as
  Orange Plan's shipped defaults. Note the course's implementation is
  *confidence-based* (Monte Carlo bands), not withdrawal-rate-based — which
  means the Kitces critique of withdrawal-rate guardrails doesn't apply; the
  course is already on the risk-based side of that argument.
- **"82% doesn't mean 18% chance of going broke"** — this is a genuinely good
  explanation and it matches how the literature describes Monte Carlo output
  (850 of 1,000 paths surviving). It's currently asserted; one line grounding
  it would let it carry more weight.

---

## Simplification: five concrete changes

Ordered by impact per unit of effort.

1. **Split the 3,172-word estate walkthrough into two lessons.** It already
   announces its own seam in the title ("set the backstop **+** read the
   estate-tax number"). Two ~1,600-word lessons match the length of every other
   walkthrough in the course. Lowest-risk, highest-return change here.

2. **Give Module 8 a term primer.** It carries the heaviest jargon load in the
   course (trust/probate/beneficiary/executor) and its teach lesson is the
   longest non-walkthrough. A short "five words before we start" opener would
   let the substantive lessons stop pausing to define things.

3. **Target the confidence-ring lesson specifically.** It has the highest average
   sentence length in the course (11 words) *and* the hardest concept (Monte
   Carlo interpretation). It's the one place where the writing and the concept
   difficulty peak together — the strongest candidate for a worked example or a
   visual.

4. **Just-in-time definitions for the top ~10 terms, not a glossary.** A glossary
   is a page nobody visits. First use of `LTV`, `RMD`, `cost basis`, `waterfall`,
   `drawdown` should carry its definition inline. This matches the existing
   progressive-disclosure principle in `CLAUDE.md`.

5. **Leave the sentence-level prose alone.** At 8.9 words/sentence the voice is
   already doing its job, and it's a real asset — the opening ("I had the asset
   figured out. What I didn't have was a plan.") is the kind of line that makes
   people keep reading. Don't sand that off in the name of simplification.

---

## Filming: what's teleprompter-ready and what isn't

Measured with production mode separated out:

| | Lessons | Words | Avg prose share |
| --- | --- | --- | --- |
| **TEACH** (talking head / teleprompter) | 39 | 32,316 | **56%** |
| **DEMO** (walkthroughs, screen recording) | 11 | 20,922 | 49% |

Two things fall out of this.

**1. The sentence length is an asset, not a problem.** 8.9 words/sentence is close
to ideal for teleprompter — short sentences are what let you read naturally
without losing your place or running out of breath. Recommendation #5 above
("leave the prose alone") gets stronger, not weaker, once filming is the goal.
At ~140 wpm the 39 teach lessons are roughly **3.8 hours of finished video**,
averaging ~6 minutes each. That's a sane per-lesson runtime.

**2. But only ~56% of a teach lesson is speakable as written.** The other 44% is
tables, bullet lists, and headings — content that carries meaning *visually* and
turns to mush when read aloud. "Investable only: $175k ÷ $295k = about 60%" is
fine on a page and unspeakable on camera.

The lessons furthest from film-ready:

| Prose | Tables | Bullets | Lesson |
| --- | --- | --- | --- |
| 33% | 11 | 10 | Give every future cost a lane |
| 39% | 27 | 14 | Harvesting losses and gains |
| 40% | 13 | 5 | Give every dollar a job: Reserve / Bridge / Forever |
| 40% | 10 | 14 | Every debt gets a job |
| 40% | 14 | 9 | Asset location: the right account for each holding |
| 43% | 0 | 20 | The four Bitcoin allocation tiers |

These aren't badly written — they're *reference material*, which is the right
format for a written lesson and the wrong one for a script.

### The approach that changes least

Don't rewrite the tables into prose. **Promote them to on-screen graphics and
write narration over them.** For each structured block:

- The table/list becomes a lower-third or full-screen card — it's already
  designed as a visual, so this is mostly a design pass, not a writing pass.
- The script gains 2–3 spoken lines pointing at it ("Three tiers here. Most
  people land in the middle one, and here's how you tell.")
- The existing prose stays **verbatim**. That's the majority of the lesson and
  it's already in your voice.

This keeps the "without changing much" constraint intact: the prose is untouched,
the tables move from page to screen, and the only new writing is the connective
narration. It also plays to the strength of the material — the tables are genuinely
good, and they'll land harder as graphics than as read-aloud lists.

### Production note on the walkthroughs

The 11 walkthroughs (20,922 words) are a different mode entirely — screen
recording with voiceover, not teleprompter. They shouldn't be scripted the same
way, and the 3,172-word estate walkthrough flagged above is worth splitting
*before* filming rather than after, since it's ~25 minutes of screen capture in
one take.

### On the transcripts — yes, send them

Concretely useful. What I'd pull from them:

- **Sentence rhythm** — your natural spoken length vs. the course's 8.9 written
  words, so scripts land where you actually talk.
- **Openers and closers** — how you start and end a video, which is the most
  formulaic and most voice-specific part of a script.
- **Transitions and connective tissue** — the phrases you use to move between
  ideas. This is exactly what the 44% table-to-narration conversion needs, and
  it's the part most likely to sound like a robot if I invent it.
- **Contraction and filler patterns** — written prose over-uses "do not" where
  you'd say "don't."

3–5 transcripts of videos you feel sound most like you is plenty. More helps
marginally; the wrong ones (heavily edited, or a format you don't want to copy)
hurt. Drop them anywhere in the repo and I'll work from them.

## Walkthrough audit: course vs. actual app

Extracted every bold UI label from the 11 walkthrough lessons (~280 distinct
strings), then checked each against `src/`.

**Result: 97 of 107 testable labels match the code exactly.** The walkthroughs
are in good shape. The failures are worth fixing individually, not systemically.

### Real mismatches — course says X, app says Y

| Course says | App actually says | Where |
| --- | --- | --- |
| **Save as PDF** | **Download PDF** | `src/pages/Report.jsx:593`, `src/pages/EstateSecurity.jsx:1873` |
| **Spending & Reserve** | **Cash Flow & Reserve** | 4 occurrences in `src/` |
| **BTC-loan safety check** | **Safety check** | course over-specifies the label |

The first two are the ones that will actually strand a user mid-walkthrough,
and both have the same underlying cause: **the course uses both forms
inconsistently.** It already says "Download PDF" and "Review Cash Flow &
Reserve" elsewhere — those matched exactly. So this is drift within the course,
not the app renaming things. Pick the app's wording and normalise.

### Needs a human check

**"Tax funding" picker.** The walkthrough tells users to set a **Tax funding**
option ("Plan cash flow" vs. "Withheld from each conversion"). Searching the
code, `tax funding` appears **only in comments and a test note** —
`runProjection.jsx:8589`, `:15369`, `:17767` — never as user-visible text. The
*behaviour* clearly exists; what I can't confirm from grep alone is what the
control is actually labelled on screen. Worth eyeballing the Roth conversion UI
before filming that walkthrough.

### Not bugs — correctly absent from the app

`Heir Letter`, `Family Custody Map`, `Executor Packet` are **course toolkit
documents** (numbered 06/07/08), not app features. They flagged as "missing from
code" and should not be chased. Minor cosmetic drift: `Before / After` (rendered
as two labels), `Insurance gaps` (singular in code), `Annual custody review`
(exists as `custodyReview` / `reviewCadence`).

### The bigger gap: the course teaches the concept but never names the page

Reverse audit — how often the course mentions each app page by name:

| App page | Mentions in course | Module that teaches the concept |
| --- | --- | --- |
| **Tax Center** | **0** | Module 5 — Tax Strategy (entire module) |
| **Withdrawal Strategy** | **0** | Module 6 — sell/borrow/hold, income waterfall |
| **Liabilities** | **0** | Module 4 — Debt Strategy (entire module) |
| **Estate Security** | **0** | Module 8 — Estate & Inheritance (entire module) |
| **Freedom Number** | **0** | Module 1 — the confidence number |
| Coach | 1 | — |
| Methodology | 1 | — |
| Investing | 1 | — |
| *(well covered)* | | |
| Allocation | 54 | Module 3 |
| Report | 51 | Module 10 |
| Cash Flow | 46 | Module 2 |
| Life Events | 15 | Module 9 |
| AI Review | 14 | — |

**Four modules teach a subject thoroughly and never tell the user which page it
lives on.** Someone finishes Module 4 understanding debt tolerance and the two
ratios, then opens the app and has to guess that it's under "Liabilities."

This is the same failure as the tooltip gap: the course teaches *concepts*
excellently and *navigation* barely. Both are cheap to fix — a "where this
lives" line at the top of each module's walkthrough, plus the "How to read the
app" lesson proposed above.

Worth noting **Methodology** (1 mention) is where the app documents its own
math. For a course whose strongest lesson is "How to read a financial plan,"
that page is a natural reference and is currently invisible.

### Pending: Retirement Income page change (Austin, 2026-07-29)

A change to the Retirement Income page is in flight and not yet pushed.
**Everything below is provisional until it lands** — do not act on these
without re-running the audit first:

- Labels in the fixture that touch this area: `Income Floor`, `Income sources`,
  `Retirement income`, `Retire at age`, `Earliest Retirement Age`,
  `Expected Social Security`, `Tax-free income`, `Plan cash flow`,
  `Compare withdrawal approaches`, `Compare strategies`, `Selected strategy`,
  `Run Monte Carlo`.
- The **Tax funding** open question above sits in this territory (Roth
  conversion funding) and may be resolved or changed by the same work.
- The reverse-audit finding that **Withdrawal Strategy** is never named in the
  course may or may not still apply depending on how the page is restructured.
- **One existing course note is at risk of going stale**, and it's the most
  fragile line in the course:

  > ⚠ There's no "income floor" panel on the Income page. The floor renders as
  > **Income Floor** in the projection-chart hover tooltip and as the stacked
  > bands in the income-sources chart. Look on the chart, not for a numeric panel.

  That is a workaround for a specific UI shape. If the Retirement Income change
  adds a panel — or moves the floor — this note becomes actively wrong and will
  send users looking in the wrong place. Re-check it first.

**To re-run after the push:** `./course-export/audit-ui-labels.sh` from the repo
root. It reproduces this audit against current `src/` and exits non-zero on any
missing label. Not wired into CI — that's a cost decision, and per `CLAUDE.md`
new always-on triggers get proposed, not added.

### Suggested fix order

1. Normalise **Save as PDF → Download PDF** and **Spending & Reserve → Cash Flow
   & Reserve** across the walkthroughs (course-side drift, pure find/replace).
2. Eyeball the **Tax funding** control and correct the label if needed.
3. Add a "where this lives in the app" line to the Module 4, 5, 6, and 8
   walkthroughs.
4. Then film — these are all cheaper to fix in text than to re-shoot.

## Completeness: what the course actually contains

Verified against the course revision, not assumed:

```
50 topic dirs  =  50 read.md  =  50 nav rows      1:1, nothing missing
50 learning-goals.json  (756 goals total)
11 unit.json
 0 activity files of any other type
```

**All 50 lessons and all lesson text are captured.** Every topic is a single
`read.md`. The master file now also carries the 756 learning goals, which the
original export dropped.

### The course is lessons-only, by design

`bootstrap-outline.json` still specifies a check for every module — "Module 0
check" through "Module 10 check" — and none exist in the built course.

**This is intentional. Austin removed the quizzes and flashcards (2026-07-29).**
The outline is the stale artifact here, not the course. Do not re-raise this as
a coverage gap, and do not "restore" the checks when reconciling the outline
against the built course.

Practical consequence for the master file and for filming: there is exactly one
content type to script, and no interstitial assessment to design around. The
`[TEACH]` / `[DEMO]` split is the only production distinction that matters.

### 23 planned lessons have no built counterpart

The outline lists 66 lesson titles; 50 were built. Some of the 23 are clearly
renames or merges — "Choose your custody level" reads as folded into "Custody:
the five questions and choosing your level", and "Choosing your estate attorney:
the Bitcoin questions" into "The executor, the four legal documents, and
choosing an estate attorney".

But several have no obvious home in the built course, and two stand out:

- **"Choosing your Bitcoin growth assumption"** — this is the exact subject of
  the one factual error found above (the "40% forever (its historical rate)"
  line). There may once have been a dedicated lesson that would have handled it
  properly.
- **"Sequence-of-returns risk"** — a concept the course leans on (it's why the
  guardrails exist and why the reserve is sized the way it is) but never teaches
  in its own lesson.

Others without a clear counterpart: "Cash flow is the engine", "The surplus
flywheel", "Find your Bitcoin path", "State taxes and relocation: a big lever",
"Capstone: you have a plan", "The yearly re-read: your before-and-after",
"Walkthrough: will your estate ever owe tax?".

This is a triage job, not a bug list — most may be deliberate. But it should be
a decision rather than an accident, especially the two called out above.

## What I did not check

- The remaining ~300 percentage claims are mostly worked-example arithmetic
  (the $175k/$745k allocation math, the debt-ratio scenarios). I spot-checked
  the framework claims, not every computed figure in every example.
- Tax specifics (bracket thresholds, RMD ages, estate exemption amounts) are
  time-sensitive and should be re-verified against the current tax year before
  each course refresh. I did not audit those against 2026 tables.

## Sources

- [SSA — Retirement Age and Benefit Reduction](https://www.ssa.gov/benefits/retirement/planner/agereduction.html)
- [SSA — Delayed Retirement Credits](https://www.ssa.gov/benefits/retirement/planner/delayret.html)
- [SSA — Early or Late Retirement](https://www.ssa.gov/oact/quickcalc/early_late.html)
- [Bitcoin drawdown history (TradingView / Glassnode BTC_ATHDRAWDOWN)](https://www.tradingview.com/chart/BTC_ATHDRAWDOWN/9AUq2iAG-Bitcoin-What-Historical-Drawdown-in-a-Bear-Market/)
- [NYDIG — Charting Drawdowns During Up Cycles](https://www.nydig.com/research/charting-drawdowns-during-up-cycles)
- [Bitcoin price history and CAGR](https://www.bestbrokers.com/bitcoin-trading/bitcoin-price-history/)
- [Glassnode — BTC 4yr CAGR](https://studio.glassnode.com/charts/4yr-cagr?a=BTC)
- [Kitces — Why Guyton-Klinger Guardrails Are Too Risky For Retirees](https://www.kitces.com/blog/guyton-klinger-guardrails-retirement-income-rules-risk-based/)
- [White Coat Investor — Guyton-Klinger Guardrails Approach](https://www.whitecoatinvestor.com/guyton-klinger-guardrails-approach-for-retirement/)

---

## 🐞 Live bug: 10 outcomes checklists render empty

Found 2026-07-29 from a screenshot of lesson 1.3, which shows **0 / 0** items
where four should be listed.

**Cause.** The outcomes component takes its items from a single-quoted HTML
attribute:

```
data-params='{"items":["...","..."]}'
```

In ten lessons an apostrophe inside an item was escaped **shell-style** rather
than HTML-style — the literal sequence `'"'"'` appears in the file:

```
"Understand what your earliest retirement date is and how it'"'"'s calculated"
```

The first `'` closes the attribute. Everything after it is discarded, the JSON
never parses, and the checklist renders with zero items. It fails silently —
the card still draws, so it looks intentional rather than broken.

**Affected lessons (10 of 50):**

1. The confidence ring: your plan's stress test
2. Find your surplus
3. Give every future cost a lane
4. Size the reserve to your life
5. Give every dollar a job: Reserve, Bridge, Forever
6. Every debt gets a job
7. The three buckets, your bracket roadmap, and the state lever
8. Walkthrough: document your custody map in Orange Plan
9. The executor, the four legal documents, and choosing an estate attorney
10. The 90-day dead man's switch

**Fix.** Replace `'"'"'` with `&#39;` in those ten `data-params` attributes, or
switch the attribute to double quotes and escape the inner JSON quotes. The
item text itself is intact in every case — only the escaping is wrong, so
nothing has to be rewritten.

**Detection.** `grep -rl "'\"'\"'" /course/units/*/topics/*/activities/read.md`
in the Honen sandbox returns exactly the affected files. Worth re-running after
any bulk content edit, since this is the kind of thing that gets reintroduced by
a generation script.

Two lessons here beyond the fix: an apostrophe in a learning goal is enough to
silently delete the whole checklist, and the failure is invisible from the
authoring side — you only see it by looking at the rendered lesson. Whatever
generated these should be escaping for HTML, not for a shell.


---

## ⚠ Audit correction: items 1 and 2 were false positives

Withdrawn 2026-07-29 after reading the lessons in full. **Do not make these
edits** — both would have introduced errors into correct text.

**"Save as PDF".** The audit flagged this because the app button says
"Download PDF". Read in context, the walkthrough is correct:

> Open the **Account menu** in the top right, then click **Report**, then
> **Download PDF**.
>
> The button triggers your browser's print dialog. Choose **Save as PDF** and
> put the year in the filename.

Two different things — the app button *is* "Download PDF", and "Save as PDF" is
the option in the **browser's** print dialog. Renaming it would have made the
instruction wrong.

**"Spending & Reserve".** Not a claimed app label. It is one of the course's own
section headings, and it already names the real location beside it:

> `### Spending & Reserve · Plan → Income`

**The method flaw.** `audit-ui-labels.sh` extracts every **bold** string from
the walkthroughs and greps `src/` for it. But bold is used for three different
things — UI labels, emphasis, and section names — and only the first should be
checked against code. Roughly 2 of 3 flagged "mismatches" turned out to be the
other two kinds.

The 97/107 match rate still holds and is still useful as a regression signal.
But **a flagged label is a question, not a defect.** Read the surrounding
sentence before changing anything. The script cannot tell "the app calls this X"
from "here is a heading that happens to be bold".

This does not affect the remaining audit finding (**BTC-loan safety check** vs
**Safety check**) or the open **Tax funding** question, both of which are
genuine label references.


---

## 🐞 Live bug: dollar amounts rendering as LaTeX math

Found 2026-07-29 by comparing a pasted lesson against its source. **Higher
severity than the checklist bug** — this one corrupts the numbers themselves,
in a course whose entire subject is numbers.

**Source** (lesson 2.1, Find your surplus):

```
| **Surplus** | **$29,000 / year (~$2,400/mo)** |
```

**What the reader shows:** the text between the two `$` signs is typeset as an
equation, rendering vertically, character by character —

```
29
,
000
/
y
e
a
r
```

Same failure in the body text: `Enter your paycheck ($190,000) instead of your
actual spending ($80,000)` renders as `190 , 000 ) i n s t e a d o f ...`

**Cause.** The renderer is treating `$…$` as inline math delimiters (KaTeX /
MathJax convention). Any line with two or more unescaped dollar signs is a
candidate. A financial course is close to the worst possible content for that
default.

**Exposure: 33 of 50 lessons** have at least one line with paired `$`. Worst
offenders:

```
22  Harvesting losses and gains
 9  Find your surplus
 8  The RMD risk and Roth conversions
 7  Spending, floor, and the gap
 7  Drift and the LTV cushion
 6  The income waterfall, draw, and refill
 6  Cost basis: the unlock for everything else
```

**Not every candidate breaks.** `($150k, $100k, etc.)` in the baseline
walkthrough renders fine, because most math parsers reject a span that ends in
whitespace. The trigger is roughly: two `$` on a line with the closing one
tight against a non-space character. So treat 33 as the exposure ceiling, not a
confirmed count.

**Fix options**, cheapest first:

1. **Disable math rendering** for lesson content, if the platform allows it.
   One switch, fixes all 33, nothing to re-edit. Almost certainly right — a
   financial planning course has no use for LaTeX.
2. Escape as `\$` in the source.
3. Use `&#36;` in the affected lines.

**Detection:** `grep -c '\$[^$]*\$' <lesson>` lists candidates per file.

**Verify visually before mass-editing.** The evidence here is a paste plus the
source; option 1 would make the escaping question moot, so confirm on screen
which lines actually break before rewriting anything. If the platform can turn
math off, nothing needs escaping at all.

---

## 🔴 Lesson 2.3 redesign: "Give every future cost a lane"

**Austin's call, 2026-07-29.** The current lesson is off-message and should be
rebuilt around future cash-flow planning via Life Events. Recorded here as a
spec; Austin owns the final shape.

### What's wrong

The lesson's core table applies a conventional time-horizon-to-allocation
framework to Bitcoin:

| Timeframe | What NOT to hold *(current text)* |
|---|---|
| 1 to 3 years | Stocks, **Bitcoin** |
| 3 to 7 years | **Bitcoin** |
| 7+ years | Cash |

Three independent problems, beyond it not being Austin's view:

1. **Contradicts the product's stated default.** `CLAUDE.md`: "Bitcoin
   maximalist perspective… The default is 'never sell.'" Telling a holder not to
   hold Bitcoin against a six-year cost is the opposite.
2. **Contradicts lesson 2.2.** The reserve is sized precisely so a bad market
   never forces a Bitcoin sale. This lesson then moves Bitcoin out pre-emptively
   — doing voluntarily what the reserve exists to prevent.
3. **Omits borrowing.** The app treats BTC-backed loans as a first-class debt
   type with collateral tracking and live LTV, and Module 6 is "Sell, borrow, or
   hold." Here the options are sell-or-don't-own. The Bitcoin-native answer to a
   dated cost is missing.

There's also a compliance edge: a column headed **"What NOT to hold"** is
prescriptive allocation advice, against the "educational, not advisory" rule.

### What to keep

**Timeframe is still the right axis** — Austin's note: *"how to plan based on
timeframes is good, but not correct."* Also worth keeping:

- Known costs are not emergencies; the reserve is not their funding source.
- Pre-fund anything that would break monthly surplus in one hit.
- Small dated costs come from flow; big ones need a plan.
- The freedom date should reflect known costs honestly.

### What to change

Change the question the timeframe answers. Currently it's *"what asset should
this money sit in"* (allocation advice). It should be *"where does this money
come from, and how do you fund it without being forced to sell at the wrong
time"* (cash-flow planning).

Reframe the funding sources as a menu, not a prohibition:

| Source | When it fits |
|---|---|
| Monthly surplus routed ahead of the date | Anything you can accumulate before it lands |
| Pre-funded cash lane | Near-dated, where certainty beats growth |
| **Borrow against Bitcoin** | You want the cost covered without selling; LTV and liquidation covered in Module 4 |
| **Planned sale in a low-bracket year** | The sale is intentional and tax-placed (Module 5), not forced |
| Reduce, delay, or drop the cost | Always on the table, and usually cheapest |

Timeframe then determines *how much runway you have to choose*, rather than what
you're forbidden to own. A cost eight years out has room for all five options; a
cost eight months out has fewer. That's the honest version of the same insight,
and it keeps the never-sell default intact.

### What the lesson is actually for

**Austin, 2026-07-29:** *"This is what the lesson should actually help with.
Cash flow planning. Things people may not be thinking about."*

That reframes the job entirely. The current lesson assumes you already know your
future costs and only need somewhere to park the money. The valuable version
**surfaces the costs you haven't thought of** — that's the part a Bitcoiner
can't get from a generic planning article, and it's the part the app's Life
Events feature exists to hold.

Blind spots to cover explicitly:

- **Weddings.** Yours or a child's. Large, dated, and routinely unplanned for.
- **Helping kids.** Beyond tuition — a down payment, a car, a business, ongoing
  support. Often the largest unmodelled transfer in a plan.
- **Long-term care.** The one most people skip entirely, and the most expensive.
- **The retirement spending smile.** Retirement spending is not a flat line, and
  modelling it as one is wrong in both directions.

### The retirement spending smile — with the nuance intact

Worth teaching properly, because the popular version is oversimplified.

- **The smile.** Average real spending is U-shaped: higher early (travel, the
  "go-go" years), falling through mid-retirement, rising late as healthcare
  climbs.
- **The decline is large.** Blanchett's 2014 work puts the real drop at roughly
  **26% between ages 65 and 84**.
- **But the median retiree "smirks," not smiles.** Blanchett's newer work finds
  the median pattern is a steady decline that flattens — *without* the late-life
  upturn. The smile is the average; the tail is driven by the minority with
  serious care costs.

The planning consequence is the honest version: **most people's spending falls,
but the ones whose spending rises late rise a lot.** That's a risk-shaped
problem, not a straight-line assumption — which is exactly what this course's
confidence ring is built to model.

Long-term care sizing, for the same reason:

- **57%** of Americans who turned 65 in 2022 will develop a disability serious
  enough to require long-term care.
- **22%** will need it for more than five years.

A coin flip on needing it at all, and a one-in-five chance of a multi-year bill.
That belongs in a plan as an event, not a footnote.

### Structure to build

1. **Which life events actually move cash flow.** The app's five types — Job or
   income change, Windfall or inheritance, Large purchase, College expense,
   Expense change — sorted by whether they move the plan.
2. **The blind spots.** Weddings, helping kids, long-term care, the spending
   smile. This is the section that earns the lesson.
3. **Getting them into the app.** Life Events is the feature; the current lesson
   never names it.
4. **Where the money comes from.** The five-source menu above — including
   borrowing and planned low-bracket sales.
5. **How timeframe changes your options.** Runway to choose, not prohibition on
   holding.
6. **Reading the effect.** The event lands in the projection and moves the
   freedom date.

### Draft section breakdown — a checklist to think through

**Austin, 2026-07-29:** *"Break it down by sections so it feels like a checklist
or step by step through potential things to think about, with maybe a note about
how to think about them."*

Each section is one prompt plus the lens. The lens asks a question rather than
issuing a rule, which keeps it educational and avoids the "what NOT to hold"
problem that sank the original.

---

#### 1. Family milestones

**Think about:** A wedding — yours or a child's. Helping with a down payment. A
child's car, first business, or a stretch of ongoing support.

**How to think about it:** These are the costs people feel awkward putting a
number on, so they don't, and the plan quietly assumes they're zero. Put in a
rough number and a rough year. A wrong number in the plan beats a real cost
outside it.

#### 2. Aging parents

**Think about:** Support you may provide, travel to care for them, or a cost
that lands with no notice.

**How to think about it:** Usually undated and often uncomfortable, which is why
it gets skipped. It doesn't need a date to be modelled — a range and a
likelihood is enough to see whether it would bend the plan.

#### 3. Home and property

**Think about:** Roof, HVAC, renovation, a move, a second property.

**How to think about it:** The dated ones are easy. The honest question is
whether you're carrying a house whose maintenance you haven't priced. Ballpark
year is fine.

#### 4. Education

**Think about:** Kids' tuition, private school, your own retraining.

**How to think about it:** The one cost most people do model — and usually the
one they model too precisely while missing everything else on this list.

#### 5. The healthcare bridge

**Think about:** If you stop working before 65, you're buying your own coverage
until Medicare.

**How to think about it:** This is a known, dated, multi-year cost, and it's the
one that most often moves a freedom date. Module 6 covers it in depth; here it's
just about getting it into the plan as an event. *(Cross-reference, don't
duplicate.)*

#### 6. Long-term care

**Think about:** **57%** of Americans who turned 65 in 2022 will need care
serious enough to qualify as long-term care. **22%** will need it more than five
years.

**How to think about it:** A coin flip on needing it, one in five on a
multi-year bill. Too likely to leave out, too variable to model as a single
number. The useful question isn't "what will it cost" but "would my plan survive
the five-year version." *(Module 8 owns the insurance answer.)*

#### 7. Income changes you can see coming

**Think about:** A sabbatical, a partner stopping work, a planned business sale,
a step down before full retirement.

**How to think about it:** People model costs and forget income has events too.
A year at half income is a cash-flow event exactly like a large purchase.

#### 8. Windfalls

**Think about:** Inheritance, an equity event, a large bonus.

**How to think about it:** Left out because they feel like counting chickens.
But a windfall with no plan becomes lifestyle, and a windfall with a plan is a
funding source for everything above it on this list.

#### 9. Tax events you create

**Think about:** The tax bill on a planned Roth conversion. Estimated taxes on a
Bitcoin sale.

**How to think about it:** Self-inflicted and fully predictable, which makes
them the easiest to place — and the most annoying to be surprised by. Module 5
sets the timing.

#### 10. The shape of retirement spending

**Think about:** Retirement spending is not a flat line. Average real spending
falls roughly **26% between 65 and 84**, and healthcare climbs late.

**How to think about it:** The average is a "smile." The *median* retiree is a
"smirk" — a steady decline with no late upturn. Most people's spending falls;
the ones whose spending rises late rise a lot. Plan the flat line and you're
wrong in both directions: too conservative early, too optimistic about the tail.
The confidence ring is the tool for a risk-shaped cost like this.

---

**Closing move.** Everything above becomes a Life Event in the app, then the
freedom date is re-read. The point of the lesson lands there: the date only
means something if the plan knows what's coming.

### Open questions for Austin

- Does the "lane" metaphor survive, or does it go with the allocation framing?
- How hard should borrowing be pushed here vs. deferred to Module 4?
- Does the college example stay? It's concrete and good, but its three options
  currently omit borrowing — adding a fourth row may be the whole fix.
- **Does this become more than one lesson?** The blind-spot material plus the
  spending smile plus funding sources is more than 625 words of content. The
  spending smile in particular may belong in Module 6 (Retirement Income), where
  the bridge years and guardrails already live.
- **Long-term care overlaps Module 8** ("Insurance: the risks you can't
  self-insure yet"). Decide whether it's introduced here as a cash-flow event
  and paid off there, or owned entirely by Module 8.

### Sources

- [Blanchett — How Spending Evolves in Retirement: A Smile, a Smirk, or Something Else? (Financial Planning Review)](https://onlinelibrary.wiley.com/doi/10.1002/cfp2.70032)
- [Retirement "smirk" spending pattern](https://moneywise.com/managing-money/retirement-planning/retirement-smirk-spending-theory-blanchett-prudential)
- [Retirees of all income levels reduce spending over time (PLANADVISER)](https://www.planadviser.com/retirees-of-all-income-levels-reduce-spending-over-time-per-study/)
- [Morningstar — How likely are you to have an extended long-term-care need?](https://www.morningstar.com/retirement/how-likely-are-you-have-an-extended-long-term-care-need)


---

## Gap: "retirement spending excludes debt payments" is never stated

**Austin, 2026-07-29.** The app keeps retirement spending and debt payments in
separate fields, same as it does for current spending. **No lesson says so.**

Searched every lesson: the only place the two appear together is the onboarding
Review screen, which lists "Retirement spending target" and "Monthly debt
payments" as adjacent rows. That implies the separation without ever stating it.

Why this is worse than a plain omission: the baseline walkthrough carries a
strong, explicit warning for the *current* Living row —

> ⚠ Your spending number goes in the **Living** row. Not your paycheck. Not your
> debt payments. This is where the biggest data-entry mistake dies.

Being emphatic about one field and silent about the neighbouring one invites the
reader to assume the rule doesn't apply there. A user who dutifully excluded
debt from Living may well add it back into retirement spending, which
double-counts debt service and pushes the freedom date out.

**Where to state it:**

1. **Lesson 1.4**, onboarding Step 3, on the Retirement spending sub-slide —
   the field where the number is actually entered. Highest value.
2. **Lesson 2.4**, Step 3 — extend the existing warning to name both fields.
3. **Module 6**, "Spending, floor, and the gap" — the retirement-spending
   lesson proper.

Cheap to fix, and it protects the single most consequential input in the plan.


---

## Gap: nav titles and page titles disagree in 10 lessons

Found 2026-07-29 while slotting lesson 3.1.

**Two are substantive** — a learner clicks one title and lands on a page headed
something else:

| Nav title | Page H1 |
|---|---|
| The four Bitcoin allocation tiers | **Find your Bitcoin path: the four allocation tiers** |
| The two emotion gates: stress-test + price context | **Two checks that keep your allocation honest** |

**Eight are cosmetic** — punctuation or connector drift:

| Nav title | Page H1 |
|---|---|
| Start here: what this course is and how to use it | Start here |
| Find your surplus: Keep, Cut, Reduce | Find your surplus |
| Give every dollar a job: Reserve **/** Bridge **/** Forever | Reserve**,** Bridge**,** Forever |
| The RMD risk **+** Roth conversions | The RMD risk **and** Roth conversions |
| Offense: the four plays | Offense: the four **debt** plays |
| Walkthrough: model **it** in Orange Plan | Walkthrough: model **tax strategy** in Orange Plan |
| The income waterfall **+** draw and refill | The income waterfall**,** draw**,** and refill |
| External demo: hardware wallet setup **+** exchange hardening | …setup **and** exchange hardening |

### This partially resolves action item 14

Several titles I listed as "planned but never built" are built — under a
different nav name. **"Find your Bitcoin path"** is the H1 of lesson 3.1. So
the 23-lesson gap is overstated; some fraction is renames, not drops. Item 14
should be re-triaged against H1s as well as nav titles before anyone concludes
content is missing.

### Cross-references follow the H1, not the nav

Lesson 3.1 closes with *"The next lesson covers the two checks that keep your
allocation honest"* — which is the **H1** of 3.2, not its nav title ("The two
emotion gates"). So the in-lesson prose and the navigation are already using two
different naming systems. Whichever wins, they should match, or the hand-off
sentences will keep pointing at titles the learner can't find in the sidebar.

**For filming:** pick one name per lesson before recording. Saying a title on
camera that doesn't match the sidebar is a re-shoot.


---

## Lesson renaming pass (Austin, 2026-07-29)

*"I want the naming to be more descriptive of what the lesson is, and redo them."*

### The convention

1. **One name per lesson.** Nav title and page H1 identical. This alone fixes
   the 10 mismatches and the hand-off sentences that currently point at titles
   the learner can't find in the sidebar.
2. **No pronouns.** "Walkthrough: model **it**" and "route **it**" tell the
   reader nothing in a sidebar, in search, or in a video title.
3. **Name the payoff, not just the metaphor.** Metaphors are good and stay —
   but pair them with the concrete thing. "The bridge years" → "The bridge
   years: retiring before Social Security."
4. **Front-load the searchable noun.** People scan the left edge.
5. **Keep the voice.** Punchy is fine. Vague is not. Where a current title is
   already both concrete and short, it stays — about a third of them do.

### Proposed names — v2

**v1 was rejected as still too abstract.** It kept the framework name and bolted
a subtitle on ("The contribution waterfall: where your next dollar goes"). The
metaphor was still leading.

**v2 rule: the title is the question the lesson answers, in the learner's
words.** If someone couldn't explain the title before taking the lesson, it's
too abstract. Metaphors stay *inside* the lesson, where they're taught — they
just stop being the label.

| # | Current | Proposed |
|---|---|---|
| 0.1 | Start here: what this course is and how to use it | What this course builds, and what to have ready |
| 1.1 | Gather your numbers | The documents and numbers to collect first |
| 1.2 | What your plan rests on: assumptions | Picking your Bitcoin growth rate and inflation |
| 1.3 | The confidence ring: your plan's stress test | Your earliest retirement date, and how likely it is to hold |
| 1.4 | Walkthrough: set up your plan and build your baseline… | Walkthrough: set up Orange Plan and get your first retirement date |
| 2.1 | Find your surplus: Keep, Cut, Reduce | Working out what you have left over each month |
| 2.2 | Size the reserve to your life | How much cash to hold so you never have to sell Bitcoin |
| 2.3 | Give every future cost a lane | Future costs people forget to plan for |
| 2.4 | Walkthrough: build cash flow and reserve… | Walkthrough: enter your income, spending, and cash reserve |
| 3.1 | The four Bitcoin allocation tiers | How much of your money belongs in Bitcoin |
| 3.2 | The two emotion gates: stress-test + price context | What you'd actually do if Bitcoin dropped 70% |
| 4.3 | Give every dollar a job: Reserve / Bridge / Forever | Splitting your money by when you'll need it |
| 4.4 | The contribution waterfall | Which account to put your next dollar in |
| 4.5 | Asset location: the right account for each holding | Which account to hold each investment in |
| 4.6 | Walkthrough: route it in Orange Plan | Walkthrough: set your target mix and where new money goes |
| 4.1 | Defense: tolerance first, then the two ratios | How much debt is too much |
| 4.2 | Drift and the LTV cushion | Keeping a Bitcoin-backed loan from being liquidated |
| 4.3 | Offense: the four plays | Four ways to use debt instead of selling Bitcoin |
| 4.4 | Every debt gets a job | Deciding what to do with each debt you have |
| 4.5 | Walkthrough: give every debt a job… | Walkthrough: enter your debts and set a payoff plan |
| 5.1 | Cost basis: the unlock for everything else | Finding what you paid for your Bitcoin |
| 5.2 | The three buckets, your bracket roadmap, and the state lever | Taxable, tax-deferred, and Roth: what goes where |
| 6.3 | The RMD risk + Roth conversions | Roth conversions and avoiding a forced-withdrawal tax bill |
| 6.4 | Harvesting losses and gains | Using losses and gains to lower your tax bill |
| 5.3 | Walkthrough: model it in Orange Plan | Walkthrough: plan your Roth conversions and sales |
| 6.1 | Spending, floor, and the gap | How much you'll spend in retirement, and what's missing |
| 7.2 | The bridge years | Funding the years between retiring and Social Security |
| 6.2 | The healthcare bridge | Paying for health insurance before Medicare |
| 7.4 | The income waterfall + draw and refill | Which account to withdraw from first in retirement |
| 6.3 | Sell, borrow, or hold | Selling, borrowing, or holding to cover retirement spending |
| 6.4 | The guardrails: turning the confidence number into a paycheck | How much you can safely spend each year |
| 7.7 | Walkthrough: build the paycheck… | Walkthrough: turn your plan into a monthly paycheck |
| 7.1 | Custody: the five questions and choosing your level | Choosing how to store your Bitcoin |
| 7.2 | The hardware wallet and the recovery test | Setting up a hardware wallet and testing recovery |
| 7.3 | Close the doors: single points of failure, hardening, and scams | Closing the gaps that get people's Bitcoin stolen |
| 7.4 | External demo: hardware wallet setup + exchange hardening | Demo: hardware wallet setup and locking down your exchange |
| 7.5 | Walkthrough: document your custody map… | Walkthrough: write down where your Bitcoin is held |
| 8.1 | The executor, the four legal documents, and choosing an estate attorney | The four legal documents, and who carries them out |
| 8.2 | The access split | Who can reach your Bitcoin, and when |
| 8.3 | The heir letter | Writing instructions your family can actually follow |
| 8.4 | The 90-day dead man's switch | Setting up a check-in that releases access if you die |
| 8.5 | Insurance: the risks you can't self-insure yet | The risks you can't cover yourself yet |
| 9.6 | Advanced: do you need a trust, and which one? | Whether you need a trust, and which kind |
| 9.7 | Walkthrough: set the backstop + read the estate-tax number… | *splitting — see item 5* |
| 9.1 | A review is not a rebuild: the two rhythms | Checking your plan without rebuilding it |
| 9.2 | The monthly pass | Your five-minute monthly check |
| 9.3 | The annual review: all six areas | Your once-a-year review, all six areas |
| 10.4 | Walkthrough: run the annual review… | Walkthrough: run your annual review |
| 11.1 | How to read a financial plan | How to read your financial plan |
| 11.2 | Walkthrough: walk your report in Orange Plan | Walkthrough: read your plan report |

**All 50 changed.** Every framework name moved out of the title: waterfall,
tiers, gates, lanes, guardrails, bridge, access split, dead man's switch. They
are all still taught — the lesson teaches the term, the title just stops
assuming it.

**Approved in principle, 2026-07-29.** Austin: *"It should tell them what it's
about, what the objective is at a glance without having to guess."*

That closes the one open question. I'd floated keeping **guardrails** and **the
confidence ring** as branded titles since they're Orange Plan's own language —
but both fail the test exactly as stated: you have to already know the term to
know what the lesson is about. No carve-outs. The terms still get taught inside
their lessons and still appear in the app UI, where the learner meets them with
context around them.

**The accepted cost:** these titles are longer and less distinctive. That's the
trade — memorability for comprehension — and it's the right one for a sidebar
someone scans *before* they have the vocabulary.

### Module names need the same pass

The lesson pass doesn't fix the level above it. Module names are still framework
labels, and they're what a learner reads first:

| # | Current | Proposed |
|---|---|---|
| 0 | Start Here | Start here |
| 1 | Foundation: baseline, assumptions, and the confidence number | Your numbers and your first retirement date |
| 2 | Cash Flow + Reserve | Your monthly surplus and cash reserve |
| 3 | Allocation & Next-Dollar | How much Bitcoin to hold, and where new money goes |
| 4 | Debt Strategy | Using and paying down debt |
| 5 | Tax Strategy | Lowering your tax bill |
| 6 | Retirement Income | Turning the plan into a paycheck |
| 7 | Custody | Storing your Bitcoin safely |
| 8 | Estate & Inheritance | Passing your Bitcoin on |
| 9 | Maintenance (Capstone) | Keeping the plan current |
| 10 | Your Financial Plan Review | Reading your finished plan |

"Allocation & Next-Dollar" and "Maintenance (Capstone)" are the two worst —
"Next-Dollar" is internal shorthand, and "Capstone" describes the module's role
in the curriculum rather than what the learner gets from it.

Module descriptions already carry the plain-language version underneath, so
these mostly exist as sidebar labels. That's exactly where the scan happens.

### Two that need a decision, not just a rename

**8.1 — "The executor, the four legal documents, and choosing an estate
attorney."** The title is long because the lesson does three jobs, and at 1,674
words it's the longest non-walkthrough in the course. Shortening the title hides
that rather than fixing it. Either split off the attorney material, or keep the
long title as an honest label.

**5.2 — "The three buckets, your bracket roadmap, and the state lever."** Same
shape, 1,436 words, three subjects. The proposed rename is cosmetic; the real
question is whether the state lever is its own lesson. Note "State taxes and
relocation: a big lever" appears in `bootstrap-outline.json` as a planned lesson
— so it may have been folded in here.

### Knock-on work

Renaming is not just a field edit:

- **In-lesson hand-off sentences** reference the next lesson by name. At least
  3.1 does. Every hand-off needs checking after a rename.
- **Cross-module references** ("Module 7 covers…") are by module, so those are
  safe.
- **`ai-knowledge/`** — per `CLAUDE.md`, run `scripts/sync-ai-knowledge.sh` if
  any of this reaches app navigation or Settings groups. Course titles alone
  probably don't, but confirm.
- **Do this before filming.** A title said on camera that doesn't match the
  sidebar is a re-shoot.


---

## Terminology collision: "the three buckets" means two different things

Found 2026-07-29 from lesson 3.2's hand-off line.

| Where | What "the three buckets" are | Sorted by | Uses |
|---|---|---|---|
| **Module 3**, lesson 4.3 | Reserve / Bridge / Forever | **Time horizon** | 16 |
| **Module 5**, lesson 5.2 | Taxable / tax-deferred / Roth | **Tax treatment** | 8 |

Both introduce themselves the same way:

> *"Every dollar you own sits in one of three buckets."* — Module 3
> *"Where your money sits: the three buckets"* — Module 5

A learner is told twice, two modules apart, that their money lives in three
buckets — and they're different buckets both times. Worse, the two systems are
orthogonal and *combine*: a dollar has both a time-horizon bucket and a tax
bucket simultaneously. Lesson 4.5 (asset location) depends on exactly that
interaction, so the reader needs to hold both at once with no way to tell them
apart by name.

Lesson 3.2's hand-off makes it concrete: *"The next lesson covers the three
buckets that give every dollar in your plan a job"* — pointing at the Module 3
set, using a phrase Module 5 will later claim.

**The v2 renames already fix the titles** — 4.3 becomes "Splitting your money by
when you'll need it" and 5.2 becomes "Taxable, tax-deferred, and Roth: what goes
where". Neither says "buckets". But the **body text still collides**, which is
where the reader actually meets it.

**Options:**

1. **Give one of them a distinct name.** Module 3's is already Reserve / Bridge /
   Forever — those names are good and specific. Drop "three buckets" as the
   collective term there and let the three names carry it. Module 5 keeps
   "buckets", which is the industry-standard term for tax treatment anyway.
2. Qualify both every time ("time buckets" / "tax buckets"). Cheaper, but adds a
   word to 24 occurrences and still relies on the reader catching the modifier.

Option 1 is cleaner and is the smaller edit. Module 5's usage matches how CPAs
and every other planning resource talk, so that's the one to leave alone.


---

## 🔴 Math error: the couple's surplus is spent twice

Found 2026-07-29 while slotting lesson 4.4. **Highest-priority finding in this
document.** Per `CLAUDE.md`, wrong numbers are the worst possible failure, and
this is in the worked example that runs through the entire course.

**Lesson 2.1** reaches the surplus by *subtracting* retirement contributions:

| Step | Amount |
|---|---|
| Gross income | $190,000 |
| Taxes | -$40,000 |
| **401(k) contribution** | **-$12,000** |
| Living expenses | -$80,000 |
| Debt payments | -$22,000 |
| **Roth IRA** | **-$7,000** |
| **Surplus** | **$29,000 / year (~$2,400/mo)** |

**Lesson 4.4** then routes that same surplus *into* the same two accounts:

| Rung | Amount | |
|---|---|---|
| **401(k)** | **$1,000/mo** | = $12,000/yr — already deducted above |
| HSA | $300/mo | = $3,600/yr — never appears in 2.1 at all |
| **Roth IRA** | **$583/mo** | = $7,000/yr — already deducted above |
| Bitcoin + taxable | ~$517/mo | |

**$19,000/yr is counted twice.** It is removed from income to *produce* the
surplus, then presented as where the surplus *goes*. The couple's genuinely
uncommitted money is about **$9,800/yr (~$817/mo)**, not $29,000.

The HSA is a separate problem: $3,600/yr of contributions appear in 4.4 that
never existed in the 2.1 walk.

**Why it matters beyond the arithmetic.** 2.1 tells the reader *"That $2,400 a
month is the budget every later module has to work with."* Every downstream
module does use it. If the figure is overstated by roughly two-thirds, the
allocation splits, the contribution routing, and the reserve build-cap examples
all inherit the error.

### Two ways to fix it — Austin's call

**Option A — surplus is pre-routing.** Stop subtracting 401(k) and Roth in the
2.1 walk. Surplus becomes $48,000/yr (~$4,000/mo), defined as "money not already
committed to taxes, living, or debt." 4.4's routing table then works unchanged,
and the waterfall genuinely decides where retirement money goes.

*This is the more coherent framing* — the waterfall's whole premise is that it
decides the retirement contributions, so those can't already be settled before
the waterfall runs. It does mean the $2,400 figure changes everywhere it appears.

**Option B — surplus is post-routing.** Keep the 2.1 walk. Fix 4.4 to route only
the uncommitted ~$817/mo, and show the 401(k)/Roth rungs as *already satisfied*
rather than as new allocations.

*Smaller edit, but weaker teaching* — the waterfall demo shrinks to two live
rungs, which undercuts the lesson.

**Recommendation: Option A.** It matches what a surplus is for, and it makes 4.4
the lesson it's trying to be. Cost is a find-and-replace on the couple's numbers
across every lesson that quotes $2,400/mo or $29,000/yr.

**Before either fix:** re-check every other figure in the couple's story. The
same example carries through ~15 lessons and this error survived to publication,
so a full pass on their arithmetic is warranted rather than patching these two
lessons alone.


---

## Fixes applied to the course, 2026-07-29

Made directly in the Honen working revision (a draft fork of the published
revision, so reversible).

**Item 16 — 10 empty outcomes checklists. Fixed.** Replaced the shell-escaped
apostrophe `'"'"'` with `&#39;` in all ten `data-params` attributes. Verified:
**0 of 50** lessons now have a malformed attribute. Item text was untouched —
only the escaping changed.

Note the bug was invisible to a size check: `&#39;` and `'"'"'` are both five
characters, so file sizes are identical before and after. The only proof is the
`changedFiles` list and the re-scan.

**Item 3 — the CAGR claim. Fixed.** Lesson 1.2 now reads:

> **Bitcoin at 40% forever** (a deliberately conservative number, well under what
> Bitcoin has actually done). Earliest retirement lands around **age 50**.

Confirmed zero remaining "historical rate" claims anywhere in the course. Wording
is my draft — swap it if it doesn't sound like you, it's a one-line change.

### Not applied, and why

- **Item 17 (currency as LaTeX)** — the right fix is probably a platform switch
  to disable math rendering, not escaping 33 files. Escaping first would be
  wasted work and could look wrong if math is already off. Needs a look at
  Honen's settings.
- **Item 22 (double-counted surplus)** — Option A vs B changes the couple's
  numbers across ~15 lessons. That's a decision, not a fix.
- **Items 20/21 (renaming, terminology)** — same: the naming is approved in
  principle but which term wins is yours to call.

---

## Terminology tangle: four systems, three of them overlapping

Lesson 4.6 exposed the last piece. Consolidating item 21:

| System | Names | Where | Sorts by |
|---|---|---|---|
| A | Reserve / Bridge / **Forever** | Module 3 course text | Time horizon |
| B | Reserve / Bridge / **Legacy** | **The app itself** | Time horizon |
| C | "the three buckets" | Module 5 | Tax treatment |
| D | "the three **wrappers**" | Lesson 4.5 | Tax treatment |

**A vs B is the worst of these** — the course and the product disagree on the
name of the same feature. Lesson 4.6 has to stop mid-walkthrough and say so:

> *"Note: Legacy is what the app calls the Forever bucket. Same thing."*

A course whose job is teaching people to drive the app should not need that
sentence. Either the app adopts Forever or the course adopts Legacy. Given the
app is the thing users live in, **Legacy probably wins** — but "Forever" is the
better teaching word and it's load-bearing in Module 3's framing, so this is a
real product call, not a copy edit.

**C vs D** is a straight duplicate: two names for taxable / tax-deferred / Roth,
one module apart. Pick one. "Wrappers" is more precise; "buckets" is more common
in client conversation.

**A/B vs C/D** is the collision already logged: "buckets" means both time horizon
and tax treatment, and lesson 4.5 needs the reader to hold both at once.

**Suggested resolution:** time horizon keeps the three proper names (Reserve /
Bridge / Legacy) and drops "buckets" as its collective noun. Tax treatment keeps
"buckets" *or* "wrappers" — one of them — everywhere. That leaves each concept
with exactly one name and removes the need for 4.6's apology line.


---

## Stale in-module references: fixed as found (running log)

The outline restructure cut intro lessons from several modules, shifting every
"Lesson N" reference inside them. Fixed directly in the course under the
standing policy, each verified single-occurrence first:

| Lesson | Was | Now |
|---|---|---|
| 6.4 closer | "next lesson covers relocation" (folded into 5.2) | points at walkthrough |
| 7.3 closer | "next lesson covers advanced custody" (folded into 7.1) | points at external demo |
| 7.5 | refs to Lessons 2/3/5 | Lessons 1/2/3 |
| 7.5 Step 5 | custody level "(Foundation/Substantial/HNW)" — those are the estate tiers | "(1 to 4, from Lesson 1)" |
| 8.1 | broken UTF-8 byte in "Directive anticipée" | repaired |
| 9.6 closer | "next lesson covers the attorney questions" (they're in 8.1) | routes to walkthrough via Lesson-1 pointer |
| 9.7 | five refs: Lesson 4→3, 2→1, 6→5 (×2), 7→6 (×2) | fixed |

**Left alone (ambiguous):** 9.7's "estate-level self-triage from Lesson 2" —
no module-8 lesson contains a self-triage; the likely target is the custody
module's five questions or an outline lesson that was cut. Needs Austin.

**Module 9's internal refs were checked and are correct** — the only module
whose numbering survived the restructure intact.


---

## Toolkit PDF verification (2026-07-29)

Austin supplied the three toolkit PDFs. Text extracted mechanically and every
claim the course makes about them checked. **The documents are in excellent
shape** — near-perfect agreement with the lessons that describe them.

### Verified correct, claim by claim

**06 The Heir Letter** — "NEVER IN THIS LETTER" banner present with the exact
never-list from lesson 8.3 (including "exact recovery steps" and "where the
config file lives"); the opening line to the family and the closing "FROM ME TO
YOU" section both present, exactly as 9.7 promises; call order matches 8.3
(executor → attorney → technical helper); header correctly says Module 8.

**07 Family Custody Map** — the "location only — never the words, PIN, or
passphrase" caption 7.5 quotes is there; footer "Review yearly — Module 9"
matches; header correctly says Module 7. The PDFs carry the *current* module
numbers — they postdate the outline restructure that left the stale in-lesson
references.

**08 The Executor Packet** — all six sections in the exact order 9.7's table
lists; "a dozen certified copies" of death certificates; section 2 names the
Heir Letter and Family Custody Map, as claimed; the Acceptance language 9.7
quotes is **verbatim** in the PDF, both signature lines present; footer review
note matches.

### Found and fixed (course side)

**7.5 said the Custody Map "has four blocks" — the PDF has five.** The lesson's
table omitted INSURANCE & OTHER (policies, property, anything else the family
should find). Fixed in the course: table now lists all five. This block is also
where the map connects to 8.5's insurance audit, so omitting it undercut a
cross-module link the documents themselves make.

### Found, needs Austin (item 26 — PDF edits, not course edits)

Two PDF footers claim app behavior the course's own walkthroughs say doesn't
exist:

| PDF | Footer claims | Course says |
|---|---|---|
| 07 | "In Orange Plan: Protect → custody map keeps this live and **reminds you yearly**" | 7.5/10.4: "There is no scheduler in Orange Plan"; no "custody map" surface is named in Protect — the checklist plays that role |
| 08 | "In Orange Plan, Protect → **executor packet** tracks contacts and **reminds you when it's stale**" | No executor-packet surface appears anywhere in the walkthroughs; the packet is toolkit-only |

06's footer, by contrast, is accurate ("Protect → heir letter tracks contacts
and content, exports the PDF") — that surface exists exactly as described.

Either the app grows those surfaces/reminders, or the two footers get softened
to match ("pair with your annual review" instead of "reminds you"). Users who
follow a footer to a feature that isn't there is the same failure mode as a
stale hand-off, but in print.

### Item 15, sharpened

The 06/07/08 numbering still implies 01–05 exist. New evidence: lessons 8.5 and
9.7 tell learners to use "the Coverage Audit worksheet" but — unlike 06/07/08,
which get explicit 📎 Materials pointers — it's never given a location or
number. If it's one of 01–05, the course sends people to a document without
saying where it lives.


---

## 27. Readability / simplicity audit (2026-07-30)

**Method.** Flesch-Kincaid Grade Level and Flesch Reading Ease run over every
lesson in MASTER-COURSE.md, with my flag blocks, tables, headings and list
bullets stripped and money/percentages normalised so `$1,250` counts as one
word, not three.

**Result: median grade 6.3, reading ease 73.3. 47 of 49 lessons at or below
grade 8. Zero lessons at grade 10 or above.** The prose is already at or below
6th-grade reading level. Sentence difficulty is NOT the barrier.

Hardest lessons (grade / ease / words-per-sentence):
```
8.3  4.5 Asset location                     15.5 w/sent   <- only real outlier
7.3  4.4 Every debt gets a job              19.4 w/sent   <- longest sentences
7.7  6.3 The RMD risk + Roth conversions    12.1
7.4  9.7 Walkthrough: backstop + estate tax 14.9
6.2  1.3 The confidence ring                14.6
```
Easiest: 0.1 (4.6), 2.3 (4.8), 2.2 (4.9), 4.1 (5.0), 6.3 (4.3).

**The three actual barriers (not reading level):**

1. **Term density.** roth 78, bracket 76, basis 74, trust 61, confidence 58,
   taxable 55, conversion 44, drawdown 42, passphrase 38, LTV 37, harvest 34,
   RMD 33, multisig 25.
2. **Define-late gaps** (term used N modules before it is explained):
   - LTV used in 1.4, spelled out in 4.1 -> 3 modules late. FIXED.
   - RMD used in 4.4 table, defined in 6.3 -> 2 modules late. FIXED.
   - passphrase / multisig used in 3.1, taught in Module 7. FIXED (inline gloss).
   - Roth used in 1.4, never defined anywhere. FIXED.
3. **Lesson length.** Median 750 words; 4 lessons over 1,400:
   1.4 (2,812 - by far the largest), 4.6 (1,703), 7.1 (1,669), 9.7 (1,431).
   In the live Honen draft, restructured 8.1 is 2,321 words.

**Fixed directly in the Honen draft (mechanical first-use definitions):**
- 1.4 L125 `live LTV` -> `live LTV (loan-to-value: what you owe divided by what
  the collateral is worth)`
- 1.4 L143 `**Roth IRA.**` -> prefixed `(Roth means you pay the tax now, and the
  growth and the withdrawals come out tax-free later.)`
- 4.4 L20 `no RMDs.` -> `no RMDs - no required minimum distributions, the
  withdrawals the government forces out of traditional accounts once you reach a
  certain age.`
- 3.1 L53 passphrase gloss; L61 multisig gloss.

**Still open (decisions, not fixes):**
- 4.5 Asset location is the one lesson with genuine prose difficulty (grade 8.3,
  15.5 w/sent). Candidate for a sentence-level rewrite before filming.
- 4.4 Every debt gets a job has the longest sentences in the course (19.4).
- 1.4 at 2,812 words is the strongest split candidate in the course, ahead of 8.1.
- A one-screen glossary lesson (item 8, "How to read the app") would carry the
  13 heavy terms above; the report already exposes a "What these terms mean"
  glossary panel we can point at instead of duplicating it.


---

## 28. "Update Transactions" coverage audit (2026-07-30)

**Question:** does the course explain how to update transactions in the app?

**Answer: yes, in six places, but thinly and with two real gaps.**

Coverage map (all verified against the course source):
| Lesson | What it says |
|---|---|
| 1.1 Gather your numbers | download transaction-history CSVs from every exchange and brokerage |
| 1.4 Step 6 (onboarding) | the Transactions onboarding step; tells you to hit **Skip for now** |
| 1.4 Step 3 (baseline lap) | the three (now four) update methods |
| 2.4 Cash flow walkthrough | Verify Spending needs 2-3 months of linked/imported transactions |
| 5.3 Tax walkthrough Step 1 | the deepest treatment: Dashboard -> Update Transactions -> file path, the two questions, dedupe against earlier imports |
| 11.1 / 11.2 Annual review | the dialog source step, the choices table, the review-before-save rule |

### Gap 1 — the course says THREE methods, the app offers FOUR. FIXED.
`TransactionsAutopilotStartSteps.jsx` renders four `SourceChoice` tiles, and
`Dashboard.jsx:1576-1577` always passes both `onOpenAIEntry` and
`onOpenManualEntry`, so all four are always visible. The course was missing
**"Describe one transaction to AI"** (*"Tell Orange Plan AI about one purchase
or sale. Review every field before saving."*) in both places that enumerate
them.

Fixed in the draft:
- 1.4 Step 3 — list rewritten to four, using the app's own labels
  (`A linked account` / `A downloaded file` / `Describe one transaction to AI`
  / `I'll enter them myself`), and the dialog's real heading added
  (*"How would you like to update transactions?"*). Also corrected
  "Import a CSV" -> "a CSV **or Excel** export", matching the app.
- 11.2 Step 2 — "Three choices" -> "Four choices", AI row added to the table,
  and the linked-account row now quotes the real sub-copy instead of a
  paraphrase.

### Gap 2 — CORRECTING an existing transaction or lot is never covered. OPEN.
The course teaches how to GET transactions in. It never teaches how to fix one
that is wrong, which is the more common real-world need and is where the Tax
module's "reconstruction homework" actually gets done.

What exists in the app and is unnamed in the course:
- **Dashboard -> a holding row -> `Lots` button** (or the row's three-dot menu)
  -> dialog **"Purchase Lots - {asset} ({ticker})"**, sub-line *"Track purchase
  lots to keep cost basis accurate."* (`ManageLotsDialog.jsx`, wired at
  `Dashboard.jsx:1360`/`1378`/`1612`). Add, edit, and delete purchase lots.
- **The lock rule a student WILL hit:** a purchase lot already consumed by a
  sale cannot be edited. `isPurchaseLotEditable()` gates it, the row's edit
  button goes to aria-label *"Purchase lot locked by a sale"* with title
  *"Delete related sales before editing this lot"*, and the error reads
  *"This lot has already been used in a sale. Delete the related sell
  transactions first so lot history stays accurate."*
- **The duplicate guard:** *"Remaining lot quantity exceeds this holding by X.
  Edit or delete duplicate lots instead of adding a new one."*
- Holding rows also expose **Add transaction** and **Transfer**
  (`openTransactionDialog`), separate from the Update Transactions dialog.

**Recommendation:** a short "fix a wrong transaction" section, ~250 words,
appended to the 5.3 Tax walkthrough (where basis reconstruction already lives)
rather than a new lesson. Needs Austin's voice on the lock rule - it is a
real friction point and reads as a bug unless it is explained as a
lot-history-integrity guard. FLAGGED, not written.


### Gap 2 — CLOSED (2026-07-30)

Wrote **"### Fixing a lot that came in wrong"** (~300 words) into the 5.3 Tax
walkthrough, placed at the end of Step 2 (Land on the lots) so it sits right
where the coverage banner tells the student something is broken. No step
renumbering — it is an H3 inside Step 2, not a new Step.

Covers: the `Lots` button path and the Purchase Lots dialog; the neighboring
Add transaction and Transfer actions (Transfer verified against
`AddTransactionDialog.jsx:344-350` — moves the holding and its full history,
preserves dates and cost basis, explicitly NOT a disposition); the sold-lot
edit lock, framed as a history-integrity guard with the unwind order
(delete the sale, fix the lot, re-enter the sale); and the duplicate-quantity
guard framed as "that's a double import."

Lesson integrity re-verified: 1 H1, 1 artifact open, 1 close. 1,321 -> 1,625
words. "What good looks like" already leads with the coverage banner
reconciling, which is exactly this section's outcome — no change needed there.
Left the "about 20 minutes" estimate alone: the fix section is a branch most
students will skip.

MASTER-COURSE.md synced with all of items 27 and 28 (glosses, the four update
methods in both 1.4 and 11.2, and the new lot-fixing section). Now 6,120 lines
/ 52,557 words.


---

## 29. Item 22 RESOLVED — Option A applied (2026-07-30)

Austin delegated the call ("do what you think is best for the program").
**Chose Option A**: surplus is defined pre-routing. The waterfall's premise is
that it DECIDES the retirement contributions, so those cannot already be settled
before it runs. Option B keeps the arithmetic honest but collapses lesson 4.4 to
two live rungs, which guts the lesson it is trying to be.

### Canonical fact sheet for the couple (all figures now derive from this)

| Item | Value |
|---|---|
| Gross income | $190,000/yr = $15,833/mo (course rounds to $15,800) |
| Taxes (fed + payroll, no state) | -$40,000 |
| Living expenses | -$80,000 |
| Debt service (mortgage + car) | -$22,000/yr = $1,833/mo (course rounds to $1,850) |
| **Surplus (pre-routing)** | **$48,000/yr = $4,000/mo** |
| Waterfall: 401(k) / HSA / Roth | $1,000 + $300 + $583 = $1,883/mo |
| Waterfall: Bitcoin + taxable | **$2,117/mo** |
| Debt | $280,000 mortgage @3.25% + $18,000 car @7% = $298,000 |
| Assets | $175k BTC + $90k funds + $30k cash + $450k house = $745,000 |
| DTA | 298/745 = 40.0% |
| DTI | 1,833/15,833 = 11.6% ~ 12% |

Every one of these was re-derived and asserted in code, not eyeballed.

### Edits applied

- **2.1 Find your surplus** — deleted the `401(k) contribution -$12,000` and
  `Roth IRA -$7,000` rows; surplus $29,000/$2,400 -> **$48,000/$4,000**; added a
  paragraph explaining WHY contributions are not subtracted (they are decisions,
  not expenses, and Module 3 is where they get made). That paragraph is the
  teaching payload of the fix, not decoration.
- **4.4 The contribution waterfall** — "$2,400/mo surplus routes" ->
  "$4,000/mo"; Bitcoin + taxable rung ~$517/mo -> **~$2,117/mo**.
- **9.3 The annual review** — DTI reconciled from the unsourced "~$1,600/mo …
  ~10%" to "~$1,850/mo … ~12%", matching 4.1 and deriving from the $22,000
  debt-service line. (This closes item 25.)

### The trap that a find-and-replace would have sprung

Lesson 2.3 "Size the reserve to your life" contains an UNRELATED **$2,400/mo** —
the retirement spending gap ($80,000 spending - $51,600 Social Security =
$28,400/yr). A blind replace of "$2,400" would have corrupted the reserve-sizing
example. It was left untouched. Option A incidentally REMOVES the collision,
since the surplus is now $4,000/mo and $2,400/mo means only one thing in the
course.

### Also fixed this pass

**Lesson 4.1 Defense** carried two leftovers from my own Module 4 restructure: a
stray mid-lesson "The next lesson covers…" hand-off sitting before the app
section, and a duplicated "Have every debt's balance, rate, minimum payment, and
term ready." sentence. Both deleted; 1,149 -> 1,117 words. A scan of all 12
restructured lessons (Modules 4 and 8) found no other duplicate lines or
misplaced hand-offs.

### Transport fidelity warning (affects any future export)

While reading 4.1, `cat` returned `Ã·` where the file actually contains a correct
`÷` (octal `303 267` = 0xC3 0xB7). `grep` rendered the same character correctly
in the same response. The sandbox transport is NOT reliably byte-faithful for
non-ASCII, and the corruption is sporadic rather than systematic. Any lesson
transcribed from `cat` output must be checked with a per-line non-ASCII codepoint
audit before it is trusted. Related: the sandbox's `wc -c` returns CHARACTERS not
bytes, and its `md5sum` is not comparable to GNU `md5sum` — cross-boundary md5 is
a broken checker and produced one false alarm already.


---

## 30. Master-file gap CLOSED — full course sync (2026-07-30)

The master is now a verified faithful copy of the entire Honen draft. Method:
the sandbox md5 was reverse-engineered (it hashes UTF-16 code units mod 256,
not bytes), giving a one-hash-per-lesson byte-exact verification both sides.

**Verified exports (16 lessons, every one hash-MATCH):** all of Module 4
(4.1-4.5) and Module 8 (8.1-9.7) post-restructure, plus walkthroughs 7.7, 7.5,
10.4, 11.2. Files in `lessons/`.

**Fingerprint alignment (word-count streams) for Modules 1-2 drift:** 2.1 and
2.2 proved IDENTICAL to Honen. 1.4 was missing 8 production-note lines and 2.4
missing 8 — all were the walkthrough-audit ⚠ notes added Honen-side and never
synced. All 16 patched into the master at their anchors.

**Real content corruption found IN the course and fixed there:**
- 4.1: three `Ã·` mojibake (should be ÷) — the earlier "transport artifact"
  diagnosis was WRONG; od shows codepoints, not bytes, so the file genuinely
  contained the mojibake.
- 8.3: mojibake ⚠ and 4× → on the two pre-flight lines; also `Â·`.
- 9.7: 12 table arrows and 2 em-dashes mojibake'd.
- 3 lessons (7.4, 8.1, 8.3) carried a LONE UTF-16 SURROGATE (broken 📎 emoji)
  that renders as �. The channel cannot round-trip astral chars at all (writes
  lose the low surrogate too), so the emoji was dropped in Honen; local files
  keep plain text. NO astral emoji can ever be written to Honen via MCP.
- Course-wide scans now clean: zero mojibake patterns, zero lone surrogates.

**2.3:** two stale inline annotations ("This is the table to remove",
"Missing a fourth row") converted to proper > flag lines tied to item 18.

**Master final:** 6,526 lines, ~54,300 content words, 50/50 lessons at parity.

## 31. FILMING-CHECKLIST.md created (2026-07-30)

Production plan derived from the synced master: 31 talking-head / 11 screen /
8 hybrid lessons, ~53,400 spoken-source words ≈ 5¾ h raw narration at 155 wpm.
Phases: (0) demo-account seeding with the canonical fact sheet + the four
blocking decisions (renames, 2.3 rebuild, Retirement Income push, 2026-figure
verification); (1) teleprompter prep rules (strip ⚠ notes/outcomes/tables,
hybrid cut point = "Now put it in the app"); (2) batch shooting order (4 camera
days + app-capture days in course order); (3) per-lesson checkbox table with
word counts, runtime estimates, and lesson-specific capture prerequisites
lifted from each walkthrough's own pre-flight.


---

## 32. App-vs-course verification sweep #2 (2026-07-31)

**Method.** All 285 quoted UI strings in MASTER-COURSE.md extracted and matched
against a normalized corpus of all 681 non-test source files, with a second
targeted-fragment pass for the 85 the first pass couldn't auto-match. Plus a
git-log review of every src/ commit since the last audit (2026-07-15).

**Result: the course matches the app everywhere except one page — and that
page changed 2 days ago.**

- 117 strings verified verbatim; the rest resolved to placeholder templates
  (verified by fragment), course-invented spoken lines (not UI claims), or one
  HTML-escaped `&amp;` false miss.
- **Commit 073fdf0 (2026-07-29, Austin's Retirement Income push) replaced the
  Income page's "Compare withdrawal approaches" card** — the one 7.7 Step 5
  documented. Gone: the Compare strategies button, the 3-row comparison table,
  winner badges, the "Lasts to" column, the Tax bracket fill preset chip, the
  Advanced → Withdrawal order → Show disclosure, the "Most plans leave this on
  Bitcoin-last" note, and the UNSAVED/✓ Applied save chips. New: a promoted
  "Withdrawal order" section (eyebrow "Income strategy"), a live 3-tile outcome
  strip (Bitcoin at LE / After-tax net worth at LE / Lifetime taxes) with
  signed deltas vs the saved plan, 4 preset chips (Balanced, Preserve Bitcoin,
  Blended drawdown, Avoid early penalties), the two segmented order controls
  always visible, and Apply to plan / Revert.

**Fixed (Honen + master + lessons/07-7, all three hash-verified in sync):**
- 7.7: Step 5 rewritten as "Set the withdrawal order"; old Step 5b absorbed
  (the controls ARE the section now); outcomes checklist item, "What good looks
  like" bullet, and What-got-built row 4 updated. 1,901 → 1,918 words.
- 7.4 "In the app": the bracket-fill pointer now routes through Withdrawal
  order → Custom phases → Bracket-aware rule + ceiling, which is where
  bracket-fill actually lives post-redesign (verified in
  DrawdownPhaseControls.jsx / incomeStrategyDrafts.js — tax_bracket_fill is
  deliberately excluded from the chip list).
- Verified NOT damaged: the Tax page's Roth "Compare strategies" table (5.3
  Step 4) is a different feature and survives; Income Blueprint tab, "Review
  income plan" button, and the whole Retirement operating plan section are
  untouched.

**Also checked, still true after the last 3 weeks of commits:** dead-man's
switch strings (2 commits touched internals, no copy changes), Cash Flow income
rows (rename/remove commits added copy, removed none the course quotes),
onboarding step strings, lot/import dialogs, Protect/estate strings.

**Filming impact:** the checklist's 7.7 blocker is cleared; its note now says
the push landed and the script matches the new UI.


## 33. Screen-share structure (2026-08-04)

Austin asked whether the master marks where screen shares are filmed. It
didn't — only by convention. Two changes:

1. **19 🎥 markers inserted in MASTER-COURSE.md** (flag lines, stripped from
   teleprompter text): full-lesson banners on the 11 walkthrough/check/demo
   lessons; a "SCREEN SHARE STARTS HERE — segment {n}-B" cut-point marker at
   "Now put it in the app" in the 8 hybrid lessons.
2. **SCREEN-SHOOT-LIST.md** generated: capture run sheet in course order —
   19 segments, ~184 min raw capture at screen pace (120 wpm), each with
   pre-record app-state checkboxes (pulled from the lessons' own
   Pre-flight/Prerequisites) and tickable beats (step heading + click path).

Segment IDs: lesson number for full-lesson captures (e.g. 5.3), {n}-B for
hybrid app tails (e.g. 4.1-B; the matching A-roll is {n}-A).


---

## 34. Evergreen-numbers policy (Austin, 2026-08-04) — CLOSES item 11

Austin's rule: the course must not show current-year numbers so it lasts into
next year. Full sweep of the master for year-pegged figures:

**Already compliant (by design):** scripts never speak a law-set number; 5.2
and 6.3 frame all bracket/deduction/RMD figures as tilde-marked snapshots with
"these move every year" language; 7.2/6.2 use "verify current law" phrasing;
9.6 bans speaking the exemption aloud.

**Four leaks found and fixed (master + Honen + scripts):**
1. 1.4 quoted the app's SS helper including "~$1,900/mo" average → course text
   now says the helper points to ssa.gov/myaccount, no figure.
2. 4.4 "Maxing $7,000/yr" (the IRA limit, law-set) → "Maxing the year's IRA
   limit ($7,000 when they ran it)" — arithmetic chain ($583/mo → $2,117
   remainder) intact, figure framed as a snapshot.
3. 9.6 quoted the app sub-caption with "$15M" baked in → "{amount}".
4. The two item-11 "verify 2026 figures before filming" flags → replaced with
   the policy: DON'T re-verify yearly; figures stay as framed snapshots.

**Policy now in FILMING-CHECKLIST (Phase 0) and SCREEN-SHOOT-LIST (header):**
never speak a law-set number as fact; keep snapshot framing on worked
examples; on screen captures never zoom/dwell on a law number — call it "the
current number the app shows." The app updates with the law; the video doesn't
have to.

**🐞 APP BUG flagged (not fixed here — orange-plan repo, product decision):**
`src/components/onboarding/steps/SocialSecurityStep.jsx:268` hard-codes
"The average is ~$1,900/mo." in onboarding helper copy. That static string
ages in the APP exactly the way Austin doesn't want the videos to. Suggest
removing the average or sourcing it from a maintained constant.

## 35. Filming rhythm confirmed (Austin, 2026-08-04)

One module at a time, chronologically. Per module: sitting 1 = all
teleprompter A-roll for the module back-to-back (talk lessons + hybrid -A
segments); sitting 2 = the module's screen captures in shoot-list order
(walkthrough/check lessons + hybrid -B segments). Hybrids were designed for
exactly this split-and-edit-together flow. App state carries forward module to
module, which matches chronological order by construction.


---

## 36. International/foreign-law content removed (Austin, 2026-08-04)

Austin: "I don't know international law so we should not be talking about that
stuff." Correct call — the course was making specific claims about UK Trustee
Act 2000, forced heirship, nil-rate bands, alter-ego trusts, superannuation
nominations, and EU civil-law instruments, none of which Austin can vouch for
on camera, and which sit badly with the educational-not-advisory posture.

**Removed (master + Honen + scripts, ~900 words):** all seven "For non-US
holders" sections (5.1, 5.2, 6.3, 6.4, 8.1, 8.5, 9.6) including the
US/UK/Canada/Australia/EU document-equivalence tables and the rewritten
UK-attorney question; foreign-law claims trimmed from the 8.1 and 9.6 banners.

**Replaced with** one standard short section: "If you're outside the US — this
course teaches US rules. The frameworks travel well, but the account types,
tax rules, and legal containers don't. Map the concepts with a qualified local
professional." Banners simplified to the same posture.

Hand-off lines inside the removed sections were preserved. Honen edits hit the
usual sandbox mojibake (octal em-dashes stored as 3-char sequences) — caught
by the standard scan and fixed; course verified clean.

## 37. Architecture confirmation: students read structure, videos speak prose

Austin: "we don't want scripts to be the text users read... step by step
instructions for implementation, and lessons with clear explanations."
Confirmed — that IS the current architecture, no change needed:
- Honen lessons / modules-md = student-facing: structured explanations,
  tables, step-by-step walkthrough instructions. Bullets are a feature here.
- scripts/ = video-only narration layer, converted to spoken prose (2.2 done,
  38 pending Austin's verdict on the sample). Spoken conversions NEVER flow
  back into student text.


---

## 38. Voice calibration COMPLETE — Austin dictated 2.2 (2026-08-04)

Austin dictated lesson 2.2 himself. His dictation now IS the 2.2 script
(cleaned only for stutters and the cut-off final sentence), replacing both AI
versions, and is marked as the calibration master every other conversion must
match. Guide updated with dictation-derived rules: "In today's lesson" opener,
future-tense "going to" scaffolding, "I think" hedges on every judgment,
unpack-don't-compress, explicit "because" on claims, homework as a spoken
numbered list, and the teach lesson referring to app work as "the walkthrough
below this video."

**Content decisions Austin made while dictating — propagated to lesson text
(master + Honen 2.2):**
1. Drawdown recovery window: "1 to 3 years" → "about 1 to 5 years" (more
   conservative; his call).
2. NEW retirement-reserve guidance: sequence-of-returns risk fades ~5 years
   into retirement; after that the reserve can shrink toward a 12-month floor,
   or run up to ~3 years for the risk-averse.

**Flagged, not changed:** his dictation collapsed the four-options question
(hold cash / sell / borrow / cut) to two-ish options — the borrow option
didn't appear. The lesson text still teaches four. Needs Austin's call:
deliberate simplification (update lesson + app cross-refs) or dictation
omission (script keeps four when he re-records)?

**Structural signal:** "the walkthrough below this video" — teach video and
walkthrough video are separate assets on the same lesson page. Matches the
hybrid A/B filming model already in place.

## Item 39 — Confidence verdict bands (decided 2026-08-04)

> 🚩 **DECIDED, PENDING APP CHANGE (Austin, 2026-08-04):** confidence verdict
> bands move to **80+ on track · 70-79 review · <70 needs attention** (red line
> raised from 60 to 70; research: MoneyGuidePro 70-90 zone, Kitces 70-90 with
> adjustment plan, aim 80-95). App still renders 80/60 today
> (`VitalsStrip.jsx` ~L307; `confidenceDisplay.jsx` also uses a 50 line —
> unify when implementing). DO NOT film any bands on-screen readout in 1.3/1.4
> until the app ships this, then update course copy to match.
