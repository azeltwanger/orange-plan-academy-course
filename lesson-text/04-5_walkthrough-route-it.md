# Walkthrough: route your surplus and investments

<!-- PLAN-LIFECYCLE:LESSON-TEXT -->

This walkthrough takes the surplus built in Module 2, subtracts the Reserve and extra-debt routes chosen in Modules 2 and 3, directs the amount left into contribution accounts, tells Orange Plan what each account buys, and then turns the modeled plan into real payroll and recurring-transfer instructions.

## Before you start

- Finish the Module 2 Cash Flow and Reserve work.
- Enter every debt and any extra-payment amount in Module 3.
- Complete the Module 4 decisions about Bitcoin allocation, timeframes, next-dollar priority, and asset location.
- Make sure the real accounts and current holdings are already in Foundation.

## 1. Start with the amount that exists

Open **Cash Flow → This month** and read the real monthly surplus.

Then open **Routing · waterfall order** and read all three claims:

1. **Cash reserve**
2. **Extra debt**
3. **Contributions**

The number beside Contributions is the pool available to the contribution accounts. Do not enter the original surplus into every account.

A current deficit routes $0 now, but Reserve and contribution settings remain editable and can apply in later modeled years when cash flow supports them.

## 2. Set the portfolio destination first

On **Strategy → Allocation**:

1. Verify what each account currently holds.
2. Assign accounts to **Reserve**, **Bridge**, or **Legacy**.
3. Save a target mix totaling 100%.
4. Set a drift band you would actually act on.

A known cost five to ten years away may still use Bitcoin as part of the funding source. The committed portion should become less Bitcoin-dependent as the date approaches. The life event holds the cost, Bridge holds the protected amount, and Bitcoin can remain the Legacy source until a planned sale moves dollars into Bridge.

## 3. Add the contribution destinations

Return to **Cash Flow → Routing → Contributions**.

Use **+ Add account type** for the accounts that belong in the plan.

> **Important:** this adds a contribution row to Orange Plan. It does not open the real account.

The current app supports account types including employer plans, IRAs, HSA, self-employed plans, 529, UTMA/UGMA, and taxable brokerage.

## 4. Choose an amount rule for every account

Non-taxable contribution rows may offer:

- **Custom $/mo**
- **Fill to match**
- **Max**

Taxable brokerage offers:

- **Leftover**
- **Fixed**

The app applies active fixed routes in the displayed account order. Taxable **Leftover** receives what remains. When the requested amounts exceed the available contribution pool, later rows show **limited by available surplus**.

The displayed account order is app mechanics, not a universal financial-planning rule. The amounts and active rows should reflect the next-dollar policy chosen in lesson 4.3.

## 5. Configure employer-plan details

For a supported employer plan, enter:

- match rate
- match up to % of pay
- contribution mode
- Traditional, Split, or Roth employee-deferral treatment

**Fill to match** requires a salary income source for the owner and a complete match formula.

In the current app, the employee-deferral tax split is shared across 401(k), spouse 401(k), and 403(b) contributions. Employer match is modeled as Traditional.

## 6. Choose what every account buys

Each contribution row has a **How it invests** choice:

- **Current mix:** new modeled contributions follow the account's current holdings mix.
- **Set mix:** enter Bitcoin, stocks, bonds, cash, and other percentages totaling 100%.
- **Choose holdings:** route percentages to eligible existing holdings, a named new security, or an asset bucket.

These are projection instructions. Adding a security here does not buy it, open the account, or prove the outside provider offers it.

## 7. Reconcile the full contribution pool

Collapse the rows and read the amount actually routed to each account.

Confirm that:

- the routed amounts add to the Step 3 contribution pool;
- no **limited by available surplus** warning is being ignored;
- taxable **Leftover** receives only the actual remainder;
- every active account has a deliberate investment route.

When requests are larger than the pool, reduce an amount, change the priority, increase surplus, or deliberately accept that the later route starts only when future cash flow supports it.

## 8. Make it real outside Orange Plan

Orange Plan models the plan. It does not move money, open accounts, change payroll, or place trades.

| Orange Plan route | Real implementation |
|---|---|
| 401(k), 403(b), 457(b), payroll HSA | Change payroll elections with the employer or plan administrator |
| IRA or taxable brokerage | Set a recurring transfer and purchase, or a dated monthly manual purchase |
| Bitcoin | Set a recurring purchase or monthly purchase process and the custody-transfer rule |
| 529 | Set the recurring contribution with the state plan or provider |
| Taxable **Leftover** | Use a monthly sweep after the month closes, or use a conservative fixed recurring amount |

Create a short implementation list with:

- account
- Orange Plan amount
- outside provider instruction
- investment purchased
- start date
- confirmation date

The outside provider may use a percentage of pay instead of a monthly dollar amount. Convert the annual target using the real pay schedule and verify the first paycheck.

## 9. Verify the first posted month

After the first payroll contribution or recurring purchase posts:

1. Update the real transaction or holding in Orange Plan.
2. Compare the actual amount with the saved route.
3. Confirm the account bought what the plan expected.
4. Correct the route or the outside automation when they do not match.

A saved plan setting is not proof that the money moved.

## 10. Review and stress-test

Run **Route with AI** after the routes are saved. Ask it to review the contribution plan against Reserve, debt, Bridge needs, target allocation, and account wrappers.

Then run the deep-drawdown scenario and ask whether the routing would force the household to stop contributions, raid the reserve, or sell an investment during the drawdown.

## Complete when

- [ ] The starting surplus is the real amount from Cash Flow.
- [ ] Reserve and extra-debt claims are visible before Contributions.
- [ ] Every usable contribution account has a deliberate mode and amount.
- [ ] The displayed routed amounts add to the contribution pool.
- [ ] Every active row says how the new money invests.
- [ ] Employer match and tax treatment are entered correctly.
- [ ] Accounts are assigned to Reserve, Bridge, and Legacy.
- [ ] The target mix totals 100% and the drift band is saved.
- [ ] Real payroll, transfer, and purchase instructions are active outside Orange Plan or have an assigned date and owner.
- [ ] The first posted contribution will be checked against the plan.

> **Current Build Your Plan limitation:** the Allocation area can show complete after timeframe assignments and target mix are saved. It does not independently prove that contribution routes or outside automations are complete. Use this checklist as the source of truth for that implementation step.
