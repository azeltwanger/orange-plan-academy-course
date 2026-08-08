# Unit 6 · Module 5 — Tax Strategy

*Cost basis first. Then the three account buckets, the tax window planner, RMD risk and Roth conversions, harvesting, and state taxes.*

> **US-specific module.** Everything here runs on the US Internal Revenue Code: brackets, Roth accounts, RMDs, wash-sale rules, state taxes. Said ONCE, at the top of 5.1, and never repeated per lesson.

## 5.1 Cost basis: what you paid, and how to reconstruct it
*`TEACH` · 715 words · ~5 min*

> 🐞 Currency mangling in the lot-sale figures (item 17). Reconstructed from
> arithmetic: hardware lot basis $7,500 → gain $17,500; exchange lot basis
> $15,000 → gain $10,000.

**By the end of this lesson, you can:**

- Understand what cost basis is and why it unlocks every tax move
- See how the same sale produces different tax bills depending on which lot you sell from
- Reconstruct basis while records still exist
- Never leave basis blank

---
One thing before we start this module, and I'll say it once. Everything in this module is built on US tax law. Brackets, Roth accounts, RMDs, wash-sale rules, state taxes. If you're outside the US, the way of thinking travels and the specific rules do not, so take these frameworks to a tax professional in your own country and let them map the containers.

Real tax strategy works forward: act in the years your rate is low, and act before the government forces the timing. Every forward-looking move starts with one number being right.

### What cost basis is

Cost basis is what you paid for each lot of Bitcoin: the price, the date, and the amount.

Your gain is the sale price minus that basis, and your tax is built on the gain. Without basis, you can't prove the gain was small.

Basis is tracked per lot, not for the whole stack. A lot is one purchase (the coins you bought on one day at one price). When you sell, you're selling out of a specific lot, and the tax follows that lot's price.

### Same sale, two different tax bills

The couple's 1.75 BTC, at an illustrative $100,000/coin, is worth $175,000. They paid $60,000, split across two lots:

| Lot | Location | Quantity | Basis | Per coin |
|---|---|---|---|---|
| 1 | Hardware wallet | 1.5 BTC | $45,000 | $30,000 |
| 2 | Exchange | 0.25 BTC | $15,000 | $60,000 |

Same stack, two lots. Say they sell 0.25 BTC. That's $25,000 either way:

- **From the hardware wallet** ($30k/coin): basis $7,500, gain **$17,500**.
- **From the exchange** ($60k/coin): basis $15,000, gain **$10,000**.

At the 15% long-term capital gains rate, that's a ~$1,125 difference on a sale they were making anyway.

### What clean basis unlocks

Four moves become available:

- **Time your sales.** Choose low- or high-basis lots on purpose.
- **Harvest losses.** Prove the loss and offset gains and income.
- **Harvest gains.** Reset your basis higher in a low-tax year.
- **Model the tax.** Know the real bill before you act.

Without clean basis, all four are guesswork.

### Rebuilding what's missing

Almost nobody has clean records. Exchanges shut down, coins move through wallets, and old buys are older than any statement you can download.

The path is the same every time:

- Pull every record that exists from every exchange and wallet.
- For the rest, build a reasonable estimate. Narrow the purchase window as tightly as you honestly can, use the price range from that window, and write down how you got there.
- Convert a blank into a number you can defend.

The IRS standard is "reasonable and documented," not "perfect." Your best estimate, as long as it's reasonable, is good.

### Never leave basis blank

⛔ **Never leave basis blank.**

If there's no basis at all, the gain gets treated as the entire sale price.

On the 0.25 BTC sale above: $10,000 of real gain becomes $25,000 of gain, because the whole sale price counts. At 15%, a $1,500 bill turns into $3,750. Purely for missing a record.

### Your decision

How far back you can reconstruct, and what you'll do about anything you can't.

### Put it in Orange Plan

Strategy → Tax → cost basis. Enter what you have, and flag the lots you can't prove.

### You are done when

Every lot has a basis you could show someone, or is flagged as unproven. No records means a basis of zero, which means tax on the entire sale price, so an unproven lot is a real number in your plan rather than a gap.


## 5.2 Taxable, tax-deferred, and Roth: bracket windows and state taxes
*`TEACH` · ~1,175 words · ~8 min*

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

Two things decide your federal tax bill: where your money sits, and when you act. A third dial sits on top of both: where you live when you act.

### Where your money sits: the three buckets

Every dollar you own for retirement sits in one of three:

| Bucket | Tax going in | Tax on growth | Tax on withdrawal | Forced withdrawals |
|---|---|---|---|---|
| **Taxable** | Already taxed | On gains, at cap-gains rates | On gains only | No |
| **Tax-deferred** (Traditional IRA/401k) | Pre-tax | None for now | Ordinary income | Yes (RMDs at 73) |
| **Roth** (IRA or 401k) | After-tax | None, ever | None, ever | No (Roth IRA) |

Every year, you get to choose which bucket the money comes from. That choice sets the rate you pay.

Go all-in on any one bucket and you remove your choices later. Even all-Roth (which sounds safe) leaves cheap tax-deferred dollars on the table.

### When you act: reading a tax bracket

Your tax rate isn't fixed. It changes by life stage.

Your income gets sliced up, and each slice gets taxed at its own rate. Being in the 22% bracket doesn't mean you pay 22% on everything. It means the next dollar you earn gets taxed at 22%.

The space between where your income lands and where the next rate starts is your **room**. A measurable amount you can fill without moving into the next bracket.

### Running the couple's bracket today

Gross income: $190,000. Bracket lines and standard deductions move every year. Run this with the current figures when you plan.

| Step | Amount |
|---|---|
| Gross income | $190,000 |
| Minus 401(k) pre-tax | -$12,000 |
| Equals AGI | $178,000 |
| Minus standard deduction (~$31,400 married) | -$31,400 |
| Equals taxable income | ~$146,600 |

That's the 22% bracket, with ~$60,000 of room before the next one. They could add $60,000 of income and still pay 22¢ on the dollar.

### The bracket roadmap: three stages

Your income through retirement runs in three stages, and each one has a different amount of room in it.

**Stage 1: Early retirement (paychecks stop).** Say they retire at 60. Paycheck stops. They're living off the taxable bucket, so reported income drops (often to the lowest it's ever been).

Second thing in their favor: when they sell an asset, only the gain counts as income, not the whole sale. A big sale can produce a small amount of income.

They sell Bitcoin to fund $80,000 of spending. Only the gain counts: about $60,000 of realized gain that year.

The standard deduction and the 0% long-term capital gains bracket stack, giving a married couple a real 0% ceiling. **Read the current one off the app's Tax page rather than speaking it** — it moves every year, and this lesson outlives the tax year.

| Step | Amount |
|---|---|
| Zero-percent ceiling | the current one, off the Tax page |
| Minus realized gain | -$60,000 |
| Equals unused 0% room | ~$68,000 |

They funded the whole year and paid $0 on those gains.

**Stage 2: Pre-Social Security.** Still flexible. Benefits haven't started, nothing is forced. Keep filling those low brackets on purpose.

**Stage 3: Social Security + forced withdrawals.** Benefits turn on at 67 (~$51,600/yr for the couple). RMDs stack at 73. Income jumps.

Hard deadline on the cheap years. Most people waste them because nobody told them the window existed.

The couple's window has ~$68,000/yr sitting empty.

### Where you live: the state lever

Named here, taught in the library, because it only becomes a real decision for some people.

**What everybody needs:** when you sell, you owe federal tax, and then your state can tax that same gain again at its own rate. Most states tax a capital gain as ordinary income with no special long-term rate; a handful do not tax income at all. **The state that charges you is the one you are a resident of in the year you sell**, not the one you lived in when you bought. On a large retirement-year sale that runs into tens of thousands of dollars on one transaction, and unlike most moves in this module, it pays every year rather than once.

> **Advanced Library → A5.3 "State taxes and relocation: what the lever is
> actually worth"** if you are actually considering a move, or your Tax page
> shows an unrealized gain large enough that the state rate would change what
> you do. It carries the worked swing, how residency is actually determined,
> and the sequencing that keeps a big sale right after a move from becoming an
> audit. If moving is not on the table, the tax plan is complete without it.


### Your decision

> 🔶 **F24 — ADDED BEAT, not new teaching.** 5.2 had *Put it in Orange Plan* and
> *You are done when* but no *Your decision*, making it the one core lesson that
> said what to do without naming what was being decided. The wording is lifted
> from its own done-when line.

**Whether you are acting in this year's window, or deliberately passing on it.** A pass is a real answer and a finished one, provided you made it on purpose after looking.

### Put it in Orange Plan

Strategy → Tax → Moves this year. Model one sale and read the tax it produces.

### You are done when

You know which bucket your money sits in and roughly in what proportion, and you have either identified your low-income window or established you don't have one yet. A deliberate pass on this year's window is a real outcome.

Then watch the walkthrough below this video, where we model it in Orange Plan.


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
