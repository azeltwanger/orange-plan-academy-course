# Advanced Module 7 — Advanced Custody

## A7.2 What self-custody actually asks of you

*`TEACH` · ~470 words · ~3 min*

> **Gate.** Optional throughout. Watch it if you are weighing whether you want
> the whole job of self-custody, or if the weight of it is what has been
> stopping you. Your custody plan is complete without it.

**By the end of this lesson, you can:**

- Name the responsibility self-custody transfers to you
- Decide whether you want the whole job, part of it, or none of it
- Match that honest answer to the custody level you can actually maintain

---

A client put this better than I ever have.

He said that with self-custody, you are the point of failure. And you are not only the failure point. You are also the attack vector.

Then he made the point that most of life does not work this way. We outsource violence to the police. We outsource security to banks and other institutions. A big part of civilization is handing the hard and dangerous jobs to people whose job it is to carry them.

Bitcoin gives you the ability to take one of those jobs back.

That is why custody can feel heavier than the rest of a financial plan. It is not another investment checkbox. You are accepting a responsibility that somebody else carries for nearly every other asset you own.

### What the whole job includes

The whole job is not just owning a hardware wallet.

It includes protecting the recovery material, keeping the process usable, testing that recovery works, maintaining the devices and software, noticing new single points of failure, and making sure somebody besides you can follow the process when your family needs it.

The device is one part. The ongoing responsibility is the job.

### Three honest answers

The first honest answer is that you want the whole job. That can be the right choice when the amount, your skill, and your willingness to maintain it all line up.

The second answer is that you want part of it. That is what collaborative custody is for, and it is why a hardened institution can legitimately hold part of a stack. You keep some control and hand off some responsibility.

The third answer is that you do not want the job right now. That is also a real answer. Taking responsibility you will not maintain is not more sovereign. It is just a new way to lose access.

If you take the job, I think some caution is appropriate. You should feel the weight of it. Then build a process strong enough that you do not have to think about it every day.

### Your decision

Whether you want the whole job, part of it, or none of it right now.

### Homework

1. Write which parts of custody you are willing to own and which parts you want help carrying.
2. Name the one recovery or maintenance task you would need to prove before moving more Bitcoin into self-custody.
3. Match the answer to the custody level from the core module. Do not choose a more complicated setup than your household can operate.

You are done when the custody setup matches the responsibility you are actually willing to maintain, not the identity you want it to signal.

## A7.3 Concentration: one institution, one vendor, one firmware
*`TEACH` · ~486 words · ~3 min*

> **Gate.** Watch this if either is true on your own screen: (1) your
> non-self-custodied Bitcoin sits at a single institution and losing access to
> it for a few months would change your life, or (2) every satoshi you own is
> behind one model of one device from one manufacturer. If neither is true,
> your custody plan is complete without this.

**By the end of this lesson, you can:**

- Tell a concentration failure apart from a custody failure
- Decide whether your custodial Bitcoin belongs at more than one institution
- Name what your entire self-custodied stack is trusting
- Decide honestly whether you can maintain a second setup at all

---

In today's lesson, we're going to find concentration that remains after choosing a custody level.

Custody type and concentration are different questions.

A household can use a strong institution and still have every custodial asset behind one login. It can self-custody and still have every satoshi behind one device model, one firmware family, one wallet implementation, and one recovery process.

### Institution concentration

The 2022 failures showed what happens when customers become unsecured creditors, lose access, or wait through a bankruptcy process.

The lesson is not that every institution fails or that splitting money makes it self-custody.

The lesson is that one institution should not be able to freeze every asset the family needs next month.

I would look at a second independent institution when:

- the custodial amount is large enough that months without access would change the plan;
- the account is part of the emergency or spending bridge;
- one provider holds every taxable, retirement, or lending relationship;
- the second institution genuinely fails in a different way.

Two accounts using the same email, phone, identity provider, bank, or underlying custodian may not be as independent as they look.

### The cost of another account

Every extra account adds another password, authenticator, recovery process, tax record, beneficiary form, and executor row.

Three weak accounts can be worse than one hardened account.

Add an institution only when the reduced concentration is worth the maintenance and the family map is updated immediately.

### Vendor concentration in self-custody

Self-custody removes the chosen custodian's control. It does not remove every dependency.

A hardware wallet still depends on device hardware, firmware, backup standards, wallet software, supply chain, and the user's recovery process.

Using a second vendor or implementation can reduce a correlated vendor or firmware failure.

It does not guarantee safety. A second setup that nobody understands adds human and recovery risk.

### Different failure domains

Diversification only helps when the second path is actually independent.

Examples:

- a hardware wallet from another manufacturer with a compatible but independently implemented recovery path;
- multisig keys from different device vendors;
- part self-custody and part institution;
- separate email, authentication, and recovery paths for custodial accounts.

I would not add a second device or provider just to have more pieces. I would add it when one flaw, provider, credential, household event, or process error can still reach everything.

### Your decision

Whether the current amount justifies a second institution or independent signing path, and whether the household can maintain it well.

### Homework

1. Draw every custodial and self-custody dependency.
2. Circle any one provider, credential, vendor, firmware family, or location that reaches the entire stack.
3. Decide whether to reduce that concentration or accept it deliberately.
4. Add every new account or setup to the family map the same day.

You are done when the remaining concentration is visible, deliberate, and small enough that one failure does not destroy the household plan.


## A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
*`TEACH` · ~648 words · ~4 min*

> **Gate.** Watch this before you have made a hundred small transfers, not
> after. It applies if you buy Bitcoin regularly in small amounts, or if your
> wallet already shows a long list of separate chunks under coin control.

**By the end of this lesson, you can:**

- Explain why your balance is a stack of bills rather than a bucket
- Set a transfer threshold against Austin's 0.01–0.02 BTC rule of thumb, and know the fee test the number is protecting
- Decide whether you have a consolidation chore waiting
- Use a fresh receiving address every time, and say why it matters

---

In today's lesson, we're going to cover the wallet operations that matter after the hardware and recovery process are working.

### Your balance is a set of outputs

Bitcoin does not maintain one account balance inside the protocol.

A wallet tracks unspent transaction outputs, or UTXOs. Each incoming transaction can create one or more outputs the wallet may later spend as inputs.

When you spend, the wallet selects enough inputs to fund the payment and usually creates change back to a new wallet-controlled output.

### Why small outputs matter

Fees depend partly on how much transaction data has to be included.

Spending many small inputs can require more data than spending one larger input.

That does not mean every small UTXO is protocol dust.

Dust has a technical policy meaning tied to the cost of spending an output. Separately, an output can be economically unattractive to spend at a high fee rate even when it is not protocol dust.

The planning question is whether the fee to spend the output later would be material relative to the output.

### Austin's transfer rule

Austin's rule of thumb is to accumulate small exchange purchases and transfer around 0.01 to 0.02 Bitcoin at a time rather than moving every small buy immediately.

That is not a Bitcoin rule and it is not a permanent threshold.

Before using it, check:

- the current fee environment;
- the amount exposed to the exchange while waiting;
- withdrawal fees and minimums;
- whether the future spend fee would still be a rounding error;
- the household's counterparty-risk limit.

If the exchange balance becomes larger than the household is willing to expose, move it even when the threshold has not been reached.

### Consolidation

Consolidation spends several UTXOs to a new output controlled by the same wallet.

It can reduce the number of inputs a later transaction needs, especially when performed during a low-fee period.

It also has costs.

Combining outputs can link activity that was previously less obviously related, reducing privacy. It creates an on-chain transaction and fee now. It can also produce a larger output that becomes a more obvious target for future coin selection.

So consolidation is not automatic cleanup. It is a fee-versus-privacy decision.

Do not consolidate in an emergency, during a high-fee spike, or merely because the wallet shows many rows.

### Address use

Use a fresh receive address when the wallet provides one.

Address reuse can make payments easier to link and can expose more of the wallet's activity to counterparties or observers.

The wallet should verify the receive address on the trusted hardware display before a meaningful transfer.

A descriptor or extended public key can reveal many addresses and wallet history. It cannot sign by itself, but it is privacy-sensitive and belongs in the recovery plan rather than in public notes.

### Labels and coin control

Labeling acquisition source and purpose can help with tax records, privacy decisions, and future coin selection.

Coin control is an advanced tool. Selecting the wrong output can break the intended tax identification, combine private clusters, or create inefficient change.

Use it only when you understand the wallet's behavior and the tax record is made no later than the transaction.

### Your decision

The transfer threshold, whether consolidation is currently justified, and which privacy trade-off you accept.

### Homework

1. Open coin control or the wallet's UTXO view without changing anything.
2. Identify very small outputs, labels, and repeated addresses.
3. Estimate the fee to spend them at a normal and high fee rate.
4. Decide whether to leave them, consolidate during a low-fee period, or change the future transfer threshold.
5. Update the annual custody review with the decision.

You are done when the threshold is tied to current fees and counterparty exposure, and consolidation is treated as a privacy decision rather than housekeeping.


## A7.1 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · ~1,127 words · ~7 min*

> **Gate.** Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.

**By the end of this lesson, you can:**

- Tell passphrase, collaborative multisig, and DIY multisig apart by what each one buys and costs
- Build a passphrase strong enough to protect a stack (the 7-random-word standard)
- Vet a collaborative-custody provider with four questions
- Back up the multisig config file the way you back up a key

---

In today's lesson, we're going to compare three ways to add separation beyond a single-signature wallet: a passphrase, independent multisig, and collaborative multisig.

I would only add complexity when it removes a specific failure and your family can still operate the recovery process.

### Start with the two tests

Test one: can one person or one stolen item authorize a spend?

Test two: can one lost item or one unavailable person permanently block recovery?

A passphrase and multisig answer those tests in different ways.

### A bip39 passphrase

A BIP39 passphrase is an optional string used with a compatible mnemonic backup to derive a different wallet.

It is not simply an extra recovery word appended to the list.

Every possible passphrase derives a valid wallet. A typo does not produce an error. It produces a different wallet, often one with a zero balance.

That means the exact passphrase is part of the recovery material for the intended wallet.

The mnemonic without the passphrase can still derive the standard wallet. Whether that standard wallet is empty, a decoy, or used for a small balance is a deliberate design choice—not something the protocol does automatically.

### What the passphrase buys

If the mnemonic and passphrase are stored separately, finding one does not reveal the intended passphrase wallet.

Operationally, the household can place the two elements with different people or locations.

But this is not cryptographic multisig. There are not two independent signers and there is no threshold policy enforced on-chain.

Anyone who obtains both elements can derive the wallet. Losing either can make the intended wallet unrecoverable.

### Austin's passphrase rule

Austin's course rule is a long randomly generated passphrase, often seven random words, written and backed up offline.

That is an operational recommendation, not a BIP39 minimum and not a universal password rule.

Whatever method you choose, the passphrase must be generated without a human pattern, recorded exactly, kept separate from the mnemonic, backed up on its own side, and tested on the intended wallet.

Do not enter it into a password manager, AI, generic cloud note, or everyday computer merely because it is called a passphrase.

### Independent multisig

In a 2-of-3 multisig wallet, any two signing keys can authorize a spend and one key cannot.

That threshold can pass both tests: no single key spends, and one key can be lost.

The signing keys are only part of the recovery package.

The household also needs the wallet policy or descriptor and enough script, derivation, and key-origin information for compatible software to reconstruct the wallet.

A descriptor can reveal wallet structure, public keys, and addresses. Protect it for privacy and back it up for availability.

The descriptor helps reconstruct and watch the wallet, but it cannot sign a transaction by itself.

One signing key stored with the descriptor is still one signing key in a 2-of-3 wallet. The old course incorrectly said that combination quietly created single-key control. It does not.

### Where the policy lives

The policy or descriptor can be copied more freely than a signing secret because it cannot spend, but do not publish it.

Keep redundant copies in places the recovery team can reach. Avoid storing the only policy copy inside one hardware wallet or only with one provider.

You are done when any two people who are supposed to recover the wallet can do it without guessing derivation paths or depending on one company.

### Key distribution

A common 2-of-3 design places keys in separate failure domains.

For example:

- one key with the owner;
- one key in a separate secure location or with a trusted participant;
- one key with a collaborative provider or another independent location.

The exact people and locations are estate and threat-model decisions.

Do not put two keys, or their sufficient backups, in the same safe, household, office, or provider if the purpose is to survive that failure.

### Collaborative multisig

Collaborative custody uses a provider for setup, policy coordination, recovery assistance, transaction review, or one signing key.

Do not assume the label guarantees provider independence.

Verify:

1. What is the actual threshold?
2. Which signing keys does the client control?
3. Can the client meet the threshold without the provider?
4. Has the client exported the wallet policy or descriptor?
5. Which compatible software can reconstruct and spend without the provider?
6. What happens if the provider disappears, is enjoined, or changes terms?
7. Can the provider delay or veto a transaction under the contract or software workflow even when it cannot sign alone?

A provider cannot move a true 2-of-3 wallet with only one key. But the practical recovery claim is only proven after the client restores the policy and signs with the client-controlled threshold outside the provider's normal interface.

### Passphrase versus multisig

Choose a passphrase when the household wants a smaller increase in hardware and software complexity and can protect two exact recovery elements.

Choose multisig when on-chain threshold signing, loss tolerance, and distributed control justify the operational work.

Choose collaborative multisig when the household values assistance and has verified that provider independence is real rather than promised.

### Testing

For a passphrase wallet:

- recover on a spare compatible setup;
- enter the exact passphrase;
- verify the intended wallet fingerprint or address;
- confirm the standard no-passphrase wallet is understood;
- test the family process without revealing both elements to one unintended person.

For multisig:

- export and restore the policy or descriptor;
- verify the intended receive address on each signing device;
- create a small test transaction;
- sign with each intended two-key combination, or at least every combination the recovery plan depends on;
- prove one key cannot complete the transaction;
- for collaborative custody, complete a provider-independent recovery test.

### The family and estate layer

The access map names roles and process, not secrets.

The legal plan names who has authority. The key plan names who can technically sign. Those two systems must agree, but one does not replace the other.

A trustee, executor, heir, or provider holding one key does not automatically have legal control or unilateral technical control. The governing documents and full signing policy decide the result together.

### Your decision

Which failure you are removing and why the added complexity is worth maintaining.

### Homework

1. Write the two access-test answers for the proposed setup.
2. Inventory every required recovery element, including the policy or descriptor.
3. Run the exact spare-device or provider-independent recovery test.
4. Update the no-secrets custody map and legal plan so roles match the signing policy.

You are done when the setup survives the failure it was built for and the family can recover it without the vendor, without guessing, and without one unintended person holding enough to spend.
