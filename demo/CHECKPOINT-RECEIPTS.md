# Academy demo checkpoint receipts

Checkpoint receipts are the evidence connecting a course example to the current Orange Plan calculation.

They prevent three problems:

1. a script inventing a result the app did not produce,
2. the same demo household producing different numbers across lessons without explanation,
3. and a later app change silently making a recorded walkthrough stale.

The machine-readable schema is [`checkpoint-receipt.schema.json`](checkpoint-receipt.schema.json).

## Receipt naming

```text
demo/receipts/<fixture-version>/<checkpoint-id>/<app-commit>.json
```

Example structure:

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

Do not create a canonical receipt until the approved inputs are entered into the current app in an isolated synthetic context.

## Required receipt identity

Every receipt records:

- fixture version,
- checkpoint ID,
- capture time,
- exact app commit,
- app and projection-engine version when available,
- source-input hash,
- isolated storage context,
- app surface and save/apply behavior,
- decisions applied,
- page outputs,
- reconciliation checks,
- known holds,
- and confirmation that no secrets or customer data are present.

## Checkpoint-specific output minimums

### `demo-v1-baseline`

Capture:

- current net worth and source totals,
- total Bitcoin quantity and current percentage,
- planned retirement age,
- Baseline spending,
- Plan confidence target,
- confidence at planned age,
- earliest target-qualified month or age,
- assumption values actually saved,
- and any data-quality warnings.

Reconcile:

- account and holding totals,
- 1.75 BTC quantity,
- debt and asset rows,
- expected life events,
- and current Plan inputs.

### `demo-v1-cashflow`

Capture:

- income,
- app-calculated taxes,
- living spending,
- debt payments,
- displayed surplus,
- bare-bones spending,
- reserve basis and months,
- target amount,
- current reserve amount,
- and months funded.

Reconcile:

- displayed surplus with the current app source rows,
- debt not duplicated inside living spending,
- reserve basis × months with the displayed target,
- and committed cash excluded when applicable.

The clean $40,000 teaching tax estimate and $4,000 monthly surplus are not canonical when the app produces a materially different result for the approved state and tax inputs.

### `demo-v1-debt`

Capture:

- each balance, rate, payment, and treatment,
- displayed DTI and DTA,
- auto-loan extra principal,
- projected payoff timing,
- and the household ceiling recorded with the plan.

Reconcile:

- required payments with Cash Flow,
- $298,000 starting debt at the reference state,
- extra principal without reducing the reserve,
- and DTA with the same current asset values used elsewhere.

### `demo-v1-allocation`

Capture:

- current holding mix,
- current Bitcoin percentage and denominator,
- target and review band,
- Reserve / Bridge / Legacy or goal assignments,
- saved contribution route,
- and any one-time preview kept separate from the saved route.

Reconcile:

- holdings across every account,
- route totaling the same current surplus,
- employer match outside household routing dollars,
- no automatic Bitcoin purchase implied by the taxable Bridge route,
- and no duplicated known-cost funding.

### `demo-v1-tax`

Capture:

- current Bitcoin quantity covered by tax lots,
- known basis,
- unresolved quantity and status,
- current-year tax roadmap values,
- projected traditional balance / required-distribution context,
- and any comparison kept as a preview rather than saved implementation.

Reconcile:

- 1.75 BTC holdings with 1.75 BTC of lot quantity,
- known and unknown basis remaining separate,
- transfers not becoming fake sales and purchases,
- and the app comparison not being described as completed tax execution.

### `demo-v1-income`

Capture:

- retirement living spending,
- recurring income by year,
- living-spending gap,
- first-year total need,
- tax and debt costs,
- reserve refill when applicable,
- total draw,
- account and holding source split,
- Bitcoin sold or retained,
- reserve months funded,
- Conservative / Balanced / Aggressive amounts,
- current Plan spending confidence,
- saved starting-spending choice,
- and annual policy values.

Reconcile:

- total draw with the full source split,
- Bitcoin sold or retained across every surface,
- current Plan amount with the spending-band comparison,
- Plan confidence remaining separate from the spending choice and guardrails,
- and borrowing excluded from the saved Core baseline unless the approved decision changes.

### `demo-v1-protect`

Capture:

- custody type and process status,
- recovery-test date/status,
- highest single point of failure,
- Family Custody Map status,
- beneficiary and role status,
- heir-letter and delivery status,
- policy and coverage-gap status,
- and the app's readiness result.

Reconcile:

- app status with the real-world proof limitation,
- no secret material inside the app or screenshot,
- provider records remaining provider-owned,
- legal authority remaining attorney/provider/court-dependent,
- and incomplete real-world work not being marked complete merely to produce a checkmark.

### `demo-v1-final`

Capture:

- saved recurring stress tests,
- one active choice Scenario,
- Scenario deltas,
- final report values,
- ending assets and projected estate,
- one to three next actions,
- PDF/report version,
- encrypted export created for secure storage,
- and the six-sentence plan summary.

Reconcile:

- every decided Scenario with its actual source page,
- report values with the current saved plan,
- action owners and dates,
- PDF versus encrypted export roles,
- and no claim that in-app restore currently works while restore remains disabled.

## Receipt status

A reconciliation can be:

- `pass`
- `fail`
- `blocked`
- `not_applicable`

A receipt with a failed reconciliation is evidence of a problem, not a canonical example.

A blocked reconciliation can be retained for audit but keeps the affected script, slide, or walkthrough out of the filming queue.

## Screenshot rule

Screenshots are supporting evidence, not the receipt itself.

Before committing or sharing a screenshot:

- confirm the account is synthetic,
- remove browser/profile identifiers,
- remove credentials, account numbers, addresses, exact custody locations, and personal data,
- record the app commit and page,
- and avoid showing any secret-bearing custody material.

## Replacement rule

A new app commit does not automatically invalidate every receipt.

Rerun the affected checkpoint when an app change modifies:

- an input contract,
- calculation,
- label used in teaching,
- page route,
- save/apply state,
- completion rule,
- report field,
- AI review source,
- or demo output.

Use the app PR's Academy-impact classification to identify the checkpoint needing re-verification.

## Course-use rule

A script, slide, walkthrough, report example, or landing-page claim may use an app-owned number only when it names or traces to a passing receipt for the same fixture and relevant app behavior.

The receipt is not a promise that a customer will receive the same result. It proves only what the fictional household produced under the recorded inputs, app commit, and projection version.