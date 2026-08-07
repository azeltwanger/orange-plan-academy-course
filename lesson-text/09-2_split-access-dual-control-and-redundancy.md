# Split access: dual control and redundancy

Divide the ability to reach your Bitcoin into two pieces held by two people. Either piece alone is useless; only together can they move coin. Heirs hold one, the executor holds the other.

## Why the simple options fail

- **One person gets everything:** a non-heir now has unilateral control of the inheritance, protected only by good faith.
- **Nobody gets enough:** you tell no one "to be safe," and the stack dies on a device nobody can open.

Every access setup has to pass two separate tests, and they are not the same test.

1. **Dual control.** Can one person spend alone? If yes, that person is a single point of theft and a single point of pressure.
2. **Redundancy.** Can one lost copy, or one unavailable person, permanently stop recovery? If yes, you have built a way to lose the Bitcoin that has nothing to do with anyone being dishonest.

Handing one person everything fails test 1. Telling nobody fails test 2. **The split below passes test 1 by design and fails test 2 by default.** Test 2 is a separate job.

## Poor man's multisig (passphrase)

Seed + passphrase opens a *different wallet* than the seed alone. (The passphrase itself follows the custody module's 7-random-word standard.) So: the seed alone opens a real-but-empty wallet; the passphrase alone opens nothing. Wife holds the seed; the executor holds the passphrase. Together, full access; apart, nothing. A bad actor gets nothing, so test 1 passes.

**Test 2 fails as built.** Seed plus passphrase is **two-of-two**: both are required, every time. A lost seed card means the passphrase opens nothing. An executor who dies without passing the passphrase on means the seed opens an empty wallet. Either loss is total and permanent, and neither involves anyone behaving badly. Half of a two-of-two is zero.

## Making the split survive a loss

Every backup you add against loss is a potential path to unilateral access. That tension resolves one way: **each component gets its own backup, and that backup stays on its own side of the split.**

- **The seed's backup belongs to the seed side.** A second steel copy the seed holder controls, or that their successor can reach. Never anywhere the passphrase holder can also get to.
- **The passphrase's backup belongs to the passphrase side.** Written once, sealed, held by the executor or their named successor. Never with the seed, never in the same house or safe.

Each side can then lose a copy and still recover, and neither side can act alone. A "backup" in a shared safe quietly collapses a two-of-two into one person with everything.

If you only ever make one copy of each half, that is a legitimate choice for a small stack. It is not a no-single-point-of-failure setup and should not be described to your family as one.

## Multisig version

A 2-of-3 vault passes **both** tests structurally, without you engineering the backups: any two of three suffice, so losing one key entirely is survivable, and no single holder can spend.

2-of-3: you hold two keys (you spend normally), the executor holds a sealed third (can't spend alone), a provider holds the last (never your seed). After you're gone, executor + provider = threshold, with guided recovery. The job shifts to **keeping the config file away from whoever holds a key**: config beside a key quietly turns 2-of-3 into single-key.

## Test the split while you're alive

One Saturday: move ~$1,000 into the passphrase wallet → spouse restores the seed on a spare device → executor reads the passphrase over the phone → the $1,000 appears. A hoped-for split becomes a proven one. The pieces stay distributed afterward, because writing them together anywhere undoes the split.

## The misconception

"I'll split the seed words 12 and 12." That makes the wallet *weaker*: together they have everything, and either half makes the other a shorter guess. **Splitting a seed weakens the wallet. Splitting the seed from a passphrase strengthens it.**

## Your decision

**Who holds each half of your access.**

1. **Split two different objects, never one object in two pieces.** Half a seed weakens the wallet; a seed separated from a passphrase strengthens it.
2. **Pick people who don't share a household, a safe, or a bad week.** Two halves in one house is one location.
3. **Choose reliability over technical skill.** The process is written down; they mainly need to follow it and be findable.
4. **Plan as if one might go wrong.** Neither half is worth anything alone, which is what protects you.

## Homework

1. Name who holds each half and where each piece lives.
3. Run the test with a small amount, start to finish.
3. Confirm the halves stay separate and were never written together.
