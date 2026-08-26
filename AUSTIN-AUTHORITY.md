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

---

## Operating amendment — 2026-08-08

Austin: *"I can correct things that I disagree with during dictation. Just need
to get structure right for the course so it provides structure and clarity based
on what people and users actually need and want."*

**What this changes.** Open planning judgments no longer block production. Austin
catches and corrects them at the microphone, where he is reading the words
anyway. Waiting for a written ruling on every C-item stalls the course for
decisions he can make faster out loud.

**What this does NOT change.** Everything in this file still stands:

- Never delete or replace one of Austin's stated positions, numbers, or rules of
  thumb and substitute your own. F1 and F5 are why this rule exists.
- Never silently resolve a contradiction by picking the side you prefer.
- Still flag A / B / C. Still write the flag.

**The difference is only what a flag does.** It used to mean *stop and wait*. It
now means *write it in `AUTHORITY-FLAGS.md`, note it in the script where he will
see it while reading, and keep moving.* A flag is a marker for the dictation
booth, not a gate.

**Where a flag still blocks:** when getting it wrong would require a re-shoot
rather than a re-read. Structural choices — how many lessons, what order, which
module something lives in, what gets its own video — cannot be fixed at the
microphone. Those still need Austin before filming.

**The standing priority, in his words:** structure and clarity, driven by what
users actually need, evidenced by the 24 client calls. Not more content, and not
more analysis.

---

## Structural-source amendment — 2026-08-26

Austin: *"we drifted so far from my slide decks and the slide decks are the flow we should generally use."*

The slide decks now control the **module flow and teaching sequence** for the required core course. This supersedes any earlier instruction that reduced them to loose concept or visual source material.

The complete source hierarchy and module-by-module interpretation live in `SLIDE-DECK-AUTHORITY.md`.

In practical terms:

1. Dictation controls the spoken recommendation and Austin's voice.
2. Slide decks control the decision flow and why one teaching step follows another.
3. Current production app behavior controls click paths, available fields, calculations, and walkthrough mechanics.
4. Research verifies facts and limitations but does not invent course philosophy.
5. Generated scripts are drafts with no authority of their own.

Deck flow may be adapted when the app changed or when a self-paced lesson needs a clearer boundary. It may not be replaced by generic copywriting structures, repetitive `YOUR DECISION / PUT IT IN / DONE WHEN` filler, or page-by-page app navigation.

A teach lesson explains the concept and decision. The walkthrough performs the clicks, inputs, saving, and verification. When a walkthrough follows, the teach lesson ends with a natural handoff rather than duplicating the implementation steps.