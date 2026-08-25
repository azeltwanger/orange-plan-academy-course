# Orange Plan Academy — canonical demo household

**Status:** approved inputs; reconciled engine candidate generated; deployed UI receipts pending  
**Version:** `demo-v1-inputs`  
**Approved by Austin:** 2026-08-19  
**Engine candidate:** app commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Final output authority:** accepted receipts under `demo/` and `DEMO-CHECKPOINT-RUN-SHEET.md`

## Why this exists

The Academy uses one continuous fictional household so the learner watches one plan take shape instead of relearning a new example in every lesson.

This file owns the demo inputs and the accepted interpretation of app outputs. A script, lesson, visual, or walkthrough may not quietly change one value. A separate example is allowed only when it is labelled **illustrative — not the demo household**.

The household is fictional. It contains no client data, Austin household data, credentials, or Bitcoin secrets.

## Input versus output

Course-owned facts and decisions are approved below. Orange Plan owns confidence, earliest date, tax, allocation scope, payoff timing, withdrawal sources, Bitcoin sold, Scenario deltas, and other projection outputs.

The current reconciled engine candidate is `demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md`. It can be used to finish scripts and production briefs. The deployed interface still has to verify the visible label, rounding, save/preview state, and screenshot evidence before a final receipt is accepted.

---

# Household

| Item | Canonical input |
|---|---:|
| Primary adult | Alex, age 45 |
| Spouse | Jordan, age 43 |
| Children | Two, ages 10 and 12 |
| Filing status | Married filing jointly |
| State | Colorado |
| Household retirement start | When Alex is 55 |
| Planning age | 95 |
| Current year | Use the recording year shown in the accepted app build |

The current app has one household retirement date anchored to the primary person's age. Jordan does not have a separate retirement-age input in this saved plan. A March retirement date leaves partial-year household wages before retirement begins. Each spouse's Social Security still has its own start age.

# Current cash flow

## Income

| Source | Annual | Monthly | Reliability |
|---|---:|---:|---|
| Alex W-2 salary | $150,000 | $12,500 | Stable |
| Jordan W-2 salary | $40,000 | $3,333 | Stable |
| **Gross household income** | **$190,000** | **$15,833** | — |

## Current source rows and routing

| Item | Annual / monthly result | Status |
|---|---:|---|
| Round teaching tax estimate | $40,000/year | Used only for the simple equation |
| Reconciled engine tax | $36,862/year | UI receipt pending |
| Normal living spending, debt excluded | $80,000/year | Approved input |
| Required debt payments | Approximately $1,833/month | Approved debt rows |
| Saved extra auto principal | $500/month | Included in Cash Flow planned debt |
| Decision capacity before extra debt | Approximately $4,261/month | Engine candidate |
| Displayed surplus after planned debt | Approximately $3,761/month | Engine candidate |
| Contribution route after debt | $3,500/month | Approved decision |
| Operating cushion after route | Approximately $261/month | Engine candidate |

The round teaching reconciliation remains:

> $190,000 income − $40,000 tax − $80,000 living spending − $22,000 required debt payments = $48,000/year, or $4,000/month.

The full household route is still $4,000/month:

> $500 extra debt + $3,500 account contributions = $4,000.

The app's post-debt headline is lower because the $500 extra principal is already inside the Debt row. Do not subtract or route it a second time.

## Spending definitions

| Spending value | Amount | Meaning |
|---|---:|---|
| Current normal living spending | $80,000/year | Ordinary working-life spending; debt excluded |
| Bare-bones essentials | $60,000/year · $5,000/month | Temporary minimum during a job loss or emergency |
| Retirement living spending | $100,000/year in today's dollars | Deliberately higher active-retirement lifestyle with more travel and healthcare; debt excluded |

# Current assets and accounts

**Illustrative reference price: $100,000 per BTC.** The accepted app receipt records the price and date used.

| Account / holding | Owner | Holding mix | Reference value | Job | Allocation scope |
|---|---|---|---:|---|---|
| Cash reserve account | Joint | Cash | $30,000 | Reserve | Included |
| Taxable brokerage | Joint | Stocks | $25,000 | Bridge | Included |
| Alex 401(k) | Alex | $15,000 stocks + $10,000 bonds | $25,000 | Legacy | Included |
| Jordan Roth IRA | Jordan | Stocks | $10,000 | Legacy | Included |
| Alex family HSA | Alex | Stocks | $5,000 | Healthcare Bridge | Included |
| 529 | Children | $20,000 stocks + $5,000 bonds | $25,000 | College | **Excluded: beneficiary-restricted** |
| Hardware wallet | Joint planning record | 1.50 BTC | $150,000 | Legacy | Included |
| Exchange operating balance | Alex | 0.25 BTC | $25,000 | Operating balance | Included |
| Primary residence | Joint | Home | $450,000 | Residence | Excluded |

## Three useful denominators

| Scope | Amount | Bitcoin percentage | Question answered |
|---|---:|---:|---|
| **Allocatable portfolio used by Orange Plan** | **$270,000** | **64.8%** | What mix is managed toward the household target? |
| Financial balances including the 529 | $295,000 | 59.3% | How much financial wealth exists, including college money? |
| Gross assets including the home | $745,000 | 23.5% | How concentrated is the entire balance sheet before debt? |

The Allocation page excludes the primary residence and beneficiary-restricted 529. The household is above its approved 40–60% Bitcoin review band. That triggers a review, not an automatic taxable sale.

## Drawdown reference

| Scope | Result after a 75% Bitcoin decline, other holdings flat |
|---|---:|
| Bitcoin loss | $131,250 |
| Allocatable portfolio | $138,750 |
| Financial balances including the 529 | $163,750 |

# Debt

| Debt | Balance | Rate | Required payment | Core treatment |
|---|---:|---:|---:|---|
| Mortgage | $280,000 | 3.25% fixed | $1,450/month | Required payment only |
| Auto loan | $18,000 | 7.0% fixed | Approximately $383/month | $500/month recurring extra principal |
| **Total** | **$298,000** | — | **Approximately $1,833/month required** | — |

| Metric | Engine candidate |
|---|---:|
| DTI | 11.6% |
| DTA at reference valuation | 40.0% |
| Auto payoff | 2027 · Alex age 46 |

Approved fictional household ceiling:

- Do not intentionally exceed **25% DTI**.
- Do not add debt when **DTA is 40% or higher**.

# Reserve

| Input | Approved decision |
|---|---:|
| Bare-bones monthly basis | $5,000 |
| Working target | 6 months |
| Target amount | $30,000 |
| Current reserve | $30,000 |
| Working status | Fully funded |
| Initial retirement target | 18 months of the selected retirement basis; app calculates the amount |

# Contribution and next-dollar route

| Destination | Monthly household dollars | Reason |
|---|---:|---|
| Auto-loan extra principal | $500 | Approved 7% debt treatment; already in Cash Flow Debt |
| Alex 401(k) employee contribution | $750 | Captures the assumed match |
| Alex family HSA | $625 | Qualified Healthcare Bridge |
| Jordan Roth IRA | $625 | Long-term tax-free qualified growth |
| Taxable Bridge / saved allocation | $1,500 | Accessible early-retirement funding; holdings follow target and drift |
| **Full route** | **$4,000** | $500 debt + $3,500 contributions |

Employer-match teaching assumption:

- 50% match on the first 6% of Alex's $150,000 salary
- $9,000/year or $750/month employee contribution for the full assumed match
- $4,500/year or $375/month employer contribution, shown separately

Reverify recording-year contribution limits, HSA eligibility, and employer HSA contributions before filming.

# Known future costs

## Vehicle replacement

| Item | Amount |
|---|---:|
| Purchase ceiling | $35,000 in 5 years |
| Expected vehicle proceeds | $10,000 |
| Expected purchase-year cash flow | $5,000 |
| Amount to accumulate | $20,000 |

## Optional college commitment

The household commits **$80,000 total across both children**, not unlimited tuition and not $80,000 per child.

| Source | Amount |
|---|---:|
| Existing 529 | $25,000 |
| Parent cash flow during college | $20,000 |
| Student work, aid, or deliberately accepted borrowing | $10,000 |
| Remaining source | $25,000 |
| **Total commitment** | **$80,000** |

One college payment remains active in the first retirement calendar year.

# Cost basis

| Quantity | Status | Basis |
|---:|---|---:|
| 1.25 BTC | Complete lots | $48,000 known |
| 0.40 BTC | Exchange export available | Reconstruction pending |
| 0.10 BTC | Old records missing | Unknown |
| **1.75 BTC** | Quantity reconciles | Tax result incomplete until unresolved units are handled |

# Planning assumptions and baseline result

| Item | Approved / engine result |
|---|---:|
| Bitcoin return view | Built-in Power Law |
| Other broad returns | Current app defaults captured with the receipt |
| Baseline inflation | 3% |
| Inflation stress Scenario | 4% |
| Confidence target | 80% |
| Test runs | 1,000 |
| Household retirement start | Alex age 55 |
| Planning age | 95 |
| Confidence at planned date | 94.6% |
| Earliest date reaching 80% | May 2032 · Alex age 51 |
| 4% inflation Scenario | 91.6%, or 3 points below baseline |

# Retirement income

## Approved inputs

| Input | Decision |
|---|---:|
| Retirement living spending | $100,000/year in today's dollars |
| Part-time work | $20,000/year in today's dollars for the first 3 retirement years |
| Alex Social Security | $30,000/year in today's dollars at 67 |
| Jordan Social Security | $22,000/year in today's dollars when Jordan reaches 67 |
| Starting paycheck | **Keep $100,000/year** |
| Annual policy | Lower 60% · target 80% · upper 95% · 10% maximum correction |
| Borrowing | Excluded from saved Core; Advanced comparison only |

## Spending-reference outputs

| Choice | Engine candidate |
|---|---:|
| Conservative / 95% | $99,317/year |
| Balanced / 80% | $170,216/year |
| Aggressive / 60% | $249,904/year |
| Current Plan | $100,000/year at 94.6% |

The cards show capacity. They do not tell the household to maximize spending.

## First retirement calendar year

Retirement begins in March 2036. The year therefore includes partial-year household wages before retirement, inflation-adjusted part-time work, a college expense, remaining debt, and tax.

| Component | Engine candidate |
|---|---:|
| Inflation-adjusted base living spending | $129,912 |
| College expense | $13,439 |
| Living need | $143,351 |
| Debt payments | $17,400 |
| Taxes | $10,632 |
| **Total need** | **$171,383** |
| Partial-year household wages | $42,557 |
| Inflation-adjusted part-time income | $26,878 |
| **Recurring income** | **$69,435** |
| **Total draw** | **$101,948** |

### Source split

| Holding source | Rounded amount |
|---|---:|
| Cash | $2,200 |
| Stocks | $1,800 |
| Bitcoin | $97,900 |
| Taxable account total | $101,946 |

The $2 source difference is display rounding. The engine calculates $97,948 of Bitcoin sale proceeds. At the projected 2036 price of $1,235,921, that equals approximately **0.079251 BTC**.

# Custody, estate, and protection starting state

- 1.50 BTC on one hardware wallet; 0.25 BTC at one exchange
- Recovery not yet tested
- Device and backup share one physical failure domain
- Jordan has not operated the wallet
- Family Custody Map incomplete
- Intended primary beneficiary is the spouse
- An old workplace account still names a parent
- Executor, backup, will review, POA, healthcare directive, heir letter, and delivery paths remain incomplete
- Insurance policy terms remain intentionally TBD

Protect can record status. It cannot prove a working recovery, valid legal document, accepted provider record, or active insurance coverage.

# Checkpoint contract

| Checkpoint | Current status | Remaining final evidence |
|---|---|---|
| `demo-v1-baseline` | RECONCILED ENGINE CANDIDATE | Confirm labels, rounding, and saved state in UI |
| `demo-v1-cashflow` | RECONCILED ENGINE CANDIDATE | Confirm visible tax, Debt row, surplus, reserve, and source links |
| `demo-v1-debt` | RECONCILED ENGINE CANDIDATE | Confirm DTI, DTA, and payoff presentation |
| `demo-v1-allocation` | RECONCILED ENGINE CANDIDATE | Confirm denominator, excluded accounts, band, and review state |
| `demo-v1-tax` | ENGINE CANDIDATE / BASIS + CPA HOLD | Confirm roadmap UI and unresolved-basis warning |
| `demo-v1-income` | RECONCILED ENGINE CANDIDATE | Confirm first-year rows, source split, and Bitcoin dollars/units |
| `demo-v1-protect` | UI + REAL-WORLD HOLD | Record app status without overstating proof |
| `demo-v1-final` | ENGINE CANDIDATE | Confirm Scenario/report/PDF/export surfaces |

# Change control

1. Change an approved input here first.
2. Record why it changed and which lessons use it.
3. Update the machine-readable fixture and app generator.
4. Rerun affected engine and UI checkpoints.
5. Update scripts, lesson text, visuals, and walkthroughs from the accepted receipt.
6. Never solve continuity by changing one lesson alone.
