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

### F7 · Advanced gate conditions — surfaced for Austin approval

I wrote the condition that decides whether a student watches each advanced
lesson — including the Roth gate's *"all three must be true"*, the trust gate's
trigger list, and the healthcare gate's *"only if you stop work before 65."*

These are triage rules: they decide who gets told to skip what. Each is a
judgment call about applicability.

**Austin decides:** review `ADVANCED-GATE-APPROVAL.md`, which now puts every live gate on one page with the owning lesson. This remains an approval item rather than a silent editorial decision, but it no longer requires hunting through the master.

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

### F12 → SUPERSEDED BY F22 · Is the next-dollar process a strict waterfall or a flexible comparison?

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

**Live now: the waterfall reading.** This is the single highest-traffic decision
in the core course, so a change here is expensive after filming and cheap now.

**Austin decides:** strict order, or a comparison with a default ordering?

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

### F22 · The next-dollar lesson (4.3) — strict waterfall, HOLD FOR REDICTATION

**The problem, stated plainly.** 4.3 says: *"every rung above has to be full, or
maxed, before you move down to the next one. Money flows down the ladder, not
sideways."* It then funds HSA, Roth and traditional accounts before taxable
Bitcoin.

That does not match how Austin actually advised clients. With Peyton, choosing
between taxable savings and a Solo 401(k), the comparison ran across the current
deduction, early-retirement access, how underfunded the taxable side was, income
uncertainty, and the option of splitting the contribution. When future income
felt uncertain, access to taxable money mattered enough that the deduction was
not automatically decisive.

**The intended shape** — the whole of what an editor is permitted to write down:

- a stated **default order**
- **strong presumptions**: capture unusually valuable employer money · deal with
  debt the Debt module marked urgent · fix a reserve gap that creates forced-sale
  risk
- **named conditions** that override the default
- a **comparison zone** among HSA / Roth / traditional / taxable Bitcoin /
  taxable bridge assets, weighed on tax benefit today, whether the account can
  hold the wanted Bitcoin exposure, access before retirement age, which timeframe
  is actually underfunded, income stability
- **deliberate splitting** when one dollar answers two legitimate needs

**Austin supplies the order and the wording. Nothing has been rewritten toward
the new shape** — the strict text is preserved verbatim so he can dictate over
it. This is the highest-traffic decision in the core course, which is why it is
cheap to change now and expensive after filming.

**Two things deliberately left alone until he dictates**, because both are
downstream of an order that does not exist yet:

1. The proposed title *"Route your next dollar: the default order and when it
   changes"*, and the proposed completion line: *"You have a saved default route,
   you know which facts override it, and you know whether this month's answer is
   one destination or a deliberate split."*
2. The Module 4 checkpoint lines about rung 2 and the skipped rungs.

### F23 ✅ RESOLVED · Module 2 order stays 2.4 optional college, 2.5 walkthrough

Austin explicitly authorized the course-wide update without a major restructure. The existing order is now locked: lesson 2.4 is the optional college funding stack, lesson 2.5 is the walkthrough, and the hand-off stays on the last required teach lesson so a student who correctly skips college still reaches the walkthrough.

This is no longer a filming blocker.
