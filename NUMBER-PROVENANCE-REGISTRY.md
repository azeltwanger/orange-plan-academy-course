# Orange Plan Academy — number provenance registry

**Purpose:** answer the most repeated client question in one maintained place:

> Where did this number come from?

Every important output is taught using four lines:

- **WHAT IT MEANS** — the plain-language question answered
- **CALCULATED FROM** — the upstream inputs and calculation concept
- **EDIT SOURCE** — where the learner corrects or changes the source
- **THIS AFFECTS** — the important downstream results that should move

This registry is the course-level contract. The current app code and checkpoint receipt remain the authority for exact implementation and displayed values.

## Use rules

- A concept lesson explains the relationship.
- A walkthrough points to the current source and result.
- A checkpoint receipt proves the fictional demo value.
- A tooltip or AI explanation may use the same four-line structure.
- Do not promise that every output is one literal database field.
- When a number is wrong, fix the upstream input or deliberately change the decision. Do not edit an output until it looks better.
- When the app calculation changes, classify the app PR as a concept, walkthrough, demo-account, or professional/reference impact and update this registry.

---

# Baseline and retirement timing

## Net worth / current position

| Field | Contract |
|---|---|
| **What it means** | Current assets minus current liabilities under the app's included-account rules |
| **Calculated from** | Active account and holding values, real-estate/other asset values, and active debt balances |
| **Edit source** | Accounts, holdings, manual asset values, and debt rows |
| **This affects** | Current-position summary, debt-to-assets, allocation context, plan funding, report |
| **Primary lesson** | 1.1 and 9.2 |
| **Checkpoint** | `demo-v1-baseline` |
| **Important qualification** | Investable assets, gross assets, and net worth use different denominators; do not substitute one for another |

## Planned retirement age

| Field | Contract |
|---|---|
| **What it means** | The retirement start age the learner asked Orange Plan to test |
| **Calculated from** | Saved Plan input; date/month handling may derive from household birth date and selected age |
| **Edit source** | Plan → Retirement |
| **This affects** | Contribution years, income timeline, withdrawal start, confidence, earliest-date comparison, taxes |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |

## Baseline retirement spending

| Field | Contract |
|---|---|
| **What it means** | Annual living spending the retirement plan is expected to support in the app's stated dollar basis |
| **Calculated from** | Saved Baseline spending plus dated life events and later modeled inflation; debt, tax, and refill remain separate lines when the app shows them separately |
| **Edit source** | Plan spending input and the specific life event |
| **This affects** | Confidence, earliest date, spending-band amounts, total need, total draw, tax, sales, reserve basis when selected |
| **Primary lesson** | 1.3 and 6.1 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-income` |
| **Important qualification** | Do not duplicate debt payments or one-time life events inside annual living spending |

## Plan confidence target

| Field | Contract |
|---|---|
| **What it means** | The minimum share of test runs the learner wants before a retirement date qualifies as the earliest date |
| **Calculated from** | User-selected target; current product default and allowed range are app facts |
| **Edit source** | Plan → Retirement |
| **This affects** | Earliest target-qualified date and target/verdict language; it does not rewrite the planned retirement age |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Important qualification** | Separate from the starting-spending comparison and annual spending guardrails on Income |

## Plan confidence result

| Field | Contract |
|---|---|
| **What it means** | Share of the 1,000 current test runs where the saved plan remained funded through the planning age |
| **Calculated from** | Entire saved projection: balances, holdings, returns, inflation, income, spending, debts, life events, taxes, retirement timing, contributions, and saved strategies |
| **Edit source** | The underlying input or strategy that is wrong or deliberately being tested; there is no direct “make confidence higher” source field |
| **This affects** | Plan verdict, earliest target-qualified date, Scenario comparison, annual review |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Important qualification** | Not a guarantee, grade, literal bankruptcy probability, or separate deterministic result |

## Earliest target-qualified date

| Field | Contract |
|---|---|
| **What it means** | First month or age where confidence reaches or exceeds the learner's Plan confidence target |
| **Calculated from** | Repeated current test-run results across possible retirement start dates using the same saved plan and selected target |
| **Edit source** | Plan confidence target and the underlying plan inputs/decisions—not the displayed date |
| **This affects** | Retirement-timing decision, Scenario comparison, report, action plan |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Important qualification** | Comes from the same confidence framework as the planned-age result |

---

# Cash Flow and Reserve

## Gross income

| Field | Contract |
|---|---|
| **What it means** | Current recurring income before modeled tax and deductions under the selected income type |
| **Calculated from** | Active income sources, amount, frequency, owner, start/end dates, and recurring/one-time treatment |
| **Edit source** | Income / Cash Flow source rows |
| **This affects** | Tax, surplus, DTI, contributions, confidence, retirement timing |
| **Primary lesson** | 1.1 and 2.1 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-cashflow` |

## Estimated current taxes

| Field | Contract |
|---|---|
| **What it means** | App estimate of current federal, payroll, state, and other included tax for the modeled year or monthly cash-flow view |
| **Calculated from** | Filing status, state, income types, deductions/settings included by the app, withholding/payment overrides, and current tax configuration |
| **Edit source** | Household/tax settings, income sources, and any current tax-payment override supported by Cash Flow |
| **This affects** | Surplus, available routing, report, and later retirement-tax comparisons |
| **Primary lesson** | 2.1 and 5.2 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Important qualification** | App estimate is not the filed return; the clean demo teaching estimate is not canonical when the current app produces a materially different result |

## Normal living spending

| Field | Contract |
|---|---|
| **What it means** | Recurring living costs the current plan is expected to fund outside separately modeled debt payments |
| **Calculated from** | Saved spending input and, where used, linked/imported transaction review and exclusions |
| **Edit source** | Cash Flow / Plan spending source and transaction review |
| **This affects** | Surplus, retirement spending, confidence, reserve basis when selected, earliest date |
| **Primary lesson** | 2.1 |
| **Checkpoint** | `demo-v1-cashflow` |

## Bare-bones spending

| Field | Contract |
|---|---|
| **What it means** | Temporary minimum living cost during an emergency or reduced-spending period |
| **Calculated from** | Learner-selected essential spending amount; it is a planning input rather than an app inference unless current product behavior states otherwise |
| **Edit source** | Cash Flow → Reserve settings |
| **This affects** | Reserve target when selected as basis, survival time, retirement cash-buffer planning |
| **Primary lesson** | 2.1 and 2.2 |
| **Checkpoint** | `demo-v1-cashflow` |

## Required debt payments

| Field | Contract |
|---|---|
| **What it means** | Current required payments for active debts in the period |
| **Calculated from** | Debt rows, payment amount/frequency, start/end or payoff schedule, and active status |
| **Edit source** | Debt page / debt records |
| **This affects** | Surplus, DTI, payoff timing, retirement-year need, confidence |
| **Primary lesson** | 2.1 and 3.1 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-debt` |
| **Important qualification** | Keep out of living spending when the debt row already owns the payment |

## Reliable surplus

| Field | Contract |
|---|---|
| **What it means** | Recurring money left after modeled current tax, living spending, and required debt payments |
| **Calculated from** | Income − estimated taxes − living spending − required debt payments under the current Cash Flow source rows |
| **Edit source** | The underlying income, tax, spending, or debt source—not the displayed surplus |
| **This affects** | Reserve build, extra debt, contributions, future balances, confidence, earliest date |
| **Primary lesson** | 2.1 and 4.3 |
| **Checkpoint** | `demo-v1-cashflow` |

## Reserve target amount

| Field | Contract |
|---|---|
| **What it means** | Cash amount selected to protect the household from income loss, unexpected costs, or retirement forced sales |
| **Calculated from** | Selected monthly spending basis × target months |
| **Edit source** | Cash Flow → Reserve settings |
| **This affects** | Reserve funding gap, routing available for other goals, retirement cash-buffer plan |
| **Primary lesson** | 2.2 |
| **Checkpoint** | `demo-v1-cashflow` |

## Reserve months funded

| Field | Contract |
|---|---|
| **What it means** | Current reserve-designated amount expressed in months of the selected spending basis |
| **Calculated from** | Included reserve holdings ÷ selected monthly basis, subject to the current app's reserve-inclusion rules |
| **Edit source** | Reserve-designated holdings, spending basis, and target settings |
| **This affects** | Readiness status, routing, refill, forced-sale risk |
| **Primary lesson** | 2.2 and 6.1 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-income` |

## Known future-cost funding gap

| Field | Contract |
|---|---|
| **What it means** | Part of a committed future cost that still lacks a source |
| **Calculated from** | Commitment − current dedicated savings − expected cash flow − expected proceeds − deliberately accepted financing |
| **Edit source** | Life event and its dedicated account/contribution plan |
| **This affects** | Current routing, Bridge need, future withdrawals, confidence, earliest date |
| **Primary lesson** | 2.3 and 2.4 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-allocation` |

---

# Debt

## Debt-to-income (DTI)

| Field | Contract |
|---|---|
| **What it means** | Share of gross monthly income committed to the app's included required monthly debt payments |
| **Calculated from** | Included required monthly payments ÷ gross monthly income |
| **Edit source** | Debt payment rows and income sources |
| **This affects** | Cash-flow pressure, app debt band, borrowing room, surplus context |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |
| **Important qualification** | Household ceiling can be lower than the app's outer planning bands |

## Debt-to-assets (DTA)

| Field | Contract |
|---|---|
| **What it means** | Total included debt compared with current included gross asset values |
| **Calculated from** | Active debt balances ÷ included current asset values |
| **Edit source** | Debt and asset/holding records |
| **This affects** | Balance-sheet pressure, app debt band, future borrowing decision |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |
| **Important qualification** | Can change quickly with Bitcoin price even when debt barely changes; name the denominator |

## Projected payoff date

| Field | Contract |
|---|---|
| **What it means** | Modeled date the debt reaches zero under the saved payment and extra-principal assumptions |
| **Calculated from** | Balance, rate, required payment, recurring extra principal, lump sums, and payment timing |
| **Edit source** | Debt strategy and real debt terms |
| **This affects** | Future cash flow, routing after payoff, retirement-year debt cost, confidence |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |

## Bitcoin-loan LTV, when applicable

| Field | Contract |
|---|---|
| **What it means** | Loan balance relative to current pledged-collateral value under the app/lender definition |
| **Calculated from** | Loan balance ÷ current value of pledged Bitcoin, plus lender-specific terms when modeling calls, top-ups, or liquidation |
| **Edit source** | Debt/loan record, pledged collateral, and actual lender terms |
| **This affects** | Margin-call risk, liquidation, top-up need, borrowing capacity, estate liability |
| **Primary lesson** | Advanced loan lesson; named in 3.1 and 6.2 only when relevant |
| **Checkpoint** | Optional advanced demo receipt, not Core baseline |

---

# Allocation and contributions

## Current asset mix

| Field | Contract |
|---|---|
| **What it means** | Combined household exposure by holding type across included investable accounts |
| **Calculated from** | Current holdings and values across accounts, grouped by current app asset class |
| **Edit source** | Account and holding records |
| **This affects** | Allocation, drawdown, drift, projections, account location, report |
| **Primary lesson** | 4.1 and 4.2 |
| **Checkpoint** | `demo-v1-allocation` |

## Current Bitcoin percentage

| Field | Contract |
|---|---|
| **What it means** | Share of the selected investable denominator currently represented by Bitcoin exposure |
| **Calculated from** | Included direct and indirect Bitcoin holding value ÷ included investable asset value |
| **Edit source** | Holdings, classifications, and current price source |
| **This affects** | Drift, drawdown dollars, routing, custody stakes, confidence |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Important qualification** | Investable percentage, gross-assets percentage, and net-worth exposure are different questions |

## Target allocation

| Field | Contract |
|---|---|
| **What it means** | Household's chosen long-term mix under the current target policy |
| **Calculated from** | Saved learner decision; product may normalize or validate totals under current rules |
| **Edit source** | Allocation target editor |
| **This affects** | Drift, contribution routing, previews, drawdown target, account instructions |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Important qualification** | Target is not automatically today's trade |

## Allocation drift

| Field | Contract |
|---|---|
| **What it means** | Difference between current and target exposure under the page's displayed convention |
| **Calculated from** | Current mix compared with target mix |
| **Edit source** | Holdings/current values and target allocation |
| **This affects** | Review state, suggested contribution direction, one-time preview |
| **Primary lesson** | 4.1 and 4.3 |
| **Checkpoint** | `demo-v1-allocation` |

## Bitcoin drawdown hit

| Field | Contract |
|---|---|
| **What it means** | Approximate current portfolio loss attributable to the selected Bitcoin decline before other holdings move |
| **Calculated from** | Bitcoin holding value × selected decline; percentage shorthand is Bitcoin allocation × decline |
| **Edit source** | Current/Scenario holdings, price, allocation, and selected stress percentage |
| **This affects** | Holdability, reserve adequacy, debt/collateral risk, custody consequence |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |

## Reserve / Bridge / Legacy funding

| Field | Contract |
|---|---|
| **What it means** | Current money assigned to near-, medium-, and long-term jobs compared with their dollar needs |
| **Calculated from** | Account/holding job assignments, reserve settings, known costs, and year-by-year retirement Bridge needs |
| **Edit source** | Allocation/job assignments, life events, Cash Flow reserve, Retirement Income |
| **This affects** | Contribution route, forced-sale risk, early-retirement accessibility |
| **Primary lesson** | 4.2 |
| **Checkpoint** | `demo-v1-allocation` and `demo-v1-income` |

## Available contribution dollars

| Field | Contract |
|---|---|
| **What it means** | Recurring current surplus available to assign to reserve, debt, and contributions |
| **Calculated from** | Current reliable surplus; employer match is separate employer money |
| **Edit source** | Cash Flow source rows and saved routing/contribution records |
| **This affects** | Account growth, debt payoff, Bridge/Legacy funding, confidence, earliest date |
| **Primary lesson** | 4.3 |
| **Checkpoint** | `demo-v1-allocation` |

## Saved next-dollar route

| Field | Contract |
|---|---|
| **What it means** | Household's current assignment of recurring surplus across selected destinations |
| **Calculated from** | Reserve status, employer benefit, debt treatment, timeframe gaps, account eligibility, tax plan, and target allocation |
| **Edit source** | Cash Flow contribution/routing controls and underlying account elections |
| **This affects** | Account balances, payoff date, access, tax path, confidence |
| **Primary lesson** | 4.3 |
| **Checkpoint** | `demo-v1-allocation` |
| **Important qualification** | Route must not exceed surplus or double-count employer contributions |

---

# Tax

## Bitcoin quantity covered by tax lots

| Field | Contract |
|---|---|
| **What it means** | Current taxable Bitcoin quantity explained by acquisition/disposition history |
| **Calculated from** | Active acquisition lots minus supported dispositions and ownership-changing events |
| **Edit source** | Transaction import, lot records, and transfer matching |
| **This affects** | Basis completeness, sale comparison, tax confidence, lot selection |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |

## Known cost basis

| Field | Contract |
|---|---|
| **What it means** | Supported tax investment in the units still owned |
| **Calculated from** | Acquisition lots, permitted acquisition costs, and supported adjustments/dispositions |
| **Edit source** | Transaction and lot records—not market value |
| **This affects** | Gain/loss, projected tax, net proceeds, sell/borrow comparison, withdrawal planning |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |
| **Important qualification** | Unknown basis remains unknown; a zero-basis stress test is not automatically the filing position |

## Unrealized gain

| Field | Contract |
|---|---|
| **What it means** | Current market value minus known basis for the included units |
| **Calculated from** | Current quantity/value and known lot basis |
| **Edit source** | Holdings/price and lot records |
| **This affects** | Sale tax estimate and lot comparison; it does not create tax by itself |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |

## Projected tax by year

| Field | Contract |
|---|---|
| **What it means** | App estimate of federal and state tax from the modeled income and transactions in each year |
| **Calculated from** | Filing status, state, ordinary income, gains/losses, modeled deductions, Social Security, pension, withdrawals, conversions, and other included items |
| **Edit source** | Household/tax settings and the underlying income, basis, event, contribution, conversion, and withdrawal strategy |
| **This affects** | Surplus, total retirement need, total draw, source mix, confidence, earliest date |
| **Primary lesson** | 5.2 and 6.1 |
| **Checkpoint** | `demo-v1-tax` and `demo-v1-income` |
| **Important qualification** | Planning estimate, not the filed return; current-law details remain maintained reference/professional review |

## Traditional balance at required-distribution stage

| Field | Contract |
|---|---|
| **What it means** | Projected traditional balance exposed to the applicable future distribution rules |
| **Calculated from** | Current balance, contributions, returns, withdrawals, conversions, and applicable start age |
| **Edit source** | Traditional account records and contribution/withdrawal/conversion strategy |
| **This affects** | Future taxable income, conversion-window value, Medicare-related costs, withdrawal flexibility |
| **Primary lesson** | 5.2 |
| **Checkpoint** | `demo-v1-tax` |
| **Important qualification** | Applicable age depends on current law and birth year; keep the current table out of evergreen video |

## Roth-conversion comparison

| Field | Contract |
|---|---|
| **What it means** | Difference between Baseline and a defined conversion amount/timing under the app model |
| **Calculated from** | Conversion schedule plus all modeled current/future income, tax, account, Social Security, and withdrawal effects |
| **Edit source** | Conversion preview/strategy and underlying tax inputs |
| **This affects** | Current tax, Roth/traditional balances, future RMDs, withdrawals, estate, confidence |
| **Primary lesson** | Advanced; window identified in 5.2 |
| **Checkpoint** | `demo-v1-tax` |
| **Important qualification** | App comparison does not execute the conversion or determine the filed amount |

---

# Retirement Income

## Recurring retirement income

| Field | Contract |
|---|---|
| **What it means** | Modeled income arriving in the year without selling portfolio assets |
| **Calculated from** | Social Security, pension, part-time work, rental/other recurring sources, owner, dates, and current app tax treatment |
| **Edit source** | Underlying income records and start/end/claim dates |
| **This affects** | Living gap, Bridge, total draw, tax, reserve target/funding |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |

## Portfolio-funded living gap

| Field | Contract |
|---|---|
| **What it means** | Retirement living spending not covered by recurring income before adding separately modeled tax, debt, events, or refill |
| **Calculated from** | Retirement living spending − recurring income in the year |
| **Edit source** | Plan spending and income source records |
| **This affects** | Bridge need and full total draw |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |

## First-year total need

| Field | Contract |
|---|---|
| **What it means** | Full modeled cash requirement for the retirement year before recurring income is subtracted |
| **Calculated from** | Living spending + modeled tax + remaining debt + dated events + reserve refill and other included costs |
| **Edit source** | The underlying Plan, tax, debt, event, and reserve sources |
| **This affects** | Total draw and funding sources |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |

## Total draw

| Field | Contract |
|---|---|
| **What it means** | Amount the projection needs from accounts after recurring income |
| **Calculated from** | First-year/full annual need − recurring income, under the current projection and strategy |
| **Edit source** | Underlying need/income sources and saved strategy—not the displayed draw |
| **This affects** | Account withdrawals, holding sales, Bitcoin sold, tax, reserve, debt/loan, confidence |
| **Primary lesson** | 6.1 and 6.2 |
| **Checkpoint** | `demo-v1-income` |

## Account and holding source split

| Field | Contract |
|---|---|
| **What it means** | Accounts and holdings that fund the total draw under the saved retirement strategy |
| **Calculated from** | Total draw, account access, withdrawal phases, tax ceiling/strategy, asset order, available holdings, and borrowing policy when applicable |
| **Edit source** | Withdrawal phases, account strategy, asset strategy, and optional borrowing policy |
| **This affects** | Taxes, Bitcoin sold, account balances, reserve refill, estate, confidence |
| **Primary lesson** | 6.2 |
| **Checkpoint** | `demo-v1-income` |
| **Required reconciliation** | Source amounts add to the same total draw |

## Bitcoin sold or retained

| Field | Contract |
|---|---|
| **What it means** | Engine-calculated Bitcoin sale/retention under the year's funding strategy and modeled price |
| **Calculated from** | Total draw, available assets, account/asset order, allocation constraints, and borrowing policy when applicable |
| **Edit source** | Holdings and retirement funding strategy—not the displayed sale total |
| **This affects** | Capital gains, tax, future Bitcoin balance, custody exposure, estate, loan/collateral need |
| **Primary lesson** | 6.2 |
| **Checkpoint** | `demo-v1-income` |
| **Required reconciliation** | Agrees across funding card, chart, report, tooltip, and receipt |

## Retirement-spending reference amount

| Field | Contract |
|---|---|
| **What it means** | Annual starting spending supported near the selected reference confidence under the current retirement strategy |
| **Calculated from** | Current spending search/test-run framework, assumptions, and saved funding strategy |
| **Edit source** | Underlying Plan inputs and strategy; the reference amount itself is calculated |
| **This affects** | Starting paycheck, total need, draw, sales, tax, reserve use, long-term result |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` |
| **Important qualification** | Conservative/Balanced/Aggressive are planning choices, not personality labels |

## Current Plan spending confidence

| Field | Contract |
|---|---|
| **What it means** | Test-run result associated with the Baseline retirement-spending amount under the current strategy |
| **Calculated from** | Current Plan spending evaluated on the same retirement-spending test framework |
| **Edit source** | Baseline spending and the underlying plan/strategy |
| **This affects** | Comparison with reference choices and starting-paycheck decision |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` |
| **Important qualification** | Separate from Plan confidence used to find the earliest retirement date |

## Annual spending-policy update

| Field | Contract |
|---|---|
| **What it means** | Suggested paycheck for the next annual policy period |
| **Calculated from** | Prior saved target, inflation adjustment, latest confidence, target-confidence amount, lower/upper triggers, and annual correction cap |
| **Edit source** | Spending policy plus the current underlying plan inputs |
| **This affects** | Next-year cash need, total draw, sources, sales, reserve refill |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` and future annual-review receipt |
| **Important qualification** | Cap is a maximum; this is an annual policy review, not a market-timing signal |

## Loan balance at death, when borrowing is used

| Field | Contract |
|---|---|
| **What it means** | Projected outstanding borrowing liability at the planning/end-of-life point under the saved loan strategy |
| **Calculated from** | Draw schedule, interest, repayments, collateral events, lender assumptions, and the projection timeline |
| **Edit source** | Borrowing policy and actual lender terms |
| **This affects** | Estate value, collateral exposure, repayment need, liquidation and counterparty risk |
| **Primary lesson** | Advanced borrowing; comparison named in 6.2 |
| **Checkpoint** | Optional advanced receipt |

---

# Protect

## Custody readiness

| Field | Contract |
|---|---|
| **What it means** | Completion status of the custody-process fields and checklist saved in Protect |
| **Calculated from** | Current custody type, people, documents, review dates, and required checklist items under app rules |
| **Edit source** | Protect records |
| **This affects** | Next protection action, report, family handoff status |
| **Primary lesson** | 7.1–7.3 |
| **Checkpoint** | `demo-v1-protect` |
| **Important qualification** | Does not prove the backup is accurate, recovery worked, or the family can execute it |

## Recovery test status

| Field | Contract |
|---|---|
| **What it means** | Recorded status/date of a real manufacturer-supported or custody-design recovery test |
| **Calculated from** | User-entered completion record; the app does not perform or validate the actual recovery |
| **Edit source** | Protect after the real test |
| **This affects** | Custody readiness and family action list |
| **Primary lesson** | 7.2 |
| **Checkpoint** | `demo-v1-protect` |

## Beneficiary / estate readiness

| Field | Contract |
|---|---|
| **What it means** | Completion status of saved people, beneficiary, document, review-date, and provider-confirmation fields |
| **Calculated from** | Protect records under current completion rules |
| **Edit source** | Protect plus the real attorney/provider record |
| **This affects** | Next estate action, report, family handoff status |
| **Primary lesson** | 8.1 and 8.3 |
| **Checkpoint** | `demo-v1-protect` |
| **Important qualification** | Does not validate state-law documents, court authority, or provider acceptance |

## Insurance / protection gap

| Field | Contract |
|---|---|
| **What it means** | Family need not covered by surviving income, usable assets, verified benefits, and existing coverage under the saved assumptions |
| **Calculated from** | Survivor cash flow, debts, commitments, transition costs, available resources, and actual policy terms |
| **Edit source** | Survivor assumptions and policy records |
| **This affects** | Quote amount, premium, survivor plan, estate liquidity, possible asset sales |
| **Primary lesson** | 8.4 |
| **Checkpoint** | `demo-v1-protect` |
| **Important qualification** | A first-pass gap is not a licensed coverage recommendation |

---

# Scenarios, report, and maintenance

## Scenario delta

| Field | Contract |
|---|---|
| **What it means** | Difference between the saved Baseline result and the same framework with defined Scenario overrides |
| **Calculated from** | Baseline projection compared with Scenario projection under the listed changed inputs |
| **Edit source** | Scenario definition until the household decides; then update the real source page |
| **This affects** | Retirement, cash flow, tax, holdings, debt, reserve, and estate comparison metrics |
| **Primary lesson** | 9.2 |
| **Checkpoint** | `demo-v1-final` |

## Report metric

| Field | Contract |
|---|---|
| **What it means** | Readable summary of a saved source row or projection result at the report date |
| **Calculated from** | Current saved plan, projection, and report assembly rules |
| **Edit source** | Underlying account, holding, debt, income, spending, assumption, event, strategy, or Protect record—not the PDF |
| **This affects** | Household review, professional handoff, annual comparison, action list |
| **Primary lesson** | 9.2 |
| **Checkpoint** | `demo-v1-final` |

## Data freshness / stale result

| Field | Contract |
|---|---|
| **What it means** | Whether the displayed result was generated from the current relevant source inputs and receipt/version under the app's freshness rules |
| **Calculated from** | Input hashes, saved projection/Monte Carlo receipts, timestamps, version checks, and page-specific source data where supported |
| **Edit source** | Update stale source data and rerun the applicable calculation |
| **This affects** | Whether the learner should trust the current output, annual review, AI explanation, report |
| **Primary lesson** | 9.1 and 9.2 |
| **Checkpoint** | Every receipt |

## Encrypted export status

| Field | Contract |
|---|---|
| **What it means** | Whether the encrypted Orange Plan export was created for secure user-managed storage under the current app behavior |
| **Calculated from** | Successful export action and file creation |
| **Edit source** | Data/Privacy export control |
| **This affects** | Secure portability/storage process and annual action list |
| **Primary lesson** | 9.1 and 9.2 |
| **Checkpoint** | `demo-v1-final` |
| **Important qualification** | In-app plan restore is currently unavailable; do not describe the file as presently restorable until the app re-enables and verifies restore |

---

# Walkthrough minimum

The walkthrough does not need to recite every row in this registry.

For the module's primary output, it must say or show:

1. What it means
2. What created it
3. Where the learner changes the source
4. What should move next

Then it verifies the canonical demo value against the checkpoint receipt.

# Maintenance owner

Update this registry when:

- a formula or denominator changes,
- an input is moved or renamed,
- a preview becomes a saved strategy or vice versa,
- a completion rule changes,
- a report/AI source changes,
- a new output becomes important to a learner decision,
- or a professional review changes the interpretation.

A copy change that does not alter meaning can update the walkthrough without changing the concept contract.