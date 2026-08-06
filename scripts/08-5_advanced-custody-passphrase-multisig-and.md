TELEPROMPTER SCRIPT — segment 8.5
8.5 Advanced custody: passphrase, multisig, and collaborative
1444 words · ~9.3 min at 155 wpm
============================================================

Once you're at Level 3 or 4, "advanced" means removing the single points of failure a single-device, single-seed setup has. Every setup here takes one of those "only ones" and splits it into two. You pay for that in complexity, and in what your family has to be able to do.

== THE THREE PATHS ==

Two definitions:

- Passphrase. An extra word you choose on top of your seed. The wallet doesn't open without both.
- Multisig (multi-signature). The wallet is secured by several separate keys, and more than one has to sign before Bitcoin moves. A common setup is two-of-three: three keys, any two can spend, losing any single one costs nothing.

The three paths:

Path 1: Passphrase single-sig. One seed plus a hidden extra word.

- Best for. A modest stack.
- Buys you. The simplest advanced plan a family can follow.
- Watch out for. A forgotten passphrase locks the funds permanently. No reset mechanism. The passphrase gets its own backup, stored separately from the seed. Practice with a small amount first.

Making the passphrase strong (the 7-word standard).

A passphrase you make up yourself is the weak point of the whole setup. Humans pick quotes, song lyrics, names, and dates, and attackers run exactly those lists first. The fix is randomness you didn't choose:

- Use 7 random words picked from a wordlist by dice or by an offline generator (the diceware method, or a password manager's passphrase generator with the device offline). Not words you thought of. Random means the tool picked them, not you.
- Why 7: each word drawn at random from a standard 7,776-word list multiplies the guesses needed by 7,776. Seven words is roughly 90 bits of entropy, about 1,700,000,000,000,000,000,000,000,000 combinations. A machine guessing a trillion combinations per second would need millions of years. Four or five words is where "pretty good" lives; seven is the floor for money that has to stay safe forever.
- Never: personal facts, quotes, lyrics, addresses, pet names, keyboard patterns, or a password you use anywhere else. If it means something to you, it's guessable.
- Exactness matters. A wallet passphrase is case-sensitive and unforgiving. Record it exactly, letter for letter, on paper or steel. It never gets typed into anything online.
- The same standard covers three things: the wallet passphrase, the password manager's master password, and the encrypted plan-backup passphrase from the walkthroughs. One method, three uses.

The trade-off is built in: a passphrase strong enough to be unguessable is also unrecoverable if lost. That's why it gets its own backup, stored separately from the seed, and why you practice with a small amount first.

Path 2: Collaborative multisig. You hold two keys, a provider holds one, plus the configuration.

- Best for. A meaningful balance, or heirs who aren't technical.
- Buys you. A professional on call to guide them.
- Watch out for. An annual fee and some vendor dependence. The provider's one key can't spend on its own, so they never actually custody your Bitcoin.

How collaborative custody actually works, and why the key count matters. It's a two-of-three: three keys exist, any two can move Bitcoin. You hold two of them. The provider holds the third.

That split produces two properties worth understanding before you decide:

- They can never take your Bitcoin. One key out of a required two spends nothing. They are a co-signer, not a custodian. This is the difference between collaborative custody and an exchange.
- They can never lock you out. You already hold two keys, which is a spending quorum by itself. You do not need their permission or their participation to move your own money.

So what you're actually buying is three things: a key you didn't have to store yourself, a copy of the configuration file held by someone whose job is not losing it, and a human being who will pick up the phone and walk your family through recovery on the worst week of their lives. That third one is the whole reason this path exists.

Before you pick a provider, verify these four:

1. Can you recover with the provider gone? They should hand you the configuration file, or descriptor, and it should work in open-source wallet software they don't control. If the answer is "you'd have to call us," that's a custodian wearing a multisig costume.
2. Is there a documented inheritance process? What exactly happens when your executor calls, and what proof do they require?
3. What's the annual fee, and what happens to your wallet if you stop paying it?
4. What do they require from you, in identity verification and in privacy terms, to open the account?

The honest downside is that you're depending on a company continuing to exist across a timeline measured in decades. That's a real risk. But it's bounded by the key count: the worst case is a provider that vanishes, and you spend an afternoon recovering with your two keys and the config file. Compare that to the DIY worst case, where the person who understood the setup is the one who died.

Path 3: DIY multisig. You hold every key, and the configuration, yourself.

- Best for. Technically proficient people.
- Buys you. Maximum privacy and full independence.
- Watch out for. Your heirs inherit the complexity with no professional to guide them. This path trades your family's recovery odds for your independence.

Compare across four rows:

┄┄ TABLE (REFERENCE — not prompter-readable; the spoken read must be written above this during voice conversion) ┄┄
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

- Decide whether an advanced setup is warranted at all. Staying at a well-run Level 2 is a legitimate answer.
- If you're adding a passphrase, generate it with 7 random words from a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
- If you're considering collaborative custody, ask a provider the four questions and write down their answers before you pay anything.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.
