# Orange Plan Academy — canonical demo household

**Status:** approved course-owned inputs; app-calculated outputs pending  
**Version:** `demo-v1-inputs`  
**Approved by Austin:** 2026-08-19  
**Engine output authority:** dated receipts from `DEMO-CHECKPOINT-RUN-SHEET.md`

## Why this exists

The Academy uses one continuous fictional household so the learner watches one plan take shape instead of relearning a new example in every lesson.

This file owns the demo inputs. A script, lesson, slide, or walkthrough may not quietly change one of these values. A separate example is allowed only when it is labelled **illustrative — not the demo household**.

The household is fictional. It contains no client data, Austin household data, credentials, or Bitcoin secrets.

## Input versus output

### Course-owned inputs

These are facts or decisions the course deliberately enters. They are approved below.

### Orange Plan outputs

Confidence, earliest retirement date, projected tax, withdrawal sources, Bitcoin sold, reserve refill, Scenario deltas, ending assets, and estate results come from the current app. They remain blank until the accepted checkpoint run.

---

# Household

| Item | Canonical input |
|---|---:|
| Primary adult | Alex, age 45 |
| Spouse | Jordan, age 43 |
| Children | Two, ages 10 and 12 |
| Filing status | Married filing jointly |
| State | Colorado |
| Planning age | 95 |
| Current year | Use the recording year shown in the accepted app build |

# Current cash flow

## Income

| Source | Annual | Monthly | Reliability |
|---|---:|---:|---|
| Alex W-2 salary | $150,000 | $12,500 | Stable |
| Jordan W-2 salary | $40,000 | $3,333 | Stable |
| **Gross household income** | **$190,000** | **$15,833** | — |

## Current outflow and surplus

| Item | Annual | Monthly | App owner |
|---|---:|---:|---|
| Teaching estimate for federal and payroll taxes | $40,000 | $3,333 | App tax engine owns the accepted output |
| Normal living spending, excluding debt payments | $80,000 | $6,667 | Plan / Cash Flow |
| Required debt payments | $22,000 | $1,833 | Debt rows |
| **Reliable surplus available to route** | **$48,000** | **$4,000** | Calculated from the teaching inputs |

Reconciliation:

> $190,000 income − $40,000 taxes − $80,000 living spending − $22,000 debt payments = **$48,000 per year**, or **$4,000 per month**.

The $40,000 tax amount is a clean teaching estimate, not the household's filed return. The accepted app output replaces it when materially different.

## Spending definitions

| Spending value | Amount | Meaning |
|---|---:|---|
| Current normal living spending | $80,000/year | Ordinary working-life spending; debt excluded |
| Bare-bones essentials | $60,000/year · $5,000/month | Temporary minimum during a job loss or emergency |
| Retirement living spending | $100,000/year in today's dollars | Deliberately higher active-retirement lifestyle with more travel and healthcare; debt excluded |

# Current assets and accounts

**Illustrative reference price: $100,000 per BTC.** The app checkpoint records the price actually used.

| Account / holding | Owner | Wrapper | Holding mix | Reference value | Primary job |
|---|---|---|---|---:|---|
| Cash reserve account | Joint | Taxable cash | Cash | $30,000 | Reserve |
| Taxable brokerage | Joint | Taxable | Stocks | $25,000 | Bridge |
| Alex 401(k) | Alex | Traditional | $15,000 stocks + $10,000 bonds | $25,000 | Legacy |
| Jordan Roth IRA | Jordan | Roth | Stocks | $10,000 | Legacy |
| Alex family HSA | Alex | HSA | Stocks | $5,000 | Healthcare Bridge |
| 529 | Children | Education | $20,000 stocks + $5,000 bonds | $25,000 | College |
| Hardware wallet | Joint planning record | Taxable direct Bitcoin | 1.50 BTC | $150,000 | Legacy |
| Exchange operating balance | Alex | Taxable Bitcoin | 0.25 BTC | $25,000 | Purchase / transfer balance |
| **Investable assets** | — | — | $175,000 BTC + $75,000 stocks + $15,000 bonds + $30,000 cash | **$295,000** | — |
| Primary residence | Joint | Real estate | Home | $450,000 | Residence |
| **Gross assets** | — | — | — | **$745,000** | — |

## Current asset mix

| Asset class | Value | Percent of investable assets |
|---|---:|---:|
| Bitcoin | $175,000 | 59.3% |
| Stocks | $75,000 | 25.4% |
| Bonds | $15,000 | 5.1% |
| Cash | $30,000 | 10.2% |
| **Total** | **$295,000** | **100%** |

Bitcoin is 23.5% of gross assets before debt at the illustrative price. The allocation lesson always names the denominator.

# Debt

| Debt | Balance | Rate | Required payment | Remaining structure | Core treatment |
|---|---:|---:|---:|---|---|
| Mortgage | $280,000 | 3.25% fixed | $1,450/month | Approximately 25 years | Required payment only |
| Auto loan | $18,000 | 7.0% fixed | Approximately $383/month | Approximately 4 years | $500/month recurring extra principal |
| **Total** | **$298,000** | — | **Approximately $1,833/month** | — | — |

## Reference debt metrics

| Metric | Calculation | Reference result |
|---|---|---:|
| Net worth | $745,000 assets − $298,000 debt | $447,000 |
| DTI | $1,833 required payments ÷ $15,833 gross monthly income | 11.6% |
| DTA | $298,000 debt ÷ $745,000 gross assets | 40.0% |

DTA changes with live asset values.

## Approved household debt ceiling

- Do not intentionally exceed **25% DTI**.
- Do not add debt when **DTA is 40% or higher**.

These are fictional household rules, not universal product warning lines.

# Reserve

| Input | Approved decision |
|---|---:|
| Bare-bones monthly basis | $5,000 |
| Working target | 6 months |
| Working target amount | $30,000 |
| Current reserve | $30,000 |
| Working status | Fully funded |
| Initial retirement cash-buffer target | 18 months of the selected retirement basis; app calculates the amount |

# Contribution and next-dollar route

The household has **$4,000 per month** available to route. Employer money is not subtracted from that amount.

| Destination | Monthly household dollars | Reason |
|---|---:|---|
| Alex 401(k) employee contribution | $750 | 6% of salary; captures the assumed match |
| Auto-loan extra principal | $500 | Approved 7% debt treatment |
| Alex family HSA | $625 | Qualified healthcare Bridge |
| Jordan Roth IRA | $625 | Long-term tax-free qualified growth |
| Taxable Bridge / investment allocation | $1,500 | Accessible early-retirement funding; holdings follow target and drift |
| **Total** | **$4,000** | Equals reliable surplus |

Employer-match teaching assumption:

- 50% match on the first 6% of Alex's $150,000 salary
- Employee contribution for the full assumed match: $9,000/year or $750/month
- Employer contribution: $4,500/year or $375/month

Reverify recording-year limits, HSA eligibility, and any employer HSA contribution before filming.

# Known future costs and life events

## Vehicle replacement

| Item | Amount |
|---|---:|
| Purchase ceiling | $35,000 in 5 years |
| Expected current-vehicle proceeds | $10,000 |
| Expected purchase-year cash flow | $5,000 |
| Amount to accumulate | $20,000 |

## College — optional lesson

The household keeps an **$80,000 total family commitment across both children**, not unlimited tuition and not $80,000 per child.

| Source | Amount |
|---|---:|
| Existing 529 | $25,000 |
| Parent cash flow during college | $20,000 |
| Student work, aid, or deliberately accepted borrowing | $10,000 |
| Remaining amount to accumulate or fund from assets | $25,000 |
| **Total family commitment** | **$80,000** |

# Cost basis and transaction history

| Quantity | Record status | Basis status |
|---:|---|---|
| 1.25 BTC | Complete acquisition lots | $48,000 known basis |
| 0.40 BTC | Exchange export available | Reconstruction pending |
| 0.10 BTC | Old account history missing | Unknown and visibly unresolved |
| **1.75 BTC** | Quantity reconciles | Tax estimate incomplete until unresolved lots are handled |

# Planning assumptions

| Assumption | Approved input |
|---|---|
| Bitcoin return view | Built-in Power Law |
| Stocks, bonds, cash, and real estate | Current standard app defaults; exact values captured in the checkpoint receipt |
| Baseline inflation | 3% |
| Inflation stress Scenario | 4% |
| Holding override rule | Use only when the broad asset class would model the specific holding incorrectly |
| Plan confidence target | 80% |
| Test runs | 1,000 |
| Planned retirement age | 55 |
| Planning age | 95 |

# Retirement income inputs

| Input | Approved decision |
|---|---:|
| Retirement living spending | $100,000/year in today's dollars |
| Planned retirement age | 55 |
| Plan confidence target | 80% |
| Part-time income | $20,000/year in today's dollars for the first 3 retirement years |
| Alex Social Security | $30,000/year in today's dollars starting when Alex is 67 |
| Jordan Social Security | $22,000/year in today's dollars starting when Jordan is 67, two years after Alex |
| Starting-spending choice | Decide after the Income checkpoint compares the calculated reference amounts with the current $100,000 Plan amount |
| Annual policy defaults | Lower 60% · target 80% · upper 95% · 10% maximum correction |
| Borrowing | Excluded from the saved Core baseline; Advanced comparison only |

## Outputs deliberately blank until the app run

- Confidence at age 55
- Earliest date reaching the 80% target
- Conservative, Balanced, Aggressive, and current-Plan spending results
- First-retirement-year total need
- Taxes and debt costs in that year
- Recurring income in that year
- Total draw
- Account and holding source split
- Bitcoin sold or retained
- Retirement reserve months funded
- Year-by-year tax roadmap
- Conversion comparison
- Ending assets and estate
- Scenario deltas
- Protect readiness

# Custody starting state

| Item | Starting state |
|---|---|
| Long-term balance | 1.50 BTC on one hardware wallet |
| Operating balance | 0.25 BTC at one exchange |
| Recovery | Not tested |
| Device and backup | Same physical failure domain |
| Family knowledge | Alex understands the setup; Jordan has not operated it |
| Exchange security | Strong password; stronger authentication and recovery review still needed |
| Family Custody Map | Incomplete |

Core outcome:

- manufacturer-supported receive, send, and recovery test,
- separated physical, human, and provider failure domains,
- Jordan practices on a small wallet,
- and a process map with no secrets.

# Estate and protection starting state

| Area | Starting state |
|---|---|
| Intended primary beneficiary | Spouse |
| Intended contingent beneficiaries | Children, subject to attorney design for minors |
| Known mismatch | Old workplace retirement account still names a parent |
| Executor and backup | Not confirmed |
| Will | Needs current attorney review |
| Financial power of attorney | Verify |
| Healthcare directive | Verify |
| Heir letter | Incomplete |
| Discovery and delivery paths | Incomplete |
| Insurance terms | Intentionally TBD until real fictional policy inputs are chosen |

# Checkpoint contract

| Checkpoint | Work completed | Required reconciliation |
|---|---|---|
| `demo-v1-baseline` | Household, accounts, debts, income, spending, assumptions, life events, confidence target | Balance sheet, 1.75 BTC, source rows |
| `demo-v1-cashflow` | Spending and reserve settings | $4,000 monthly surplus; $30,000 reserve |
| `demo-v1-debt` | Debt treatments | Payments, DTI, DTA, payoff timing |
| `demo-v1-allocation` | Target, band, jobs, route | Route equals $4,000; no duplicate contribution |
| `demo-v1-tax` | Lots and tax-review status | 1.75 BTC; known and unresolved lots remain separate |
| `demo-v1-income` | Spending, income sources, funding strategy, annual policy | Total draw equals sources; Bitcoin sold agrees everywhere |
| `demo-v1-protect` | Recovery, people, beneficiaries, documents, gaps | App checklist does not overstate real-world proof |
| `demo-v1-final` | Scenarios, report, capstone, PDF, encrypted export | Six-sentence summary agrees with the saved plan |

# Change control

1. Change an approved input here first.
2. Record why it changed and which lessons use it.
3. Update the machine-readable fixture.
4. Rerun affected app checkpoints.
5. Update scripts, lesson text, slides, and walkthroughs from the accepted receipt.
6. Never solve continuity by changing one lesson alone.
