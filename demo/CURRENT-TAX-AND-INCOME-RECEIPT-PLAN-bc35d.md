# Orange Plan Academy — current Tax and Income receipt plan

**App code target:** `bc35d739878f3daf502735d203f2677ab6565ba8`  
**Status:** code contract prepared; deployed evidence not yet captured  
**Household:** approved synthetic Alex and Jordan demo  
**Privacy:** synthetic data only

## Purpose

The original engine checkpoint proves that the baseline projection and reconciled demo outputs can be reproduced. This receipt set proves the newer exact-tax-fact and voluntary-withdrawal behavior the learner will actually use.

Do not substitute a code reference for a visible receipt. Every receipt below needs the current route, labels, state, source values, rounding, and saved-versus-preview behavior.

## Receipt T1 — exact-fact readiness overview

Capture the current Tax Center or report surface that shows whether exact facts are:

- complete,
- incomplete,
- not entered,
- or not applicable.

Record:

- owner,
- account type,
- missing fact category,
- visible warning/help text,
- source-edit route,
- downstream result qualified by the missing fact,
- and whether the status is saved or calculated.

**Acceptance:** the learner can tell the difference between an account existing and its tax/access history being ready.

## Receipt T2 — Roth IRA history

Use a synthetic Roth IRA owned by the correct spouse.

Capture:

- account owner and type,
- regular contribution-history fields,
- prior distribution/history fields when present,
- conversion history or executed-conversion connection,
- save behavior,
- validation state,
- and the resulting readiness summary.

Do not place an unsupported contribution-basis amount into the Core baseline merely to make the receipt green. Unknown remains unknown unless the synthetic source record supplies it.

**Acceptance:** the app does not treat the full Roth balance as regular contribution basis.

## Receipt T3 — designated Roth workplace plan

Capture the exact-fact workflow for a designated Roth workplace account.

Record:

- owner,
- workplace-plan account type,
- participation or rollover facts requested by the current UI,
- save behavior,
- and the distinction from Roth IRA history.

**Acceptance:** the course can show why “Roth” is not one interchangeable record.

## Receipt T4 — HSA exact facts

Capture:

- owner,
- HSA account,
- current eligibility/coverage facts requested by the UI,
- qualified-use or reimbursement facts requested by the UI,
- disclosures or warnings,
- save behavior,
- and resulting readiness state.

No real medical detail is required. Use synthetic categories and amounts only.

**Acceptance:** the learner understands that the balance alone does not establish a tax-free reimbursement for every health expense or premium.

## Receipt T5 — conversion comparison

On the current conversion workflow, compare:

1. no conversion,
2. a smaller synthetic amount,
3. the proposed ceiling amount.

Record:

- tax year,
- owner/account source,
- selected ceiling or comparison amount,
- current modeled tax,
- tax-payment source,
- traditional/Roth balance effects,
- exact-fact readiness shown beside the result,
- saved Baseline versus Preview/Scenario state,
- and what remains professional-only.

**Acceptance:** the preview is not presented as an executed conversion or a filing conclusion.

## Receipt T6 — executed conversion record

Use a separate synthetic executed transaction.

Capture:

- how a completed conversion is entered or imported,
- transaction date and owner/account connection,
- withholding or cash-tax treatment when the UI supports it,
- save behavior,
- and how the executed record differs from the proposed strategy.

**Acceptance:** the app and course do not blur planning intent with a transaction that actually occurred.

## Receipt I1 — voluntary withdrawal blend

Use one retirement year with a voluntary account blend.

Capture:

- total spendable-cash need,
- target account mix,
- base voluntary withdrawals,
- iterative tax/penalty funding created by those withdrawals,
- final source totals by account,
- and any spill only after an eligible target source is exhausted or blocked by a documented safety rule.

**Acceptance:** the chosen voluntary blend remains the target for voluntary tax feedback rather than falling silently to an unrelated taxable-first order.

## Receipt I2 — required and direct-withholding separation

On the same or a second synthetic year, show separately:

- required RMD funding,
- voluntary withdrawal funding,
- direct custodian conversion withholding when present,
- and the total account-source reconciliation.

**Acceptance:** required distributions and direct withholding are not described as ordinary voluntary-blend funding.

## Receipt I3 — report and year-detail provenance

Capture the report or year-detail surface that traces:

- total need,
- recurring income,
- account draw,
- tax created by funding,
- exact-fact readiness,
- and the source location for correction.

**Acceptance:** a learner can answer “where did this number come from?” without guessing from the account balance.

## Receipt data contract

For each receipt, record:

```yaml
receipt_id:
app_commit:
route:
verified_date:
owner:
account_type:
state: saved_baseline | unsaved_input | preview | scenario | executed_record | read_only_output
visible_labels:
inputs:
outputs:
source_reconciliation:
readiness_status:
rounding:
external_proof_owner:
professional_hold:
screenshot_or_recording_reference:
austin_acceptance:
```

## Completion rule

This receipt set is accepted only when:

- every visible label and state has been checked in the deployed app,
- the approved synthetic household or clearly isolated synthetic transaction is used,
- no unknown fact is invented,
- all account-source totals reconcile,
- the current app commit and verification date are recorded,
- and the affected Core and Advanced scripts use the same meaning and limitation.
