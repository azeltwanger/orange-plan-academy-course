TELEPROMPTER SCRIPT — segment A7.4
A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
~6 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to cover the wallet operations that matter after the hardware and recovery process are working.

== YOUR BALANCE IS A SET OF OUTPUTS ==

Bitcoin does not maintain one account balance inside the protocol.

A wallet tracks unspent transaction outputs, or UTXOs. Each incoming transaction can create one or more outputs the wallet may later spend as inputs.

When you spend, the wallet selects enough inputs to fund the payment and usually creates change back to a new wallet-controlled output.

== WHY SMALL OUTPUTS MATTER ==

Fees depend partly on how much transaction data has to be included.

Spending many small inputs can require more data than spending one larger input.

That does not mean every small UTXO is protocol dust.

Dust has a technical policy meaning tied to the cost of spending an output. Separately, an output can be economically unattractive to spend at a high fee rate even when it is not protocol dust.

The planning question is whether the fee to spend the output later would be material relative to the output.

== AUSTIN'S TRANSFER RULE ==

Austin's rule of thumb is to accumulate small exchange purchases and transfer around 0.01 to 0.02 Bitcoin at a time rather than moving every small buy immediately.

That is not a Bitcoin rule and it is not a permanent threshold.

Before using it, check:

- the current fee environment;
- the amount exposed to the exchange while waiting;
- withdrawal fees and minimums;
- whether the future spend fee would still be a rounding error;
- the household's counterparty-risk limit.

If the exchange balance becomes larger than the household is willing to expose, move it even when the threshold has not been reached.

== CONSOLIDATION ==

Consolidation spends several UTXOs to a new output controlled by the same wallet.

It can reduce the number of inputs a later transaction needs, especially when performed during a low-fee period.

It also has costs.

Combining outputs can link activity that was previously less obviously related, reducing privacy. It creates an on-chain transaction and fee now. It can also produce a larger output that becomes a more obvious target for future coin selection.

So consolidation is not automatic cleanup. It is a fee-versus-privacy decision.

Do not consolidate in an emergency, during a high-fee spike, or merely because the wallet shows many rows.

== ADDRESS USE ==

Use a fresh receive address when the wallet provides one.

Address reuse can make payments easier to link and can expose more of the wallet's activity to counterparties or observers.

The wallet should verify the receive address on the trusted hardware display before a meaningful transfer.

A descriptor or extended public key can reveal many addresses and wallet history. It cannot sign by itself, but it is privacy-sensitive and belongs in the recovery plan rather than in public notes.

== LABELS AND COIN CONTROL ==

Labeling acquisition source and purpose can help with tax records, privacy decisions, and future coin selection.

Coin control is an advanced tool. Selecting the wrong output can break the intended tax identification, combine private clusters, or create inefficient change.

Use it only when you understand the wallet's behavior and the tax record is made no later than the transaction.

== YOUR DECISION ==

The transfer threshold, whether consolidation is currently justified, and which privacy trade-off you accept.

== HOMEWORK ==

1. Open coin control or the wallet's UTXO view without changing anything.
2. Identify very small outputs, labels, and repeated addresses.
3. Estimate the fee to spend them at a normal and high fee rate.
4. Decide whether to leave them, consolidate during a low-fee period, or change the future transfer threshold.
5. Update the annual custody review with the decision.

You are done when the threshold is tied to current fees and counterparty exposure, and consolidation is treated as a privacy decision rather than housekeeping.
