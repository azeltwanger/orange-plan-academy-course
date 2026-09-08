ADVANCED TELEPROMPTER SCRIPT — segment A7.4
A7.4 UTXOs, dust, consolidation, and address use
347 words · ~2.2 min at 155 wpm · PRE-DICTATION FILMING DRAFT
PUBLICATION GATE: Research complete. Verify current wallet behavior and network fees before demonstrating; use a test wallet and never expose live addresses unnecessarily.
============================================================

A Bitcoin wallet balance is made of individual unspent transaction outputs, or UTXOs. They are closer to separate bills in a wallet than one bank-account balance.

When you spend, the wallet selects one or more UTXOs as inputs. The transaction fee is driven more by the data size and number of inputs and outputs than by the dollar amount being sent.

That is why many tiny withdrawals can become expensive later. Spending a small UTXO can cost a meaningful percentage of its value when fees are high.

There is no permanent minimum withdrawal threshold that works in every year. Bitcoin's dollar price and the fee market change. The useful practice is to avoid automatically creating a large pile of tiny outputs and to consider batching withdrawals when the custody and counterparty trade-off is acceptable.

Consolidation spends several UTXOs into a smaller number of new outputs. Doing it during a low-fee period can reduce the number of inputs needed later.

Consolidation also has privacy costs. Inputs combined in one transaction become linked on-chain, and the resulting larger output may reveal more about the wallet's history or future spending. Do not consolidate every output automatically merely because fees are temporarily low.

Coin control lets an experienced user choose which UTXOs are spent. It can help with privacy, accounting, and avoiding uneconomic outputs, but it adds room for mistakes. Learn it on a test wallet before using it with meaningful funds.

Address reuse reduces privacy because multiple receipts become easy to associate. A modern wallet normally generates a new receive address from the same wallet for each payment. Verify the address on the trusted signing device before sharing it.

Keep tax lots and UTXOs conceptually separate. One is an on-chain spendable output; the other is a tax-accounting record. A transaction can combine UTXOs from several tax lots. The tax records still need to identify which lot was disposed of.

Review UTXO health at the annual custody check: too many tiny outputs, any consolidation worth planning, current fees, privacy implications, and whether the wallet and backup still reconstruct the same addresses.
