# Orange Plan Academy — course ↔ app contract

**Status:** active pre-dictation contract  
**App source verified:** customer-facing concept review against `azeltwanger/orange-plan` `main` at `8019bfcf14387f2e15746b18707534bfcb7eb4e5` on 2026-08-19  
**Reproducible demo engine:** `course-support/academy-demo-checkpoints` at `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5` on 2026-08-20  
**Course branch:** `course-repair/app-match-voice-pass`  
**Exact walkthrough status:** hold until Austin completes the deployed Build Your Plan flow end to end

## The contract

Orange Plan owns saved data, calculations, visible product state, and app completion rules.

The Academy owns:

- the durable financial-planning concept,
- the trade-off,
- Austin's judgment,
- the continuous teaching example,
- the question the household must answer,
- and the human planning finish line.

A learner should finish each planning area able to answer:

1. What decision did I make?
2. Where did the important number come from?
3. What changed in the plan?
4. What remains a preview, Scenario, or real-world/professional action?

The course must not become a textbook disconnected from implementation or a click tour that breaks every time a control moves.

## Authority when sources disagree

1. Accepted deployed app behavior and current calculation
2. Austin-approved planning judgment
3. Verified mathematical, tax, legal, custody, and insurance facts
4. Approved demo decision and accepted checkpoint receipt
5. This contract and `CURRENT-COURSE.md`
6. Current script and lesson text
7. Versioned walkthrough
8. Visual
9. Old coaching deck, generated bundle, or specification

A mockup, code branch, old route, or specification does not prove a customer-facing feature has shipped.

## Durable teaching loop

Every Core area follows the same loop:

1. Name the decision.
2. Teach only the concept required to make it intelligently.
3. Show what gets better, worse, or more fragile.
4. Continue the same fictional household.
5. Trace the important number to its source.
6. State Austin's planning judgment without presenting it as a universal command.
7. End with the learner's decision and a checkable finish line.
8. Use a versioned walkthrough to implement it in the accepted app.

The concept video avoids temporary click paths. The walkthrough owns route, label, save behavior, screenshot, and app version.

## Number provenance

The first time an important output appears in a planning area, teach:

- **WHAT IT MEANS** — the question it answers
- **CALCULATED FROM** — source inputs and saved strategy
- **EDIT SOURCE** — where the real source changes
- **THIS AFFECTS** — downstream results that should move

The promise is not that every output maps to one database column. The promise is that the learner can explain which facts and decisions created it.

## Saved input, preview, Scenario, and read-only output

The old app-wide rule “If you did not click Apply, it did not happen” is false.

Orange Plan has distinct product states:

- **Saved input** — part of the working plan under the page's own save behavior
- **Preview** — comparison result that has not changed the saved strategy
- **Scenario** — a saved question beside the baseline
- **Read-only output** — calculated result changed at its source rather than directly

Every walkthrough names the state being viewed. A page-specific rule is never taught as a universal app rule.

# Current product contracts used by Core

## Household retirement date

The current model uses one household retirement date anchored to the primary person's age.

For the canonical demo:

- retirement is shown as Alex age 55,
- the household earned-income transition follows that date,
- a March retirement date creates partial-year household wages,
- Jordan does not retain W-2 income for two additional years merely because Jordan is younger,
- and each spouse's Social Security still has its own start age.

The course must not imply a separate spouse retirement-age control that the app does not have.

## Plan → Retirement confidence

The current inputs are:

- planned household retirement age,
- Baseline retirement spending,
- confidence target.

The target:

- defaults to 80%,
- accepts whole percentages from 50% through 99%,
- represents the minimum share of 1,000 test runs that must remain funded through planning age,
- and is used to find the earliest retirement date reaching the selected target.

Confidence at the planned date and the earliest target-qualified date come from the same test-run framework. Core does not teach a second deterministic retirement result beside them.

Canonical engine candidate:

- confidence at Alex age 55: 94.6%,
- earliest 80% date: May 2032 / Alex age 51.

Final walkthrough wording still waits for the visible UI receipt.

## Cash Flow and Debt ownership

Cash Flow separates:

- income,
- modeled tax,
- living spending,
- Debt,
- surplus available after the saved debt treatment,
- account routing,
- and remaining cushion.

For the canonical demo:

- required debt is approximately $1,833/month,
- saved extra auto principal is $500/month,
- planned Debt is approximately $2,333/month,
- post-debt surplus is approximately $3,761/month,
- account routing is $3,500/month,
- operating cushion is approximately $261/month.

The course may describe the full household decision as $4,000/month only when it explicitly means:

> $500 extra debt + $3,500 account contributions

The $500 cannot be subtracted or routed twice.

## Allocation scope

The current Allocation builder excludes:

- the primary residence,
- beneficiary-restricted accounts such as the 529.

Canonical candidate:

- app allocatable portfolio: $270,000,
- Bitcoin: $175,000,
- current Bitcoin allocation: 64.8%,
- target: 50%,
- review band: 40–60%.

The household is above the review band. The product/course response is **review**, not an automatic taxable sale.

A broader $295,000 financial-balance denominator including the 529 and a $745,000 gross-asset denominator including the home answer different questions. The lesson must name the denominator.

## Holding-specific projection assumptions

Broad Plan assumptions remain the default.

A holding override is used only when the broad class would model the actual exposure incorrectly, such as a spot Bitcoin ETF classified broadly as a stock. Return and cash yield remain separate concepts.

## Plan → Income

Income contains separate decisions:

1. current Plan spending,
2. calculated starting-spending reference choices,
3. withdrawal/account/asset strategy,
4. annual spending policy,
5. reserve-refill behavior,
6. optional borrow-versus-sell comparison when relevant.

Canonical spending references:

- Conservative / 95%: $99,317/year
- Current Plan: $100,000/year at 94.6%
- Balanced / 80%: $170,216/year
- Aggressive / 60%: $249,904/year

The demo keeps $100,000 because that is the lifestyle the household chose. The calculated choices show capacity; they do not instruct the household to maximize spending.

The current annual policy uses:

- lower trigger 60%,
- target 80%,
- upper trigger 95%,
- maximum one-year correction 10% toward the target amount.

The course identifies these as Orange Plan product defaults assembled from researched components, not one published researcher's exact parameter set.

## First retirement-year funding

The first retirement calendar year begins in March 2036 and includes partial-year household wages, inflation-adjusted part-time income, college, remaining debt, and tax.

Canonical candidate:

- total need: $171,383,
- recurring income: $69,435,
- total draw: $101,948,
- rounded taxable source total: $101,946,
- Bitcoin sale proceeds: $97,948,
- projected Bitcoin price: $1,235,921,
- Bitcoin sold: 0.079251 BTC.

The dollar sale, projected price, and units must come from the same projection year. The course never divides future sale dollars by today's fixture price.

Incomplete basis for 0.50 BTC keeps the tax estimate professionally qualified even when the cash-funding equation reconciles.

## Scenarios

A Scenario is a question beside the baseline. It changes only the selected overrides.

Canonical stress example:

- 3% baseline inflation: 94.6% confidence,
- 4% inflation Scenario: 91.6%,
- delta: −3.0 percentage points.

The course does not invent an earliest-date or estate delta when that comparison is not shown.

## Protect and real-world proof

Protect can track people, documents, status, and dates. It cannot prove:

- a wallet backup works,
- another family member can recover,
- a legal document is valid,
- a provider accepted a beneficiary designation,
- or an insurance contract supplies the stated coverage.

The walkthrough states both the app completion rule and the human/real-world finish line.

No seed phrase, private key, passphrase, PIN, password, wallet backup, xprv, authentication code, full account number, or exact custody location goes into Orange Plan, a course document, screenshot, AI tool, or review packet.

## Encrypted export

Orange Plan currently creates a passphrase-protected encrypted export for secure storage and portability.

**In-app plan restore is temporarily unavailable.** Therefore:

- the course does not call the export a restore the learner can use today,
- the active plan and source records remain intact,
- the passphrase is stored separately,
- and a future import walkthrough requires a fresh product verification.

The readable PDF and encrypted export have different jobs. Neither contains Bitcoin secrets.

## Build Your Plan

The concept architecture is complete, but exact Build Your Plan metadata remains preview-dependent.

No walkthrough is recorded until Austin has used the deployed flow end to end and the course records:

- stable step ID,
- current label,
- primary route,
- save/apply/autosave behavior,
- app completion rule,
- human planning finish line,
- relevant lesson IDs,
- number keys,
- and accepted app commit.

Spoken concepts use durable planning-area names rather than temporary step numbers.

# Continuous demo and receipts

Core uses `DEMO-HOUSEHOLD.md` unless an example is explicitly labelled **illustrative — not the demo household**.

Authority order:

1. Austin-approved demo decision
2. human-readable demo source
3. machine-readable fixture
4. current app engine and deployed synthetic account
5. accepted checkpoint receipt

The current reconciled engine candidate may finish script arithmetic and visual briefs. A screenshot-level claim waits for the deployed page to confirm visible label, rounding, source rows, and state.

Every walkthrough begins with fixture version and starting checkpoint and ends with:

- what changed,
- ending checkpoint,
- app completion rule,
- human finish line,
- and unresolved professional or real-world proof.

# Core map

| Module | Human decision | Durable app area | Important outputs | Human finish line |
|---|---|---|---|---|
| 0 · Start Here | How the learner uses the app, Academy, AI, and security boundary | AI Review / privacy | Engine result vs AI explanation | Learner can state app-calculates / AI-explains / learner-decides and the no-secrets rule |
| 1 · Baseline | Facts, expected changes, assumptions, spending, confidence target | Accounts, onboarding, Plan | Net worth, confidence, earliest target-qualified date | First plan is honest about verified, estimated, and missing data |
| 2 · Cash Flow | Normal and bare-bones spending, repeatable route, reserve, known costs | Cash Flow | Tax, Debt, post-debt surplus, route, reserve | Learner can rebuild the source equation without double-counting debt |
| 3 · Debt | Treatment for each debt and household ceiling | Debt | DTI, DTA, payment, payoff | Every debt has a reasoned treatment that preserves liquidity |
| 4 · Allocation | Target, band, jobs, location, and next-dollar route | Allocation + Cash Flow | Scope, current/target mix, drawdown, route | Learner can name the denominator, dollar drawdown, and recurring route |
| 5 · Tax | Basis readiness and one action, CPA question, or pass | Tax | Quantity, basis status, roadmap | Unresolved data stays visible and execution remains professional |
| 6 · Income | Spending, income floor, draw, sources, paycheck, annual policy | Plan → Income | Need, income, draw, source split, BTC sold, spending choices | Retirement paycheck and funding strategy reconcile and can be explained |
| 7 · Custody | Recoverable custody for each balance | Protect + real custody | Checklist status only | Receive, send, recovery, family practice, and failure-domain work are real |
| 8 · Estate / Insurance | Who acts, which records control, how family starts, which gaps remain | Protect + professional/provider records | Readiness and gaps | Legal authority, technical process, and family instructions connect without secrets |
| 9 · Maintain / Test | Review cadence, Scenarios, capstone, annual records | Transactions, Scenarios, Report | Scenario delta, report, action list | Learner can explain the plan in six sentences and owns one to three actions |

# Core versus Advanced

Core teaches the concepts every learner needs for a usable plan.

Advanced begins only when a condition is visible in the learner's plan. Every Advanced lesson opens with:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced includes detailed model mechanics, Bitcoin-backed loans, conversion sizing, harvesting, relocation, special account-access methods, pre-Medicare healthcare, passphrases, multisig implementation, trusts, estate tax, and complex insurance analysis.

# Change-impact rule

Every customer-facing app change should be classified:

- `none`
- `concept update`
- `walkthrough update`
- `demo-account update`
- `professional/reference update`

When the app changes:

1. update this contract and the crosswalk,
2. rerun the affected synthetic checkpoint,
3. update the concept only when the decision or explanation changed,
4. update the walkthrough when implementation changed,
5. update the visual when it became false,
6. rerun the full Academy audit.

This keeps Orange Plan Academy matched to the product without rerecording the entire course after every UI change.
