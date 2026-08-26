# Unit 6 · Module 5 — Tax Strategy

*Cost basis first. Then the three account buckets, the tax window planner, RMD risk and Roth conversions, harvesting, and state taxes.*

> **US-specific module.** Everything here runs on the US Internal Revenue Code: brackets, Roth accounts, RMDs, wash-sale rules, state taxes. Said ONCE, at the top of 5.1, and never repeated per lesson.

## 5.1 Cost basis: what you paid, and how to reconstruct it
*`TEACH` · ~961 words · ~6 min*

> 🐞 Currency mangling in the lot-sale figures (item 17). Reconstructed from
> arithmetic: hardware lot basis $7,500 → gain $17,500; exchange lot basis
> $15,000 → gain $10,000.

**By the end of this lesson, you can:**

- Understand what cost basis is and why it unlocks every tax move
- See how the same sale produces different tax bills depending on which lot you sell from
- Reconstruct basis while records still exist
- Label every material lot verified, estimated for planning, or unproven

---

In today's lesson, we're going to cover cost basis, which is the record that makes every other tax decision in this module usable.

Quick note before we start: this module is US-specific. The framework still helps outside the US, but the rules and reporting do not travel with it.

### What cost basis is

Cost basis is generally what you paid to acquire an asset, adjusted for the costs and events that the tax rules tell you to include.

For a Bitcoin purchase, that normally means the dollars you paid for the Bitcoin plus acquisition costs that belong in basis. Your gain or loss is measured from the amount you receive when you dispose of it, after the adjustments that apply, minus the basis of the units you disposed of.

Basis is tracked by units or lots, so one purchase can have a completely different cost and holding period from the next purchase.

### Same sale, two different tax bills

Let's run it on the couple.

They hold 1.75 Bitcoin worth an illustrative $175,000. They acquired it in two lots.

Lot one is 1.5 Bitcoin with a total basis of $45,000, or $30,000 per coin.

Lot two is a quarter Bitcoin with a $15,000 basis, or $60,000 per coin.

Now they sell a quarter Bitcoin for $25,000.

If the identified units come from lot one, the basis is $7,500 and the gain is $17,500.

If the identified units come from lot two, the basis is $15,000 and the gain is $10,000.

The sale proceeds are the same, but the gain changes because the Bitcoin came from a different lot.

That is why "I own 1.75 Bitcoin" is not enough information for a tax plan.

### Specific identification is a record, not a retrospective choice

For Bitcoin in self-custody, current IRS guidance lets you specifically identify the units you are disposing of when two things are true.

First, no later than the date and time of the transaction, your books and records identify the particular units using enough information to distinguish them, such as acquisition date and time or acquisition price.

Second, you keep records that establish those identified units were actually removed from that wallet.

For Bitcoin held by a broker, the broker decides which identifiers it can accept. After 2025, the instruction generally has to reach the broker no later than the transaction, and you keep your own substantiation.

So HIFO, FIFO, or any other lot rule is not a button you invent after the year is over. It is a documented instruction that has to satisfy the rule for the wallet or account involved.

If specific identification fails, the current default is generally the earliest-acquired units of that asset in that wallet or account.

### Transfers do not erase the history

Moving Bitcoin between wallets you own is generally not a taxable disposition, apart from any Bitcoin used to pay the transaction fee.

But the tax history still has to travel with the Bitcoin.

The blockchain proves that an output moved. It does not prove what you originally paid, whether the acquisition was a purchase, income, gift, inheritance, mining, or something else, or which tax lot you intended to dispose of later.

That is why the useful record connects three things: the acquisition record, the wallet or account movement, and the final disposition.

### Reconstructing what is missing

Start with the records that were created when the transactions happened.

Download every exchange and brokerage export you can still access. Pull confirmations, old tax files, bank or card statements, email receipts, and wallet transaction history. Match withdrawals and deposits between your own accounts so a transfer is not mistaken for a sale or a new purchase.

Then separate every unresolved item into one of three states.

**Verified.** The source records support the acquisition date, quantity, and basis.

**Estimated for planning.** You have evidence that narrows the range, but not enough to claim the number as settled. Orange Plan can use it for a projection as long as the uncertainty is visible.

**Unproven.** You cannot substantiate a basis yet.

The course used to say the IRS standard was simply "reasonable and documented." That was too broad. Documentation helps, but it does not create a general safe harbor that lets you make up a basis the return can claim.

If a meaningful lot remains unproven, work through the evidence with a tax professional before filing a disposition from it.

### Zero basis is a stress test, not an automatic legal answer

For planning, a zero-basis assumption can show the conservative tax exposure if no basis is allowed.

But do not confuse that stress test with a legal conclusion that the asset definitely has zero basis. And do not invent a number merely to avoid zero.

So in the plan, label what is known, what is estimated, and what is still unproven.

### What clean basis unlocks

Once the records are clean, you can:

- identify units before a sale;
- see whether a loss actually exists;
- model gain harvesting in a low-tax year;
- compare selling, holding, gifting, or borrowing without guessing at the tax;
- reconcile the app with Form 1099-DA, Form 8949, and your return.

### Your decision

Which lots are verified, which are planning estimates, and which are still unproven.

### Put it in orange plan

Dashboard → Update Transactions for the history, then Strategy → Tax to review basis and modeled sales.

Use the file, AI-assisted, or manual path that matches the records you have. A linked source appears only when the app has a supported investment source.

### You are done when

Every material lot is labeled honestly, the available evidence is saved outside the app, and an unproven lot is visible as an unresolved tax item instead of being silently assigned a number.


## 5.2 Taxable, tax-deferred, and Roth: bracket windows and state taxes
*`TEACH` · ~920 words · ~6 min*

> ✅ **Law-set figure removed (2026-08-08).** This lesson used to speak the
> ~$128,000 of 0% capital-gains room for a married couple. It is now read off
> the app's Tax page instead, in both the script and the master. Everything
> that remains is mechanism ("the 22% bracket means the next dollar") or the
> couple's own illustrative numbers, which are fine to speak.

> ⚠ **The buckets/wrappers inconsistency lives inside this lesson's own
> outcomes**: the checklist says "three tax **wrappers**" while the body teaches
> "three **buckets**". Item 21.
>
> ✅ The `u0027` text Austin saw on screen was the interim state of the checklist
> repair — already fixed; refresh.
>
> ✅ **Evergreen policy (Austin, 2026-08-04) replaces item 11.** Do NOT update
> these figures each year. The text already frames them as tilde-marked
> snapshots ("move every year… run with current figures"). On camera, say the
> frame line and never read a threshold as a fact — the app shows current law.
>
> 📌 **Item 14 evidence:** the planned lesson "State taxes and relocation: a big
> lever" was folded in here as "the state lever" section.

**By the end of this lesson, you can:**

- Understand the three tax wrappers
- Read a tax bracket and know what 'room' means
- Map your projected income against brackets across a lifetime
- Identify the low-bracket years worth targeting
- Understand how state residency changes the tax bill on every sale

---

In today's lesson, we're going to give each tax bucket a job, find the years when your rate may be lower, and build the roadmap the app will test.

### The three tax buckets

The first bucket is taxable.

This is your brokerage account, Bitcoin held personally, and other taxable property. There is no age restriction on using it. When you sell an appreciated asset, the gain is generally taxed under the capital-gain rules, and the result depends on basis, holding period, total income, state, and the units you identified.

The second bucket is tax-deferred.

Traditional 401(k)s and traditional IRAs generally give you a tax benefit on the way in, then tax distributions as ordinary income later. They also come with required-distribution rules.

The third bucket is Roth.

Roth contributions go in after tax. Qualified Roth distributions are generally tax-free. That word qualified matters. A nonqualified withdrawal can expose earnings to income tax or an additional tax, and conversion amounts can have their own five-year clocks when withdrawn early.

Under current law, Roth IRAs and designated Roth plan accounts do not require lifetime distributions from the original owner.

### The job of each bucket

Taxable money is the flexible bridge. It can fund years before retirement-account access, pay a Roth-conversion tax from outside the converted account, and create capital-gain planning opportunities.

Tax-deferred money is useful when the deduction today is worth more than the ordinary-income cost you expect later. The risk is letting the account grow into forced distributions that arrive on the government's schedule.

Roth is the long-duration tax-free bucket when the rules for a qualified distribution are met. It is often the last bucket you want to exhaust, but that is a plan decision, not a universal withdrawal command.

### Find the window

The tax window is the period when earned income falls but required distributions and other forced income have not yet started.

For an early retiree, it can begin when work ends. Social Security may start later. Required distributions start later still, at the applicable age for that person under current law.

For the 45-year-old couple in this course, current law points to age 75, not 73. A different birth year can produce a different applicable age, so read the current value in the app and IRS guidance rather than memorizing one age for everyone.

The window is useful because the household may control more of the income that fills it.

Possible moves include:

- realizing long-term gains while room remains in a lower capital-gain band;
- converting part of a traditional account to Roth;
- drawing from traditional accounts before required distributions;
- delaying a taxable sale or conversion when another year is cheaper.

### The bracket top is the starting point, not the answer

A common shortcut is "fill the bracket and stop."

I think that leaves out too many of the other costs that can change at the same time.

A conversion or gain can also change:

- how much of Social Security is taxable;
- Marketplace premium tax credits before Medicare;
- Medicare IRMAA later;
- the Net Investment Income Tax;
- state tax;
- capital-gain stacking;
- deductions, credits, and other income-based rules.

So I would not stop at the federal bracket. I would look at what the next dollar actually costs after every rule it touches.

Orange Plan can model the federal, state, and plan-level result. The current-year return still belongs with the tax professional who can see the entire household.

### Capital-gain room

Long-term capital gains have their own rate bands, but ordinary taxable income fills the stack first.

That means a household does not simply get a separate bucket of gains taxed at zero. The gain sits on top of the other taxable income, and only the portion that fits inside the current zero-rate band receives that rate.

A federal zero rate also does not mean a zero total cost. State tax, ACA credits, NIIT, and other interactions can still move.

### State tax is a second model

State tax deserves its own line because residence is not just the address on the day of a sale.

States can use domicile, statutory residency, part-year rules, source-income rules, community-property rules, and special treatment for trusts or businesses.

The app can compare two state assumptions. It cannot prove that a move changed your legal domicile or that a particular state has no claim on a transaction.

Treat the state comparison as a reason to ask a better question before a large move, not as a residency opinion.

### The couple's roadmap

The couple's working years are high-income years. Their first retirement years may be lower-income years. Social Security begins later, and required distributions later still.

So their roadmap is:

1. Use taxable assets as the bridge.
2. Each year, model gains and Roth conversions together.
3. Check healthcare and state effects before applying anything.
4. Re-run after Social Security, Medicare, or required distributions begin.
5. Keep Roth available for later flexibility rather than spending it by default.

### Your decision

What job each account has, and which years deserve a tax-window review.

### Put it in orange plan

Strategy → Tax. Read the yearly roadmap, model one sale and one conversion, and keep them as previews until you deliberately apply the plan change.

### You are done when

You know what job each account has, you can point to the low-income years on the timeline, and you can explain what the next dollar actually costs before you decide how large the move should be.


## 5.3 Walkthrough: model it in Orange Plan
*`DEMO` · 1,321 words*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **5.3**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

> App page is **Tax Center** — never named. **Tax funding** control label needs
> eyeballing.

> ✅ **Corrects my reverse-audit claim.** The app location is named throughout:
> **Strategy → Tax**. "Tax Center" is the component filename. Item 4's Module 5
> entry is withdrawn.
>
> ✅ **Resolves item 7:** the "Tax funding" picker is named here with both
> options ("Plan cash flow (withdrawal order)" / "Withheld from each
> conversion") — matches the engine behavior found in runProjection.jsx.

**By the end of this lesson, you can:**

- Import transaction history and confirm cost basis for every lot
- Model a Roth conversion schedule on your own numbers
- Read your harvest room and export a Form 8949 draft for your CPA
- Run the state-tax scenario to see the annual and compounded impact

---

You have your five tax levers: basis, buckets, RMDs, conversions, harvesting, and state tax. Now every one of them runs against your own numbers.

Set aside about 20 minutes. Have last year's tax return handy and a wallet or exchange export ready.

> ⚠ Before the harvest step, know that harvest room only shows up for recorded purchase lots. Holdings with only an aggregate basis are excluded, and the app says so. Run the import step first, or the harvest rows will be empty.

<!-- PLAN-LIFECYCLE:TAX-HISTORY -->
Foundation recorded what each account owns today. This step answers a different question: what did you pay, and when? Historical purchase records belong here because they affect taxes, not because Foundation was incomplete.

### Step 1: Import your transaction history

The transactions importer isn't on the Tax page. It lives on the Dashboard.

**Dashboard → Update Transactions** opens the dialog. Choose **A downloaded file** → *Upload a CSV or Excel file from the account or service.*

Answer two questions:

- Which account are these transactions for?
- Does this export include all available history? (**Yes**, or **No, or I'm not sure**.)

The importer checks the file against earlier imports before saving, so re-importing an overlapping range doesn't duplicate.

Remember: the app never invents basis. A flagged lot is your reconstruction homework.

### Step 2: Land on the lots

**Strategy → Tax → Tax lots → View all lots.**

Read the **coverage banner** at the top:

- **"Tax-lot records reconcile"** means you're done with the reconstruction homework from the cost-basis lesson.
- **"Cost-basis history is incomplete"** means look at the count: *"N of N taxable positions fully match by known-basis lot quantity; N partial; N missing basis."*

If any count is unresolved, click **Import or reconcile history** and go back to Step 1. The missing-basis count is your homework list.

Then read the lot table columns: **Asset · Purchased · Qty · Cost basis · Avg price · Value · Gain/loss · Term · Account.** The **Term** column reads LT or ST per lot.

#### Fixing a lot that came in wrong

Importing gets transactions in. It doesn't make them right. A bad date, a duplicated buy, a lot that landed with no basis — you fix all of those in one place.

**Dashboard → find the holding → click `Lots`** on the row (it's also in the row's three-dot menu). The dialog is **"Purchase Lots — {asset}"**, and the sub-line tells you the job: *"Track purchase lots to keep cost basis accurate."* Add a lot, edit one, delete one. That's the reconstruction homework from the cost-basis lesson, done.

Same row, same menu, two neighbors worth knowing: **Add transaction** records a single buy, sell, or transfer against that holding, and **Transfer** moves a holding to a different account carrying its dates and cost basis with it — it is not a sale and creates no taxable event.

Two guardrails will stop you in here. Both are the app protecting your history, not bugs:

**A lot that's already been sold is locked.** The edit button goes gray and reads *"Purchase lot locked by a sale."* The message: *"This lot has already been used in a sale. Delete the related sell transactions first so lot history stays accurate."* Rewriting a purchase underneath a sale that already happened would quietly change a gain you may have already reported. The app makes you unwind it in order — delete the sale, fix the lot, re-enter the sale.

**Lots can't add up to more than you own.** *"Remaining lot quantity exceeds this holding by X. Edit or delete duplicate lots instead of adding a new one."* That's almost always a double import. Find the duplicate and delete it rather than papering over it with a second lot.

When you're done, re-read the coverage banner at the top of the lot table. That's the scoreboard.

### Step 3: Ground the three buckets

The taxable, tax-deferred, and tax-free split isn't on the Tax page. It renders in the Retirement year-detail drawer.

**Plan → Retirement → click a year on the chart → drawer → Account mix.**

The collapsed summary shows *"N% tax-free"* with a three-segment bar. Expand for the rows: **Taxable**, **Tax-deferred**, **Tax-free**.

Where your money sits changes how it's taxed. Your bracket roadmap starts from real balances, not idealized ones.

If it's 100% in one bucket, the rest of this walkthrough is going to be short. A bucket mix is what makes the levers work.

### Step 4: Model a Roth conversion

**Strategy → Tax → Moves this year → Roth conversion.**

The right side reads **"None modeled"** (unmodeled) or **"~$X lifetime"** (modeled).

Open it. You'll see **Compare strategies**: a table with columns **Strategy, After-tax NW @{age}, Saved, Cost**. The table computes on open. Nothing to click to "run" it.

Below that: the **Selected strategy** block with four tiles: **Lifetime saved**, **NW impact @{age}**, **Window**, **Total tax cost**.

Actions: **Customize schedule** (opens the bracket-fill editor) and **Apply to Plan** (commits it).

Open **Customize schedule → Conversion schedule** panel:

- **Conversion timeline** with legend "Amount converted" and "Tax cost."
- Per-year rows: **Year, Age, Amount**.
- Hover a timeline bar for detail: *"Conversion tax cost," "Projected year-end traditional,"* and IRMAA when it applies.
- **Tax funding** picker: **Plan cash flow (withdrawal order)** or **Withheld from each conversion**.

Prefer **Plan cash flow**. That's paying the conversion tax from taxable cash, never from the conversion itself.

Commit with **Apply schedule**.

Watch *"Projected year-end traditional"* shrink across the schedule years. That is the future RMD balance getting smaller before it can turn into a bracket spike.

### Step 5: Harvest room and Form 8949

Same section, one row over: **Moves this year → Harvest gains** or **Harvest losses**.

The row eyebrow reads **Modeled, not advice.**

Either row opens a wizard: **Harvest 0% Gains** or **Harvest Losses**.

For the headroom read, look one section up: **Room this year → Long-term gains → $X more at 0%.**

For the lot-by-lot view, go back to the lots table and use the preset filter: **Review filtered gains** or **Review filtered losses**.

Then on the lots view, click **Export 8949** in the top right. This produces **Form8949_{year}.csv**.

This export is the artifact you hand your CPA, not a screenshot.

If you see the toast *"No lots to review,"* harvest room is empty. Either you have no eligible lots this year, or the import in Step 1 wasn't complete.

### Step 6: Run the state scenario

**Scenarios → What if... → See more scenarios → Move to no-tax state.**

It isn't in the first four cards. You have to expand.

The scenario description writes itself: *"What if you moved from {your state} to a state with no income tax?"*

One click creates the scenario and selects it under **Your scenarios**. The plan re-runs.

The plan now reflects the state-tax swing on your own numbers. Note that residency is a legal standard, not just a change of address.

### Step 7: Run the AI review

**Strategy → Tax → Review Tax Strategy** (header button, near **Download Tax Summary**).

The review reads your tax context, the future tax projection, and the strategy comparisons (the same conversion table from Step 4).

It asks one clarifying question: *"Is there a tax event this year that Orange Plan does not yet include?"*

Answer honestly. Things like a big sale being contemplated, an inheritance, or a business exit.

Then read at least one thing it surfaced out loud and say whether you agree.

**When to run it:** after the lots are clean and the window is visible, but before you commit to a conversion or a harvest. It reviews and explains. It does not decide.

### Step 8: Capture your decisions

Write down three things. Paper is fine.

1. **This year's tax moves.** The harvests you're actually doing, and any conversion you're applying.
2. **Next low-income-year moves.** What the model shows you should do in the bridge window.
3. **The exact questions for your CPA.** The specific dollar amounts and dates from the model, in the order they'd need to happen.

The one question worth writing on top of that list: **"Am I leaving low brackets empty?"**

<!-- PLAN-LIFECYCLE:MODULE-5 -->
### Build Your Plan handoff

Foundation recorded what the accounts own today. Tax records what was paid and when. Return to **Build Your Plan → Tax** after importing or reconstructing as much basis as reasonably exists, then record that the available history has been reviewed. Missing records remain visible; they do not get invented.

### What good looks like

- Coverage banner reads **Tax-lot records reconcile**. No missing-basis count.
- **Account mix** is an actual mix, not everything in one bucket. Levers require a mix.
- **Conversion schedule** shows the bracket filled, not spilled. Total tax cost is what you're choosing to pay. Lifetime saved is what you're buying. A near-zero lifetime saved means the window isn't there this year.
- **Future RMD pressure.** "Projected year-end traditional" visibly shrinks across the schedule years.
- **Harvest room.** What's actionable this year ("$X more at 0%") versus what waits for a lower-income year.
- **8949 export.** A file named Form8949_{year}.csv.
- **State scenario.** The annual swing and the compounded one, framed honestly against the life trade-off.

### Handing it off

Your CPA doesn't need the app. They need:

- The Form 8949 export for reported sales.
- A one-page summary of the conversion schedule the model is suggesting: age, year, amount, tax cost, and projected end-of-year traditional balance.
- Your CPA question list from Step 8.

The next module covers retirement income: how to turn your assets into a paycheck when the paychecks stop.

---

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A5.1 RMD risk and Roth conversions**
  → *Watch this only when all three are true on your own Tax page: you hold meaningful pre-tax retirement assets, you expect lower-income years before forced distributions begin, and you have a way to pay the conversion tax that is not the converted money. All three, not two. If Orange Plan does not show that combination, your core tax plan is complete without it.*
- **A5.2 Harvesting losses and gains**
  → *Watch this if your Tax page shows either harvestable losses or unused 0% gains room this year. If it shows neither, there is nothing to harvest and your tax plan is complete.*
- **A5.3 State taxes and relocation: what the lever is actually worth**
  → *Watch this if either is true: you are actually considering a move, or your Tax page shows an unrealized gain large enough that your state's rate would change what you do. If moving is not on the table, your tax plan is complete without this.*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
