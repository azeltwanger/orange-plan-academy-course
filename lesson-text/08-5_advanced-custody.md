# Advanced custody: passphrase, multisig, and collaborative

Once you've found your single points of failure, advanced custody splits them. Every setup here turns one "only one" into two, and you pay for it in complexity and in what your family has to be able to do. Staying at a well-run Level 2 is a legitimate answer.

## The three paths

- **Passphrase single-sig**: one seed + a hidden extra word. Simplest family-followable advanced plan. ⚠ A forgotten passphrase is permanent; back it up separately, practice small.
**Why a passphrase at all:** someone cleans your house and finds your seed phrase in a drawer. Without a passphrase they have your Bitcoin. With one, they have words that open an empty wallet.

⚠ **The temptation is to pick something short and memorable** so you can't forget it. Memorable means guessable, and this guards money for decades. The answer isn't a passphrase you can remember. It's 7 random words backed up properly in two places, so you never have to.

**Password manager?** Fine as *one* copy, never the only one, and only if someone else can get into it if you're gone. A passphrase that dies with you is a secure way to lose your Bitcoin. Keep a physical copy.

**Making the passphrase strong: the 7-word standard.** A passphrase you invent is the weak point; quotes, lyrics, names, and dates get cracked first. Use **7 random words** from a wordlist, picked by dice or an offline generator (diceware), never by you. Each random word multiplies the guesses needed by ~7,776; seven words is ~90 bits of entropy, which is millions of years of guessing at a trillion tries per second. Never personal facts or reused passwords. Record it exactly (case-sensitive), on paper or steel, never typed online. Same standard for three things: wallet passphrase, password manager master password, plan-backup passphrase. Built-in trade-off: unguessable also means unrecoverable, so it gets its own backup, stored away from the seed.

- **Collaborative multisig (2-of-3)**: you hold two keys, a provider holds one (never your seed). Heirs get a guided recovery. Costs a fee + some vendor dependence.
**How collaborative custody works (2-of-3, and the key count is the point).** Three keys, any two can spend. **You hold two; the provider holds one.** So they can never take your Bitcoin (one key of a required two spends nothing, making them a co-signer, not a custodian) and they can never lock you out (your two keys are already a spending quorum). You're buying three things: a key you didn't store yourself, a config-file copy held by someone whose job is not losing it, and a human who will walk your family through recovery.

**Verify before choosing a provider:** (1) Can you recover with them gone? They should hand you the config/descriptor, and it should work in open-source software they don't control. "You'd have to call us" is a custodian in a multisig costume. (2) Is there a documented inheritance process, and what proof does the executor need? (3) What's the annual fee, and what happens if you stop paying? (4) What identity and privacy terms does opening the account require?

The real downside is depending on a company across decades. But it's bounded: worst case, the provider vanishes and you recover with your two keys and the config. The DIY worst case is that the person who understood the setup is the one who died.

- **DIY multisig**: maximum privacy and independence; your heirs inherit the complexity with no help coming.

**The config file:** keys hold the money; the config is the map that reassembles a multisig wallet. Heirs with all three seeds and no config recover *nothing* (a real ~$300k loss). It has no spending power, so back it up aggressively, and never store it beside a key.

## Homework

1. Decide whether an advanced setup is warranted at all. A well-run Level 2 is a valid stopping point.
2. Adding a passphrase? Generate it from 7 random words (dice or an offline generator), back it up separately from the seed, practice with a small amount.
3. Considering collaborative custody? Ask a provider the four questions and get the answers in writing before paying anything.
4. Running multisig? Find the config, back it up, tell one person it exists.
