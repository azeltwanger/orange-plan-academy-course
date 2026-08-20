# Academy visual data receipt — app commit 3105664

**Status:** reconciled engine data; final screenshots and visible labels still require deployed UI acceptance  
**Fixture:** `demo-v1-inputs`  
**As-of:** 2026-08-20  
**BTC reference price:** $100,000  
**Monte Carlo:** 1,000 runs · seed `20260820`

Use this file when producing concept visuals. Do not retrieve numbers from old live-client decks or placeholder mockups.

## Module 1 · Baseline and confidence

- Household retirement start: March 2036, Alex age 55
- Plan confidence target: 80%
- Confidence at planned date: 94.6%
- Earliest target-qualified date: May 2032, Alex age 51
- Boundary confidence: 80.0%

**Visual rule:** one test-run framework produces both confidence at the planned date and the earliest date reaching the target.

## Module 2 · Cash Flow and Reserve

- Gross income: $190,000/year
- Round teaching tax: $40,000/year
- Current engine tax: $36,862/year
- Living spending: $80,000/year, debt excluded
- Required debt: $1,833/month
- Extra auto principal: $500/month
- Planned debt shown by Cash Flow: $2,333/month
- Capacity before extra debt: $4,261/month
- Displayed surplus after planned debt: $3,761/month
- Contribution route after debt: $3,500/month
- Operating cushion: $261/month
- Bare-bones spending: $5,000/month
- Reserve: $30,000 · 6 months · fully funded

**Visual rule:** show the $500 extra debt inside the Debt row. Do not subtract it twice.

## Module 3 · Debt

- Total debt: $298,000
- DTI: 11.6%
- DTA at reference valuation: 40.0%
- Mortgage: $280,000 at 3.25%, required payment only
- Auto: $18,000 at 7%, plus $500/month extra
- Auto payoff candidate: 2027, Alex age 46
- Household ceiling: 25% DTI; no new debt at 40%+ DTA

## Module 4 · Allocation and the next dollar

### Allocation scope

- App allocatable portfolio: $270,000
- 529 excluded: $25,000
- Home excluded: $450,000
- Bitcoin: $175,000
- Current app Bitcoin allocation: 64.8%
- Target: 50%
- Review band: 40–60%
- Status: above band; review, not automatic sale

### Drawdown

- Bitcoin loss at 75%: $131,250
- Allocatable portfolio after loss: $138,750
- Financial balances including the 529 after loss: $163,750

### Route

- $500 extra debt, already inside Cash Flow Debt
- $750 workplace contribution
- $625 family HSA
- $625 spousal Roth IRA
- $1,500 taxable Bridge / saved allocation
- Full decision: $4,000/month
- Post-debt contribution route: $3,500/month

**Visual rule:** name the denominator and distinguish the full route from the post-debt contribution amount.

## Module 5 · Tax

- Bitcoin quantity: 1.75 BTC
- Known lots: 1.25 BTC with $48,000 basis
- Reconstruction pending: 0.40 BTC
- Unknown: 0.10 BTC
- Current-year modeled tax: $36,862

**Visual rule:** quantity can reconcile while basis remains incomplete. Do not present the tax roadmap as filing-grade.

## Module 6 · Retirement Income

### Spending choices

- Conservative / 95%: $99,317/year
- Current Plan: $100,000/year at 94.6%
- Balanced / 80%: $170,216/year
- Aggressive / 60%: $249,904/year
- Saved demo paycheck: $100,000/year

### First retirement calendar year

- Base living spending: $129,912
- College event: $13,439
- Living need: $143,351
- Debt: $17,400
- Tax: $10,632
- Total need: $171,383
- Partial-year household wages: $42,557
- Inflation-adjusted part-time income: $26,878
- Recurring income: $69,435
- Total draw: $101,948

### Sources

- Cash: $2,200
- Stocks: $1,800
- Bitcoin: $97,900 rounded
- Taxable source total: $101,946 rounded
- Bitcoin sale proceeds: $97,948
- Projected 2036 Bitcoin price: $1,235,921
- Bitcoin sold: 0.079251 BTC

**Visual rule:** explain the partial calendar year, inflation, college, debt, and tax before showing the draw.

## Module 9 · Scenario

- Baseline inflation: 3%
- Baseline confidence: 94.6%
- Stress inflation: 4%
- Stress confidence: 91.6%
- Delta: −3.0 percentage points
- Plan target: 80%

**Visual rule:** one changed input, one measured effect. Do not invent an earliest-date or estate delta that the comparison does not show.

## Values intentionally excluded from Core headlines

- Ending net worth at age 95: $428,365,615

This value is highly assumption-sensitive. It may appear in a complete report receipt but should not become a promise, outcome claim, or primary teaching visual.
