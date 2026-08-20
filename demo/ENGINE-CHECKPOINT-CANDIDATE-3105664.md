# Orange Plan Academy — reconciled app-engine checkpoint candidate

**Status:** engine-generated and diagnostics-reconciled; deployed UI acceptance still required  
**App commit:** `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Fixture:** `demo-v1-inputs`  
**As-of date:** 2026-08-20  
**BTC reference price:** $100,000  
**Monte Carlo:** 1,000 test runs · seed `20260820`  
**Generated:** 2026-08-20T16:27:35.877Z

The current Vercel preview built successfully and published the result and provenance diagnostics. The generator ran the same projection, Monte Carlo, allocation, Cash Flow, and retirement-funding builders used by Orange Plan. This is the current output candidate; it is not yet a final screenshot/UI receipt.

## Baseline and confidence

| Output | Engine result |
|---|---:|
| Planned retirement date | March 2036 · Alex age 55 |
| Planned retirement spending | $100,000/year in today's dollars |
| Plan confidence target | 80% |
| Confidence at the planned date | 94.6% |
| Earliest date reaching 80% | May 2032 · Alex age 51 |
| Confidence at the earliest boundary | 80.0% |

### Spending references

| Choice | Calculated amount / result |
|---|---:|
| Conservative · 95% | $99,317/year |
| Balanced · 80% | $170,216/year |
| Aggressive · 60% | $249,904/year |
| Current Plan amount | $100,000/year at 94.6% |

### Recommended teaching decision

Keep **$100,000/year** as the demo household's starting retirement paycheck unless Austin explicitly changes it after the UI review.

The household chose a $100,000 lifestyle; it should not raise spending to $170,216 merely because the model supports it. The current amount lands almost exactly on the Conservative reference. This makes the lesson's trade-off real: the spending cards are choices, not an instruction to maximize consumption. The household could instead use the excess capacity to retire earlier, reduce risk, save less aggressively, or leave more to heirs.

This remains a small Austin confirmation, not a new dictation task.

## Cash Flow — reconciled with page math

| Output | Current result |
|---|---:|
| Gross income | $190,000/year |
| Current living spending | $80,000/year |
| Required debt payments | $1,833/month |
| Saved extra auto principal | $500/month |
| Planned debt payments shown in Cash Flow | $2,333/month |
| Engine current-year tax | $36,862/year |
| Capacity before the extra-debt decision | $4,261/month |
| Displayed monthly surplus after planned debt | $3,761/month |
| Approved contribution route after extra debt | $3,500/month |
| Operating cushion after the route | $261/month |

The course's **$4,000 next-dollar route** remains valid when described correctly:

- $500/month is the extra-debt decision already included in planned debt payments.
- $3,500/month is routed to the workplace plan, HSA, Roth IRA, and taxable Bridge.
- The Cash Flow page therefore shows about $3,761 after planned debt, and about $261 remains after the $3,500 contribution route.

The round $40,000 tax amount remains a teaching estimate for the source equation. The current app result is $36,862 and should be used whenever the screen itself is being read.

## Debt

| Output | Engine result |
|---|---:|
| Total debt | $298,000 |
| Required monthly payments | $1,833 |
| DTI | 11.6% |
| DTA at reference valuation | 40.0% |
| Auto-loan payoff | 2027 · Alex age 46 |

The auto payoff includes the saved $500/month extra-principal strategy.

## Allocation — current app denominator

The Allocation page excludes the primary residence and beneficiary-restricted 529 from the target-allocation denominator.

| Scope | Amount |
|---|---:|
| Total financial balances including the 529 | $295,000 |
| 529 excluded from target allocation | $25,000 |
| Allocatable portfolio used by the app | $270,000 |
| Bitcoin | $175,000 |
| Current Bitcoin allocation | 64.8% |
| Target | 50% |
| Review band | 40–60% |

The household is above the review band. That triggers a review, not an automatic taxable sale. The first response can route new money away from Bitcoin; any sale remains a separate tax and planning decision.

### Drawdown

| Output | Amount |
|---|---:|
| Bitcoin loss in a 75% drawdown | $131,250 |
| Allocatable portfolio after the Bitcoin loss, other holdings flat | $138,750 |
| Total financial balances including the excluded 529 after the same loss | $163,750 |

Every lesson and visual must name the denominator.

## Tax roadmap status

The engine produced a year-by-year roadmap, but the demo still has incomplete basis:

- 1.25 BTC with $48,000 known basis
- 0.40 BTC with reconstruction pending
- 0.10 BTC with missing records

Keep projected tax qualified until the basis record and external CPA review are complete. Distant-year values are assumption-sensitive planning results, not return-preparation amounts or promises.

Selected current engine values include:

| Year / age | Taxes | Debt payments | Spending | Net worth |
|---|---:|---:|---:|---:|
| 2026 / 45 | $36,862 | $27,996 | $80,000 | $769,642 |
| 2036 / 55 | $10,632 | $17,400 | $129,912 | $4,522,924 |
| 2048 / 67 | $6,520 | $14,036 | $191,610 | $22,526,200 |
| 2056 / 75 | $12,261 | $0 | $242,726 | $60,109,946 |

Use the roadmap to teach direction and planning windows. Do not turn distant precision into a headline.

## First retirement calendar year — fully reconciled candidate

Retirement begins in March 2036, so the first retirement calendar year includes two months of pre-retirement wages plus the first year of inflation-adjusted part-time income.

| Component | Engine result |
|---|---:|
| Base living spending, inflation-adjusted | $129,912 |
| College expense active that year | $13,439 |
| Living need including life event | $143,351 |
| Remaining debt payments | $17,400 |
| Taxes | $10,632 |
| **Total need** | **$171,383** |
| Partial-year earned income before retirement date | $42,557 |
| Inflation-adjusted part-time income | $26,878 |
| **Recurring income** | **$69,435** |
| **Total draw from accounts** | **$101,948** |
| Rounded source total | $101,946 |

The $2 difference is display rounding.

### Funding sources

| Source | Amount |
|---|---:|
| Cash | $2,200 |
| Stocks | $1,800 |
| Bitcoin | $97,900 |
| **Taxable accounts total** | **$101,946** |

| Bitcoin result | Amount |
|---|---:|
| Bitcoin sale dollars | $97,948 |
| Projected Bitcoin price in 2036 | $1,235,921 |
| Bitcoin sold | 0.079251 BTC |

This corrects the earlier fixed-price quantity error. The quantity now uses the projected retirement-year Bitcoin price.

The lesson should name why the first calendar year contains partial wages, part-time income, college, debt, and tax. Otherwise the app numbers look like hidden calculations.

## Stress Scenario

| Output | Engine result |
|---|---:|
| 4% inflation confidence at age 55 | 91.6% |
| Change versus the 3% baseline | −3.0 percentage points |

Use this to teach sensitivity: higher inflation lowers confidence. Do not use the distant ending estate as the main decision result.

## Known hold outside the engine

Protect remains a UI and real-world checkpoint. The projection engine cannot prove:

- a wallet backup works,
- another family member can recover,
- legal documents are valid,
- a provider accepted a beneficiary change,
- or an insurance contract supplies the stated coverage.

## Acceptance status

Completed:

- [x] Reconcile the result with Cash Flow math.
- [x] Reconcile the Allocation denominator and excluded holdings.
- [x] Reconcile the first-year funding equation and source split.
- [x] Correct Bitcoin units sold using the projected retirement-year price.
- [x] Publish a successful deployed preview containing the current result artifacts.

Still required before final receipts:

- [ ] Open the deployed pages and confirm labels, rounding, saved/preview state, and displayed values.
- [ ] Capture screenshots or recording references for the eight checkpoints.
- [ ] Complete Protect using UI status plus real-world evidence boundaries.
- [ ] Record exact Build Your Plan step IDs, routes, completion rules, and save behavior after Austin uses the deployed flow.
- [ ] Apply outside CPA, custody, estate-attorney, and insurance corrections.
- [ ] Rerun Academy audits after accepted values are propagated into the course.
