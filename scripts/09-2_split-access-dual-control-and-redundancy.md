TELEPROMPTER SCRIPT — segment 9.2
9.2 Split access: dual control and redundancy
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to design who can reach your Bitcoin after you're gone, and prove it works while you're still here.

Before we design anything, I need to give you two tests, because most people design for one of them and just assume they got the other one for free. They didn't, and that assumption is how people lose Bitcoin.

== WHY BOTH SIMPLE OPTIONS FAIL ==

Let me show you why the two obvious answers both fail. The couple's stack is $175,000.

Option one is that one person gets everything. He writes the seed on a card and hands it to her brother, the executor. Now a man who isn't an heir has unilateral control of $175,000 of his sister's inheritance, and the only thing protecting it is his own good faith. Even if he's a great guy, the plan is now built on one person never having a bad year.

Option two is that nobody gets enough. He tells nobody, to be safe. Then he dies. And $175,000 sits on a device his wife can't open, forever.

Everything in this lesson lives between those two extremes.

== THE TWO TESTS ==

🎬 GRAPHIC: two checkboxes, held on screen for the whole lesson. TEST 1 — can one person spend alone? TEST 2 — can one lost copy, or one person you can't reach, permanently stop recovery?

Test one is dual control. Can one person spend alone? If the answer is yes, then that person is a single point of theft, and they're also a single point of pressure, because somebody can lean on them.

Test two is redundancy. Can one lost copy, or one person you can't reach, permanently stop recovery? If the answer is yes, then you've built a way to lose the Bitcoin that has nothing to do with anybody being dishonest.

Two completely different tests. Handing one person everything fails test one. Telling nobody fails test two.

The part that gets missed, and it's really the reason this lesson exists, is that passing one of these does not give you the other. Most setups that pass test one fail test two by default, and test two is a separate job you have to go do on purpose.

== YOUR DESIGN FOLLOWS YOUR CUSTODY LEVEL ==

Now, what you can actually build depends on the custody level you picked back in the custody module. You don't need a more advanced setup to do this lesson. You need an honest design for the setup you already have.

At Level 1, on a hardened exchange or broker, the institution is your dual control, so what you're designing isn't a secret at all. Your heirs get the beneficiary designation on the account, and your executor gets the process: which institution, what they'll ask for, who to call. The company handles test one, and the account existing regardless of who remembers a password handles test two.

At Level 2, one hardware wallet and one seed, be honest about what you can and can't do. You cannot split a single seed between two people, and I'll come back to why that idea is actively dangerous. So the honest design is: the seed goes to your heir, backed up in more than one place, and your executor holds the process rather than the secret. Where the device is, where the backups are, what to do, who to call.

That design passes test two, because a lost copy doesn't end you, and it fails test one, because your heir can spend alone. For a lot of households that's an acceptable trade, and it's far better than either failure we opened with. Choose it knowing what it is, and don't describe it to your family as a no-single-point-of-failure plan.

At Level 3 or 4, the passphrase or the multisig, you can pass both tests at once. A passphrase lets you hand two different objects to two different people, where neither does anything alone. A two-of-three multisig gets both tests from the arithmetic, because any two keys can spend and no single key can. Building either one is in the advanced custody lesson, and that's the right place for it, because it's a custody decision, not an estate decision.

The estate job is the same at every level: name who holds what, answer both tests out loud, and be honest about the one you didn't pass.

== EVERY BACKUP IS ALSO A PATH IN ==

Whatever level you're at, there's one tension you have to resolve deliberately, because it's the actual design problem underneath all of this.

Every backup you add to protect against loss is also another potential path to somebody getting unilateral access.

It resolves the same way every time: each piece gets its own backup, and that backup stays on its own side. Never in the same house, never in the same safe, never with the person holding the other piece. Do it that way and each side can lose a copy and still recover, while neither side gains anything it shouldn't have. Do it carelessly and a backup in a shared safe quietly collapses your whole design into one person holding everything.

This is also why the executor and the heirs should be different people wherever you can manage it. They're the two sides of whatever you build.

== TEST IT WHILE YOU'RE ALIVE ==

Just like the hardware backup, this gets proven, not hoped for.

So, the couple's Saturday afternoon. He moves about $1,000 into the setup. Whoever is supposed to be able to recover it does the recovery, on a spare device, following only what's written down. And they watch the $1,000 appear on the screen. If two people are supposed to be needed, run it twice: once with both, and once with only one, to confirm the one alone can't.

That afternoon converts a hoped-for plan into a proven one, for $1,000 they never actually spent, on a day when nobody was grieving. One rule after the test: the pieces stay distributed. Writing everything down together in one place undoes the entire design.

== THE MISCONCEPTION THAT GETS PEOPLE HURT ==

Last thing, and I hear it most from people at Level 2 who want to pass test one without changing their setup. "I'll just split the seed words between two people." Someone actually did this. 24 words, 12 to each of two people.

If the two people trust each other, together they have the whole thing, so there's no protection at all. And if either one gets the other half through a leak or a guess, they have unilateral access, and 12 words is a far shorter guess than 24.

So splitting a seed makes the wallet weaker, while splitting a seed from a passphrase makes it stronger. Those sound almost identical and they do opposite things. If you want to pass test one, you change your custody setup. You do not chop up your seed.

== YOUR DECISION ==

Your decision out of this lesson is who holds what, and which of the two tests your design passes.

Design for the custody level you actually have, not the one you'd like to have, because an access plan built on a setup you haven't finished isn't a plan. Pick people who don't share a household, a safe, or a bad week. Choose for reliability over technical skill, since the process is written down and the person mainly has to follow it and be findable. And assume neither person goes rogue, while planning as if one might.

== HOMEWORK ==

Your homework for this lesson is to:

1. Name the person holding each piece, and write down where each piece lives.
2. Answer both tests in writing. Can one person spend alone? Can one lost copy or one unreachable person stop recovery? Write down the answer you don't like, because that's the one you'll otherwise forget you chose.
3. If you failed test two, fix it first. Back up each piece on its own side before you do anything else. A loss you caused yourself is far more likely than a betrayal.
4. Run the test with a small amount, start to finish, so you know it actually works.
5. Confirm afterwards that the pieces are still in separate places, and that they were never written down together.
