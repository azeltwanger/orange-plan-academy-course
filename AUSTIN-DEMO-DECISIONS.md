# Austin's demo-household decisions

**Status:** approved by Austin on 2026-08-19; first app-engine decision applied on 2026-08-20  
**Input authority:** `DEMO-HOUSEHOLD.md`  
**Output authority:** accepted receipts under `demo/` and `DEMO-CHECKPOINT-RUN-SHEET.md`

These decisions are locked for `demo-v1-inputs`. They are fictional teaching choices, not universal recommendations. Any future change must be made in the demo source first and then propagated through app checkpoints, scripts, lesson text, slides, and walkthroughs.

## Approved decision set

| # | Decision | Approved value | Status |
|---:|---|---|---|
| 1 | Fictional household | **Alex, 45 · Jordan, 43 · two children, 10 and 12 · Colorado · married filing jointly** | APPROVED |
| 2 | Broad assumptions | **Built-in Power Law Bitcoin view · current standard app defaults for stocks/bonds/cash/real estate · 3% baseline inflation** | APPROVED |
| 3 | Inflation stress test | **4% inflation as a saved Scenario, not the baseline** | APPROVED |
| 4 | Retirement target | **Alex retires at 55 · $100,000 annual retirement living spending in today's dollars · planning age 95 · Plan confidence target 80%** | APPROVED |
| 5 | Spouse retirement timing | **The current app applies age 55 to each spouse's earned-income timeline, so Jordan continues working for two years after Alex retires** | APP INTERPRETATION — VERIFY IN UI |
| 6 | Early-retirement work | **Alex earns $20,000/year in today's dollars for the first 3 retirement years, then it ends** | APPROVED |
| 7 | Social Security timeline | **Alex: $30,000/year at age 67 · Jordan: $22,000/year when Jordan reaches 67 two years later; both entered in today's dollars** | APPROVED |
| 8 | Bitcoin allocation | **50% target · 40–60% review band** | APPROVED |
| 9 | Household debt ceiling | **Do not intentionally exceed 25% DTI; do not add debt when DTA is 40% or higher** | APPROVED |
| 10 | Tax-advantaged route | **$625/month to Alex's family HSA · $625/month to Jordan's Roth IRA** | APPROVED |
| 11 | HSA job | **Healthcare Bridge for qualified costs before and early in retirement** | APPROVED |
| 12 | Starting retirement paycheck | **Keep the deliberate $100,000/year Plan amount. The first engine checkpoint measures it at 94.6%, versus approximately $99,317 Conservative / 95%, $170,216 Balanced / 80%, and $249,904 Aggressive / 60%.** | APPROVED FROM ENGINE CHECKPOINT · UI VERIFY |
| 13 | College | **Keep the optional $80,000 total family commitment in the continuous household** | APPROVED |
| 14 | Core borrowing rule | **Exclude borrowing from the saved Core baseline; compare it only in gated Advanced when relevant** | APPROVED |

## Why the demo keeps $100,000 instead of selecting $170,216

The household chose a $100,000 retirement lifestyle before seeing the spending cards. The engine result shows that amount is already near the 95% Conservative reference.

The Academy should not teach the Balanced card as an instruction to increase spending until confidence falls to 80%. The cards show available choices. The household still decides which lifestyle it wants to fund. In this demo, the current $100,000 amount is deliberate and remains the saved starting paycheck.

## Fixed reconciled inputs

These remain unchanged unless the fictional household itself is redesigned:

- $190,000 gross household income
- $80,000 current living spending, excluding debt payments
- $40,000 round teaching tax estimate pending Cash Flow UI comparison
- $22,000 required annual debt payments
- $4,000 monthly repeatable route
- $5,000 bare-bones monthly spending
- 6-month / $30,000 working reserve
- 1.75 BTC, $75,000 stocks, $15,000 bonds, and $30,000 cash at the illustrative starting valuation
- $280,000 mortgage and $18,000 auto loan
- $500 monthly extra principal to the auto loan
- $750 workplace contribution to capture the assumed employer match
- $1,500 taxable Bridge / investment route
- $35,000 vehicle ceiling in 5 years with $20,000 left to accumulate
- 1.25 BTC / $48,000 known basis, 0.40 BTC reconstruction pending, and 0.10 BTC unknown
- no Bitcoin-backed loan in the saved Core household

## First engine outputs now available

See `demo/ENGINE-CHECKPOINT-CANDIDATE-4456b3c.md`.

The current engine reports:

- 94.6% confidence at Alex age 55
- earliest 80% target-qualified date in May 2032, Alex age 51
- current app allocation of 64.8% Bitcoin because the 529 is excluded from the target-allocation denominator
- $100,000 current spending at 94.6% confidence
- first-retirement-year total draw of approximately $101,948 before final UI verification

## Next step

1. Finish the expanded provenance diagnostic.
2. Verify every candidate output in the deployed UI.
3. Capture the eight final checkpoint receipts.
4. Apply the external professional corrections.
5. Give Austin the scripts for one final voice-and-judgment read.

No additional dictation is required to lock these inputs or the $100,000 starting-paycheck decision.
