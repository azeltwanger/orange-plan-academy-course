# 1.3 · How the numbers flow

**Paste `00-STYLE.md` first, then this.**

> **This is the course's reusable reference frame.** Recall the same frame in later modules instead of redesigning it.

## What it has to make obvious
Every result comes from an owning fact or choice, and a changed fact makes the saved result stale until recalculated.

## The visual
A four-band horizontal flow:

    WHAT YOU CHANGE → WHAT ORANGE PLAN CALCULATES → WHAT MOVES → RESULT STATE

Three example rows sit below it.

## Labels and data

Row 1 — cash flow:

    Income − taxes − living − debt payments
    → amount available to save
    → Reserve and contribution routing
    → simulation result becomes stale when the modeled amount changes

Row 2 — life event:

    Expected life event
    → future cash flow in that year
    → account withdrawals and retirement dates
    → recalculated result becomes Current

Row 3 — strategy:

    Current choice → Preview choice
    → before-and-after simulation count, dates, taxes, or spending
    → Save to plan
    → Current updates

## Motion
Build left to right. End by highlighting the state transition **Current → Stale → Recalculate → Current**.
