# Orange Plan Academy — current app delta review

**Previous app contract:** `34f42d94f4e236e6b82bad07e2b7bff0a578835e`  
**Current app main reviewed:** `bc35d739878f3daf502735d203f2677ab6565ba8`  
**Scope:** 23 app commits between those points  
**Status:** code-level teaching impact applied; deployed labels, rounding, saved state, and screenshots still require receipts

## Why this pass was required

The app added a materially better exact-fact layer for Roth, workplace Roth, HSA, conversion, tax-report, and voluntary-withdrawal behavior after the previous Academy app contract was written.

The course should teach what the current app can now store and model without pretending the app can determine legal eligibility, plan-document terms, Marketplace results, or tax-return conclusions by itself.

## Material app changes

### 1. Exact tax facts now exist as a separate input layer

Current main added an exact-fact editor, owner-specific storage, validation, readiness summaries, warnings, and report surfaces for facts that cannot be safely inferred from an account label or balance.

Relevant code includes:

- `src/components/tax/ExactTaxFactsEditor.jsx`
- `src/lib/db/exactTaxFacts.js`
- `src/lib/exactTaxFactsSummary.js`
- `src/pages/TaxCenter.jsx`
- `src/pages/taxCenter/taxCenterWarnings.js`
- `src/components/report/TaxRoadmapTimeline.jsx`
- `src/lib/annualTaxSummary.js`

**Course consequence:** missing exact facts must remain visibly unresolved. A projection can use only the facts supplied; it cannot manufacture contribution basis, participation dates, prior conversion history, or account-specific access rights.

### 2. Roth IRA history and distribution ordering became more explicit

Current main added Roth IRA history storage and projection ordering logic rather than treating the full Roth balance as one interchangeable tax-free pool.

Relevant code includes:

- `src/lib/rothIraHistory.js`
- `src/lib/rothDistributionOrdering.js`
- `src/lib/rothProjectionOrdering.js`
- `src/pages/taxCenter/RothIraHistorySettings.jsx`
- tests for Roth history, ordering, exact facts, and executed conversions

**Course consequence:** Core and Advanced must continue separating regular contribution basis, conversion amounts, earnings, owner history, and applicable five-year/access questions. The app can apply recorded facts; the CPA still owns the legal and filing conclusion.

### 3. Designated Roth workplace-plan facts became account-specific

Current main added an explicit contract for designated Roth workplace-plan facts and projection handling.

Relevant code includes:

- `src/lib/workplacePlanProjectionFacts.js`
- account create/edit payload and normalization changes
- exact designated-Roth migrations and tests

**Course consequence:** “Roth” is not enough to establish the access, basis, rollover, or distribution result. The learner must identify the wrapper and owner and enter the available exact facts.

### 4. HSA facts became explicit rather than inferred

Current main added HSA exact-fact storage, disclosure, and projection integration.

Relevant code includes:

- `src/lib/hsaProjectionFacts.js`
- `src/lib/hsaProjectionDisclosures.js`
- exact HSA migrations and integration tests

**Course consequence:** the HSA can support the Healthcare Bridge only to the extent the household has an actual account, eligible expenses, remaining balance, and records. Orange Plan can model recorded facts; it cannot prove that a reimbursement is qualified or that a premium is eligible.

### 5. Planned and executed Roth conversions are different states

Current main expanded the conversion schedule, executed-conversion entry, synchronization, annual tax summary, and report support.

Relevant code includes:

- `src/pages/taxCenter/RothConversionSchedulePanel.jsx`
- `src/pages/taxCenter/executedConversionForm.js`
- `src/lib/executedRothConversions.js`
- conversion CRUD, synchronization, and reporting tests

**Course consequence:** a proposed conversion is a comparison. A saved strategy is still not proof the custodian executed it. After execution, the actual amount and date must be recorded and reconciled.

### 6. The saved voluntary-withdrawal blend now governs tax feedback

Current main preserves the active account blend for voluntary withdrawals, including iterative tax funding. Required RMDs remain modeled separately.

The current product copy is:

> **Target mix for voluntary withdrawals, including tax funding. Required RMDs are modeled separately.**

Relevant code includes:

- `src/pages/withdrawalStrategy/AdvancedWithdrawalControls.jsx`
- `src/components/shared/runProjection.jsx`
- `src/lib/projectionWithdrawalContext.js`
- withdrawal sequencing and tax-feedback regression tests

**Course consequence:** do not teach that the base withdrawal follows the saved blend while the tax created by that withdrawal silently falls back to taxable-first. The chosen voluntary policy applies to both. RMDs are a separate required source.

### 7. Reports now expose more of the fact-readiness boundary

Current main added exact-fact summaries and warnings to report and tax surfaces.

**Course consequence:** the Academy should teach learners to read both the modeled result and its readiness state. A number can reconcile mathematically while remaining professionally qualified because an exact fact is missing.

## Lesson impact

| Lesson | Change required | Result of this pass |
|---|---|---|
| Core 5.2 | Explain exact-fact readiness, owner/account distinctions, and planned versus executed tax actions | Added to current app addendum; final spoken insertion held for UI receipt |
| Core 6.2 | State that voluntary account blends include tax funding and RMDs remain separate | Added to current app addendum and receipt plan |
| A3.1 | Preserve unresolved basis and execution evidence | No structural rewrite; receipt now includes readiness/warning state |
| A3.2 | Add exact Roth facts, planned versus executed conversions, and three-way comparison | Script and lesson text updated |
| A3.3 | Preserve lot/action execution boundary and report warning state | No structural rewrite |
| A4.1 | Use exact Roth, workplace-plan, and HSA facts without treating them as professional proof | Script and lesson text updated |
| A4.2 | Connect HSA exact facts to the Healthcare Bridge while keeping quotes/program results external | Script and lesson text updated |
| A4.3 | Apply the active voluntary blend to tax funding and keep RMDs separate | Script and lesson text updated |

## What did not change

This delta does not change:

- the one-confidence-number model,
- the 80% target logic,
- the Core demo household decision,
- the Allocation denominator,
- the sell-versus-borrow gate,
- the custody architecture,
- or the trust gate.

## Receipt holds created by this pass

Before filming, capture the current deployed state for:

1. exact-fact readiness and missing-fact warnings,
2. owner and wrapper labels,
3. Roth IRA history entry and save behavior,
4. designated Roth workplace-plan facts,
5. HSA fact entry and disclosure,
6. no/smaller/proposed conversion comparison,
7. saved strategy versus recorded executed conversion,
8. voluntary account blend including tax funding,
9. required RMD treatment shown separately,
10. annual Tax and Report readiness output.

## Dictation rule

Austin can review the stable judgment and examples now. Do not finalize the exact screen wording for Core 5.2, Core 6.2, A3.2, A4.1, A4.2, or A4.3 until the deployed receipt confirms the labels and state transitions.
