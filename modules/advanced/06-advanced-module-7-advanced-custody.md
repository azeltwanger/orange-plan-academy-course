# Advanced Module 7 — Advanced Custody

## A7.2 What self-custody actually asks of you

*`TEACH` · 300 words · ~2 min*

> **Gate.** Optional throughout. Watch it if you are weighing whether you want
> the whole job of self-custody, or if the weight of it is what has been
> stopping you. Your custody plan is complete without it.

**By the end of this lesson, you can:**

- Name what self-custody actually transfers to you
- Decide honestly whether you want the whole job, or part of it

---
A client put this better than I ever have.

He said: with self-custody, you are the point of failure. And not just the failure, you're the attack vector. And then he made the point that most of life doesn't work this way. We outsource violence to the police. We outsource security to the banks. That's basically what civilization is, handing off the hard, dangerous jobs to somebody whose job it is.

And Bitcoin asks you to take one of those jobs back.

I think that's right, and it explains why custody feels heavier than the rest of this course. It isn't just another checkbox. It's you accepting a responsibility that, for every other asset you own, somebody else carries for you.

Two things follow from that.

The first one is that it's completely reasonable to not want the whole job. That's what collaborative custody exists for, and it's why a hardened exchange position is a legitimate setup for part of your stack. Taking the job back is a choice, not an obligation.

The second one is that if you do take it, being a little paranoid is appropriate, not a character flaw. You should feel the weight. The people who get hurt are usually the ones who didn't.

### Your decision

**Whether you want the whole job.**

It is completely reasonable not to. That is what collaborative custody exists
for, and it is why a hardened exchange position is a legitimate setup for part
of a stack. Taking the job back is a choice, not an obligation.

## A7.3 Concentration: one institution, one vendor, one firmware
*`TEACH` · ~815 words · ~5 min*

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

### Don't hold it all at one institution

You picked a custody level in the core course. This lesson asks a different question about the same stack: how concentrated is it? Not what type of custody, but how many baskets.

Start with whatever you have not self-custodied yet. How many institutions is it sitting in?

Those 2022 failures weren't self-custody failures. They were concentration failures. The customers who lost everything are the ones who had everything in one place.

So for the custodial part of your stack, your exchange balance, any ETF shares, your retirement exposure, the question is whether one company's bad week can take all of it. I'd add a second institution in three cases. When the custodial amount is big enough that losing access for a few months would change your life. When you're using an exchange balance as your emergency pile, because that job needs a backup for the week the account is frozen. And when the institutions actually fail in different ways, because two exchanges are more correlated with each other than an exchange and a brokerage ETF are.

It costs you something, though, and I don't want to gloss over it. Every extra account is another login, another email to secure, another two-factor setup. Three sloppy accounts are worse than one hardened one. Every extra account is another set of tax lots to reconcile. And every extra account is one more row your executor has to find, so if it doesn't make it onto your Family Custody Map, you've effectively hidden money from your own family.

So the honest rule: self-custody is the real answer to counterparty risk. Splitting across institutions is the hedge for whatever isn't self-custodied yet. Add the second institution when the amount justifies the maintenance, and not before.

### No custody setup is trust-free

There's one more layer, and it's the one people miss, because it sounds like self-custody already solves it. Self-custody removes counterparty risk. It does not remove trust. It moves it.

When you hold your own keys, you're still trusting the company that made your hardware wallet. The firmware running on it, including every version you install after this one. That the device generated your seed with real randomness. And whatever wallet software you use to check your balance and build transactions.

None of that is an argument against self-custody. I self-custody, and I think most people holding a meaningful amount should. It's an argument for being honest about what you're actually relying on, because the thing you never examined is the thing that can take all of it.

So the same concentration question applies here. If every satoshi you own is behind one model of one device, running one company's firmware, generated by one implementation, then one trust is holding up your entire stack. That's the same concentration as keeping everything at one exchange. It's just harder to see, because it feels like independence.

Spreading it out is what protects you from a total loss. A second device from a different manufacturer. A multisig where the keys don't all come from one vendor. Or keeping part of the stack in a different custody model entirely.

Now, I'd slow down here, because more setups is not automatically safer. A second device you don't understand, don't back up, and never test is a new way to lose money, not a hedge. So size this to three things: how comfortable you actually are, how much technical ability you want to use, and how much responsibility you're honestly willing to take on. And if the honest answer is that you can only maintain one setup well, run one setup well and keep it simple. Three setups you half understand is how people lose money.

### Your decision

Two decisions, and either one can honestly come back as "not yet."

Whether your custodial Bitcoin should sit at more than one institution, which you decide from the amount rather than from principle. And whether your self-custodied stack should sit behind more than one vendor, which you decide from what you can genuinely maintain.

If the honest answer to both is that you can run one setup well and that's it, then run one setup well. That is a real answer, not a postponed one.

### Homework

Your homework for this lesson is to:

1. For anything not self-custodied, count the institutions it's sitting in and be honest about whether that number matches what's at stake.
2. Go through what your whole stack is trusting: the device, the manufacturer, the firmware, the wallet software. If one answer covers everything you own, decide whether spreading it out is worth the setup you'd have to maintain.
3. Whatever you add, add it to your Family Custody Map the same day. An account your executor can't find is money you hid from your own family.


## A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
*`TEACH` · ~830 words · ~5 min*

> **Gate.** Watch this before you have made a hundred small transfers, not
> after. It applies if you buy Bitcoin regularly in small amounts, or if your
> wallet already shows a long list of separate chunks under coin control.

**By the end of this lesson, you can:**

- Explain why your balance is a stack of bills rather than a bucket
- Set a transfer threshold against Austin's 0.01–0.02 BTC rule of thumb, and know the fee test the number is protecting
- Decide whether you have a consolidation chore waiting
- Use a fresh receiving address every time, and say why it matters

---

In today's lesson, we're going to cover two operational things about moving Bitcoin that almost nobody explains, and both of them came from clients asking me directly.

### Your wallet is a stack of bills

A client asked me what happens to all the small buys he'd made over the years. His worry was that a bunch of tiny purchases might end up stranded, and that's actually a real thing.

Your wallet isn't a bucket with a balance in it. It's more like a wallet full of bills. Every time Bitcoin lands in your wallet, that deposit is its own separate chunk, and the technical name for one of those chunks is a UTXO, an unspent transaction output. Your balance is the sum of the bills, and when you spend, your wallet grabs one or more whole bills to cover the amount. You spend whole bills, not slices of them.

Now the part that costs money. Every chunk you spend adds to the fee, and that fee doesn't care how big the chunk is. So a very small deposit can become uneconomical to move, because the fee to spend it approaches or exceeds what it's worth. That's what people mean by dust.

If you've been buying small amounts regularly, you can end up with a wallet made of a hundred tiny chunks. Nothing is lost. But the day you go to move it all, you're paying to spend every one of those chunks at once, and if fees are high that day, it gets expensive.

### The two fixes

There are two fixes, one for going forward and one for what you already have.

Going forward, transfer on a threshold rather than on a schedule. Instead of moving every small buy to cold storage the day it happens, let them accumulate on the exchange and move them in one transaction.

My rule of thumb is about 0.01 to 0.02 Bitcoin as a minimum per transfer. Your smaller monthly buys accumulate on the exchange until they hit that threshold, and then they move in one transaction.

The reason behind the number is what to hold onto if fees or the price move a long way from where they are now: you want the fee to spend that chunk later to be a rounding error against the chunk, not a real bite out of it.

The trade-off is real, though, and worth saying out loud. Everything waiting for the threshold is sitting on an exchange, which is exactly the counterparty risk the custody module is about. So the threshold is a fee decision bounded by a custody decision. If the accumulating balance gets big enough to worry you, move it and pay the fee.

For what you already hold, the fix is consolidation. You send those small chunks to yourself in one transaction, which combines them into one bigger chunk. Do it deliberately on a day when fees are low, not on the day you urgently need to move money. It's a chore for a quiet Sunday and an annual custody review item, not an emergency.

### Addresses are public

The second thing is addresses. Another client was surprised to learn that if somebody knows one of your receiving addresses, they can look up the entire history of that address on the blockchain. Bitcoin's ledger is public. That's the whole design.

So if you use the same receiving address over and over, you've handed anyone who has it a running total of everything you've ever received there. That's not a theft risk directly. It's a privacy risk that becomes a personal safety question once somebody can tie an address to your name.

The fix is easy. Use a fresh receiving address every time you receive. Modern wallets generate a new one automatically and it's usually the default, so mostly this is about not overriding it. And don't post an address publicly and then keep using it.

This is also another reason to check the address on the device screen every single time. It should be a new one. If it isn't, find out why before you send.

### Your decision

Your decision here is your transfer threshold, and whether you have a consolidation chore waiting.

### Homework

Your homework for this lesson is to:

1. Open your wallet and look at how many separate chunks your balance is actually made of. Most wallets will show you this; some call it coin control.
2. Write down your transfer threshold. Austin's rule of thumb is 0.01 to 0.02 Bitcoin as a minimum per transfer; check what fees are doing today and confirm that still leaves the fee as a rounding error against the chunk.
3. If you're holding a pile of small chunks, put consolidation on your annual review as a low-fee-day chore.
4. Confirm your wallet is generating a fresh receiving address each time, and that you haven't published one you keep reusing.


## A7.1 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · 1,354 words · ~9 min*

> **Gate.** Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.

**By the end of this lesson, you can:**

- Tell passphrase, collaborative multisig, and DIY multisig apart by what each one buys and costs
- Build a passphrase strong enough to protect a stack (the 7-random-word standard)
- Vet a collaborative-custody provider with four questions
- Back up the multisig config file the way you back up a key

---

Once you're at Level 3 or 4, "advanced" means removing the single points of failure a single-device, single-seed setup has. Every setup here takes one of those "only ones" and splits it into two. You pay for that in complexity, and in what your family has to be able to do.

### The three paths

**Two definitions:**

- **Passphrase.** An extra word you choose on top of your seed. The wallet doesn't open without both.
- **Multisig (multi-signature).** The wallet is secured by several separate keys, and more than one has to sign before Bitcoin moves. A common setup is two-of-three: three keys, any two can spend, losing any single one costs nothing.

**The three paths:**

**Path 1: Passphrase single-sig.** One seed plus a hidden extra word.

- **Best for.** A modest stack.
- **Buys you.** The simplest advanced plan a family can follow.
- **Watch out for.** A forgotten passphrase locks the funds permanently. No reset mechanism. The passphrase gets its own backup, stored separately from the seed. Practice with a small amount first.

**Making the passphrase strong (the 7-word standard).**

A passphrase you make up yourself is the weak point of the whole setup. Humans pick quotes, song lyrics, names, and dates, and attackers run exactly those lists first. The fix is randomness you didn't choose:

- **Use 7 random words** picked from a wordlist by dice or by an offline generator (the diceware method, or a password manager's passphrase generator with the device offline). Not words you thought of. Random means the tool picked them, not you.
- **Why 7:** each word drawn at random from a standard 7,776-word list multiplies the guesses needed by 7,776. Seven words is roughly 90 bits of entropy, about 1,700,000,000,000,000,000,000,000,000 combinations. A machine guessing a trillion combinations per second would need millions of years. Four or five words is where "pretty good" lives; seven is the floor for money that has to stay safe forever.
- **Never:** personal facts, quotes, lyrics, addresses, pet names, keyboard patterns, or a password you use anywhere else. If it means something to you, it's guessable.
- **Exactness matters.** A wallet passphrase is case-sensitive and unforgiving. Record it exactly, letter for letter, on paper or steel. It never gets typed into anything online.
- **The same standard covers three things:** the wallet passphrase, the password manager's master password, and the encrypted plan-backup passphrase from the walkthroughs. One method, three uses.

The trade-off is built in: a passphrase strong enough to be unguessable is also unrecoverable if lost. That's why it gets its own backup, stored separately from the seed, and why you practice with a small amount first.

**Path 2: Collaborative multisig.** You hold two keys, a provider holds one, plus the configuration.

- **Best for.** A meaningful balance, or heirs who aren't technical.
- **Buys you.** A professional on call to guide them.
- **Watch out for.** An annual fee and some vendor dependence. The provider's one key can't spend on its own, so they never actually custody your Bitcoin.

**How collaborative custody actually works, and why the key count matters.** It's a two-of-three: three keys exist, any two can move Bitcoin. You hold two of them. The provider holds the third.

That split produces two properties to weigh before you decide:

- **They can never take your Bitcoin.** One key out of a required two spends nothing. They are a co-signer, not a custodian. This is the difference between collaborative custody and an exchange.
- **They can never lock you out.** You already hold two keys, which is a spending quorum by itself. You do not need their permission or their participation to move your own money.

So what you're actually buying is three things: a key you didn't have to store yourself, a copy of the configuration file held by someone whose job is not losing it, and a human being who will pick up the phone and walk your family through recovery on the worst week of their lives. That third one is the whole reason this path exists.

**Before you pick a provider, verify these four:**

1. **Can you recover with the provider gone?** They should hand you the configuration file, or descriptor, and it should work in open-source wallet software they don't control. If the answer is "you'd have to call us," that's a custodian wearing a multisig costume.
2. **Is there a documented inheritance process?** What exactly happens when your executor calls, and what proof do they require?
3. **What's the annual fee**, and what happens to your wallet if you stop paying it?
4. **What do they require from you**, in identity verification and in privacy terms, to open the account?

The honest downside is that you're depending on a company continuing to exist across a timeline measured in decades. That's a real risk. But it's bounded by the key count: the worst case is a provider that vanishes, and you spend an afternoon recovering with your two keys and the config file. Compare that to the DIY worst case, where the person who understood the setup is the one who died.

**Path 3: DIY multisig.** You hold every key, and the configuration, yourself.

- **Best for.** Technically proficient people.
- **Buys you.** Maximum privacy and full independence.
- **Watch out for.** Your heirs inherit the complexity with no professional to guide them. This path trades your family's recovery odds for your independence.

**Compare across four rows:**

| | Passphrase | Collaborative multisig | DIY multisig |
|---|---|---|---|
| Single point of failure | Still one seed to protect | None (2-of-3) | None (2-of-3) |
| Maintenance load | Lowest | Shared with provider | Highest |
| Heir-friendliness | Good, if documented | Best. Heirs get guided. | Hardest. No help coming. |
| Cost and independence | Free, fully sovereign | Fee plus vendor | Free, fully sovereign |

Look at all four rows before picking. Technical people often stop at row one and end up with something their family can't use.

**Running the table on the same household.** $175,000 of Bitcoin. He's 45 and healthy. Wife has never restored a wallet. Kids are 10 and 12.

- **DIY multisig** wins row one. But it hands a widow and two middle-schoolers a recovery job nobody in the house can do.
- **Collaborative** is a real option, and if the stack triples it's the right one. But they'd be paying an annual fee for a problem they don't have yet.
- **Passphrase path fits.** One seed, one extra word, split between two people. The only path his wife could realistically be walked through in an afternoon.

Match the setup to your family and your stack. Only add complexity when it buys real risk reduction.

### The config file: the multisig piece that gets people killed

The keys hold the money. The **config** is the file that records how those keys connect into one wallet: which keys, the 2-of-3 rule, the technical addresses. That file is the map.

- The keys are the money.
- The config is the only file that says which wallet those keys open.

With the config, your heirs have three seeds in separate locations plus the map. The wallet reassembles. Without it, they can have all three seeds in hand and still be locked out.

Not hypothetical. A man dies with a 2-of-3 multisig holding ~$300,000. Everything right on the keys: three seeds, three separate locations, executor holds one, family finds all three. They recover nothing. $300,000 lost to a missing file.

**The config file's superpower: it's public.** The config has no spending power. Losing it to a thief costs you privacy, not coins. You can back it up aggressively, in a way you'd never back up a seed.

> ⚠ The config file is a recovery dependency. Back it up wherever you back up keys. Keep extra copies. Make sure someone besides you knows it exists.

A collaborative provider holds the config for you. On top of the support, the annual fee is buying the one file your heirs can't reconstruct on their own.


### Building the estate split on each path

The estate module gives you the two tests: can one person spend alone, and can one lost copy permanently stop recovery. What it deliberately doesn't do is show you how to build a setup that passes both, because that's a custody decision. So each path carries the split differently.

On the passphrase path, Anthony Park calls this poor man's multisig, and it works because of how a passphrase behaves. Seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins. So the seed by itself opens a real wallet that's empty, and the passphrase by itself is a word that opens nothing. Two objects, each worthless alone, which is exactly what lets you hand each one to a different person.

Your heir holds the seed. Your executor holds the passphrase. Together they have full access, apart they have nothing. That's test one, passed by design.

Now test two, and this is the trap. Seed plus passphrase is a two-of-two. Both pieces are required every single time. So if the seed card is lost in a fire, the passphrase opens nothing. And if the executor dies without passing the passphrase on, the seed opens an empty wallet. Either one is a total, permanent loss with nobody having done anything wrong. Half of a two-of-two is zero.

Which means each half needs its own backup, on its own side. A second steel copy your heir controls, or one their own successor can reach, never anywhere the passphrase holder can also get to. The passphrase written once, sealed, held by the executor or whoever he names after him, never in the same house or the same safe as the seed.

On the multisig path, a two-of-three vault passes both tests structurally, without you engineering the backups yourself. Any two of the three can spend, so losing one key entirely is survivable, and no single holder can spend alone. Both tests, handled by the arithmetic.

The distribution that makes it work as an estate plan: you hold two keys, so nothing about your day changes and you spend on your own just like today. Your executor holds the third as a sealed seed card, and since one key alone can't spend, they can't touch anything while you're alive. If you're with a collaborative provider, they hold the remaining key and never your seed phrase. After you're gone, your executor and the provider hold two keys between them, which meets the threshold, and the provider verifies who the executor is and walks them through it. Your heirs get a guided recovery instead of a technical exam.

The one thing to get right is where the config file sits. An executor's key stored next to the config file is one step from control, and that quietly turns your two-of-three into a single-key setup. So the config lives in a password manager, never printed, never stored with any physical key.

So with a passphrase you're splitting two different objects between two people. With multisig the keys are already separate, and the job becomes keeping the config away from whoever holds a key. Same principle, different setup.

### Homework

- Decide whether an advanced setup is warranted at all. Staying at a well-run Level 2 is a legitimate answer.
- If you're adding a passphrase, generate it with 7 random words from a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
- If you're considering collaborative custody, ask a provider the four questions and get the answers in writing before you pay anything.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.
