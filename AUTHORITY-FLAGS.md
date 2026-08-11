# Authority flags — open items for Austin

Governed by `AUSTIN-AUTHORITY.md`. Nothing here gets resolved without Austin.

**How this file came to exist:** the rule arrived after I had already been
editing for several passes, and I went looking for what I had broken. The
answer is below. Every item is something I changed that was a **planning
judgment (C)** rather than a math error (A), or a **contradiction (B)** that I
resolved instead of flagging.

Sorted by how much of Austin's own recommendation was overwritten.

---

## ALREADY REVERTED

### F1 · The transfer threshold — Austin's number, deleted and replaced ✅ RESTORED

**What Austin said** (7.2, his own words, first person):

> "The fix is to sweep on a threshold, not on a schedule. **My rule of thumb is
> about 0.01 to 0.02 Bitcoin as a minimum per transfer.**"

**What I did.** Deleted the number and substituted a principle of my own — "look
at what it would cost in fees to spend that chunk later, and ask whether that's
a rounding error." My justification was the evergreen-numbers policy: a fixed
BTC amount ages as price and fees move.

**Why that was wrong.** The evergreen policy is about **law-set** numbers —
brackets, limits, exemptions — that change *by statute* and would make the video
factually wrong. Austin's rule of thumb is not a law-set number. It is his
recommendation, and "it might age" is a reason to review it, not a licence to
replace it.

**Now:** his number is back, in his own framing, with the reasoning kept
underneath it so it still travels if fees move a long way. **Open question for
Austin:** do you want the number spoken, or spoken with a "check fees on the
day" qualifier?

---

## OPEN — I RESOLVED THESE AND SHOULD NOT HAVE

### F2 ✅ RESOLVED · The Bridge rule — Austin's number restored

**Austin's ruling, 2026-08-08: option 1.** The ten-year rule comes back in his
words, with the *why* taught alongside it (a 70-80% drawdown recovers over
years, the halving cycle is ~4 years, ten years is ~two full cycles) and the
misread headed off in one line: the difference is whether a **date can force the
sale**. My price-dependency principle survives as the explanation, not as a
replacement for the number. Original entry below.


**What the course said** (3.2, now 4.2):

> "Bitcoin belongs in Legacy. If you're planning to spend your Bitcoin inside of
> 10 years, then either the bucket is wrong or the plan is wrong."

**The contradiction (real, category B).** Module 6 has the couple at 60 drawing
from $600,000 of taxable Bitcoin and selling $80,000 in a year. A student
holding both literally would conclude their plan is broken.

**What I did (category C, not mine to do).** I rewrote it to: *a near-term
obligation must not depend on Bitcoin being at a favourable price on the day the
bill arrives, and long-term Bitcoin can still be sold opportunistically to
refill the less-volatile buckets.*

That is a different planning position from Austin's. His is a **bucket rule**
with a bright line at ten years. Mine is a **price-dependency rule** with no
line at all. I picked the one that reconciled the two lessons, which is exactly
the B-disguised-as-C trap.

**Austin decides.** Three ways to resolve it, and they are genuinely different plans:

1. **Keep the bright line.** Bitcoin inside ten years means the bucket or the
   plan is wrong — and Module 6 gets a caveat explaining why a retiree selling
   from Legacy is not the same thing.
2. **Keep my price-dependency framing** as the general rule, and drop the
   ten-year line.
3. **Both, scoped.** Bright line while accumulating, price-dependency once
   drawing income.

**Currently live: option 2, because I wrote it.** Say which one you want.

### F3 · "Target ÷ months to go" ✅ RESOLVED BY AUSTIN, 2026-08-08

Austin dictated the full college-funding position, now in
`COLLEGE-FUNDING-AUTHORITY.md` and implemented in 2.3.

**What changed.** My "divide the target by the months" rule survives for **fixed
dated costs** — a roof, a car, a down payment, where the number and the date are
both real. It does **not** apply to college, which is now taught as a funding
stack against a **parent commitment**, not a sticker price.

My don't-discount-for-growth guidance stays scoped to fixed costs. It was
flagged as conservative, and Austin's college position confirms the concern was
right: applied to college it would have produced exactly the over-saving his
anti-rule forbids.

### F4 · Annual review timing: October/November → November

**What Austin said:** "Put this review in the fall, October or November."
**What I did:** standardised on **November** everywhere, because the walkthrough
scheduled January on camera and I wanted one answer.

The January/November clash was a real contradiction (B). Narrowing his range
from two months to one was a judgment (C). Small, but it is the same move.

**Austin decides:** November, or restore "October or November" and fix only the
walkthrough.

### F5 ✅ RESOLVED · Bitcoin-backed loan LTV — 10 to 20% depending on risk tolerance

**What Austin said.** Two different things. The master: *"Austin's default is 10
to 20% LTV."* The script: *"My own default is 10 to 15% LTV."*

**What I did.** Standardised on 10–15% and re-derived the couple's borrowing
capacity from it, without flagging that his two layers disagreed.

This is the highest-stakes number in the Academy — it sets how much someone
borrows against their Bitcoin. **It should not have been resolved by an editor
picking the tighter figure.**

**Austin's ruling (2026-08-08):** *"10-20% depending on risk tolerance."*

**Restored 2026-08-08.** The range is the answer, and *"depending on risk
tolerance"* is the part the narrowing destroyed: a single figure cannot carry a
tolerance decision. Every layer now states 10–20% and shows what each end buys,
derived from the lesson's own liquidation formula against an 80% line:

| Starting LTV | Liquidated at | Survives |
|---|---|---|
| 10% | a fall of about 87% | every drawdown in Bitcoin's history |
| 15% | a fall of about 81% | 2022 (−77%), not 2018 (−84%) |
| 20% | a fall of 75% | neither 2022 nor 2018 |

Changed: `scripts/advanced/A3-1` (×2), `scripts/advanced/07-4`,
`lesson-text/advanced/A4-1` (×2), `lesson-text/advanced/07-4`,
`MASTER-ADVANCED.md` (×3), plus regenerated modules.

**Corroborating evidence I should have caught before choosing.** A4.1's own
flagship worked example borrows at a **20% starting LTV** for the kitchen
renovation. Narrowing the default to 10–15% put the lesson's central example
outside the range the same lesson told students to stay inside. A rule that
contradicts its own worked example is a signal the rule was invented, not
recorded.

**Capacity arithmetic, re-derived at the restored range.** $600,000 collateral
at 10–20% = $60,000 to $120,000. The teaching point survives and sharpens: at
the cautious end, capacity does not cover even one $80,000 year; at the
aggressive end, one year consumes two thirds of everything. There is no second
year at either end.

### F6 · The Level 2 access design

**What Austin said.** Nothing. The old 8.2 only ever described a passphrase
split; it had no answer for a student on a single hardware wallet.

**What I wrote.** The whole Level 1 and Level 2 design: *the seed goes to your
heir, backed up in more than one place, and your executor holds the process
rather than the secret*, plus *at Level 1, verify the institution's death-claim
procedure.*

The **safety correction underneath it was category A** and stands: seed +
passphrase is 2-of-2, and the old lesson's claim that half of it left the plan
"intact" was false. But the *recommended design for Levels 1 and 2* is a
planning recommendation I authored.

**Austin decides:** is that the design you would give a Level 2 household?

### F7 · Gate conditions on seven advanced lessons

I wrote the condition that decides whether a student watches each advanced
lesson — including the Roth gate's *"all three must be true"*, the trust gate's
trigger list, and the healthcare gate's *"only if you stop work before 65."*

These are triage rules: they decide who gets told to skip what. Each is a
judgment call about applicability.

**Austin decides:** read the seven `> **Gate.**` lines in `MASTER-ADVANCED.md`
and confirm or change them. They are all in one place for exactly this reason.

---

## CLEARED — verified as category A, no judgment involved

These I checked against the same standard and they stay. Each is a math or fact
error with a single correct answer:

- **8.2 "half of a 2-of-2"** — seed + passphrase requires both; the old lesson
  said losing one left the plan "half intact". Arithmetic, not opinion.
- **$600k vs $400k taxable Bitcoin** — 6.2 divides $600,000 by $80,000 to get
  ~7.5 years, and the demo seed is $600k. Advanced 7.4 used $400k. One of them
  is wrong and the arithmetic says which.
  **Second sweep, 2026-08-08:** the first pass fixed the *scripts* and left two
  layers behind. `MASTER-COURSE.md` still had the couple's balances **swapped**
  ($400k taxable / $600k traditional, the mirror of the script) and drew the
  wrong conclusion from them: *"$400,000 ÷ $80,000 ≈ 5 years"* and *"they spent
  five years sitting in their cheapest brackets"*, against the script's 7.5
  years and seven. `lesson-text/advanced/07-4` carried $400k in its setup line
  and a $300k step-up gain instead of $500k. Both corrected; `modules/` and
  `modules/advanced/` regenerated. This is the standing hazard firing in the
  direction nobody watches — **a script edit never reaches the master**, and the
  student read layer is generated from the master, so the wrong number was the
  one students would have read.
- **The 4.4 balance sheet** summing to $385,000 against the canonical $295,000.
- **The 99% confidence line** — "a plan that only survives at 99% confidence is
  built on optimism" is backwards. A high modelled success rate means the
  opposite.
- **"Plan → Goals"** — a click path to a page that does not exist.
- **The $128,000 0% capital-gains ceiling** — law-set, changes by statute, and
  the standing evergreen policy already covers it. This is the category the
  policy was written for; F1 was not.


---

## NEW — raised by the college-funding position

### F8 ✅ RESOLVED · Does the funding-stack logic generalise beyond college?

**Austin approved the generalisation, 2026-08-08.** The six questions now lead
2.3 as the general rule for any dated cost, explicitly covering cars, weddings,
a house, home repairs, business investment and family support. Original entry
below.


Austin's position is explicitly about **college**: uncertain school, aid
package, student contribution, and whether the child attends at all.

A roof, a car, or a down payment has none of that uncertainty. There is no aid,
no student contribution, no chance the roof declines to need replacing. So 2.3
currently keeps the simple treatment for those and applies the stack only to
college.

**Flagged, not decided:** is there a third category — a cost that is real but
whose *amount* is uncertain, like a wedding you have promised to contribute to,
or eldercare? Those look more like college than like a roof.

### F9 ✅ RESOLVED · 2.3 was 14.5 minutes doing two jobs — split 2026-08-08

**Austin's ruling: option 2, with one amendment.** 2.3 is now the required
future-cost lesson (six questions, ~10 min) and **2.4 is an optional college
lesson** (~7 min) that stays visibly inside Module 2 rather than moving to the
Advanced Library — college is conditional, not advanced. The Module 2 walkthrough
renumbered 2.4 → 2.5. Both are recorded in **one continuous sitting** with the
edit cutting immediately before *"College is a funding stack, not a bill you
prepay"*, so the split costs no extra production. Original entry below.

**Original entry — F9 · 2.3 is now 14.5 minutes, the longest lesson in Module 2 (was 12.5)**

The college position roughly doubled the lesson. It replaced a framing that was
wrong, so the content is not padding — but 2.3 now does two distinct jobs:
fixed dated costs, and college as a funding stack.

**Two options, Austin's call:**

1. **Leave it at 12.5 min.** One lesson, one place to look for "future costs".
2. **Split it.** 2.3 fixed dated costs (~5 min), 2.4 college as a funding stack
   (~7 min). Matches the "one thing at a time" principle and lets someone with
   no kids skip the second cleanly.

Option 2 adds a lesson after the v1.0 freeze. That is legitimate under the
freeze rule — the old framing was inaccurate — but it is a structural change
and belongs to Austin, not to me.

### F10 · Every college figure is statute-set or annual

Published prices, net prices, the 529 student-loan and Roth-rollover limits,
federal loan ceilings, parent PLUS (changed 1 July 2026), FAFSA asset
treatment. **None is spoken in the video.** All live in `lesson-text/02-4`
(the optional college lesson) with verify-before-acting warnings.

Austin's own instruction already scoped these to text; this note records that
the implementation matches, and that the lesson text is now a
**verify-annually** surface like the tax figures.

### F11 · App modelling request, not started

Austin specified what the college life event should capture: the commitment
(children, dollars/percentage/benchmark, years, tuition-only or total, per
child or pooled), expected offsets (grants, student work, employer benefit,
existing 529), funding sources (monthly 529 contribution, cash flow while
enrolled, planned Bitcoin/taxable, student loan ceiling, parent loan ceiling,
remaining gap), and timing/risk (first enrollment year, year-one amount, amount
protected, amount still Bitcoin-dependent, result under a 70–80% drawdown,
alternative-school scenario).

Output should read **"Your $80,000 parental commitment is 73% funded"**, never
"College is 38% funded".

**Not started.** This is app work and it touches the projection.

---

# Source-material review, 2026-08-08

Raised by the four-bucket sort (`SOURCE-MATERIAL-POLICY.md`). Every item below
is **bucket 2: a planning judgment.** None is applied. None becomes a course
edit without Austin's word.

### F12 → SUPERSEDED BY F22 (RESOLVED) · Is the next-dollar process a strict waterfall or a flexible comparison?

**2026-08-08: this is now F22 below, and it is no longer only a question.** The
client calls answered the "is the strict reading right" half — it is not — and
the lesson is marked HOLD FOR REDICTATION. What remains for Austin is the actual
order and wording, which is exactly what F22 asks for. Also note the lesson
number in the original entry is stale: the next-dollar lesson is **4.3**, not
2.2. Original entry below.

**Original entry — F12 · Is the next-dollar process a strict waterfall or a flexible comparison?**

Lesson 2.2 currently reads as a waterfall. The broader philosophy is more
contextual: tax benefit, investment menu, Bitcoin exposure, liquidity, employer
match, and early-retirement access all bear on the same dollar.

**Live now: neither.** Answered via F22 on 2026-08-11 — a default ordering with
named overrides, not a strict waterfall. See F22 for the settled structure.

**Original open question, kept for the record:** strict order, or a comparison
with a default ordering?

### F13 · Should a Level 2 custody design deliberately let one heir act alone?

**Partially addressed 2026-08-08.** The *universal* dual-control rule is gone:
the course now teaches redundancy and dual control as separate tests, and says a
single-signature household where the owner can spend alone is sound. That
removes the contradiction. It does not answer the narrower question below, which
is about what design to actively recommend at Level 2. Still open.


Bears directly on F6, which is still open.

### F14 · Should the executor and the heir usually be different people?

The course currently implies separation without stating it as a rule.

### F15 · Is a professional executor ever the default answer?

Source material leans yes for complex estates. The course does not say.

### F16 ✅ RESOLVED · What conditions trigger a trust conversation?

**Austin approved the trigger-driven gate, 2026-08-08.** Nine triggers and four
levels are now live in the estate walkthrough, replacing the net-worth reading.
"Trust not currently indicated," written down with a date, is a completed
decision. Original entry below.


The uploaded four-level estate gate uses triggers (blended family, minor
children, multiple heirs, business ownership, Bitcoin concentration, probate or
privacy concerns, incapacity, multi-state, advanced custody) rather than net
worth alone. Better than a net-worth rule, but the specific trigger list is a
planning judgment. Would improve the existing trust gate in 8.x without adding
a lesson. A valid outcome stays *"basic estate plan is sufficient; trust not
currently indicated"* — a completed decision.

### F17 ✅ LARGELY RESOLVED · When is a future cost funded by cash, Bitcoin sales, borrowing, or a blend?

**Answered by the same approval.** Questions 3, 4 and 5 of the six make the mix
an explicit decision per cost rather than a default. What remains genuinely open
is only whether Austin wants a *recommended* default blend for any category, and
he has not asked for one. Original entry below.


The college position answers this for college. It does not answer it for cars,
weddings, a house purchase, home repairs, business investment, or family
support. See F8 — same question, still open.

### F18 · Does disability insurance belong in every working-age household's core checklist?

The stated principle is to identify the risk and route the relevant person, not
to build an insurance curriculum. Whether disability is the exception is
Austin's call.

### F19 · Secure one year or two years of college support before enrollment?

The dictated position says *"year one, perhaps year two."* The word "perhaps"
is doing real work and the course has to pick something a student can act on.

---

## Not bucket 2 — a contradiction worth flagging (category B)

### The coded-location proposal fails the same test 8.2 was fixed to pass

The proposal to replace exact locations on the family-facing custody map with
coded references (*"Seed backup: Location A"*, with retrieval instructions held
by the executor) is a real theft-risk improvement: a stolen family document
stops being a treasure map.

**But it introduces a second single point of failure at the document layer.**
Run it through the two tests the corrected 8.2 teaches:

1. *Can one person act alone?* No — good, that is the point.
2. *Can one lost copy or unavailable person permanently prevent recovery?*
   **Yes.** If the executor packet holding the decode is lost, destroyed, or
   held by someone unreachable, the family has a map with no legend. The
   Bitcoin is recoverable in principle and unreachable in practice.

This is precisely the dual-control-mistaken-for-redundancy defect that made the
old 8.2 dangerous, reappearing one layer up in the paperwork. Any coded-location
scheme must therefore specify **where the second copy of the legend lives** and
who can reach it, or it is 2-of-2 wearing a filing-cabinet costume.

Not a reason to reject the proposal. A condition on accepting it.


---

# Repo-parity and client-call pass, 2026-08-08

Raised while repairing the layer disagreements found in the repo audit. F20 and
F21 are new. F22 supersedes F12. F23 records a structural consequence.

### F20 · The 7-to-10-year funding lane is unstated

The rebuilt 2.3 dictation names four lanes: **0–1 · 1–3 · 3–7 · 10+**. Nothing is
said about **7 to 10 years**.

The retired table closed that gap by running "no Bitcoin" all the way through ten
years. The new dictation narrows the explicit no-Bitcoin statement to 3–7, and
picks up again at 10+. So a cost seven and a half years out currently has no
stated lane.

**Not resolved here.** Extending "no Bitcoin" to ten would be re-imposing the
table Austin replaced; starting the Bitcoin schedule at seven would be loosening
a rule he kept. Both are planning judgments. The master, the lesson text and the
`2-3_cost-lanes` visual all render the lanes exactly as spoken, with the gap
visible.

**Adjacent evidence, added 2026-08-11 — not an answer.** Austin's Week 3 deck
sets the *bucket* timeframes at Reserve 0–3, **Bridge 4–10**, Legacy 10+, and
puts Bridge at moderate volatility, *"a balanced mix that can flex with your
needs."* That points at 7-to-10 behaving like the current 3–7 row. It is
**recorded, not applied**, for two reasons: buckets and dated-cost lanes are
different axes — one is what a pool of money is for, the other is where a
specific bill's money waits — and extending "no Bitcoin" to ten is precisely
the retired table F20 says not to re-impose by inference. The deck makes the
question cheaper to answer; it does not answer it.

**One sentence at the mic settles it.** Austin: what happens between 7 and 10?

### F21 · An inserted section in 1.3 — "Where the numbers come from"

**Not from any prior dictation.** ~45 seconds, written 2026-08-08 to close the
single most repeated stall in the 24 client calls: *where did this number come
from · which page controls it · what changes when I edit this · which account
funds this expense*. Peyton needed the life-event → future-spending → funding
account chain explained more than once.

**Why a section and not a lesson.** The repo already identified provenance as the
highest-leverage improvement and left it as a backlog item. A new teaching lesson
was explicitly out of scope, so this is the smallest thing that closes it: one
reusable visual (`visuals/1-3b_number-flow.md`), introduced in 1.3, recalled in
every module walkthrough as **CALCULATED FROM · EDIT SOURCE · THIS AFFECTS**.
The pattern is the one the retirement-paycheck visual already proves.

**Austin: keep it, rewrite it, or cut it at the mic.** The graphic carries the
idea either way, and the walkthrough sheets already point at it. Nothing else
depends on the spoken words.

### F22 · The next-dollar lesson (4.3) — RESOLVED 2026-08-11, script still owed

**Status: the order is settled. The spoken script is not.**

**What was wrong.** 4.3 taught: *"every rung above has to be full, or maxed,
before you move down to the next one. Money flows down the ladder, not
sideways."* It then funded HSA, Roth and traditional accounts before taxable
Bitcoin. That did not match how Austin actually advised clients. With Peyton,
choosing between taxable savings and a Solo 401(k), the comparison ran across
the current deduction, early-retirement access, how underfunded the taxable side
was, income uncertainty, and the option of splitting the contribution. When
future income felt uncertain, access to taxable money mattered enough that the
deduction was not automatically decisive.

**What settled it.** Austin supplied his own **Week 3 · Accounts + Allocation**
deck (slide 8, "Build the contribution waterfall"), plus the override in his own
words: *"Typical order, adjust per situation: employer match → HSA → Roth IRA →
back to 401k → taxable/self-custody BTC. This is adjustable per situation based
on allocation targets. If you don't have any taxable and want to retire early
the path changes."*

**The settled structure, now taught in master / lesson-text / visual:**

- **Three gates first**, each completing by deliberate skip: reserve if still
  short · employer match if available · extra debt if the debt strategy says
  that debt wins.
- **Then a fork on time horizon**, not a ladder. **Legacy (10+ yrs)** is the
  default: HSA → Roth IRA → back to the 401(k) → taxable or self-custody Bitcoin
  above the limits. **Bridge (4–10 yrs)**: taxable or another flexible account.
- **Named override:** little or nothing in taxable + wants to retire early →
  Bridge moves up. Also: the account cannot hold the wanted Bitcoin exposure,
  and income uncertainty making access outweigh the deduction.
- **Deliberate splitting** when one dollar answers two legitimate needs.
- **Then place it inside the account** per the allocation targets.

**Still owed by Austin — one thing.** `scripts/04-3_...md` is his spoken prose
and has **not** been rewritten. The strict text is preserved verbatim under a
header block that spells out the settled structure to dictate against. **Layer
parity between the master and that script is expected to disagree until he
dictates**, and `CLAIM-REGISTRY.md` scopes the MUST rules to the layers that
have actually been updated so the gate reports that honestly instead of going
permanently red.

**Also still his, deliberately not applied:** the proposed title *"Route your
next dollar: the default order and when it changes"*. The current title, "which
account gets funded first", no longer quite describes a lesson whose answer
forks by time horizon — but a retitle is his call and it moves the script's
filename slug, so it waits for the dictation.

**Applied downstream on resolution:** the Module 4 checkpoint lines (now
"saved default route / what overrides it / one destination or a deliberate
split"), the 4.3 visual brief (now three gates and a fork, with a `Never render`
line forbidding the six-rung form), and a **math fix**: the master's routing
table labelled $1,000/mo as "captures full 50%-up-to-6% match", but 6% of the
$150,000 salary is $750/mo. The script had it right all along, splitting $750 at
the match and $250 past it. The master now matches the script.

### F23 · Where the Module 2 walkthrough hand-off now sits

A consequence of the F9 split, recorded so it is a decision rather than a
side effect.

The say-once rule puts the walkthrough hand-off on the **last teach lesson of a
module that has a capture**. After the split that is 2.4 — the *optional* college
lesson — so a student who correctly skips college would never hear it.

**What was done:** the hand-off sits on **2.3**, the last *required* teach lesson,
and is worded to work on both paths: *"Then watch the module walkthrough, where we
build cash flow and reserve in Orange Plan. If college applies to you, take the
college lesson first."* `tools/build-dictation-order.py` now derives the hand-off
from the last required lesson, so an optional lesson never captures it.

**The alternative Austin may prefer:** put college last (2.5) and leave the
walkthrough at 2.4, which makes the hand-off literal again at the cost of putting
an optional lesson after the module's capture. Cheap to switch before filming.
### F24 · The Rule of 55 — the app models it, the course never mentions it

**Raised 2026-08-11 by the app review. This is a curriculum judgment, so it is
Austin's, and nothing has been added.** `SOURCE-MATERIAL-POLICY.md` and the
original directive both say not to add broad new curriculum, so this is a flag,
not an edit.

**What the app does now.** `src/lib/ruleOf55Ledger.js`,
`isRuleOf55EligibleEmployerPlanAccountType`, and
`getRuleOf55PenaltyFreeWithdrawal` model penalty-free access to workplace-plan
dollars from age 55 for a user who separates from service in or after the year
they turn 55. The projection consumes it. A student who retires at 55 will watch
the app hand them their 401(k) without a penalty.

**What the course says.** 59½ is taught as the unlock age, in four places that
are spoken or shown on camera:

| Where | What is said |
|---|---|
| `scripts/04-4` | *"a 10% penalty if you pull money before 59 and a half"* |
| `scripts/04-4` | *"access before 59 and a half depends on whether the dollars are contributions, conversions, or earnings"* |
| `scripts/04-5` | Bridge is badged *"before 59½"* |
| `scripts/06-1` | 🎬 GRAPHIC timeline marker: *"59½ (retirement accounts unlock)"* |

The 4.4 line about contributions / conversions / earnings is **correct and
matches** the app's new Roth ordering work (`rothDistributionOrdering.js`,
`taxFreeLedger.js`). The gap is specifically the workplace-plan exception at 55.

**Why it matters more than it looks.** 4.3's settled override (F22) is
*"little or nothing in taxable, and you want to retire early → the Bridge path
moves up"*, and its reasoning is that retirement accounts *"lock the money behind
an age you are not planning to wait for."* For a 55-to-59 retiree with a
workplace plan, the app now says that lock is softer than the course does. The
override is still right — the Rule of 55 needs separation from service, applies
only to the plan you left, and does nothing for IRAs — but the flat framing is
the part that is now incomplete against his own product.

**Austin decides, and it is a small decision:**

1. Leave 59½ as the core-course simplification and put the Rule of 55 in the
   Advanced Library, or
2. Add one qualifying sentence to 6.1's timeline graphic and 4.4, or
3. Say nothing and accept the app being more precise than the video.

Any of the three is defensible. What is not defensible is not knowing, which is
why this is flagged before dictation rather than after filming.

**Related fix already applied (category A, not a judgment):** the 4.4 wrapper
table said *"RMDs start at 73"* flat. SECURE 2.0 sets it at 73 or 75 by birth
year and the app computes it per user via `getRMDStartAge(birthYear)`. The
master now says *"in your seventies — the exact age depends on your birth year,
and the app computes yours."* The script already said *"start in your
seventies"* and was correct; only the doc layer carried the number.

### F25 · A7.1 is numbered first and sequenced last

**Raised 2026-08-11 by the structural audit. Not a filming blocker — the
Advanced Library is not in the dictation order.**

Advanced Module 7 runs **A7.2 → A7.3 → A7.4 → A7.1**. The sequence is
consistent everywhere — the master, the generated module file, and the core
course's "Related advanced lessons" pointer all list A7.1 fourth — so this is
not drift between layers. It is one lesson whose number disagrees with its
position in all of them at once.

The position looks deliberate: A7.2, A7.3 and A7.4 are Level 1–2 operational
lessons, and A7.1 is the Level 3/4 escalation, gated on failing an access test
from the estate module. Read as a capstone it belongs last. Read as a number it
belongs first.

**Austin decides:** renumber it **A7.5** so number and position agree, or leave
it and accept that students see A7.1 fourth. Renumbering cascades — the master
heading, the script and lesson-text filenames, the generated module file, and
the core pointer — so it is a clean batch job, but it is a job, and
`check-crossrefs.py` will catch anything missed.

Every other advanced module is in numeric order, and Advanced Module 2 is
deliberately empty (*"Reference material only. No filmed lessons."*), which the
audit confirmed is intentional rather than a gap.
