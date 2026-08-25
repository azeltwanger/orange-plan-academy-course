# Build Your Plan — walkthrough pre-production briefs

**Status:** ready for deployed verification; not a recording script  
**Observed preview:** app commit `2a3bf8872b35e782c6fb098d1a65ffcdf9a85666`  
**Demo engine:** app commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Fixture:** `demo-v1-inputs`

These briefs finish the instructional design before Austin records. They contain the decision recall, observed mission/task IDs, starting and ending checkpoints, provenance moments, and two finish lines.

They deliberately do **not** contain final button-by-button clicks. The exact route, label, order, focus behavior, save state, and screenshots are accepted only after Austin uses the deployed seven-mission flow end to end.

## Shared recording pattern

Every walkthrough opens with:

> “You already made the decision in the lesson. Now we are putting it into the plan and checking what changed.”

Then:

1. Open the relevant Build Your Plan mission.
2. Name the starting checkpoint.
3. Identify which tasks are automatic and which are manual.
4. Enter or review only the data/decision taught by the related lessons.
5. Read one important output using:
   - What it means
   - Calculated from
   - Edit source
   - This affects
6. Return to Build Your Plan.
7. State:
   - app completion rule,
   - human planning finish line,
   - unresolved professional or real-world work.
8. Save the ending checkpoint.

A manual checkbox is never filmed as proof of a task the app cannot verify.

---

# Walkthrough 1 · Get organized

**Mission ID:** `organized`  
**Lessons recalled:** 1.1, 1.2, 2.3, optional 2.4  
**Starting checkpoint:** approved source records  
**Ending checkpoint:** `demo-v1-baseline`

## Decision recalled

- Which information is verified, estimated, or missing?
- Which future changes belong in the Baseline as life events?
- Which questions remain Scenarios?

## Observed tasks

1. `add_accounts` — Add every account
2. `add_holdings` — Add the holdings inside them
3. `split_household` — Separate mine, yours, and joint
4. `life_events` — Put the big future costs and changes on the calendar

## Demo implementation

- Add the synthetic accounts.
- Add the actual holdings inside them rather than one account balance only.
- Confirm Alex, Jordan, joint, and child-benefit ownership.
- Add the vehicle and college events.
- Confirm 1.75 BTC across the hardware wallet and exchange.

## Provenance moment

**Current position / net worth**

- What it means: included assets minus included debt
- Calculated from: accounts, holdings, prices/manual values, and liabilities
- Edit source: the underlying records
- This affects: DTA, plan funding, report, and estate context

## App completion rule

- At least one account
- At least one holding
- Household split manually checked
- At least one life event

## Human finish line

Every meaningful account, holding, debt, income source, and expected event is represented honestly, and the learner can explain what is rough or missing.

## Deployed verification questions

- Does the mission provide an honest no-life-event state?
- Does ownership save automatically or require a separate action?
- What does the return-to-plan control say?

---

# Walkthrough 2 · Find financial capacity

**Mission ID:** `capacity`  
**Lessons recalled:** 2.1, 2.2, 3.1, 4.3  
**Starting checkpoint:** `demo-v1-baseline`  
**Ending checkpoints:** `demo-v1-cashflow` and `demo-v1-debt`

## Decisions recalled

- Normal living spending: $80,000/year, debt excluded
- Bare-bones spending: $5,000/month
- Reserve: 6 months / $30,000
- Mortgage: required payment only
- Auto: $500/month extra principal
- Full route: $500 extra debt + $3,500 account contributions

## Observed tasks

1. `cash_flow` — Confirm income, taxes, living spending, and Debt
2. `reserve` — Choose the working reserve
3. `debt` — Choose the Debt treatment
4. `contributions` — Route the next dollar

## Demo implementation

Verify the page against:

- gross income: $190,000/year
- modeled tax: about $36,862/year
- required debt: about $1,833/month
- saved extra auto principal: $500/month
- planned debt: about $2,333/month
- capacity before extra debt: about $4,261/month
- post-debt surplus: about $3,761/month
- account route: $3,500/month
- operating cushion: about $261/month
- reserve: $30,000 held and targeted

## Provenance moment

**Displayed post-debt surplus**

- What it means: amount left for accounts and cushion after the saved Debt treatment
- Calculated from: income − tax − living spending − required debt − saved extra principal
- Edit source: source rows and Debt strategy
- This affects: contributions, account growth, confidence, and earliest date

## App completion rule

- Income and current spending exist
- Reserve basis/months saved
- No debt or every debt reviewed
- Routing manually checked

## Human finish line

The learner can rebuild the page math, explain why Debt is separate from living spending, and avoid routing the $500 extra principal twice.

---

# Walkthrough 3 · Aim the portfolio

**Mission ID:** `portfolio`  
**Lessons recalled:** 4.1–4.4  
**Starting checkpoint:** `demo-v1-debt`  
**Ending checkpoint:** `demo-v1-allocation`

## Decisions recalled

- App Allocation denominator: $270,000
- Bitcoin: $175,000 / 64.8%
- Target: 50%
- Review band: 40–60%
- Status: above band; review, not automatic sale
- 75% Bitcoin loss: $131,250
- Future account route: $3,500/month after the saved debt treatment

## Observed tasks

1. `allocation_range` — Choose the Bitcoin range you will review against
2. `timeframes` — Give Reserve, Bridge, and Legacy a job
3. `contribution_allocation` — Decide what future dollars buy
4. `account_location` — Choose which holdings belong in which accounts

## Demo implementation

- Confirm 529 and primary residence are excluded from target Allocation.
- Save the 50% target and 40–60% band.
- Assign Reserve, Bridge, Healthcare Bridge, Legacy, College, and operating roles.
- Direct new taxable money toward the underweight side rather than automatically buying more Bitcoin.
- Review account location without triggering unnecessary taxable trades.

## Provenance moment

**Current Bitcoin allocation**

- What it means: Bitcoin as a share of the app's allocatable portfolio
- Calculated from: included Bitcoin ÷ included target-allocation holdings
- Edit source: holdings, prices, classifications, and inclusion rules
- This affects: drift, contribution direction, drawdown, confidence, and custody stakes

## App completion rule

- Holdings exist and target totals 100
- All in-scope holdings have timeframe jobs
- Future-dollar choice manually checked
- Account-location choice manually checked

## Human finish line

The learner can name the denominator, current percentage, target/band, dollar drawdown, jobs, account trade-offs, and next contribution action.

---

# Walkthrough 4 · Plan the tax path

**Mission ID:** `tax`  
**Lessons recalled:** 5.1–5.2  
**Starting checkpoint:** `demo-v1-allocation`  
**Ending checkpoint:** `demo-v1-tax`  
**Product state:** skippable/deferred

## Decisions recalled

- Quantity reconciles at 1.75 BTC.
- 1.25 BTC has $48,000 known basis.
- 0.40 BTC reconstruction is pending.
- 0.10 BTC remains unknown.
- Current priority: finish the record and prepare a defined CPA question.

## Observed tasks

1. `cost_basis` — Get cost basis usable before the next sale
2. `tax_report` — Read the year-by-year tax roadmap
3. `tax_opportunities` — Flag conversion, harvesting, or repayment windows
4. `tax_follow_through` — Record what happens now, later, or never

## Demo implementation

- Reconcile quantity without fabricating basis.
- Show the known, pending, and unknown lot states.
- Read the current roadmap as a planning estimate.
- Record one current action and one CPA question.
- Leave conversion/harvesting as reviewed opportunities rather than executed decisions.

## Provenance moment

**Projected tax**

- What it means: app estimate for the modeled year
- Calculated from: filing status, state, income, gains, basis, withdrawals, conversions, and current tax rules modeled by the app
- Edit source: the underlying tax/income/basis/strategy records
- This affects: Cash Flow, total need, draw, source mix, confidence, and earliest date

## App completion rule

All four tasks are manually checked, or the product mission is deferred.

## Human finish line

Basis uncertainty remains visible and the learner leaves with one action, one professional question, or a deliberate pass.

## Professional hold

Do not finalize this walkthrough's tax wording until the CPA/tax-attorney packet is returned and applied.

---

# Walkthrough 5 · Build the retirement paycheck

**Mission ID:** `retirement_income`  
**Lessons recalled:** 1.3, 6.1–6.3  
**Starting checkpoint:** `demo-v1-tax`  
**Ending checkpoint:** `demo-v1-income`  
**Product state:** skippable/deferred

## Decisions recalled

- Household retirement: March 2036 / Alex 55
- Retirement lifestyle: $100,000/year in today's dollars
- Income floor: part-time work, then staggered Social Security
- Saved starting paycheck: $100,000/year at 94.6%
- Borrowing excluded from the Core baseline
- Annual policy: 60 / 80 / 95 with up to 10% correction

## Observed tasks

1. `retirement_timing` — Set retirement timing and spending
2. `income_floor` — Add Social Security, pensions, and other recurring income
3. `withdrawal_strategy` — Choose the withdrawal and refill policy
4. `sell_borrow_hold` — Decide when you sell, borrow, or keep holding

## Demo implementation

Verify first retirement calendar year:

- total need: $171,383
- recurring income: $69,435
- total draw: $101,948
- cash: about $2,200
- stocks: about $1,800
- Bitcoin: about $97,900
- sale proceeds: $97,948
- projected BTC price: $1,235,921
- units sold: 0.079251 BTC

Compare spending cards:

- Conservative: $99,317
- Current: $100,000 at 94.6%
- Balanced: $170,216
- Aggressive: $249,904

Keep the deliberate $100,000 paycheck.

## Provenance moment

**Total draw and Bitcoin sold**

- What they mean: amount required from accounts and the Bitcoin portion of that source
- Calculated from: total need − recurring income, then the saved account/asset policy and modeled price
- Edit source: underlying need/income sources, holdings, and strategy
- This affects: tax, balances, custody exposure, confidence, and estate

## App completion rule

- Retirement age and spending exist
- Required recurring-income inputs exist
- Withdrawal/refill task manually checked
- Sell/borrow/hold task manually checked

## Human finish line

Need, income, draw, sources, dollars, projected price, units, paycheck, and annual policy all reconcile and can be explained. Borrowing may remain deliberately excluded.

## Professional hold

Apply CPA qualifications to withdrawal/tax language before final recording.

---

# Walkthrough 6 · Protect the plan

**Mission ID:** `protect`  
**Lessons recalled:** 7.1–8.4  
**Starting checkpoint:** `demo-v1-income`  
**Ending checkpoint:** `demo-v1-protect`

## Observed tasks

1. `custody_recovery` — Document custody and prove recovery
2. `beneficiaries` — Check beneficiaries everywhere
3. `estate_roles` — Name the people and documents that let others act
4. `heir_letter` — Write the heir letter and add the backup delivery path
5. `coverage` — Fill the insurance gaps the family cannot absorb

## Demo implementation

Record, without secrets:

- long-term and operating custody jobs,
- recovery still incomplete,
- device/backup physical failure,
- Jordan practice still incomplete,
- old provider beneficiary mismatch,
- people/documents still needing attorney work,
- heir letter/delivery still incomplete,
- insurance policy terms still open.

Do not turn intended future work into a completed checkmark.

## Provenance moment

**Protect readiness**

- What it means: status of the fields/checklist saved in the app
- Calculated from: current product completion rules
- Edit source: Protect records
- This affects: next action and report status
- It does **not** prove: recovery, legal validity, provider acceptance, insurance coverage, or family capability

## App completion rule

All five tasks use manual completion keys.

## Human finish line

The required real-world test/provider/document/contract evidence exists, or the open work remains visibly open with an owner and date.

## Professional hold

Apply custody, Colorado estate-attorney, and licensed-insurance corrections before final recording.

---

# Walkthrough 7 · Use and review the plan

**Mission ID:** `review`  
**Lessons recalled:** 9.1–9.2  
**Starting checkpoint:** `demo-v1-protect`  
**Ending checkpoint:** `demo-v1-final`

## Observed tasks

1. `read_plan` — Run the plan and read the result
2. `run_scenario` — Compare one real decision
3. `action_list` — Turn the result into one to three actions
4. `save_record` — Save the annual record and schedule the next review

## Demo implementation

- Read 94.6% confidence and May 2032 earliest target date.
- Run the 4% inflation Scenario: 91.6%, down 3 points.
- Keep the 3% Baseline unchanged.
- Complete the demo capstone.
- Assign one to three actions.
- Save the readable PDF and encrypted export separately.
- State that in-app restore is currently unavailable.

## Provenance moment

**Scenario delta**

- What it means: difference from the saved Baseline after one defined override
- Calculated from: same projection framework with Scenario input(s)
- Edit source: Scenario definition until a real decision updates its source page
- This affects: only the comparison outputs the app actually shows

## App completion rule

All four tasks use manual completion keys.

## Human finish line

The learner can explain the plan in six sentences, owns one to three actions, knows the next review date, and accurately describes the PDF/export roles.

---

# Final deployed-verification log

| Mission | Deployed label/order confirmed | Routes/focus confirmed | Auto/manual/skip behavior confirmed | Receipt accepted | Austin used end to end | Ready to record |
|---|---|---|---|---|---|---|
| Get organized |  |  |  |  |  | NO |
| Find financial capacity |  |  |  |  |  | NO |
| Aim the portfolio |  |  |  |  |  | NO |
| Plan the tax path |  |  |  |  |  | NO |
| Build the retirement paycheck |  |  |  |  |  | NO |
| Protect the plan |  |  |  |  |  | NO |
| Use and review the plan |  |  |  |  |  | NO |

The briefs are complete when this table is filled from the deployed flow—not from the code observation alone.
