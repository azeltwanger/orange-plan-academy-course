TELEPROMPTER SCRIPT — Advanced A5.1
A5.1 Decide whether a passphrase solves a real problem
~8 min at 155 wpm · VOICE-MATCHED DRAFT — Austin review + custody review pending
============================================================

> **Watch this only if a tested single-signature wallet still has a specific privacy, discovery, or access-control problem that a passphrase may solve. Otherwise keep the simpler recovery-ready setup.**

The question is not, “Is a passphrase more secure?”

It can reduce one risk and create another.

The useful question is: **what exact failure are we solving, and can the household recover both required pieces for decades?**

== WHAT A PASSPHRASE ACTUALLY DOES ==

A wallet passphrase is not a PIN and it is not a label attached to one existing wallet.

Under supported wallet designs, the backup words plus an exact passphrase derive one wallet. The same backup plus a different passphrase derives another valid wallet.

There is no central record telling the device which passphrase was intended.

A missing character, different capitalization, extra space, or different word can open a different wallet rather than display “wrong password.”

The manufacturer cannot reset it.

That is both the protection and the danger.

== WORK THE TWO-SIDED EXAMPLE ==

The demo household has already proven that its ordinary backup restores the expected hardware-wallet addresses.

Now imagine someone finds a copy of those backup words.

Without a passphrase, the finder may have enough information to recreate the wallet and move the Bitcoin.

With a correctly designed passphrase wallet, the backup words alone open a different wallet and do not reveal the passphrase-protected balance.

That is the risk the passphrase can reduce: discovery of one backup is no longer automatically discovery of the main wallet.

Now reverse the problem.

Alex dies. Jordan has the correct backup words but cannot find the exact passphrase. Jordan restores the words, sees an empty or decoy wallet, and has no way to know whether the main passphrase is missing, mistyped, or remembered incorrectly.

The same control that stopped the thief can permanently stop the family.

A passphrase is not free security. It changes the custody design from one required secret to at least two required components.

== DO NOT USE MEMORY AS THE BACKUP ==

A passphrase that exists only in the owner's memory is a single point of failure.

A phrase that is easy to remember can also be easier to guess, especially when it uses names, quotes, dates, addresses, or facts about the owner.

The generation method and strength need device-neutral custody review. The durable course rule is:

- use a supported method with sufficient randomness,
- record the exact value without interpretation,
- keep it offline under the custody plan,
- and do not rely on memory as the only copy.

Orange Plan records that a passphrase is part of the process. It never receives the passphrase.

== SEPARATION AND REDUNDANCY ARE BOTH REQUIRED ==

Keeping the passphrase beside the backup words defeats much of the separation benefit.

Keeping only one copy of each creates a fragile two-of-two system: lose either required component and the wallet may be unrecoverable.

The design needs to answer:

- Who can reach the backup words?
- Who can reach the passphrase when legally authorized?
- What physical event could destroy both?
- What happens if one person dies, divorces, moves, or becomes unavailable?
- How is a successor brought into the process?

Do not improvise the legal inheritance design by handing one secret to an heir and the other to an executor without attorney and custody review. Key possession and legal authority are different questions.

== BUILD A PRACTICE WALLET FIRST ==

Before changing the main wallet, create a small passphrase-protected practice wallet using the exact device class and recovery process being considered.

Prove four things:

1. The ordinary backup without the passphrase opens the expected non-passphrase wallet.
2. The exact passphrase opens the intended passphrase wallet.
3. A small receive and send work from that wallet.
4. Another required person can follow the process without the main secret appearing in the instruction document.

Then repeat the recovery from a clean or compatible device using the manufacturer's current procedure.

The test is not complete because the owner can type the passphrase from memory on the device already configured for it.

== DECIDE WHETHER THE PROBLEM IS LARGE ENOUGH ==

A passphrase may make sense when:

- one discovered backup would otherwise expose a life-changing balance,
- the household has a real privacy or physical-access concern,
- the custody setup and device support it cleanly,
- and the family can maintain the second component.

It may be the wrong answer when:

- the household is still struggling with ordinary backup recovery,
- only one person understands the wallet,
- the passphrase would exist only in memory,
- or a collaborative multi-key design would solve the actual family problem more cleanly.

I would rather have a simple setup the family has proven than a more sophisticated setup nobody else can recover.

== WHERE READINESS COMES FROM ==

**What it means:** whether backup plus exact passphrase can recreate, verify, and spend from the intended wallet under the family process.

**Calculated from:** no app calculation. It comes from the supported recovery test and component map.

**Edit source:** the real custody design, people, locations, and test date.

**This affects:** loss risk, theft risk, family recovery, estate coordination, and the custody level recorded in Protect.

== YOUR DECISION ==

Choose whether the passphrase solves a named risk, how both components are backed up and separated, and who must prove recovery.

== PUT IT IN ORANGE PLAN ==

Record the custody type, component roles at a process level, people, review date, and successful test. Never enter the backup words, passphrase, PIN, or private key.

== YOU ARE DONE WHEN ==

The household can state the risk the passphrase removes, the new loss path it creates, and has successfully recovered a practice wallet with the exact two-component process.

**Return to Core:** update the Family Custody Map and single-point-of-failure review only after the design has been tested.
