ADVANCED TELEPROMPTER SCRIPT — segment A7.1
A7.1 Passphrase, collaborative custody, and DIY multisig
457 words · ~2.9 min at 155 wpm · PRE-DICTATION FILMING DRAFT
PUBLICATION GATE: Research complete. Verify exact devices, wallet software, descriptors, provider roles, and recovery procedures before any setup-specific footage.
============================================================

Advanced custody is only safer when the added complexity removes a real risk that the household understands.

A passphrase wallet uses a normal seed plus an additional passphrase to derive a different wallet. The passphrase is sometimes called a twenty-fifth word, but it does not have to be one word and it is not a second signature.

Anyone with the seed and exact passphrase can control the wallet. A wrong passphrase can still produce a valid but different wallet, which makes recovery mistakes especially dangerous.

The benefit is that possession of the seed alone may not reveal the intended wallet. The risk is losing, mistyping, or failing to communicate the passphrase. Test the exact recovery with a trivial amount and store the recovery components according to a deliberate plan.

A two-of-three multisig wallet uses three keys and requires two valid signatures. One lost key does not necessarily destroy access, and one stolen key does not spend alone.

The wallet also depends on public configuration information: the keys or xpubs, threshold, script type, derivation paths, and related descriptor data. This configuration has no private spending key by itself, but it is essential to reconstructing the wallet correctly and can reveal privacy information.

Collaborative custody shares the operational burden with a provider. The customer may hold two keys while the provider holds one, or use another arrangement defined by the service. The provider may also retain the wallet configuration, help verify an executor, and guide recovery.

The trade-off is dependence on the provider's continued operation, policies, identity checks, jurisdiction, security, fees, and privacy. Understand how to recover without the provider when the product claims that is possible.

DIY multisig removes the provider but leaves every task with the household: device diversity, key generation, backups, descriptor storage, software compatibility, transaction signing, inheritance, and periodic testing.

Device diversity can reduce one-vendor risk, but too many device types can also make the process harder to maintain. Each component should have a reason.

Compare the three setups on:

- what one stolen component can do;
- what one lost component does;
- how many people and locations are required;
- how recovery works after ten years;
- how the family gets help;
- what happens when a vendor or provider disappears;
- ongoing cost and maintenance;
- and whether the legal plan matches the technical control.

Do not move a life-changing stack directly into a new advanced setup. Build a small test wallet, send and receive, replace or lose one component on purpose, recover it, and document the process without writing secrets into the documentation.

The safest setup is not the one with the most hardware. It is the simplest design that removes the household's actual failure points and can still be recovered by the people who will inherit the responsibility.
