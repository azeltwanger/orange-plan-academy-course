# A7.4 — Understand UTXOs before consolidating coins

Status: TEACHING_REPAIR_NEEDED — the prior course-wide pass was rejected for voice and teaching clarity. This component still needs individual repair; it is not approved.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CAPTURE
Sources: CUSTODY, PRIMARY
Use when: the household has many small Bitcoin receipts or is considering consolidation or coin control.

### Read aloud

Before consolidating Bitcoin, understand what you are combining and why. A balance can be made of many unspent outputs. Spending more inputs can affect transaction size, fees and privacy, even when the total Bitcoin sent is the same.

Transaction fees depend primarily on the transaction's data weight and the fee rate, not simply on the dollar amount being sent. Spending many small outputs can require more transaction data than spending one larger output of the same total value.

That matters for frequent small withdrawals or long histories of small receipts. A balance may be worth holding, yet parts can be expensive to spend when fees are high. There is no permanent dollar or Bitcoin threshold that is correct in every fee environment.

Consolidation spends several outputs into fewer outputs you control. It can reduce the number of inputs needed later, but it also has a fee today and privacy consequences. Combining outputs can link them on the public transaction graph. Coin control can help manage which outputs are combined when the wallet supports it.

First identify the purpose. Are you reducing future spending complexity, preparing for a planned transaction, or responding to a fee concern? Then check current fee conditions, wallet support, backup status, and the privacy trade-off. Consolidating everything because a course mentioned it is not a useful rule.

Use the correct network and verify the destination through the trusted device process. A transaction to yourself still needs careful review. Confirm that the wallet and tax records preserve the movement and any relevant fee treatment without inventing a new purchase at the current price.

For multisig or other wallet types, input size and recovery requirements can differ. Use the actual wallet's current documentation and test with a small value where appropriate. Avoid manually following a procedure written for a different script type or device.

The separate demonstration uses a small test setup. Match any procedure to your own wallet and backup method before using it. You may conclude that no consolidation is necessary now.

Use the wallet's fee preview and coin selection to compare a proposed transaction with fewer inputs. The useful question is whether paying a fee now and linking those outputs is worth the possible later simplification. Current fee conditions can change, and the actual size depends on the wallet and transaction. A course example cannot supply a permanent consolidation threshold for your holdings.

Return with a deliberate decision to consolidate or leave the outputs alone, the fee/privacy trade-off understood, and a verified safe transaction process. Match any procedure to your own wallet and backup method. More wallet activity is not itself an improvement.

### Production notes

Use Bitcoin developer documentation and current wallet-specific coin-control instructions. No universal dust cutoff, fee quote, address publication, or secret display. Tax treatment of network fees requires applicable review. Return to 7.2–7.4.

### Member checkpoint

- Explain output count, fee weight, and consolidation trade-offs.
- Verify wallet support and recovery before transacting.
- Consolidate only for a defined purpose under a safe current procedure.

### Source-led visual and teaching notes — not spoken

Generic inputs → recipient/change outputs and a fee-preview comparison; no actual wallet address or live fee quote. Distinguish a self-transfer from a new purchase in tax history.

Editorial reason: Make coin consolidation a conditional maintenance decision with fee and privacy consequences.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

On the separately approved test setup, inspect output selection and the actual fee preview without revealing sensitive identifiers. Compare input counts, explain privacy links and verify the destination on the trusted device. No transaction until the exact wallet procedure and recovery status are reviewed. Return to 7.2–7.4.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
