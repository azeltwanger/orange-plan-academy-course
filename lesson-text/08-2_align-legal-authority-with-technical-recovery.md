# 8.2 · Align legal authority with the technical recovery path

This lesson is about making sure the legal plan and the custody plan lead to the same outcome.

I do not want to give you one universal formula such as "the heirs hold the seed and the executor holds the passphrase." That can work in a carefully designed and tested plan, but it can also create new failure points or give the wrong person practical control.

The right structure depends on the custody method, the people involved, the legal roles, and what each component can actually do.

Start with the principle: no unnecessary person should hold enough information or authority to act alone, but the family must still have a complete, tested recovery path when the proper conditions are met.

With ordinary single-signature custody, anyone who obtains the seed can usually recover that wallet. If a BIP39 passphrase is also used, the seed without the exact passphrase opens a different wallet. The passphrase is not a second signer and it does not create legal dual control. It is another secret that must be recovered exactly.

Splitting those two objects between people can reduce one-person access in some designs, but it can also mean one lost memory, one unavailable person, or one family dispute locks everybody out. It should only be used when the full recovery has been tested and the attorney understands who has legal authority to combine the components.

Do not split a recovery phrase itself into arbitrary word groups and hand the pieces to different people. That creates fragile backups, can reduce security in ways people do not expect, and is not a substitute for a designed secret-sharing or multisig system.

With multisig, the structure is different.

A two-of-three wallet requires two valid signatures from the defined keys. One key alone cannot spend. That can create real operational separation, but the keys are not the entire recovery plan.

The wallet descriptor or configuration records how the keys are combined, including the threshold and derivation information. Without the correct configuration, heirs may struggle to reconstruct the intended wallet even if they have key material.


A collaborative custody provider may hold one key, a copy of the public wallet configuration, and an established recovery process. The value is not only the third key. It is also the support, identity-verification, continuity, and documented procedure. The trade-off is vendor dependence, fees, privacy considerations, and the need to understand what happens if the company changes or disappears.

A DIY multisig arrangement removes the provider but moves every operational duty to the household. Key distribution, descriptors, device compatibility, replacement, inheritance, and recovery documentation all become your responsibility.

The legal role also needs to be clear.

An executor, trustee, spouse, beneficiary, and technical helper may all be different people. The person with a key may not be the person legally entitled to direct a transaction. The person with legal authority may not be technically capable of signing one.

That is why I like separating roles on paper:

- Who has legal authority while you are alive but incapacitated?
- Who has authority after death?
- Who can locate each recovery component?
- Who can provide technical help without receiving every secret?
- Which provider or professional verifies the event and the identity?
- What stops one person from acting prematurely?
- What happens if one person or provider is unavailable?

The system should be tested at the process level while you are alive. You do not need to expose a real seed to the family. You can use a trivial-value test wallet or a documented tabletop exercise to confirm everybody knows the first call, the role they have, and the components that exist.

The plan should also account for change. Hardware wallets fail. Providers merge or close. Executors age. Families move. A custody design that works today can become unusable if it is never reviewed.

The deliverable is not a diagram that looks sophisticated. It is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.

The heir letter in the next lesson tells the family how to start without disclosing the components themselves.

## Apply it

Use walkthrough 8.5 to enter the decision and confirm what Orange Plan calculated.

## Module checkpoint

- [ ] Executor and backup are chosen and contacted.
- [ ] Baseline legal documents and beneficiary forms have a clear status.
- [ ] Legal authority and technical recovery are mapped together.
- [ ] Heir letter and executor packet contain no secrets.
- [ ] The communication backstop is armed and tested when applicable.
- [ ] Insurance gaps are documented for licensed review.
