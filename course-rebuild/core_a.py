CORE = {
    "0.2": {
        "title": "How to use Orange Plan AI",
        "source": "Austin direction from 2026-08-25; current-app behavior verified for the filming rebuild",
        "body": r"""
In today's lesson, I'm going to show you how I would actually use the AI inside Orange Plan while you're building and maintaining your financial plan.

I don't think the best use of it is opening a blank chat and asking a generic question like, "What should I do with my money?" The useful part is that the AI can look at the section of the plan you're already working on, read the numbers the app calculated, and help you understand what those numbers mean or what you may be missing.

The orange AI Review button opens the Plan Guide. You can open it from anywhere in the app, and the first set of options changes depending on the page you're on.

If you're on Cash Flow, it can help you check whether the income, spending, and surplus look believable. On Debt, it can review which loans are creating the most pressure or risk. On Allocation, it can look at your current holdings, your target, and the timeframes those accounts need to fund. On Tax, it can help you spot a conversion or harvesting question that is worth modeling before you take it to your CPA. On Retirement Income, it can help explain what is driving the date, the confidence result, or the amount the portfolio needs to provide.

The app is still doing the calculations. The AI is there to help you read the output, question it, and think through the decision. I would use it more like a second set of eyes than somebody making the decision for you.

A few prompts I think are useful throughout the course are:

- What changed after the numbers I just updated?
- Which three inputs are affecting this result the most?
- What information looks missing, stale, or inconsistent?
- What am I not thinking about before I make this decision?
- Compare these two choices and explain the trade-offs in plain language.
- What should I model before I take this question to my CPA, attorney, or insurance professional?

That last one is important. The AI can help you show up to a professional conversation with the right numbers and a much better question. It should not pretend to replace the person who has to apply current tax law, read an insurance contract, or draft a legal document for your state.

There is also a daily Bitcoin market report inside the Plan Guide. I use this as a quick way to understand what is happening without checking a bunch of different sites.

🎬 VISUAL — Open the daily Bitcoin report and scroll slowly through the sections.

It gives you the current price and recent price changes, how far Bitcoin is from its prior high, ETF and public-company activity when it matters, leverage and futures data when those are relevant, the most useful on-chain change, and the larger macro or industry news that could actually matter. It should also separate information that sounds important from information that would genuinely change the planning read.

The report is not a trading signal. The more useful question at the end is whether anything that happened today changes what you need to do in the plan. Most days, it should not. Staying informed and changing your strategy are two different things.

The AI becomes more valuable as the plan gets more complete. After you replace the onboarding estimates with your real holdings, ask what changed. After you enter the real spending number, ask whether anything else in the plan now looks inconsistent. After you add debts, ask what could create a forced sale in a Bitcoin drawdown. After you set a target allocation, ask whether your reserve, Bridge funding, and custody can support it.

It is also good at finding unfinished work. It may notice an account with no holdings, a debt with an old rate, a life event that is missing from the future cash flow, cost basis that still needs to be reconstructed, or a preview that was never applied to the baseline plan.

You can use another AI too. In Settings under Data and Privacy, Orange Plan has an AI Strategy Review Export. That file is designed to give ChatGPT, Claude, or another AI a useful summary of the plan without including the personal information it does not need. Review the export before you upload it, then ask the same kinds of questions you would ask inside the app.

That export is not the same thing as your encrypted backup. The encrypted backup exists to restore the plan and should never be uploaded to an AI tool.

And there is one rule that applies to every AI, every export, and every part of this course: never enter a seed phrase, private key, wallet backup, passphrase, PIN, password, Social Security number, full account number, or backup-file password into an AI chat. The AI does not need any of those things to help with the plan.

Before moving on, open the Plan Guide once from the page you're currently on. Run one review using your own numbers, open the daily Bitcoin report so you know where it lives, and locate the AI Strategy Review Export in Settings. After that, use the AI when you need help understanding the decision in front of you, not as another thing you have to check every day.
""",
    },
    "1.3": {
        "title": "What the onboarding retirement age actually means",
        "source": "Foundation deck flow; Orange Plan main deterministic onboarding verified at 8ed57cbde2bf051c990ec5d1dcbf1178e98fa8d8",
        "body": r"""
In today's lesson, we're going to cover the retirement age you saw at the end of onboarding, what that number actually means, and why it is only the starting point for the plan.

Onboarding only asked you for a small amount of information. It used your age, income, spending, rough account values, Bitcoin holdings, and the growth model you selected to give you a first estimate.

That is useful because you can get a direction without spending an hour entering every account and every detail before you see anything. But the number can look more complete than it really is, so I want to explain exactly what the app is doing.

The onboarding age comes from one set of assumptions. Orange Plan projects those assumptions forward at different retirement ages and finds the earliest age where that version of the plan lasts through the life-expectancy setting.

There are not 1,000 different market paths being averaged together during onboarding. It is one deterministic projection using the rough numbers and the growth model you selected.

So I would think about the onboarding age as a first estimate of what might be possible if those inputs are reasonably close. It is not your finished retirement date, and it is not a promise that the plan is going to work exactly that way.

The reason it is still helpful is that it gives you something concrete to work from. It also shows you how much the growth assumption can move the result. A more conservative Bitcoin model will usually move the age later. A more aggressive model will usually move it earlier.

But the growth model is only one part of the final answer.

The onboarding estimate does not yet have every real account and holding. It does not know all of your debts, expected future expenses, retirement income, Social Security, cost basis, withdrawal order, or tax strategy. Those are the parts we're going to build through the course.

That is why the next step is not to keep changing the growth model until you get the age you want. The next step is to replace the rough estimate with the information that is actually true.

Foundation is going to replace the rough account values with your real accounts and current holdings. Cash Flow is going to verify your income, spending, usable surplus, reserve, and expected life events. Debt is going to add the real loan terms and the decision attached to each debt. Allocation is going to decide what your new dollars are for, which account they go into, and what they buy. The later modules build the tax strategy and retirement paycheck.

Once the full plan is built, Orange Plan can run it through 1,000 different market paths. That is where the confidence result comes from.

The onboarding estimate and the confidence check answer different questions.

The onboarding estimate asks: using this one set of assumptions, what is the earliest age where the projection lasts?

The confidence check asks: when the full plan is run through 1,000 different market paths, how often does it still work as written?

That second question becomes much more useful after the information underneath it is complete. A precise confidence percentage based on rough onboarding data would look more trustworthy than it really is.

As you enter the real data, the age may move earlier or later. That is not the app changing its mind. It means the model is using better information.

After the plan is built, you will also choose the confidence target the retirement date has to meet. The finished earliest date is the first date that clears that target, not just the first date where the single deterministic projection works.

The main thing I want you to take away from this lesson is that onboarding gave you a useful place to start. It did not finish the plan for you.

In the Foundation walkthrough below this lesson, I'll show you how to replace the rough account estimates with your real accounts and holdings, verify the personal details behind the plan, and review the assumptions onboarding used. We are not going to enter every part of the financial plan in that walkthrough. Each later module enters the information it owns.
""",
    },
    "2.1": {
        "title": "Find the surplus your plan can actually use",
        "source": "Cash Flow + Reserve deck and Module 2 detailed outline, updated for current Cash Flow page",
        "body": r"""
In today's lesson, we're going to figure out the amount of money your plan can actually put to work every month.

I think this is where a financial plan becomes real. You can have a strong opinion about Bitcoin, taxes, retirement accounts, or borrowing, but none of those decisions can use more money than your cash flow produces.

Bitcoin may be the asset that builds the wealth, but the surplus is the engine underneath it. It is what lets you keep buying through a drawdown, build a reserve, pay extra on a debt when that makes sense, and avoid getting forced to sell at the exact time you do not want to.

🎬 VISUAL — Cash Flow by Stage from the Week 2 deck: Working → Approaching → Retired.

Cash flow also changes jobs as your life changes.

While you're working, income is usually higher than spending. The surplus fills the reserve and funds investments.

As you approach retirement, the job starts to change. You may still have income, but you are also pre-funding the cash and accessible money that will cover the first years without a paycheck.

Once you're retired, there may not be a surplus at all. There is a gap between what you spend and what comes in from Social Security, a pension, or other reliable income. The reserve gets drawn down and refilled from the portfolio instead of being filled from a paycheck.

For this module, we're starting with the working version: what comes in, what goes out, and what is honestly left.

The first thing I would do is list every income stream separately. That means each paycheck, self-employment income, rental income, recurring interest or dividends if you actually rely on them, and any tax-free income. I would also note how stable each one is. Two households can earn the same amount and need very different reserves if one has two stable salaries and the other has one variable business income.

Then we need the spending number. This is one of the easiest inputs to get wrong.

Your spending is not your gross income. It is not the amount hitting the bank before taxes. And in Orange Plan, minimum debt payments are entered separately, so you do not want to count the same payment again inside living expenses.

What we want here is what your household normally spends on the actual life you live: housing, food, utilities, insurance, travel, subscriptions, and the rest of the day-to-day categories.

I would use two or three real months if you have them. A rough number from memory is fine as a starting point, but transaction history is where you find the expenses you forgot and the months that were not normal.

From there, I like to go through the spending with three labels: Keep, Cut, and Reduce.

Keep is anything essential or clearly worth what it costs. The goal is not to make your life miserable just to make a projection prettier.

Cut means it is not worth paying for at all. Unused subscriptions, recurring charges you forgot, or spending that is not buying much happiness or utility.

Reduce means you keep it but lower the ongoing cost. Insurance, phone plans, internet, memberships, or another recurring bill you have not compared in years.

The best changes are usually boring and repeat every month. Saving forty dollars on a bill with one phone call is more useful than relying on willpower every week.

And after the easy items, the biggest levers are usually housing, vehicles, and location. Those are harder changes, but they move the surplus much more than finding another three-dollar subscription.

🎬 VISUAL — Keep / Cut / Reduce cards, followed by the housing / car / location appendix slide.

There is one more number you need besides normal spending: your bare-bones spending.

That is not the amount you want to live on. It is the minimum amount the household could run on during a job loss, a business slowdown, or a major Bitcoin drawdown. Housing, food, utilities, insurance, healthcare, minimum debt payments, and the other expenses that do not disappear just because the month is bad.

Normal spending tells the plan what your life costs. Bare-bones spending tells you how much cash it takes to buy time in an emergency. The next lesson uses that second number to size the reserve.

Now we can calculate the usable surplus:

Income, minus taxes, minus living expenses, minus required debt payments.

What is left is the pool the plan has available for the reserve, extra debt, and contributions.

I would not count a retirement contribution as an expense in this calculation. A contribution is a decision about where the surplus goes. We are going to make that decision in the Allocation and Next-Dollar module.

The last part is choosing a surplus you can actually rely on. The mathematical average may say you have four thousand dollars left, but if every third month has a large irregular bill, routing all four thousand is going to create stress and reversals.

I would rather start with a slightly lower number that can move automatically every month than a larger number you constantly pull back.

Check the timing too. If all of the bills clear before the second paycheck, the month can feel tight even when the annual math works. Moving due dates or scheduling transfers after bills clear can make the same surplus much easier to maintain.

And check withholding. A large refund can mean part of your surplus was trapped in payroll all year. Owing a surprise tax bill can mean the apparent surplus was never yours. The goal is not a perfect refund. It is making sure the monthly number is honest.

Once the surplus is reliable, it creates a flywheel. You improve cash flow, route the money into the plan, build more assets and flexibility, and that flexibility can create a larger surplus later. What breaks the flywheel is lifestyle creep, panic-selling, or trying to speed it up with leverage before the foundation is ready.

In the walkthrough for this module, I'll show you where income and living expenses go, how to compare the plan to real transactions, and how to read the surplus Orange Plan calculates. Then we'll use your bare-bones number and reserve decision from the next lesson to build the first part of the routing plan.
""",
    },
    "2.3": {
        "title": "Add the future changes your plan should expect",
        "source": "Foundation and Cash Flow decks; Austin clarification that this lesson is life-event planning, not a universal funding-lane doctrine",
        "body": r"""
In today's lesson, we're going to cover the future changes that should already be part of your baseline plan.

Your current income and spending are only the starting point. Real life is not going to stay flat for the next thirty or forty years. A child may start college, you may replace a car, sell a house, change jobs, help a parent, receive an inheritance, or spend more in the first few years of retirement than you do later.

If a change is likely enough that you are genuinely planning around it, I want it in the baseline as a life event.

If it is only a question you want to explore, I want it in Scenarios.

That is the same distinction from Foundation. "We expect to replace the roof in five years" is a life event. "What if we bought a second house?" is a scenario unless that decision has actually been made.

The reason life events matter is that they change the future cash flow in the year they happen. A large expense increases what the plan has to fund. A job change may lower or raise income. Selling a house may remove one asset, add cash, and change spending. A recurring college event may affect several years in a row.

You do not need perfect information to add one. Use the best amount and date you can reasonably defend today, then update it as the event gets closer.

I would start by making a list in four groups:

- future income changes, such as a planned job change, reduced hours, business income ending, or a pension beginning;
- large purchases, such as a vehicle, roof, home renovation, or house move;
- family commitments, such as college, support for parents, a wedding, or a gift;
- retirement changes, including healthcare before Medicare, higher travel spending early, or long-term care later.

🎬 VISUAL — Foundation life-events slide: retirement target, college, income changes, home purchase or sale, large expenses, legacy or family support.

For each one, ask four practical questions.

First, how confident are you that it is happening? If the answer is low, it probably belongs in Scenarios.

Second, when is it likely to happen? A range is fine if the exact year is not known yet.

Third, what amount are you actually committing the plan to fund? That can be different from the maximum possible cost.

Fourth, where might the money come from? Current cash flow, existing cash, taxable investments, Bitcoin, a dedicated account, financing, or a combination.

That fourth question does not mean we are deciding the debt strategy in this lesson. It simply keeps us from acting as if every future purchase must be fully saved in cash today. The Debt module decides whether financing improves or weakens the plan. The Allocation module decides how new dollars are invested and which money needs to stay accessible.

The timing still matters, but I do not want to turn it into a rigid rule that says every expense at a certain year must use a certain asset.

If the bill is coming in the next year or two and the amount is non-negotiable, it should not depend on Bitcoin being at a favorable price when the bill arrives.

If the event is more than five years away, Bitcoin can remain part of the funding plan. I would not automatically move the entire future expense into cash at year five. The part you have firmly promised should become less dependent on Bitcoin as the date gets closer. The flexible portion can stay invested longer.

That is the useful principle: the closer the event gets, the more certain the required funding needs to become. The exact path depends on the flexibility of the amount, the date, and the rest of your plan.

College is the clearest example, so it gets the next optional lesson. The amount you help with, whether you use Bitcoin or a 529, what can come from cash flow while the student is enrolled, and whether the student uses work or a limited amount of loans are separate decisions. A sticker price is not a funding plan.

In the module walkthrough, I'll show you how to add an expected income or expense event, choose whether it repeats, and see how it changes the future projection. We'll also keep the funding decision separate from the event itself: the life event tells Orange Plan what the future costs; Cash Flow, Debt, and Allocation determine how you prepare for it.
""",
    },
    "2.4": {
        "title": "Optional: decide how much college help you are actually funding",
        "source": "Austin college-planning direction, current Education target behavior, and the optional college material from the old deck",
        "body": r"""
This lesson is optional. It is for you if you have children, grandchildren, or another education goal you expect to help pay for. If that does not apply, skip it and go straight to the module walkthrough.

The first college-planning question is not which account to open.

It is how much you are actually committing to help with.

That may be four years of in-state tuition. It may be tuition only, a fixed dollar amount per child, a percentage of the final net cost, or whatever a specific savings account plus a set amount of cash flow can support.

I think parents get into trouble when they start with the largest possible sticker price and treat the whole number as their obligation before deciding what they are actually promising.

The published cost, the net cost after aid, and the amount the parents choose to provide can all be different numbers.

So I would build the decision in this order.

First, choose the commitment. What do you want your child to be able to count on from you?

Second, estimate the likely cost of that commitment. Use the type of school you are realistically planning for today, current tuition and living costs, and a reasonable inflation assumption. This is an estimate that gets updated, not a contract with a school that has not been chosen yet.

Third, list every funding source.

That can include existing 529 money, new 529 contributions, Bitcoin or other taxable investments, cash flow while the student is enrolled, grants and scholarships, student work, family gifts, and a bounded amount of student borrowing.

🎬 VISUAL — Build the college funding stack from the bottom up: parent commitment, then sources. Do not show sticker price as the automatic parent target.

A lot of conventional college planning starts with the 529. I do not think that should be automatic for a Bitcoiner.

A 529 can give you tax advantages when the money is used for qualified education expenses. It also limits the investment menu, has rules around how the money is used, and may not give you the Bitcoin exposure you actually want.

Bitcoin gives you more flexibility and, in my view, a stronger long-term growth asset. It also brings volatility, no education-specific tax shelter, and the risk that the price is down when tuition is due.

For my own planning, if college is still more than five years away, I am comfortable using Bitcoin as a meaningful part of the savings plan instead of assuming every dollar has to go into a 529. That does not mean I would wait until freshman year and hope the price cooperates.

As the date gets closer, I would revisit the commitment, the likely school cost, the aid picture, and the amount already available. Then I would start protecting the portion I have firmly promised.

In the final year or two, the first year of the commitment should have a reliable source. That source could be 529 money, cash, current income, a sale made during a stronger market, or a combination. Later years can remain more flexible and get recalculated after the actual aid package is known.

Current cash flow while the student is enrolled is easy to overlook. A family may not need the full four-year commitment sitting in an account before college starts if part of each year's bill can be paid from the income they are still earning.

The student can participate too. Work, scholarships, grants, and a reasonable amount of federal student loans can all be part of the plan. I would separate bounded student borrowing from unlimited parent or private borrowing. A manageable loan that gives the student ownership is a very different decision from putting the parents' retirement plan at risk.

You may have heard the one-third idea: roughly one-third saved beforehand, one-third paid from current cash flow or investments while the student is enrolled, and one-third handled through aid, student work, or loans.

I think that can be a useful starting framework because it reminds you there are several funding sources. I would not treat it as a rule. One family may want to cover the entire commitment. Another may have a strong retirement plan but limited current savings. Another may have a child choosing a much less expensive path.

The plan should reflect the decision you actually made, not a generic percentage.

Orange Plan can help with the numbers. The college life event establishes the amount and the years the plan is expected to fund. The Education section can show the education target, what is already in education accounts, the remaining gap, and how the current plan is projected to cover it. It does not decide the family commitment for you, and education contributions stay separate from the broader Reserve, Bridge, and Legacy savings target.

After you choose the commitment, compare it with what is already saved and what the current projection may provide. The remaining amount is the part that needs a funding decision. Some of it may become a monthly 529 contribution. Some may remain part of the Bitcoin plan. Some may be paid from future income.

In the walkthrough, I'll show you how to add the college event, connect the years and amount to the plan, read the Education target and gap, and add a 529 contribution if that is part of your decision. The important thing before the clicks is that you can say, in one sentence, how much you are helping with and which sources are expected to pay for it.
""",
    },
}
