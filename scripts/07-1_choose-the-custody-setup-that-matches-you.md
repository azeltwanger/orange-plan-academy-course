TELEPROMPTER SCRIPT — segment 7.1
7.1 Choose the custody setup that matches your stack and family
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to choose the custody setup you can actually maintain and your family can actually recover.

The four levels in this course are an Orange Plan framework. They are not a Bitcoin protocol standard and they are not a score.

The right level is the simplest setup that protects the amount at stake, survives the failures you care about, and still works when somebody besides you has to use it.

== THE JOB OF CUSTODY ==

Bitcoin exists on the network. Custody is control of the signing material that can authorize a spend.

Depending on the setup, that can involve:

- an institution's account and legal claim process;
- one hardware wallet and its recovery material;
- a wallet backup plus a passphrase;
- multiple signing keys and a wallet policy or descriptor;
- a collaborative provider and a documented provider-independent recovery path.

Do not call every one of those things a seed. The backup standard matters.

== FIVE QUESTIONS BEFORE THE LEVEL ==

First: how much is at stake today, and what could it become under assumptions you would defend?

Second: who depends on it?

Third: which loss worries you most—online account takeover, physical theft, backup loss, coercion, provider failure, incapacity, or death?

Fourth: how much operational complexity will you actually maintain?

Fifth: can somebody else follow the recovery process without improvising or learning Bitcoin during a crisis?

I would choose the simplest setup you can actually prove works.

== LEVEL 1: HARDENED INSTITUTION ==

Level 1 delegates signing control to a regulated or otherwise chosen institution.

Your job is account security, beneficiary and death-claim paperwork, withdrawal controls, and diversification of whatever counterparty exposure you keep.

The family recovery test is not a device restore. It is the institution's login-recovery and death-claim process.

Verify what documents the institution requires, who can make the claim, whether a beneficiary designation exists, how long the process can take, and what happens if the institution fails.

This level trades self-custody risk for counterparty and legal-claim risk. That can be a legitimate trade when it is deliberate.

== LEVEL 2: SINGLE-SIGNATURE HARDWARE WALLET ==

Level 2 moves signing control into a hardware wallet and a compatible wallet setup.

The recovery material may be a BIP39 mnemonic, another single backup, or a supported multi-share standard. Record the actual standard rather than assuming every device uses 12 or 24 words.

The hardware wallet is replaceable. The recovery material and any required passphrase or wallet information are the durable pieces.

I think this is simple enough for a lot of households to maintain well. The risk is that one complete backup can authorize the wallet, and one missing required piece can also block recovery.

== LEVEL 3: ADDED SEPARATION ==

Level 3 adds another independent element, often a passphrase or another deliberately separated custody arrangement.

A BIP39 passphrase derives a different wallet. Every passphrase, including a typo, derives a valid wallet. That gives separation, but it also creates another thing that must be entered exactly and recovered.

A passphrase is not multisig. The mnemonic and passphrase are both required to derive that wallet, but the protocol does not enforce two independent signers.

This level only improves the plan when the new element has its own backup, its own location, and a tested family process.

== LEVEL 4: THRESHOLD SIGNING ==

Level 4 uses a threshold policy such as 2-of-3 multisig, either independently or with a collaborative provider.

Two signing keys can authorize a spend and one cannot. Losing one key can be survivable.

The keys are not the whole recovery package. The family also needs the wallet policy or descriptor, script and derivation information, and compatible software or a provider-independent recovery process.

A descriptor cannot sign, but losing the policy can make reconstruction slow, uncertain, or dependent on a provider.

Collaborative custody is only provider-independent when the client truly holds enough keys to meet the threshold, has exported the policy data, and has tested recovery in compatible software without the provider.

== COMPLEXITY CAN BECOME THE BIGGEST RISK ==

A second device, passphrase, multisig, or provider can reduce one failure and create three new ones.

More pieces mean more backups, more updates, more inheritance instructions, and more ways for the written plan to drift from reality.

A single-signature setup maintained and tested well can be safer than a multisig nobody can reconstruct.

== YOUR DECISION ==

Choose the level from the failure you are trying to remove and the process your household can operate.

Then write down why that level fits your household.

"We use Level 2 because we can maintain one hardware-wallet recovery process and accept the single-backup control risk."

Or:

"We use Level 4 because the amount justifies threshold signing and we have tested recovery without the provider."

== PUT IT IN ORANGE PLAN ==

Protect → Protection tier. Save the level, why it fits, and the next review trigger.

Do not put a backup, seed, passphrase, PIN, private key, descriptor, or exact storage location into Orange Plan.

== YOU ARE DONE WHEN ==

The level fits the amount and your family, you can explain the risk you accepted, and you have actually tested the recovery process instead of assuming it works.
