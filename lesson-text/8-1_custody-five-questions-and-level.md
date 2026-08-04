# Custody: the five questions and choosing your level

Custody is whether you can reach your Bitcoin, whether anyone else can, and whether the process survives without you. (Inheritance, the legal transfer, is the next module.) A balance in someone else's system is a claim on *their* Bitcoin, not ownership of yours (Celsius, BlockFi, FTX).

## The five questions

1. Where is the Bitcoin held?
2. What type of custody?
3. Who knows what to do?
4. What happens if you're unavailable?
5. Where are the single points of failure?

A normal Bitcoin household scores 2 of 5. The score turns worry into specific jobs. Also: **name the job each pile does**: long-term cold storage and an emergency-reachable account need different custody, and an exchange can freeze exactly the week you need it.

## The one rule

**Document the process, never the secrets.** Secrets = seed phrase, private keys, passphrase, PIN. Write down who holds what and what to do, never the words that unlock it.

## The four levels

| Level | Setup | For |
|---|---|---|
| 1 · Hardened exchange/ETF | Strong password, app 2FA, secured email, withdrawal delays | Small stack or still learning |
| 2 · Hardware wallet | Seed offline, test transaction, **proven wipe-and-restore**, steel backup | The default once a stack is meaningful |
| 3 · Passphrase + split access | Process a spouse/executor can follow, annual review | The stack matters to more than you |
| 4 · Collaborative or DIY multisig | Professional support or full DIY, tested family process | One mistake would be unacceptable |

**Every level is a trade.** Level 1 buys convenience and costs counterparty risk (frozen exactly when you need it). Level 2 buys true ownership and costs maintenance (one seed, one point of failure). Level 3 buys survivability and costs complexity (a lost passphrase is permanent). Level 4 buys "no single mistake ends it" and costs the most complexity of all. More sovereignty always means more responsibility; more convenience always means more counterparty risk. You choose which risks you hold, you never eliminate them.

Match the level to stakes and skill. A mismatch in either direction is the failure. Custody is not a purity test: a simple setup your family can use beats an advanced one nobody understands. (The app separately tiers its checklist by estate size: Foundation / Substantial / High Net Worth.)

## Don't hold it all at one institution

A second question applies to whatever isn't self-custodied: **how many institutions is it in?** Celsius, BlockFi, and FTX were concentration failures, not self-custody failures. The people who lost everything had everything in one place.

**Split across institutions when:** the custodial amount is large enough that losing access for months would change your life; an exchange balance is doubling as your emergency-reachable pile; or the institutions fail in genuinely different ways (two exchanges are more correlated than an exchange and a brokerage ETF, and both more than either and a hardware wallet).

**What it costs:** every extra account is another login, email, and 2FA to secure (three sloppy accounts beat by one hardened one), another set of tax lots to reconcile, and another row your executor must find. If it isn't on the Family Custody Map, you've hidden money from your own family.

**The rule:** self-custody is the real answer to counterparty risk; splitting institutions is the hedge for whatever isn't self-custodied yet. Add the second institution when the amount justifies the maintenance, not before.

## Advanced setups

- **Passphrase single-sig**: one seed + a hidden extra word. Simplest family-followable advanced plan. ⚠ A forgotten passphrase is permanent; back it up separately, practice small.
**Making the passphrase strong: the 7-word standard.** A passphrase you invent is the weak point; quotes, lyrics, names, and dates get cracked first. Use **7 random words** from a wordlist, picked by dice or an offline generator (diceware), never by you. Each random word multiplies the guesses needed by ~7,776; seven words is ~90 bits of entropy, which is millions of years of guessing at a trillion tries per second. Never personal facts or reused passwords. Record it exactly (case-sensitive), on paper or steel, never typed online. Same standard for three things: wallet passphrase, password manager master password, plan-backup passphrase. Built-in trade-off: unguessable also means unrecoverable, so it gets its own backup, stored away from the seed.

- **Collaborative multisig (2-of-3)**: you hold two keys, a provider holds one (never your seed). Heirs get a guided recovery. Costs a fee + some vendor dependence.
**How collaborative custody works (2-of-3, and the key count is the point).** Three keys, any two can spend. **You hold two; the provider holds one.** So they can never take your Bitcoin (one key of a required two spends nothing, making them a co-signer, not a custodian) and they can never lock you out (your two keys are already a spending quorum). You're buying three things: a key you didn't store yourself, a config-file copy held by someone whose job is not losing it, and a human who will walk your family through recovery.

**Verify before choosing a provider:** (1) Can you recover with them gone? They should hand you the config/descriptor, and it should work in open-source software they don't control. "You'd have to call us" is a custodian in a multisig costume. (2) Is there a documented inheritance process, and what proof does the executor need? (3) What's the annual fee, and what happens if you stop paying? (4) What identity and privacy terms does opening the account require?

The real downside is depending on a company across decades. But it's bounded: worst case, the provider vanishes and you recover with your two keys and the config. The DIY worst case is that the person who understood the setup is the one who died.

- **DIY multisig**: maximum privacy and independence; your heirs inherit the complexity with no help coming.

**The config file:** keys hold the money; the config is the map that reassembles a multisig wallet. Heirs with all three seeds and no config recover *nothing* (a real ~$300k loss). It has no spending power, so back it up aggressively, and never store it beside a key.

## Homework

1. Score the five questions; write the number.
2. Write your level today vs the level your amount and family require.
3. Running multisig? Find the config, back it up, tell one person it exists.
