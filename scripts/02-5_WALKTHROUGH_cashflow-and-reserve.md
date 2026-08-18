# 2.5 · WALKTHROUGH — Build cash flow and reserve

**WALKTHROUGH RUN SHEET · current-app rewrite · ~12 min**

> **DO** = the current app path  
> **SEE** = what to point at  
> **WHERE THIS NUMBER COMES FROM** = what it means · calculated from · edit source · this affects  
> **⚠** = the mistake to prevent
>
> Narrate naturally. This is not teleprompter prose.

---

## DEMO STATE

Carry the same household forward from Module 1.

| Item | Demo value |
|---|---:|
| Household income | $190,000/yr |
| Taxes | $40,000/yr |
| Living spending | $80,000/yr |
| Debt payments | $22,000/yr |
| Surplus | $48,000/yr · $4,000/mo |
| Normal living spending | about $6,667/mo |
| Bare-bones essentials | $5,000/mo |
| Cash reserve target | 6 months |
| Current reserve | $30,000 · fully funded |

**Before recording**

- [ ] The demo account contains the same income, spending, debts, accounts, and holdings used in Module 1
- [ ] At least 2 completed months of transactions are available if Verify Spending is being shown
- [ ] The reserve cash holding is visible on Dashboard
- [ ] The Plan confidence result from Module 1 has been run and saved
- [ ] Clean browser and notifications off

---

## DECISIONS FROM THE LESSONS

This walkthrough implements four decisions:

1. The household's believable monthly surplus
2. Normal living spending
3. Bare-bones monthly essentials
4. Reserve target months and monthly build cap

The app calculates the reserve target from the spending basis and target months. The student decides the inputs.

---

## □ 1 · Read this month's cash flow

**DO** Open **Cash Flow**.

**SEE** The page opens on the **This month** verdict:

- `You have $X/mo left to put to work`, or
- `Spending runs $X/mo ahead of income`

**SEE** The flow directly below it: **Income → Taxes → Living → Debt payments → Surplus**.

### WHERE THIS NUMBER COMES FROM — SURPLUS

- **WHAT IT MEANS:** the amount left after the current monthly obligations are covered.
- **CALCULATED FROM:** income − taxes − living spending − debt payments.
- **EDIT SOURCE:** the four expandable rows on Cash Flow, plus the debt records that feed Debt payments.
- **THIS AFFECTS:** reserve funding, extra-debt routing, contributions, and the retirement projection.

**⚠** Living is the household's living spending. It is not gross income and it does not include debt payments. The app already carries debt separately.

**SAY IN YOUR OWN WORDS:** The $4,000 is not a second number we typed. It is what is left after the four rows above it.

---

## □ 2 · Verify the four source rows

**DO** Expand each row one at a time:

1. **Income**
2. **Taxes**
3. **Living**
4. **Debt payments**

**SEE** Each row opens its own editor on the same page.

**DO** Confirm each income stream separately. For the demo household, show both earners rather than one combined mystery number.

**DO** Confirm the current tax payments and withholding.

**DO** Confirm Living is about $80,000 per year, or about $6,667 per month.

**SEE** Debt payments are pulled from the debts already entered. Do not rebuild the debt strategy here.

**⚠** If the surplus looks wrong, fix one source row and watch the verdict recalculate. Do not hunt for a surplus field. There is no surplus field.

---

## □ 3 · Check spending against completed months

**DO** Open the **Verify Spending** card and select **Review**.

**SEE** The drawer compares one completed-month spending figure with the Living amount saved in the plan. It also states how many months the figure averages.

**DO** Open **By month** and walk through 2 completed months.

**DO** For a transaction that should not count in the spending average, open its three-dot menu and choose **Ignore from Verify Spending**.

**SEE** The row stays visible, is struck through, and is labelled ignored.

**DO** Open the same menu and show **Include again**.

**⚠** There is no separate ignored-status filter. Do not tell students to leave the month and recover excluded items somewhere else.

**⚠** The spending review helps calibrate the saved Living amount. It does not silently replace the plan. Make the update deliberately when the completed-month evidence is better than the old estimate.

### WHERE THIS NUMBER COMES FROM — VERIFIED SPENDING

- **WHAT IT MEANS:** the average of the completed months and transactions currently counted by Verify Spending.
- **CALCULATED FROM:** the available completed-month transaction history after the user's included/ignored decisions.
- **EDIT SOURCE:** the Verify Spending drawer for transaction treatment; the Living row for the amount the plan uses.
- **THIS AFFECTS:** surplus, reserve sizing when current spending is the basis, and every projection that uses current spending.

---

## □ 4 · Set the reserve policy

**DO** Scroll to **Reserve settings** at the bottom of Cash Flow.

**SEE** Four controls:

1. **Target months**
2. **Reserve basis**
3. **Monthly build cap**
4. **Bare-bones essentials**

**DO** Enter **$5,000/mo** for Bare-bones essentials.

**DO** Select **Bare-bones** as the reserve basis.

**DO** Select **6 months**.

**DO** Set the monthly build cap. For the fully funded demo household, leave it at the amount the household would use if the reserve falls below target; use **$1,000/mo** for the demonstration.

**SEE** The page autosaves. Wait for **Saved ✓** before moving on.

**⚠** If Bare-bones is selected before an amount exists, the app warns that current spending is being used until the bare-bones number is entered.

### WHERE THIS NUMBER COMES FROM — RESERVE TARGET

- **WHAT IT MEANS:** the amount of cash the household wants available for the reserve's current job.
- **CALCULATED FROM:** selected spending basis × target months.
- **EDIT SOURCE:** Bare-bones essentials or Living, Reserve basis, and Target months in Reserve settings.
- **THIS AFFECTS:** whether Cash Flow routes money to the reserve first and how much surplus remains for debt and contributions.

**SEE** For the demo household: $5,000 × 6 months = **$30,000**.

**⚠** The app performs this multiplication and displays the target. The student's job is choosing the spending basis and number of months.

---

## □ 5 · Read the routing waterfall

**DO** Scroll to **Routing · waterfall order**.

**SEE** The order:

1. **Cash reserve**
2. **Extra debt**
3. **Contributions**

**SEE** The reserve row shows the current amount, target, and either `fully funded` or the estimated months to full.

**SEE** In the demo account, $30,000 of $30,000 is fully funded, so the current surplus routes past the reserve.

**⚠** Extra-debt decisions are made on **Strategy → Debt** and read here. Contribution account choices are managed in the contribution rows on Cash Flow. This is one waterfall using decisions owned by different pages.

### WHERE THIS NUMBER COMES FROM — AMOUNT ROUTED TO RESERVE

- **WHAT IT MEANS:** how much of the current surplus is being claimed by the reserve this month.
- **CALCULATED FROM:** reserve gap, monthly build cap, and the surplus available after current expenses.
- **EDIT SOURCE:** Reserve settings and the source rows that create the surplus.
- **THIS AFFECTS:** how much reaches Extra debt and Contributions.

---

## □ 6 · Confirm the reserve holding

**DO** Open **Dashboard** and find the exact cash or cash-equivalent holding used as the reserve.

**DO** Use the holding row's three-dot menu and select **Add shield** if it is not already marked.

**SEE** The holding receives the **Shield** marker.

**⚠** Mark the exact holding, not a vague account total. Cash may already count automatically; a treasury or money-market holding needs the plan to know it is reserve money.

**⚠** This action identifies which holding is doing the reserve job. It does not set target months. The policy lives in Cash Flow; the holding identity lives on Dashboard.

---

## □ 7 · Recheck the retirement result

**DO** Return to **Plan → Retirement**.

**SEE** If the saved cash-flow changes made the prior test stale, the confidence section shows **Recheck**.

**DO** Recheck the plan.

**SEE** Compare the result with the Module 1 starting snapshot.

**SAY IN YOUR OWN WORDS:** We did not type a new confidence number. We changed the inputs and policy that feed the plan, then ran the same test again.

### WHERE THIS NUMBER COMES FROM — THE UPDATED CONFIDENCE RESULT

- **WHAT IT MEANS:** the share of 1,000 test runs where the updated plan lasted through the planning age.
- **CALCULATED FROM:** the full saved plan, now including the corrected spending, surplus, and reserve policy.
- **EDIT SOURCE:** the source pages that own those inputs; the ring itself is not editable.
- **THIS AFFECTS:** whether the planned retirement age reaches the selected target and the earliest date that does.

---

## WHAT CHANGED

Before this module, the household had rough spending and a reserve balance.

After this module, it has:

- a $4,000 monthly surplus traced to four source rows,
- normal spending of about $6,667/mo,
- bare-bones essentials of $5,000/mo,
- a 6-month, $30,000 reserve target calculated by the app,
- the exact reserve holding identified,
- a visible routing order for every next dollar,
- an updated retirement confidence result based on the saved plan.

---

## DONE WHEN

- [ ] Income, Taxes, Living, and Debt payments are believable source numbers
- [ ] The surplus is a calculated app result, not an estimate held in the student's head
- [ ] Normal and bare-bones spending are both saved
- [ ] Target months, basis, and monthly build cap are deliberate
- [ ] The app shows the reserve target and current funded status
- [ ] The exact reserve holding is identified
- [ ] The student can explain what gets the first claim on the next dollar
- [ ] The Plan confidence result has been rechecked after the saved changes

**END**
