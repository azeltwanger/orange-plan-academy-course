TELEPROMPTER SCRIPT — segment 8.4
8.4 Single points of failure, account hardening, and scams
~9 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover single points of failure, account hardening, and the scam rules. This is the lesson about closing the doors you didn't know were open.

== THREE SHAPES OF A SINGLE POINT OF FAILURE ==

A single point of failure is anything that exists only once, where losing it means the Bitcoin is unreachable. And it comes in three shapes.

The first shape: the thing gets destroyed. A device, a backup.

The second shape: the thing is fine, but the person is unavailable, because only one person knows the process.

And the third shape: you're fine, your Bitcoin is fine, and the custodian won't let you move it. An exchange freezes an account.

Most people count the devices and completely forget the custodians.

== THREE ORDINARY TUESDAYS ==

Let me make this concrete with the couple. Their setup: one hardware wallet in a desk drawer, one paper seed backup in the same house, a quarter Bitcoin on an exchange protected by SMS two-factor, and a wife who has never restored a wallet.

Now, three completely ordinary events.

First: the house floods. The device and the only seed backup are in the same building, so about $150,000 of Bitcoin goes out with the drywall. Two copies in one location were never really two copies.

Second: he's hospitalized for 6 weeks. Nothing was stolen, nothing was lost, but nothing can move either. She can't sell a dollar of it, and she can't even tell anyone what exists.

Third: the exchange freezes his account during a routine review. The $25,000 is unreachable for however long the review takes, and nobody will give him a date.

Three ordinary Tuesdays, no hackers involved anywhere. The failure that actually loses Bitcoin is almost always just one thing without a backup.

== THE NINE-QUESTION HUNT ==

So the hunt is 9 questions, and for each one you ask: is there only one?

Only one device? Only one seed backup? Only one location? Only one person who knows everything? One weak exchange login? One heir with no idea what exists? A document that contradicts your beneficiary forms, which are the forms your bank and retirement accounts keep on file naming who gets the money? A passphrase nobody else can recover? And multisig keys all sitting in one place?

The couple checks six of nine. And again, they're not careless. A normal setup collects only-ones on its own over the years, because nothing ever asked the question.

== THE FIX METHOD ==

The fix method matters as much as the list, because trying to fix all nine at once is how nothing gets fixed.

Step one: list your top three, ranked by what the loss would cost. Not by how easy each one is to fix. Step two: pick the one at the top. Step three: fix that one, and only that one. Step four: re-check and repeat.

For the couple, the top item is the seed backup and the device sharing an address. The fix is a steel backup stored somewhere else. The in-laws' place, a safe deposit box, a second property. That's one afternoon of work.

The next one is the hospital scenario, which is a person problem. She needs to have restored a wallet once, with a small amount, so the procedure lives in two heads instead of one.

And notice the pattern: every only-one turns into one of three things. A backup, a second location, or a second person who knows the process. Never the secrets. The process.

== ACCOUNT HARDENING ==

Now, account hardening, and I'll start with why I take this personally. A couple of years ago, someone called my bank pretending to be me and tried to move about $10,000. They didn't get it. But that's the day I moved my exchange and email logins onto physical security keys.

In most real-world losses, nobody breaks the encryption on your Bitcoin. They log in as you.

The hardening order matters, so do it in this order.

First, secure your email account, before anything else. Your email is the master key, because every other account will reset its password to that inbox on request. If they get the email, they get everything downstream.

Second, a strong, unique password on every account.

Third, app-based two-factor, not SMS, and turn the authenticator's cloud backup off.

Fourth, withdrawal delays and allowlists on at the exchange. And never click login links out of an email or a DM. Type the address yourself.

Why not SMS? Because of the SIM swap. Someone talks your carrier into moving your number onto their SIM, and from that moment, your texts arrive on their phone. A SIM swap takes the exchange and the email in one afternoon.

And one step better than the authenticator app: a hardware security key. A physical key is bound to the real site's address and checks it before signing. A lookalike phishing site simply doesn't get a response. That takes phishing off the table entirely, and it's the cheapest upgrade in this whole lesson.

== THE SCAM RULES ==

The scam rules are short.

If a call says your account is hacked, hang up and contact the provider yourself, through the app or the number on your card. And guaranteed returns are a scam. All of them. There's no exception waiting for you.

The common thread in every scam is urgency. Every scam needs you to act before you think. So when something feels urgent, close the app and slow down. That one habit catches scams you've never even seen before, because it doesn't need to recognize the scam. It just needs to notice the pressure.

== TWO THINGS NOBODY TELLS YOU: UTXOS AND ADDRESSES ==

There are two operational things that almost nobody explains, and both of them came from clients asking me directly.

The first one is UTXOs. A client asked me what happens to all the small buys he'd made over the years. His worry was that a bunch of tiny purchases might end up stranded, and that's actually a real thing, so let me explain it.

Your wallet isn't a bucket with a balance in it. It's more like a wallet full of bills. Every time Bitcoin lands in your wallet, that deposit is its own separate chunk, and the technical name for one of those chunks is a UTXO. When you spend, your wallet grabs one or more of those chunks to cover the amount.

Every chunk costs a fee to spend, and that fee doesn't care how big the chunk is. So a very small deposit can become uneconomical to move, because the fee to spend it approaches or exceeds what it's worth. That's what people mean by dust.

If you've been buying small amounts regularly, you can end up with a wallet made of a hundred tiny chunks. Nothing is lost. But the day you go to move it all, you're paying fees on every one of those chunks at once, and if fees are high that day, it gets expensive.

The fix is called consolidation. You send those small chunks to yourself in one transaction, which combines them into one bigger chunk. And you do it deliberately on a day when fees are low, not on the day you urgently need to move money. That's a chore for a quiet Sunday, not an emergency.

The second thing is addresses. Another client was surprised to learn that if somebody knows one of your receiving addresses, they can look up the entire history of that address on the blockchain. Bitcoin's ledger is public. That's the whole design.

So if you use the same receiving address over and over, you've handed anyone who has it a running total of everything you've received there.

The fix is easy: use a fresh receiving address every time you receive. Modern wallets generate a new one automatically, and it's usually the default. Just don't override it, and don't post an address publicly and then keep using it. And this is another reason to check the address on the device screen every single time, because it should be a new one.

== HOMEWORK ==

Your homework for this lesson is to:

1. Make your own only-one list, all 9 questions.
2. Pick the one at the top, ranked by cost of loss, and fix it this week. Not all nine. Just that one.
3. Then watch the demo and the walkthrough below this video, where I set up a hardware wallet on screen and then we document your custody map in Orange Plan.

And one pointer before you go. If one lost seed, or one person you can't reach, could end your access, the advanced library compares the three ways to fix that: a passphrase, collaborative multisig, and running multisig yourself. Your custody plan is complete without them. That lesson is there for when the amount or the family situation says you need more.
