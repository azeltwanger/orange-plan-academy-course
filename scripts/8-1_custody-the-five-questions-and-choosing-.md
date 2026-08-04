TELEPROMPTER SCRIPT — segment 8.1
8.1 Custody: the five questions and choosing your level
1778 words · ~11.5 min at 155 wpm
============================================================

Custody is more than where your Bitcoin sits. It covers whether you can reach it, whether anyone else can, and whether there's a process that still works when you're not around.

It's different from inheritance. Inheritance is the legal transfer (wills, executor, who gets what). Module 8 covers that. This module secures access while you're alive and makes it recoverable if you're not.

In 2022, Celsius customers watched a balance sit on a screen while withdrawals were frozen. Same at BlockFi and FTX. The number was theirs. The Bitcoin was not. A Bitcoin balance in someone else's system is a claim on their Bitcoin, not ownership of yours.

== THE FIVE QUESTIONS ==

Custody comes down to five:

- Where is the Bitcoin held?
- What type of custody are you using?
- Who knows what to do?
- What happens if you're unavailable?
- Where are the single points of failure?

A typical Bitcoin household: he's 45, she's 43, two kids ages 10 and 12. They hold 1.5 BTC on a hardware wallet in a desk drawer, and 0.25 BTC on an exchange.

- Where: they can answer cold. ✓
- What type: one hardware wallet, one exchange account, no passphrase. ✓
- Who knows what to do: he does. She's never touched the device. ✗
- What happens if he's unavailable: nothing. ✗
- Single points of failure: they've never asked. ✗

Two out of five. That's a normal Bitcoin household, not a careless one. The score turns a vague worry into three specific jobs.

== NAME THE JOB BEFORE YOU PICK THE SETUP ==

Different jobs can call for different custody.

For the couple, the 1.5 BTC is long-term cold storage. It's the retirement stack and shouldn't move in a hurry. The 0.25 BTC on the exchange is the buying account — but it's also quietly doing a second job nobody assigned: it's what they'd reach for in an emergency. Different job, different custody answer, because an exchange can freeze an account in exactly the week they need it.

Name the job, so one setup doesn't cover two jobs that need different things.

== THE ONE RULE THIS MODULE RUNS ON ==

You document the process, never the secrets.

By "secrets" I mean the things that actually move Bitcoin: seed phrase (the words your whole wallet rebuilds from), private keys, passphrase, PIN. Anyone with one of those has your Bitcoin.

What you write down: who holds what, what type of setup it is, and what someone should do. Never the words that unlock it. You can share the document with your executor and store it safely, because nothing in it is worth stealing.

== CHOOSING YOUR LEVEL ==

A custody level is how much protection a setup gives you and what it asks back: skill, maintenance, and what your family has to be able to do. The right level matches how much is at stake and who depends on it.

The mistake is a mismatch, in either direction. Celsius customers had too little custody for the amount at stake. Others move a life-changing stack onto a hardware wallet they've never tested, which is more custody than their skill supports. Both cases: the setup doesn't match what's at stake.

== THE FOUR LEVELS ==

Level 1: Hardened exchange or broker. Small stack, or still learning.

- Setup: strong password, app-based 2FA, secured email, withdrawal delays on.
- The word is hardened, not neglected. A small stack on a locked-down exchange is legitimate.

Level 2: Hardware wallet. The default destination once a stack becomes meaningful.

- Setup: seed stays offline, test transaction first, wipe-and-restore proven, backup on steel.
- Removes freeze risk. Hands you maintenance instead.

Level 3: Passphrase plus split access. The stack matters to more than just you.

- Setup: hardened single-sig with a passphrase, a process your spouse or executor can follow, annual review.
- The split makes the setup survivable without you.

Level 4: Collaborative or DIY multisig. For stacks where a single mistake is unacceptable.

- Setup: professional support (collaborative) or full-DIY, coordination with trust and estate plan, family process actually tested.
- Buys you a setup where one mistake no longer ends it.

== SIZING IT ON A REAL HOUSEHOLD ==

The couple holds 1.5 BTC on a hardware wallet and 0.25 BTC on an exchange. At an illustrative $100,000/coin, the hardware wallet is $150,000 and the exchange is $25,000.

The $25,000 is Level 1 money on a Level 1 setup. Honest match, as long as it's hardened.

The $150,000 is Level 3 money. His wife and two kids depend on it. Neither kid is a teenager yet.

Compare against where it's sitting: Level 2, and Level 2 isn't finished (no proven wipe-and-restore, seed still on paper).

Homework: finish Level 2 honestly, then add the split that makes it Level 3. Two jobs, in that order.

== THE APP'S TIER ==

Orange Plan runs three tiers keyed to estate size:

┄┄ TABLE — on screen, speak the pattern, don’t read the cells ┄┄
| Tier | Net worth |
|---|---|
| Foundation | Under $500k |
| Substantial | $500k to $2M |
| High Net Worth | Above $2M |
┄┄ end table ┄┄

The tier filters the security checklist so a Foundation household isn't held to the hardware items a high-net-worth household is.

Two dials work together: your custody level (your call, based on skills and family) and the app's tier (which checklist items you're held to, based on what's at stake).

== CUSTODY IS NOT A PURITY TEST ==

The right setup is one you can maintain, explain, and recover from. A simple setup your family can actually use beats an advanced one nobody understands.

You'll hear people say real Bitcoiners self-custody everything, immediately. That claim is wrong. You move up a level by earning it, with skill and with need, not with ideology.

== ADVANCED SETUPS: PASSPHRASE, MULTISIG, COLLABORATIVE ==

Once you're at Level 3 or 4, "advanced" means removing the single points of failure that a single-device, single-seed setup has. Advanced setups take one of those "only ones" and split it into two. You pay for that in complexity and what your family has to be able to do.

Two definitions:

- Passphrase. An extra word you choose on top of your seed. The wallet doesn't open without both.
- Multisig (multi-signature). The wallet is secured by several separate keys, and more than one has to sign before Bitcoin moves. A common setup is two-of-three: three keys, any two can spend, losing any single one costs nothing.

The three paths:

Path 1: Passphrase single-sig. One seed plus a hidden extra word.

- Best for. A modest stack.
- Buys you. The simplest advanced plan a family can follow.
- Watch out for. A forgotten passphrase locks the funds permanently. No reset mechanism. The passphrase gets its own backup, stored separately from the seed. Practice with a small amount first.

Path 2: Collaborative multisig. You hold two keys, a provider holds one, plus the configuration.

- Best for. A meaningful balance, or heirs who aren't technical.
- Buys you. A professional on call to guide them.
- Watch out for. An annual fee and some vendor dependence. The provider's one key can't spend on its own, so they never actually custody your Bitcoin.

Path 3: DIY multisig. You hold every key, and the configuration, yourself.

- Best for. Technically proficient people.
- Buys you. Maximum privacy and full independence.
- Watch out for. Your heirs inherit the complexity with no professional to guide them. This path trades your family's recovery odds for your independence.

Compare across four rows:

┄┄ TABLE — on screen, speak the pattern, don’t read the cells ┄┄
| | Passphrase | Collaborative multisig | DIY multisig |
|---|---|---|---|
| Single point of failure | Still one seed to protect | None (2-of-3) | None (2-of-3) |
| Maintenance load | Lowest | Shared with provider | Highest |
| Heir-friendliness | Good, if documented | Best. Heirs get guided. | Hardest. No help coming. |
| Cost and independence | Free, fully sovereign | Fee plus vendor | Free, fully sovereign |
┄┄ end table ┄┄

Look at all four rows before picking. Technical people often stop at row one and end up with something their family can't use.

Running the table on the same household. $175,000 of Bitcoin. He's 45 and healthy. Wife has never restored a wallet. Kids are 10 and 12.

- DIY multisig wins row one. But it hands a widow and two middle-schoolers a recovery job nobody in the house can do.
- Collaborative is a real option, and if the stack triples it's the right one. But they'd be paying an annual fee for a problem they don't have yet.
- Passphrase path fits. One seed, one extra word, split between two people. The only path his wife could realistically be walked through in an afternoon.

Match the setup to your family and your stack. Only add complexity when it buys real risk reduction.

== THE CONFIG FILE: THE MULTISIG PIECE THAT GETS PEOPLE KILLED ==

The keys hold the money. The config is the file that records how those keys connect into one wallet: which keys, the 2-of-3 rule, the technical addresses. That file is the map.

- The keys are the money.
- The config is the only file that says which wallet those keys open.

With the config, your heirs have three seeds in separate locations plus the map. The wallet reassembles. Without it, they can have all three seeds in hand and still be locked out.

Not hypothetical. A man dies with a 2-of-3 multisig holding ~$300,000. Everything right on the keys: three seeds, three separate locations, executor holds one, family finds all three. They recover nothing. $300,000 lost to a missing file.

The config file's superpower: it's public. The config has no spending power. Losing it to a thief costs you privacy, not coins. You can back it up aggressively, in a way you'd never back up a seed.

A collaborative provider holds the config for you. On top of the support, the annual fee is buying the one file your heirs can't reconstruct on their own.

== HOMEWORK ==

- Score yourself on the five questions. Write down the number. For most people it's one or two.
- Write down which level you're at today and which level your amount and family say you should be at.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.

The next lesson covers the hardware wallet setup and the recovery test.
