# `scripts/` — what is here and how to film it

One file per teach lesson or screen recording, sorted by lesson number.

| File | What it is | How it is filmed |
|---|---|---|
| `03-1_...` | Teach lesson | Teleprompter, camera on Austin |
| `03-2_WALKTHROUGH_...` | App walkthrough run sheet | Screen recording, narrated naturally while following the sheet |
| `A3-1_...` | Advanced Library lesson | Teleprompter or reference text, depending on demand |

## Provenance is not the same as quality

A script header must say where the words came from.

| Header state | Meaning |
|---|---|
| **AUSTIN DICTATION** | Austin recorded these words and they were transcribed. Highest authority |
| **VOICE-REVIEWED SCRIPT** | Authored script that Austin has read and approved for filming |
| **AUTHORED SCRIPT — VOICE PASS N (Austin review pending)** | Structurally and factually edited, but not yet approved as Austin's spoken version |
| **GENERATED** | Derived from a master file and safe to regenerate |
| **WALKTHROUGH RUN SHEET** | Production instructions, not teleprompter prose |

The legacy label **SPOKEN-PROSE VERSION (calibrated)** does **not** mean the words came from Austin. Treat every remaining file with that header as requiring a voice pass.

Do not solve that by deleting the scripts. Scripts are fast to edit and useful for filming. Solve it by making the provenance honest, fixing the structure and app facts, running the voice pass, and then having Austin approve the spoken version.

## Teach-lesson structure

Each core teach lesson does five things in this order:

1. Explain the financial-planning concept.
2. Simplify it into a decision the student can make.
3. Work the decision through the shared demo household.
4. Name where the decision lives in Orange Plan.
5. End with a checkable finish line.

The standard close remains:

- `YOUR DECISION`
- `PUT IT IN ORANGE PLAN`
- `YOU ARE DONE WHEN`

Use `VOICE-GUIDE.md` for cadence and language. Lesson 2.2 is the strongest current calibration sample because it began as Austin's dictation.

## Walkthrough run-sheet structure

Walkthroughs are not product tours. They demonstrate the decisions taught in the module on the same demo household used throughout the course.

Every walkthrough contains:

1. **DEMO STATE** — exact starting numbers and prior decisions.
2. **DECISIONS FROM THE LESSONS** — what is being implemented.
3. **DO** — the current app path.
4. **SEE** — the result to point at.
5. **WHERE THIS NUMBER COMES FROM** — for each important output:
   - **WHAT IT MEANS**
   - **CALCULATED FROM**
   - **EDIT SOURCE**
   - **THIS AFFECTS**
6. **WHAT CHANGED** — before and after in the demo household.
7. **DONE WHEN** — both the app state and the human planning decision.

The question from client calls that the course must answer repeatedly is:

> **Where did this number come from?**

Do not answer that with a database field or a vague statement that “the app calculated it.” Name the upstream inputs, where the student edits them, and what the output moves downstream.

## Current-app rule

A walkthrough is recorded only after its path has been clicked through on the current app or an Austin-approved preview.

- Direct plan inputs may autosave or save when the field is committed.
- Strategy surfaces may preview until **Save** or **Apply to plan**.
- Scenarios remain separate questions.

Never turn one page's save behavior into a rule for the entire app.

Exact Build Your Plan walkthroughs stay on hold until the feature exists in a working preview and Austin has completed it end to end.
