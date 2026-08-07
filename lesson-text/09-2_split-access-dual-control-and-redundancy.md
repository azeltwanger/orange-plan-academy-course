# Split access: dual control and redundancy

Design who can reach your Bitcoin after you are gone, and prove it works while you are still here.

## Why the simple options fail

- **One person gets everything:** a non-heir now has unilateral control of the inheritance, protected only by good faith.
- **Nobody gets enough:** you tell no one "to be safe," and the stack dies on a device nobody can open.

## The two tests

Every access setup has to pass two separate tests, and they are not the same test.

1. **Dual control.** Can one person spend alone? If yes, that person is a single point of theft and a single point of pressure.
2. **Redundancy.** Can one lost copy, or one unavailable person, permanently stop recovery? If yes, you have built a way to lose the Bitcoin that has nothing to do with anyone being dishonest.

Handing one person everything fails test 1. Telling nobody fails test 2. **Passing one does not give you the other.** Most setups that pass test 1 fail test 2 by default, and test 2 is a separate job you have to do on purpose.

## Your design follows your custody level

You do not need a more advanced setup to do this lesson. You need an honest design for the setup you already have.

| Level | The design | Test 1 | Test 2 |
|---|---|---|---|
| **1** · hardened exchange or broker | The institution is your dual control. Heirs get the beneficiary designation; the executor gets the process: which institution, what they will ask for, who to call | Handled by the company | Handled by the account existing regardless of who remembers a password |
| **2** · one hardware wallet, one seed | The seed goes to your heir, backed up in more than one place. The executor holds the *process*, not the secret: where the device is, where the backups are, what to do, who to call | **Fails**. Your heir can spend alone | Passes |
| **3-4** · passphrase or multisig | Two objects to two people (passphrase), or 2-of-3 where any two keys spend and no single key can (multisig). **Implementation is in Advanced Custody**: it is a custody decision, not an estate decision | Passes | Passes, once each piece is backed up on its own side |

The Level 2 trade is acceptable for a lot of households, and far better than either failure above. Choose it knowing what it is, and **do not describe it to your family as a no-single-point-of-failure plan.**

The estate job is the same at every level: name who holds what, answer both tests out loud, and be honest about the one you did not pass.

## Every backup is also a path in

This is the real design problem. Every backup you add to protect against loss is another potential path to unilateral access.

It resolves the same way every time: **each piece gets its own backup, and that backup stays on its own side.** Never in the same house, never in the same safe, never with the person holding the other piece. Done that way, each side can lose a copy and still recover while neither side gains anything it should not have. Done carelessly, a backup in a shared safe collapses the whole design into one person holding everything.

This is also why the executor and the heirs should be different people wherever you can manage it. They are the two sides of whatever you build.

## Test it while you are alive

Move about $1,000 into the setup. Whoever is supposed to be able to recover it does the recovery, on a spare device, following only what is written down. Watch the $1,000 appear.

If two people are supposed to be needed, **run it twice**: once with both, and once with only one, to confirm the one alone cannot.

One rule after the test: the pieces stay distributed. Writing everything down together in one place undoes the entire design.

## The misconception that gets people hurt

*"I'll just split the seed words between two people."* Someone actually did this: 24 words, 12 each.

If the two people trust each other, together they have the whole thing, so there is no protection. If either gets the other half through a leak or a guess, they have unilateral access, and 12 words is a far shorter guess than 24.

**Splitting a seed makes the wallet weaker. Splitting a seed from a passphrase makes it stronger.** They sound almost identical and do opposite things. To pass test 1, you change your custody setup. You do not chop up your seed.

## Your decision

**Who holds what, and which of the two tests your design passes.**

1. Design for the custody level you actually have. An access plan built on a setup you have not finished is not a plan.
2. Pick people who do not share a household, a safe, or a bad week.
3. Choose for reliability over technical skill. The process is written down; the person mainly has to follow it and be findable.
4. Assume neither person goes rogue, and plan as if one might.

## Homework

1. Name the person holding each piece, and write down where each piece lives.
2. Answer both tests in writing. Write down the answer you do not like, because that is the one you will otherwise forget you chose.
3. If you failed test 2, fix it first. A loss you caused yourself is far more likely than a betrayal.
4. Run the test with a small amount, start to finish.
5. Confirm afterwards that the pieces are still in separate places, and were never written down together.
