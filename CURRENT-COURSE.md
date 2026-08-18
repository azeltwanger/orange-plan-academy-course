# Orange Plan Academy — current course

**This is the entry point for the course repair branch.**

The Academy is being reconciled to the current Orange Plan app, the Build Your Plan workflow, Austin's client-teaching voice, and one continuous demo household.

## What the course is

The core course takes someone from having disconnected financial information to a usable Bitcoin financial plan.

Each planning area follows the same educational pattern:

1. Explain the financial-planning concept.
2. Show the trade-offs and judgment call.
3. Work through the decision on the continuous demo household.
4. Use the walkthrough to complete the matching work in Orange Plan.
5. Explain where the important numbers came from.
6. End with a checkable planning decision.

**Build Your Plan is the navigation spine for the walkthroughs. It is not required to be the exact syllabus for every concept lesson.**

## Current source-of-truth order

During the repair, use this order:

1. `CURRENT-COURSE.md` — approved course outline and migration status
2. `COURSE-APP-CONTRACT.md` — pedagogy, app behavior, demo, and number-provenance rules
3. `BUILD-YOUR-PLAN-CROSSWALK.md` — how walkthroughs track the app's build flow
4. `scripts/` files marked `AUSTIN DICTATION`, `VOICE-MATCHED DRAFT`, or `AUSTIN APPROVED`
5. `lesson-text/` — student-facing written version aligned to the reviewed script
6. `research/CLIENT-CALL-VOICE-EVIDENCE.md` and `research/CLIENT-CONFUSION-REGISTRY.md`
7. Slides — visual and teaching source material, updated when they teach a retired concept or wrong fact

`MASTER-COURSE.md`, `MASTER-ADVANCED.md`, generated module files, Circle output, and aggregate script files still contain the previous course in places. **Do not film or publish from those layers until the affected module has been synchronized and marked current below.** They are migration inputs, not proof that a lesson is ready.

## Core course outline

### Module 0 — Start Here

**Outcome:** The learner understands what will be built, how the course and app work together, and the security rule for AI.

- How to use the course
- How Orange Plan AI works and what never goes into it

### Module 1 — Build Your Baseline and Read the Plan

**Outcome:** A verified first plan with deliberate assumptions, a chosen confidence target, and a retirement result the learner can explain.

- Gather and verify the source information
- Baseline versus life event versus Scenario
- Broad Plan assumptions
- Holding-specific return or income overrides when applicable
- Planned retirement age and baseline spending
- Confidence target, confidence result, and earliest target-qualified date
- Walkthrough: complete the relevant baseline work through Build Your Plan and read the first plan

### Module 2 — Cash Flow and Reserve

**Outcome:** Normal spending, bare-bones spending, a reliable surplus, and a reserve policy with a practical funding plan.

- Find the true surplus
- Separate normal, bare-bones, and irregular spending
- Size the working reserve
- Fund known future costs by time horizon
- Optional college funding
- Walkthrough: complete Cash Flow and Reserve through Build Your Plan

### Module 3 — Debt Strategy

**Outcome:** Every debt has a deliberate treatment and the household has a debt ceiling it can hold through a full Bitcoin cycle.

- Read debt cost and cash-flow pressure
- Decide what each debt is doing in the plan
- Decide what receives extra principal
- Set the household's debt ceiling
- Walkthrough: complete Debt through Build Your Plan

Bitcoin-backed borrowing remains optional/advanced unless the learner already has or is actively considering a loan.

### Module 4 — Allocation and the Next Dollar

**Outcome:** A target allocation, time-horizon jobs, account placement, and a repeatable route for new money.

- Set a Bitcoin allocation that can survive the full drawdown
- Separate target allocation, account holdings, and today's action
- Assign Reserve, Bridge, and Legacy jobs
- Build the next-dollar route
- Place holdings inside the appropriate accounts
- Walkthrough: complete Allocation and Contributions through Build Your Plan

### Module 5 — Tax Strategy

**Outcome:** Cost-basis readiness, an understanding of the three tax buckets, and one current tax action or a deliberate pass.

- Reconstruct and protect cost-basis records
- Understand taxable, tax-deferred, and Roth money
- Read the household's tax roadmap
- Identify the current planning window
- Walkthrough: complete Tax through Build Your Plan

Detailed conversions, harvesting, state relocation, and edge cases remain gated advanced material.

### Module 6 — Retirement Income

**Outcome:** A starting retirement paycheck, reliable income floor, portfolio gap, withdrawal order, and annual adjustment policy.

- Confirm retirement spending
- Build the reliable income floor
- Read the portfolio gap and bridge years
- Choose the starting spending target
- Set withdrawal order and first-year funding
- Understand Bitcoin sold versus retained and optional borrowing
- Set annual guardrails and reserve-refill rules
- Walkthrough: complete Retirement Income through Build Your Plan

### Module 7 — Custody and Recovery

**Outcome:** A custody setup the household can operate and recover, with no single point of failure and no secrets stored in Orange Plan.

- Choose the appropriate custody level
- Set up and prove recovery
- Find and fix single points of failure
- Harden accounts
- Create the no-secrets custody map
- Walkthrough: complete the custody work in Protect

### Module 8 — Estate and Family Handoff

**Outcome:** A real family starting point: executor, legal documents, beneficiaries, custody handoff, heir letter, and delivery process.

- Choose and confirm the executor
- Review beneficiaries and core legal documents
- Design the family access process
- Create the heir letter and executor packet
- Set up delivery and review procedures
- Review the coverage gap
- Walkthrough: complete the estate work in Protect

Trusts, estate-tax planning, and complex custody remain gated advanced material.

### Module 9 — Maintain, Test, and Read the Plan

**Outcome:** A repeatable review cadence, useful Scenarios, a readable report, and an encrypted backup.

- Monthly review
- Annual review
- Update triggers
- Build and compare Scenarios
- Read the finished report
- Save the report and encrypted backup
- Walkthrough: complete the final Build Your Plan work

## Advanced Library

Advanced material is optional and linked from the core area that makes it relevant. It does not count toward core progress unless the learner's own plan makes the issue necessary.

Primary sections:

- Modeling and assumptions
- Holding-level return and income assumptions
- Bitcoin-backed loans and leverage
- Allocation and behavior
- Tax optimization
- Retirement income and pre-Medicare healthcare
- Sell-versus-borrow comparisons
- Advanced custody
- Trusts and complex estate planning

Each lesson begins with a plan-visible gate:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

## Number-provenance standard

Every walkthrough explains important outputs using:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

This is required for surplus, reserve target, debt ratios, allocation, projected tax, confidence, earliest retirement date, retirement spending, first-year funding, Bitcoin sold or retained, and Protect readiness.

## Script provenance

| Label | Meaning |
|---|---|
| `AUSTIN DICTATION` | Directly transcribed Austin recording |
| `VOICE-MATCHED DRAFT` | Rewritten from Austin's dictation, client calls, slides, and current app; Austin review pending |
| `AUSTIN APPROVED` | Austin reviewed the final wording and cleared it for filming |
| `WALKTHROUGH — APP VERIFICATION PENDING` | Structure is drafted; exact recording waits for a verified current preview |
| `ARCHIVED` | Historical only; not a current production source |

The old `SPOKEN-PROSE VERSION (calibrated)` label is retired. It does not prove Austin said or approved the wording.

## Migration status

| Area | Structure | App match | Voice pass | Walkthrough |
|---|---|---|---|---|
| Module 0 | Review pending | Review pending | Dictated portions exist | No core walkthrough |
| **Module 1** | **Approved** | **In progress** | **1.1–1.3 first pass complete** | **Hold exact clicks for Build Your Plan preview** |
| Module 2 | Approved outline | Audit started | Pending after Module 1 review | Rebuild required |
| Module 3 | Approved outline | Audit started | Pending | Rebuild required |
| Module 4 | Approved outline | Page still changing | Pending | Record last among core |
| Module 5 | Approved outline | Audit pending | Pending | Rebuild required |
| Module 6 | Approved outline | Major app change identified | Pending | Full rebuild required |
| Module 7 | Approved outline | Audit pending | Pending | Rebuild required |
| Module 8 | Approved outline | Technical corrections identified | Pending | Rebuild required |
| Module 9 | Approved outline | Audit pending | Pending | Rebuild required |
| Advanced | Core split approved | Audit pending | Last | Gated reference demos |

## Current Module 1 review files

- `scripts/01-1_what-to-gather-before-you-build-the-plan.md`
- `scripts/01-2_set-your-growth-and-inflation-assumption.md`
- `scripts/01-3_read-your-retirement-date-and-confidence.md`
- Matching files under `lesson-text/`
- `research/CLIENT-CALL-VOICE-EVIDENCE.md`
- `research/CLIENT-CONFUSION-REGISTRY.md`

## Repo-cleanup sequence

1. Finish and approve Module 1 as the production template.
2. Create one versioned demo-household source and checkpoint exports.
3. Rebuild walkthrough sheets around the Build Your Plan crosswalk.
4. Synchronize the approved module into the master, Circle, checkpoints, and production files.
5. Move superseded generations, stale walkthroughs, and prior structural documents into `archive/`.
6. Repeat module by module.
7. After all modules migrate, make this file and the cleaned directory structure the permanent repo entry point.
