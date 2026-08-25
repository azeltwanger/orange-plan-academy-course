# Demo-number reconciliation

**Status:** approved inputs and reproducible engine candidate reconciled; deployed UI receipts pending  
**Input authority:** `../DEMO-HOUSEHOLD.md`  
**Engine candidate:** `../demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md`  
**Visual values:** `../demo/VISUAL-DATA-RECEIPT-3105664.md`

This file records the reconciliation logic behind the continuous fictional household. It prevents an old deck, placeholder script, or one-off example from replacing the current demo without an explicit change.

## Rules

1. Austin-approved decisions begin in `AUSTIN-DEMO-DECISIONS.md`.
2. `DEMO-HOUSEHOLD.md` owns the human-readable continuous demo.
3. `demo/demo-v1-inputs.json` mirrors the source inputs for automation.
4. Orange Plan owns confidence, tax, payoff, Allocation scope, withdrawal, Bitcoin-sale, Scenario, and report outputs.
5. The current engine candidate may finish script arithmetic and visual briefs.
6. Final screenshot-level claims require the deployed UI to confirm labels, rounding, source rows, and Saved / Previewing / Scenario state.
7. A separate example must say **illustrative — not the demo household**.
8. When an input changes, update the source, rerun the engine and affected UI receipt, then update scripts, lesson text, visuals, and walkthroughs.

---

# Approved household and assumptions

| Area | Canonical value |
|---|---|
| Household | Alex 45; Jordan 43; two children 10 and 12; Colorado; married filing jointly |
| Retirement timing | One household retirement start, displayed using Alex's age; Alex 55 in March 2036 |
| Planning age | 95 |
| Gross income | Alex $150,000 + Jordan $40,000 = $190,000 |
| Current living spending | $80,000/year, debt excluded |
| Bare-bones spending | $60,000/year · $5,000/month |
| Retirement living spending | $100,000/year in today's dollars |
| Bitcoin return view | Built-in Power Law |
| Other broad returns | Current app defaults, recorded with the accepted receipt |
| Baseline inflation | 3% |
| Stress inflation Scenario | 4% |
| Plan confidence target | 80% with 1,000 test runs |
| Part-time income | Alex $20,000/year in today's dollars for first 3 retirement years |
| Social Security | Alex $30,000 at 67; Jordan $22,000 when Jordan reaches 67 two years later |
| Saved starting paycheck | $100,000/year |
| Borrowing | Excluded from saved Core; gated Advanced comparison only |

## Household retirement-date correction

The current model does not use a separate spouse-retirement-age control for this plan.

- The retirement date is one household earned-income transition.
- The displayed age is Alex's because Alex is the primary person.
- A March retirement date creates partial-year household wages in 2036.
- Jordan does not retain W-2 income for two extra years merely because Jordan is younger.
- Each spouse's Social Security still has its own start age.

This correction is now reflected in Lessons 1.3 and 6.1 and in the course/app contract.

---

# Balance sheet and Allocation scope

At the controlled $100,000 Bitcoin reference price:

| Holding / asset | Value | App target-allocation scope |
|---|---:|---|
| Bitcoin · 1.75 BTC | $175,000 | Included |
| Stocks outside 529 | $55,000 | Included |
| Bonds outside 529 | $10,000 | Included |
| Cash | $30,000 | Included |
| 529 stocks and bonds | $25,000 | Excluded: beneficiary-restricted |
| Primary residence | $450,000 | Excluded: primary residence |

Three valid denominators:

| Scope | Total | Bitcoin percentage |
|---|---:|---:|
| **Orange Plan allocatable portfolio** | **$270,000** | **64.8%** |
| Financial balances including 529 | $295,000 | 59.3% |
| Gross assets including home | $745,000 | 23.5% |

The app target-allocation decision uses $270,000. The 529 is already committed to the children and should not make the retirement allocation look less concentrated.

Approved target and band:

- Bitcoin target: 50%
- Review band: 40–60%
- Current 64.8%: above band
- Product/course response: review, not automatic taxable sale

75% Bitcoin drawdown:

- Bitcoin loss: $131,250
- App allocatable portfolio after loss, other holdings flat: $138,750
- Financial balances including 529 after loss: $163,750

---

# Cash Flow and routing

## Concept equation

The simple lesson uses a round tax estimate:

> $190,000 income − $40,000 tax − $80,000 living − $22,000 required debt = $48,000/year · $4,000/month

That is a teaching reconciliation, not the exact page headline.

## Current app interpretation

| Item | Engine candidate |
|---|---:|
| Current modeled tax | $36,862/year |
| Required debt | $1,833/month |
| Saved extra auto principal | $500/month |
| Planned Debt shown by Cash Flow | $2,333/month |
| Capacity before the extra-debt decision | $4,261/month |
| Displayed post-debt surplus | $3,761/month |
| Account contribution route | $3,500/month |
| Operating cushion | $261/month |

The full household decision remains:

> $500 extra debt + $3,500 account contributions = $4,000/month

The extra $500 is already inside Cash Flow's Debt line. It cannot be subtracted or routed again.

## Account route

| Destination | Household dollars / month |
|---|---:|
| Auto-loan extra principal | $500 |
| 401(k) employee contribution | $750 |
| Family HSA | $625 |
| Spousal Roth IRA | $625 |
| Taxable Bridge / saved allocation | $1,500 |
| **Full decision** | **$4,000** |

The assumed $375/month employer match is separate employer money.

---

# Debt

| Item | Candidate |
|---|---:|
| Mortgage | $280,000 · 3.25% · $1,450/month required only |
| Auto loan | $18,000 · 7% · about $383 required + $500 extra |
| Total debt | $298,000 |
| DTI | 11.6% |
| DTA at reference valuation | 40.0% |
| Auto payoff | 2027 · Alex age 46 |

Approved fictional household rule:

- keep DTI below 25%,
- add no new debt at 40%+ DTA.

The rule is separate from the app's general warning bands.

---

# Future costs

Vehicle in 5 years:

> $35,000 ceiling − $10,000 vehicle proceeds − $5,000 purchase-year cash flow = $20,000 remaining source

College commitment across both children:

> $25,000 existing 529 + $20,000 parent cash flow + $10,000 student/aid/accepted borrowing + $25,000 remaining source = $80,000

The first retirement calendar year still contains one college payment. That life event is part of why the first-year need is higher than Base living spending.

---

# Cost basis

| Quantity | Status |
|---:|---|
| 1.25 BTC | Complete lots · $48,000 known basis |
| 0.40 BTC | Exchange export available · reconstruction pending |
| 0.10 BTC | Records missing · unknown |
| **1.75 BTC** | Current quantity reconciles |

The funding equation can reconcile while the tax result remains incomplete. No course asset may call the sale filing-grade until unresolved basis is handled and the CPA review is applied.

---

# Reconciled app-owned outputs

## Baseline and confidence

| Output | Candidate |
|---|---:|
| Confidence at household retirement date, Alex 55 | 94.6% |
| Earliest date reaching 80% | May 2032 · Alex 51 |
| Boundary confidence | 80.0% |

## Starting-spending choices

| Choice | Candidate |
|---|---:|
| Conservative / 95% | $99,317/year |
| Current Plan | $100,000/year at 94.6% |
| Balanced / 80% | $170,216/year |
| Aggressive / 60% | $249,904/year |

The household keeps $100,000 because that is the lifestyle it chose. Capacity is not a command to maximize spending.

## First retirement calendar year

| Component | Candidate |
|---|---:|
| Base living, inflation-adjusted | $129,912 |
| College event | $13,439 |
| Living need | $143,351 |
| Debt | $17,400 |
| Tax | $10,632 |
| **Total need** | **$171,383** |
| Partial-year household wages | $42,557 |
| Inflation-adjusted part-time income | $26,878 |
| **Recurring income** | **$69,435** |
| **Total draw** | **$101,948** |

Holding sources:

- cash: about $2,200,
- stocks: about $1,800,
- Bitcoin: about $97,900,
- rounded taxable-account source total: $101,946.

Bitcoin sale:

- proceeds: $97,948,
- projected 2036 Bitcoin price: $1,235,921,
- quantity sold: 0.079251 BTC.

The dollars, projected price, and quantity must come from the same modeled year.

## Inflation Scenario

| Output | Candidate |
|---|---:|
| 3% baseline confidence | 94.6% |
| 4% Scenario confidence | 91.6% |
| Difference | −3.0 percentage points |

The Scenario teaches direction and sensitivity. It does not create an unreported earliest-date or estate delta.

---

# Real-world and external holds

The projection engine cannot prove:

- wallet recovery,
- another family member's capability,
- legal-document validity,
- provider acceptance of a beneficiary change,
- or insurance coverage under an actual contract.

The deployed UI still must confirm:

- visible labels and rounding,
- page routes,
- Saved / Previewing / Scenario state,
- source-line drill-down,
- Protect checklist behavior,
- report/PDF/export behavior,
- and safe screenshot evidence.

Actual outside CPA, custody, Colorado estate-attorney, and insurance reviews remain not sent.

## Current decision status

There are no remaining demo-input decisions before Austin's voice pass. The remaining holds are UI evidence, external professional corrections, Build Your Plan walkthrough verification, and Austin's final wording/judgment approval.
