# Usability test — Modules 0 through 3

The next revision should be driven by evidence, not by another read-through.
This is the instrument. Run it before changing any more curriculum.

**What is being tested:** whether a smart person who is not a financial planner
can get from nothing to a funded reserve and a debt policy, using the course and
the app, without you in the room.

**What is not being tested:** whether they liked it. Satisfaction is a lagging,
polite signal. Completion and hesitation are the leading ones.

---

## Recruiting

**Three people. Not more.** Three finds roughly 80% of the problems that matter
and costs a week. Five costs three weeks and finds the same list.

Each one must be:

- Not a financial planner, accountant, or advisor
- A Bitcoin holder, at any size, because the emotional content is real for them
  and fake for everyone else
- Willing to enter **their own real numbers**. Test data hides every problem
  worth finding, because nobody hesitates over a number that isn't theirs

Deliberately vary these across the three:

| Vary | Why |
|---|---|
| Self-employed vs W-2 | The tax-reserve subtraction only bites one of them |
| Has debt vs debt-free | Module 3 completes differently, and "not applicable is complete" is untested |
| Has a spouse vs solo | The household handoff and the executor/heir split change shape |

## Setup

- Screen share, recorded, with their permission.
- **You say nothing.** This is the hard part and the whole point. Every time you
  explain something, you delete the finding.
- The only thing you may say is: *"What are you thinking right now?"*
- If they ask you a question, answer with *"What would you do if I weren't
  here?"* — and write the question down. Every one of those is a course defect,
  an app defect, or an FAQ entry.
- Stop a task at 15 minutes whether or not it is finished. An unfinished task is
  data, not a failure.

## The tasks

Give them the task, not the lesson. Let them find the lesson.

| # | Task, in their words | Passes when |
|---|---|---|
| 1 | "Get set up and tell me what the course is going to cover." | They can name roughly what is coming and in what order |
| 2 | "Get your real numbers into Orange Plan." | Baseline entered; totals match what they'd say out loud |
| 3 | "Set your growth and inflation assumptions, and tell me why you chose them." | They can defend each number without hedging |
| 4 | "Read your retirement date and your confidence number, and tell me what they mean together." | Both read as a pair; they say the first read is provisional |
| 5 | "Find your surplus." | A real surplus number, with the tax reserve taken out first if self-employed |
| 6 | "Set your reserve target." | Target set in **months**, and they can say what it's for |
| 7 | "Give every debt a job, and tell me your ceiling." | Every debt has a job with a reason; a ceiling said out loud |
| 8 | "Is Module 3 finished?" | They open the checklist and answer from it, not from memory |

## What to record

Four codes. Timestamp each one. Nothing else.

| Code | Means | Why it matters |
|---|---|---|
| **P** | Paused more than ~5 seconds before acting | They did not know what to do next |
| **R** | Replayed or re-read a passage | The explanation did not land the first time |
| **M** | Mis-entered — wrong field, wrong units, wrong layer | Usually a labelling defect, not a comprehension one |
| **F** | Failed to complete the task in 15 minutes | The most important code. Everything else is texture |

Plus one free-text column: **the question they asked you.**

```
time   code   task   what happened                          their words
0:04:12  P      2     stopped at monthly vs annual income     "is this gross?"
0:07:30  M      5     entered SS estimate as annual           —
0:11:02  R      6     replayed the months-of-spending part    —
```

## The four hypotheses this test is built to falsify

Written in advance so the results cannot be rationalised afterwards.

1. **Provenance.** People will ask "where did this number come from?" at least
   once each. *Falsified if nobody asks.* If confirmed, it is app work, not
   course work.
2. **Layers.** People will put a hypothetical into the baseline, or hesitate
   about whether something is a life event. *Falsified if the new Module 1
   framework prevents it.*
3. **Tax reserve.** The self-employed tester will get a wrong reserve unless the
   subtraction lands. *Falsified if they separate tax money unprompted.*
4. **Completion.** People will say a module is finished when the videos are
   watched, not when the checklist is true. *Falsified if they open the
   checklist on task 8 without being told to.*

## Reading the results

- **Two or three testers hit the same P or M in the same place** → fix it. That
  is a defect.
- **One tester hits something once** → note it, do not fix it. That is a person.
- **Any F** → that module does not ship until it is understood. A task nobody
  can finish is worth more than any runtime target.
- **Sort every question they asked** into the table in `FAQ-AND-AI-BACKLOG.md`.
  Most will belong in the app or the FAQ. Resist the reflex to answer a
  repeated question with a new video.

## After

Fix only what two or more testers hit. Re-run tasks 5 through 8 with one new
person to confirm the fix. Then move on to Modules 4 onward.

---

## Pre-test pass, already run

`tools/cold-read-audit.py` was run over Modules 0–3 first, so testers are not
spending attention on defects a script could find. It checks, in course order,
for terms used before they are defined, actions with no click path, and figures
with no stated source.

**Fixed as a result:**

- **1.3** introduced "withdrawal order" four modules before it is taught. It was
  in a paragraph added during the previous pass, which is how new jargon gets in.
- **2.3** used "bridge years" in Module 2, defined in Module 6. Now says what it
  means locally — a low-income year is a cheap year to sell in — and hands the
  name to the retirement module.
- **0.2**, the second lesson in the whole course, name-dropped cost basis,
  harvesting, Roth conversions, seed phrases and passphrases before any of them
  existed. Rewritten to describe them rather than name them, except in the
  one-hard-rule sentence, where naming them literally is the point.

**Known and accepted:**

- **0.1** names most planning topics without defining them. That is the roadmap,
  and the client calls specifically praised it. Naming what is coming is not the
  same defect as using a term as though it were understood.
- **2.2** uses "sequence risk" with only a partial gloss. It is Austin's
  dictation and the VOICE-GUIDE calibration master, so it is flagged rather than
  edited — **watch whether any tester pauses there.** If two do, it is worth a
  short pickup recording.
