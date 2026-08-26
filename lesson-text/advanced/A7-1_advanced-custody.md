# Advanced custody: passphrase, multisig, and collaborative

## Passphrase

A BIP39 passphrase is an optional string that derives a different wallet. Every passphrase, including a typo, derives a valid wallet. It is not an extra mnemonic word and it is not multisig.

Austin's seven-random-word rule is an operational standard, not a protocol minimum. Store and back up the exact passphrase separately from the mnemonic and test the intended wallet.

## 2-of-3 multisig

Any two signing keys can authorize a spend; one cannot. Recovery also needs the wallet policy/descriptor or enough script, derivation, and key-origin data to reconstruct it.

A descriptor is privacy-sensitive but cannot sign. One key plus a descriptor remains one key in a 2-of-3 wallet.

## Collaborative custody

Verify the actual threshold, which keys the client controls, whether the client can meet the threshold without the provider, whether the policy is exported, compatible recovery software, and the contractual delay/veto powers.

## Complete when

The exact passphrase or intended key combinations were tested on a spare setup, the policy/descriptor was restored, provider-independent recovery was proven when claimed, and the legal roles match the signing policy.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
