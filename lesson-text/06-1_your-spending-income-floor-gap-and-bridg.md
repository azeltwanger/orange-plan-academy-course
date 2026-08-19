# Build the retirement spending target, income floor, and portfolio gap

## Retirement spending

Retirement spending is annual living spending. It excludes debt payments already modeled separately.

The demo household uses:

- Current living spending: $80,000 per year
- Retirement living spending: $100,000 per year in today's dollars

The higher retirement amount reflects a deliberately different active-retirement lifestyle. Dated large costs belong in life events rather than being counted twice.

## Income floor

The floor is recurring income arriving without asset sales.

Demo inputs:

- $20,000 of part-time income for the first 3 retirement years
- About $52,000 of later durable income beginning at age 67

Use real start and end dates. The floor changes over time.

## Portfolio-funded gap

**Living spending − recurring income = portfolio-funded living gap**

- First 3 retirement years: $100,000 − $20,000 = $80,000 before taxes, remaining debt, events, or refill
- After later income begins: $100,000 − $52,000 = $48,000 before other costs

## Total draw

The Income page adds spending, tax, debt costs, life events, and reserve refill, then subtracts recurring income. The result is the total draw from accounts.

Canonical taxes, total draw, and source split must come from the current demo checkpoint rather than script estimates.

## Bridge years

Review the income bridge year by year. A separate account-access bridge may exist, but do not assume every retirement account follows one universal age rule.

## Cash buffer

Cash Flow owns reserve basis and target months. Income shows current funding in months of that basis.

## Where the numbers come from

### Spending

- **What it means:** annual living-spending target
- **Calculated from:** saved Plan spending and life events
- **Edit source:** Plan and event records
- **This affects:** cash need, confidence, earliest date, tax, and withdrawals

### Recurring income

- **What it means:** income without portfolio sales
- **Calculated from:** verified sources and dates
- **Edit source:** income records
- **This affects:** gap, Bridge, total draw, tax, and reserve

### Total draw

- **What it means:** amount needed from accounts
- **Calculated from:** spending, tax, debt, events, refill, and recurring income
- **Edit source:** underlying source lines
- **This affects:** sales, Bitcoin retained, tax, loans, and long-term results

## Done when

The household can explain spending, income floor, gap, total draw, and accessible Bridge funding.
