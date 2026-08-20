# Orange Plan Academy — pre-dictation QA

**Purpose:** finish every structural, numeric, factual, and production change that could make Austin repeat his voice work.

Austin's final read should be a targeted voice-and-judgment pass, not another course rebuild.

## Gate status

| Gate | Status | Evidence / remaining work |
|---|---|---|
| Current outline and one-decision lesson ownership | **PASS** | `CURRENT-COURSE.md`; 28 current Core scripts |
| Continuous demo input reconciliation | **PASS — APPROVED** | `AUSTIN-DEMO-DECISIONS.md`, `DEMO-HOUSEHOLD.md`, and `demo/demo-v1-inputs.json` |
| App-calculated demo outputs | **HOLD** | Enter the approved household once and capture receipts in `DEMO-CHECKPOINT-RUN-SHEET.md` |
| Duplication and runtime | **PASS** | Core has been trimmed so adjacent lessons own distinct decisions; automated course audit remains authoritative |
| Core-versus-Advanced boundary | **PASS** | Advanced conditions are visible and non-blocking |
| App-concept accuracy | **PASS WITH CHECKPOINT HOLD** | Unified confidence, Income controls, source ownership, save/preview distinction, current encrypted-export limitation, and preview-dependent Build Your Plan status are corrected |
| Script / lesson-text parity | **PASS** | 28 matching pairs; automated audit scans both layers |
| External professional responses | **HOLD** | Canonical CPA, custody, estate-attorney, and insurance packets are in `professional-review/` |
| Slide correction map | **PASS — REBUILDS LATER** | `research/SLIDE-CORRECTION-MAP.md` identifies keep/edit/replace/move/remove by page |
| Capstone | **PASS** | `MY-ORANGE-PLAN-CAPSTONE.md` turns the finished plan into one usable summary |
| Permanent audits | **PASS — RERUN AFTER EACH CHANGE** | Course, fixture, receipt, provenance, voice, and pre-dictation control checks exist under `tools/` and `.github/workflows/` |
| Build Your Plan preview | **HOLD FOR WALKTHROUGHS** | Exact clicks wait for the deployed preview Austin has used end to end |
| Austin final voice review | **NOT STARTED** | Begins only after the applicable holds below are resolved |

## Approved demo decisions

The following are now locked for `demo-v1-inputs`:

- Alex, 45; Jordan, 43; two children, ages 10 and 12; Colorado; married filing jointly
- Built-in Power Law Bitcoin view
- Current standard app defaults for stocks, bonds, cash, and real estate
- 3% baseline inflation and a separate 4% inflation stress Scenario
- Retirement at 55, $100,000 retirement living spending in today's dollars, planning age 95, and 80% Plan confidence target
- $20,000 of part-time income during the first 3 retirement years
- Alex Social Security of $30,000 at age 67
- Jordan Social Security of $22,000 when Jordan reaches 67 two years later
- 50% Bitcoin target with a 40–60% review band
- Do not intentionally exceed 25% DTI; do not add debt at DTA of 40% or higher
- $625/month to Alex's family HSA and $625/month to Jordan's Roth IRA
- HSA assigned to the qualified Healthcare Bridge
- Optional $80,000 total-family college commitment
- Borrowing excluded from the saved Core baseline

The starting retirement paycheck is deliberately not locked. Orange Plan must first calculate the reference spending amounts and measure the current $100,000 Plan amount.

## Demo arithmetic already reconciled

The course-owned source inputs reconcile:

- $190,000 income − $40,000 teaching tax estimate − $80,000 living spending − $22,000 debt payments = $48,000 annual / $4,000 monthly surplus
- $5,000 bare-bones spending × 6 months = $30,000 working reserve
- $280,000 mortgage + $18,000 auto loan = $298,000 debt
- $1,833 required monthly debt ÷ $15,833 gross monthly income = about 11.6% DTI
- $298,000 debt ÷ $745,000 illustrative gross assets = about 40.0% DTA
- $175,000 Bitcoin ÷ $295,000 investable assets = about 59.3%
- A 75% decline in $175,000 of Bitcoin removes $131,250 before other assets move
- $750 + $500 + $625 + $625 + $1,500 = the $4,000 monthly route
- Vehicle goal: $35,000 − $10,000 proceeds − $5,000 purchase-year cash flow = $20,000 to accumulate
- College: $25,000 existing + $20,000 parent cash flow + $10,000 student/aid/defined borrowing + $25,000 remaining source = $80,000 total-family commitment
- Cost-basis quantities: 1.25 + 0.40 + 0.10 = 1.75 BTC

App-calculated confidence, tax, retirement funding, Bitcoin sales, estate, and Scenario results remain blank until the checkpoint run.

## Remaining holds before Austin reads once

### 1. App-calculated demo outputs

Enter the approved household in the accepted app build and capture:

- confidence at planned age,
- earliest date reaching the target,
- current and target allocation output,
- tax roadmap,
- first-year retirement need and source split,
- Bitcoin sold and retained,
- starting-spending reference amounts and current Plan confidence,
- reserve status,
- ending assets and estate,
- Scenario deltas,
- and Protect readiness status.

Use `DEMO-CHECKPOINT-RUN-SHEET.md`. Do not invent an output in a script, lesson, or slide.

### 2. Starting retirement-paycheck decision

After `demo-v1-income` is captured, compare:

- Conservative,
- Balanced,
- Aggressive,
- and the current $100,000 Plan amount.

Use the Balanced 80% reference unless the household deliberately chooses the current Plan amount after seeing its measured confidence and practical monthly difference.

### 3. External professional responses

Before Austin gives final approval to the affected claims:

- Module 5 and tax-sensitive Module 6 sections require the Bitcoin-aware CPA response.
- Module 7 and the technical side of 8.2 require the custody-professional response.
- Modules 8.1–8.3 require the estate-attorney response.
- Module 8.4 requires the licensed-insurance response.

A reviewer marks each claim OK, qualify, change, current fact, professional only, or remove. Apply the minimum factual correction before Austin reads that section.

### 4. Build Your Plan preview

This does not block evergreen concept approval. It blocks exact walkthrough scripts and screen recording.

The current app contract and crosswalk define the decisions, provisional areas, app/human finish lines, and required metadata. Exact step IDs, labels, controls, routes, save behavior, completion rules, and screenshots are filled only after Austin completes the deployed preview.

## Readiness by module

| Module | Structural pass | Demo / app output | Professional response | Ready for Austin |
|---|---|---|---|---|
| 0 · Start Here | PASS | N/A | N/A | **After final course state is locked** |
| 1 · Baseline | PASS | CHECKPOINT HOLD | N/A | **No** |
| 2 · Cash Flow | PASS | CHECKPOINT HOLD where displayed outputs are used | N/A | **No** |
| 3 · Debt | PASS | CHECKPOINT HOLD | N/A | **No** |
| 4 · Allocation | PASS | CHECKPOINT HOLD | CPA qualification only where tax location is stated | **No** |
| 5 · Tax | PASS | CHECKPOINT HOLD | CPA HOLD | **No** |
| 6 · Retirement Income | PASS | CHECKPOINT + STARTING-PAYCHECK HOLD | CPA HOLD on tax mechanics | **No** |
| 7 · Custody | PASS | REAL-WORLD TEST LANGUAGE COMPLETE | CUSTODY HOLD | **No** |
| 8 · Estate / Insurance | PASS | POLICY / REAL-WORLD HOLD | ATTORNEY + INSURANCE HOLD | **No** |
| 9 · Maintain / Test / Read | PASS | CHECKPOINT HOLD | N/A | **No** |

## Current app-state notes

### Confidence

Plan confidence defaults to 80%, accepts 50–99%, and uses 1,000 test runs to evaluate the planned age and find the earliest target-qualified date. The Core course does not teach a second deterministic retirement date.

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
