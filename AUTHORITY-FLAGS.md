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

**What Austin said** (8.2, his own words, first person):

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

### F2 · The Bridge rule — the exact example in the rule

**What the course said** (4.2, now 5.2):

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

### F3 · "Target ÷ months to go", and the growth guidance

**What Austin said.** Nothing. 3.3 worked the couple's example ($100,000 over
8 years ≈ $1,000/month) but never stated a general rule.

**What I wrote.** The rule *target ÷ months to go*, **plus** a recommendation
not to discount for expected growth, with my own reasoning: *inside about five
years you should not be taking that risk anyway, and over a longer horizon
arriving early is a better failure than arriving short.*

The division is arithmetic. **The no-growth-discount guidance is a planning
judgment and it is mine, not Austin's.** It is also deliberately conservative,
which is precisely the direction the rule warns about — it makes people save
more than a growth-adjusted number would.

**Austin decides:** keep the plain division, or discount for expected growth in
the lane, or say both and let the student choose.

### F4 · Annual review timing: October/November → November

**What Austin said:** "Put this review in the fall, October or November."
**What I did:** standardised on **November** everywhere, because the walkthrough
scheduled January on camera and I wanted one answer.

The January/November clash was a real contradiction (B). Narrowing his range
from two months to one was a judgment (C). Small, but it is the same move.

**Austin decides:** November, or restore "October or November" and fix only the
walkthrough.

### F5 · Bitcoin-backed loan LTV: 10–20% → 10–15%

**What Austin said.** Two different things. The master: *"Austin's default is 10
to 20% LTV."* The script: *"My own default is 10 to 15% LTV."*

**What I did.** Standardised on 10–15% and re-derived the couple's borrowing
capacity from it, without flagging that his two layers disagreed.

This is the highest-stakes number in the Academy — it sets how much someone
borrows against their Bitcoin. **It should not have been resolved by an editor
picking the tighter figure.**

**Austin decides.** Which is your default?

### F6 · The Level 2 access design

**What Austin said.** Nothing. The old 9.2 only ever described a passphrase
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

- **9.2 "half of a 2-of-2"** — seed + passphrase requires both; the old lesson
  said losing one left the plan "half intact". Arithmetic, not opinion.
- **$600k vs $400k taxable Bitcoin** — 7.3 divides $600,000 by $80,000 to get
  ~7.5 years, and the demo seed is $600k. Advanced 7.4 used $400k. One of them
  is wrong and the arithmetic says which.
- **The 4.4 balance sheet** summing to $385,000 against the canonical $295,000.
- **The 99% confidence line** — "a plan that only survives at 99% confidence is
  built on optimism" is backwards. A high modelled success rate means the
  opposite.
- **"Plan → Goals"** — a click path to a page that does not exist.
- **The $128,000 0% capital-gains ceiling** — law-set, changes by statute, and
  the standing evergreen policy already covers it. This is the category the
  policy was written for; F1 was not.
