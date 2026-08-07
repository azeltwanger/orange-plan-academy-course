# Unit 8 · Module 7 — Custody

*Custody as operational protection: choose your level on the four-tier ladder, set up hardware with a proven recovery test, close single points of failure, and — when it fits — go advanced with passphrase, multisig, or collaborative custody.*

## 8.1 Custody: the 5 questions
*`TEACH` · 2,050 words · ~13 min*

**By the end of this lesson, you can:**

- Score your household against the five custody questions
- Match your custody level (1-4) to your stack and family
- Name what each level buys you and what it costs you
- Decide whether your custodial Bitcoin should sit at more than one institution
- Apply the never-document-the-secrets rule

---

Custody is more than where your Bitcoin sits. It covers whether you can reach it, whether anyone else can, and whether there's a process that still works when you're not around.

It's different from inheritance. Inheritance is the legal transfer (wills, executor, who gets what). Module 8 covers that. This module secures access while you're alive and makes it recoverable if you're not.

In 2022, Celsius customers watched a balance sit on a screen while withdrawals were frozen. Same at BlockFi and FTX. The number was theirs. The Bitcoin was not. A Bitcoin balance in someone else's system is a claim on their Bitcoin, not ownership of yours.

### The five questions

Custody comes down to five:

- Where is the Bitcoin held?
- What type of custody are you using?
- Who knows what to do?
- What happens if you're unavailable?
- Where are the single points of failure?

A typical Bitcoin household: he's 45, she's 43, two kids ages 10 and 12. They hold 1.5 BTC on a hardware wallet in a desk drawer, and 0.25 BTC on an exchange.

- **Where:** they can answer cold. ✓
- **What type:** one hardware wallet, one exchange account, no passphrase. ✓
- **Who knows what to do:** he does. She's never touched the device. ✗
- **What happens if he's unavailable:** nothing. ✗
- **Single points of failure:** they've never asked. ✗

Two out of five. That's a normal Bitcoin household, not a careless one. The score turns a vague worry into three specific jobs.

### Name the job before you pick the setup

Different jobs can call for different custody.

For the couple, the 1.5 BTC is long-term cold storage. It's the retirement stack and shouldn't move in a hurry. The 0.25 BTC on the exchange is the buying account — but it's also quietly doing a second job nobody assigned: it's what they'd reach for in an emergency. Different job, different custody answer, because an exchange can freeze an account in exactly the week they need it.

Name the job, so one setup doesn't cover two jobs that need different things.

### The one rule this module runs on

**You document the process, never the secrets.**

By "secrets" I mean the things that actually move Bitcoin: seed phrase (the words your whole wallet rebuilds from), private keys, passphrase, PIN. Anyone with one of those has your Bitcoin.

> ⚠ No seed phrases, no private keys, no passphrases, no PINs. In any app, document, photo, cloud note, or AI tool. Ever.

What you write down: who holds what, what type of setup it is, and what someone should do. Never the words that unlock it. You can share the document with your executor and store it safely, because nothing in it is worth stealing.

## 8.2 Choosing your custody level
*`TEACH` · ~1,250 words · ~8 min*

**By the end of this lesson, you can:**

- Match a custody level to your stack and your family
- Name what each level buys you and what it costs
- Decide whether custodial Bitcoin should sit at more than one institution
- Spot the moment a price run-up outgrows your setup

---

You know where your gaps are from the 5 questions. Now: what setup should you be running at all?

### Choosing your level

A custody level is how much protection a setup gives you and what it asks back: skill, maintenance, and what your family has to be able to do. The right level matches how much is at stake and who depends on it.

The mistake is a mismatch, in either direction. Celsius customers had too little custody for the amount at stake. Others move a life-changing stack onto a hardware wallet they've never tested, which is more custody than their skill supports. Both cases: the setup doesn't match what's at stake.

### The four levels

**Level 1: Hardened exchange or broker.** Small stack, or still learning.

- Setup: strong password, app-based 2FA, secured email, withdrawal delays on.
- The word is hardened, not neglected. A small stack on a locked-down exchange is legitimate.

**Level 2: Hardware wallet.** The default destination once a stack becomes meaningful.

- Setup: seed stays offline, test transaction first, wipe-and-restore proven, backup on steel.
- Removes freeze risk. Hands you maintenance instead.

**Level 3: Passphrase plus split access.** The stack matters to more than just you.

- Setup: hardened single-sig with a passphrase, a process your spouse or executor can follow, annual review.
- The split makes the setup survivable without you.

**Level 4: Collaborative or DIY multisig.** For stacks where a single mistake is unacceptable.

- Setup: professional support (collaborative) or full-DIY, coordination with trust and estate plan, family process actually tested.
- Buys you a setup where one mistake no longer ends it.

### Every level is a trade

There is no custody setup without a trade-off. Each level buys one protection by handing you a different risk to manage:

| Level | What it buys | What it costs |
|---|---|---|
| 1 · Hardened exchange/ETF | Convenience, easy inheritance, no self-responsibility | Counterparty risk. The account can be frozen exactly when you need it |
| 2 · Hardware wallet | Removes freeze risk. True ownership | Maintenance and self-responsibility. One seed is one point of failure |
| 3 · Passphrase + split | Theft protection, survivable without you | More complexity. A lost passphrase is a permanent loss |
| 4 · Multisig | No single mistake can end it | Highest complexity. Config-file dependence, a fee (collaborative) or heirs' complexity (DIY) |

The pattern: more sovereignty always means more responsibility, and more convenience always means more counterparty risk. You never eliminate risk, you choose which risks you hold and which you hand to someone else. That's why the level is matched to stakes and skill instead of picked on ideology.

### Don't hold it all at one institution

Everything above is about *what type* of custody. There's a second question that applies to whatever you have not self-custodied: **how many institutions is it sitting in?**

Celsius, BlockFi, and FTX weren't a self-custody failure. They were a concentration failure. Customers who lost everything had everything in one place.

So for the custodial portion of your stack, the exchange balance, the ETF shares, the retirement-account exposure, the question is whether one company's bad week can take all of it.

**When splitting across institutions earns its keep:**

- The custodial amount is large enough that losing access for months would change your life.
- You're using an exchange balance as an emergency-reachable pile. That job needs an alternative when the account is frozen.
- The institutions genuinely fail in different ways. Two exchanges are more correlated than an exchange and a brokerage ETF, which are more correlated than either and a hardware wallet.

**What it costs you, and this is not small:**

- Every extra account is another login, another email to secure, another 2FA to protect. Three sloppy accounts are worse than one hardened one.
- Every extra account is another set of tax lots to track and reconcile in the tax module.
- Every extra account is another row your executor has to find. It has to land on the Family Custody Map, or you've hidden money from your own family.

**The honest rule:** self-custody is the real answer to counterparty risk, and splitting across institutions is the hedge you use for whatever isn't self-custodied yet. Add the second institution when the amount justifies the maintenance, not before. A small stack on one hardened exchange is a legitimate setup, and adding accounts to it just adds surface area.

### Sizing it on a real household

The couple holds 1.5 BTC on a hardware wallet and 0.25 BTC on an exchange. At an illustrative $100,000/coin, the hardware wallet is $150,000 and the exchange is $25,000.

The $25,000 is Level 1 money on a Level 1 setup. Honest match, as long as it's hardened.

The $150,000 is Level 3 money. His wife and two kids depend on it. Neither kid is a teenager yet.

Compare against where it's sitting: Level 2, and Level 2 isn't finished (no proven wipe-and-restore, seed still on paper).

Homework: finish Level 2 honestly, then add the split that makes it Level 3. Two jobs, in that order.

### The app's tier

Orange Plan runs three tiers keyed to estate size:

| Tier | Net worth |
|---|---|
| **Foundation** | Under $500k |
| **Substantial** | $500k to $2M |
| **High Net Worth** | Above $2M |

The tier filters the security checklist so a Foundation household isn't held to the hardware items a high-net-worth household is.

Two dials work together: your custody level (your call, based on skills and family) and the app's tier (which checklist items you're held to, based on what's at stake).

### Custody is not a purity test

The right setup is one you can maintain, explain, and recover from. If your family can't actually use it, the advanced version isn't protecting anything.

You'll hear people say real Bitcoiners self-custody everything, immediately. That claim is wrong. You move up a level by earning it, with skill and with need, not with ideology.

### Advanced setups: passphrase, multisig, collaborative

Once you're at Level 3 or 4, "advanced" means removing the single points of failure that a single-device, single-seed setup has. Advanced setups take one of those "only ones" and split it into two. You pay for that in complexity and what your family has to be able to do.

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

That split produces two properties worth understanding before you decide:

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

### Homework

- Score yourself on the five questions. For most people the answer is one or two.
- Name the level you're at today and the level your amount and your family say you should be at. If those differ, that gap is the module's whole job.
- For anything not self-custodied, count the institutions it sits in and ask whether that number matches what's at stake.


## 8.3 The hardware wallet and the recovery test
*`TEACH` · 678 words · ~5 min*

**By the end of this lesson, you can:**

- Set up a hardware wallet safely from scratch
- Never leak the seed phrase, ever
- Perform a wipe-and-restore recovery test
- Consolidate small transactions when fees are low

---

A seed backup is only as good as your ability to actually restore from it. This lesson walks through the setup, then the recovery test that proves the backup works before serious money depends on it.

### Where your Bitcoin actually lives

Your Bitcoin isn't on the device. When you set up a hardware wallet, it generates a **seed phrase** (12 or 24 words), and every key to your Bitcoin is derived from those words. The device is a safe place to use them.

- The device is replaceable.
- The seed is not.

If the device breaks, you rebuild the wallet on a new device from the seed. If the seed is wrong, a broken device is the end of the stack.

Most hardware wallets wipe themselves after a set number of wrong PIN entries. Right feature (stops a thief guessing their way in). Also means your entire stack lives on the paper backup. The device can erase itself on a Tuesday afternoon, and that paper becomes the only copy.

### The six-step setup

1. **Buy the device directly from the manufacturer.** Never used, never third-party. A device someone else touched can arrive with a seed they already know.
2. **Generate a brand-new wallet on the device itself.** The seed is created by the device and has never existed anywhere else.
3. **Write the seed down offline. Set a PIN.**
4. **Send a small test transaction to the wallet.** About 0.01 BTC (~$1,000). Small enough that losing it is survivable, big enough that you take it seriously.
5. **Wipe the device.** Factory reset, on purpose, with that $1,000 sitting on it. This is where most people stop short.
6. **Restore from your written seed** and confirm the test transaction reappears.

The wipe proves three things at once: the seed was written correctly, you know the procedure under calm conditions, and the backup works.

- If the restore works, the $150,000 stays where it is and you've proven the backup.
- If it fails, you find out with $1,000 at risk instead of $150,000.

### The never list

> ⚠ Never type your seed words into a computer, phone, website, screenshot, photo, or AI chat. Ever. Never buy a used or third-party device.

The seed exists on paper or steel, offline, and nowhere else. Anything with a screen and a network connection can be read.

Paper degrades and burns. For a meaningful stack, seed goes on steel, and backups live in separate locations.

### Moving coin well: UTXOs and sweep thresholds

Every transfer into your wallet creates a **UTXO** (unspent transaction output). Think of it as a separate bill in your wallet. Your balance is the sum of the bills, and you spend whole bills, not slices.

Send 10 small buys in, and you're holding 10 small bills. Really small ones are called dust because the fee to move them can approach or exceed what they're worth. Either way, holding many small UTXOs raises what it costs to move your Bitcoin later.

Network fees depend on how many bills you're spending, not how much they're worth. A fee that's trivial against a large bill can eat a meaningful slice of a small one.

**Sweep on a threshold, not a schedule.** Rule of thumb: ~0.01 to 0.02 BTC as a minimum per transfer. Smaller monthly buys accumulate on the exchange to the threshold, then move in one transaction.

If you already have a pocketful of small bills, **consolidation** is the fix. Combine many small pieces into one in a single transaction, best done when network fees are low. Annual custody review item. Maintenance, not an emergency.

### Homework

If you've never done the wipe-and-restore, watch the demo lesson and do it, with a small test amount, before serious money is on the line.


## 8.4 Close the doors: single points of failure, hardening, and scams
*`TEACH` · 777 words · ~6 min*

> ✅ **Fixed in course:** stale hand-off promised "advanced custody" next — that
> material lives in 8.1; now points at the external demo.

**By the end of this lesson, you can:**

- Identify the three shapes of a single point of failure
- Run the nine-question hunt against your own setup
- Harden exchange and email accounts against real attacks
- Recognize the pattern behind Bitcoin scams

---

### Three shapes of a single point of failure

Anything that exists only once, where losing it means the Bitcoin is unreachable. Three shapes:

1. **The thing gets destroyed.** Device, backup.
2. **The thing is fine, and the person is unavailable.** Only one person knows the process.
3. **You and your Bitcoin are both fine, and the custodian won't let you move it.** An exchange freezes an account.

Most people count devices and forget custodians.

### Three ordinary Tuesdays

The couple: one hardware wallet in a desk drawer, one paper seed backup in the same house, 0.25 BTC on an exchange with SMS 2FA, wife who has never restored a wallet.

- **The house floods.** Device and only seed backup are in the same building. About $150,000 of Bitcoin goes with the drywall. Two copies in one location aren't really two copies.
- **He's hospitalized for six weeks.** Nothing stolen, nothing lost, but nothing can move either. She can't sell a dollar of it or tell anyone what exists.
- **The exchange freezes his account during a review.** $25,000 unreachable for however long the review takes.

Three ordinary events, no hackers involved. The failure that loses Bitcoin is almost always one thing without a backup.

### The nine-question hunt

For each row, ask: is there only one?

1. Only one device.
2. Only one seed backup.
3. Only one location.
4. Only one person who knows everything.
5. One weak exchange login.
6. One heir with no idea what exists.
7. A document that contradicts your beneficiaries.
8. A passphrase nobody else can recover.
9. Multisig keys all sitting in one place.

The couple checks six of nine. Not careless. A normal setup collects "only ones" on its own, because nothing ever asked.

### The fix method

1. List your top three, ranked by what the loss would cost, not by how easy each one is to fix.
2. Pick the one at the top.
3. Fix that one, and only that one.
4. Re-check and repeat.

For the couple, top item is the seed backup and device sharing an address. Fix: a steel backup stored somewhere else (in-laws, safe deposit box, second property). One afternoon.

Next: the hospital scenario, which is a person problem. She needs to have restored a wallet once with a small amount, so the procedure lives in two heads.

Every "only one" turns into one of three things: a backup, a second location, or a second person who knows the process. Never the secrets.

### Account hardening

A couple years ago, someone called Austin's bank pretending to be him and tried to move ~$10,000. They didn't get it. But that's the day he moved his exchange and email logins onto physical keys.

Most real-world losses look like this. Nobody breaks the encryption on your Bitcoin. They log in as you.

**The order matters:**

1. **Secure the email account first.** Your email is the master key. Every other account resets its password to that inbox on request.
2. Strong, unique password on every account.
3. App-based 2FA (not SMS), with the authenticator's cloud backup off.
4. Withdrawal delays and allowlists on. Never click login links from an email or DM.

**The SIM swap trap.** SMS 2FA has a specific weakness: someone talks your carrier into moving your number onto their SIM. From that moment, your texts arrive on their phone. A SIM swap takes the exchange and the email in one afternoon.

**Hardware keys beat authenticator apps.** A physical security key is bound to the real site's address and checks it before signing. A lookalike site doesn't get a response, which takes phishing off the table. Cheapest upgrade in this lesson.

### The scam rules

> ⚠ Urgency is the red flag. No real company ever asks for your seed. "Send 1, get 2 back" is always a scam.

- Call says your account is hacked? Hang up and contact the provider yourself.
- Guaranteed returns are a scam.

Urgency is the common thread. Every scam needs you to act before you think. When something feels urgent, close the app and slow down. That habit alone catches scams you've never seen before.

### Homework

Make your own "only one" list, pick the one at the top, and fix it this week. Not all nine. Just that one.


## 8.5 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · 1,354 words · ~9 min*

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

That split produces two properties worth understanding before you decide:

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

### Homework

- Decide whether an advanced setup is warranted at all. Staying at a well-run Level 2 is a legitimate answer.
- If you're adding a passphrase, generate it with 7 random words from a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
- If you're considering collaborative custody, ask a provider the four questions and get the answers in writing before you pay anything.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.


## 8.6 External demo: hardware wallet setup + exchange hardening
*`DEMO` · 877 words*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **8.7**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

> ❓ **Decision needed (item 24):** this read text is a *shooting script* —
> "review your footage before publishing," "if it fails, retake," staging/blur
> instructions. Producer-facing, not learner-facing. Once the video exists,
> decide whether this text is replaced with a learner summary or kept as-is.

**By the end of this lesson, you can:**

- Follow a hardware wallet setup end-to-end, from box to first restore
- Harden an exchange account in the right order
- Understand what to record and what never to record

---

About a 9-minute screen-record demo. Not Orange Plan. Vendor tools only.

This is the one lesson where the app never opens. The procedure: hardware wallet from box to first restore, plus the exchange settings that stop most losses. The custody map walkthrough is where all of this becomes a checked box.

Set aside about 20 minutes to run through it. Have:

- A manufacturer-direct hardware wallet, still sealed.
- A throwaway demo wallet with trivial funds.
- A demo exchange account you're willing to burn. Separate from anything real.
- Something to stage or blur the seed display: tape, a physical shield, or a tested camera angle.

Production safety is the whole job. Never let a real seed, a QR of a seed, or a PIN entry pattern reach the frame. Review your footage before publishing for stray reflections, second monitors, or a phone screen in the shot.

Because nothing in this lesson touches the app, it doesn't age with the app. Record it once, keep it forever.

### Step 1: Hardware wallet, the six steps (~5:30)

Vendor device plus vendor app. Six ordered beats:

| # | Beat | What actually happens |
|---|---|---|
| 1 | Buy direct from the manufacturer. | Never used, never third-party. A used or third-party device may have already been compromised. |
| 2 | Generate a new wallet on the device. | The seed comes from the device's own randomness. You never type a seed you got from anywhere else. |
| 3 | Write the seed offline, set a PIN. | Show the act (hand on paper or steel) but never the words. Then the PIN entry, with no pattern on screen. |
| 4 | Send a small test transaction. | Trivial amount, in and out. Enough to have a real on-chain record. |
| 5 | Wipe the device. | The scary step. Factory reset the device you just set up. This is where most people back out, and it's the whole reason to do it on a throwaway. |
| 6 | Restore from seed and confirm the test transaction reappears. | Type the words back in from the offline copy. If the balance and history return, the seed is real. If they don't, the seed backup was theatre. The wipe surfaces the problem while only a trivial amount is at stake. |

When the balance reappears: only now has this device earned real money.

> ⚠ The seed word display, the PIN entry, and the restore input screens are the three moments the camera should never see directly. Stage them, blur them, or turn away. A single frame catching the seed is a lifetime of exposure.

### Step 2: Exchange hardening (~2:30)

Generic exchange settings. Name vendors as examples, not endorsements. Four ordered beats:

| # | Beat | Why it's on the list |
|---|---|---|
| 1 | Strong unique password. | Password reuse is how one leaked breach becomes every account. A password manager is fine here (it's not a wallet). |
| 2 | Two-factor auth off SMS, onto an authenticator app or physical security key. | SIM-swap is the boring attack that keeps working. |
| 3 | Secure the email account first. | The email account is the master key. Reset flows on every exchange route through it. Harden the email before the exchange. |
| 4 | Withdrawal delays and allow-listing on. | Delays give an attacker no fast path to move funds out. Allow-listing means even a session takeover can only send to your own destinations. |

Say the frame out loud: most losses are account takeovers, not broken cryptography. The math on Bitcoin isn't what gets attacked. The account you access it through is.

### Step 3: The never-list (~1:00)

Camera, no screen. Four sentences, said plainly:

- Never type seed words into a computer, phone, website, screenshot, or AI chat.
- Never buy a used or third-party device.
- Urgency is the red flag. Close the app and slow down.
- No real company ever asks for your seed.

Everything else in this space is a variation on those four.

### What good looks like

- The restore step actually completes on camera. Test transaction reappears in balance and history. If it fails, retake.
- Every seed frame is staged or blurred. Watch the footage.
- The hardening walk names the email account first. Order matters.
- The never-list gets said to the camera, not to a screen. No UI in that shot.

### Handing it off

The custody-map walkthrough is where this demo becomes a checked box. Three of the checklist items exist specifically to prove you did what this demo taught: recovery tested, backup verified, signing device tested recently. Check them only if you actually ran the demo. An unchecked item is honest. A checked item that never happened is dangerous, because the plan now believes something untrue.

## 8.7 Walkthrough: document your custody map in Orange Plan
*`DEMO` · 1,718 words · ~8 min*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **8.7**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Walk the custody checklist in the app honestly, tier by tier
- Fill out a Family Custody Map with zero secrets on it
- Export an encrypted backup of the plan itself
- Record your top single point of failure and this week's fix

---
This walkthrough turns your custody decisions into an on-screen map. Checklist honest, tier confirmed, top single point of failure named, and an encrypted backup of the plan itself.

Set aside about 15 minutes to run it slowly the first time. Have your custody level from the custody-level lesson in mind, and know whether your dead-man switch will need cloud sync.

Zero secrets on screen. The checklist doesn't ask for any. Every item is a checkbox. The only free-text moment in this whole walkthrough is a backup passphrase prompt in Step 3, and you'll know exactly what it is before you type.

### Pre-flight (before you open Protect)

Two things to check so the walkthrough doesn't stall:

⚠ Tier is keyed to estate net worth, not your custody choice. Protect renders only the current tier's checklist items:

- **Foundation** ($0 to $500,000).
- **Substantial** ($500,000 to $2 million).
- **High Net Worth** ($2 million or more).

The three **Hardware** items only exist at Substantial and above. If your net worth lands at Foundation, that group is simply absent.

⚠ Storage mode matters for Module 8's dead-man switch. In **Local Only**, the switch panel replaces itself with *"Automatic check-in emails require cloud sync."* Heir letter, beneficiaries, and the checklist still work locally. But if you plan to arm the switch next module, flip to Cloud at **Settings → Data & Privacy** now.

### Step 1: Orient on Protect

**Protect** (primary nav). Page heading: **Protect**.

Read the top strip:

- Eyebrow **Estate readiness → {n} of 5 essentials in place**.
- Five segments across the bar: **Dead man's switch, Heir letter, Protection tier, Checklist, Beneficiaries**.
- Below the bar: **Next: {action} · start →**. The app naming the next single fix.

Below that is the **Needs attention** queue. One row per incomplete essential, each with its own action. The queue enforces the fix-one-thing method: always the next essential, one action each.

⚠ Two different "checklist" strings live on Protect. The segment on the readiness bar says **Checklist**. The row inside Needs attention says **Security checklist**. Both are real. Use the right one for the surface you're pointing at.

### Step 2: Walk the checklist as the map

**Protect → Needs attention → Security checklist row → Open checklist**.

The panel opens with your tier label:

*"{n} of {n} for your tier. Substantial ($500K–$2M). Items name outcomes; any custody model can satisfy them."*

Four groups, each headed *"{group} · {n} of {n}"*:

| Group | Items | What it covers |
|---|---|---|
| Hardware | 3 | Recovery tested, backup verified, storage documented (Substantial and above only). |
| Distribution | 4 | No single point of failure. Locations, people, devices. |
| Legal | 6 | Will, powers, custody instructions. |
| Access after death | 4 | The Module 8 handoff. |

17 items total at Substantial. Each item has a **How** toggle for custody-model-neutral guidance. Checked items render struck through.

⚠ The top unchecked item is this week's fix, not the whole list. This checklist is a map you audit and repair one item at a time, not a to-do you run in an afternoon.

The recovery-test callback, verbatim from the app:

- *Full recovery process tested end-to-end*
- *Backup seed verified readable*

Those only get checked if you actually did the wipe-and-restore. A checked item that never happened is dangerous, because the plan now believes something untrue.

The single-point-of-failure callback:

- *Storage locations documented. Hints only, no exact details*
- *No single point of failure can destroy access (one device, one location, one person)*

⚠ There are no free-text fields anywhere in the checklist. It's checkboxes plus the "How" toggles. Never write secrets down in the app. The only free-text estate fields in the whole app live in Module 8's heir-letter dialog, and that dialog carries its own red warning banner.

### Step 3: Back up the plan itself

**Settings → Data & Privacy → Data & backups → Backup & Restore → Export Plan**.

Panel copy: *"Export your entire plan as an AES-encrypted restore backup file protected by a passphrase."*

⚠ Clicking **Export Plan** opens a browser passphrase prompt in plaintext. The prompt reads *"Enter a passphrase to encrypt your Orange Plan export."* This is a native browser prompt, visible on screen. It's a backup-file passphrase, not a wallet passphrase. Two different objects with two different jobs, both built to the 7-random-word standard from the advanced-custody lesson. Type it somewhere private, or use an obvious throwaway you can discard.

Success toast: **Plan exported**.

The sibling **Data Privacy** panel on this same page shows the mode: **Cloud** or **Local Only**.

The rest of the module was about protecting the coins. This one button protects the map. In Local Only mode, this file is your only backup, because there's no cloud copy to fall back on.

⚠ The click target is the row **Data & backups** (summary: "Storage mode, encrypted backups, AI review export"). **Backup & Restore** is the panel heading you see after the row expands. If you go looking for a top-level Backup & Restore tab, you won't find it.

### Step 4: Save the Family Custody Map

The app's checklist is the state of your custody map. 17 items, honest. The **Family Custody Map** PDF is the printable page of it: one sheet, one row per account, where everything is and who knows the process. The app can't hand that to a family in a filing cabinet. This is the artifact that can.

**Course toolkit: Family Custody Map** (PDF). Available under **Materials → 07 Family Custody Map**. Print it or fill it as a PDF, then store it with the will and your Heir Letter.

Fill it as you talk. It has five blocks:

| Block | What goes in |
|---|---|
| BITCOIN | Hardware wallet, exchange, ETF, collaborative custody. One row per instance, provider named. |
| WHERE THE BACKUPS ARE | Location only. Never seed words, PIN, or passphrase. "Steel backup: safe deposit box, First National, downtown branch." Not "steel backup: `abandon abandon…`" |
| ACCOUNTS | Retirement, bank, brokerage. Retirement transfers by beneficiary form. Keep those current (Module 8 hooks into this). |
| INSURANCE & OTHER | Policies, property, anything else the family should find. |
| DOCUMENTS | Will, POA, healthcare directive, Executor packet, Heir letter. Where the original is, and who has a copy. |

⚠ This map never contains a secret. It says *where* things are, never *how* to open them. The template's own footer says it: *"never the words, PIN, or passphrase."* If your instinct is to write the seed on this map, stop and go back to the no-secrets rule before continuing.

⚠ The map is the companion to the Heir Letter in the estate module. The letter says who to call and in what order. The map says what exists and where. Both need to be findable by the executor, and neither can contain a secret.

Set the review date on the footer: *"Review yearly. Module 9."* That becomes an input to next module's annual walkthrough.

### Step 5: Record your decisions

There is no scheduler in Orange Plan. These decisions live in your calendar or a note.

- **Custody level chosen** (Foundation, Substantial, or High Net Worth). Your call, based on the self-triage. Not the app's tier, which is estate-size-based.
- **Top single point of failure and the one fix this week.**
- **Annual custody review** on the calendar, recurring.

Optional on-screen anchor for the tier decision: **Protect → Protection tier → Mark as reviewed**.

Optional artifact: **Protect header → Download estate summary** produces a PDF of the readiness state.

The custody card you just built becomes the input to Module 9's annual review. That walkthrough re-reads this checklist honestly and asks: what changed since last year?

### Step 6: The "Draft with AI" button you'll scroll past

While you're on Protect, you'll pass a **Draft with AI** button in the Heir letter section. Walk past it in this lesson. It belongs to Module 8, where you're actually writing the letter.

If you want a line as you pass it: *"there's an assistant for the heir letter. That's next module."*

### What good looks like

- **The Needs attention list is shorter at the end than the start.** And the top remaining item gets named out loud as this week's fix.
- **Hardware items are honest.** *Full recovery process tested end-to-end* is checked only if you actually did the wipe-and-restore. Leave unchecked anything you haven't done; a checked item that never happened makes the plan believe something untrue.
- **Distribution items are the only-one hunt, itemized.** *Key material stored in 2+ physical locations* and *No single person can access funds alone*, both true, is the bar. Both unchecked and the map has a real gap.
- **Access after death** is the handoff to Module 8. Those four items are next module's homework list.
- **Nothing secret got typed.** Say the absence as the win. The one moment you'll touch a passphrase is the backup export in Step 3, and you'll have explained exactly what it is and is not.
- **The plan file exists on disk**, encrypted with a passphrase you control.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Honest checklist state (the custody map) | Protect → Security checklist (17 items, tier-filtered) |
| 2 | Family Custody Map filled in on paper | Course toolkit → **07 Family Custody Map** (PDF). Stored with the will. |
| 3 | Tier confirmed | Protect → Protection tier → Mark as reviewed |
| 4 | Top SPOF and its fix | Needs attention top row plus a recorded decision |
| 5 | Encrypted plan backup on disk | Settings → Data & Privacy → Data & backups → Export Plan |
| 6 | Annual custody review on the calendar | Recorded decision (no in-app scheduler) |
| 7 | Optional artifact | Protect header → Download estate summary |

### Handing it off

The next module (Estate & Inheritance) turns "Access after death" from four checkbox promises into a working handoff. You'll pair the Custody Map you just saved with two more toolkit documents: the **Heir Letter** (who to call and in what order) and the **Executor Packet** (the operations manual for the person who runs the process). Everything on this custody map is the prerequisite for that walkthrough.
