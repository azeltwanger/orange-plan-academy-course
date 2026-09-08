# 1.4 — Choose assumptions you can explain

Status: SOURCE_LED_REVIEW — revised using the accepted Reserve reference; integrated wording awaits Austin's review.
Adapted source: `course-v2/sessions/01-first-working-plan.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`, Austin's August 25 assumptions dictation, and the sources identified in `delivery/source-led-batch-01.md`.
App references: model choices and exact preset paths require final build verification; no current preset rate is asserted.

Kind: teach
Gate: OWNER_REVIEW
Sources: DICTATION, FOUNDATION, APP, MASTER

### Read aloud

The assumptions you choose here affect every later decision. They help determine what retirement timing looks possible, how much you need to save, and what different account and tax strategies might do.

I would start with numbers you could explain to a family member or friend. Not the numbers that make the plan look best, and not an extreme worst case you don't actually believe. We want an honest starting point, then separate comparisons that show what happens when we're wrong.

Start with the investment-growth assumptions. For a simple example, ten thousand dollars growing at ten percent a year for ten years becomes about twenty-six thousand before tax. At twenty percent, it becomes about sixty-two thousand. These are hypothetical calculations, not forecasts. The starting money is identical. The assumption makes a very different future picture.

That is why I would be careful about solving a retirement shortfall by turning up Bitcoin's expected return. The date may look better immediately, but the household has not saved more, reduced a bill, or changed how it will pay for anything. It is now depending on a stronger outcome.

I lean toward a defensible, more conservative starting point when the plan can work that way. If returns are better, we can review the extra options that creates. If the plan requires very optimistic returns just to meet essential needs, I want that dependency visible before the household acts on it.

My preference for a long Bitcoin plan is to let the assumed growth decline over time rather than carry one large annual percentage through every decade. Power Law is one model I've used to think about that. It is still a model, not a guarantee about adoption or future price. Read the path it produces and decide whether it represents the belief you intend to use.

A declining model can use a higher rate early and a lower rate later. An average across the whole period doesn't tell you the rate being used in a particular year. Look at an early year and a later year so you understand that difference. Changing the label from one preset to another means little until you know what changed underneath it.

Inflation deserves the same attention. A lifestyle costing a hundred thousand dollars today would cost about a hundred thirty-four thousand in ten years at three percent annual inflation. That is another hypothetical example. The extra dollars buy the same lifestyle; they are not necessarily extra discretionary spending.

Check whether each spending input is in today's dollars or future dollars. If you've already increased a cost for inflation and then enter it as a today's-dollar amount, you can build the increase in twice. Being clear about the units matters as much as choosing the percentage.

Income growth is another assumption. A salary and a business may not grow the same way. A raise you expect at a particular date, or a planned reduction in hours, is a specific change to put on the timeline. It should not disappear inside a general annual rate.

The horizon is how long the plan needs to provide for you. Ending a projection at eighty-five asks less of the assets than carrying it to ninety-five. Consider both people in a couple and the years a surviving spouse may still need support. We want to understand what period we're asking the plan to fund.

Also check how the investments are represented. Direct Bitcoin, a spot Bitcoin fund, a company connected to Bitcoin, and a leveraged fund are not interchangeable records. A company has its own business and financing decisions. Don't give every Bitcoin-related holding the same return treatment simply because Bitcoin is in the story. Use the supported classification and review any deliberate override separately.

Once you have a starting set of assumptions, compare a less favorable version. Begin with one change, such as slower investment growth, while keeping spending, contributions and retirement timing the same. Then you can see what that assumption changes. A combined stress case can come later.

I also want to look at a more optimistic comparison when it matters to the decision. Stronger growth can change the future balances and the tax or account questions worth reviewing. We should not make every decision from an unusually pessimistic picture either. The purpose is to understand the range, not to choose whichever result feels best.

For Alex and Morgan, the first comparison will keep their intended retirement timing and spending choices fixed while we change an investment assumption. The actual result comes from the app demonstration. We won't assign them a winning age in advance.

In the working chapter, we'll read the chosen model, inflation and horizon, compare a different assumption, and distinguish the comparison from the saved plan. You are ready to continue when you can explain what your starting assumptions mean, why you chose them, and which one you most need to test. We can revisit the numbers as the evidence or your life changes.

### Visual notes — not spoken

Use the Foundation deck's starting-assumptions and scenario-comparison visuals. Keep the existing arithmetic cards: $10,000 × 1.10^10 ≈ $25,937; $10,000 × 1.20^10 ≈ $61,917; $100,000 × 1.03^10 ≈ $134,392. Label them hypothetical, before tax where relevant, and separate from the Reed plan. A declining-rate diagram is conceptual, with no unverified preset percentages or promised price path. Compare an early and late year on the actual model only during the recorded insert.

### Production notes

Source ledger: `delivery/source-led-batch-01.md`. Preserve both source judgments: lean conservative/defensible for the baseline and examine bullish alternatives when they change tax/account decisions. The personal Power Law preference comes from the end of the original dictation. Do not silently turn that into a universal recommendation or assert a permanent risk ranking among preset names.

The original dictation's old preset rates, unsupported 50-to-58 retirement example, market-cap/inflow explanation and inconsistent inflation arithmetic are not carried forward. The existing current script's clearly hypothetical arithmetic supplies the visual instead; see the explicit reconciliation in the source ledger. No historical claim is being newly certified. No new return-model implementation or current market benchmark was researched in this editorial pass.

W01 chapter 8 owns the exact choices, units, custom-period entry and Current/Preview behavior. Any sentence that describes an unavailable override remains held for correction against the accepted product direction. A material change to model semantics reopens the affected teaching, not just the screenshot. Do not film the old side-panel click path from dictation.

### Member checkpoint

- Explain the chosen growth model, inflation basis and household horizon.
- Distinguish an assumption change from a real change to income, saving or spending.
- Identify one less-favorable comparison and when an optimistic comparison would answer a useful planning question.
