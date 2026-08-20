# Orange Plan Academy — send-ready CPA or tax-attorney review

**Reviewer:** Bitcoin-aware US CPA or tax attorney  
**Course state:** approved synthetic inputs and reconciled app-engine candidate; deployed UI receipt pending  
**Source pass:** completed 2026-08-20 against current primary IRS authority  
**External status:** **not reviewed / not sent**

This is a narrow claim review. The reviewer is not being asked to validate Orange Plan's software, prepare a return, select an investment, or approve Austin's voice.

## Response codes

`OK` · `QUALIFY` · `CHANGE` · `CURRENT FACT` · `PROFESSIONAL ONLY` · `REMOVE`

For every non-OK response, provide:

1. the minimum corrected wording,
2. the primary authority,
3. and whether the point belongs in evergreen video, maintained lesson text, or professional implementation only.

## Claims to review

| ID | Current course position | Specific question |
|---|---|---|
| T-01 | A taxable digital-asset disposition generally creates gain or loss from amount realized minus basis in the units disposed of. | Is this accurate and sufficiently qualified for Core? |
| T-02 | Each taxable Bitcoin acquisition can have its own date/time, quantity, basis, and holding period. | Which records belong in evergreen teaching versus maintained reference? |
| T-03 | A movement between accounts or wallets owned by the same taxpayer is generally a transfer rather than a sale, with basis and holding period continuing. | Add the minimum caveat for fees, spouse/entity/IRA/LLC ownership, gifts, wrapped assets, conversions, and changed beneficial ownership. |
| T-04 | Unknown basis remains visibly unresolved. A zero-basis assumption can be a clearly labelled conservative planning test, but is not automatically the filing position. | Is this the safest consumer wording? |
| T-05 | An app FIFO/HIFO comparison affects the expected tax only when the real disposition is identified and documented under the current broker-account or unhosted-wallet rules. | Confirm the current timing, account/wallet scope, broker support, adequate-identification standard, and default earliest-acquired treatment. |
| T-06 | Taxable, traditional, Roth, and HSA accounts create different access and tax treatment. Not every traditional contribution is deductible and not every Roth distribution is qualified. | Supply the shortest durable qualifications. |
| T-07 | The applicable RMD age depends on birth year and current law. Roth IRA and designated Roth owners generally have no lifetime RMD, while beneficiary rules still apply. | Confirm exact maintained-reference wording and what should remain out of evergreen video. |
| T-08 | A lower-income period after earned income and before later Social Security/pension/RMD income can create a Roth-conversion or gain-realization window. | Identify the pro-rata, five-year, Medicare/IRMAA, Social Security, state, estimated-tax, withholding, and cash-to-pay-tax warnings essential to Core. |
| T-09 | Spending only from taxable assets can leave low ordinary-income brackets unused while traditional balances continue growing. A bracket-aware mix is worth comparing, not automatically applying. | Is the balance appropriate? |
| T-10 | Early retirement-account access is fact-specific. Rule of 55, 72(t)/SEPP, Roth IRA contribution basis, plan rules, and other exceptions are not interchangeable. | Which examples may be named in Core without teaching implementation? |
| T-11 | Proceeds from a bona fide loan are generally not income, while interest, collateral liquidation, debt cancellation, refinance, entity ownership, and estate repayment can have separate consequences. | Provide the safest Core wording and identify professional-only fact patterns. |
| T-12 | Lender liquidation of Bitcoin can create a taxable disposition even when the timing was involuntary. | Confirm basis, lot, amount-realized, and reporting caveats. |
| T-13 | The course does not assume Bitcoin-loan interest is deductible. Use and tracing of proceeds, limitations, taxpayer status, and records control. | Confirm the explicit default warning. |
| T-14 | Life-insurance death proceeds are generally excluded from federal gross income, while taxable interest, transfer-for-value/reportable-sale, ownership, and estate issues can change the result. | Confirm minimum Core qualification. |
| T-15 | Disability-benefit taxation can depend on who paid the premium and whether the employee share was paid after tax. | Confirm durable concise wording. |
| T-16 | Orange Plan is a planning model, not a return. A projected tax roadmap can identify the year and comparison while the taxpayer and professional own filing and execution. | Is this boundary clear enough? |

## Demo-specific questions

The fictional household has 1.75 BTC:

- 1.25 BTC with $48,000 known basis,
- 0.40 BTC with an exchange export available for reconstruction,
- 0.10 BTC with missing records.

The current app-engine candidate reports:

| Output | Candidate result |
|---|---:|
| Current-year modeled federal/state tax | $36,862 |
| Round Cash Flow teaching estimate | $40,000 |
| First-retirement-year modeled tax | $10,632 |
| First-retirement-year total draw | $101,948 |
| Bitcoin sale proceeds | $97,948 |
| Projected Bitcoin price | $1,235,921 |
| Bitcoin sold | 0.079251 BTC |

### T-17 · Round teaching tax estimate

The $40,000 figure exists only to make the simple working Cash Flow equation easy to follow. Whenever the current app page is being read, the course uses the app's $36,862 modeled result instead.

**Question:** Is that distinction pedagogically acceptable, or should the concept lesson use only the current app result?

### T-18 · Incomplete basis and retirement withdrawal

The funding amount can reconcile even when the tax result is not filing-grade because 0.50 BTC remains unresolved.

**Question:** Is this the right qualification?

> “The model can show how much cash the plan needs and which holding supplies it, while the tax estimate remains incomplete until the lot record is resolved or the CPA approves a filing position.”

### T-19 · First-year taxable-first source

The saved demo strategy uses taxable accounts first. The first-year source is approximately $2,200 cash, $1,800 stock, and $97,900 Bitcoin.

**Question:** Does Core need any additional warning before showing this as a household-specific funding output rather than a universal withdrawal recommendation?

### T-20 · Roth conversion roadmap

The course currently identifies a possible low-income window but does not hardcode a conversion amount.

**Question:** Which minimum fields must a learner bring to a CPA before a conversion comparison is actionable?

## Current files in scope

- `scripts/04-4_asset-location-which-account-each-holdin.md`
- `scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md`
- `scripts/05-2_taxable-tax-deferred-and-roth-bracket-wi.md`
- tax-sensitive portions of `scripts/06-1_your-spending-income-floor-gap-and-bridg.md`
- `scripts/06-2_set-your-withdrawal-order-and-refill-rul.md`
- tax statements in `scripts/08-4_insurance-term-life-disability-umbrella-.md`
- matching files under `lesson-text/`
- `demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md`

## Cleanup already completed

- No separate deterministic retirement result is taught.
- Exact RMD ages are not hardcoded into spoken Core.
- Roth is not described as having “no RMDs ever” without an owner/beneficiary qualification.
- The old $18,000 retirement-year tax/debt example and $60,000/$38,000 withdrawal split are retired.
- Temporary 2025 broker-selection relief is not described as the permanent procedure.
- A future Bitcoin sale quantity uses the projected year's Bitcoin price rather than today's reference price.
- Unresolved basis remains visible.

## Return format

| ID | Code | Corrected wording / qualification | Primary authority | Evergreen, maintained reference, or professional only |
|---|---|---|---|---|
|  |  |  |  |  |

Finish with any material Bitcoin tax issue missing from the decisions Core teaches.
