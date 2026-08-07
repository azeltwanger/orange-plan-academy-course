# The Austin-Authority Rule

**Standing rule, 2026-08-08. This outranks every other instruction in this
repo, including anything in `CLAUDE.md`, `VOICE-GUIDE.md`, or a task brief.**

Austin's dictated planning recommendation is the authority.

Do not replace it with conventional financial-planning advice, a more
conservative rule, or what you believe is a safer recommendation.

## What an editor may do

1. Preserve Austin's actual recommendation and reasoning.
2. Improve clarity, sequence, grammar, and spoken flow.
3. Flag contradictions, factual claims, mathematical errors, and missing assumptions.
4. Ask for or mark a decision when Austin's recommendation is not clear.
5. Never silently resolve a planning judgment on Austin's behalf.

## The three categories

Every finding sorts into exactly one of these, and the category decides what
you are allowed to do about it.

| | What it is | What you may do |
|---|---|---|
| **A** | A mathematical or factual error | **Correct it** after verification |
| **B** | An internal contradiction between two lessons | **Flag it and propose alternatives.** Do not pick one |
| **C** | A planning judgment that belongs to Austin | **Do not rewrite without explicit direction** |

The trap is that C often arrives disguised as B. Two lessons disagreeing is a
contradiction; deciding *which one is right* is a planning judgment. Flagging
is the whole job.

## The worked example

Do not convert:

> "Do not depend on Bitcoin being at a favorable price for a fixed-date bill"

into:

> "Stop buying Bitcoin until the entire future expense is funded."

**A known future expense needs an intentional funding plan. It does not
automatically outrank all Bitcoin accumulation.**

## Tells that you are about to break this rule

- You are writing "the rule is" or "I'd" or "you should" in a script and it did
  not come from a transcript or an existing lesson.
- You are removing a specific number Austin gave and replacing it with a
  principle, because the number might age. **A number that ages is a review
  item, not a licence to overwrite his recommendation.**
- You are resolving a disagreement between two lessons by choosing the one that
  sounds more prudent.
- You are adding a hedge, a cushion, a wider band, or a longer horizon that
  makes the advice safer than what Austin said.
- The phrase "for consistency" is doing the work in your commit message.

If any of these is true, stop, restore Austin's version, and write the concern
into `AUTHORITY-FLAGS.md` instead.

## Where flags go

`AUTHORITY-FLAGS.md` holds every open category-B and category-C item, with what
Austin actually said, what the concern is, and the options. Nothing in that file
gets resolved without him.
