# AI-FACTS — how the Orange Plan AI actually works

Source of truth for lesson 0.2 and every AI beat in the walkthroughs.
Verified against the app code on 2026-08-25. Every claim here has a file
behind it. If the app changes, this file changes first, then the lesson.

Nothing here is written in Austin's voice. It's the fact sheet to dictate
from.

---

## 1 · The two names, and where it lives

| what | name on screen | where |
|---|---|---|
| The button | **AI Review** | top utility bar, the one orange gradient pill (`src/Layout.jsx:78`) |
| The panel that opens | **Plan Guide** | slide-over from the right (`src/components/ai/AIReviewDrawer.jsx`) |

Panel subtitle, verbatim: *"Current plan context · educational analysis"*.

The panel lives in the app shell, not on a page, so it opens from anywhere.
It stays **mounted while closed** — closing it and navigating to another page
does not lose the conversation. Open Plan Guide on Cash Flow, go check a
number on Tax Center, slide it back open, keep going.

Available to **every signed-in user**. There is no separate AI plan or add-on
(`api/ai/_lib/entitlements.js`).

---

## 2 · The per-page buttons — this is the "different prompt on each page" part

Besides the global panel, nine pages carry their own AI button. These are not
shortcuts to the same prompt. Each one launches a **different guided
workflow** with its own knowledge file, its own opening question, and its own
answer contract.

| page | button label (verbatim) | workflow it launches |
|---|---|---|
| Cash Flow | **Route with AI** | next-dollar-routing |
| Liabilities (Strategy → Debt) | **Review Debt Strategy** (mobile: *Review debt*) | debt-strategy-review |
| Allocation | **Review portfolio** | portfolio-allocation-review |
| Tax Center | **Review Tax Strategy** (mobile: *Review tax*) | tax-roth-window |
| Withdrawal Strategy | **Review income plan** | retirement-income-review |
| Withdrawal Strategy (borrowing) | **Review Borrowing Strategy** | btc-loan-safety-check |
| Scenarios | **Review scenario** | scenario-review |
| Protect (Estate Security) | **Draft with AI** | estate-heir-letter |
| Linked Accounts | **Explain review items** | linked-accounts-review |

There are **26 guided workflows** in total
(`src/lib/ai/guidedWorkflowRegistry.js`) — the nine buttons above plus ones
reached by asking, e.g. *Set my reserve target*, *Evaluate leverage
capacity*, *Compare selling vs. borrowing*, *Evaluate Roth conversions*,
*Review harvesting opportunities*, *Test a planning decision*, *Prepare for
estate planning*.

**Two things change per workflow:**

1. **The knowledge it loads.** A cash-flow review loads the cash-flow-reserve
   domain file. A tax review loads tax-cost-basis. A debt review loads
   debt-leverage. It is not loading everything and hoping — the file list is
   fixed per review type (`api/ai/_lib/knowledgeContext.js`).
2. **The instructions it's held to.** Each review type carries its own focus
   rules. The tax one, for example, is told not to propose a Roth conversion
   unless there's actually a pre-tax balance in the plan, and to treat
   cost-basis quality as a gate on any harvesting conclusion
   (`api/ai/review.js`).

The panel is also **page-aware without a button**: open it from Tax Center and
the tax starter jumps to the top of the list (`orderStartersForPage`).

---

## 2a · Daily Bitcoin report

Plan Guide has a **Market brief** card labelled **Run daily Bitcoin report**. It launches the Bitcoin Market Daily assistant.

Verified against `knowledge/assistants/bitcoin-market-daily.md` and `PlanReviewConversation.jsx` on 2026-08-25. The brief is built to replace doomscrolling with a read under two minutes. It sweeps:

- price over 24h, 7d, 30d and trailing one year, plus distance from verified ATH
- ETF flows and fund-level outliers
- newly disclosed public-company Bitcoin purchases or sales and financing
- the most useful on-chain change for the day
- futures, leverage, funding, liquidations and options when material
- yields, Fed expectations, the dollar, oil and geopolitics, and fresh macro releases
- material regulation, custody, exchange, mining and institutional news

The reader-facing structure includes Market read, Price context, Market dynamics, On-chain, Flows, Macro, Industry news, What to ignore, Since yesterday, Watch next, and a short **Your plan** section when plan context is supplied.

It is explicitly not a price prediction or trading call. The plan section ends with whether the day's move changes a plan action.

---

## 3 · What it reads

**It does not get your whole plan by default.** The request is built as
targeted context for the page and question — the transport is literally
stamped `mode: 'prebuilt_targeted_context', full_export_sent: false`
(`src/lib/ai/planReviewClient.js`).

What goes in a request:

- **Targeted plan context** for the area under review — the app-computed
  numbers, not raw everything.
- **Page context**: which route, page, tab, section, and what's selected.
- **A label on every value.** This is the part worth pointing at. Each number
  is tagged **applied** (saved, used by projections), **draft** (typed but not
  saved), **preview** (modeled in a sandbox, not applied), **stale** (saved,
  but inputs changed since), or **unknown**. Coverage is tagged complete /
  partial / missing. Freshness is tagged fresh / stale
  (`src/lib/ai/contextContract.js`). That's why it can say "your confidence
  number is stale" instead of quoting an old number as current.

**Follow-up messages don't resend everything.** The first review reads the
full context; follow-ups replay a pruned digest so the conversation keeps
continuity without re-billing the whole payload (`api/ai/_lib/planDigest.js`).

**If it needs detail the digest dropped, it asks for it.** There are 22 read
tools — `get_holdings`, `get_accounts`, `get_debts`, `get_projection_years`,
`get_cash_flow`, `get_life_events`, `get_tax_strategy_context`,
`get_retirement_income_context`, `calculate_btc_loan_scenario`, and more
(`api/ai/_lib/reviewTools.js`). Worth knowing: **these run in your browser,
not on the server.** The server only defines the shape of the request; your
browser answers it from the plan it already has and sends back only the rows
that were actually asked for.

---

## 4 · What it never sees

- **Raw transaction rows are stripped before the request leaves your browser**
  — every time, not as a setting (`stripRawTransactionRows`,
  `src/lib/ai/contextContract.js`). It gets spending summaries and counts.
- **The Linked Accounts tool excludes** raw transactions, account masks,
  institution and account names, IDs, exact balances, and holding details.
- **The Protect tool never returns** names, contact details, letter content,
  secrets, recovery assignments, or exact storage locations. It gets counts
  and completion status — enough to say "the beneficiary row is empty,"
  never enough to say who or where.
- **Secrets are actively blocked, not just discouraged.** The heir-letter
  drafting flow scans what you type for secret-like patterns — seed phrase,
  recovery words, private key, passphrase, PIN, a safe combination, an xprv
  key, a long base58 string — and **refuses to draft** until it's removed
  (`src/lib/ai/heirLetterSafety.js`).
- **It also strips "who holds which key."** If you write something like "my
  brother has the second seed word set," that sentence is rewritten before it
  is sent, down to the category ("Multisig/collaborative custody, category
  only") with the holder mapping removed. Same file.

The canonical rule the AI itself is given, verbatim from
`knowledge/core/compliance.md`:

> "Never share seed phrases, private keys, wallet backups, passphrases, PINs,
> passwords, full account numbers, or Social Security numbers — with me or any
> AI. If you've already shared one, treat it as compromised."

---

## 5 · Where it runs, and who can train on it

- Model: **Claude Sonnet 5**, routed through OpenRouter and **pinned to
  Anthropic's own backend**. Verified live 2026-08-07 against the
  `ai_model_config` table: one `global` row reading
  `openrouter/anthropic/claude-sonnet-5`, set 2026-07-01, and no per-task or
  per-user overrides. The Sonnet 4.6 / Haiku 4.5 strings in
  `api/ai/_lib/modelResolver.js` are only the zero-config FALLBACKS; the DB row
  wins, so do NOT read the model out of that file.
- **Fixed 2026-08-07.** Between 2026-07-01 and 2026-08-07 the global row was
  the ONLY row, so every task type ran on Sonnet 5, including the three the
  code intended for Haiku (message log: Haiku traffic stops 2026-06-30, Sonnet
  5 starts 2026-07-02). Three `task_type` rows now pin
  `memory_extraction`, `intent_classification`, and `transaction_extraction`
  to `openrouter/anthropic/claude-haiku-4.5`. Everything user-facing still
  inherits the global Sonnet 5 row. Current resolution:

  | task type | resolves to | source |
  |---|---|---|
  | plan_review, plan_followup, daily_report, daily_followup, admin_test | Sonnet 5 | inherits global |
  | memory_extraction, intent_classification, transaction_extraction | Haiku 4.5 | task_type row |

  All 8 task types are editable in the app at **Admin → AI → Models**; the tab
  renders every type whether or not a row exists (empty = inherit). Changes
  apply on the next request, no deploy.
- **On camera, say "Claude Sonnet" with no version number.** The version is a
  config row that can change without a deploy, and a lesson shouldn't age out
  the next time it does. Lesson 0.2 is already written that way.
- **Every request carries `data_collection: 'deny'`** — a provider-level floor
  that excludes any inference provider that retains or trains on prompts
  (`api/ai/_lib/provider.js`). This is set on every model, not just the
  default one.
- Conversations are stored **in your own account** in Orange Plan's database,
  under row-level security, so they're readable by you and not by other users
  (`api/ai/_lib/aiLog.js`).

---

## 6 · Memory — opt-in, off by default

Off unless you turn it on. Panel: **Preferences → Memory** inside Plan Guide
(`src/components/ai/AIMemoryPanel.jsx`).

When on, it stores **how you think**, not what you own: preferences ("prefers
borrowing over selling Bitcoin," "wants concise answers"), constraints
("self-employed, variable income," "spouse not aligned on concentration"),
and standing goals ("wants to be work-optional by 55").

Hard exclusions in the extraction rules (`api/ai/_lib/userMemory.js`): no
dollar balances, no account numbers, no secrets of any kind, no one-off
question details, no transient market opinions, no advice.

Capped at **24 items**, max 4 added per review. Every item is visible in the
panel, deletable one at a time, and there's a clear-all. Toast on clear-all,
verbatim: *"Orange Plan no longer remembers anything about you."*

---

## 6a · AI Strategy Review Export

Verified against `src/components/settings/DataPrivacySettings.jsx` on 2026-08-25.

Path: **Settings → Data & Privacy → Data & backups → AI Strategy Review Export**.

- **Download AI Review Markdown** creates the privacy-scrubbed reader file.
- **Download Full JSON** creates the structured version.
- Screen copy: *"A privacy-scrubbed Markdown file for AI review. This is not a restore backup."*
- Screen warning: personal details removed; review before uploading; never share passwords, seed phrases, private keys, SSNs, account numbers, or backup passphrases.

The export is designed for another AI the user prefers. It is separate from the AES-encrypted restore backup and must never be described as a backup.

---

## 7 · What it's told it can't do

From `knowledge/core/compliance.md`, loaded by every assistant:

**Does:** teach, compare, model, calculate, prioritize, and flag what needs
professional verification.

**Never:** tells you to sell / convert / borrow / buy, claims certainty about
Bitcoin's price, states a current tax bracket or limit without a verified
source, presents a projection as a prediction, or claims to be your advisor
or fiduciary.

**Out of scope entirely:** altcoins, DeFi, NFTs, yield schemes; picking
specific tickers to buy or sell; options strategies; preparing or filing a tax
return; drafting legal instruments as legal advice; price predictions with
dates or numbers; politics.

**In scope, though people assume otherwise:** tax *planning*
math is allowed. Roth conversion comparisons, harvesting math, cost basis,
IRMAA, Social Security taxation, after-tax net worth comparisons. The boundary
is **filing and execution, not arithmetic.** The compliance file says it
directly: *"Discuss tax considerations directly instead of defaulting to 'ask
a CPA.'"* And: *"Do not bury answers in disclaimers."*

**Reviewing what you already hold is in lane** — stocks, index funds, bonds,
cash, real estate, 401(k) positions. The boundary is altcoin advocacy and
individual security *selection*, not looking at a real portfolio.

---

## 8 · The rule that matters most for trust: the app computes, the AI narrates

The instruction it gets on every review, verbatim from `api/ai/review.js`:

> "The app computes, you narrate: never perform arithmetic the plan engine
> already did. [...] Any number you derive yourself that differs from a
> plan-engine number must be labeled as an estimate."

So the surplus, the reserve status, the payoff dates, the LTV cushion, the
guardrails spending target, the success rate, the income floor — those come
from the same projection engine that draws your charts. The AI reads them and
explains them. It is explicitly forbidden from rebuilding them.

It's also told: *"Use only the plan data provided. Never invent or estimate
numbers that are not in the data. If something important is missing, say what
is missing instead of guessing."*

---

## 9 · The review always comes back in the same four sections

Locked format (`api/ai/review.js`):

1. **Planner Read** — two or three sentences: what this plan is trying to do
   and how it's going.
2. **Top 3 Things I See** — the three most consequential observations, each
   tied to your actual numbers.
3. **Next 3 Moves** — three concrete ordered steps, framed as options with
   trade-offs. Never "you should."
4. **One Question** — the single question whose answer would most improve the
   review.

If it spots a contradiction in your data, it opens with a one-line data-check
flag above Planner Read.

---

## 10 · Output is checked before you see it

- Banned strings (old assistant names) **reject the response outright**.
- Em dashes are scrubbed to commas before display — a hard formatting ban.
- Every dollar figure it emits is logged for review, because that's where a
  hallucinated number would show up.
- The check runs on each chunk **before it's flushed to the screen**, so a bad
  response is withheld mid-stream rather than shown and then retracted
  (`api/ai/review.js`, `api/ai/_lib/outputValidator.js`).

---

## 11 · Limits

Per user, per day, resetting at **midnight UTC**
(`api/ai/_lib/usageLimits.js`):

- **10 plan reviews** (a review = a new conversation)
- **100 messages**

Your reviews and action items are saved when you hit the cap.

---

## 12 · Does it know this course? — NOT YET. Say it that way.

**Current state, verified:** the knowledge repo has a `curriculum/` folder
(14 lesson files, a roadmap, and SOPs), but it is **not in the build bundle**
and **no assistant loads it**. The AI knows the app, the planning frameworks,
the compliance rules, and the domain files. It does **not** know the Academy
lessons today.

What it *would* take: add the curriculum files to the sync bundle and to the
plan-review assistant's file list. Small change, not built yet.

**So on camera:** don't promise it in the present tense. If you want to
mention it, mention it as what's coming — the honest version is "the AI knows
the app and the frameworks it's built on; teaching it this course is on the
list." Do not say it can walk someone through a lesson. It can't yet.

Update this section the day it ships, then update lesson 0.2.

---

## 13 · What's genuinely worth telling students

Ranked by what actually changes their behavior:

1. **It reads your real plan, not a generic one.** Every answer is against
   your numbers, and every number is tagged applied / draft / preview / stale,
   so it knows the difference between what you've saved and what you're
   playing with.
2. **The math is the app's, not the model's.** That's the whole reason to
   trust the numbers in an answer.
3. **Never type a secret into it, and it will stop you if you try.**
4. **The button is different on every page on purpose.** Ask from the page
   you're on and you get the workflow built for that decision.
5. **It reviews and explains. You decide.** Say this ONCE, in this lesson,
   and never again.

---

## 14 · Which workflow each lesson points at

Added to `lesson-text/` on 2026-08-07 (Austin: *"we could just mention you can
use the AI to assist you with X workflow"*). **Lesson text only, never spoken**
— the walkthroughs stay lean and this costs zero video minutes.

Every block quotes the workflow's real `intentExamples` phrase, so typing it
into Plan Guide actually routes to that workflow. All 45 title + phrase strings
were verified against `guidedWorkflowRegistry.js`. If a title or trigger phrase
changes in the app, fix it here and in the lesson text.

| lesson | workflow | phrase the student types |
|---|---|---|
| 2.1 Find your surplus | Review spending tradeoffs | "review my expenses for ways to save" |
| 2.2 Size the reserve | Set my reserve target | "set my reserve target" |
| A4.1 The price context check | Build my portfolio strategy | "help me choose my target allocation" |
| 3.1 The two ratios | Evaluate leverage capacity | "evaluate my leverage capacity" |
| A3.1 Bitcoin-backed loans | Evaluate borrowing capacity | "evaluate bitcoin borrowing capacity" |
| 5.2 Buckets, brackets, state | Identify tax planning opportunities | "identify tax planning opportunities" |
| A5.1 RMD risk + Roth | Evaluate Roth conversions | "find my Roth conversion window" |
| A5.2 Harvesting | Review harvesting opportunities | "should I harvest gains or losses" |
| 6.2 Income waterfall | Compare withdrawal strategies | "which retirement drawdown strategy fits me" |
| A6.2 Sell, borrow, or hold | Compare selling vs. borrowing | "should I sell bitcoin or borrow" |
| 7.5 Custody map | Review Protection Plan | "can my family access what they need" |
| 8.1 Executor + documents | Prepare for estate planning | "what should I ask an estate attorney" |
| 9.1 The monthly pass | Continue my plan | "what should I work on next" |
| 9.3 Scenarios | Test a planning decision | "build a scenario for this choice" |
| 9.2 How to read a plan | Review my full plan | "what should I fix first" |

The other 11 workflows already have page buttons and are covered in the
walkthroughs, so they get no text pointer.
