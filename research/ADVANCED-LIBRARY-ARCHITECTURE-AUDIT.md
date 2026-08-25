# Advanced Library architecture audit

**Status:** Core references and Advanced taxonomy are locked; individual Advanced scripts still require a later app, factual, and voice pass  
**Purpose:** prevent Core from sending learners into a bloated, contradictory, or required-feeling Advanced library after Austin has already approved the Core wording.

## Decision

Keep the Advanced Library, but treat it as a **conditional reference system**, not a second linear course.

A learner does not watch Advanced in order. The app or Core decision reveals a condition; the learner follows one link, solves that condition, and returns to the plan.

Every Advanced lesson begins:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced never counts toward Core progress merely because the content exists.

## Stable Advanced sections

1. **Modeling and assumptions**
2. **Bitcoin-backed borrowing and leverage**
3. **Tax optimization and implementation**
4. **Early-retirement access and healthcare**
5. **Advanced custody**
6. **Trusts and complex estate planning**

Do not add a seventh catch-all section unless a repeated plan-visible condition does not fit one of these.

---

# 1 · Modeling and assumptions

## Gate

Watch only when the learner needs to understand or change the model beyond selecting and interpreting the standard Plan assumptions.

## Keep

- How the 1,000 test runs vary returns and inflation
- Why confidence is a planning measure rather than a guarantee
- Power Law / declining-return assumptions and sensitivity
- One-variable stress testing
- Holding-specific return and cash-yield overrides
- Data freshness and model-version limits

## Merge

- Monte Carlo mechanics and confidence mechanics belong in one reference sequence.
- Power Law and declining-return rationale belong in the same sequence rather than separate competing models.
- Holding-specific assumptions should be a short applied reference, not a long standalone lecture.

## Remove from Advanced

- Re-teaching the four Plan values from Core 1.3
- A second deterministic-versus-Monte-Carlo framework
- Advice to customize every holding merely because the control exists
- Probability theory that does not change a planning decision

## Core links

- 1.2 · assumptions and holding override
- 1.3 · confidence interpretation
- 9.2 · weaker-return and inflation Scenarios

---

# 2 · Bitcoin-backed borrowing and leverage

## Gate

Watch only when the learner already has a Bitcoin-backed loan or is actively deciding whether to borrow.

## Recommended sequence

1. **What the loan changes** — liability, interest, collateral, custody, tax, and estate
2. **LTV and survivability** — lender definitions, call/liquidation rules, top-up resources, and the price path the household can withstand
3. **Cash-flow and repayment plan** — interest, refinance, payoff, income, and loan-at-death
4. **Sell-versus-borrow comparison** — after-tax cash, Bitcoin retained, interest, collateral, counterparty risk, and ending liability
5. **Operational checklist** — provider terms, custody, auto top-up, monitoring, records, and exit rules

## Merge

- “Sell versus borrow” is the decision output of the borrowing sequence, not a separate philosophy module.
- Current-strategy loans and retirement borrowing should share one risk framework, with different timing examples.
- LTV, liquidation, and top-up mechanics belong together.

## Keep out of Core

- Normalizing a 50% starting LTV
- Universal lender rankings
- Interest-only versus amortizing slogans
- Treating loan proceeds as free tax savings
- Assuming interest deductibility
- Relying on one price path or ending-net-worth result
- Borrowing as the condition that makes retirement possible

## Required professional / current-reference gates

- Actual lender agreement and current product rules
- Tax treatment of interest, liquidation, cancellation, refinance, and entity/retirement-account ownership
- Estate repayment and collateral authority

## Core links

- 3.1 · existing Bitcoin-backed debt
- 6.2 · sell / hold / borrow decision
- Protect · lender/collateral custody and family process

---

# 3 · Tax optimization and implementation

## Gate

Watch only when the current tax roadmap, lots, or life stage shows a specific opportunity.

## Separate lessons by trigger

### Cost-basis reconstruction and identification

Trigger: unresolved lots or a planned taxable sale.

Advanced owns broker/wallet identification procedure, record timing, fee treatment, ownership changes, and current reporting implementation.

### Roth-conversion sizing

Trigger: meaningful traditional balance plus a possible lower-income window.

Advanced owns bracket ceiling, pro-rata rule, five-year considerations, Medicare/IRMAA, Social Security, state, withholding/estimated tax, cash to pay tax, and implementation calendar.

### Gain or loss harvesting

Trigger: current taxable lots plus a real gain/loss opportunity.

Advanced owns current law, identification, replacement/reacquisition treatment, carryovers, state interaction, and execution.

### State relocation

Trigger: a genuine move under consideration.

Advanced owns residency, domicile, sourcing, timing, state treatment, and lifestyle/legal implementation. Do not make relocation a tax-only recommendation.

### Account-access methods

Trigger: retirement before ordinary access and an uncovered Bridge.

Coordinate with the Retirement section below rather than duplicating Rule of 55, 72(t), and Roth-basis material in two places.

## Merge

- “Tax roadmap” remains Core; Advanced lessons begin at the specific action.
- RMD reduction belongs inside conversion sizing rather than a standalone fear lesson.
- 0% gain harvesting belongs with the harvesting trigger, not as a universal annual task.

## Remove / avoid

- Exact annual thresholds hardcoded in evergreen video
- “Fill the bracket” without the other income-based consequences
- “No RMDs ever” without owner/beneficiary distinction
- App lot-method preview treated as real execution
- State-tax savings shown without residency and lifestyle costs

## Core links

- 5.1 · basis readiness
- 5.2 · tax window and current action
- 6.2 · bracket-aware retirement funding
- 8.4 · life/disability tax coordination when relevant

---

# 4 · Early-retirement access and healthcare

## Gate

Watch only when the household retires before Medicare or lacks enough accessible Bridge money before the intended retirement-account access method.

## Recommended sequence

1. **Map the access Bridge** — taxable assets, cash, HSA, account rules, and year-by-year need
2. **Account-access options** — identify methods that may apply; do not teach them as interchangeable
3. **Pre-Medicare healthcare** — premiums, out-of-pocket costs, subsidies/credits, income interactions, HSA use, and state/household specifics
4. **Test the combined plan** — access, tax, healthcare, and retirement-income effects in the same Scenario

## Merge

- Rule of 55, Roth contribution basis, 72(t)/SEPP, and other methods belong under one “access options” reference with separate implementation warnings.
- Pre-Medicare healthcare and conversion sizing cross-link because income decisions can affect healthcare costs.

## Keep out of Core

- “Everything unlocks at 59½”
- A universal account-access order
- Treating the HSA as unrestricted Bridge cash
- A national healthcare-cost estimate presented as the household's answer
- Detailed current subsidy thresholds in evergreen video

## Core links

- 4.2 · Healthcare Bridge job
- 4.4 · wrapper/access trade-offs
- 6.1 · account-access Bridge
- 6.2 · retirement funding phases

---

# 5 · Advanced custody

## Gate

Watch only when the current single-signature or third-party setup fails the household's dual-control, redundancy, family, privacy, or consequence-of-loss requirements.

## Recommended sequence

1. **Passphrase decision** — exact-wallet behavior, plausible-deniability claims, backup, compatibility, family recovery, and permanent-loss risk
2. **Collaborative custody** — threshold, provider role, fees, privacy, succession, provider-independent recovery, and inheritance process
3. **DIY multisig** — threshold, keys, coordinator, descriptor/configuration, verification, maintenance, privacy, and family execution
4. **Practice and migration** — test wallet, address verification, source-device safety, small transfer, recovery evidence, and rollback plan

## Merge

- All multi-key designs share one dual-control/redundancy framework from Core 8.2.
- Provider comparison belongs inside collaborative custody, not a universal brand lesson.
- Descriptor/configuration records belong with multisig recovery, not as a generic document.

## Keep out of Core

- Hand-splitting ordinary seed words
- A passphrase as the default “family-ready” level
- A universal instruction to wipe the only meaningful device
- “More advanced is safer”
- Calling a provider-assisted design noncustodial without explaining threshold and recovery
- Treating a descriptor as harmless public information with no privacy consequence

## Required current-reference gate

The exact device, wallet standard, coordinator, provider, and recovery process must be verified at recording/implementation time.

## Core links

- 7.1 · custody level and job
- 7.2 · recovery proof
- 7.3 · failure domains
- 8.2 · dual control and redundancy

---

# 6 · Trusts and complex estate planning

## Gate

Watch only when counsel identifies a probate, incapacity, privacy, control, tax, creditor, minor/special-needs, blended-family, business, or estate-size trigger.

## Recommended sequence

1. **Does a trust solve a real problem?**
2. **Revocable trust implementation questions** — titling, incapacity, probate, privacy, trustee/successor, provider and custody coordination
3. **Irrevocable / estate-tax planning questions** — transfer, control, gift/estate consequences, valuation, basis, trustee powers, creditor/family concerns
4. **Bitcoin custody inside the legal design** — authority, threshold, key holders, provider records, privacy, succession, and recovery
5. **Retirement accounts and beneficiary trusts** — attorney/CPA coordination; do not treat like ordinary retitling

## Merge

- “Bitcoin in a trust” is not one universal strategy; it belongs inside the legal job the trust is solving.
- Estate-tax planning, creditor planning, and control planning should not be blended into a single “irrevocable wins” lesson.
- Custody and legal authority remain linked but separate responsibilities.

## Remove / avoid

- “Future Bitcoin growth escapes the estate” as a universal claim
- “Trusts avoid tax” without the exact structure and transfer consequences
- Telling every Bitcoin holder to use a trust
- Universal executor/heir separation
- Universal seed/passphrase distribution
- A four-key picture labelled 2-of-3
- A fixed dead-man-switch interval in evergreen video
- Advising a trust or fiduciary to ignore diversification duties without state-specific counsel and governing-document analysis

## Required professional gate

A current attorney licensed in the household's state and the appropriate tax professional own implementation.

## Core links

- 8.1 · roles, documents, and provider records
- 8.2 · legal authority versus technical access
- 8.3 · heir letter and discovery
- 8.4 · estate liquidity and insurance coordination

---

# Topics that do not deserve a standalone Advanced lesson

Unless a real plan-visible trigger emerges, keep these as short reference sections or merge them into the sequences above:

- General “advanced allocation and behavior” after Core already teaches target, band, and drawdown
- One holding-specific override per video
- Generic “Bitcoin retirement philosophy”
- A feature tour of every Scenario control
- A list of every tax strategy without a current opportunity
- Product/provider rankings that age quickly
- Detailed contribution-limit recitation
- A glossary video

## Advanced lesson standard

Each Advanced lesson must include:

1. **Gate** — who needs this now?
2. **Problem** — what plan-visible risk or opportunity exists?
3. **Decision** — what must the learner choose?
4. **Trade-off** — what improves and what gets more complex or fragile?
5. **App comparison** — what can Orange Plan model or record?
6. **Implementation owner** — learner, provider, CPA, attorney, custody practitioner, or insurer
7. **Stop signs** — when not to proceed
8. **Done when** — evidence rather than mere intent
9. **Return path** — which Core/Build Your Plan area receives the decision

## Recommended production order after Core

Produce Advanced by demand and consequence, not by existing file number:

1. Cost-basis identification and Roth-conversion sizing
2. Bitcoin-backed loan survivability and sell-versus-borrow
3. Pre-Medicare healthcare and account access
4. Collaborative custody, DIY multisig, and passphrase
5. Trust gate and Bitcoin/legal coordination
6. Model mechanics and holding overrides as maintained reference

The actual learner questions, support volume, and plan-trigger counts should refine this order.

## Core impact decision

No Core module or lesson needs to move because of the Advanced audit.

Before Austin's Core read, only the cross-links and gates must remain stable. The individual Advanced scripts can receive their later voice/app/professional pass without forcing a re-dictation of Core, provided the six-section taxonomy and gate wording remain intact.
