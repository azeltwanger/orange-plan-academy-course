# Orange Plan Academy — canonical demo household

**Status:** approved course-owned inputs; reproducible engine candidate generated; deployed UI verification pending  
**Version:** `demo-v1-inputs`  
**Approved by Austin:** 2026-08-19  
**Engine candidate:** app commit `4456b3c954ea29630b4d9c73aff6a52711cfad15`  
**Final output authority:** accepted receipts under `demo/` and `DEMO-CHECKPOINT-RUN-SHEET.md`

## Why this exists

The Academy uses one continuous fictional household so the learner watches one plan take shape instead of relearning a new example in every lesson.

This file owns the demo inputs and the accepted interpretation of app outputs. A script, lesson, slide, or walkthrough may not quietly change one value. A separate example is allowed only when it is labelled **illustrative — not the demo household**.

The household is fictional. It contains no client data, Austin household data, credentials, or Bitcoin secrets.

## Input versus output

### Course-owned inputs

Facts and decisions the course deliberately enters. These are approved below.

### Orange Plan outputs

Confidence, earliest target-qualified date, displayed tax, debt payoff timing, allocation scope, withdrawal sources, Bitcoin sold, Scenario deltas, and ending assets come from the current app.

The first reproducible engine candidate is recorded in `demo/ENGINE-CHECKPOINT-CANDIDATE-4456b3c.md`. It may guide script revisions, but the deployed interface still has to verify the displayed value, label, state, and source.

---

# Household

| Item | Canonical input |
|---|---:|
| Primary adult | Alex, age 45 |
| Spouse | Jordan, age 43 |
| Children | Two, ages 10 and 12 |
| Filing status | Married filing jointly |
| State | Colorado |
| Alex retirement age | 55 |
| Jordan retirement age | 55, two calendar years after Alex because Jordan is younger |
| Planning age | 95 |
| Current year | Use the recording year shown in the accepted app build |

The current app result reflects Jordan continuing W-2 work for two years after Alex retires. That timing must be visible in the retirement-income lesson so the first-year recurring income does not look unexplained.

# Current cash flow

## Income

| Source | Annual | Monthly | Reliability |
|---|---:|---:|---|
| Alex W-2 salary | $150,000 | $12,500 | Stable |
| Jordan W-2 salary | $40,000 | $3,333 | Stable |
| **Gross household income** | **$190,000** | **$15,833** | — |

## Current outflow and routing

| Item | Annual | Monthly | Status |
|---|---:|---:|---|
| Round teaching estimate for current taxes | $40,000 | $3,333 | Explainable teaching input |
| First engine current-year tax candidate | $36,862 | $3,072 | UI verification pending |
| Normal living spending, excluding debt payments | $80,000 | $6,667 | Approved input |
| Required debt payments | Approximately $22,000 | Approximately $1,833 | Approved debt rows |
| **Repeatable amount routed by the household** | **$48,000** | **$4,000** | Approved decision |

Teaching reconciliation:

> $190,000 income − $40,000 taxes − $80,000 living spending − $22,000 required debt payments = **$48,000 per year**, or **$4,000 per month**.

The current engine estimates lower tax. That means the maximum calculated amount before flexible routing may be slightly above $4,000. The Academy should describe $4,000 as the amount the household deliberately commits every month, leaving a small operating cushion, rather than pretending it is the exact maximum output.

The Cash Flow UI still needs to confirm the displayed tax, required-debt treatment, and monthly surplus before the final receipt is accepted.

## Spending definitions

| Spending value | Amount | Meaning |
|---|---:|---|
| Current normal living spending | $80,000/year | Ordinary working-life spending; debt excluded |
| Bare-bones essentials | $60,000/year · $5,000/month | Temporary minimum during a job loss or emergency |
| Retirement living spending | $100,000/year in today's dollars | Deliberately higher active-retirement lifestyle with more travel and healthcare; debt excluded |

# Current assets and accounts

**Illustrative reference price: $100,000 per BTC.** The accepted app receipt records the price and date used.

| Account / holding | Owner | Wrapper | Holding mix | Reference value | Primary job | Allocation scope |
|---|---|---|---|---:|---|---|
| Cash reserve account | Joint | Taxable cash | Cash | $30,000 | Reserve | Included |
| Taxable brokerage | Joint | Taxable | Stocks | $25,000 | Bridge | Included |
| Alex 401(k) | Alex | Traditional | $15,000 stocks + $10,000 bonds | $25,000 | Legacy | Included |
| Jordan Roth IRA | Jordan | Roth | Stocks | $10,000 | Legacy | Included |
| Alex family HSA | Alex | HSA | Stocks | $5,000 | Healthcare Bridge | Included |
| 529 | Children | Education | $20,000 stocks + $5,000 bonds | $25,000 | College | **Excluded from household target allocation** |
| Hardware wallet | Joint planning record | Taxable direct Bitcoin | 1.50 BTC | $150,000 | Legacy | Included |
| Exchange operating balance | Alex | Taxable Bitcoin | 0.25 BTC | $25,000 | Operating balance | Included |
| Primary residence | Joint | Real estate | Home | $450,000 | Residence | Excluded |

## Three denominators

| Scope | Amount | Bitcoin percentage | What it answers |
|---|---:|---:|---|
| **Allocatable portfolio used by Orange Plan** | **$270,000** | **64.8%** | What mix is the household managing toward its target? |
| Financial/investment balances including the 529 | $295,000 | 59.3% | How much financial wealth exists, including money committed to college? |
| Gross assets including the home | $745,000 | 23.5% | How concentrated is the whole balance sheet before debt? |

The Allocation page excludes the beneficiary-restricted 529 because those dollars already have a separate owner/job and are not available to rebalance the household's retirement portfolio.

## App allocation result

| Output | Result |
|---|---:|
| Current Bitcoin in the allocatable portfolio | $175,000 |
| Current Bitcoin allocation | 64.8% |
| Approved target | 50% |
| Approved review band | 40–60% |
| Status | Above the review band; review required, not an automatic sale |

The $1,500 taxable Bridge / investment route follows target and drift. While Bitcoin is above the band, new money can move toward non-Bitcoin holdings first. A taxable sale remains a separate tax, access, and planning decision.

## Drawdown reference

| Scope | Result after a 75% Bitcoin decline, other assets flat |
|---|---:|
| Bitcoin loss | $131,250 |
| Allocatable portfolio | $138,750 |
| Financial balances including the excluded 529 | $163,750 |

# Debt

| Debt | Balance | Rate | Required payment | Remaining structure | Core treatment |
|---|---:|---:|---:|---|---|
| Mortgage | $280,000 | 3.25% fixed | $1,450/month | Approximately 25 years | Required payment only |
| Auto loan | $18,000 | 7.0% fixed | Approximately $383/month | Approximately 4 years before extra principal | $500/month recurring extra principal |
| **Total** | **$298,000** | — | **Approximately $1,833/month required** | — | — |

## Debt outputs

| Metric | Result |
|---|---:|
| DTI | 11.6% |
| DTA at the reference valuation | 40.0% |
| Engine candidate auto payoff | 2027 · Alex age 46 |

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

The household deliberately routes **$4,000 per month**. Employer money is additional.

| Destination | Monthly household dollars | Reason |
|---|---:|---|
| Alex 401(k) employee contribution | $750 | 6% of salary; captures the assumed match |
| Auto-loan extra principal | $500 | Approved 7% debt treatment |
| Alex family HSA | $625 | Qualified healthcare Bridge |
| Jordan Roth IRA | $625 | Long-term tax-free qualified growth |
| Taxable Bridge / investment allocation | $1,500 | Accessible early-retirement funding; holdings follow target and drift |
| **Total** | **$4,000** | Repeatable route |

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

One child still has a modeled college payment in Alex's first retirement year. That is why the first-year living/life-event need is higher than the inflated $100,000 retirement-spending input.

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
| Stocks, bonds, cash, and real estate | Current standard app defaults; exact values stored with the engine/UI receipt |
| Baseline inflation | 3% |
| Inflation stress Scenario | 4% |
| Holding override rule | Use only when the broad asset class would model the specific holding incorrectly |
| Plan confidence target | 80% |
| Test runs | 1,000 |
| Alex retirement age | 55 |
| Jordan earned-income end | Jordan age 55, two years later |
| Planning age | 95 |

# Baseline and confidence outputs

| Output | First engine candidate |
|---|---:|
| Confidence at Alex age 55 | 94.6% |
| Earliest date reaching the 80% target | May 2032 · Alex age 51 |
| Confidence at the boundary | 80.0% |
| 4% inflation Scenario confidence at age 55 | 91.6% |

The earliest date is the first date for Alex under the saved household timeline. Jordan's earned-income end remains tied to Jordan reaching age 55. The UI walkthrough must make that spouse timing visible.

# Retirement income inputs and decisions

| Input | Approved decision |
|---|---:|
| Retirement living spending | $100,000/year in today's dollars |
| Alex retirement age | 55 |
| Jordan retirement age | 55, two years later |
| Plan confidence target | 80% |
| Alex part-time income | $20,000/year in today's dollars for the first 3 retirement years |
| Alex Social Security | $30,000/year in today's dollars starting at 67 |
| Jordan Social Security | $22,000/year in today's dollars starting when Jordan is 67 |
| **Starting retirement paycheck** | **Keep the current $100,000/year Plan amount** |
| Annual policy defaults | Lower 60% · target 80% · upper 95% · 10% maximum correction |
| Borrowing | Excluded from the saved Core baseline; Advanced comparison only |

## Spending-reference outputs

| Choice | Engine candidate |
|---|---:|
| Conservative / 95% | $99,317/year |
| Balanced / 80% | $170,216/year |
| Aggressive / 60% | $249,904/year |
| Current Plan amount | $100,000/year at 94.6% confidence |

The household keeps $100,000 because that is the lifestyle it deliberately chose. The cards show capacity and trade-offs; they do not instruct the household to maximize spending.

## First-retirement-year candidate

| Output | Engine candidate |
|---|---:|
| Year / Alex age | 2036 / 55 |
| Living need including current life events | $143,351 |
| Total need including tax and debt | $171,383 |
| Recurring income | $69,435 |
| Total draw | $101,948 |
| Account source | Taxable accounts |
| Bitcoin sale dollars | $97,948 |

The expanded diagnostic is responsible for naming the exact income and expense components and correcting the BTC quantity sold. Until then, do not insert the generated “1 BTC” figure into a script.

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
| Insurance terms | Intentionally TBD until fictional policy inputs are chosen and reviewed |

# Checkpoint contract

| Checkpoint | Current status | Required final reconciliation |
|---|---|---|
| `demo-v1-baseline` | ENGINE CANDIDATE | Confirm 94.6% at age 55 and May 2032 earliest date in UI |
| `demo-v1-cashflow` | PARTIAL ENGINE CANDIDATE | Confirm displayed tax, required debt treatment, surplus, and $30,000 reserve |
| `demo-v1-debt` | ENGINE CANDIDATE | Confirm DTI, DTA, and 2027 auto payoff in UI |
| `demo-v1-allocation` | ENGINE CANDIDATE | Confirm $270,000 denominator, 64.8% BTC, target, band, and action state |
| `demo-v1-tax` | ENGINE CANDIDATE / BASIS HOLD | Confirm roadmap presentation and unresolved-basis warning |
| `demo-v1-income` | ENGINE CANDIDATE / DIAGNOSTIC HOLD | Reconcile total need, recurring income, sources, BTC dollars and units |
| `demo-v1-protect` | UI + REAL-WORLD HOLD | App checklist may not overstate recovery/legal/provider proof |
| `demo-v1-final` | ENGINE CANDIDATE | Confirm report, Scenario delta, capstone, PDF, and encrypted-export state |

# Change control

1. Change an approved input here first.
2. Record why it changed and which lessons use it.
3. Update the machine-readable fixture and app generator.
4. Rerun affected engine and UI checkpoints.
5. Update scripts, lesson text, visuals, and walkthroughs from the accepted receipt.
6. Never solve continuity by changing one lesson alone.
