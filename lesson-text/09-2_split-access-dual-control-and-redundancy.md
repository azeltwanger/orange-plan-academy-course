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
| **1** · hardened exchange or broker | **Not household dual control.** You have delegated custody, and the institution's procedure is what stands between one person and the money. Heirs get the beneficiary designation; the executor gets the path: which institution, what they will ask for, who to call | Answered by the company's process, not by your design | Answered by the account existing regardless of who remembers a password |
| **2** · one hardware wallet, one seed | The seed goes to your heir, backed up in more than one place. The executor holds the *process*, not the secret: where the device is, where the backups are, what to do, who to call | **Fails**. Your heir can spend alone | Passes |
| **3-4** · passphrase or multisig | Two objects to two people (passphrase), or 2-of-3 where any two keys spend and no single key can (multisig). **Implementation is in Advanced Custody**: it is a custody decision, not an estate decision | Passes | **Passphrase: only if you design it.** Seed + passphrase is 2-of-2, so each half needs its own separate backup. **2-of-3 multisig: from the arithmetic**, since losing one key is survivable |

⚠ **At Level 1, verify the institution's death-claim procedure.** That procedure *is* your plan. If it is slow, or requires something your family will not have, that is the gap, and no amount of household design fixes it.

The Level 2 trade is acceptable for a lot of households, and far better than either failure above. Choose it knowing what it is, and **do not describe it to your family as a no-single-point-of-failure plan.**

The estate job is the same at every level: name who holds what, answer both tests out loud, and be honest about the one you did not pass.

## Every backup is also a path in

This is the real design problem. Every backup you add to protect against loss is another potential path to unilateral access.

It resolves the same way every time: **each piece gets its own backup, and that backup stays on its own side.** Never in the same house, never in the same safe, never with the person holding the other piece. Done that way, each side can lose a copy and still recover while neither side gains anything it should not have. Done carelessly, a backup in a shared safe collapses the whole design into one person holding everything.

This is where the executor question comes back. **If your design puts the executor on one side and the heirs on the other, they have to be different people**, or one person holds both sides on day one. If your design does not split them that way, and plenty do not, a spouse serving as both is fine. It is a consequence of your design, not a rule about executors.

## Test it while you are alive

Move about $1,000 into the setup. Whoever is supposed to be able to recover it does the recovery, on a spare device, following only what is written down. Watch the $1,000 appear.

If two people are supposed to be needed, **run it twice**: once with both, and once with only one, to confirm the one alone cannot.

One rule after the test: the pieces stay distributed. Writing everything down together in one place undoes the entire design.

## The misconception that gets people hurt

*"I'll just split the seed words between two people."* Someone actually did this: 24 words, 12 each.

Look at what that builds. If the two people trust each other, together they have the whole thing, so there is no protection at all. And you have created a **2-of-2**: either half going missing loses everything permanently. You took on the redundancy problem without buying any dual control.

**Splitting a seed from a passphrase gives you two objects designed to be separate. Chopping one seed in half gives you two fragments of one object**, and a wallet that fails if either fragment does. They sound almost identical and do opposite things. To pass test 1, you change your custody setup. You do not chop up your seed.

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
