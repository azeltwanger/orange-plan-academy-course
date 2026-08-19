# Austin's demo-household decisions

**Purpose:** settle the small number of fictional planning choices that change calculated outputs across several modules. These are not script rewrites. Approve the recommendation or replace the value once, then the demo checkpoint run uses the result everywhere.

**Input authority after approval:** `DEMO-HOUSEHOLD.md`  
**Output authority after entry:** `DEMO-CHECKPOINT-RUN-SHEET.md`

## Recommended decision set

| # | Decision | Recommended default | Why this is the cleanest teaching choice | Austin |
|---:|---|---|---|---|
| 1 | Fictional household | **Alex, 45 · Jordan, 43 · two children, 10 and 12 · Colorado · MFJ** | Generic, not copied from a client; state tax remains visible without using Austin's own household | Approve / change |
| 2 | Broad assumptions | **Built-in Power Law Bitcoin view · current standard defaults for stocks/bonds/cash/real estate · 4% inflation** | Matches Austin's declining-Bitcoin-return preference and demonstrates a deliberately conservative spending assumption without customising every asset | Approve / change |
| 3 | Retirement target | **Age 55 · $100,000 annual retirement living spending in today's dollars · planning age 95 · Plan target 80%** | Creates a meaningful early-retirement Bridge and makes the retirement lifestyle intentionally different from the current $80,000 working-life spending | Approve / change |
| 4 | Early retirement work | **$20,000/year in today's dollars for the first 3 retirement years, then ends** | Demonstrates that income is a dated timeline and reduces the earliest Bridge without making work permanent | Approve / change |
| 5 | Social Security timeline | **Today's-dollar inputs: Alex $30,000/year at age 67 · Jordan $22,000/year when Jordan reaches 67 two years later** | Better than one combined $52,000 amount appearing while the younger spouse is 65; teaches staggered income starts and still reaches $52,000 combined | Approve / change |
| 6 | Bitcoin allocation | **50% target · 40–60% review band** | Current illustrative mix is 59.3%, so it sits near the upper edge and teaches target/band/action without forcing an automatic sale | Approve / change |
| 7 | Household debt ceiling | **Do not intentionally exceed 25% DTI; do not add debt when DTA is 40% or higher** | Leaves room below the app's outer bands and demonstrates that the household ceiling is more conservative than a product warning line. DTI uses required payments ÷ gross income; DTA uses debt ÷ gross assets. | Approve / change |
| 8 | Tax-advantaged part of the route | **$625/month to Alex's family HSA · $625/month to Jordan's Roth IRA** | Adds exactly to the existing $1,250 route and stays within the 2026 under-50 IRA limit while preserving a simple HSA/Roth comparison. Demo assumes HSA eligibility and no employer HSA contribution. | Approve / change |
| 9 | HSA job | **Healthcare Bridge** | The household retires before Medicare and may use qualified HSA funds for the healthcare portion of the Bridge; it is not presented as unrestricted spending money | Approve / change |
| 10 | Starting retirement paycheck | **Use the calculated Balanced 80% amount unless the current $100,000 Plan amount already falls inside the accepted range and is the deliberate household choice** | Preserves the lesson's actual decision instead of forcing a number before the app calculates the bands | Decide after `demo-v1-income` |
| 11 | College | **Keep the optional $80,000 total family commitment in the continuous household** | Gives the known-cost lesson a realistic long-horizon example; it remains optional for learners and is not unlimited tuition | Approve / change |
| 12 | Core borrowing rule | **Excluded from the saved core baseline; compare only in gated Advanced** | The core retirement plan should work without lender, interest, LTV, liquidation, collateral, and estate risk | Approve / change |

## Decisions already fixed by the reconciled model

These should not be reopened unless the fictional household itself changes:

- $190,000 gross household income
- $80,000 current living spending, debt excluded
- $40,000 teaching tax estimate pending engine comparison
- $22,000 required annual debt payments
- $4,000 reliable monthly surplus
- $5,000 bare-bones spending and 6-month / $30,000 working reserve
- 1.75 BTC, $75,000 stocks, $15,000 bonds, $30,000 cash at the illustrative starting balance sheet
- $280,000 mortgage and $18,000 auto loan
- $500 monthly auto-loan extra principal
- $750 workplace contribution to capture the assumed match
- $1,500 taxable Bridge / investment route
- $35,000 vehicle ceiling in 5 years with $20,000 left to accumulate
- 1.25 BTC / $48,000 known basis, 0.40 BTC reconstruction pending, 0.10 BTC unknown
- no Bitcoin-backed loan in the saved core household

## What happens after approval

1. Replace every `proposed` or `Austin approval pending` marker in `DEMO-HOUSEHOLD.md`.
2. Update the phased Social Security sources in Lessons 6.1 and the matching lesson text.
3. Enter the household once in the accepted app build.
4. Capture the eight checkpoint receipts.
5. Replace every app-output placeholder in scripts and slides with the accepted receipt value.
6. Apply external professional corrections.
7. Give Austin the scripts for one final voice-and-judgment read.

No spoken dictation is needed to approve this page. A simple list of changed row numbers is enough.
