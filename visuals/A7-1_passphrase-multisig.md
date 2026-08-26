# A7.1 · Advanced custody methods and remaining failures

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That passphrase, multisig, collaborative custody, institutional custody, and an intentional split remove different failures. None removes every failure.

## The visual
Top row, three technical panels:

**Passphrase single-sig:** one compatible mnemonic feeds a standard wallet and, with the exact passphrase, a different derived wallet. A typo reaches another valid but unintended wallet.

**2-of-3 multisig:** three signing keys surround a separate policy/descriptor card. Any two keys sign; one cannot. The policy card has a clear **CANNOT SIGN** label.

**Institutional custody:** the institution controls keys and withdrawals; the household receives support and administration but accepts counterparty and access risk.

Bottom row, a comparison table with two rows:

- What one failure can no longer do
- What can still fail

A final strip shows an **intentional split** across distinct failure domains and the warning: **Every extra method must solve a named risk.**

## Labels and data
Do not imply “None” under single point of failure. Use exact language:

- Passphrase: seed alone cannot spend the intended wallet; seed/passphrase recovery and family process can still fail.
- Multisig: one lost key does not lose the wallet; policy data, key distribution, software, provider, and family process can still fail.
- Institutional: personal key loss is transferred; provider, withdrawal, jurisdiction, identity, and family administration can still fail.

Never render an actual mnemonic, passphrase, key, descriptor, fingerprint, address, provider name, or account number.

## Motion
Each panel first removes one failure, then reveals the remaining failures. The intentional-split strip only appears after the trade-offs are visible.
