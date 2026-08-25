# Orange Plan Academy — current app delta review

**Status:** code-level course impact pass complete; deployed UI receipts still required  
**Previous Advanced app review:** `34f42d94f4e236e6b82bad07e2b7bff0a578835e`  
**Current app code reviewed through:** `bc35d739878f3daf502735d203f2677ab6565ba8`  
**Review date:** 2026-08-25

## Why this pass was required

Orange Plan changed materially after the first Core and Advanced app contracts were written. The later app added exact Roth, workplace-plan, and HSA fact records; applied those records inside projection and reporting; changed how voluntary withdrawal blends fund their own tax feedback; and surfaced more explicit readiness and warning states.

Those are not cosmetic changes. They alter what the Academy should tell a learner to verify before relying on a conversion, an early-retirement access source, an HSA reimbursement, or a withdrawal blend.

## Current product changes that affect the course

### 1. Exact tax facts now sit underneath broad account labels

The app now distinguishes account labels from the facts needed to model their tax and access behavior. Relevant current code and tests cover:

- Roth IRA contribution and distribution history,
- executed Roth conversions and conversion history,
- designated Roth workplace-plan facts,
- HSA eligibility and qualified-use facts,
- owner-specific fact loading,
- projection ordering and tax-free distribution tracking,
- and report/readiness warnings when exact facts are incomplete.

**Course consequence:** “Roth,” “workplace Roth,” and “HSA” can no longer be taught as sufficient facts by themselves. The learner must know which exact facts are present, which remain unknown, and which conclusion stays provisional.

### 2. Roth access is an evidence problem, not a balance-label shortcut

The app can now use owner-specific Roth IRA history and ordering facts. A Roth balance may contain regular contribution basis, conversion dollars with different dates, and earnings. Those components can have different tax and additional-tax treatment.

**Course consequence:** Core still teaches the three tax pools. Advanced A3.2 and A4.1 teach the exact-history gate. The Academy must not call the entire Roth balance an available early-retirement Bridge or imply that one five-year sentence resolves every Roth dollar.

### 3. Workplace Roth and Roth IRA are not interchangeable records

The app now has an exact designated-Roth workplace-plan contract in addition to Roth IRA history. Plan participation, rollover, and account-specific facts can affect what the projection may safely infer.

**Course consequence:** scripts must name the actual account type and owner. A workplace Roth label cannot silently inherit Roth IRA contribution-basis logic.

### 4. HSA modeling now requires exact eligibility and use facts

The app now contains exact HSA fact handling and projection disclosures. The account balance alone does not establish that every dollar can fund any healthcare or premium expense tax-free.

**Course consequence:** Core can assign the HSA the job of Healthcare Bridge. Advanced A4.1–A4.3 must require qualified-expense records and current eligibility facts before treating a specific reimbursement as available.

### 5. Voluntary withdrawal blends now fund their own tax feedback

The current withdrawal engine applies the active account blend to voluntary funding, including iterative taxes, penalties, and positive Social Security-taxability true-ups. Required distributions and direct custodian conversion withholding remain separate.

**Course consequence:** Core 6.2 must distinguish:

- the household’s voluntary withdrawal target mix,
- required RMD funding,
- and direct conversion withholding.

The lesson should no longer imply that tax created by a blended withdrawal silently falls to a hidden taxable-first order when the chosen accounts still have eligible capacity.

### 6. Conversion and withdrawal comparisons have stronger readiness boundaries

The current Tax Center, projection engine, reports, and warnings can carry exact-fact readiness through the plan. A calculated result can still be provisional when owner history, basis, plan documents, healthcare facts, or a real execution record is incomplete.

**Course consequence:** an app result and a filing/execution conclusion remain different layers. The course should show what Orange Plan knows, what it is conservatively inferring, and what the CPA or provider must confirm.

## Lesson impact decisions

| Lesson | Impact | Required course change |
|---|---|---|
| Core 4.3 · Next dollar | Minor | Keep HSA routing conditional on eligibility and employer contributions; do not imply the account label proves current contribution eligibility. |
| Core 5.2 · Tax pools/windows | Material | Add exact-fact readiness: broad pool first, owner/account history second, professional execution third. |
| Core 6.2 · Withdrawal strategy | Material | Teach that the selected voluntary account mix also funds its modeled tax feedback; keep RMDs and direct conversion withholding separate. |
| Advanced A3.2 · Roth conversion | Material | Require owner-specific Roth/workplace-plan history and distinguish conversion preview from executed conversion records. |
| Advanced A4.1 · Access Bridge | Material | Build the map from exact supported amounts, not full account balances; name Roth IRA, workplace plan, and HSA evidence separately. |
| Advanced A4.2 · Healthcare | Moderate | Keep HSA as a qualified source only after exact facts and receipts support it; the app still does not replace a current coverage quote. |
| Advanced A4.3 · Integrated funding | Material | Use the current voluntary blend and exact-fact readiness when comparing spendable cash, taxes, healthcare, and Bridge survival. |
| Reports / capstone | Moderate | Surface whether exact facts are complete, incomplete, or not applicable rather than displaying one unqualified tax-ready status. |

## Teaching model after this pass

Use three layers whenever a Roth, workplace plan, HSA, conversion, or early withdrawal appears:

1. **Account label** — what wrapper is this?
2. **Exact facts** — which owner, contributions, conversions, earnings, plan terms, eligibility, and records actually apply?
3. **Execution proof** — what did the provider, tax record, plan administrator, or professional confirm?

Orange Plan can calculate only from the facts it has. The Academy should never turn a missing exact fact into a confident account-access or tax conclusion.

## Receipt requirements created by this delta

Before final filming, capture current deployed evidence for:

- exact-fact readiness and warning language,
- Roth IRA history entry and save behavior,
- designated Roth workplace-plan facts,
- HSA exact facts and disclosures,
- no / smaller / proposed Roth conversion comparison,
- executed conversion versus proposed conversion state,
- voluntary account blend and tax-feedback source reconciliation,
- required-distribution separation,
- direct conversion-withholding separation,
- report output when exact facts are incomplete,
- and the source location for correcting each fact.

## What this pass does not claim

This review does not establish that:

- the deployed UI exactly matches the code path,
- the demo household’s exact facts have been entered and accepted,
- a Roth or HSA amount is legally available,
- an employer plan permits a particular distribution,
- a conversion amount is appropriate,
- or a tax return will match the projection.

Those remain UI, plan-document, provider, record, and professional gates.

## Course release rule

The changed lessons may enter Austin’s voice-and-judgment review after the script and lesson text incorporate this delta. They become final only after the current app receipts and applicable CPA/plan/healthcare evidence are applied, followed by one clean Austin read.
