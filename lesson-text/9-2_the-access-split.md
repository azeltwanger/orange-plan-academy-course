# The access split

Divide the ability to reach your Bitcoin into two pieces held by two people. Either piece alone is useless; only together can they move coin. Heirs hold one, the executor holds the other.

## Why the simple options fail

- **One person gets everything:** a non-heir now has unilateral control of the inheritance, protected only by good faith.
- **Nobody gets enough:** you tell no one "to be safe," and the stack dies on a device nobody can open.

The split does two jobs: **no unilateral access** (nobody can help themselves, or be pressured into moving it alone) and **no single point of failure** (one lost piece doesn't lose the Bitcoin).

## Poor man's multisig (passphrase)

Seed + passphrase opens a *different wallet* than the seed alone. (The passphrase itself follows the custody module's 7-random-word standard.) So: the seed alone opens a real-but-empty wallet; the passphrase alone opens nothing. Wife holds the seed; the executor holds the passphrase. Together, full access; apart, nothing. A bad actor gets nothing; a lost card still leaves half the plan intact.

## Multisig version

2-of-3: you hold two keys (you spend normally), the executor holds a sealed third (can't spend alone), a provider holds the last (never your seed). After you're gone, executor + provider = threshold, with guided recovery. The job shifts to **keeping the config file away from whoever holds a key**: config beside a key quietly turns 2-of-3 into single-key.

## Test the split while you're alive

One Saturday: move ~$1,000 into the passphrase wallet → spouse restores the seed on a spare device → executor reads the passphrase over the phone → the $1,000 appears. A hoped-for split becomes a proven one. The pieces stay distributed afterward, because writing them together anywhere undoes the split.

## The misconception

"I'll split the seed words 12 and 12." That makes the wallet *weaker*: together they have everything, and either half makes the other a shorter guess. **Splitting a seed weakens the wallet. Splitting the seed from a passphrase strengthens it.**

## Homework

1. Decide who holds each half.
2. Run the Saturday-afternoon test with a small amount.
3. Verify nothing anywhere holds both halves together.
