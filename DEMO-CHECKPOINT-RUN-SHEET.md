# Orange Plan Academy — demo checkpoint run sheet

**Purpose:** verify the reconciled synthetic household on the deployed Orange Plan pages and turn the current engine candidate into eight final UI receipts.

**Input authority:** `DEMO-HOUSEHOLD.md`  
**Engine candidate:** `demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md`  
**Detailed UI checklist:** `demo/UI-ACCEPTANCE-CHECKLIST-3105664.md`  
**Final output authority:** accepted dated receipts under `demo/`  
**Security:** fictional data only; never use a client account, Austin's personal plan, credentials, wallet addresses, exact custody locations, or Bitcoin secrets

## Current stage

The approved household has already been mapped into the current Orange Plan engine and reconciled through:

- the projection engine,
- 1,000 seeded test runs,
- earliest-date search,
- Cash Flow diagnostics,
- Debt calculations,
- Allocation scope,
- Retirement Income funding,
- and the 4% inflation Scenario.

This run no longer exists to discover the numbers from scratch. It verifies what the customer-facing page visibly labels, rounds, saves, previews, and explains.

## Product limitation

Orange Plan can create a passphrase-protected encrypted export, but in-app plan restore is currently unavailable. The receipts and export are records, not a restore workflow the course can promise today.

## Before the run

Record:

| Item | Value |
|---|---|
| Deployed URL |  |
| App commit / version |  |
| Run date and time |  |
| Recorder |  |
| Browser / viewport |  |
| Bitcoin price shown |  |
| Storage mode |  |
| Synthetic account ID |  |
| Demo household version | `demo-v1-inputs` |
| Build Your Plan version / state |  |

Confirm the account contains only synthetic data and the source values match `DEMO-HOUSEHOLD.md`.

## Evidence saved at every checkpoint

Each receipt stores:

- receipt ID,
- fixture version,
- app commit/version,
- deployed route,
- screenshot or recording reference,
- Saved / Previewing / Scenario / read-only state,
- visible source lines,
- visible output and rounding,
- app completion rule,
- human planning finish line,
- discrepancies and resolution,
- and the next checkpoint.

No receipt contains a credential, account number, wallet address, wallet backup, seed phrase, private key, passphrase, PIN, password, or exact custody location.

---

# 1 · `demo-v1-baseline`

**Route:** current Plan → Retirement surface

Expected:

| Output | Candidate |
|---|---:|
| Household retirement age | Alex 55 |
| Baseline retirement spending | $100,000/year in today's dollars |
| Planning age | 95 |
| Confidence target | 80% |
| Confidence at planned date | **94.6%** |
| Earliest target-qualified date | **May 2032 · Alex age 51** |
| Boundary confidence | **80.0%** |

Verify:

- one household retirement date is shown using the primary person's age,
- a March retirement date is compatible with partial-year household wages,
- no separate deterministic retirement result is presented beside the test-run result,
- and the retirement age, spending, and target edit sources are clear.

## 2 · `demo-v1-cashflow`

**Route:** `/cash-flow`

Expected:

| Output | Candidate |
|---|---:|
| Gross income | $190,000/year |
| Modeled tax | **$36,862/year** |
| Living spending | $80,000/year, debt excluded |
| Required debt | $1,833/month |
| Extra auto principal | $500/month |
| Planned debt | $2,333/month |
| Capacity before extra debt | $4,261/month |
| Post-debt surplus | **$3,761/month** |
| Contribution route after debt | $3,500/month |
| Operating cushion | $261/month |
| Reserve | $30,000 current / target · 6 months |

Verify the $500 extra principal is already inside planned Debt and is not routed a second time.

The full household decision is:

> $500 extra debt + $3,500 account contributions = $4,000/month

The round $40,000 tax remains a concept-teaching estimate. A walkthrough reading the page uses the current displayed tax.

## 3 · `demo-v1-debt`

**Route:** `/debt`

Expected:

| Output | Candidate |
|---|---:|
| Total debt | $298,000 |
| Required payments | $1,833/month |
| DTI | **11.6%** |
| DTA | **40.0%** at the reference valuation |
| Auto payoff | **2027 · Alex age 46** |

Verify the household ceiling is clearly separate from the app's general risk bands:

- keep DTI below 25%,
- do not add debt at 40%+ DTA.

## 4 · `demo-v1-allocation`

**Route:** `/allocation`

Expected scope:

| Scope | Candidate |
|---|---:|
| App allocatable portfolio | **$270,000** |
| Excluded 529 | $25,000 |
| Excluded primary residence | $450,000 |
| Bitcoin | $175,000 |
| Current Bitcoin allocation | **64.8%** |
| Target | 50% |
| Review band | 40–60% |
| Status | Above band; review, no automatic trade |

Expected drawdown:

- 75% Bitcoin loss: $131,250
- Allocatable portfolio after loss, other holdings flat: $138,750

Verify the page makes the denominator discoverable and the taxable Bridge route follows target/drift rather than automatically buying more Bitcoin.

## 5 · `demo-v1-tax`

**Route:** `/tax`

Expected basis state:

- total Bitcoin: 1.75 BTC
- complete lots: 1.25 BTC with $48,000 known basis
- reconstruction pending: 0.40 BTC
- unknown: 0.10 BTC

Verify:

- unresolved basis is visible,
- the tax roadmap is labelled as a planning result,
- an app lot-method preview is not described as executed identification,
- and no unknown basis is silently presented as complete.

The current-year engine tax is $36,862. Distant roadmap values remain assumption-sensitive and this receipt remains professionally qualified until the CPA response is applied.

## 6 · `demo-v1-income`

**Route:** `/income`

### Spending choices

| Choice | Candidate |
|---|---:|
| Conservative / 95% | $99,317/year |
| Current Plan | **$100,000/year at 94.6%** |
| Balanced / 80% | $170,216/year |
| Aggressive / 60% | $249,904/year |
| Saved starting paycheck | **$100,000/year** |

Verify Plan confidence, starting-spending choice, and annual guardrails are visibly separate controls.

### First retirement calendar year

| Component | Candidate |
|---|---:|
| Base living | $129,912 |
| College | $13,439 |
| Living need | $143,351 |
| Debt | $17,400 |
| Tax | $10,632 |
| **Total need** | **$171,383** |
| Partial-year household wages | $42,557 |
| Inflation-adjusted part-time income | $26,878 |
| **Recurring income** | **$69,435** |
| **Total draw** | **$101,948** |

### Sources

| Source | Candidate |
|---|---:|
| Cash | $2,200 |
| Stocks | $1,800 |
| Bitcoin | approximately $97,900 |
| Rounded taxable source total | $101,946 |
| Bitcoin sale proceeds | $97,948 |
| Projected 2036 BTC price | $1,235,921 |
| Bitcoin sold | **0.079251 BTC** |

The $2 source difference is display rounding. Verify the dollars, projected price, and Bitcoin units all come from the same year.

## 7 · `demo-v1-protect`

**Route:** `/protect`

Capture the app status for:

- custody type and balance jobs,
- recovery test,
- top physical/human/provider failure,
- Family Custody Map,
- beneficiaries and roles,
- heir letter and delivery,
- insurance records and open gaps,
- and overall readiness.

Do not accept a checkmark as proof of:

- a working wallet recovery,
- another family member's capability,
- a valid legal document,
- an accepted provider beneficiary record,
- or active insurance coverage.

Record both the app completion rule and the real-world proof still missing.

## 8 · `demo-v1-final`

**Routes:** `/scenarios`, `/your-plan`, report, PDF, and export controls

Expected inflation Scenario:

| Output | Candidate |
|---|---:|
| Baseline inflation | 3% |
| Baseline confidence | 94.6% |
| Scenario inflation | 4% |
| Scenario confidence | **91.6%** |
| Delta | **−3.0 percentage points** |
| Plan target | 80% |

Verify the baseline remains unchanged and the comparison does not invent an earliest-date or estate delta it does not show.

Also verify:

- report values agree with their source pages,
- one to three actions have owners and dates,
- PDF is the readable annual record,
- encrypted export is the passphrase-protected data copy,
- and restore is not described as currently available.

Do not use the $428,365,615 modeled ending value as a Core promise or primary visual.

---

# Build Your Plan metadata pass

After Austin completes the deployed Build Your Plan flow, record for every step:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `accepted_app_commit`
- `verified_date`
- `demo_household_version`
- `starting_checkpoint`
- `ending_checkpoint`
- `planning_decisions_implemented`
- `saved_input_or_preview_or_scenario`
- `app_completion_rule`
- `human_completion_rule`
- important number keys

Do not write an exact click path from a mockup or source branch Austin has not used.

# Final reconciliation

Before an output appears in spoken video, visual, or walkthrough, confirm:

- the value exists in an accepted receipt,
- the visible label and rounding match,
- saved/preview/Scenario state is named,
- source rows reconcile,
- the Allocation denominator is stated,
- extra debt is not counted twice,
- retirement sources equal the total draw within display rounding,
- Bitcoin dollars, projected price, and units agree,
- unresolved basis is not presented as a complete tax result,
- Protect does not overstate real-world proof,
- and the app commit/version is stored.

When a check fails, fix the source or app. Do not create a course-only explanation for a number that does not reconcile.
