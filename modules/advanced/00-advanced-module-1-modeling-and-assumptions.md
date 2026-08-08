# Advanced Module 1 — Modeling and Assumptions

## A1.1 How Orange Plan models Bitcoin: fat tails, correlations, floors and caps
*`TEACH` · ~400 words · ~3 min*

> **Gate.** Watch this if either is true on your own screen: changing one
> assumption moved your Plan page's confidence number by more than 10 points and
> you want to know why, or you are about to hand your report to someone who will
> ask how the simulation works. If your number is stable and nobody is auditing
> it, core 1.3 already taught you to *read* it and your plan is complete without
> this. This lesson is how the number is *built*.

**By the end of this lesson, you can:**

- Explain why a normal bell curve is the wrong model for Bitcoin
- Say what the floors and caps on the fat tail are anchored to
- Explain why the assets are correlated rather than independent

---

In today's lesson, we're going to open up the simulation behind your confidence number, because you shouldn't have to take a number on faith to trust it.

### Why bitcoin needs a fat-tailed model

Most models out there assume returns follow a normal bell curve. And if you point one of those at Bitcoin, it's going to tell you that a year down 70% basically never happens. Anyone who's been in Bitcoin for more than a cycle knows that's wrong.

Bitcoin has had years down more than 70%, and it's had years where it tripled. Those extreme years show up in Bitcoin's history far more often than a bell curve would predict. That's what "fat tails" means — the extremes on both ends stay likely, instead of vanishing the way they do in a normal distribution.

So the engine uses a fat-tailed distribution for Bitcoin, calibrated to its actual return history. If you built a plan on a bell-curve model of Bitcoin, the plan would look sturdier than it actually is.

### Volatility and correlations

Every asset in the simulation gets its own volatility. Bitcoin runs at roughly 50%, easing toward 20% as it matures — which is about three times as far as stocks move in a typical year. And that, by the way, is exactly why a Bitcoin holder needs a bigger cash reserve than a stock holder does.

The extremes are grounded in reality too. Bitcoin's single-year floor in the model is set just past its worst actual year, and there's a cap on the upside so the fat tail doesn't produce years that never happened.

The assets also don't run independently, because markets move together in the real world. Bitcoin and stocks are tied at a correlation of about 0.35 — they don't move in lockstep, but they tend to fall in the same years more often than not. And inflation runs negatively correlated with stocks, so in the paths where your costs rise, your balances tend to fall. Those relationships come from long-term capital market research.

### What this means for your number

None of this makes the model right. It makes it honest about what it doesn't know, which is a different and more useful thing.

A model that assumed Bitcoin behaved like a bond fund would hand you a confidence number that looked wonderful and meant nothing. What you're getting instead is a number built on the assumption that the extremes stay likely, because for Bitcoin, they have.

### Homework

Your homework for this lesson is to:

1. Open your assumptions and confirm you could defend each one out loud. That's the standard, and it's the same standard the report's assumptions section is held to.
2. If any of them came from wanting a better answer rather than from information, change it back.
