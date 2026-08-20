# Orange Plan Academy — app-engine checkpoint candidate

**Status:** engine-generated; deployed UI verification still required  
**App commit:** `4456b3c954ea29630b4d9c73aff6a52711cfad15`  
**Fixture:** `demo-v1-inputs`  
**As-of date:** 2026-08-20  
**BTC reference price:** $100,000  
**Monte Carlo:** 1,000 runs · seed `20260820`  
**Generated:** 2026-08-20T14:50:48.375Z

This file records app-owned outputs from the reproducible Academy generator. It is not yet the final UI receipt. A spoken script may use an output only after the value is either confirmed in the deployed interface or explicitly described as an engine checkpoint.

## Baseline and confidence

| Output | Engine result |
|---|---:|
| Planned retirement date | March 2036 · Alex age 55 |
| Planned retirement spending | $100,000/year in today's dollars |
| Plan confidence target | 80% |
| Confidence at the planned date | 94.6% |
| Earliest date reaching 80% | May 2032 · Alex age 51 |
| Confidence at the earliest boundary | 80.0% |

### Teaching decision

The saved starting retirement paycheck remains **$100,000/year**.

The engine calculates approximately:

- Conservative / 95%: **$99,317**
- Balanced / 80%: **$170,216**
- Aggressive / 60%: **$249,904**
- Current $100,000 Plan amount: **94.6%**

The household does not raise its lifestyle to $170,216 merely because the plan can model it. The $100,000 amount is the lifestyle it deliberately chose and sits almost exactly at the conservative reference. This is the course example for why the spending cards are choices rather than an instruction to maximize spending.

## Cash Flow candidate

| Output | Engine result / course treatment |
|---|---:|
| Gross income | $190,000/year |
| Current living spending | $80,000/year |
| Required debt payments | Approximately $22,000/year |
| Engine current-year tax | $36,862 |
| Round teaching tax estimate | $40,000 |
| Round reliable route | $4,000/month |

The $40,000 tax figure remains a round teaching estimate. The current engine result implies more than $4,000 is available before flexible routing, so the $4,000 route should be described as a deliberate repeatable amount rather than the exact maximum calculated surplus. The Cash Flow UI still needs to confirm its displayed monthly number and whether it shows required debt only or includes the saved extra-principal route.

## Debt

| Output | Engine result |
|---|---:|
| Total debt | $298,000 |
| Required monthly payments | $1,833 |
| DTI | 11.6% |
| DTA at the reference valuation | 40.0% |
| Auto-loan payoff | 2027 · Alex age 46 |

The auto payoff reflects the required payment plus the saved $500/month extra-principal strategy.

## Allocation — denominator correction

The current Allocation engine excludes the primary residence and beneficiary-restricted education account from the household target-allocation denominator.

| Scope | Amount |
|---|---:|
| Total financial/investment balances including the 529 | $295,000 |
| Education account excluded from target allocation | $25,000 |
| **Allocatable portfolio used by the app** | **$270,000** |
| Bitcoin | $175,000 |
| Current Bitcoin allocation | 64.8% |
| Target | 50% |
| Review band | 40–60% |

The household is **above** the review band rather than merely near its upper edge. This triggers a review, not an automatic sale. New contributions can be routed away from Bitcoin first; any taxable rebalance remains a separate tax and planning decision.

### Drawdown

| Output | Amount |
|---|---:|
| Bitcoin loss in a 75% drawdown | $131,250 |
| Allocatable portfolio after that Bitcoin loss, other holdings flat | $138,750 |
| Total financial balances including the excluded 529 after the same loss | $163,750 |

The lesson must name which denominator it is showing.

## Tax roadmap status

The engine produced a year-by-year tax roadmap, but 0.50 BTC still has unresolved basis. Keep the projected tax qualified until the basis and external CPA review are complete.

Current known record:

- 1.25 BTC with $48,000 of known basis
- 0.40 BTC with reconstruction pending
- 0.10 BTC with missing records

Do not treat the roadmap as a filed return or use distant-year values as precise promises.

## First retirement year — candidate equation

| Output | Engine result |
|---|---:|
| Year / Alex age | 2036 / 55 |
| Living need, including active life events | $143,351 |
| Total need, including tax and debt | $171,383 |
| Recurring income | $69,435 |
| Total draw from accounts | $101,948 |
| Account source | Taxable accounts |
| Rounded source total | $101,946 |
| Bitcoin sale dollars | $97,948 |

The $2 source difference is display rounding.

The income and spending components are being expanded in a second provenance diagnostic before the course uses this equation. The current result appears to include Jordan's continued wages, Alex's part-time income, and an overlapping college cost. Those components must be named on screen so $69,435 and $143,351 do not look like unexplained hidden numbers.

**Do not use the current generated `1 BTC sold` quantity.** The first generator divided the future sale dollars by the fixed $100,000 reference price rather than the projected 2036 Bitcoin price. The dollar sale is app-owned; the correct quantity is pending the provenance diagnostic.

## Final and stress results

| Output | Engine result |
|---|---:|
| 4% inflation Scenario confidence at age 55 | 91.6% |
| Change versus 3% baseline | −3.0 percentage points |
| Ending modeled net worth at age 95 | $428,365,615 |

The very large distant ending value is assumption-sensitive and is not a decision headline for Core. Use the 4% Scenario primarily to teach direction and sensitivity, not to promise a future estate value.

## Remaining acceptance work

- [ ] Run the provenance diagnostic for first-year spending and income components.
- [ ] Correct the projected Bitcoin quantity sold.
- [ ] Confirm Cash Flow's actual displayed tax and surplus.
- [ ] Compare every candidate value with the deployed page.
- [ ] Capture screenshots and the save/preview state.
- [ ] Create the eight final receipts using `demo/checkpoint-receipt.schema.json`.
- [ ] Rerun the Academy audits after accepted values are propagated.
