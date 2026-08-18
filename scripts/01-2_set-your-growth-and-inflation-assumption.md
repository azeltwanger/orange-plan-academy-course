TELEPROMPTER SCRIPT — segment 1.2
1.2 The three layers of a plan, and setting your assumptions
~11 min at 155 wpm · VOICE-MATCHED DRAFT — Austin review pending
============================================================

So in this lesson we're going to separate what is true today, what you actually expect to happen, and the questions you only want to test.

Then we're going to set the assumptions the plan uses to project everything forward.

These two ideas solve a lot of the confusion that comes up when people first start using planning software, because if you do not know whether something belongs in the real plan or in a what-if, it is easy to change the wrong thing and then not understand where the result came from.

== BASELINE, LIFE EVENT, OR SCENARIO ==

The first type of information is your baseline.

Your baseline is what is true today.

Your household earns $190,000. You own 1.75 Bitcoin. Your mortgage balance is $280,000. Your living spending is around $80,000 a year outside of debt payments.

Those are the starting facts. They are not goals, and they are not guesses about what might happen later.

The second type is a life event.

A life event is a change that you genuinely expect the plan to include.

Maybe daycare ends in 2 years. Maybe one spouse plans to stop working when a child is born. Maybe you know you are going to replace a car in 5 years, help with college, move, or make a large gift to family.

You may not know the exact date or amount yet. But if you would be surprised if the event never happened at all, I would generally include it in the saved plan and use the best estimate you have today.

The third type is a scenario.

A scenario is a question.

What if I retire 3 years earlier?

What if Bitcoin returns are lower than I expect?

What if we move to another state?

What if retirement spending is $20,000 higher?

Those can all be useful questions. But they should stay separate from the baseline until you actually make a decision.

Let's use our demo household.

Their current income is baseline data.

The vehicle replacement they expect in 5 years is a life event.

Retiring at 52 instead of the age they have currently planned is a scenario.

If they put every question into the baseline, then they lose the plan they were supposed to compare the question against.

So the way I think about it is:

Facts go into the baseline.

Expected changes go into life events.

Questions stay in Scenarios.

== WHERE ASSUMPTIONS FIT ==

Assumptions are the rules the model uses to move the plan into the future.

The Bitcoin return model is an assumption. Stock, bond, real-estate, and cash returns are assumptions. Inflation is an assumption. Life expectancy is an assumption.

A life event might say that the household spends $30,000 on a vehicle in 5 years. Inflation tells the app how the cost of their regular life changes before and after that year.

The baseline might say they own 1.75 Bitcoin today. The Bitcoin return model tells the app how that holding changes through the projection and the 1,000 test runs.

So an assumption is not a prediction that has to come true exactly. It is the starting rule the saved plan is using.

== SET A BASE VIEW YOU CAN EXPLAIN ==

When I work through this with someone, I want the assumptions to be realistic enough that they are comfortable making decisions from the result.

I do not think the goal is to choose the set of numbers that gives you the earliest retirement date.

Let's say our demo household uses a very high flat Bitcoin return for the entire plan. The retirement date is going to move much closer because Bitcoin is a large part of their assets.

If we switch to a return that declines as Bitcoin gets larger, the date is probably going to move later.

Nothing about their life changed. We only changed the rule the projection was using.

That is why assumptions can move the result more than almost anything else in the app.

Orange Plan has built-in Bitcoin views, including a power-law option, and the Bitcoin return views decline over time.

I think a declining shape makes more sense for long-term planning because it is going to take more capital to keep growing at the same percentage rate as Bitcoin gets larger.

Power law is what I use in my own planning until I have a reason to change it. That is still my assumption. It is not a promise about what Bitcoin is going to do, and I would still test a weaker return in Scenarios.

== INFLATION ==

Inflation works in the other direction because it increases the amount the plan has to fund.

If the household spends $80,000 today, 3% inflation takes that same lifestyle to roughly $125,000 in 15 years. At 4%, it is closer to $144,000.

That 1% difference looks small in the settings, but it is adding to the spending need every year through retirement.

I run inflation higher in my own plan because I would rather have the model overstate future costs than understate them.

That is my judgment. You do not have to use the same number. The number needs to be something you can explain and something you are comfortable planning around.

== BROAD ASSUMPTIONS AND HOLDING OVERRIDES ==

The Plan assumptions are broad defaults for the different asset classes.

That is the right place to start because most stock holdings can use the stock assumption, most cash can use the cash assumption, and spot Bitcoin can use the Bitcoin assumption.

But sometimes one holding does not behave like the rest of the category it is sitting in.

This came up with a client who held FBTC. It was listed as an ETF, so it was being treated like a stock even though the exposure was Bitcoin. The right return assumption for that holding was the same Bitcoin assumption we were using for spot Bitcoin.

You can also have a preferred security that is mainly held for income, a rental property with its own appreciation and rental yield, a money-market holding with a specific yield, or a concentrated stock that you do not want modeled like the broad market.

When that happens, set the assumption on the holding itself instead of changing the return for every asset in the category.

The holding editor can use a fixed return, the Plan's Bitcoin assumptions, a declining return, or custom return periods. It also has a separate income or yield setting when the holding produces income.

The return assumption is how the value of the holding changes.

The income or yield setting is the cash income the holding produces.

Those are different parts of the projection, so only enter the one that actually applies.

And I would not create a custom forecast for every holding just because the control exists. Leave the broad assumption in place unless the holding would otherwise be modeled incorrectly.

== SAVED INPUTS, PREVIEWS, AND SCENARIOS ==

The other thing to understand is that Orange Plan does not have one save rule across every page.

Some fields are direct plan inputs. Planned retirement age, baseline spending, confidence target, and many Cash Flow settings save when you finish the field or when the page confirms that it is saved.

Other pages let you preview a strategy before you commit it. You may be able to compare a withdrawal order, a spending choice, or a borrowing strategy and see the result move without changing the saved plan. Those pages have their own Save or Apply to plan action.

A Scenario is separate on purpose. Saving the Scenario saves the question. It does not quietly replace the baseline plan.

So I would not use the blanket rule that nothing happened unless you clicked Apply. That is true on some strategy pages and false on direct-input pages.

Look at what the page is telling you.

Does it say Saved?

Does it say Previewing or Not saved?

Is there a Save or Apply to plan button?

Are you inside a named Scenario?

That tells you whether you are looking at the current plan or a proposed change.

== WHERE THE RESULT CAME FROM ==

If the retirement result moves after you change inflation, we should be able to explain why.

Future spending is rising faster, which means the plan has to fund more money every year. That can lower confidence and move the earliest date later.

If a Bitcoin ETF is using stock returns, the edit source is that holding's advanced settings.

If a large future purchase is missing, the edit source is the life event.

You do not fix the result at the result. You find the input or planning decision that produced it.

== HOW I WOULD CHOOSE THE ASSUMPTIONS ==

I would use 4 questions.

First, can you explain where the number came from?

Second, is the return shape realistic across the full planning period instead of assuming one high percentage forever?

Third, which direction would you rather be wrong?

And fourth, what happens when you test a weaker version in Scenarios?

The point is not to predict the future exactly. The point is to build a useful base plan and understand which assumptions the result depends on.

== YOUR DECISION ==

Your decision is the return view and inflation rate the saved plan is going to use.

Then decide whether any specific holding genuinely needs a different return or yield from the broad asset-class assumption. Most holdings will not.

== PUT IT IN ORANGE PLAN ==

During onboarding, choose the Planning Assumptions view you want to start with.

After onboarding, go to Plan, then Retirement, and open Edit assumptions when you need to review or change the saved Plan assumptions.

For a holding-specific assumption, go to the holding on Dashboard, select Edit, open Advanced settings, and then Projection overrides.

Use Scenarios when you want to test a different return or inflation view without replacing the baseline.

== YOU ARE DONE WHEN ==

You can sort something into baseline, life event, or scenario without guessing.

You can explain why you chose the return and inflation assumptions in the saved plan.

Any holding that genuinely needs a different return or yield has a deliberate override, and every other holding is deliberately using the broad Plan assumption.

And before you leave a page, you can tell whether you saved a plan input, previewed a strategy, or saved a separate Scenario.
