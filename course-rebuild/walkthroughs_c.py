WALKTHROUGHS = {
    "5.3": {
        "title": "WALKTHROUGH — Reconcile basis and model the tax window",
        "body": r"""
# 5.3 · WALKTHROUGH — Reconcile basis and model the tax window

**Screen capture · about 15 minutes**

## Before recording

- Complete exchange and brokerage exports available.
- At least one lot with basis, one missing or uncertain lot, and one transfer example.
- Last year's return or a current-year income estimate for the professional handoff.
- Use US-only framing once; do not repeat a disclaimer on every screen.

## 1 · Import the history from the current transaction entry point

**DO** Dashboard → **Update holdings / transactions** → downloaded file.

**SELECT** the account and whether the file contains all available history.

**SEE** duplicate / overlap review before import.

**⚠** Importing history must not create a second current balance. Review transfers and duplicates before approving.

## 2 · Review tax-lot coverage

**DO** Tax → Tax lots → **View all lots**.

**SEE** complete · partial · missing coverage and the list of unresolved holdings.

**SAY** The app does not invent basis. Missing is a work item, not zero and not a supported estimate.

**DO** Open one holding's lot editor from the current source path and show add / edit / delete.

**⚠** A lot already consumed by a recorded sale may be locked. Correct the transaction chain in order rather than editing around it.

## 3 · Demonstrate a transfer

**DO** Record or inspect a transfer between two accounts owned by the same taxpayer.

**SEE** quantity and basis move to the destination without being counted as a second purchase.

**⚠** Fees and ownership changes can have separate consequences. The demonstration is not a blanket statement that every transfer is tax-free.

## 4 · Read the three tax buckets

**DO** Open the current account-mix or year-detail view that displays Taxable · Tax-deferred · Tax-free.

**SAY** The mix creates options. One hundred percent in one bucket removes future control.

## 5 · Model a Roth conversion

**DO** Tax → current-year moves → Roth conversion → compare strategies.

**SEE** conversion amount · tax cost · after-tax outcome · future Traditional balance / required-distribution pressure.

**DO** Customize the schedule across several years.

**SHOW** the tax-funding choice.

**SAY** Paying from outside cash preserves more inside Roth, but the app model does not decide withholding, estimated-payment timing, or the filed position.

**⚠** Include capital-gain stacking, Social Security, ACA, Medicare, state tax, NIIT, deductions, and credits in the CPA question. Do not read one bracket as the all-in cost.

## 6 · Review harvesting candidates

**DO** Open gain and loss harvesting views.

**SEE** eligible lots and any displayed long-term-gain room.

**DO** Export Form 8949 data.

**SAY** The export is the professional handoff. Current wash-sale treatment and lot-identification requirements are verified before execution.

## 7 · Compare the state scenario

**DO** Scenarios → **Move to no-tax state** or the current state-change scenario.

**READ** the change in taxes and the whole-plan result.

**SAY** Residency is a legal and factual standard. The scenario measures the lever; it does not establish domicile.

## 8 · Run the tax review

**DO** Tax → **Review Tax Strategy**.

**ANSWER** whether a sale, inheritance, business event, healthcare subsidy, or other tax item is missing from the model.

**ASK** which one or two moves are worth bringing to the CPA this year.

## 9 · Build the handoff packet

Save or list:

- basis coverage and reconstruction notes;
- lot export / Form 8949 data;
- modeled conversion schedule and tax-funding source;
- harvesting candidates;
- state assumption;
- healthcare and Medicare interactions;
- exact questions with dollar amounts and dates.

## 10 · Close Tax

**DO** Build Your Plan → **Tax**.

**SEE** the available history reviewed, and conversion / harvesting reviews intentionally completed or passed.

## Module 5 checkpoint

- No missing lot is silently treated as a known number.
- Transfers and duplicates are reconciled.
- The tax buckets and low-income window are visible.
- A conversion or withdrawal range is modeled, not executed blindly.
- Harvesting candidates and the 8949 export are saved.
- The professional questions are ready before the calendar deadline.
""",
    },
    "6.4": {
        "title": "WALKTHROUGH — Build the retirement paycheck",
        "body": r"""
# 6.4 · WALKTHROUGH — Build the retirement paycheck

**Screen capture · about 16 minutes**

> This module builds every retirement-income input and strategy. The first saved full 1,000-path confidence run waits until Module 9, after Custody and Estate are also intentionally complete.

## Before recording

- Retirement spending decision from Lesson 6.1.
- Current Social Security estimates and start ages.
- Pension or other durable-income details.
- Healthcare bridge estimate when retirement begins before Medicare.
- Account timeframes and contribution plan from Module 3.
- Tax-window work from Module 5.

## 1 · Confirm retirement spending

**DO** Plan → Retirement → current spending and retirement-age controls.

**ENTER / VERIFY** baseline annual spending.

**SAY** The number includes the expected lifestyle and healthcare. Required debt payments remain modeled separately.

**DO** Add large irregular costs as life events rather than inflating every year.

## 2 · Add the healthcare bridge when needed

**DO** Life events → Expense change.

**ENTER** start at retirement · current annual premium / retained cost · duration until Medicare or the chosen transition date.

**⚠** Use current quotes. Do not reuse a premium from a recorded lesson.

## 3 · Build the income floor

**DO** Planning profile / retirement benefits → Social Security and start age.

**ENTER** monthly benefit in the field that expects a monthly number.

**ADD** spouse benefit · pension · other durable income using the current owning controls.

**SEE** the floor in the Income chart and year-by-year detail.

## 4 · Read the gap and Bridge years

**DO** Plan → Income → Income Blueprint → click early retirement years.

**SEE** spending need · durable income / floor · portfolio-funded gap.

**COUNT** the years before retirement-account access, Social Security, pension, or other income begins.

**COMPARE** the gap with the accounts assigned to Bridge.

**⚠** A funded total portfolio can still have an access problem. The Bridge must exist in money the household can actually use.

## 5 · Compare Social Security timing when it matters

**DO** Scenarios → claim at an earlier age versus a later age using current presets or a custom scenario.

**READ** benefit size · Bridge withdrawals · taxes · Bitcoin / portfolio remaining.

**SAY** The larger check is not the only result. Waiting has a portfolio cost during the Bridge.

## 6 · Set the withdrawal strategy

**DO** Income Blueprint → Withdrawal order / income strategy.

**SHOW** account order and what is sold inside accounts as separate controls.

**COMPARE** sequential with the current tax-aware or blended option.

**SEE** lifetime taxes · Bitcoin remaining · after-tax result update in preview.

**SAY** Strict taxable-first can waste low ordinary-income brackets. Tax-aware uses the current year's mix instead of waiting for a later cliff.

**DO** Apply the chosen strategy only after the comparison is understood.

**⚠** A preview is not the baseline until Apply is used. Revert removes the draft.

## 7 · Read the Reserve / Bridge / Legacy draw-and-refill system

**SEE** the cash / Reserve buffer and the account timeframes.

**SAY** Spending comes from the Reserve. Bridge refills it. Legacy refills Bridge when the plan and market conditions support it.

**SHOW** where the annual update or refill status will appear once the operating plan is active.

**⚠** Do not claim the app predicts a good sale day. The rule is an annual operating decision, not market timing.

## 8 · Preview sell, borrow, or hold

**DO** Retirement Borrowing / Bitcoin-backed loans workbench.

**COMPARE** sell-only / bracket-aware / borrow-first / custom options that exist in the current build.

**SEE** interest · debt · Bitcoin at lender versus custody · after-tax result / projected legacy.

**TOGGLE** step-up or estate assumptions only as a model, with current-law caveat.

**⚠** Nothing changes until Apply. Verify lender terms and tax treatment outside the app before applying a borrowing strategy.

## 9 · Show, but do not complete, the confidence operating plan

**DO** Open the Retirement operating plan / What you can spend section.

**POINT OUT** the confidence target choices and annual guardrail area.

**SAY** Lesson 6.3 explained how this works. We are deliberately waiting to run and save the first full confidence result until Module 9, after every Build Your Plan area is complete.

**⚠** Do not seed a placeholder result or read a percentage as final during this walkthrough.

## 10 · Close Retirement income

**DO** Build Your Plan → **Retirement income**.

**SEE** retirement age and spending · Social Security · withdrawal strategy complete.

## Module 6 checkpoint

- Retirement spending, healthcare, and irregular costs are honest.
- The income floor and gap can be stated from memory.
- Bridge years and accessible funding are verified.
- Social Security timing was compared when material.
- A withdrawal order is applied and understood.
- Sell / borrow / hold remains a preview unless intentionally applied.
- The first full confidence run is explicitly deferred to Module 9.
""",
    },
}
