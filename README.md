# Orange Plan Academy

This repository contains the Orange Plan Academy core course, optional Advanced Library, spoken scripts, student lesson text, demo-account controls, slide source material, and production tooling.

## Start here

Use these files in this order:

1. **`CURRENT-COURSE.md`** — current core outline, production stage, and source-of-truth rules
2. **`DEMO-HOUSEHOLD.md`** — the only working source for continuous-demo inputs
3. **`AUSTIN-DEMO-DECISIONS.md`** — one approve/change sheet for the remaining fictional planning judgments
4. **`PRE-DICTATION-QA.md`** — what is complete, what is held, and what must happen before Austin's final voice pass
5. **`DEMO-CHECKPOINT-RUN-SHEET.md`** — how the working household is entered and how app-calculated outputs are captured once
6. **`scripts/`** and **`lesson-text/`** — the current 28 spoken drafts and their matching written lessons
7. **`COURSE-APP-CONTRACT.md`** and **`BUILD-YOUR-PLAN-CROSSWALK.md`** — the course/app agreement and preview-dependent walkthrough routing
8. **`professional-review/`** — the only current CPA, custody, estate-attorney, and insurance review packets
9. **`research/SLIDE-CORRECTION-MAP.md`** — page-by-page treatment of the existing live-teaching decks

Read **`AUSTIN-AUTHORITY.md`** before changing Austin's planning recommendations.

## Current stage

The pre-dictation structural pass is substantially complete:

- 28 core teach scripts exist across Modules 0–9.
- Every script has a matching student lesson.
- Every lesson owns one main planning decision.
- Core and Advanced are separated by a visible condition.
- One continuous fictional household reconciles cash flow, assets, debts, reserve, contribution routing, future costs, basis, custody, and estate starting state.
- The professional review packets and slide correction map are ready.
- The permanent course audit checks both spoken scripts and matching lesson text.
- The audit passes with 28 scripts, 23,559 spoken words, no missing lesson text, and no current critical or warning findings.
- Script headers total about **214 production minutes, or 3 hours 34 minutes**, before walkthroughs. The raw word-count estimate is about 152 minutes; the difference allows for teaching pace, visuals, and examples.

Austin's final voice and judgment review has **not** started. Before it does, the remaining work is intentionally narrow:

- approve or change the recommended values in `AUSTIN-DEMO-DECISIONS.md`,
- enter the approved fictional household in the current app and capture calculated checkpoint outputs,
- receive and apply external professional review for the high-stakes modules,
- and verify the deployed Build Your Plan preview before recording exact walkthrough clicks.

## Course structure

0. Start Here
1. Build Your Baseline and Read the Plan
2. Cash Flow and Reserve
3. Debt Strategy
4. Allocation and the Next Dollar
5. Tax Strategy
6. Retirement Income
7. Custody and Recovery
8. Estate and Family Handoff
9. Maintain, Test, and Read the Plan

The Advanced Library is optional. It is linked from the core planning area that makes it relevant and does not count toward core completion unless the learner's own plan triggers it.

## Repository map

| Path | Purpose |
|---|---|
| `scripts/` | Current spoken core drafts plus historical walkthrough sheets that are explicitly not current until reverified |
| `lesson-text/` | Current student-facing reference lessons |
| `professional-review/` | Canonical high-stakes review packets |
| `research/` | Client-call evidence, confusion registry, runtime ownership, demo reconciliation, and slide audit |
| `visuals/` | Visual briefs and graphic source material |
| `tools/course_audit.py` | Permanent structural, provenance, runtime, script/text parity, and legacy-language audit |
| `modules/` | Previous generated module splits; migration input only |
| `archive/` | Historical course generations and retired sources |

`MASTER-COURSE.md`, `MASTER-ADVANCED.md`, `ALL-SCRIPTS.md`, generated modules, Circle output, and old production checklists are **not current production authority**. They are synchronized only after a module is Austin-approved.

## Script provenance

| Label | Meaning |
|---|---|
| `AUSTIN DICTATION` | Direct transcription of Austin's recording |
| `AUSTIN DICTATION + VOICE-MATCHED COMPLETION` | Austin's spoken material preserved and incomplete sections filled from verified voice evidence; Austin review pending |
| `VOICE-MATCHED DRAFT` | Rewritten from Austin dictation, client calls, slides, and current app behavior; Austin review pending |
| `AUSTIN APPROVED` | Austin completed the final read and cleared the wording for filming |
| `ARCHIVED` | Historical only |

The old `SPOKEN-PROSE VERSION (calibrated)` label is retired because it did not distinguish Austin's words from authored prose.

## The walkthrough rule

Concept videos teach the durable financial-planning decision. Walkthroughs are replaceable, versioned, and track the accepted Build Your Plan implementation after the deployed preview is verified.

Every walkthrough must:

1. Recall the decision.
2. Enter through the relevant Build Your Plan area.
3. Continue the same demo household checkpoint.
4. Name whether the learner is viewing a saved input, preview, or Scenario.
5. Implement only the decision the lesson taught.
6. Explain the important result using **What it means · Calculated from · Edit source · This affects**.
7. Return to Build Your Plan.
8. Distinguish the app completion rule from the human planning finish line.

## Current encrypted-export limitation

Orange Plan can create a passphrase-protected encrypted export for secure storage and portability. **In-app plan restore is currently unavailable.** Course materials must not describe that export as a restore the learner can use today. The current plan and source records remain necessary until the app exposes and verifies a restore process again.

## Before filming

A lesson is film-ready only after:

- demo inputs and app-calculated outputs reconcile,
- app terminology and behavior match the accepted build,
- required professional review is applied,
- Austin approves the planning judgment and spoken wording,
- the matching lesson text agrees,
- the visual supports the same concept,
- and the walkthrough is verified against the deployed preview.
