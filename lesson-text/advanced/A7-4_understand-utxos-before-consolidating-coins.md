# A7.4 — Understand UTXOs before consolidating coins

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: DEVICE_CAPTURE
Sources: CUSTODY, PRIMARY
Use when: You are considering consolidating Bitcoin outputs or selecting outputs manually for a transaction.
After lesson: 7.2
Complete before: Complete before that wallet transaction; it is not a requirement to consolidate.
Return to: Finish the relevant safe wallet work, then lesson 7.3

### Read aloud

Your Bitcoin balance may look like one number, but the wallet can spend it using several separate unspent transaction outputs, usually called UTXOs. Understanding that helps when fees, privacy or many small receipts become a real issue.

You don't need to manage every output by hand for ordinary use. This lesson is for a consolidation or coin-control decision with a specific purpose.

Think of the wallet's spendable balance as separate pieces created by earlier transactions. A new transaction selects pieces as inputs and creates new outputs, including change when appropriate. The fee depends on the transaction's data size and the selected fee rate—not simply how many dollars you are sending.

Virtual bytes are a measure used for that size. Satoshis are small units of Bitcoin. A fee rate in satoshis per virtual byte lets you compare how much the selected transaction would pay.

For an arithmetic example, a preview of 500 virtual bytes at 2 satoshis per virtual byte gives a fee of 1,000 satoshis. At 20 satoshis per virtual byte, that same size costs 10,000 satoshis.

Those are hypothetical fee calculations, not today's rates. The wallet, script type, inputs, and outputs determine the size of your transaction. Read both its size and fee rate in the preview.

Spending many small outputs can require more transaction data than spending fewer larger outputs. Consolidation combines selected outputs into fewer outputs you control. That can reduce the input work needed for a later payment, but you pay a fee now to do it.

Privacy changes too. Combining outputs can reveal a common-control link between histories that were previously separate. Don't consolidate everything by default just because the fee looks low. A future convenience can come with a link you cannot undo on the public transaction record.

Coin control, when supported, lets you choose which outputs to spend. First identify why you are doing that: preparing for a particular payment, reducing future complexity, or keeping sources separate. Then compare the actual preview with the wallet's ordinary selection.

There isn't a permanent dollar or Bitcoin cutoff for useful consolidation. An output's cost to spend depends on the fee environment and transaction type. A quoted dust threshold from a different script or policy isn't a universal minimum for every wallet.

Before transacting, verify the wallet setup and recovery status. Use the correct network and the trusted device process to confirm the destination. A self-transfer still sends real funds and deserves the same address and fee checks as another payment.

Preserve the ownership and purchase history in the records. Moving coins to your own new output does not automatically mean you acquired the Bitcoin again at today's price. Real transaction-fee treatment needs the appropriate supported tax handling rather than an invented balancing purchase.

Coin control selects transaction outputs; it does not, by itself, establish which tax lots you have legally identified. A consolidation can combine several purchase histories into one output. Keep the acquisition records and any required timely identification alongside the transaction history.

The demonstration uses a separate small-value setup. It shows the available outputs, actual preview and privacy comparison without publishing sensitive addresses or recovery material. Match the procedure to the exact wallet and software before using it with your own holdings.

Compare the fee paid now, the possible saving on a later payment, and the privacy cost. Consolidate only the outputs that fit your purpose—or leave them alone when a transaction wouldn't improve the situation.

### Visual and source notes — not spoken

Current Trezor coin-control and UTXO documentation and COLDCARD UTXO management support input, fee and privacy mechanisms; no universal dust value carried into narration. New hypothetical 500 vB at 2 or 20 sat/vB gives 1,000 or 10,000 sats. Actual size depends on wallet/script and inputs/outputs. No live fee quote, specific address, real secret, blanket consolidation or tax-basis reset. Device capture remains gated.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Use an approved practice wallet to inspect actual output selection and fee preview; show the generic multiplication separately. Narration: “This is the fee for this transaction shape. Consolidating may simplify a later payment, but it spends fees now and links these outputs.” No broadcast until explicitly authorized and exact procedure verified; no sensitive identifiers filmed.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Source-based technical check — not spoken

September 8, 2026: P10; S7, S26. This is a cross-check between output selection and tax identification; not a claim that each output is a unique tax lot or that a self-transfer resets basis. Preserve metadata privacy and the actual device procedure. See [the technical review](../../delivery/professional-topic-review.md). These are source-backed clarifications; licensed sign-off, actual inputs and execution remain separate.

### Member checkpoint

Choose a justified consolidation, coin-control action or deliberate pass after reading the actual fee/privacy trade-off and safe procedure.
