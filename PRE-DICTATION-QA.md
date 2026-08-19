# Orange Plan Academy — pre-dictation QA

**Purpose:** finish every structural, numeric, factual, and production change that could make Austin repeat his voice work.

Austin's final read should be a targeted voice-and-judgment pass, not another course rebuild.

## Gate status

| Gate | Status | Evidence / remaining work |
|---|---|---|
| Current outline and one-decision lesson ownership | **PASS** | `CURRENT-COURSE.md`; 28 current core scripts |
| Continuous demo input reconciliation | **PASS WITH ONE APPROVAL SHEET** | Arithmetic reconciles in `DEMO-HOUSEHOLD.md`; approve/change `AUSTIN-DEMO-DECISIONS.md` once |
| App-calculated demo outputs | **HOLD** | Enter the approved household once and capture receipts in `DEMO-CHECKPOINT-RUN-SHEET.md` |
| Duplication and runtime | **PASS** | 23,559 spoken words; 214 header minutes; audit has 0 critical findings and 0 warnings |
| Core-versus-Advanced boundary | **PASS** | Advanced conditions are visible and non-blocking |
| App-concept accuracy | **PASS WITH CHECKPOINT HOLD** | Unified confidence, Income controls, source ownership, save/preview distinction, current encrypted-export limitation, and preview-dependent Build Your Plan status are corrected |
| Script / lesson-text parity | **PASS** | 28 matching pairs; automated audit scans both layers |
| Professional review packets | **PASS — RESPONSES HOLD** | Canonical packets in `professional-review/` |
| Slide correction map | **PASS — REBUILDS LATER** | `research/SLIDE-CORRECTION-MAP.md` identifies keep/edit/replace/move/remove by page |
| Capstone | **PASS** | `MY-ORANGE-PLAN-CAPSTONE.md` turns the finished plan into one usable summary |
| Permanent audit | **PASS** | `.github/workflows/course-audit.yml` runs `tools/course_audit.py` on scripts, lesson text, and control-file changes |
| Build Your Plan walkthroughs | **HOLD** | Current `main` does not confirm a dedicated shipped flow; exact clicks wait for the deployed preview Austin has used end to end |
| Austin final voice review | **NOT STARTED** | Begins only after the applicable holds below are resolved |

## What has already been done

### Structure and progression

- The 10-module spine is locked.
- Every lesson has one primary decision.
- Difficult concepts have one owner; later lessons use short callbacks.
- Debt remains before Allocation because the treatment is decided before the dollars are routed.
- Tax remains before Retirement Income because the withdrawal lesson applies the tax pools and windows.
- Custody and Estate stay separate because operational access is not legal authority.
- Optional college and all Advanced topics are visibly non-blocking.

### Runtime and duplication

The current scripts contain **23,559 spoken words**.

- Raw estimate at 155 words per minute: about **152 minutes**
- Production header total, including pauses and visuals: about **214 minutes / 3 hours 34 minutes**
- Current audit result: **28 scripts · 0 critical · 0 warnings · 0 missing lesson texts**

No further global shortening pass is planned before Austin reads. A section is cut later only when the spoken read proves it repeats without adding understanding.

### Demo arithmetic

The canonical working inputs reconcile:

- $190,000 income − $40,000 teaching tax estimate − $80,000 living spending − $22,000 debt payments = $48,000 annual / $4,000 monthly surplus
- $5,000 bare-bones spending × 6 months = $30,000 working reserve
- $280,000 mortgage + $18,000 auto loan = $298,000 debt
- $1,833 required monthly debt ÷ $15,833 gross monthly income = about 11.6% DTI
- $298,000 debt ÷ $745,000 illustrative gross assets = about 40.0% DTA
- $175,000 Bitcoin ÷ $295,000 investable assets = about 59.3%
- A 75% decline in $175,000 of Bitcoin removes $131,250 before other assets move
- $750 + $500 + $1,250 + $1,500 = the $4,000 monthly route
- Vehicle goal: $35,000 − $10,000 proceeds − $5,000 purchase-year cash flow = $20,000 to accumulate
- College: $25,000 existing + $20,000 parent cash flow + $10,000 student/aid/defined borrowing + $25,000 remaining source = $80,000 total family commitment
- Cost-basis quantities: 1.25 + 0.40 + 0.10 = 1.75 BTC

App-calculated confidence, tax, retirement funding, Bitcoin sales, estate, and Scenario results remain blank until the checkpoint run.

## Remaining holds before Austin reads once

### 1. Approve the demo decision sheet

`AUSTIN-DEMO-DECISIONS.md` contains the recommended choices and the reason for each one:

1. Fictional state and household names
2. Broad app assumptions and inflation
3. Retirement age, spending, planning age, and Plan target
4. Part-time income amount and dates
5. Staggered Social Security timeline for the two spouses
6. Bitcoin target and review band
7. Household DTI/DTA ceiling
8. Exact HSA/Roth split inside the $1,250 route
9. HSA Bridge or Legacy job
10. Starting-spending choice after the app calculates the available bands
11. Whether college remains in the continuous household
12. Saved core borrowing rule

Austin can approve the page or list only the row numbers to change. No dictation is needed.

After approval, remove the remaining `proposed` markers from `DEMO-HOUSEHOLD.md` and update any affected factual example once.

### 2. Capture demo checkpoint outputs

Enter the approved household in the accepted app build and capture:

- confidence at planned age,
- earliest date reaching the target,
- current and target allocation output,
- tax roadmap,
- first-year retirement need and source split,
- Bitcoin sold and retained,
- starting-spending bands,
- reserve status,
- ending assets and estate,
- Scenario deltas,
- and Protect readiness status.

Use `DEMO-CHECKPOINT-RUN-SHEET.md`. Do not invent an output in a script or slide.

### 3. Apply external professional responses

Before Austin gives final approval to the affected claims:

- Module 5 and tax-sensitive Module 6 sections require the Bitcoin-aware CPA response.
- Module 7 and the technical side of 8.2 require the custody-professional response.
- Modules 8.1–8.3 require the estate-attorney response.
- Module 8.4 requires the licensed-insurance response.

A reviewer marks each claim accurate, qualify, replace, state/fact-pattern dependent, or professional-only. Apply the minimum factual correction before Austin reads that section.

### 4. Verify the deployed Build Your Plan preview

This does not block approval of evergreen concept lessons. It blocks only exact walkthrough scripts and screen recording.

The current app contract and crosswalk define the decisions, provisional areas, app/human finish lines, and required metadata. Exact step IDs, labels, controls, routes, save behavior, completion rules, and screenshots are filled only after Austin completes the deployed preview.

## Readiness by module

| Module | Structural pass | Demo / app output | Professional response | Ready for Austin |
|---|---|---|---|---|
| 0 · Start Here | PASS | N/A | N/A | **After final course state is locked** |
| 1 · Baseline | PASS | CHECKPOINT HOLD | N/A | **No** |
| 2 · Cash Flow | PASS | CHECKPOINT HOLD for displayed app outputs | N/A | **No** |
| 3 · Debt | PASS | CHECKPOINT HOLD | N/A | **No** |
| 4 · Allocation | PASS | DECISION + CHECKPOINT HOLD | CPA qualification only where tax location is stated | **No** |
| 5 · Tax | PASS | CHECKPOINT HOLD | CPA HOLD | **No** |
| 6 · Retirement Income | PASS | DECISION + CHECKPOINT HOLD | CPA HOLD on tax mechanics | **No** |
| 7 · Custody | PASS | REAL-WORLD TEST LANGUAGE COMPLETE | CUSTODY HOLD | **No** |
| 8 · Estate / Insurance | PASS | POLICY / REAL-WORLD HOLD | ATTORNEY + INSURANCE HOLD | **No** |
| 9 · Maintain / Test / Read | PASS | CHECKPOINT HOLD | N/A | **No** |

## Current app-state notes

### Confidence

Plan confidence defaults to 80%, accepts 50–99%, and uses 1,000 test runs to evaluate the planned age and find the earliest target-qualified date. The core course does not teach a second deterministic retirement date.

### Income

The starting-spending choices and annual guardrail policy are separate from Plan confidence and from the saved withdrawal strategy. The current product preset is 60 / 80 / 95 with a 10% maximum correction.

### Encrypted export

Orange Plan creates a passphrase-protected encrypted export. In-app plan restore is temporarily unavailable. The course describes the file as a secure storage and portability copy, not a restore the learner can use today.

### Build Your Plan

A dedicated shipped Build Your Plan page is not confirmed on current `main`. Exact walkthrough implementation remains preview-dependent rather than being inferred from specifications or old content.

## Definition of ready for Austin

A lesson moves to Austin only when:

- no known structural change remains,
- all demo values appearing in speech are approved inputs or accepted checkpoint outputs,
- app terminology and state are current,
- required professional corrections are applied,
- script and lesson text agree,
- and contradictory slides are already identified.

At that point, Austin reads once, dictates only the sections he would naturally explain differently, and marks the final wording `AUSTIN APPROVED`.
