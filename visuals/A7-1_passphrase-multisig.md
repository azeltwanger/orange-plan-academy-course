# A7.1 · Passphrase and multisig

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That a passphrase derives a different wallet, while multisig enforces a signing threshold and also needs recoverable wallet-policy data.

## The visual
Two panels.

**Left — passphrase:** one compatible mnemonic feeds the standard wallet and, with an exact passphrase, a different derived wallet. A typo branches to another valid but unintended wallet. Do not imply the standard wallet must be empty or is automatically a decoy.

**Right — 2-of-3 multisig:** three signing keys surround a separate policy/descriptor card. Any two keys sign; one cannot. The policy card restores wallet structure and addresses but carries a clear **CANNOT SIGN** label.

## Labels and data
Austin's operational rule: seven random words, stored and backed up separately—not a protocol minimum. Exact passphrase required. Signing keys 2 of 3. Policy/descriptor required for practical recovery and privacy-sensitive.

Never render an actual mnemonic, passphrase, key, descriptor, fingerprint, or address.

## Motion
Left: exact passphrase reaches the intended wallet; a one-character change visibly reaches another valid wallet. Right: valid key pairs light in turn while the descriptor stays visible but never enters a signing slot.
