# When should a holding use its own assumptions?

> **Watch this only if one holding would be modeled incorrectly by the broad Plan default.**

## Default rule

Most holdings should inherit the Plan assumption for their asset class. Overrides correct a genuine mismatch; they are not a tool for tuning the retirement result.

## Worked example: a Bitcoin ETF

An ETF label can cause a spot Bitcoin ETF to look like a stock holding even though its economic exposure is Bitcoin.

The correct fix is to make the holding follow the Plan's Bitcoin assumptions—not to invent a separate optimistic return.

## Return versus income

- **Return:** changes the future value of the holding
- **Income/yield:** creates cash flow

Do not enter the same expected result in both fields.

## Period-specific assumptions

Use a custom period when a real contract or decision changes:

- a note matures,
- a rental is sold,
- a distribution ends,
- or another documented stage begins.

Do not build a custom schedule merely to improve confidence.

## Three-question test

1. Is the holding attached to the wrong broad class?
2. Does it have documented economics or an end date the class cannot represent?
3. Would the correction affect a material planning decision?

If none apply, keep the default.

## Number provenance

- **What it means:** holding-specific return and cash-income behavior
- **Calculated from:** saved holding override periods and rates
- **Edit source:** holding advanced projection assumptions
- **This affects:** future value, income, tax, allocation, confidence, and withdrawals

## Done when

Every override has a real source, does not double-count return and income, and produces an explainable downstream change.
