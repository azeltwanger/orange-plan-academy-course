# Orange Plan Academy — canonical demo household

**Status:** proposed source of truth for pre-dictation reconciliation  
**Version:** `demo-v1-inputs`  
**Approval:** Austin approval pending  
**Engine outputs:** not canonical until the household is entered into the current app and checkpointed

## Why this exists

The Academy uses one continuous fictional household so a learner can watch one plan take shape instead of relearning a new example in every lesson.

This file owns the demo inputs. A script, lesson text, slide, or walkthrough may not quietly change one of these values. A separate example is allowed only when it is labelled **illustrative — not the demo household**.

The household is fictional. It is not copied from either client-call household and contains no client-identifying information.

## Two kinds of numbers

### Locked source inputs

These are the values the course deliberately enters or decides. They can be used before an app run.

### App-calculated outputs

Confidence, earliest retirement date, projected tax, year-by-year withdrawals, Bitcoin sold, reserve refill, ending estate, and similar results are calculated by Orange Plan. They are not invented for continuity.

Draft teaching examples may use round numbers to explain a mechanism. Those values must be labelled illustrative until a saved demo checkpoint produces the real output.

---

# Household

| Item | Canonical input |
|---|---:|
| Primary adult | Alex, age 45 |
| Spouse | Jordan, age 43 |
| Children | Two, ages 10 and 12 |
| Filing status | Married filing jointly |
| State | Colorado — working demo state, Austin approval pending |
| Planning age | 95 |
| Current year | Use the recording year shown in the app; do not hardcode in evergreen teaching |

The names are intentionally generic and may be replaced before filming. The ages and family structure are the planning inputs that matter.

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
| Estimated federal and payroll taxes for the teaching reconciliation | $40,000 | $3,333 | Tax engine / income inputs |
| Normal living spending, excluding debt payments | $80,000 | $6,667 | Plan / Cash Flow |
| Required debt payments | $22,000 | $1,833 | Debt rows |
| **Reliable surplus available to route** | **$48,000** | **$4,000** | Calculated output |

Reconciliation:

> $190,000 income − $40,000 estimated taxes − $80,000 living spending − $22,000 required debt payments = **$48,000 per year**, or **$4,000 per month**.

The $40,000 tax amount is a clean teaching input for the cash-flow equation, not a claim that this is the household's final tax return. Once the demo is run, use the engine's current tax result and update the example if the difference is material.

## Spending definitions

| Spending value | Amount | Meaning |
|---|---:|---|
| Current normal living spending | $80,000/yr | Ordinary working-life spending; debt payments excluded |
| Bare-bones essentials | $60,000/yr · $5,000/mo | Temporary minimum during a job loss or emergency |
| Retirement baseline living spending | $100,000/yr in today's dollars | Planned active-retirement lifestyle, including higher travel and healthcare assumptions; debt still excluded |

The $100,000 retirement amount is deliberately higher than current living spending. The course must explain why rather than letting the number appear to drift.

# Current assets and accounts

**Illustrative Bitcoin price used only to make the starting balance sheet easy to follow: $100,000 per BTC.** The live app price will change current values and calculated ratios.

| Account / holding | Owner | Tax wrapper | Holding mix | Current value | Primary job |
|---|---|---|---|---:|---|
| Cash reserve account | Joint | Taxable cash | Cash | $30,000 | Reserve |
| Taxable brokerage | Joint | Taxable | Stocks | $25,000 | Bridge |
| Alex 401(k) | Alex | Traditional | $15,000 stocks + $10,000 bonds | $25,000 | Legacy |
| Jordan Roth IRA | Jordan | Roth | Stocks | $10,000 | Legacy |
| HSA | Alex | HSA | Stocks | $5,000 | Bridge or Legacy; final job chosen in Module 4 |
| 529 | Children | Education | $20,000 stocks + $5,000 bonds | $25,000 | College |
| Hardware wallet | Joint planning record | Taxable direct Bitcoin | 1.50 BTC | $150,000 | Legacy |
| Exchange operating balance | Alex | Taxable Bitcoin | 0.25 BTC | $25,000 | Purchase / transfer balance |
| **Investable assets** | — | — | $175,000 BTC + $75,000 stocks + $15,000 bonds + $30,000 cash | **$295,000** | — |
| Primary residence | Joint | Real estate | Home | $450,000 | Residence; not spendable portfolio |
| **Gross assets** | — | — | — | **$745,000** | — |

## Current asset mix

| Asset class | Value | Percent of investable assets |
|---|---:|---:|
| Bitcoin | $175,000 | 59.3% |
| Stocks | $75,000 | 25.4% |
| Bonds | $15,000 | 5.1% |
| Cash | $30,000 | 10.2% |
| **Total** | **$295,000** | **100%** |

A whole-balance-sheet Bitcoin percentage answers a different question. At the illustrative price, Bitcoin is 23.5% of gross assets before debt. The allocation lesson must name the denominator.

# Debt

| Debt | Balance | Rate | Required payment | Remaining structure | Core treatment at start |
|---|---:|---:|---:|---|---|
| Mortgage | $280,000 | 3.25% fixed | $1,450/mo | Approximately 25 years remaining | Required payment only |
| Auto loan | $18,000 | 7.0% fixed | Approximately $383/mo | Approximately 4 years remaining | Candidate for recurring extra principal after reserve |
| **Total** | **$298,000** | — | **Approximately $1,833/mo** | — | — |

## Balance-sheet reconciliation

| Metric | Calculation | Result at the illustrative price |
|---|---|---:|
| Net worth | $745,000 assets − $298,000 debt | $447,000 |
| DTI | $1,833 monthly required debt payments ÷ $15,833 gross monthly income | 11.6% |
| DTA | $298,000 debt ÷ $745,000 gross assets | 40.0% |

DTA will move with the live Bitcoin price. The course should not freeze 40% as though it were a permanent household fact.

# Reserve decision

| Input | Canonical decision |
|---|---:|
| Bare-bones monthly basis | $5,000 |
| Working reserve target | 6 months |
| Working reserve target amount | $30,000 |
| Current reserve | $30,000 |
| Working reserve status at the start of routing | Fully funded |
| Initial retirement cash-buffer target | 18 months of the selected retirement basis; calculated in the app |

The current reserve is intentionally fully funded so Module 4 can demonstrate the normal next-dollar route. Module 2 can still teach how the target was chosen and show a temporary checkpoint with the reserve underfunded when a funding-gap example is useful.

# Contribution and next-dollar route

The household has **$4,000 per month** available to route. Employer money is not subtracted from that amount.

| Destination | Monthly household dollars | Reason |
|---|---:|---|
| Alex 401(k) employee contribution | $750 | 6% of Alex's $150,000 salary; captures the assumed match |
| Auto-loan extra principal | $500 | Chosen 7% debt treatment; reserve remains intact |
| HSA / Roth / additional traditional contributions | $1,250 | Long-term tax-advantaged funding; exact wrapper finalized with tax review |
| Taxable Bridge and Bitcoin allocation | $1,500 | Early-access funding and target allocation |
| **Total household routing** | **$4,000** | Equals reliable surplus |

Employer-match teaching assumption:

- 50% match on the first 6% of Alex's salary
- Employee contribution needed for full match: $9,000/yr or $750/mo
- Employer contribution: $4,500/yr or $375/mo

The exact contribution limits, eligibility, and tax split are changing-year facts and must be verified for the recording year.

When the auto loan is paid off, its required payment and $500 extra-principal route become available for a new decision. Do not silently assume where those dollars go.

# Known future costs and life events

## Vehicle replacement

| Item | Amount |
|---|---:|
| Planned purchase ceiling | $35,000 in 5 years |
| Expected value from current vehicle | $10,000 |
| Expected cash flow in purchase year | $5,000 |
| Amount to accumulate in advance | $20,000 |

The app life event records the expected cost and date. The funding plan identifies the account and contribution source. Do not count the same $20,000 in two places.

## College — optional lesson

The family commits to provide **$80,000 total**, not unlimited tuition.

| Source | Amount |
|---|---:|
| Existing 529 | $25,000 |
| Expected parent cash flow during college | $20,000 |
| Student contribution, aid, or deliberately accepted borrowing | $10,000 |
| Remaining amount to accumulate or fund from assets | $25,000 |
| **Total commitment** | **$80,000** |

The exact school, aid package, and timing are intentionally unknown. Update the plan as the facts improve.

# Cost basis and transaction history

The household owns **1.75 BTC** across the hardware wallet and exchange.

| Quantity | Record status | Basis status |
|---:|---|---|
| 1.25 BTC | Complete acquisition lots | $48,000 known basis |
| 0.40 BTC | Exchange export available | Reconstruction pending |
| 0.10 BTC | Old account history missing | Unknown; visibly unresolved |
| **1.75 BTC** | Quantity reconciles | Tax estimate incomplete until unresolved lots are handled |

The course never invents basis. A planning comparison involving unresolved units must say the estimate is incomplete.

# Planning assumptions

| Assumption | Canonical input rule |
|---|---|
| Bitcoin | Use the current built-in Power Law view for the first working demo unless Austin selects another starting view |
| Stocks, bonds, and cash | Use the current app preset chosen during onboarding; capture the exact values in the checkpoint receipt |
| Inflation | Use the current saved app input; Austin approval of the exact demo value pending |
| Holding overrides | Direct Bitcoin and a spot Bitcoin ETF use Bitcoin assumptions; other overrides only when the holding genuinely differs from its broad class |
| Plan confidence target | 80% starting target |
| Test runs | 1,000 |
| Planned retirement age | 55 |
| Planning age | 95 |

Do not hardcode an app preset value into a video until the demo checkpoint records it. The concept lesson can explain why the assumption was selected without reciting a changeable default.

# Retirement income inputs

| Input | Canonical decision |
|---|---:|
| Baseline retirement living spending | $100,000/yr in today's dollars |
| Planned retirement age | 55 |
| Plan confidence target | 80% |
| Part-time income | $20,000/yr for the first 3 retirement years — proposed, Austin approval pending |
| Combined Social Security / durable later income | $52,000/yr in today's dollars beginning at age 67 — proposed, verify source and timing |
| Starting spending-policy anchor | 80% Balanced reference unless Austin chooses another demo decision |
| Annual policy defaults | Current app defaults: lower 60%, target 80%, upper 95%, correction cap 10% |
| Borrowing | Not part of the saved core baseline; compare only in an optional advanced preview |

## Outputs that are still deliberately blank

The following must come from the current app after `demo-v1-inputs` is entered:

- Confidence at planned age 55
- Earliest month or age reaching the 80% target
- Conservative, Balanced, Aggressive, and current-plan spending amounts
- First retirement-year total need
- Taxes and debt costs in that year
- Recurring income in that year
- Total draw
- Account and holding source split
- Bitcoin sold or retained
- Current and target reserve months in retirement
- Year-by-year tax roadmap
- Roth-conversion comparison
- Ending assets and estate value

The round values **68% confidence at age 55** and **age 58 as the earliest qualifying date** in the draft confidence lesson are teaching examples, not canonical demo outputs. Replace or explicitly label them after the checkpoint run.

# Custody starting state

| Item | Starting state |
|---|---|
| Long-term balance | 1.50 BTC on one hardware wallet |
| Operating balance | 0.25 BTC at one exchange |
| Hardware-wallet recovery | Not yet tested |
| Device and backup | Same physical failure domain at the start |
| Family knowledge | Alex understands the setup; Jordan has not operated it |
| Exchange security | Strong password; stronger authentication and recovery review still needed |
| Family Custody Map | Not complete |

Core custody outcome:

- Device and software verified through the manufacturer's current process
- Receive and send test complete
- Backup or recovery test complete through a safe supported method
- Physical, human, and provider failure domains reviewed
- Jordan practices on a small wallet
- Family Custody Map contains the process and people, never secrets

The demo does not assume multisig is mandatory. A supported multi-key design is an advanced comparison after the family-ready single-signature process works.

# Estate and protection starting state

| Area | Starting state |
|---|---|
| Intended primary beneficiary | Spouse |
| Intended contingent beneficiaries | Children, subject to attorney design for minors |
| Known mismatch | Old workplace retirement account still names a parent |
| Executor / personal representative | Not confirmed |
| Backup person | Not confirmed |
| Will | Needs current attorney review |
| Financial power of attorney | Status to verify |
| Healthcare directive | Status to verify |
| Heir letter | Not complete |
| Delivery / discovery paths | Not complete |
| Life insurance | Existing amount and terms intentionally TBD |
| Disability insurance | Employer policy terms intentionally TBD |
| Umbrella and long-term care | Review status TBD |

Insurance examples in the course are preliminary planning illustrations until actual policy terms are entered. Do not present the fictional household as having a verified coverage recommendation.

# Module checkpoint contract

| Checkpoint | What changes in the demo | What must reconcile |
|---|---|---|
| `demo-v1-baseline` | Accounts, holdings, debts, income, spending, assumptions, life events, confidence target entered | Balance sheet, 1.75 BTC quantity, cash-flow source rows |
| `demo-v1-cashflow` | Bare-bones spending and reserve settings confirmed | $4,000/mo surplus; $30,000 working reserve target |
| `demo-v1-debt` | Mortgage stays on schedule; auto receives $500/mo extra | Debt payment rows, DTI, DTA, payoff timing |
| `demo-v1-allocation` | Target, drift band, time-horizon jobs, and contribution route saved | Routing equals $4,000/mo; no double-counted contribution |
| `demo-v1-tax` | Lots entered; unresolved basis remains visible; tax review outcome recorded | 1.75 BTC quantity; known and unresolved lots separate |
| `demo-v1-income` | Spending target, income sources, withdrawal strategy, and annual policy saved | Total draw equals sources; Bitcoin sold agrees everywhere |
| `demo-v1-protect` | Recovery, people, beneficiaries, documents, and gaps updated | App readiness agrees with real-world completion limits |
| `demo-v1-final` | Scenarios, report, action list, PDF, and encrypted backup complete | Six-sentence summary agrees with current saved plan |

# Change-control rules

1. Change an input here first.
2. Record why it changed and which lessons use it.
3. Update the saved demo account.
4. Re-run the affected app outputs.
5. Update scripts, lesson texts, slides, and later walkthroughs from the new checkpoint.
6. Never solve a continuity problem by quietly changing one example in one lesson.

## Austin decisions still needed before the final demo run

- Confirm state and generic household names
- Confirm retirement spending of $100,000 versus current living spending of $80,000
- Confirm part-time income and Social Security assumptions
- Confirm exact broad app preset and inflation input
- Confirm whether the optional college goal remains inside the continuous household
- Confirm the final target Bitcoin allocation and drift band
- Confirm the starting retirement-spending choice

Those are targeted decisions. They do not require re-dictating the course.
