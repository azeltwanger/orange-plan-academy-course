# Orange Plan Academy — Core app-contract addendum

**App source reviewed:** `bc35d739878f3daf502735d203f2677ab6565ba8`  
**Supersedes the affected portions of:** `COURSE-APP-CONTRACT.md`  
**Affected Core lessons:** 5.2 and 6.2  
**Status:** code behavior reviewed; deployed UI receipt still required

## Why this is an addendum

The durable lesson decisions did not change, but Orange Plan added exact Roth, workplace-plan, HSA, executed-conversion, tax-readiness, and withdrawal-tax-funding behavior after the previous contract was written.

This file updates only the affected product boundary so Austin does not have to re-dictate unrelated lessons.

## Core 5.2 — Read the three tax buckets and find the useful windows

### Current app job

Orange Plan can now store and use more owner- and account-specific tax facts, including supported Roth IRA history, designated Roth workplace-plan facts, HSA facts, and executed conversion records.

The app can surface whether those exact facts are complete enough for the modeled purpose and can carry warnings into Tax and Report views.

### Teaching change

The learner should understand three levels:

1. **Account label** — taxable, traditional, Roth, HSA, workplace plan
2. **Exact fact record** — owner, contribution/history facts, conversion or participation facts, supported HSA facts, and execution record
3. **Professional conclusion** — current tax, penalty, access, filing, and program treatment

A label does not prove the exact fact. An exact fact entered into the app does not replace the CPA's legal or filing conclusion.

### Planned versus executed

A proposed Roth conversion is a planning comparison. A saved strategy remains a planned action. The actual amount and date become an executed fact only after the custodian completes the transaction and the record is reconciled.

### Final receipt required

- exact-fact readiness label and warning behavior,
- owner and account-type scope,
- saved versus executed conversion state,
- report disclosure,
- and the source field that corrects an incomplete fact.

## Core 6.2 — Choose the retirement funding and withdrawal strategy

### Current app job

The active account blend is the target mix for voluntary withdrawals, including the iterative tax funding caused by those withdrawals.

Current product wording:

> **Target mix for voluntary withdrawals, including tax funding. Required RMDs are modeled separately.**

### Teaching change

Do not teach this sequence:

- base lifestyle withdrawal follows the chosen blend,
- tax created by that withdrawal silently falls back to a hidden taxable-first order.

Teach this instead:

- the voluntary funding policy covers the full voluntary cash requirement, including its modeled tax feedback,
- an account can spill only when an eligible balance or an existing safety rule prevents the target mix,
- and required RMDs remain a separate required source rather than part of the voluntary target.

### Exact-fact boundary

The engine can use recorded Roth, workplace-plan, and HSA facts when applying a funding strategy. Missing or unresolved facts keep the access and tax result qualified.

### Final receipt required

- visible blend label,
- account-source result,
- tax-funding source reconciliation,
- required RMD separation,
- exhausted-account spill behavior,
- saved versus preview state,
- and current report parity.

## Student finish line

The learner is done when they can explain:

- which facts are labels versus exact records,
- which action is planned versus executed,
- which account mix funds voluntary spending and its tax,
- why required RMDs remain separate,
- and which unresolved fact still needs a provider or professional.
