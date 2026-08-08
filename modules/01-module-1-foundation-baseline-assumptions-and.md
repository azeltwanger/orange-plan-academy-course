# Unit 2 · Module 1 — Foundation: baseline, assumptions, and the confidence number

*Gather the six pieces of your baseline, choose your assumptions (especially the Bitcoin growth number), understand the confidence ring that stress-tests your plan, run three scenarios, and know when a plan actually needs updating.*

## 1.1 What to gather before you build the plan
*`TEACH` · ~952 words · ~6 min*

**By the end of this lesson, you can:**

- Gather the documents you need for the app
- Track down cost basis while records still exist
- Save the exports into a folder you can reuse each year

---

In today's lesson, we're going to cover the documents that you're going to need to gather before you start building your financial plan.

This part is extremely important because every decision that we make in later modules and lessons is downstream and can be based off of all of the data that we put into the model to begin with. Taking the extra time to be accurate up front is going to save you from making misguided decisions based off of guesswork and data that's not up to date and accurate.

Every number that comes out of your plan is only as good as what you put in it. If your spending number is just a rough guess, if what you need to spend in retirement and what you're currently spending month to month today is a rough guess, your retirement date is also going to be a guess. Another example: if your transaction history or your cost basis is missing, this can affect your tax calculations and prevent you from having as accurate numbers as we possibly can.

Taking 30 minutes to an hour now to gather all of this information can be a really valuable exercise in getting organized, because most people that I work with are not organized when it comes to their personal finances. Just taking the time to go through this and gather everything so that we can put all of it together in one place to make smart decisions is beneficial for you. I know it can be a little bit of a pain, but it's definitely worth it.

### What to gather

1. Your income. You want recent pay stubs so you can verify what's coming in per period and then what's coming in every year. If you own a business, you're going to want to include every stream of income that you have. If you have multiple businesses, if there are two earners, if you and your spouse both work, you're going to want to include pay stubs for both of you and earnings and income from both of you. This includes things like businesses, rental income, and investment dividends that you get.

2. Your spending. As a rule of thumb, I like to use the last 3 months as a reference for about what you spend every month. A rough number here is fine to start with. Once you link your accounts in the app, the exact figure is going to be calculated for you, so you don't have to go digging through all of your credit cards and expenses. If you don't do that, then I would recommend going through all of your spending accounts or credit cards to get a more exact figure of what you're spending every month.

3. Your assets. This is going to be every account and asset that you own. What I recommend is opening each one in a separate browser tab as you go through onboarding so you don't miss any of your accounts. This step is going to be just an inventory of all of your assets: every account and what the current balances are. This includes things like your house. You can use Zillow or an estimate of what your house might be worth in your neighborhood or area. This includes things like your pension and retirement accounts, brokerage accounts, Bitcoin, hardware wallets, exchange accounts, and anywhere where you might have dollars, checking, and savings as well.

============================================================
NOT YET DICTATED — placeholder text below, kept only so nothing is lost.
Replace when Austin records items 4-7 and the homework.
============================================================

4. Your debts. Credit cards, mortgage, auto, student loans, anything else. For each one, you want the current balance and the interest rate. And actually log in and check both, because the rate on paper from a few years ago isn't necessarily what you're being charged today.

5. Your benefits. This is anything your employer contributes toward your future — the match on your retirement plan, any pension or deferred comp. For the match, you want the formula, not just a percentage. 50% up to 6% of pay is a different thing than a flat 3%.

6. Future life events. Any known costs coming up — kids' college, a new car, a new house. There's no documents needed for this one. Just start thinking through what's on the horizon.

### Cost basis — start this one now

7. The last one is cost basis, and this is the hardest one, so it's the one to start on now.

Cost basis is the price you paid for each asset. The app uses it to model your tax liability, and knowing what you actually paid for your Bitcoin can save you real money and give you an accurate picture of what you'll owe.

Balances and rates you can pull today. Basis lives in old exchange records and accounts you may have closed, and it gets harder to recover every year.

So for Bitcoin, go into every exchange you've ever used and download the transaction history. It's usually a CSV or an Excel file. And for your brokerage and retirement accounts, every brokerage has a transaction history export.

Save all of it into a folder, because you're going to come back to these files every time you update the plan.

### Your decision

What you're going to gather, and by when.

### Put it in Orange Plan

Nothing yet. This one is a shoebox, not a screen. The walkthrough enters it all.

### You are done when

Every account, balance, income source and debt is written down in one place, and the totals match what you'd tell a planner out loud.


## 1.2 The three layers of a plan, and setting your assumptions
*`TEACH` · ~9.3 min · the script is canonical (`scripts/01-2_…`)*

> ✅ The "(its historical rate)" parenthetical is **fixed** in the script — 40%
> now reads as *"a deliberately optimistic number."* This master body predates
> the three-layers rewrite; the script layer is the current one.

**By the end of this lesson, you can:**

- Separate the three layers a plan is built from, and know which one you are typing into
- Tell a preview from a change you have actually applied, and name where your plan of record lives
- Understand what an assumption is and why it drives every projection
- See how one input can move a retirement date by years
- Pick a Bitcoin growth preset and inflation rate you can defend

---

### The three layers

| Layer | Meaning | Example |
|---|---|---|
| **Baseline** | True now | Current income is $150,000 |
| **Life event** | A change you expect | Tuition ends next year |
| **Scenario** | A question, not a decision | What if I retire three years earlier? |

**Truth goes in the baseline. Expected changes go in life events. Questions go in scenarios.**

**Second distinction:** current cash flow answers what is available *now*; the projection answers where today's pattern *leads*. This is not a budgeting app that wants every coffee categorized forever.

### Previews versus your actual plan

The third distinction is about the app rather than the plan, and it is the one people get bitten by. Many screens show what a change *would* do before anything is decided: click a chip, set a schedule, compare two strategies, and the numbers move. **That is a preview. Your plan has not changed.**

| | Where it lives | Is it your plan? |
|---|---|---|
| **Preview / sandbox** | The screen being worked on | No. Nothing is saved |
| **Applied change** | Committed with **Apply to plan** | Yes. **Revert** walks it back |
| **Scenario** | Kept separate on purpose | No. It is a question |
| **Plan of record** | The **Plan page** | Yes. What everything else is measured against |

> **If you didn't click Apply, it didn't happen.**

⚠ **Taught here on purpose.** The Apply/sandbox behaviour was previously introduced in the Module 6 walkthrough — six modules after students start being confused by it. This is the "is this my plan or a scenario?" stall from the client calls, in its app-mechanics form.

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

So your decision out of this lesson is which growth model and which inflation number your plan is going to run on.

Start with what you'd actually defend out loud, because if you can't explain why you picked a curve, then you didn't really pick it, you just left whatever the app had loaded. Then ask yourself which way you'd rather be wrong. If you're conservative and you're wrong, you just retire earlier than the screen said. If you're optimistic and you're wrong, the whole plan was built on something that didn't happen. And set inflation to what you actually believe, not whatever the default is, because your future spending rises with that number.

### Put it in Orange Plan

Plan → Retirement → Edit assumptions. Set growth and inflation, and leave the defaults only if you'd defend them.

### You are done when

You could say out loud why each assumption is the number it is. That's the same standard the report's assumptions section is held to, and it's the one that catches a number you picked because you liked the answer.


## 1.3 Read your retirement date and confidence number
*`TEACH` · ~1,131 words · ~7 min*

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

In today's lesson, we're going to cover the two numbers at the top of your plan, your earliest retirement date and your confidence number, and how to read them together.

Before either one, though, I want to name what you're looking at, because this matters more than it sounds.

What you're about to see is your first retirement read. It's a draft, built on the baseline you just entered and nothing else. Your cash flow decisions aren't in it. Your debt policy isn't in it. Your allocation and your tax decisions aren't in it, and neither is the order you'll eventually draw accounts down in, because you haven't made any of those decisions yet.

So hold it loosely in both directions. Don't treat an exciting date as finished, and don't dismiss the whole thing because the first number looks rough. This is a starting-point snapshot, and it becomes your actual plan as you make the decisions in the modules ahead. You'll watch it move, and watching it move is most of the point.

### Where the numbers come from

> 🔶 **F21 — INSERTED SECTION (~45 s), not from a prior dictation.** Added
> 2026-08-08 because the client calls kept returning to *"where did this number
> come from?"*, *"which page controls it?"* and *"which account funds this?"*,
> and no lesson answered it directly. This is the smallest thing that closes it:
> one reusable frame, recalled per module, rather than a new lesson. **Keep it,
> rewrite it, or cut it at the mic** — the graphic carries the idea either way.

> 🎬 **GRAPHIC (`visuals/1-3b_number-flow.md`) — the reusable frame.** WHAT YOU
> CHANGE → WHAT THE APP CALCULATES → WHAT MOVES DOWNSTREAM, with three worked
> rows underneath. Recalled in every module walkthrough. The three column labels
> are the words the sheets say out loud: **CALCULATED FROM · EDIT SOURCE · THIS
> AFFECTS.**

Nothing in this app is typed in twice. Every number you see is **calculated from** something upstream, has exactly one **edit source**, and **affects** something downstream.

So there are three questions worth asking about any number on your screen: what is it calculated from · where do I edit it · what does it affect.

| What you change | What the app calculates | What moves downstream |
|---|---|---|
| Income − taxes − living − debt | **Surplus** | Reserve funding, contribution routing, retirement date |
| A **life event** | Future spending in that year | Account withdrawals, retirement date, confidence |
| A **return assumption** | Projected balances and simulated paths | Earliest date and confidence number |

Every walkthrough in this course points at those same three things when a number matters. If you find yourself staring at a figure wondering where it came from, that is the question to ask, and there is always an answer.

### Your earliest retirement date

The date tells you when. The confidence number tells you how sturdy that date is. And most tools only show you the date.


Your earliest retirement date is the year your assumptions say you could stop working. I think of it as your freedom date.

And freedom means different things depending on where you're at. It might mean full retirement, it might mean work becoming optional, or it might mean stepping back to only the things that matter to you. Whatever version you're planning for, this date is when the plan says you could safely make that move.

One thing to understand about the date: it's deterministic. It runs your numbers forward using the average returns from your assumptions. One line into the future, no stress test. And real markets don't work that way — which is where the confidence number comes in.

### The confidence number

The confidence number takes your entire plan and runs it through a thousand different simulated futures, each one with different market results, and then it counts how many of them succeeded.

You'll see this called a Monte Carlo simulation, and that's the label on the button in the app. Don't let the name throw you. All it means is running your plan a thousand times instead of once, so you're looking at a range of outcomes instead of a single guess.

A client asked me a sharp question about this once. He wanted to know whether it models a bad thing happening on top of another bad thing. Like, the price already dropped 50%, does any of those runs have it dropping another 30% from there?

Yes. That's exactly what those thousand runs are for. Some of them are gentle, some of them stack a terrible year onto another terrible year, and a few of them are genuinely brutal. You're not looking at one guess about the future. You're looking at a spread of them, including the ugly ones.

So if your confidence number is 82%, that means 820 of those thousand runs succeeded on your numbers.

An 82% result means 820 of the 1,000 paths funded the plan as written. The other 180 fell short. Those paths tell you to test adjustments — spending a little less for a stretch, working a year longer, delaying a purchase. The score alone doesn't prove that one small change rescues all of them. And it isn't a forecast that you end up with nothing.

### Reading the two together

The date tells you when. The confidence number tells you how sturdy that date is.

Age 60 at 82% confidence is a real answer. Age 60 at 55% confidence is the same date on the screen with a much weaker plan behind it. So you want to look at both. A high confidence number, with a date you can live with — that's what we're building toward.

### What the simulation is actually running

Let me show you what the simulation is actually doing, because it's more than shuffling one portfolio return.

Every one of those thousand futures runs your entire plan. It starts from your real balances today — your Bitcoin, your brokerage, your retirement accounts, your cash. In year one, every asset gets its own return based on your assumptions and its historical volatility. Then your actual life runs: income comes in, taxes go out, spending happens, withdrawals happen in your order, contributions and debt payments happen. You land on new balances. Then year two starts fresh with new market returns, and it does it again. 45 years of that is one complete future.

Then it runs another 999 futures with different markets and counts how many succeeded. Running your real life inside every path is what makes the answer sensitive to your plan, and not just to your portfolio.

### How to read your number

Three things to keep in mind when you read yours:

1. A high number means fewer adjustments. 82% doesn't mean an 18% chance of going broke. It means 180 of the 1,000 paths came up short under the plan exactly as written.
2. Watch for big moves, not small ones. Small run-to-run changes aren't meaningful. If a change to your plan moves the number 5 or 10 points, that's the change telling you something.
3. And the number is directional. It's a stress test built on research and history, not a guarantee.

You're going to run your own confidence ring for the first time in the walkthrough at the end of this module.

### Your decision

Your decision here is what confidence level you're aiming for, and which lever you'd pull if you come in under it.

Pick your target before you look at your number, so the number doesn't just talk you into whatever it already says. Then decide your lever in advance, because there are really only four: work a little longer, spend a little less, save more, or change your allocation. If you pick that now, a low number turns into a to-do item instead of a bad night. And remember 100 was never the goal. A very high number usually just means you're over-saving and under-living.

### Put it in orange plan

Plan → Retirement → guardrails policy, so the app knows what on track means for you.

### You are done when

Your date and your confidence number are both on screen and you read them as a pair. If you're under where you want to be, you've named one lever you'd pull first. One, not four.

Then watch the two walkthroughs below this video, where we set the plan up in Orange Plan and build your baseline.


## 1.4 Walkthrough: set up your plan in Orange Plan
*`DEMO` · 3,297 words · ~20 min read*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **1.4**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

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
> walkthrough 6.4's Step 1.

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

## 1.5 Walkthrough: build your baseline in Orange Plan
*`DEMO` · ~1,100 words · ~9 min read*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **1.5**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

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
- A verdict word: **Very well funded** (above 95), **On track** (80 to 95), **Room for improvement** (50 to 79), or **Needs significant changes** (under 50). Read the word off the screen.
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

Module 9 covers how to read this document like a planner. For now, just save it. It's your starting-point snapshot.

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

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A1.1 How Orange Plan models Bitcoin: fat tails, correlations, floors and caps**
  → *Watch this if either is true on your own screen: changing one assumption moved your Plan page's confidence number by more than 10 points and you want to know why, or you are about to hand your report to someone who will ask how the simulation works. If your number is stable and nobody is auditing it, core 1.3 already taught you to *read* it and your plan is complete without this. This lesson is how the number is *built*.*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
