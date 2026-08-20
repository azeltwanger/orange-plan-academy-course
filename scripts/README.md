# `scripts/` — current spoken sources and walkthrough rules

This directory contains the individual spoken lesson files and historical walkthrough run sheets.

## Current production authority

The exact current Core script set is listed in `../CURRENT-COURSE.md` and linked from `../AUSTIN-REVIEW-INDEX.md`.

- The 28 current Core files are spoken drafts.
- Matching student references live under `../lesson-text/`.
- Historical walkthrough sheets remain non-current until reverified against the deployed Build Your Plan flow.
- Advanced scripts remain separate and have not received the full current voice/app/professional pass.

Do not film from a compiled master, generated module, Circle copy, old walkthrough, or an unlisted script merely because it is present in the directory.

## Current provenance labels

Provenance says where the wording came from. It does not by itself prove factual quality or filming approval.

| Header state | Meaning |
|---|---|
| **AUSTIN DICTATION** | Direct transcription of Austin's recorded words |
| **AUSTIN DICTATION + VOICE-MATCHED COMPLETION** | Austin's recorded wording is preserved; missing sections were completed from verified voice evidence; Austin review pending |
| **VOICE-MATCHED DRAFT** | Rebuilt from Austin dictation, client calls, live-teaching slides, current app behavior, and approved demo; Austin review pending |
| **AUSTIN APPROVED** | Austin completed the final spoken read and cleared the wording for filming |
| **WALKTHROUGH RUN SHEET** | Screen-production instructions, not teleprompter prose |
| **GENERATED** | Derived output; never edit as the spoken source |
| **ARCHIVED** | Historical only |

The legacy label **SPOKEN-PROSE VERSION (calibrated)** is not a current production status and does not prove Austin said or approved the wording.

## Teach-lesson structure

Each Core lesson:

1. Names the planning problem.
2. Teaches only the concept needed for the decision.
3. Shows the trade-off and Austin's planning judgment.
4. Continues the same fictional household.
5. Explains the important app number when the lesson owns one.
6. Ends with one decision and one checkable finish line.

The standard close is:

- `YOUR DECISION`
- `PUT IT IN ORANGE PLAN`
- `YOU ARE DONE WHEN`

Lesson 2.2 remains the strongest direct dictation calibration sample. Client-call evidence and recurring confusion are documented under `../research/`.

## App-owned demo values

Current spoken examples use:

- `../DEMO-HOUSEHOLD.md`
- `../demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md`
- `../demo/VISUAL-DATA-RECEIPT-3105664.md`

The app owns confidence, earliest date, displayed tax/surplus, Allocation scope, payoff, total draw, sources, Bitcoin units, Scenario deltas, and other projection outputs.

A script must not silently replace an app value with a cleaner example. A separate mechanism example must say **illustrative — not the demo household**.

## Number-provenance standard

When a lesson owns an important output, teach:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

Current high-risk examples include:

- one household retirement date,
- confidence and earliest target-qualified date,
- decision capacity versus post-debt surplus,
- app Allocation denominator,
- total need / recurring income / total draw,
- and Bitcoin sale dollars / projected price / units.

Do not answer “where did this number come from?” with a database field or “the app calculated it.” Name the upstream facts and decision.

## Walkthrough run-sheet structure

Walkthroughs are versioned implementations, not product tours.

Every final walkthrough records:

1. accepted app commit and deployed route,
2. Build Your Plan step ID and label,
3. starting checkpoint,
4. decision from the concept lesson,
5. Saved / Previewing / Scenario / read-only state,
6. current controls and save/apply behavior,
7. important output provenance,
8. before/after reconciliation,
9. ending checkpoint,
10. app completion rule,
11. human planning finish line,
12. screenshot or recording evidence.

Use `../WALKTHROUGH-RUN-SHEET-TEMPLATE.md` and `../BUILD-YOUR-PLAN-CROSSWALK.md`.

## Current walkthrough hold

Do not record an exact click path until:

- Austin has used the deployed Build Your Plan flow end to end,
- the stable step metadata is recorded,
- the synthetic UI receipt is accepted,
- and the walkthrough's app commit is saved.

A mockup, spec, source branch, or old route is not sufficient.

## Save-state rule

Orange Plan has multiple states:

- direct saved input,
- strategy preview,
- Scenario,
- read-only calculated output.

Never turn one page's save behavior into a rule for the entire app. Every walkthrough names the state on the page being shown.

## Filming rule

A script changes to `AUSTIN APPROVED` only after:

- applicable UI values and terminology are verified,
- applicable professional corrections are applied,
- matching lesson text agrees,
- Austin reads it once, replaces only wording or judgment he would naturally express differently,
- and one clean final read is complete.
