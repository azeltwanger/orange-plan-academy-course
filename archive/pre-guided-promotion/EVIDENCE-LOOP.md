# Evidence loop — how the first paying users decide v1.1

**Established 2026-08-08.** There are no recruited testers, so the first paying
customers are the evidence. This file exists so that evidence turns into
decisions instead of into opinions.

**The rule this replaces:** "someone said the course was confusing, let's rewrite
a lesson." One person's confusion is a support ticket. A *pattern* is a course
change. The table below is the difference, and it is the whole point of this
file.

---

## The revision rule

| Evidence | Response |
|---|---|
| One unusual question | Answer in support. Nothing changes |
| A repeated **terminology** question | Improve the tooltip or the FAQ |
| A repeated **"where did this number come from?"** | Fix app **provenance** — this is the number-flow frame failing, not the teaching |
| A repeated **failure to make a decision** | Revise the **core teaching**. The lesson is describing, not deciding |
| A repeated **navigation failure** | Fix the interface or the walkthrough |
| A **conditional** issue — real, but only for some households | Advanced lesson, or an optional lesson inside the module |
| A **product- or provider-specific** issue | Updateable reference material. Never evergreen narration |
| A **factual or safety** issue | Fix immediately. This one does not wait for a pattern |
| A **reproducible product, link, or course-path defect** — a broken link, a calculation bug, an impossible completion state, a button that does nothing, a course instruction pointing at a control that does not exist | **Fix immediately, once reproduced.** One customer is enough |

⚠ **Only the last two rows act on a single instance**, and both require the
issue to be *established* rather than reported — a factual error verified, a
defect reproduced. Everything above them needs repetition before it earns a
change. That asymmetry is deliberate: a broken button is broken the first time,
and a confusing sentence might just be one person having a bad evening.

**Reproduce before fixing.** "A customer said the reserve number looked wrong" is
not a defect report until someone has followed their steps and seen it. The
reproduction is what separates this row from the ones above it.

⚠ **The third row is the one to watch.** `HANDOFF.md` records provenance as the
highest-leverage improvement the calls identified. If "where did this number come
from?" keeps arriving *after* the number-flow frame ships, the frame is not
working and the fix belongs in the app, not in another lesson.

---

## What to track

Nine measures, chosen because each one maps to a specific failure and to a
specific row of the table above. Not a dashboard for its own sake.

| # | Measure | What a bad reading means |
|---|---|---|
| 1 | **Module checkpoint completion**, per module | The module is not producing its output. Compare against `MODULE-CHECKPOINTS.md` — the checkpoint is the definition of done |
| 2 | **Time to verified baseline** | Module 1 is too heavy, or onboarding is losing people before the plan exists |
| 3 | **Where customers stop** | The last lesson they finished is the one to read again |
| 4 | **Which advanced lessons get opened** | Gate conditions are wrong, in one of two directions — see below |
| 5 | **Which questions go to AI or support** | Sort each one through the revision rule. This is the primary input |
| 6 | **Which app fields are repeatedly mis-entered** | Almost always a walkthrough problem, not a teaching problem. Living spending is the known one |
| 7 | **Whether they complete the final report** | The plan of record never assembled. Everything upstream was practice |
| 8 | **Whether they run the household review** | The plan exists but only one person can operate it |
| 9 | **Whether they return for the first monthly update** | The single best predictor that the plan is real rather than a completed course |

**Measure 4 reads in both directions**, and both are actionable:

- An advanced lesson **nobody opens** may have a gate condition written so
  narrowly that people who need it do not recognise themselves.
- An advanced lesson **everybody opens** is probably core material sitting in the
  optional library, or a gate condition too loose to let anyone stop.

**Measure 9 is the one to defend.** A customer who never comes back for the first
monthly pass did not get a plan; they watched a course. `9.1` teaches the monthly
pass and the one-page operating rhythm — if measure 9 is weak, that lesson and
its checkpoint line are the first things to re-read, not the earlier modules.

---

## The acceptance test

The bar is not "did they finish the videos." A customer should be able to say all
seven of these in their own words, without looking anything up:

1. **These are our real numbers.**
2. **This is what could force us to sell Bitcoin.**
3. **This is where our next dollar goes, and why.**
4. **This is when work may become optional.**
5. **This is how retirement gets funded.**
6. **This is how our family accesses the plan.**
7. **This is what we update each month and each year.**

And the eighth, which is the provenance test: **they can point at any major
number in the app and say where it came from.**

Each statement traces to a module output in `MODULE-CHECKPOINTS.md`. If a
customer cannot say one of them, that module did not produce its output, and the
gap is in that module — not in whichever lesson they happened to be watching when
they got confused.

| Statement | Module that owes it |
|---|---|
| These are our real numbers | 1 — verified baseline |
| What could force us to sell Bitcoin | 2 — reserve policy |
| Where the next dollar goes, and why | 4 — next-dollar policy |
| When work may become optional | 1 and 6 — the date, then the paycheck |
| How retirement gets funded | 6 — paycheck, withdrawal order, guardrails |
| How our family accesses the plan | 7 and 8 — custody map, heir letter, handoff |
| What we update monthly and annually | 9 — the operating rhythm |
| Where any number came from | The number-flow frame, `visuals/1-3b_number-flow.md` |

---

## What this file is not

It is **not** a licence to change planning positions because customers found one
uncomfortable. `AUSTIN-AUTHORITY.md` still governs, and the rule is about
*authority*, not about what the evidence is worth:

> **Usage evidence does not authorise an editor to change a planning
> recommendation. Repeated problems are escalated to Austin as a planning-review
> flag.**

That is a narrower claim than "usage cannot show a recommendation was wrong,"
which was the earlier wording here and was too strong. Repeated behaviour
genuinely can show that a recommendation:

- is **systematically misapplied** — people follow it and do the wrong thing
- produces a result people **cannot maintain**
- **conflicts** with another part of the system
- needs a **narrower applicability condition** than it currently has
- **deserves Austin's reconsideration**

All five are real findings and all five get written up. None of them is an
editor's decision to act on.

The honest version of the distinction:

- *"Ten customers could not tell what the lesson wanted them to decide"* → a
  writing problem. An editor restructures the lesson to make the decision
  explicit, without touching the recommendation.
- *"Ten customers said the reserve target felt too high"* → **not permission to
  lower it, and not nothing either.** It goes to `AUTHORITY-FLAGS.md` as a
  planning-review flag with the evidence attached, and Austin decides. Ten people
  finding a target uncomfortable is exactly the kind of signal he should see.
