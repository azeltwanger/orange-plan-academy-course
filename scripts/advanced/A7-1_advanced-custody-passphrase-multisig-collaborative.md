TELEPROMPTER SCRIPT — segment A7.1
A7.1 Advanced custody: passphrase, multisig, and collaborative
~15 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to compare three ways to add separation beyond a single-signature wallet: a passphrase, independent multisig, and collaborative multisig.

I would only add complexity when it removes a specific failure and your family can still operate the recovery process.

== START WITH THE TWO TESTS ==

Test one: can one person or one stolen item authorize a spend?

Test two: can one lost item or one unavailable person permanently block recovery?

A passphrase and multisig answer those tests in different ways.

== A BIP39 PASSPHRASE ==

A BIP39 passphrase is an optional string used with a compatible mnemonic backup to derive a different wallet.

It is not simply an extra recovery word appended to the list.

Every possible passphrase derives a valid wallet. A typo does not produce an error. It produces a different wallet, often one with a zero balance.

That means the exact passphrase is part of the recovery material for the intended wallet.

The mnemonic without the passphrase can still derive the standard wallet. Whether that standard wallet is empty, a decoy, or used for a small balance is a deliberate design choice—not something the protocol does automatically.

== WHAT THE PASSPHRASE BUYS ==

If the mnemonic and passphrase are stored separately, finding one does not reveal the intended passphrase wallet.

Operationally, the household can place the two elements with different people or locations.

But this is not cryptographic multisig. There are not two independent signers and there is no threshold policy enforced on-chain.

Anyone who obtains both elements can derive the wallet. Losing either can make the intended wallet unrecoverable.

== AUSTIN'S PASSPHRASE RULE ==

Austin's course rule is a long randomly generated passphrase, often seven random words, written and backed up offline.

That is an operational recommendation, not a BIP39 minimum and not a universal password rule.

Whatever method you choose, the passphrase must be generated without a human pattern, recorded exactly, kept separate from the mnemonic, backed up on its own side, and tested on the intended wallet.

Do not enter it into a password manager, AI, generic cloud note, or everyday computer merely because it is called a passphrase.

== INDEPENDENT MULTISIG ==

In a 2-of-3 multisig wallet, any two signing keys can authorize a spend and one key cannot.

That threshold can pass both tests: no single key spends, and one key can be lost.

The signing keys are only part of the recovery package.

The household also needs the wallet policy or descriptor and enough script, derivation, and key-origin information for compatible software to reconstruct the wallet.

A descriptor can reveal wallet structure, public keys, and addresses. Protect it for privacy and back it up for availability.

The descriptor helps reconstruct and watch the wallet, but it cannot sign a transaction by itself.

One signing key stored with the descriptor is still one signing key in a 2-of-3 wallet. The old course incorrectly said that combination quietly created single-key control. It does not.

== WHERE THE POLICY LIVES ==

The policy or descriptor can be copied more freely than a signing secret because it cannot spend, but do not publish it.

Keep redundant copies in places the recovery team can reach. Avoid storing the only policy copy inside one hardware wallet or only with one provider.

You are done when any two people who are supposed to recover the wallet can do it without guessing derivation paths or depending on one company.

== KEY DISTRIBUTION ==

A common 2-of-3 design places keys in separate failure domains.

For example:

- one key with the owner;
- one key in a separate secure location or with a trusted participant;
- one key with a collaborative provider or another independent location.

The exact people and locations are estate and threat-model decisions.

Do not put two keys, or their sufficient backups, in the same safe, household, office, or provider if the purpose is to survive that failure.

== COLLABORATIVE MULTISIG ==

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

== PASSphrase VERSUS MULTISIG ==

Choose a passphrase when the household wants a smaller increase in hardware and software complexity and can protect two exact recovery elements.

Choose multisig when on-chain threshold signing, loss tolerance, and distributed control justify the operational work.

Choose collaborative multisig when the household values assistance and has verified that provider independence is real rather than promised.

== TESTING ==

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

== THE FAMILY AND ESTATE LAYER ==

The access map names roles and process, not secrets.

The legal plan names who has authority. The key plan names who can technically sign. Those two systems must agree, but one does not replace the other.

A trustee, executor, heir, or provider holding one key does not automatically have legal control or unilateral technical control. The governing documents and full signing policy decide the result together.

== YOUR DECISION ==

Which failure you are removing and why the added complexity is worth maintaining.

== HOMEWORK ==

1. Write the two access-test answers for the proposed setup.
2. Inventory every required recovery element, including the policy or descriptor.
3. Run the exact spare-device or provider-independent recovery test.
4. Update the no-secrets custody map and legal plan so roles match the signing policy.

You are done when the setup survives the failure it was built for and the family can recover it without the vendor, without guessing, and without one unintended person holding enough to spend.
