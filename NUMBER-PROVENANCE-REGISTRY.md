# Orange Plan Academy — number provenance registry

**Purpose:** answer the most repeated client question in one maintained place:

> Where did this number come from?

For every important output, the learner should be able to state:

- **WHAT IT MEANS** — the question the number answers
- **CALCULATED FROM** — the source inputs and saved strategy
- **EDIT SOURCE** — where the real source changes
- **THIS AFFECTS** — what should move downstream

The current app code and accepted checkpoint receipt own exact implementation and displayed values. This registry owns the durable explanation.

## Current demo references

**Fixture:** `demo-v1-inputs`  
**Engine candidate:** app commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Visual values:** `demo/VISUAL-DATA-RECEIPT-3105664.md`  
**UI evidence:** `demo/UI-ACCEPTANCE-CHECKLIST-3105664.md`

The candidate values can support scripts and concept visuals. Final screenshot-level claims still require the deployed page to confirm label, rounding, source rows, and Saved / Previewing / Scenario state.

## Use rules

1. A concept lesson explains the relationship.
2. A walkthrough points to the current source and state.
3. A receipt proves the fictional value for a specific app build.
4. A tooltip or AI explanation may use this same structure.
5. Do not imply every output maps to one database field.
6. Correct an upstream input or deliberately change a decision; do not manipulate an output until it looks better.
7. Name the denominator whenever a percentage can be calculated more than one reasonable way.
8. Distinguish app checklist status from real-world proof.
9. Rerun the affected checkpoint when a formula, inclusion rule, save model, or important label changes.

---

# Baseline and retirement timing

## Net worth / current position

| Field | Contract |
|---|---|
| **What it means** | Current included assets minus current included liabilities |
| **Calculated from** | Active accounts, holdings, manual asset values, and active debt balances |
| **Edit source** | Accounts, holdings, assets, and Debt |
| **This affects** | Current-position summary, DTA, plan funding, report, estate context |
| **Primary lessons** | 1.1 and 9.2 |
| **Checkpoint** | `demo-v1-baseline` |
| **Candidate** | $745,000 gross assets − $298,000 debt = $447,000 reference net worth |
| **Qualification** | Net worth, gross assets, financial balances, and app Allocation scope are different denominators |

## Planned retirement age / household retirement date

| Field | Contract |
|---|---|
| **What it means** | The household retirement start the learner asked Orange Plan to test, displayed using the primary person's age |
| **Calculated from** | Saved Plan age/date and the primary person's birth date |
| **Edit source** | Plan → Retirement |
| **This affects** | Household earned-income transition, contribution years, withdrawal start, partial-year income, confidence, earliest-date search, taxes |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Candidate** | March 2036 · Alex age 55 |
| **Qualification** | Current demo has one household retirement date, not a separate spouse-retirement-age setting; each spouse's Social Security still has its own date |

## Baseline retirement spending

| Field | Contract |
|---|---|
| **What it means** | Annual living spending the retirement plan is expected to support in the app's stated dollar basis |
| **Calculated from** | Saved Plan spending, inflation, and dated life events; tax, Debt, and refill remain separate when the page shows them separately |
| **Edit source** | Plan spending and the specific life event |
| **This affects** | Confidence, earliest date, spending references, total need, total draw, tax, sales, reserve basis when selected |
| **Primary lessons** | 1.3 and 6.1 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-income` |
| **Candidate** | $100,000/year in today's dollars |
| **Qualification** | Do not duplicate debt or a dated life event inside annual living spending |

## Plan confidence target

| Field | Contract |
|---|---|
| **What it means** | Minimum share of test runs required before a retirement date qualifies as the earliest date |
| **Calculated from** | Learner-selected target; allowed range and default are current product facts |
| **Edit source** | Plan → Retirement |
| **This affects** | Earliest target-qualified date and verdict/target copy; it does not rewrite the planned age |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Candidate** | 80% |
| **Qualification** | Separate from starting-spending choices and annual spending guardrails on Income |

## Plan confidence result

| Field | Contract |
|---|---|
| **What it means** | Share of the 1,000 test runs where the saved plan remained funded through planning age |
| **Calculated from** | Entire saved projection: balances, holdings, returns, inflation, household income transition, spending, debts, life events, taxes, contributions, retirement timing, and saved strategies |
| **Edit source** | The underlying input or strategy that is wrong or deliberately being tested; there is no direct “increase confidence” field |
| **This affects** | Plan verdict, earliest target-qualified date, Scenario comparisons, spending choices, annual review |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Candidate** | 94.6% at Alex age 55 |
| **Qualification** | Not a guarantee, grade, literal bankruptcy probability, or separate deterministic result |

## Earliest target-qualified date

| Field | Contract |
|---|---|
| **What it means** | First retirement month where confidence reaches or exceeds the selected Plan target |
| **Calculated from** | The same test-run framework evaluated across possible household retirement dates |
| **Edit source** | Confidence target and underlying plan inputs/decisions—not the displayed date |
| **This affects** | Retirement-timing decision, Scenario comparison, report, action plan |
| **Primary lesson** | 1.3 |
| **Checkpoint** | `demo-v1-baseline` |
| **Candidate** | May 2032 · Alex age 51 · 80.0% boundary confidence |
| **Qualification** | Creates an option; does not automatically replace the saved age-55 plan |

---

# Cash Flow and Reserve

## Gross income

| Field | Contract |
|---|---|
| **What it means** | Current recurring household income before modeled tax |
| **Calculated from** | Active income sources, amounts, frequency, owner, dates, and recurring/one-time treatment |
| **Edit source** | Income / Cash Flow source rows |
| **This affects** | Tax, Cash Flow capacity, DTI, contributions, confidence, retirement timing |
| **Primary lessons** | 1.1 and 2.1 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-cashflow` |
| **Candidate** | $190,000/year |

## Estimated current taxes

| Field | Contract |
|---|---|
| **What it means** | App estimate of current included federal, payroll, state, and other tax for the modeled year or Cash Flow view |
| **Calculated from** | Filing status, state, income types, modeled deductions/settings, and current tax configuration |
| **Edit source** | Household/tax settings and income sources; payment/withholding overrides when supported |
| **This affects** | Decision capacity, displayed surplus, route, report, later tax comparisons |
| **Primary lessons** | 2.1 and 5.2 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | $36,862/year |
| **Qualification** | Planning estimate, not a filed return. The course may use a clearly labelled $40,000 round teaching amount for the simple equation, but the walkthrough uses the current page result |

## Normal living spending

| Field | Contract |
|---|---|
| **What it means** | Recurring current living costs outside separately modeled Debt |
| **Calculated from** | Saved spending input and, when used, transaction review/exclusions |
| **Edit source** | Cash Flow / Plan spending and transaction review |
| **This affects** | Decision capacity, reserve basis when selected, retirement spending, confidence, earliest date |
| **Primary lesson** | 2.1 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | $80,000/year |

## Bare-bones spending

| Field | Contract |
|---|---|
| **What it means** | Temporary minimum living cost during an emergency or reduced-spending period |
| **Calculated from** | Learner-selected essential-spending input |
| **Edit source** | Cash Flow → Reserve settings |
| **This affects** | Reserve target, survival time, retirement cash-buffer planning |
| **Primary lessons** | 2.1 and 2.2 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | $5,000/month |

## Required debt payments

| Field | Contract |
|---|---|
| **What it means** | Contractual current payments for active debts before optional extra principal |
| **Calculated from** | Debt rows, payment amount/frequency, payoff schedule, and active status |
| **Edit source** | Debt records |
| **This affects** | Decision capacity, DTI, payoff, retirement-year need, confidence |
| **Primary lessons** | 2.1 and 3.1 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-debt` |
| **Candidate** | About $1,833/month |
| **Qualification** | Keep out of living spending when Debt already owns the payment |

## Saved extra debt

| Field | Contract |
|---|---|
| **What it means** | Recurring extra principal the household deliberately added beyond the required payment |
| **Calculated from** | Saved Debt strategy |
| **Edit source** | Debt treatment |
| **This affects** | Planned Debt shown in Cash Flow, post-debt surplus, payoff date, interest, later route |
| **Primary lessons** | 3.1 and 4.3 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-debt` |
| **Candidate** | $500/month to the auto loan |
| **Qualification** | Once included in Cash Flow's Debt row, it cannot be routed again from the displayed post-debt surplus |

## Decision capacity before extra debt

| Field | Contract |
|---|---|
| **What it means** | Recurring amount available after modeled tax, living spending, and required debt, before the saved extra-principal decision |
| **Calculated from** | Income − modeled tax − living spending − required debt |
| **Edit source** | Income, tax, spending, and required Debt sources |
| **This affects** | Extra-debt choice, post-debt surplus, total household next-dollar decision |
| **Primary lessons** | 2.1 and 4.3 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | About $4,261/month |

## Reliable surplus / displayed post-debt surplus

| Field | Contract |
|---|---|
| **What it means** | Amount left for account routing and cushion after the current saved Debt treatment |
| **Calculated from** | Decision capacity before extra debt − saved extra principal |
| **Edit source** | Underlying source rows and Debt strategy—not the displayed surplus |
| **This affects** | Account contributions, operating cushion, future balances, confidence, earliest date |
| **Primary lessons** | 2.1 and 4.3 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | About $3,761/month |
| **Qualification** | The full household decision can still be $4,000 when it means $500 extra debt + $3,500 account contributions |

## Account contribution route

| Field | Contract |
|---|---|
| **What it means** | Assignment of the post-debt surplus to accounts and goals |
| **Calculated from** | Employer benefit, account eligibility, Bridge/Legacy needs, tax plan, and target allocation |
| **Edit source** | Cash Flow routing/contribution controls and real provider elections |
| **This affects** | Account growth, accessibility, tax path, allocation drift, confidence |
| **Primary lesson** | 4.3 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-allocation` |
| **Candidate** | $3,500/month: $750 401(k), $625 HSA, $625 Roth IRA, $1,500 taxable Bridge |
| **Qualification** | Employer match is separate employer money; taxable Bridge follows target/drift and is not an automatic Bitcoin purchase |

## Operating cushion

| Field | Contract |
|---|---|
| **What it means** | Cash Flow amount left after the saved post-debt account route |
| **Calculated from** | Displayed post-debt surplus − account contribution route |
| **Edit source** | Underlying Cash Flow sources and routing plan |
| **This affects** | Bill timing, transfer reliability, need to reverse contributions, future route review |
| **Primary lesson** | 2.1 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | About $261/month |

## Reserve target amount

| Field | Contract |
|---|---|
| **What it means** | Cash amount selected to protect a period without normal income or portfolio sales |
| **Calculated from** | Selected monthly spending basis × target months |
| **Edit source** | Cash Flow → Reserve settings |
| **This affects** | Reserve funding gap, routing, retirement cash-buffer plan |
| **Primary lesson** | 2.2 |
| **Checkpoint** | `demo-v1-cashflow` |
| **Candidate** | $5,000 × 6 = $30,000 |

## Reserve months funded

| Field | Contract |
|---|---|
| **What it means** | Current reserve-designated amount expressed in months of the selected spending basis |
| **Calculated from** | Included reserve holdings ÷ selected monthly basis |
| **Edit source** | Reserve-designated holdings, basis, and target settings |
| **This affects** | Readiness, routing, refill, forced-sale risk |
| **Primary lessons** | 2.2 and 6.1 |
| **Checkpoint** | `demo-v1-cashflow` and `demo-v1-income` |
| **Candidate** | $30,000 / $5,000 = 6 months · fully funded |

## Known future-cost funding gap

| Field | Contract |
|---|---|
| **What it means** | Part of a committed future cost that still lacks a source |
| **Calculated from** | Commitment − dedicated savings − expected cash flow − expected proceeds − accepted financing |
| **Edit source** | Life event and dedicated account/contribution plan |
| **This affects** | Current route, Bridge need, future withdrawals, confidence, earliest date |
| **Primary lessons** | 2.3 and 2.4 |
| **Checkpoint** | `demo-v1-baseline` and `demo-v1-allocation` |
| **Candidate** | Vehicle: $20,000 remaining; college: $25,000 remaining within an $80,000 total-family commitment |

---

# Debt

## Debt-to-income (DTI)

| Field | Contract |
|---|---|
| **What it means** | Share of gross monthly income committed to included required monthly debt payments |
| **Calculated from** | Required payments ÷ gross monthly income |
| **Edit source** | Debt payment rows and income sources |
| **This affects** | Cash-flow pressure, debt band, borrowing room, household ceiling review |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |
| **Candidate** | 11.6% |
| **Qualification** | Household ceiling can be lower than the app's general bands |

## Debt-to-assets (DTA)

| Field | Contract |
|---|---|
| **What it means** | Included debt compared with current included gross asset values |
| **Calculated from** | Active debt balances ÷ included current asset values |
| **Edit source** | Debt and asset/holding records |
| **This affects** | Balance-sheet pressure, debt band, new borrowing decision |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |
| **Candidate** | 40.0% at the $745,000 gross-asset reference valuation |
| **Qualification** | Can change quickly with Bitcoin price even when debt barely changes; name the denominator |

## Projected payoff date

| Field | Contract |
|---|---|
| **What it means** | Modeled date a debt reaches zero under saved payment assumptions |
| **Calculated from** | Balance, rate, required payment, recurring extra principal, lump sums, and timing |
| **Edit source** | Debt terms and strategy |
| **This affects** | Future Cash Flow, routing after payoff, retirement-year debt, confidence |
| **Primary lesson** | 3.1 |
| **Checkpoint** | `demo-v1-debt` |
| **Candidate** | Auto loan: 2027 · Alex age 46 |

## Bitcoin-loan LTV, when applicable

| Field | Contract |
|---|---|
| **What it means** | Loan balance relative to the current pledged-collateral value under the lender/app definition |
| **Calculated from** | Loan balance ÷ pledged Bitcoin value plus lender-specific call/top-up/liquidation rules |
| **Edit source** | Loan record, collateral, and actual lender terms |
| **This affects** | Margin call, liquidation, top-up need, borrowing capacity, estate liability |
| **Primary lesson** | Advanced loan lesson; named in 3.1 and 6.2 only when relevant |
| **Checkpoint** | Optional Advanced receipt |

---

# Allocation and contributions

## Current asset mix

| Field | Contract |
|---|---|
| **What it means** | Combined exposure by holding type across the accounts included in the chosen scope |
| **Calculated from** | Current holdings and values grouped by the app's asset classes |
| **Edit source** | Accounts, holdings, classification, and price source |
| **This affects** | Allocation, drawdown, drift, projections, account location, report |
| **Primary lessons** | 4.1 and 4.2 |
| **Checkpoint** | `demo-v1-allocation` |

## App Allocation denominator

| Field | Contract |
|---|---|
| **What it means** | Holdings currently included in the household target-allocation calculation |
| **Calculated from** | Included financial holdings after the current exclusion rules |
| **Edit source** | Account/holding records, beneficiary restrictions, primary-residence flag, and app inclusion rules |
| **This affects** | Current percentage, drift, band state, contribution direction, drawdown percentage |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Candidate** | $270,000; excludes $25,000 529 and $450,000 primary residence |
| **Qualification** | Broader financial balances ($295,000) and gross assets ($745,000) answer different questions |

## Current Bitcoin percentage

| Field | Contract |
|---|---|
| **What it means** | Bitcoin exposure as a share of the app Allocation denominator |
| **Calculated from** | Included direct/indirect Bitcoin value ÷ app allocatable portfolio |
| **Edit source** | Holdings, classifications, price, and inclusion rules |
| **This affects** | Drift, review state, route, drawdown, custody stakes, confidence |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Candidate** | $175,000 ÷ $270,000 = 64.8% |

## Target allocation

| Field | Contract |
|---|---|
| **What it means** | Household's chosen long-term mix within the app Allocation scope |
| **Calculated from** | Saved learner decision under current validation rules |
| **Edit source** | Allocation target editor |
| **This affects** | Drift, band state, contribution direction, previews, account instructions |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Candidate** | 50% Bitcoin |
| **Qualification** | Target is not automatically today's trade |

## Allocation drift / review state

| Field | Contract |
|---|---|
| **What it means** | Difference between current and target exposure and whether that difference is inside the household's review band |
| **Calculated from** | Current mix compared with target and lower/upper band |
| **Edit source** | Holdings/current values, target, and band |
| **This affects** | Review state, contribution direction, one-time preview |
| **Primary lessons** | 4.1 and 4.3 |
| **Checkpoint** | `demo-v1-allocation` |
| **Candidate** | 64.8% current vs 50% target and 40–60% band · above band |
| **Qualification** | Above band means review, not automatic sale |

## Bitcoin drawdown hit

| Field | Contract |
|---|---|
| **What it means** | Approximate current dollar loss attributable to the selected Bitcoin decline before other holdings move |
| **Calculated from** | Bitcoin value × selected decline; percentage of portfolio depends on the named denominator |
| **Edit source** | Holdings, price, and selected stress percentage |
| **This affects** | Holdability, reserve, debt/collateral risk, target realism, custody consequence |
| **Primary lesson** | 4.1 |
| **Checkpoint** | `demo-v1-allocation` |
| **Candidate** | $175,000 × 75% = $131,250; app allocatable portfolio falls to $138,750 if other holdings stay flat |

## Reserve / Bridge / Legacy funding

| Field | Contract |
|---|---|
| **What it means** | Money assigned to near-, medium-, and long-term jobs compared with their needs |
| **Calculated from** | Account/holding jobs, reserve, future costs, and year-by-year retirement Bridge |
| **Edit source** | Allocation/jobs, life events, Cash Flow, Retirement Income |
| **This affects** | Contribution route, access, forced-sale risk |
| **Primary lesson** | 4.2 |
| **Checkpoint** | `demo-v1-allocation` and `demo-v1-income` |

---

# Tax

## Bitcoin quantity covered by tax lots

| Field | Contract |
|---|---|
| **What it means** | Current taxable Bitcoin quantity explained by acquisition/disposition history |
| **Calculated from** | Acquisition lots minus supported dispositions and ownership-changing events |
| **Edit source** | Transaction import, lots, and transfer matching |
| **This affects** | Basis completeness, sale comparison, tax confidence, lot selection |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |
| **Candidate** | Total quantity 1.75 BTC; 1.25 complete, 0.40 reconstruction pending, 0.10 unknown |

## Known cost basis

| Field | Contract |
|---|---|
| **What it means** | Supported tax investment in the units still owned |
| **Calculated from** | Acquisition lots, permitted costs, and supported adjustments/dispositions |
| **Edit source** | Transaction and lot records—not market value |
| **This affects** | Gain/loss, projected tax, net proceeds, sell/borrow comparison, withdrawal planning |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |
| **Candidate** | $48,000 in 1.25 BTC |
| **Qualification** | Unknown basis remains unknown; a zero-basis planning stress is not automatically the filing position |

## Unrealized gain

| Field | Contract |
|---|---|
| **What it means** | Current market value minus known basis for the included units |
| **Calculated from** | Current quantity/value and known lot basis |
| **Edit source** | Holding/price and lot records |
| **This affects** | Sale estimate and lot comparison; it does not create tax by itself |
| **Primary lesson** | 5.1 |
| **Checkpoint** | `demo-v1-tax` |

## Projected tax by year

| Field | Contract |
|---|---|
| **What it means** | App estimate of federal and state tax from modeled income and transactions in each year |
| **Calculated from** | Filing status, state, ordinary income, gains/losses, modeled deductions, Social Security, pension, withdrawals, conversions, and included items |
| **Edit source** | Tax/household settings and underlying income, basis, event, contribution, conversion, and withdrawal strategy |
| **This affects** | Cash Flow, total retirement need, total draw, source mix, confidence, earliest date |
| **Primary lessons** | 5.2 and 6.1 |
| **Checkpoint** | `demo-v1-tax` and `demo-v1-income` |
| **Candidate** | Current year $36,862; first retirement year $10,632 |
| **Qualification** | Planning estimate, not a filed return; incomplete basis and current-law details remain professionally qualified |

## Traditional balance at required-distribution stage

| Field | Contract |
|---|---|
| **What it means** | Projected traditional balance exposed to applicable future distribution rules |
| **Calculated from** | Current balance, contributions, returns, withdrawals, conversions, and applicable start age |
| **Edit source** | Traditional account records and contribution/withdrawal/conversion strategy |
| **This affects** | Future taxable income, conversion-window value, Medicare-related costs, flexibility |
| **Primary lesson** | 5.2 |
| **Checkpoint** | `demo-v1-tax` |
| **Qualification** | Applicable age depends on current law and birth year; keep the current table out of evergreen video |

## Roth-conversion comparison

| Field | Contract |
|---|---|
| **What it means** | Difference between Baseline and a defined conversion amount/timing under the model |
| **Calculated from** | Conversion schedule plus current/future income, tax, account, Social Security, and withdrawal effects |
| **Edit source** | Conversion preview/strategy and underlying tax inputs |
| **This affects** | Current tax, Roth/traditional balances, future RMDs, withdrawals, estate, confidence |
| **Primary lesson** | Advanced; window identified in 5.2 |
| **Checkpoint** | `demo-v1-tax` |
| **Qualification** | App comparison does not execute the conversion or determine the filed amount |

---

# Retirement Income

## Recurring retirement income

| Field | Contract |
|---|---|
| **What it means** | Modeled income arriving in the selected year without portfolio sales |
| **Calculated from** | Partial-year household wages when retirement begins midyear, part-time work, Social Security, pension, rental/other sources, owner, and dates |
| **Edit source** | Household retirement date and underlying income records |
| **This affects** | Living gap, Bridge, total draw, tax, reserve need |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | First retirement year: $42,557 partial-year wages + $26,878 part-time = $69,435 |

## Portfolio-funded living gap

| Field | Contract |
|---|---|
| **What it means** | Retirement living spending not covered by recurring income before separate tax, debt, events, or refill |
| **Calculated from** | Retirement living spending − recurring income in that year |
| **Edit source** | Plan spending and income records |
| **This affects** | Bridge need and full total draw |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate stages in today's dollars** | $80,000 during part-time years; $100,000 after part-time; $70,000 after Alex SS; $48,000 after both SS benefits |

## First-year total need

| Field | Contract |
|---|---|
| **What it means** | Full modeled cash requirement for the selected retirement calendar year before recurring income is subtracted |
| **Calculated from** | Inflation-adjusted living spending + dated events + tax + remaining Debt + refill/other included costs |
| **Edit source** | Underlying Plan, event, tax, Debt, and reserve sources |
| **This affects** | Total draw and funding sources |
| **Primary lesson** | 6.1 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | $129,912 living + $13,439 college + $17,400 Debt + $10,632 tax = $171,383 |

## Total draw

| Field | Contract |
|---|---|
| **What it means** | Amount the projection needs from accounts after recurring income |
| **Calculated from** | Total need − recurring income under the current projection |
| **Edit source** | Underlying need/income sources and saved strategy—not the displayed draw |
| **This affects** | Account withdrawals, holding sales, Bitcoin sold, tax, reserve, debt/loan, confidence |
| **Primary lessons** | 6.1 and 6.2 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | $171,383 − $69,435 = $101,948 |

## Account and holding source split

| Field | Contract |
|---|---|
| **What it means** | Accounts and holdings funding the total draw under the saved strategy |
| **Calculated from** | Draw, account access, phases, account/asset order, available holdings, tax strategy, and borrowing policy when applicable |
| **Edit source** | Withdrawal phases, account strategy, asset strategy, holdings, and optional borrowing policy |
| **This affects** | Tax, Bitcoin sold, account balances, refill, estate, confidence |
| **Primary lesson** | 6.2 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | Taxable accounts: about $2,200 cash + $1,800 stocks + $97,900 Bitcoin = $101,946 rounded |
| **Required reconciliation** | Source amounts equal the same total draw within visible rounding |

## Bitcoin sold or retained

| Field | Contract |
|---|---|
| **What it means** | Engine-calculated Bitcoin sale/retention for the year in dollars and units |
| **Calculated from** | Remaining draw after other sources, saved strategy, available Bitcoin, and modeled price for that year |
| **Edit source** | Holdings and retirement funding strategy—not the displayed sale total |
| **This affects** | Capital gain, tax, future Bitcoin balance, custody exposure, estate, possible borrowing need |
| **Primary lesson** | 6.2 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | $97,948 proceeds ÷ $1,235,921 projected price = 0.079251 BTC |
| **Required reconciliation** | Dollars, projected price, units, funding card, chart, report, and receipt agree |

## Retirement-spending reference amount

| Field | Contract |
|---|---|
| **What it means** | Annual starting spending supported near a selected reference confidence under the current strategy |
| **Calculated from** | Spending search using the current test-run framework, assumptions, and funding strategy |
| **Edit source** | Underlying Plan inputs and strategy; the reference amount is calculated |
| **This affects** | Starting-paycheck decision, total need, draw, sales, tax, reserve use, long-term result |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | Conservative $99,317; Balanced $170,216; Aggressive $249,904 |
| **Qualification** | Choices, not personality labels or instructions to maximize spending |

## Current Plan spending confidence

| Field | Contract |
|---|---|
| **What it means** | Test-run result associated with the saved Baseline retirement-spending amount under the current strategy |
| **Calculated from** | Current Plan spending evaluated on the same retirement-spending framework |
| **Edit source** | Baseline spending and underlying plan/strategy |
| **This affects** | Comparison with reference choices and starting-paycheck decision |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` |
| **Candidate** | $100,000 at 94.6%; saved demo paycheck remains $100,000 |
| **Qualification** | Separate from Plan confidence used to find the earliest date, even when the percentages happen to match |

## Annual spending-policy update

| Field | Contract |
|---|---|
| **What it means** | Suggested paycheck for the next annual policy period |
| **Calculated from** | Prior target, inflation, latest confidence, target-confidence amount, triggers, and correction cap |
| **Edit source** | Spending policy and current underlying inputs |
| **This affects** | Next-year need, draw, sources, sales, reserve refill |
| **Primary lesson** | 6.3 |
| **Checkpoint** | `demo-v1-income` and future annual-review receipt |
| **Candidate policy** | Lower 60% · target 80% · upper 95% · up to 10% correction |
| **Qualification** | Cap is a maximum; annual policy review, not a market-timing signal |

## Loan balance at death, when borrowing is used

| Field | Contract |
|---|---|
| **What it means** | Projected outstanding borrowing liability at the plan/end-of-life point |
| **Calculated from** | Draw schedule, interest, repayment, collateral events, lender assumptions, and timeline |
| **Edit source** | Borrowing policy and actual lender terms |
| **This affects** | Estate, collateral, repayment, liquidation, counterparty risk |
| **Primary lesson** | Advanced borrowing; comparison named in 6.2 |
| **Checkpoint** | Optional Advanced receipt |

---

# Protect

## Custody readiness

| Field | Contract |
|---|---|
| **What it means** | Completion status of custody-process fields and checklist saved in Protect |
| **Calculated from** | Custody type, people, documents, dates, and required checklist items under app rules |
| **Edit source** | Protect records |
| **This affects** | Next action, report, family handoff status |
| **Primary lessons** | 7.1–7.3 |
| **Checkpoint** | `demo-v1-protect` |
| **Qualification** | Does not prove the backup is accurate, recovery worked, or family can execute |

## Recovery test status

| Field | Contract |
|---|---|
| **What it means** | Recorded status/date of a real supported recovery test |
| **Calculated from** | User-entered completion record; the app does not validate the actual device recovery |
| **Edit source** | Protect after the real test |
| **This affects** | Custody readiness and action list |
| **Primary lesson** | 7.2 |
| **Checkpoint** | `demo-v1-protect` |

## Beneficiary / estate readiness

| Field | Contract |
|---|---|
| **What it means** | Completion status of saved people, beneficiary, document, review-date, and provider-confirmation fields |
| **Calculated from** | Protect records under current completion rules |
| **Edit source** | Protect plus real attorney/provider records |
| **This affects** | Next estate action, report, family handoff status |
| **Primary lessons** | 8.1 and 8.3 |
| **Checkpoint** | `demo-v1-protect` |
| **Qualification** | Does not validate state-law documents, court authority, or provider acceptance |

## Insurance / protection gap

| Field | Contract |
|---|---|
| **What it means** | Family need not covered by surviving income, usable assets, verified benefits, and existing coverage |
| **Calculated from** | Survivor Cash Flow, Debt, commitments, transition costs, resources, and actual policy terms |
| **Edit source** | Survivor assumptions and policy records |
| **This affects** | Quote amount, premium, survivor plan, estate liquidity, asset sales |
| **Primary lesson** | 8.4 |
| **Checkpoint** | `demo-v1-protect` |
| **Qualification** | A first-pass annual gap is not a licensed coverage recommendation |

---

# Scenarios, report, and maintenance

## Scenario delta

| Field | Contract |
|---|---|
| **What it means** | Difference between the saved Baseline result and the same framework with defined Scenario overrides |
| **Calculated from** | Baseline projection compared with Scenario projection under the listed changed inputs |
| **Edit source** | Scenario definition until the household decides; then update the real source page |
| **This affects** | Retirement, Cash Flow, tax, holdings, Debt, reserve, and estate comparison metrics |
| **Primary lesson** | 9.2 |
| **Checkpoint** | `demo-v1-final` |
| **Candidate** | 4% inflation: 91.6% vs 3% Baseline 94.6% = −3.0 percentage points |
| **Qualification** | Do not invent an earliest-date or estate delta the comparison does not show |

## Report metric

| Field | Contract |
|---|---|
| **What it means** | Readable summary of a saved source or projection result at the report date |
| **Calculated from** | Current saved plan, projection, and report assembly rules |
| **Edit source** | Underlying account, holding, Debt, income, spending, assumption, event, strategy, or Protect record—not the PDF |
| **This affects** | Household review, professional handoff, annual comparison, action list |
| **Primary lesson** | 9.2 |
| **Checkpoint** | `demo-v1-final` |

## Data freshness / stale result

| Field | Contract |
|---|---|
| **What it means** | Whether the displayed result was generated from current relevant source inputs and app/version state |
| **Calculated from** | Input hashes, receipts, timestamps, version checks, and page-specific source data when supported |
| **Edit source** | Update stale sources and rerun the applicable calculation |
| **This affects** | Whether the learner should trust the current output, annual review, AI explanation, report |
| **Primary lessons** | 9.1 and 9.2 |
| **Checkpoint** | Every receipt |

## Encrypted export status

| Field | Contract |
|---|---|
| **What it means** | Whether a passphrase-protected Orange Plan export was created for secure user-managed storage and portability |
| **Calculated from** | Successful export action and file creation |
| **Edit source** | Data/Privacy export control |
| **This affects** | Annual record and storage process |
| **Primary lessons** | 9.1 and 9.2 |
| **Checkpoint** | `demo-v1-final` |
| **Qualification** | In-app plan restore is currently unavailable; do not describe the file as presently restorable until the product re-enables and verifies restore |

---

# Walkthrough minimum

The walkthrough does not recite every row in this registry.

For the module's primary output, it must show:

1. what it means,
2. what created it,
3. where the learner changes the source,
4. what should move next,
5. and whether the page shows Saved, Previewing, Scenario, or read-only state.

Then it verifies the fictional value against the accepted receipt.

# Maintenance owner

Update this registry when:

- a formula or denominator changes,
- an inclusion/exclusion rule changes,
- an input moves or is renamed,
- a preview becomes a saved strategy or vice versa,
- a household versus spouse timing rule changes,
- a completion rule changes,
- a report/AI source changes,
- a new output becomes important to a learner decision,
- or a professional review changes the interpretation.

A copy change that does not alter meaning can update the walkthrough without changing the concept contract.
