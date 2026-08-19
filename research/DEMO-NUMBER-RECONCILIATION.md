# Demo-number reconciliation

**Status:** source-input reconciliation complete; app-calculated outputs held for checkpoint run  
**Authority:** `DEMO-HOUSEHOLD.md`

This file records what has been reconciled and prevents an older example from quietly replacing the continuous household.

## Rules

1. `DEMO-HOUSEHOLD.md` owns every continuous-demo input.
2. A script, lesson, slide, or walkthrough may not change one input locally.
3. A separate teaching example is labelled **illustrative — not the demo household**.
4. Confidence, tax, withdrawal, Bitcoin-sale, estate, and Scenario outputs come from the current app checkpoint, not from prose.
5. When a demo input changes, update the household file first, rerun every affected checkpoint, and then update course assets.

## Working household

| Area | Current canonical input |
|---|---|
| Household | Alex age 45, Jordan age 43, two children ages 10 and 12; names and Colorado state remain Austin decisions |
| Income | $150,000 + $40,000 = $190,000 gross |
| Current living spending | $80,000/year, debt excluded |
| Bare-bones spending | $60,000/year · $5,000/month |
| Teaching tax estimate for cash-flow reconciliation | $40,000/year; replace with current engine output if materially different |
| Required debt payments | $22,000/year · about $1,833/month |
| Reliable surplus | $48,000/year · $4,000/month |
| Retirement living spending | $100,000/year in today's dollars; deliberately higher than current spending and still awaiting Austin confirmation |
| Planned retirement age / planning age | 55 / 95 |
| Confidence target | 80% with 1,000 test runs |
| Part-time retirement income | $20,000/year for first 3 retirement years; proposed |
| Later durable income | $52,000/year in today's dollars beginning at age 67; proposed |

## Balance-sheet reconciliation

At the **illustrative** $100,000 Bitcoin price:

| Holding / asset | Value |
|---|---:|
| Bitcoin · 1.75 BTC | $175,000 |
| Stocks | $75,000 |
| Bonds | $15,000 |
| Cash | $30,000 |
| **Investable assets** | **$295,000** |
| Residence | $450,000 |
| **Gross assets** | **$745,000** |

| Debt | Value |
|---|---:|
| Mortgage | $280,000 |
| Auto loan | $18,000 |
| **Total debt** | **$298,000** |
| **Illustrative net worth** | **$447,000** |

Checks:

- Bitcoin allocation: $175,000 ÷ $295,000 = **59.3%** of investable assets
- Whole-gross-asset exposure: $175,000 ÷ $745,000 = **23.5%**
- DTA: $298,000 ÷ $745,000 = **40.0%**
- DTI: $1,833 ÷ $15,833 = about **11.6%**
- 75% Bitcoin decline: $175,000 × 75% = **$131,250** temporary Bitcoin loss before other assets move

The live Bitcoin price changes current values, allocation, DTA, and drawdown dollars. Recorded walkthroughs use the checkpoint date and visible price.

## Cash-flow and routing reconciliation

`$190,000 income − $40,000 estimated tax − $80,000 living − $22,000 required debt = $48,000/year = $4,000/month`

Reserve:

`$5,000 bare-bones basis × 6 months = $30,000 target`

Monthly route:

| Destination | Amount |
|---|---:|
| Workplace employee contribution | $750 |
| Auto-loan extra principal | $500 |
| HSA / Roth / additional traditional | $1,250 |
| Taxable Bridge and investment allocation | $1,500 |
| **Total** | **$4,000** |

Employer match is additional employer money and is not subtracted from the $4,000 household route.

The app checkpoint must verify that payroll contributions and the tax estimate do not double-count the employee deferral.

## Future-cost reconciliation

Vehicle in 5 years:

`$35,000 ceiling − $10,000 expected vehicle proceeds − $5,000 purchase-year cash flow = $20,000 to accumulate`

College is the total family commitment across both children unless Austin changes it:

`$25,000 existing 529 + $20,000 parent cash flow + $10,000 student/aid/defined borrowing + $25,000 remaining source = $80,000`

## Cost-basis reconciliation

| Quantity | Status |
|---:|---|
| 1.25 BTC | Complete lots; $48,000 known basis |
| 0.40 BTC | Exchange export available; reconstruction pending |
| 0.10 BTC | Records missing; basis unresolved |
| **1.75 BTC** | Current quantity reconciles |

No course asset may present a complete tax-sale result while the unresolved units remain part of the modeled sale.

## Custody and estate starting state

- 1.50 BTC on one hardware wallet
- 0.25 BTC exchange operating balance
- Recovery untested at the starting checkpoint
- Device and backup share one physical failure domain
- Alex understands the process; Jordan has not operated it
- One old workplace beneficiary record names a parent
- Executor, backup, legal-document status, heir letter, delivery path, and real insurance terms remain intentionally incomplete

The app may record readiness. The actual device, family, provider, legal, and policy process supplies proof.

## App-calculated outputs still held

Do not lock these from prose:

- confidence at planned age 55,
- earliest date reaching 80%,
- Conservative / Balanced / Aggressive / current-plan spending amounts,
- current engine tax estimate,
- year-by-year tax roadmap,
- first-retirement-year need and total draw,
- account and holding source split,
- Bitcoin sold and retained,
- retirement reserve months,
- ending assets and estate,
- Scenario deltas,
- and Protect readiness counts.

Capture them through `DEMO-CHECKPOINT-RUN-SHEET.md` after Austin approves the remaining inputs.

## Targeted Austin decisions

- Final fictional state and names
- Broad return preset and inflation
- Confirmation of age 55 and $100,000 retirement living spending
- Part-time and later durable-income assumptions
- HSA Bridge or Legacy job
- Bitcoin target and review band
- Household debt ceiling
- Exact split inside the $1,250 tax-advantaged route
- Starting-spending choice after the app calculates the bands
- Whether college remains in the continuous household
- Core borrowing excluded, with comparison only in Advanced

These decisions change app outputs across several modules. Settle them once before Austin reviews spoken wording.
