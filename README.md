# Orange Plan Academy

This repository contains the Orange Plan Academy core course, optional advanced library, scripts, student text, walkthroughs, slides, and production tooling.

## Start here

1. **`CURRENT-COURSE.md`** — the approved current outline and module-by-module migration status
2. **`COURSE-APP-CONTRACT.md`** — how the Academy teaches, how it matches the app, and how numbers are explained
3. **`BUILD-YOUR-PLAN-CROSSWALK.md`** — how walkthroughs track the Build Your Plan flow without forcing the concept course to mirror the product one-for-one
4. **`research/CLIENT-CALL-VOICE-EVIDENCE.md`** — Austin's real teaching patterns from six client calls
5. **`research/CLIENT-CONFUSION-REGISTRY.md`** — recurring questions the course and walkthroughs must answer

Read **`AUSTIN-AUTHORITY.md`** before changing Austin's planning recommendations.

## Current repair status

The course is being reconciled to:

- the current Orange Plan app,
- the Build Your Plan workflow,
- one continuous demo household,
- clear explanations of where every important number came from,
- and Austin's actual teaching voice.

**Module 1 is the active vertical slice.** Its three teaching scripts have received the first structural, app-accuracy, and voice-matching pass. Exact walkthrough clicks remain on hold until the Build Your Plan preview is usable and Austin has completed it end to end.

Do not assume that a file is current because it is generated or because an old checklist called it final. Check `CURRENT-COURSE.md` first.

## Course structure

The required core remains:

0. Start Here
1. Baseline and Confidence
2. Cash Flow and Reserve
3. Debt Strategy
4. Allocation and the Next Dollar
5. Tax Strategy
6. Retirement Income
7. Custody and Recovery
8. Estate and Family Handoff
9. Maintain, Test, and Read the Plan

The Advanced Library is optional and gated by conditions visible in the learner's own plan.

## Repository map

| Path | Purpose |
|---|---|
| `scripts/` | Spoken teaching scripts and walkthrough run sheets |
| `lesson-text/` | Student-facing written lessons |
| `research/` | Client-call evidence, confusion registry, and course research |
| `visuals/` | Visual briefs and graphic source material |
| `modules/` | Previous generated module splits; migrate module by module |
| `tools/` | Course checks and generation tooling |
| `MASTER-COURSE.md` | Previous core master; still contains stale sections during migration |
| `MASTER-ADVANCED.md` | Previous advanced master; audit and migration pending |
| `archive/` | Destination for retired course generations and stale walkthroughs |

`MASTER-COURSE.md`, `MASTER-ADVANCED.md`, `ALL-SCRIPTS.md`, generated module files, Circle output, and older production checklists are **not proof that a lesson is current during the repair**. The approved script and student-text files are synchronized back into those layers only after Austin reviews the module.

## Script labels

| Label | Meaning |
|---|---|
| `AUSTIN DICTATION` | Austin's directly transcribed words |
| `VOICE-MATCHED DRAFT` | Rewritten from dictation, client calls, slides, and current app; Austin review pending |
| `AUSTIN APPROVED` | Austin reviewed and cleared the wording for filming |
| `WALKTHROUGH — APP VERIFICATION PENDING` | Durable structure exists; exact app recording is not yet verified |
| `ARCHIVED` | Historical only |

The old `SPOKEN-PROSE VERSION (calibrated)` label is retired because it did not distinguish Austin's actual words from authored prose.

## The walkthrough rule

Concept lessons follow the clearest educational order. Walkthroughs track Build Your Plan.

Every walkthrough must:

1. Recall the planning decision.
2. Enter through the relevant Build Your Plan step.
3. Continue the same demo household.
4. Implement the decision in the current app.
5. Explain the important number using **WHAT IT MEANS · CALCULATED FROM · EDIT SOURCE · THIS AFFECTS**.
6. Return to Build Your Plan.
7. State both the app completion rule and the human planning finish line.

## Before filming

A lesson is not ready merely because prose exists.

Confirm:

- the concept and recommendation are approved,
- app terminology and behavior match current `main`,
- the demo household state is versioned,
- every important number has a provenance explanation,
- the student-text layer matches the spoken lesson,
- the walkthrough was clicked through on the current preview,
- and the script is labeled `AUSTIN APPROVED`.

## Migration sequence

1. Approve Module 1 as the template.
2. Create the versioned demo household and checkpoint exports.
3. Rebuild the Module 1 walkthrough against Build Your Plan.
4. Synchronize Module 1 into the master, checkpoints, Circle, and production tooling.
5. Archive the superseded versions.
6. Repeat for the remaining modules.

The repo cleanup will be completed module by module so no current production source is accidentally deleted before its replacement is approved.
