# Unit 2 · Module 1 — Foundation: baseline, assumptions, and the confidence number

*Gather the six pieces of your baseline, choose your assumptions (especially the Bitcoin growth number), understand the confidence ring that stress-tests your plan, run three scenarios, and know when a plan actually needs updating.*

## 2.1 Gather your numbers
*`TEACH` · 478 words · ~3 min*

**By the end of this lesson, you can:**

- Gather the documents you need for the app
- Track down cost basis while records still exist
- Save the exports into a folder you can reuse each year

---

The first step is gathering the documents you need before you start building the baseline. Every decision downstream runs on this data, so accuracy up front saves you time on every future update.

### What to gather

#### Income

Recent pay stubs so you can verify income per period and per year. Include every stream: salary for each earner, self-employment, rental income, dividends.

#### Spending

Use the last three months as a reference for what you spend in a normal month. A rough number is fine to start. Once you link your accounts in the app, the exact figure is calculated for you.

#### Assets

Every account you own. I'd recommend opening each one in a separate browser tab as you go through onboarding, so you don't miss any. This step is inventory: every account, its current balance.

#### Debts

Credit cards, mortgage, auto, student loans, anything else. For each one, you want the current balance and the interest rate. Log in and check both. The rate on paper from years ago isn't necessarily what you're being charged today.

#### Benefits

Anything your employer contributes toward your future. That includes the employer match on your retirement plan and any pension or deferred compensation.

For the match, you want the formula, not just a percentage: 50% up to 6% of pay is different from a flat 3%.

#### Future life events

Any known costs or major events coming up: kids' college tuition, a new car, a new house. No documents needed. Just start thinking through what's on the horizon.

#### Cost basis

This one is the hardest, and it's the one to start on now.

Cost basis is the price you paid for each asset. The app uses it to model your tax liability. Knowing what you paid for your Bitcoin and other assets can save real money and give you an accurate picture of what you'll owe.

Balances and rates you can pull today. Basis lives in old exchange records and accounts you may have closed, and it gets harder to recover every year.

- **Bitcoin.** Go into every exchange you've ever used and download the transaction history (usually a CSV or Excel file).
- **Brokerage and retirement accounts.** Every brokerage has a transaction history export.

Save all of it into a folder. You'll come back to these files every time you update the plan.

### Homework

Set up one folder on your computer. Download every export you can get today, and label each file with the account name and date range. Basis is the priority; the rest can be gathered in parallel.


## 2.2 What your plan rests on: assumptions
*`TEACH` · 635 words · ~5 min*

> ⚠ **FIX BEFORE FILMING — the parenthetical below is wrong.** "Bitcoin at 40%
> forever **(its historical rate)**". 40% is a fine *assumption*; it is not the
> historical rate, which runs ~60–70% depending on the window. Relabel it as a
> deliberately conservative forward number — that's both accurate and a stronger
> position to defend. See `COURSE-IMPROVEMENT-ANALYSIS.md`, action item 3.

**By the end of this lesson, you can:**

- Understand what an assumption is and why it drives every projection
- See how one input can move a retirement date by years
- Pick a Bitcoin growth preset and inflation rate you can defend

---

An assumption is an input about the future that your plan treats as truth. Every projection is built on top of these numbers, so getting them right (or at least honest) matters more than any other single decision.

The six assumptions your plan uses:

- Investment returns, including Bitcoin
- Inflation
- Spending, now and in retirement
- Life expectancy
- Savings rate before retirement
- Future life events that change income or spending

### Lean conservative

Optimistic assumptions make the plan feel good today, but if they're wrong you find out years later, with the working years already spent.

Being conservative means you might be pleasantly surprised. Being optimistic means you might have to work longer than you thought, or spend less in retirement than you planned.

If you use high Bitcoin returns, the plan pulls your retirement date closer and tells you to save less. That's not a plan; it's a wish.

### How much one assumption can move things

Let's say we have someone who's 45 with 1.75 Bitcoin and $80,000 a year of spending:

- **Bitcoin at 40% forever** (a deliberately optimistic number). Earliest retirement lands around **age 50**.
- **Bitcoin at 20% now, declining as adoption grows.** Earliest retirement moves to around **age 58**.

Eight years, from one input. Nothing else about their situation changed.

### The four Bitcoin presets

The app has four built-in growth curves:

| Preset | Starting return | Ending return |
|---|---|---|
| Conservative | ~20% | ~6% |
| Moderate | ~30% | ~8% |
| Aggressive | Higher | Declines more slowly |
| Power law | ~38% | 10 to 15% |

Power law is what I use in my own plan until proven otherwise. It's a curve fitted to Bitcoin's entire price history since 2009, so it takes the argument out of picking a number.

Every preset declines. As Bitcoin gets larger, it's harder to move.

- At **$10 billion** Bitcoin, one big institution could move the entire market.
- At **$1 trillion**, doubling takes trillions of new dollars.
- At **$10 trillion**, doubling takes tens of trillions.

A declining preset is more honest than a flat annual return.

### Inflation

Inflation sounds like nothing, but it does a lot of damage over time.

If you're spending $80,000 a year today, over 15 years:

- At **3% inflation**, that same lifestyle costs about **$125,000/yr** at age 60.
- At **4% inflation**, it costs about **$144,000/yr**. About $20,000 more, every year.

The default in the app is 3%. If you think inflation runs hotter than that going forward, push it to 4-5%. I personally run it in that range.

### The other asset classes

Bitcoin gets the most attention because it moves the plan the most, but the app also has return assumptions for **stocks, bonds,** and **cash**. Those default to reasonable numbers. You can revisit them later if you want to run something more conservative.

### How to choose yours

Four things to keep in mind:

1. **Start conservative.** If the plan works on a conservative assumption, the upside becomes a bonus.
2. **Use a declining Bitcoin return.** Flat returns aren't realistic across a 30 or 40 year plan.
3. **Take inflation seriously.** Push 3% higher if the last few years told you to.
4. **Pick something you can live with if you're wrong.** The right assumption still holds up if the future doesn't cooperate.

### Your decision

**Which growth model and inflation rate your plan runs on.**

How to think about it:

1. **Start with what you'd defend out loud.** If you can't explain why you picked a curve, it isn't yours, it's a default you inherited.
2. **Ask which way you'd rather be wrong.** A conservative assumption shows you a later date on screen. An optimistic one can make the whole plan unreliable, which costs a lot more.
3. **Set inflation to what you actually believe**, not the default, because your future spending target rises with it.

### Homework

1. Pick your Bitcoin growth model and say out loud why you picked it.
2. Set your inflation number.
3. Enter both in the app under **Plan → Edit assumptions**.
4. Write one sentence for each: why this is the assumption you'd defend.

You'll get to change these later and see what the plan looks like under different assumptions. For now, we're setting the ones your baseline plan actually runs on.

## 2.3 The confidence ring: your plan's stress test
*`TEACH` · 925 words · ~7 min*

> 🐞 **LIVE BUG — this lesson's outcomes checklist renders empty (0 / 0).** The
> apostrophe in "how it's calculated" was escaped shell-style (`'"'"'`) inside a
> single-quoted HTML attribute, which terminates the attribute early and
> truncates the JSON. **10 of 50 lessons are affected.** See
> `COURSE-IMPROVEMENT-ANALYSIS.md`, action item 16.

**By the end of this lesson, you can:** *(not rendering in the app — see above)*

- Understand what your earliest retirement date is and how it's calculated
- Understand the confidence number and what the failing percent actually means
- Read the two together to see when you could retire and how sturdy that date is
- Know why Bitcoin needs a fat-tailed model

---

### Your earliest retirement date

Your earliest retirement date is the year your assumptions say you could stop working. It's your freedom date.

Freedom means different things depending on where you're at. It might mean full retirement, work becoming optional, or stepping back to only what matters to you. Whatever version you're planning for, the earliest retirement date is when the plan says you could safely make that move.

The date is deterministic: it runs your numbers forward using the average returns from your assumptions. One line into the future, no stress test. Real markets don't work that way, which is where the confidence number comes in.

### The confidence number

The confidence number runs your entire plan through a thousand different simulated futures, each with different market results, then counts how many succeeded.

If your confidence number is 82%, that means 820 of those thousand runs succeeded on your numbers.

The failing 18% is not the probability you go broke. It's the probability you'd need to make adjustments: spending a little less for a stretch, working a year longer, or delaying a purchase. Failure in the simulation means the plan needed to bend, not that you ended up with nothing.

### Reading the two together

- The **date** tells you *when*.
- The **confidence number** tells you *how sturdy that date is*.

Age 60 at 82% confidence is a real answer. Age 60 at 55% confidence would be the same date on the screen with a much weaker plan behind it.

You want to look at both. A high confidence number with a date you can live with is what we're building toward.

### What the simulation is actually running

The simulation doesn't just shuffle a portfolio return. It runs your entire plan inside every one of those thousand futures.

For each run:

- Start from your real balances today (Bitcoin, brokerage, retirement accounts, cash).
- In year one, every asset gets its own return based on your assumptions and its historical volatility.
- Your actual life runs: income in, taxes out, spending, withdrawals in your order, contributions, debt payments. You land on new balances.
- Year two starts fresh with new market returns. Same steps. Then year three. Forty-five years of that is one complete future.

Then it runs another 999 futures with different market returns and counts how many succeeded.

Running your real life inside every path makes the answer sensitive to your plan, not just to your portfolio.

### Why Bitcoin needs a fat-tailed model

Most models assume returns follow a normal bell curve. Point one at Bitcoin and it'll tell you a year down 70% basically never happens. Anyone in Bitcoin for more than a cycle knows that's wrong.

Bitcoin has had years down more than 70%, and years where it tripled. Those extreme years show up in Bitcoin's history far more often than a bell curve would predict. "Fat tails" means the extremes on both ends stay likely, instead of vanishing the way they do in a normal distribution.

The engine uses a fat-tailed distribution for Bitcoin, calibrated to its actual return history (shape sourced from Swan Bitcoin research). If you built a plan on a bell-curve model of Bitcoin, the plan would look sturdier than it is.

### The volatility table

Every asset in the simulation has its own volatility and range:

| Asset | Volatility (annual) | Single-year range |
|---|---|---|
| **Bitcoin** | ~50%, easing toward 20% as it matures | -75% to +250% |
| Stocks | 16% | -40% to +50% |
| Real estate | 12% | (n/a) |
| Bonds | 5% | (n/a) |
| Cash | 1% | (n/a) |

Bitcoin's -75% floor is set just past its worst actual year (-73% in 2018). The +250% cap prevents the fat tail from producing years that never happened.

A 50% volatility means Bitcoin moves about three times as far as stocks in a typical year. That's why a Bitcoin holder needs a bigger cash reserve than a stock holder does (Module 2).

### Correlations

The assets aren't run independently. Markets move together in the real world.

- **Bitcoin and stocks** are tied at a correlation of about **0.35**. They don't move in lockstep, but they tend to fall in the same years more often than not.
- **Inflation** is negatively correlated with stocks: in the paths where costs rise, balances tend to fall.

Correlations come from J.P. Morgan's long-term capital market assumptions and research from ARK Invest and Fidelity Digital Assets.

### How to read your number

A few things to keep in mind:

- **A high number means fewer adjustments.** 82% doesn't mean 18% chance of going broke. It means the plan needed to adjust in 180 of the thousand runs.
- **Watch for big moves, not small ones.** Small run-to-run changes aren't meaningful. If a change to your plan moves the number 5-10 points, that's the change telling you something.
- **The number is directional.** It's a stress test on research and history. When the research updates, the app's numbers update with it.

### Your decision

**What confidence level you're aiming for, and which lever you'd pull if you come in under it.**

How to think about it:

1. **Pick your target before you see your number**, so the number doesn't talk you into whatever it already says.
2. **Decide the lever in advance.** There are only four: work a little longer, spend a little less, save more, or change the allocation. Picking now means a low number becomes a to-do instead of a bad night.
3. **Remember that 100 was never the goal.** A very high number usually means you're over-saving and under-living.

### Homework

1. Run the confidence check in the app and write your number down.
2. Write your target number next to it.
3. Name the one lever you'd pull first if you're under it. One, not four.

The next module builds the cash flow that lets you keep buying Bitcoin without being forced to sell at the wrong time.

## 2.4 Walkthrough: set up your plan in Orange Plan
*`DEMO` · 3,297 words · ~20 min read*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **2.4**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Complete Orange Plan onboarding with your baseline inputs
- Verify and correct accounts, holdings, and debts on the Dashboard
- Mark non-cash reserve holdings with the shield icon
- Set assumptions on the Plan page
- Read your earliest retirement date and run the confidence ring
- Add likely life events and save a baseline PDF

---

Two laps back-to-back. Part A is the onboarding wizard — the first 15 minutes with Orange Plan, by the end of which you have a working plan with a retirement date on it. Part B goes into the plan you just built, verifies it against reality, and gets it ready to actually use.

Set aside about 30 minutes total. Have your account balances, debt balances and rates, and last year's spending nearby before you start.

### Part A — Onboarding

The wizard has 13 steps. The counter at the top reads **1/13 · Privacy** through **13/13 · Review**. The app saves as you go, so you can leave at any point and come back. A green **Auto-saved** pill next to the progress label confirms it.

#### The layout

Learn the layout once, then ignore it:

- Top-left: **N/13 · {step name}** progress label and the **Auto-saved** pill.
- Top-right: **Sign out** and **Skip to app**.
- Bottom bar (steps 2 through 12): **Back**, **Skip for now**, and **Save & finish later**.

#### Step 1: Privacy

Two cards:

- **Cloud.** Syncs across devices, backs up your data, and enables bank linking. Pick this one.
- **Local Only.** This browser only. More private, but if the browser data is lost, it's on you.

You can change this later in Settings. Module 8's dead-man switch needs Cloud.

Click **Continue**.

#### Step 2: About You

Seven sub-slides. The button reads **Next** until the last slide, then **Continue**.

| Slide | What to enter |
|---|---|
| How old are you? | Slider to your age. |
| When do you want to retire? | Your target age. The subtitle updates: *"That gives you N years to build wealth."* |
| How do you file taxes? | Filing status. This one hard-blocks Continue if left blank. |
| How old is your spouse? | Only appears if you picked married. |
| Do you have dependents? | How many, then optional names and ages. Used so child tax credits phase out correctly over time. |
| Where do you live? | State selector. Shows a **No state tax** badge for states like TX, FL, NV. Module 5 covers why this matters. |
| How do you earn income? | W-2, self-employed, and so on. Self-employed changes the shape of Step 3. |

#### Step 3: Income and Spending

Four sub-slides for a typical W-2 household.

**Your income.** Quick-pick chips for common salary levels ($150k, $100k, etc.) or type your own.

**Spouse income.** Field: **Spouse W-2 income**. Two other spouse fields sit below (self-employment, S-corp K-1). Leave them blank unless they apply.

**Living spending.** Read the subtitle carefully: *"Living spending only. Housing, food, bills, travel, and everyday spending. Exclude debt payments."*

⚠ This is the single most important number to get right. Living expenses only. Not your paycheck. Not your debt payments. If you enter your salary here, every projection downstream will be wrong.

> ⚠ This is the single most important number to get right. Living expenses only. Not your paycheck. Not your debt payments. If you enter your salary here, every projection downstream will be wrong.

Enter your annual spending. Two panels appear:

- **Savings rate.** Green at 30% or higher, amber at 15 to 29%, plain below that.
- **Approx. monthly room before debt.** Red if negative (spending more than you take home).

**Retirement spending.** Usually the same as today, unless you know it will change. Like the living number, it excludes debt payments. The app tracks those separately. The panel shows a **Monthly in retirement** figure.

> ✅ **Added in course 2026-07-29** (item 19): the sentence below now states
> that retirement spending excludes debt payments. A matching line went into
> walkthrough 7.7's Step 1.

#### Step 4: Accounts

Heading: **Where do you hold investments?**

You can skip the Plaid **Link accounts** card if you don't want bank linking, and stay manual.

To add an account: **Add Account** → pick account type → name the account (suggested-name chips available) → pick owner (You, Spouse, or Joint) → **Add Account**.

Add every real account. Common types and example names:

- **Hardware Wallet.** Coldcard, Trezor, Ledger.
- **Crypto Exchange.** Strike, Coinbase, Kraken.
- **Taxable Brokerage.** Fidelity, Schwab, Vanguard.
- **401(k).** Fidelity 401k.
- **Savings Account.** HYSA, Ally.

There's no generic "Bitcoin account". The app makes you say where your Bitcoin is held. That distinction feeds directly into the Custody module.

When you're done, look for the green line: **✓ N accounts ready to track**.

#### Step 5: Assets

Heading: **What do you own?** A live **Total Portfolio Value** card sits at the top.

For each account, click **+ Add Holding**, pick the asset type, fill in **Holding Details**, and click **Save Holding**.

By asset type:

- **Bitcoin.** Enter **How much BTC?** as a quantity, never in dollars. Enter **Total cost basis** if you know it. If not, leave it blank.
- **Stocks or ETFs.** Enter the ticker and share count. Watch for *"Fetching live price..."* followed by the live price line.
- **Cash or Savings.** Enter the current dollar value.

⚠ Never type a price for a live asset. The app knows it. Watch the dollar line under the quantity update as you type.

⚠ The app never invents cost basis. Enter it if you know it. Leave it blank if you don't. A missing basis becomes something to fix in Module 5, not a made-up number.

> ⚠ Never type a price for a live asset. The app knows it. Watch the dollar line under the quantity update as you type.

> ⚠ The app never invents cost basis. Enter it if you know it. Leave it blank if you don't. A missing basis becomes something to fix in Module 5, not a made-up number.

#### Step 6: Transactions

Heading: **Would you like to add recent transactions?**

You're building the plan, not reconciling the books. Click **Skip for now** in the bottom bar. Footnote: *"You can skip this and use Update Transactions from the Dashboard anytime."*

You can come back later and use any of the three transaction-update methods (link, CSV, or manual) from the Dashboard.

#### Step 7: Debts

Heading: **Any debt to track?**

Click **Add Debt**, then pick a debt type. Every row shows a default rate and term.

A few examples:

- **Mortgage.** Default rate 7%, 360-month term.
- **Credit Card.** Default rate 22%.
- **BTC-Backed Loan.** Default rate 10%, 12-month term. This is a first-class debt type in the app, with collateral tracking, live LTV (loan-to-value: what you owe divided by what the collateral is worth), and liquidation lines. Modules 4 and 6 cover it.

For each real debt, enter: **Current balance**, **Interest Rate**, **Term (months)**, and **Monthly payment** (leave blank; the app estimates it).

⚠ Auto Loan prefills the rate at 8.5%. This is the app's default value, so overtype it with your actual rate.

> ⚠ Auto Loan prefills the rate at 8.5%. This is the app's default value, so overtype it with your actual rate.

The estimate line reads: *"Estimated from balance, rate, and term: $X/mo. Edit if your servicer payment is different."*

Two tiles at the top of the step show **Total Debt** and **Monthly Payments**. Module 4 gives each debt a job. A 22% credit card and a 3.25% mortgage are not the same problem.

#### Step 8: Contributions

Heading: **Ongoing Contributions**. Rows are generated from the accounts you added in Step 4.

For each row:

- Annual amount (for example, 401(k) → $12,000).
- Toggle **Employer match** to enter a match rate (%) and the pay percentage it applies to. The row computes an **Estimated employer contribution: $X** line and shows *"N% match on the first M% of salary."*
- **Roth IRA.** (Roth means you pay the tax now, and the growth and the withdrawals come out tax-free later.) Enter your annual amount. Read the shared meter: **IRA total** with *"Traditional + Roth share one annual IRA limit per person."* If you go over, the app warns you to reduce one of them.

Enter your current reality only. The optimized routing is Module 3's job. The app knows that and hands routing to Savings Strategy after onboarding.

#### Step 9: Retirement Benefits

Heading: **Expected Social Security**.

- **Your monthly amount at Full Retirement Age.** The field pre-fills a placeholder, and the helper text points you to **ssa.gov/myaccount** for your estimate.
- **Opt-out.** The **I don't expect to receive Social Security** option exists if you're planning without it.
- **When will you start Social Security?** Three cards: **62 Early (~30% less)**, **67 Full (100% benefit)**, **70 Max (~24% more)**.
- **Spouse's amount and start age.** Same three-card choice.
- **Plan through what age?** The chip **90 · Common planning age** is a reasonable default.

Longer horizons are more conservative. Running out at 90 because you planned to 80 is the failure the plan is designed against.

#### Step 10: Assumptions

Not skippable. Heading: **Planning Assumptions**.

⚠ **Moderate** is pre-selected. You have to actively pick an assumption card. The app doesn't want a passive click here.

> ⚠ Moderate is pre-selected. You have to actively pick an assumption card. The app doesn't want a passive click here.

Four cards:

| Card | Tagline | BTC | Stocks | Bonds | Inflation |
|---|---|---|---|---|---|
| **Conservative** | 20% to 6% declining BTC curve | 15% | 7% | 4% | 3.5% |
| **Moderate** | 30% to 8% | 22% | 7% | 4% | 3% |
| **Aggressive** | 45% to 10% | 30% | 8% | 4% | 3% |
| **Power law** | Bitcoin regression curve | 24% | 7% | 4% | 3% |

Even the more aggressive presets decline over time. As Bitcoin gets larger, growth slows down, which is the reason behind every declining preset in the assumptions lesson.

Pick the preset that lines up with the choice you made in the assumptions lesson. My default is Power law. Conservative if you want more headroom. The app's own line: *"These assumptions are just a starting point…"*

#### Step 11: Strategy Profile

Ten required questions. **Continue** is disabled until every one is answered.

The ten:

- Which best describes Bitcoin's role in your plan?
- How strong is your Bitcoin conviction?
- What is the maximum Bitcoin allocation you are comfortable holding?
- If Bitcoin dropped 50 to 80%, what would you most likely do?
- When do you want to be financially independent?
- How do you feel about holding cash?
- In a market downturn, how much could you cut spending temporarily?
- How do you think about debt?
- How involved do you want to be in plan execution?
- Rank your top three priorities and mark one as primary.

⚠ Answer honestly, not aspirationally. Question 4 is the allocation-module stress test asked in advance.

> ⚠ Answer honestly, not aspirationally. Question 4 is the allocation-module stress test asked in advance.

#### Step 12: Life Events

Heading: **Life Events**.

Five quick-add types: **Job or income change**, **Windfall or inheritance**, **Large purchase**, **College expense**, and **Expense change**.

For each event, add:

- Your age when this happens.
- Total cost across all years.
- Description.

Then click **Add Event**. The app spreads multi-year events (like college) across years automatically. The Continue button relabels to **Continue with N event(s)**.

Add events you're likely to have. Speculative what-ifs belong in Scenarios later, which you can build on the Plan page.

#### Step 13: Review

Watch the hero before the review content appears.

**The spinner.** Three rotating lines:

- *"Projecting your balances year by year…"*
- *"Running 300 market paths…"*
- *"Checking your spending target…"*

**The date.** Label **EARLIEST RETIREMENT · AGE {X}**, then the year appears.

**The ring.** *"This plan succeeds in {pct}% of 300 market paths at age {X}."*

⚠ The onboarding finale runs 300 paths. The Plan page's Monte Carlo runs 1,000. Same math, different sample sizes. The setup screen keeps it fast. You'll re-run the full 1,000-path ring in Part B.

> ⚠ The onboarding finale runs 300 paths. The Plan page's Monte Carlo runs 1,000. Same math, different sample sizes. The setup screen keeps it fast. You'll re-run the full 1,000-path ring in Part B.

Below the hero, the review fades in with:

- **Current snapshot** net worth, and four cards: Bitcoin, Other assets, Annual savings, Time to retirement.
- **Modeled details** rows: Household income, Current annual spending, Retirement spending target, Monthly debt payments, Social Security, Planning assumptions.

Reassurance line: *"…Nothing is locked in here. You can continue editing details once you enter the app."*

Click **Go to your dashboard**.

## 2.5 Walkthrough: build your baseline in Orange Plan
*`DEMO` · ~1,100 words · ~9 min read*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **2.5**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Verify every account and holding against reality
- Shield the holdings that are your reserve
- Read your earliest retirement date and confidence ring together
- Save a baseline PDF as your starting-point snapshot

---

Onboarding gave you a plan. This walkthrough makes it accurate and ready to use, which is the difference between a demo and a baseline.

### The baseline lap

Onboarding gave you a plan. Part B makes it accurate and gets it ready to actually use. About 15 minutes.

#### Step 1: Verify the baseline on the Dashboard

Go to the Dashboard. The hero at the top shows your **Net Worth**, and below it is the section labeled **Accounts & Holdings**.

Expand each account group and check that every holding is correct. Every holding row has an **Edit** link and a three-dot menu with **Edit holding** and **Delete holding**. The group header menu has **Edit account** and **Add holding**.

If a number is wrong, fix it at the source, meaning the holding itself. Don't nudge a total to make a mismatch go away.

⚠ You're not making it perfect. You're making it accurate.

> ⚠ You're not making it perfect. You're making it accurate.

#### Step 2: Add any missing accounts and holdings

If any accounts or holdings didn't get entered during onboarding, add them now. The flow is the same as Steps 4–5 of onboarding: **Add Account** for a new account, then **Add Holding** on an account for what's inside it.

Every real account should be in here. Hardware wallet, exchange, brokerage, retirement accounts, checking, savings.

#### Step 3: Update your transactions

Once accounts and holdings are in, keep them current by updating transactions. **Dashboard → Update Transactions** opens the dialog, and it asks *“How would you like to update transactions?”* There are four answers:

1. **A linked account.** The app connects to your bank and brokerage and pulls transactions automatically.
2. **A downloaded file.** Most exchanges and brokerages let you download a CSV or Excel export. Upload it and the app parses it.
3. **Describe one transaction to AI.** Tell Orange Plan AI about a single purchase or sale in plain language. You review every field before it saves.
4. **I'll enter them myself.** Add a purchase, sale, or transfer by hand. For accounts that don't support linking or a file export.

You don't have to do this now. The Dashboard has an **Update Transactions** button you can come back to anytime.

#### Step 4: Mark your reserve holdings with the shield icon

Not all reserves are cash. If you're holding your reserve in short-term treasuries, a money-market fund, or another safe asset, tell the app to count it as reserve.

Every non-cash holding has a **shield icon** on the row. Click it to mark that holding as part of your reserve. Cash is counted automatically.

Marking a holding as reserve tells the app to treat it as part of your safety net when it runs your plan. Module 2 covers what the reserve is and how to size it.

#### Step 5: Set your assumptions on the Plan page

Go to the **Plan** page. In the top right, click the **gear icon**.

The gear menu has:

- The four Bitcoin growth presets (Conservative, Moderate, Aggressive, Power law).
- Custom per-period returns if you want to override the presets.
- Inflation.
- Life expectancy and other planning inputs.

Pick your Bitcoin preset based on the assumptions lesson. My default recommendation is Power law, but pick what you can live with if you're wrong.

Set your inflation rate. The default is 3%. If you think inflation will run higher going forward, 4% or 5% is a more conservative choice.

Save and close the gear.

#### Step 6: Read your earliest retirement date

Still on the Plan page, look at the hero at the top. It shows your **Earliest Retirement Age**, with the year underneath.

The date on the hero is the year your plan says you could stop working, using the assumptions you just set. This is your baseline freedom date.

Underneath the date are two chips:

- **N years away**
- **$X/yr target** (the spending your plan is funding)

The chart below the hero has a toggle in the top right: **Today's $** or **Nominal $**. Leave it on **Today's $**. A million dollars in 2050 isn't a million dollars in today's money, and Today's $ is the honest view.

#### Step 7: Run the confidence ring

On the same hero, look at the right side. On a fresh plan, the ring doesn't exist yet. You'll see:

**PLAN CONFIDENCE** with a **Run Monte Carlo** button underneath.

Click it. The simulation runs a thousand market paths through your plan and takes about 10 to 20 seconds.

When it lands, three things appear:

- The ring with your confidence number.
- A verdict: **Plan on track** (80+), **Plan needs review** (60 to 79), or **Plan needs attention** (under 60).
- A **sampling range** with an "as of" date and a re-run icon.

Read the date and the ring together, the way we covered in the confidence-ring lesson. The date tells you when. The ring tells you how sturdy that date is.

#### Step 8: Add likely life events

Still on the Plan page, scroll below the projection chart to the **Life events** section.

You should already have at least one event from onboarding. Click **Add event** to add anything else that's likely coming (home sale, income change, large planned expense).

Add events you're likely to have. Not what-ifs. Speculative what-ifs belong in Scenarios, which you can build on the Plan page.

If you've already run the confidence ring, adding an event makes a **Recheck** chip appear next to the ring. Click it to re-run the simulation with the new event in place.

#### Step 9: Save your baseline PDF

Once everything looks right, save a copy of your plan as a PDF.

Open the **Account menu** in the top right (or the hamburger drawer on mobile), then click **Report**, then **Download PDF**.

The button triggers your browser's print dialog. Choose **Save as PDF** and put the year in the filename, like `baseline-2026.pdf`.

Module 10 covers how to read this document like a planner. For now, just save it. It's your starting-point snapshot.

### Using the AI assistant as you go

The app has an AI assistant built into every page.

- The top-right button on any page opens the assistant. On broad pages like the Dashboard or Plan page, it lets you ask general questions about your plan.
- On each specific page, the top button surfaces preset conversations relevant to that page. On the Plan page you'll see preset prompts about your projections, assumptions, or freedom date. On the Accounts page you'll see prompts about your holdings and allocation.

Use it whenever something in the app isn't clear, or when you want a second look at a decision before you make it. It has full context on your plan.

### What good looks like

- Savings rate is green or high amber.
- **Approx. monthly room before debt** is positive.
- **Total Portfolio Value** matches your own rough sum.
- **Total Debt** and **Monthly Payments** match what actually leaves your account.
- **IRA total** meter isn't over the shared limit.
- Every account and holding is in the app and matches reality.
- Any reserve holdings that aren't cash have the shield icon toggled on.
- The Plan page shows an earliest retirement age and a confidence ring, both readable.
- The **Life events** section has your likely events, and only those.
- You have a baseline PDF saved somewhere you can find later.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Storage mode (Cloud or Local) | Settings → Data & Privacy |
| 2 | Planning profile (ages, filing, dependents, state, income type) | Settings and Plan inputs |
| 3 | Income and spending numbers | Cash Flow and Plan |
| 4 | Accounts with owners | Dashboard → Accounts & Holdings |
| 5 | Holdings with quantity, cost basis, live prices, cash values | Dashboard account groups |
| 6 | Debts with rates and terms | Strategy → Debt |
| 7 | Ongoing contributions and employer match | Cash Flow contribution rows |
| 8 | Social Security amounts, start ages, planning horizon | Plan → Income |
| 9 | Assumption preset | Plan and Scenarios |
| 10 | Ten Strategy Profile answers | Settings |
| 11 | Life events | Plan → Retirement → Life events |
| 12 | Earliest retirement date and confidence ring (1,000 paths) | Plan hero |
| 13 | Baseline PDF | Saved locally with the year in the filename |

### Handing it off

The next module covers the cash flow that makes this plan possible. Where your surplus comes from, and how to protect it so you're not forced to sell Bitcoin at the wrong time.

---
