# How the AI works: what it reads, what it never sees

Orange Plan has an AI built in, and it appears in almost every module from here on. This lesson covers what it reads, what it never sees, where it runs, and why the button changes from page to page.

> **This page is the reference layer, and it is deliberately more detailed than the video.** The model, the exact data it can request, the memory cap, the daily limits, and what it knows about this course are product specifications: they change faster than a recorded lesson can. The video teaches the parts that do not change. This page carries the current numbers.

## Where to find it

The **AI Review** button sits in the top bar. It opens a panel called **Plan Guide**, which lives in the app rather than on any one page, so you can open it from anywhere. Closing the panel does not end the conversation: go check a number on another page, reopen it, and pick up where you left off.

It's included for every signed-in user.

## The AI does not do your math

Your surplus, reserve status, payoff dates, loan cushion, spending target, success rate, and income floor all come from the same projection engine that draws your charts. The AI reads those numbers and explains them. It is instructed never to redo arithmetic the app already performed, and anything it does calculate itself has to be labeled an estimate.

It is also told to use only the plan data it was given, and to say what is missing rather than fill a gap with a guess.

## What it reads

Not a copy of your whole plan. It receives targeted context for the question you asked, plus where you are: page, tab, and what you have selected.

Every value it receives carries a status label:

| Label | Meaning |
|---|---|
| Applied | Saved and used by your projections |
| Draft | Typed in, not saved |
| Preview | Modeled in a sandbox, not applied |
| Stale | Saved, but inputs changed since it was calculated |

That labeling is why it can tell you a confidence number is stale instead of quoting an old figure as current.

If it needs detail it wasn't given, it can request any of 22 specific things: your holdings, accounts, debts, particular projection years, life events, your tax picture. Those requests are answered by your own browser from the plan already loaded there, and only the rows requested get sent.

## What it never sees

- **Raw transactions.** Stripped out of every request, every time. It receives spending summarized and counted, never line by line.
- **Anything identifying on the Protect page.** No names, contact details, heir letter contents, recovery assignments, or storage locations. It receives completion status only, so it can tell you a beneficiary row is empty without knowing who belongs in it.
- **Linked account details.** No institution names, account names, account numbers, masks, or exact balances.

It actively blocks secrets. The heir letter drafting tool scans your input for anything resembling a seed phrase, recovery words, a private key, a passphrase, a PIN, or a safe combination, and refuses to draft until it's removed. It also catches attempts to map who holds which key and reduces that to a category before anything is sent.

**The rule with no exceptions:** never put a seed phrase, private key, wallet backup, passphrase, PIN, password, full account number, or Social Security number into any AI, including this one. If you have already done so anywhere, treat that material as compromised and move the funds to a newly generated wallet.

## Where it runs

It runs on Claude Sonnet, routed to Anthropic's servers. Every request carries a provider setting that excludes any provider that would retain your prompts or train on them.

Conversations are stored in your own account in Orange Plan's database, scoped to your user.

## Memory is off by default

Plan Guide has a **Preferences** section with a memory toggle, and it starts off.

Turned on, it stores how you think rather than what you own: that you prefer borrowing over selling, that your income is variable, that you want to be work optional by a certain age. It is blocked from storing dollar balances, account numbers, secrets, and one off details from a single question.

It holds 24 items maximum. All of them are visible in that panel, deletable individually, with a clear all option.

Turn it on if you plan to use the AI regularly and would rather not re explain your situation each time. Leave it off if you'd prefer, and nothing about the reviews changes.

## Why the button is different on every page

Nine pages carry their own AI button:

| Page | Button |
|---|---|
| Cash Flow | Route with AI |
| Strategy → Debt | Review Debt Strategy |
| Allocation | Review portfolio |
| Strategy → Tax | Review Tax Strategy |
| Withdrawal Strategy | Review income plan |
| Withdrawal Strategy (borrowing) | Review Borrowing Strategy |
| Scenarios | Review scenario |
| Protect | Draft with AI |
| Linked Accounts | Explain review items |

These are not shortcuts to the same prompt. Each loads a different slice of the knowledge base and a different set of rules. A tax review loads the tax knowledge and is held to tax specific constraints, such as not proposing a Roth conversion when the plan has no pre tax balance to convert. A cash flow review loads the cash flow knowledge instead.

There are 26 of these workflows in total. Nine have buttons; the rest you reach by asking, such as setting a reserve target or comparing selling against borrowing.

Practical version: ask from the page you're standing on.

## What comes back

Every review returns in the same four sections:

1. **Planner Read.** What your plan is trying to do and how it's going
2. **Top 3 Things I See.** The three most consequential observations, tied to your numbers
3. **Next 3 Moves.** Three ordered steps, framed as options with trade offs
4. **One Question.** The question whose answer would most improve the review

## What it won't do

It won't tell you to sell, convert, borrow, or buy. It won't predict Bitcoin's price, quote a current tax bracket or contribution limit from memory, touch altcoins, pick tickers, prepare a tax return, or draft legal documents.

One thing people assume is off limits but isn't: tax math. Roth conversion comparisons, harvesting math, cost basis, after tax comparisons are all in bounds. The line is filing and executing, not calculating.

## Limits

10 plan reviews and 100 messages per day, resetting at midnight UTC. Saved reviews and action items stay saved when you reach the cap.

## One thing it doesn't know yet

It knows the app and the planning frameworks this course is built on. It does not yet know these lessons, so it can review your plan but it cannot teach you the course. That work is planned, not shipped.

## The line to remember

It reviews and it explains. You decide.

## Homework

1. Click the **AI Review** button in the top bar so you know where it lives.
2. Open **Preferences** inside Plan Guide and decide whether memory is on or off for you.
3. Fix the one hard rule: no seed phrase, private key, passphrase, PIN, or full account number goes into any AI, including this one.
