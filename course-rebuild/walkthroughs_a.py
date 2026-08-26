WALKTHROUGHS = {
    "1.4": {
        "title": "WALKTHROUGH — Replace the onboarding estimate with real Foundation data",
        "body": r"""
# 1.4 · WALKTHROUGH — Replace the onboarding estimate with real Foundation data

**Screen capture · about 20 minutes**

> **DO** = action on screen · **SEE** = point at this result · **⚠** = avoid this mistake
> Narrate naturally. This sheet is not a teleprompter.

## Before recording

- Complete the current short onboarding with rough values.
- Use a demo account with no real accounts or holdings entered yet.
- Have a real-looking statement list ready: account names, owners, current quantities, and cash balances.
- Do not have a saved 1,000-path confidence receipt yet.

## 1 · Orient the learner

**DO** Land on Dashboard after onboarding.

**SEE** The starting retirement estimate.

**SAY** It is the deterministic estimate from Lesson 1.3: rough inputs, one set of assumptions, not the finished confidence-based date.

**DO** Open **Build Your Plan**.

**SEE** The areas and the Foundation tasks.

**SAY** Build Your Plan is the implementation roadmap. The course order teaches the decisions; each walkthrough returns here to complete the area that owns the data.

## 2 · Verify personal details

**DO** Foundation → **Set up personal details** → Planning profile.

**CHECK** date of birth or age · state or country · filing status · spouse details where applicable.

**⚠** Fix the source field. Do not edit a downstream tax or retirement total to compensate for a wrong profile input.

## 3 · Add the real accounts

**DO** Dashboard → **Add Account**.

**ENTER** account type · recognizable account name · owner.

**SHOW** at least one cash account, one retirement or brokerage account, and the actual Bitcoin custody location: exchange, hardware wallet, collaborative custody, IRA, or ETF account.

**⚠** The account is the container. Bitcoin, cash, ETFs, and other assets are holdings inside the account.

**DO** Point at **Link accounts** without waiting on a live connection.

**SAY** Linking is optional. Manual entry and imports are valid; the goal is an honest current position.

## 4 · Add current holdings

**DO** Open an account → **Add holding**.

**ENTER** Bitcoin as quantity · stocks or funds as ticker and shares where supported · cash as the current balance · property or other assets with the current value.

**SEE** The Add holding form now starts on the asset type that fits the account when the app can infer it.

**⚠** Enter basis only when it is already known. Foundation is not where years of purchase history are reconstructed.

**DO** Repeat quickly for the remaining demo accounts.

**SEE** Net worth and account totals update.

## 5 · Explain Update Holdings versus transaction history

**DO** Open the current **Update holdings / Update transactions** entry point from Dashboard.

**SHOW** the available paths: linked activity when supported · downloaded CSV or spreadsheet · one manually entered purchase, sale, or transfer · AI-assisted description when present.

**SAY** Three jobs stay separate:

1. Foundation records what each account owns now.
2. Tax records what was paid and when.
3. Maintenance records activity after the plan is built.

**⚠** A transfer between the learner's own accounts changes location, not the total amount owned. Do not import it as both a sale and a new purchase.

**⚠** Do not import the full historical tax record in this walkthrough. Module 5 owns that work.

## 6 · Verify the current position

**DO** Expand every account group on Dashboard.

**CHECK** owner · account type · quantity · current value · custody location.

**SEE** Net worth and Bitcoin share.

**SAY** If the total is wrong, fix the row that created it. Calculated totals are not inputs.

## 7 · Review the baseline assumptions

**DO** Open the Plan assumptions control from the current Retirement page.

**CHECK** Bitcoin model · inflation · life expectancy · other asset assumptions.

**OPTIONAL** Show where custom return windows live without building one.

**⚠** Review only. Do not change the assumption repeatedly to chase a preferred retirement age.

## 8 · Close Foundation

**DO** Return to **Build Your Plan → Foundation**.

**SEE** Personal details, accounts, and holdings complete from the real data.

**IF OPEN** Read the exact missing line and fix it on the owning page.

**SAY** Income, living expenses, Reserve settings, and expected life events belong to Module 2. Allocation, debt, tax history, Social Security, and withdrawal strategy come later.

## Foundation checkpoint

- Personal details are accurate.
- Every real account and custody location is listed.
- Current holdings match the source statements.
- The learner knows how to add future activity without duplicating a transfer.
- The assumptions were reviewed deliberately.
- Build Your Plan shows Foundation complete.
""",
    },
    "2.5": {
        "title": "WALKTHROUGH — Build cash flow, the Reserve, and expected life events",
        "body": r"""
# 2.5 · WALKTHROUGH — Build cash flow, the Reserve, and expected life events

**Screen capture · about 18 minutes**

## Before recording

- Have two or three months of categorized transactions available when possible.
- Know the normal living-spending number and bare-bones monthly essentials.
- Know the chosen Reserve months and a monthly build amount the household can sustain.
- Have one expected life event and, when the optional college lesson applies, one college event.

## 1 · Read the cash-flow verdict

**DO** Cash Flow → **This month**.

**SEE** The amount left to put to work, or the deficit.

**SAY** This number is calculated from income minus taxes, living expenses, and required debt payments. It is the pool the later routing decisions share.

**⚠** Do not type a surplus into multiple accounts. The app calculates one available pool.

## 2 · Enter every income stream

**DO** Expand **Income** → add each source separately.

**ENTER** salary by earner · self-employment · rental · recurring income · tax-free income when applicable.

**SAY** Which sources are stable and which are variable. That judgment affects the Reserve decision even when the annual total is identical.

## 3 · Enter normal living expenses

**DO** Expand **Living**.

**ENTER** the normal after-tax living amount from Keep / Cut / Reduce.

**⚠** Living is not gross income and does not duplicate the required debt-payment row.

**DO** Review the Taxes and Debt payments rows so the separation is visible.

## 4 · Verify spending against real activity

**DO** Open **Verify Spending** → review by month.

**SEE** Linked or imported spending compared with the saved plan amount.

**DO** Exclude one genuine one-time item using the current review control.

**SAY** One unusual month does not automatically change the baseline. Look for a repeated difference or a permanent change.

## 5 · Set the Reserve

**DO** Open **Reserve settings**.

**ENTER** bare-bones essentials first · choose Bare-bones as the basis · select target months · enter the monthly build cap.

**SEE** Orange Plan calculates target = monthly basis × target months, then shows current Reserve, remaining gap, and time to full when a build amount is set.

**⚠** The learner does not calculate and type the target amount manually.

**DO** Dashboard → exact cash holding → **Add shield / designate emergency fund** using the current holding action.

**SAY** The shield tells the plan which cash is spoken for; it does not create new cash.

## 6 · Read the routing waterfall without finishing contributions

**DO** Cash Flow → Routing.

**SEE** Reserve first · Extra debt · Contributions.

**SAY** Module 2 decides the available surplus and Reserve claim. Module 3 builds the contribution rows. Module 4 decides whether the Extra debt row changes.

**⚠** Do not configure the full investment plan here. Show the handoff and move on.

## 7 · Add expected life events

**DO** Plan → Retirement → Life events → **Add event**.

**ENTER** event type · amount · age or year · duration or recurrence when applicable.

**SHOW** one expected expense or income change.

**SEE** The future cash flow and plan result update.

**SAY** A likely expected change belongs in Life events. A hypothetical question belongs in Scenarios.

**⚠** The event records what the plan will have to fund. It does not decide whether the money comes from Bitcoin, cash flow, an account, or financing.

## 8 · Optional college implementation

**DO** Add a College event with the parent's actual commitment, not the full sticker price by default.

**SEE** The Education target, current education-account amount, projected coverage, and remaining gap where the current app displays them.

**DO** Add or review a 529 contribution only when it is part of the chosen funding mix.

**SAY** Education funding is shown separately from the broader Reserve / Bridge / Legacy savings target. The app helps quantify the plan; the family still chooses the commitment and sources.

## 9 · Close the area

**DO** Return to **Build Your Plan → Cash flow**.

**SEE** Income · Living expenses · Reserve target · Life events complete, or **Nothing major coming** selected truthfully.

## Module 2 checkpoint

- The surplus is believable and sustainable.
- Normal and bare-bones spending are separate.
- The app calculated the Reserve target and gap.
- The Reserve funding pace is saved.
- Expected life events are in the baseline; hypotheticals are not.
- The learner knows Module 3 decides where the investable surplus goes.
""",
    },
}
