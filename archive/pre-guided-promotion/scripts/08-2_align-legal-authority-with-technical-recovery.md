TELEPROMPTER SCRIPT — segment 8.2
8.2 Align legal authority with the technical recovery path
640 words · ~4.1 min at 155 wpm · PRE-DICTATION FILMING DRAFT — rebuilt from Austin's decks, dictation, research, and current app
SOURCE: Estate access-split deck, corrected by the custody and legal research audit
============================================================

This lesson is about making sure the legal plan and the custody plan lead to the same outcome.

Use one governing principle for every custody design: the legally authorized people need a complete, tested recovery path while no unnecessary person can act alone. The exact structure changes with the custody method, the people involved, the legal roles, and what each component can actually do.

With ordinary single-signature custody, anyone who obtains the seed can usually recover that wallet. If a BIP39 passphrase is also used, the seed without the exact passphrase opens a different wallet. A passphrase is another secret that must be recovered exactly. Multisig is what creates multiple signers and operational separation.

Splitting those two objects between people can reduce one-person access in some designs, but it can also mean one lost memory, one unavailable person, or one family dispute locks everybody out. It should only be used when the full recovery has been tested and the attorney understands who has legal authority to combine the components.

Do not split a recovery phrase itself into arbitrary word groups and hand the pieces to different people. That creates fragile backups, can reduce security in ways people do not expect, and is not a substitute for a designed secret-sharing or multisig system.

With multisig, the structure is different.

A two-of-three wallet requires two valid signatures from the defined keys. A two-of-three wallet can create operational separation because one key alone cannot spend. The descriptor or wallet configuration, identity process, legal authority, and people remain part of the recovery plan.

The wallet descriptor or configuration records how the keys are combined, including the threshold and derivation information. Heirs need the correct wallet configuration as well as the key material to reconstruct the intended wallet.

🎬 VISUAL — Two separate diagrams: passphrase single-sig and 2-of-3 multisig. Show what each component can and cannot do. Do not label a passphrase as a second signer.

A collaborative custody provider may hold one key, a copy of the public wallet configuration, and an established recovery process. A collaborative provider can add support, identity verification, continuity, a documented procedure, and a third key. The trade-off is vendor dependence, fees, privacy considerations, and the need to understand what happens if the company changes or disappears.

A DIY multisig arrangement removes the provider but moves every operational duty to the household. Key distribution, descriptors, device compatibility, replacement, inheritance, and recovery documentation all become your responsibility.

The legal role also needs to be clear.

An executor, trustee, spouse, beneficiary, and technical helper may all be different people. Legal authority and signing capability can belong to different people.

That is why I like separating roles on paper:

- Who has legal authority while you are alive but incapacitated?
- Who has authority after death?
- Who can locate each recovery component?
- Who can provide technical help without receiving every secret?
- Which provider or professional verifies the event and the identity?
- What stops one person from acting prematurely?
- What happens if one person or provider is unavailable?

The system should be tested at the process level while you are alive. Use a trivial-value test wallet or a documented tabletop exercise to confirm that everybody knows the first call, the role they have, and the components that exist. Keep real recovery secrets out of the exercise.

The plan should also account for change. Hardware wallets fail. Providers merge or close. Executors age. Families move. Review the custody design as devices, providers, and people change.

The deliverable is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.

The heir letter in the next lesson gives the family the safe starting instructions while the recovery components remain separate.
