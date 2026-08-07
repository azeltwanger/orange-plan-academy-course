# Unit 11 · Module 10 — Your Financial Plan Review

*Read the plan report end-to-end, walk it in the app, and set up your yearly re-read.*

## 11.1 Test a decision with a scenario
*`TEACH` · 1,150 words · ~7 min*

**By the end of this lesson, you can:**

- Tell a life event apart from a scenario, and put each one where it belongs
- Pick the right scenario type for the question you're actually asking
- Read a comparison without fooling yourself
- Know when a scenario should graduate into your actual plan

---

Your plan answers one question: if things go roughly the way you've assumed, here's where you land. A scenario answers a different one: **what happens if they don't?**

That's the whole job. You keep one baseline plan that represents your real life and your real intentions, and you keep a set of saved what-ifs beside it that you can compare against, one at a time, without disturbing the plan itself.

### Life event or scenario?

This is the distinction that decides where something goes, and the app enforces it.

- A **life event** is something you actually expect to happen. College tuition starting in eight years. A roof. A car. Retirement itself. Life events belong **in the plan**, because leaving them out makes your projection wrong.
- A **scenario** is something you're *considering*, or something you're *worried about*. Retiring three years earlier. Moving to a no-tax state. Bitcoin dropping 50% the year after you retire. Those belong **in Scenarios**, because putting them in the plan would corrupt the baseline you measure everything else against.

The test is one question: **am I telling the plan what's true, or am I asking it a question?** True things go in the plan. Questions go in Scenarios.

> ⚠ This is the single most common way people wreck their own baseline. They get curious about retiring at 55, change the retirement age in the plan itself, get distracted, and three months later they're reading a projection built on a decision they never actually made.

### The two kinds of what-if

Scenarios split cleanly into two groups, and they answer different questions.

**Stress tests** ask *would I survive this?* You're not planning for these. You're checking whether the plan holds if they happen anyway. Bear markets, a 50% drawdown right after you retire, weaker Bitcoin returns than you assumed. The only question you ask of a stress test is: **would I still be okay?**

**Choices** ask *should I do this?* These are decisions you might actually make. Retire earlier. Spend less. Move states. Claim Social Security at 62 instead of 70. Here you're comparing two futures and picking one.

Both are worth running. But notice the difference in what you do with the answer: a stress test you either survive or you go fix something. A choice you weigh, decide, and then either act on or drop.

### Choosing the scenario type

When you build a custom scenario, the app asks you what kind it is before it asks anything else. Seven types, and picking the right one just means you get shown the controls that matter and not the forty that don't:

| Type | What it covers |
|---|---|
| **Life events** | Income, spending, housing, family, and one-time events |
| **Retirement** | Timing, spending, income, and Social Security |
| **Savings** | Contribution amounts, routing, and future savings mix |
| **Debt** | Existing debts, new loans, and BTC borrowing |
| **Tax** | State, Social Security, dividends, and Roth conversions |
| **Markets** | Return assumptions and asset reallocations |
| **Advanced** | Every scenario control at once |

Start with the specific type that matches your question. **Advanced** exists for multi-part scenarios where you're changing several unrelated things at once, and it's the one to reach for last, not first.

### Change one thing at a time

This is the discipline that makes scenarios useful instead of confusing.

If you build a scenario that retires you three years earlier **and** cuts your spending **and** assumes weaker Bitcoin returns, and the result comes back worse, you've learned nothing. You can't tell which of the three did it, or whether two of them cancelled out.

One variable per scenario. If you want to know what three changes do together, that's a fourth scenario, built deliberately, and you read it *after* you understand each piece on its own.

### Reading the comparison honestly

When you select a saved scenario, the app puts it next to your plan and shows you a headline row first: **Retire at**, **Spending**, and **Success rate**. Below that, a full comparison table runs the rest, including net worth at retirement, lifetime taxes paid, effective tax rate, withdrawal rate at retirement, depletion age, and BTC at life expectancy.

Three rules for reading it.

**Read the pair, not the number.** A scenario that retires you two years earlier at a much lower success rate is a trade, and the trade is what you're reading.

**Run the Monte Carlo before you believe the success rate.** The comparison chart updates immediately, but the success rate is a simulation and it has to actually run. The button is right there in the comparison section.

**Small differences aren't differences.** These are projections built on assumptions. A scenario that lands 2% apart from your baseline is telling you the change didn't matter much. Don't reorganize your life around noise.

### When a scenario graduates

Sometimes a scenario stops being a question and becomes a decision. You've compared moving states three times, you're convinced, and you're doing it.

At that point it stops being a scenario. Go change the actual plan, and either delete the scenario or keep it as the record of the comparison that convinced you. What you don't do is leave a decision living in Scenarios, because your baseline is now wrong in a way you'll forget about.

The reverse also happens. You run a stress test, the plan survives, and there's nothing to do. That's a completed piece of work, not a failure. Save it and move on.

### Two scenarios worth keeping permanently

Most scenarios are disposable. Two aren't:

- **A deep drawdown right after retirement.** This is the sequence-of-returns test, and it's the single scenario most likely to break a Bitcoin-heavy plan. Keep it, and re-run it every year.
- **Weaker Bitcoin returns than you assumed.** If your plan only works at your optimistic growth curve, that's worth knowing every year, not once.

Both of those are also what populate the "if Bitcoin follows a different path" section of your yearly report.

### Homework

- Save one stress test: a deep drawdown right after your retirement year. Run the Monte Carlo on it.
- Save one choice you're genuinely weighing, built as a single-variable scenario.
- Answer the stress test out loud: would you still be okay? If no, build the lever you'd pull as its own scenario and see whether it actually fixes it.


## 11.2 Walkthrough: build and compare a scenario in Orange Plan
*`DEMO` · 1,250 words · ~9 min*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **11.2**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Create a scenario from a built-in what-if in one click
- Build a custom single-variable scenario end to end
- Read the comparison and run the Monte Carlo against your baseline
- Manage saved scenarios: duplicate, edit, delete

---

This walkthrough builds two scenarios: one stress test and one choice. By the end you'll have both saved, compared, and Monte Carlo'd.

Set aside about 15 minutes. Have your plan complete, because a scenario is only as meaningful as the baseline it's compared against.

### Pre-flight

⚠ **Your baseline needs to be real first.** Everything on this page is a comparison against your plan. If the plan still has stale balances or a spending number you don't believe, fix that before you run scenarios. You'd be comparing against fiction.

⚠ **The built-in what-ifs read your own settings.** The preset descriptions fill in your retirement age, your state, and your retirement spending. If those are wrong in the plan, the presets will offer you the wrong questions.

### Step 1: Orient on the page

**Scenarios** (primary nav). Page heading: **Scenarios**.

Three things live here, top to bottom:

- **What if...** — the built-in one-click presets.
- **Your scenarios** — everything you've saved. Sub-line: *"Saved what-ifs you can reopen and compare."* Empty state reads *"No custom scenarios yet."*
- The **comparison section** below, which stays empty until you select something: *"Choose a saved scenario to see the chart, key metrics, and Monte Carlo comparison."*

Top right: a **Custom scenario** button, and a **Review scenario** AI button that only appears once a scenario is selected.

### Step 2: Create the stress test in one click

**Scenarios → What if... → 50% drawdown after retirement.**

The card's description writes itself from your plan: *"BTC and stocks drop 50% the year after you retire at {your age}. The classic sequence-of-returns stress test."*

One click creates it and selects it under **Your scenarios**. The plan re-runs.

⚠ The grid shows the first four presets only. **See more scenarios** expands to all nine; **Show fewer scenarios** collapses it again. Bear Market and the 50% drawdown are always in the visible four.

The other eight, for reference: Bear Market, Retire earlier, Spend less in retirement, Move to no-tax state, Conservative BTC returns, Moderate BTC returns, Claim Social Security at 62, and Claim Social Security at 70.

### Step 3: Read the comparison

The comparison section now shows a chip with the scenario name, then **vs your plan**.

The headline row, three metrics:

| Metric | What it says |
|---|---|
| **Retire at** | The age this scenario produces |
| **Spending** | The spending it supports |
| **Success rate** | The confidence, once the simulation has run |

Expand **Full comparison metrics** for the rest: net worth at retirement, net worth at age 90, lifetime taxes paid, effective tax rate, withdrawal rate at retirement, depletion age, earliest retirement age, and BTC at retirement and at life expectancy. Each row shows baseline, scenario, and the difference, with **no change** rendered where they match.

⚠ Ask the stress test exactly one question: **would I still be okay?** Not "which line is prettier." You're checking survival, not optimizing.

### Step 4: Run the Monte Carlo

Button **Run Monte Carlo** in the comparison section. It shows a spinner with a phase label while it runs.

⚠ **Until this runs, the success rate isn't a real comparison.** The chart updates instantly off the projection, but confidence is a simulation and it has to execute. Run it before you draw any conclusion about risk.

### Step 5: Build a custom scenario

**Custom scenario** (top right) opens the **Create scenario** dialog.

**Step 1: Choose scenario type.** Seven cards. Pick the one matching your question:

Life events · Retirement · Savings · Debt · Tax · Markets · Advanced

⚠ Pick the specific type, not **Advanced**. Advanced shows every control at once, and it's for genuine multi-part scenarios. Starting there is how a simple question turns into a confusing scenario.

Then **Name** and **Description**. The name placeholder changes with the type you picked (choose Retirement and it suggests *"e.g., Retire at 55"*; choose Tax and it suggests *"e.g., Roth conversion window"*).

Name it after the question, not the answer. "Retire at 55" is a good name. "Better plan" is not.

Change **one variable**. Save.

### Step 6: Compare, then manage

Select the new scenario under **Your scenarios**. Read the same headline row, expand the full metrics, run the Monte Carlo.

The **⋯** menu on the comparison (aria label *"Scenario comparison actions"*) gives you three: **Duplicate**, **Edit**, **Delete**.

**Duplicate** is the one worth knowing. It's how you build a second scenario that differs from the first by exactly one thing, without rebuilding it from scratch.

⚠ Scenarios never touch your plan. Nothing here changes your baseline, which is exactly why you can experiment freely.

### Step 7: Run the AI review

**Review scenario** (top right, only renders when a scenario is selected and the editor is closed).

**It reads:** your saved scenarios, the projection years, your life events, and your assumptions.

**It asks:** *"Which saved scenario would you like to compare with your current plan?"*

Answer, let it run, then read one thing it surfaced and say whether you agree.

**When to run it:** when a comparison needs explaining in plain English before you hand it to someone else, or when you can't tell why two scenarios differ.

⚠ It explains and compares. It doesn't decide.

### What good looks like

- **Two scenarios saved**, one stress test and one choice.
- **Both Monte Carlo'd**, so the success rates are real numbers rather than placeholders.
- **The stress test answered out loud.** Would you still be okay, and if not, which lever?
- **Single-variable discipline.** You can say what one thing each scenario changed.
- **Your baseline is untouched.** The plan still reflects your real life.
- **Names that are questions**, so they still make sense a year from now.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | A saved sequence-risk stress test | Scenarios → What if... → 50% drawdown after retirement |
| 2 | A saved single-variable choice scenario | Scenarios → Custom scenario |
| 3 | Monte Carlo results on both | Scenarios → Run Monte Carlo |
| 4 | A read of the full comparison metrics | Scenarios → Full comparison metrics |
| 5 | (Optional) an AI explanation of the comparison | Scenarios → Review scenario |

### Handing it off

You now have saved scenarios, which is also a prerequisite for the report: the *"If Bitcoin follows a different path"* section only renders when at least one scenario exists.


## 11.3 How to read a financial plan
*`TEACH` · 1,085 words · ~8 min*

> 🐞 Currency mangling in the band example (item 17): "$80K spending sits in a
> band with a floor of ~$72K and ceiling of ~$88K."

**By the end of this lesson, you can:**

- Read a plan report in question order: position, trajectory, risk, actions
- Catch the six red flags in the first two minutes
- Save one PDF per year and compare year-over-year
- Hand the report to spouse, CPA, and attorney as the annual agenda

---

A plan report is read in the order that answers four questions:

1. **Where do you stand today?** (position)
2. **Where are you headed?** (trajectory)
3. **What could break it?** (risk)
4. **What do we do about it?** (actions)

Every number in your report belongs to one of those four.

Each question depends on the one before it. Trajectory is computed off position. Risk is your trajectory tested against assumptions you didn't pick. Actions come out of what the risk read found. Starting in the middle means trusting numbers you never checked.

### 1. Position

The honest snapshot today. Net worth, what's in Bitcoin vs everything else, what you owe.

For the couple: $30,000 cash, 300 shares of the index fund, Bitcoin across both wallets, $298,000 of debt underneath.

No judgment yet at this layer. This is just confirming the picture is true today. Position is where stale data gets caught, and reading it first stops a single wrong account from corrupting every number downstream. If you moved that quarter BTC to cold storage last month, does the report know?

### 2. Trajectory

Date and confidence get read together.

- **Earliest-retirement date** tells you *when*.
- **Confidence number** tells you *how sturdy that is*. The share of simulated futures where the plan funds your spending all the way through.

Age 60 at 82% confidence is a real answer. Age 57 at 55% confidence would be a prettier date and a worse plan.

A date on its own can always be moved earlier by assuming better returns. The confidence number surfaces the cost of that assumption.

### 3. Risk

The "what if I'm wrong" sections: different Bitcoin paths, the **spending band**, protection lines.

**The band.** Spending isn't one number in a real plan. The **floor** is what the plan asks you to live on in a bad stretch. The **ceiling** is what it lets you spend when things go well.

Ask one question of every risk section: *would I still be okay in this scenario?* For our couple, $80K spending sits in a band with a floor of ~$72K and ceiling of ~$88K. The risk read is one sentence: on the Bitcoin path they did not pick, does the plan still hold at $72K? If yes, they're okay.

### 4. Actions

Shortest section. This is where the review changes anything.

The rule from the maintenance module applies: one to three finishable actions and nothing more. For our couple: finish the cold storage move, top up the reserve, take one conversion question to the CPA. All three finishable before the next monthly pass.

### The six red flags. First two minutes

1. **A position section that doesn't match reality.** Stale balances make every number after it wrong.
2. **A date you like at a confidence you don't.** A plan that only works if you get lucky.
3. **A spending number with no band around it.** A single number gives you nothing to fall back to in a bad year.
4. **A Bitcoin-path section you've never actually looked at.** That section is what tells you what happens when your main assumption is wrong.
5. **A next-steps list longer than three items.** Long lists rarely get finished.
6. **An assumptions section you couldn't defend out loud.** Every number in the document rests on it.

If you find any of these, the review isn't finished yet.

### The standard

The standard for this module: you can answer all four questions out loud, in four sentences, about your own report.

### Save one PDF per year

Right after your annual review, while the data is fresh:

1. One PDF per year, saved with the year in the filename.
2. Save it somewhere it will still exist in ten years.

The document does its real work the second time you save one, when there are two of them side by side.

### The year-over-year re-read

A price change by itself can't tell you whether the plan got better. Take a rally year: Bitcoin worth $200K more. Feels great. But spending drifted from $80K to $88K and nobody entered it, the reserve never got topped back up, and the tax question never got asked. A rally moves one number and shows you none of that.

In 2022 Austin's net worth dropped 75%. On price alone, a catastrophe. But income hadn't changed, spending hadn't changed, the date barely moved. A report from that year would have shown him all three in a couple of minutes.

With two reports side by side, four lines to look at, in order:

1. **Net worth, and the Bitcoin share.** If the share went up while you made only small buys, price is the reason (drift you didn't choose). If the share went up because you bought more, it's a decision you made.
2. **Date + confidence, as a pair.** The same date at higher confidence is real improvement. An earlier date at lower confidence means an assumption moved, not the plan.
3. **Spending band, especially the floor.** The floor is the honest read, because it's the number you're stuck with in a bad stretch. A rising floor tells you the plan got stronger. A rising ceiling on its own doesn't.
4. **Last year's action list.** Did each one happen? Anything unfinished rolls forward.

### Three handoffs. You're not the only reader

- **Spouse sit-down.** The report is your agenda: where you stand today, the date, the band. Done in twenty minutes.
- **CPA** gets the tax pages plus the transaction export, so they can price a conversion or a harvest instead of reconstructing your year from statements.
- **Estate attorney** gets the access and estate pages plus your decisions, so the drafting conversation starts from what you already decided.

You're handing each professional a document, not asking them to log into an app. That lets three different professionals start from the same set of facts.

### The whole point

You started this course with accounts scattered everywhere and a rough guess. You're finishing with a document your family can read, your CPA can act on, and next-year-you can be measured against.

A financial plan is what that finished document represents.

## 11.4 Walkthrough: walk your report in Orange Plan
*`DEMO` · 1,572 words · ~7 min*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **11.4**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Walk your own report end-to-end
- Save the PDF for the annual review

---
Companion walkthrough for Module 10. This is the ~8-minute lap that reads the yearly report in **planner order. position, trajectory, risk, actions ** and saves the PDF. The report has eleven sections. You'll read them in a different order than the page renders them, and you'll say so on camera.

Set aside about 20 minutes to run it slowly the first time. Have the plan warm right after a monthly pass, at least one saved scenario, and a fresh confidence check already run. The report has three conditional sections that don't render without them.

The core habit is one PDF per year: the report is the "after" picture of this year and the "before" picture of next year.

### Pre-flight

⚠ **The reading order is not the same as the page order.** The report leads with trajectory; position is section **five**. Read the walkthrough below in planner order (position → trajectory → risk → actions) and jump around the page deliberately.

**Three sections are conditional.** Load them before you record, or the walkthrough will have gaps:

| Section | Renders when |
|---|---|
| **"If Bitcoin follows a different path"** | at least one saved scenario exists |
| **"Your next steps"** | steps exist (or coach mode is on) |
| **"What these terms mean"** | a glossary is present |

⚠ **The spending band renders only when explicit bands exist.** Otherwise the section reads *"Run a fresh confidence check to add the explicit probability spending bands."* Run the confidence check first, then generate the report.

The retirement-era demo household the scripts use: $80,000 spending, $120,000 reserve, $400K taxable BTC, $600K traditional, $200K Roth, and $51,600/yr Social Security. The report reads best on a plan with real numbers in every section.

### Step 1: Open the report + name the reading order

**Account menu (hamburger, far right, aria "Account menu") → "Report."**

Header shows the **"{Prepared for}"** eyebrow, the report title, and **"Download PDF"** top-right.

Say the frame on camera:

> "Nine modules assembled into one document. We're going to read it the way a planner reads it: **position, trajectory, risk, actions.** The page isn't in that order. The report leads with trajectory, and position is section five. So we're going to jump."

⚠ **The button is "Download PDF," not "Print."** It does fire the browser print dialog underneath, but the label on screen is "Download PDF."

### Step 2: "Are you on track". TRAJECTORY

**Section 1.**

The confidence ring, sub-label **"confidence,"** beside the age stat and the earliest line.

Read the date and the ring together. The date is the when, and the ring is how sturdy that date is under real market variation.

- **Green at 80+** is the healthy zone.
- A confidence of 100 was never the goal. A plan that only survives at 99% confidence is one built on optimism.

If you like both the ring and the date, that's the healthy read. If one is fine and the other isn't, the disagreement between them is where the signal lives.

### Step 3: "Where you stand today". POSITION (jump to section 5)

**Scroll to section 5**. Out of order, deliberately.

**"Net worth"** + the quarter delta + the allocation donut. Ledger groups below.

The first question of the whole read is: is this true?

⚠ **A review of wrong numbers is worthless.** If any balance looks stale, stop the read, fix it at the source (Dashboard or the linked institution), and regenerate the report. Don't try to "read around" a wrong number. The whole document is built on it.

### Step 4: "What you can spend" + "How retirement gets funded"

**Sections 3 and 4.**

The big number, then the band with three sub-labels:

- **"Lean decade"**
- **"Your plan"**
- **"Strong decade"**

Funding stages + legend below.

Your spending in the report is a band, not a single number. The floor is what you can fall back to. The ceiling is your permission to spend more when things go well. The middle is what you actually spend.

⚠ **"floor / plan / ceiling" are not the on-screen words.** Those are the concept names the course uses. The screen renders **"Lean decade / Your plan / Strong decade."** If your viewer heard the concept names in an earlier lesson, name both. Say "the band the app calls Lean decade is the floor we've been talking about."

### Step 5: "How your plan plays out" + "If Bitcoin follows a different path". RISK

**Section 2, then the conditional scenarios section (usually section 9).**

Year-by-year area chart with retirement and RMD markers.

Scenario section: delta bars captioned **"Safe annual spending. Baseline highlighted,"** then the scenario matrix.

Ask **one question** of it: *"Would I still be okay?"*

Not "which line looks prettiest" or "which scenario should I bet on." The scenarios exist to test whether the plan survives at all.

⚠ **If no scenarios are saved, the "different path" section is absent from the report.** That's why the pre-flight said to save at least one.

### Step 6: "Tax roadmap" + "Allocation"

**Sections 8 and 6.**

Tax roadmap timeline + its copy.

Allocation drift bars; and if a BTC loan exists, the card **"BTC-backed loan"** with a gauge labelled **"Liquidation risk" / "Cushion."**

Say: bring this page to your CPA. It plus Module 3's buckets, graded, is what turns a tax conversation from a guessing game into a document read.

⚠ **"Cushion" as a word appears here, on the report gauge. It does not exist on the Strategy → Debt page.** If a viewer heard "cushion" during Module 9's annual lap, this label is what they'll see when they open the report. Match your language to it.

### Step 7: "Protecting what you've built"

**Section 7.**

The readiness segment bar (the "{n} of 5 essentials" from Protect), then two ledgers:

- **"Estate"**
- **"Insurance and access"**

Say: this section is the scoreboard for Modules 7 and 8. Could your family act on this today?

⚠ **"Insurance and access" does not track policies.** Its rows come from the Beneficiaries / Executor checklist items. Protect still marks insurance **"Coming soon."** If your viewer expects to see policy detail here, they'll be confused. Name that limitation on camera once.

### Step 8: "Your next steps" + "Assumptions & methodology". ACTIONS

**Sections 10 and 11.**

Numbered steps, two digits each.

Assumptions render as a label/value grid.

Footer: **"Prepared with Orange Plan."**

Two lines to say out loud:

- **Three actions, not thirty.** A longer list is how a review stops happening.
- **If you can't defend an assumption out loud, change it and regenerate the report.** A number in the assumptions grid you can't explain is a number you don't own.

### Step 9: AI · "Review scenario"

**Scenarios → select a saved scenario → button "Review scenario."**

**It reads:** your saved scenarios, the projection years, your life events, and your assumptions.

**It asks:** *"Which saved scenario would you like to compare with your current plan?"*

Click, then let the answer arrive. Read one line it surfaced and say whether you agree.

**When to run it:** when a scenario in the report's Bitcoin-path section needs explaining in plain English before you hand the document to someone (a spouse, a CPA, an adult child).

⚠ It explains and compares. It doesn't decide.

⚠ **The button only renders when a scenario is selected and the editor is closed.** Select a scenario first, or the button won't appear.

### Step 10: Save the artifact

**Back on Report → "Download PDF."**

Save with the year in the filename. E.g. `orangeplan-report-2027.pdf`.

Say the close: this is your "after" picture for this year and your "before" picture for next year. One report saved per year, for as long as you have a plan.

### What good looks like

- **Position matches reality.** No stale balances. The read itself is the audit.
- **Date and ring get read as a pair.** A date the viewer likes at a confidence they trust. If not, they can name the lever: the operating plan from Module 6, or a scenario.
- **A band, not a single point.** All three labels are present and explainable. If you got the "Run a fresh confidence check" line instead, stop and run it.
- **The Bitcoin-path section actually read**, with "would I still be okay?" answered out loud.
- **Protection lines are green**, or the owning module has been named for a rewatch.
- **Next steps ≤ 3**, and every assumption defensible.
- **The PDF exists on disk with the year in the filename** before you close the session.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | The report, generated from current data | Account menu → "Report" |
| 2 | The saved yearly PDF | Report → "Download PDF" |
| 3 | Fixes for anything the read caught | The owning page. Dashboard, Plan, Protect |
| 4 | AI-explained scenario (optional) | Scenarios → saved scenario → "Review scenario" |
| 5 | The share plan | Recorded decision (spouse, CPA with the 8949, attorney) |

### Handing it off

That's the read. The habit of saving one report per year, with the year in the filename, is what turns a plan into a track record. Five years of "before" pictures let you see what actually moved and what only felt like it did.
