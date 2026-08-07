TELEPROMPTER SCRIPT — segment 1.2
1.2 How the AI works
1360 words · ~8.8 min at 155 wpm
============================================================

In today's lesson, we're going to cover the AI that's built into Orange Plan: what it reads, what it never sees, and where it runs.

== THE BUTTON AND THE PANEL ==

In the top bar there's a button called AI Review. It's the one orange pill up there. Clicking it slides open a panel called Plan Guide.

That panel lives in the app itself, not on any one page, so it opens from anywhere. It also stays alive when you close it. You can be in the middle of a conversation, close the panel, go look at a number on the Tax page, slide it back open, and pick up where you left off.

It's included for every signed-in user. There's no separate AI plan and no add-on to buy.

== THE RULE THAT MAKES THE NUMBERS TRUSTWORTHY ==

The AI does not do your math.

Your surplus, your reserve status, your payoff dates, your loan cushion, your spending target, your success rate, your income floor. All of those come out of the same projection engine that draws your charts. The AI reads those numbers and explains them. It's specifically instructed never to redo arithmetic the app already did, and if it ever does calculate something on its own, it has to label that as an estimate.

So when it tells you your surplus is $2,400 a month, that's your app's number, not the model's guess.

It's also told to use only the plan data it was given, and if something important is missing, to say what's missing instead of filling in the blank.

== WHAT IT READS ==

It doesn't get a copy of your whole plan. What it gets is targeted context for whatever you're asking about, plus where you are in the app: which page, which tab, what you have selected.

Every number it receives is labeled with its status. Applied means saved and actually being used in your projections. Draft means you typed it but haven't saved it. Preview means you're modeling it in a sandbox and it isn't applied. Stale means it's saved, but you've changed something since it was calculated.

That's why it can tell you your confidence number is stale instead of reading you an old number like it's current.

And if it needs detail it doesn't have, it asks for it. There are 22 things it can request: your full holdings list, your accounts, your debts, specific projection years, your life events, your tax picture. Those requests get answered by your own browser out of the plan it already has loaded, and only the rows it actually asked for get sent.

== WHAT IT NEVER SEES ==

Your raw transactions never leave your browser. They get stripped out of every request, every time. It sees your spending summarized and counted, not line by line.

On the Protect page, it never gets names, contact details, the contents of your heir letter, who holds what for recovery, or where anything is stored. It gets completion status, so it can tell you your beneficiary row is empty without ever knowing who's in it or where anything is kept.

On linked accounts, it never gets your institution names, account names, account numbers, masks, or exact balances.

And it actively blocks secrets. When you use the heir letter drafting tool, it scans what you typed for anything that looks like a seed phrase, recovery words, a private key, a passphrase, a PIN, a safe combination. If it finds one, it refuses to draft until you take it out. It'll even catch you mapping out who holds which key and strip that down to the category before it sends anything.

Never put a seed phrase, a private key, a wallet backup, a passphrase, a PIN, a password, a full account number, or a Social Security number into any AI. Not this one, not any other one. And if you've already done it somewhere, treat that material as compromised and move the funds to a newly generated wallet.

== WHERE IT RUNS ==

It runs on Claude Sonnet, routed to Anthropic's own servers. Every request Orange Plan sends carries a setting that excludes any provider that would keep your prompts or train on them.

Your conversations are stored in your own account in Orange Plan's database, locked to your user, so you can come back to them and nobody else can read them.

== MEMORY IS OFF UNLESS YOU TURN IT ON ==

Inside Plan Guide there's a Preferences section with a memory toggle. It starts off.

If you turn it on, what it remembers is how you think, not what you own. Things like: prefers borrowing over selling Bitcoin. Self-employed with variable income. Wants to be work-optional by 55. It's specifically blocked from storing dollar balances, account numbers, secrets of any kind, and one-off details from a single question.

It holds 24 items at most. Every one of them is visible in that panel, you can delete them one at a time, and there's a clear-everything button.

I'd turn it on if you plan to use the AI regularly, because it stops you re-explaining your situation every time. If that makes you uncomfortable, leave it off and nothing about the reviews changes.

== WHY THE BUTTON IS DIFFERENT ON EVERY PAGE ==

Nine pages have their own AI button. Cash Flow says Route with AI. The debt page says Review Debt Strategy. Allocation says Review portfolio. Tax says Review Tax Strategy. Scenarios says Review scenario.

Those aren't shortcuts to the same thing. Each one loads a different set of instructions and a different piece of the knowledge base. A tax review loads the tax knowledge and gets held to tax-specific rules, like not suggesting a Roth conversion when there's no pre-tax balance in your plan to convert. A cash flow review loads the cash flow knowledge instead.

There are 26 of these built in. Nine have buttons, and the rest you get to by asking, like setting a reserve target or comparing selling versus borrowing.

So the practical version is: ask from the page you're standing on, and you get the version built for that decision.

== WHAT COMES BACK ==

Every review comes back in the same four sections. A read on your plan. The top 3 things it sees. The next 3 moves. And one question, which is whichever question it thinks would most improve the review if you answered it.

The moves are always framed as options with trade-offs. It won't tell you that you should do something.

== WHAT IT WON'T DO ==

It won't tell you to sell, convert, borrow, or buy. It won't predict Bitcoin's price. It won't quote you a current tax bracket or contribution limit off memory. It won't touch altcoins, pick tickers for you, prepare a tax return, or draft legal documents.

One thing people assume it won't do that it will: tax math. Roth conversion comparisons, harvesting math, cost basis, after-tax comparisons. That's all in bounds. The line is filing and executing, not calculating.

== THE LIMITS ==

You get 10 plan reviews and 100 messages a day, and it resets at midnight UTC. Your saved reviews stay saved when you hit it.

== ONE THING IT DOESN'T KNOW YET ==

It knows the app and it knows the planning frameworks this course is built on. It does not know these lessons yet. Teaching it this course is on the list, so when that ships you'll be able to ask it about anything we cover here. Until then, it can review your plan but it can't teach you these lessons.

And the last thing, which I'm saying once here so I don't have to keep repeating it in every walkthrough: it reviews and it explains. You decide.

== HOMEWORK ==

1. Click the AI Review button in the top bar so you know where it lives.
2. Open Preferences inside Plan Guide and decide whether memory is on or off for you.
3. Fix the one hard rule: no seed phrase, private key, passphrase, PIN, or full account number ever goes into any AI, including this one.
