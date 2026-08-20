# Academy demo checkpoint receipts

Checkpoint receipts are the evidence connecting a course example to the current Orange Plan calculation and customer-facing page.

They prevent three problems:

1. a script inventing a result the app did not produce,
2. the same household producing different numbers across lessons without explanation,
3. and a later app change silently making a recorded walkthrough stale.

The current engine candidate is `ENGINE-CHECKPOINT-CANDIDATE-3105664.md`. The visible-page procedure is `UI-ACCEPTANCE-CHECKLIST-3105664.md`. The machine-readable receipt schema is `checkpoint-receipt.schema.json`.

## Receipt naming

```text
demo/receipts/<fixture-version>/<checkpoint-id>/<app-commit>.json
```

Expected checkpoints:

```text
demo/receipts/demo-v1-inputs/
  demo-v1-baseline/
  demo-v1-cashflow/
  demo-v1-debt/
  demo-v1-allocation/
  demo-v1-tax/
  demo-v1-income/
  demo-v1-protect/
  demo-v1-final/
```

## Candidate versus final receipt

The reproducible engine candidate may be used to:

- reconcile script arithmetic,
- identify a course/app mismatch,
- create the current concept-visual data contract,
- and define what the deployed page must show.

It is not a final UI receipt until the synthetic household is opened in the accepted deployed build and the recorder confirms:

- visible labels and rounding,
- route,
- Saved / Previewing / Scenario / read-only state,
- source-line reconciliation,
- app completion rule,
- human finish line,
- safe screenshot or recording evidence,
- and any discrepancy between the engine result and page.

## Required receipt identity

Every receipt records:

- fixture version,
- checkpoint ID,
- capture time,
- exact app commit/version,
- projection-engine version when available,
- source-input hash,
- isolated synthetic storage/account context,
- route and surface,
- save/apply/autosave behavior,
- decisions applied,
- page outputs,
- reconciliation checks,
- known holds,
- screenshot/recording reference,
- and confirmation that no secrets or customer data are present.

---

# Checkpoint-specific minimums

## `demo-v1-baseline`

Capture:

- current net worth and source totals,
- total Bitcoin quantity,
- household retirement age,
- Baseline spending,
- Plan confidence target,
- confidence at planned date,
- earliest target-qualified month/age,
- assumption values actually saved,
- and data-quality warnings.

Current candidate:

| Output | Value |
|---|---:|
| Household retirement start | March 2036 · Alex age 55 |
| Confidence at planned date | 94.6% |
| Plan target | 80% |
| Earliest target-qualified date | May 2032 · Alex age 51 |
| Boundary confidence | 80.0% |

Reconcile:

- 1.75 BTC quantity,
- one household retirement date anchored to the primary person's age,
- partial-year wages when retirement starts in March,
- source accounts and debts,
- life events,
- and no second deterministic retirement result.

## `demo-v1-cashflow`

Capture:

- gross income,
- app-calculated tax,
- living spending,
- required debt,
- saved extra principal,
- planned debt,
- displayed surplus,
- account contribution route,
- remaining cushion,
- bare-bones spending,
- reserve basis/months/amount/funding.

Current candidate:

| Output | Value |
|---|---:|
| Gross income | $190,000/year |
| App-modeled tax | $36,862/year |
| Required debt | $1,833/month |
| Extra auto principal | $500/month |
| Planned debt | $2,333/month |
| Decision capacity before extra debt | $4,261/month |
| Post-debt surplus | $3,761/month |
| Account route | $3,500/month |
| Operating cushion | $261/month |
| Reserve | $30,000 · 6 months · fully funded |

Reconcile:

- debt not duplicated inside living spending,
- the $500 extra principal already inside planned Debt,
- full household decision of $500 debt + $3,500 contributions = $4,000,
- reserve basis × months,
- and source links for each output.

The round $40,000 tax and $4,000 route remain useful teaching values only when their meaning is explicit. A walkthrough reading the page uses the current displayed tax and post-debt surplus.

## `demo-v1-debt`

Capture:

- each balance, rate, payment, and treatment,
- displayed DTI and DTA,
- auto-loan extra principal,
- payoff timing,
- and household policy.

Current candidate:

- total debt: $298,000,
- required payments: $1,833/month,
- DTI: 11.6%,
- DTA: 40.0% at reference valuation,
- auto payoff: 2027 / Alex age 46.

Reconcile required payments with Cash Flow and keep household ceilings separate from product warning bands.

## `demo-v1-allocation`

Capture:

- included and excluded holdings,
- app Allocation denominator,
- current Bitcoin percentage,
- target and review band,
- current review state,
- Reserve / Bridge / Legacy / goal assignments,
- saved contribution direction,
- and drawdown result.

Current candidate:

| Output | Value |
|---|---:|
| App allocatable portfolio | $270,000 |
| Excluded 529 | $25,000 |
| Excluded home | $450,000 |
| Bitcoin | $175,000 |
| Current Bitcoin percentage | 64.8% |
| Target / band | 50% · 40–60% |
| Status | Above band · review, no automatic trade |
| Bitcoin loss at 75% | $131,250 |
| Allocatable after loss | $138,750 |

Reconcile:

- the 529 and home exclusions,
- broader $295,000 financial balances not being substituted for app scope,
- taxable Bridge route not automatically buying Bitcoin,
- and target review remaining separate from implementation.

## `demo-v1-tax`

Capture:

- current Bitcoin quantity covered by lots,
- known basis,
- unresolved quantity and status,
- current-year tax,
- roadmap labels,
- and any comparison kept as preview rather than implementation.

Current basis state:

- 1.25 BTC complete with $48,000 known basis,
- 0.40 BTC reconstruction pending,
- 0.10 BTC unknown.

Reconcile:

- 1.75 BTC holdings and lot quantity,
- transfers not becoming fake sales/purchases,
- unresolved basis remaining visible,
- and app lot-method comparison not being described as executed tax identification.

This receipt remains professionally qualified until the CPA response is applied.

## `demo-v1-income`

Capture:

- retirement living spending,
- recurring income by year,
- first-year need lines,
- total need,
- recurring income,
- total draw,
- account and holding sources,
- Bitcoin dollars, projected price, and units sold,
- Conservative / current / Balanced / Aggressive choices,
- saved starting paycheck,
- annual guardrails,
- and reserve-refill state.

Current spending candidates:

| Choice | Value |
|---|---:|
| Conservative / 95% | $99,317/year |
| Current Plan | $100,000/year at 94.6% |
| Balanced / 80% | $170,216/year |
| Aggressive / 60% | $249,904/year |
| Saved starting paycheck | $100,000/year |

Current first-year candidate:

| Component | Value |
|---|---:|
| Base living | $129,912 |
| College | $13,439 |
| Debt | $17,400 |
| Tax | $10,632 |
| Total need | $171,383 |
| Partial-year household wages | $42,557 |
| Part-time income | $26,878 |
| Recurring income | $69,435 |
| Total draw | $101,948 |

Sources:

- cash about $2,200,
- stocks about $1,800,
- Bitcoin about $97,900,
- account source total $101,946 after rounding,
- Bitcoin proceeds $97,948,
- projected price $1,235,921,
- Bitcoin sold 0.079251 BTC.

Reconcile:

- source total with total draw within display rounding,
- Bitcoin dollars/price/units from the same year,
- current Plan amount with reference choices,
- Plan confidence separate from spending choices and annual guardrails,
- and borrowing excluded from the saved Core baseline.

## `demo-v1-protect`

Capture:

- custody type and balance jobs,
- recovery status/date,
- highest physical/human/provider failure,
- Family Custody Map,
- beneficiary and role status,
- heir-letter and delivery status,
- policy/coverage-gap status,
- and app readiness.

Reconcile app status with real-world proof:

- a checked field does not prove recovery,
- another person can recover only after a real practice test,
- provider records remain provider-owned,
- legal authority remains attorney/provider/court-dependent,
- insurance remains contract-dependent,
- and incomplete real-world work is not marked complete merely to create a checkmark.

## `demo-v1-final`

Capture:

- saved stress tests,
- one active choice Scenario,
- Scenario deltas,
- final report values,
- one to three actions,
- six-sentence summary,
- PDF version,
- and encrypted export state.

Current inflation Scenario:

- Baseline 3% / 94.6%,
- Scenario 4% / 91.6%,
- delta −3.0 percentage points,
- Plan target 80%.

Reconcile:

- Baseline remains unchanged,
- no unreported earliest-date or estate delta is invented,
- report values agree with source pages,
- action owners/dates are present,
- PDF and encrypted export have different jobs,
- and in-app restore is not described as currently available.

The modeled $428,365,615 ending value is not a Core promise or primary visual.

---

# Receipt status

A reconciliation can be:

- `pass`
- `fail`
- `blocked`
- `not_applicable`

A failed reconciliation is evidence of a product, source, fixture, or course problem—not a canonical example.

A blocked reconciliation can remain in the audit trail but keeps the affected script, visual, or walkthrough out of the filming queue.

## Screenshot rule

Screenshots support the receipt; they are not the receipt by themselves.

Before committing or sharing one:

- confirm the account is synthetic,
- remove browser/profile identifiers,
- remove credentials, account numbers, addresses, exact custody locations, and personal data,
- record app commit and route,
- avoid all secret-bearing custody material,
- and capture enough context to identify Saved / Previewing / Scenario state.

## Replacement rule

A new app commit does not automatically invalidate every receipt.

Rerun the affected checkpoint when an app change modifies:

- input contract,
- formula or denominator,
- label used in teaching,
- page route,
- save/apply state,
- completion rule,
- report field,
- AI source,
- or demo output.

Use the app PR's Academy-impact classification to identify the checkpoint needing re-verification.

## Course-use rule

A spoken lesson, visual, walkthrough, report example, or outcome claim may use an app-owned value only when it traces to:

1. the same approved fixture,
2. the current engine candidate or a passing final receipt,
3. the same relevant app behavior,
4. and the correct professional/real-world qualification.

The receipt does not promise that a customer will receive the same result. It proves only what the synthetic household produced under the recorded inputs, app commit, and projection version.
