# Orange Plan Academy — Advanced demonstration receipts

**Purpose:** prevent Advanced screen-shares and provider/device demonstrations from becoming unversioned click tours or unsupported implementation claims.

Every receipt uses synthetic or redacted data. It contains no seed phrase, private key, passphrase, PIN, password, xprv, authentication code, real account number, client record, or Austin personal-plan data.

## Required receipt fields

Each demonstration records:

- demo ID and lesson IDs,
- learner gate and decision,
- app commit / provider / device / document version,
- verification date,
- synthetic or redacted inputs,
- exact route, labels and save/preview state when Orange Plan is used,
- output values and number-provenance keys,
- external evidence owner,
- professional-review status and claim IDs,
- screenshot or recording references,
- result and unresolved holds,
- return-to-Core action,
- and Austin's final approval status.

The schema is `demo/advanced-demo-receipt.schema.json`.

## Receipt roster

| Demo | Supports | Primary proof | Current status |
|---|---|---|---|
| **AD1 · Inspect assumptions and holding overrides** | A1.1–A1.2 | Current app labels, model/version, saved Scenario and holding override | HOLD — UI/model receipt |
| **AD2 · Model a Bitcoin-backed loan and drawdown** | A2.1–A2.3 | Synthetic loan in current app; same-cash-need reconciliation | HOLD — current UI + CPA/lending review |
| **AD3 · Read a lender agreement and write the exit** | A2.4 | Redacted agreement version and claim-level legal/lending review | HOLD — agreement/reviewer |
| **AD4 · Reconstruct lots and prepare a sale packet** | A3.1 | Synthetic transaction chain, quantity reconciliation and provider identification evidence | HOLD — CPA/current procedure |
| **AD5 · Compare conversion, harvesting and relocation Scenarios** | A3.2–A3.4 | Current app Scenarios plus maintained tax/state worksheet | HOLD — CPA/UI/state facts |
| **AD6 · Build the pre-59½ and healthcare Bridge** | A4.1–A4.3 | Plan documents, synthetic quote worksheet and same-cash-need comparison | HOLD — plan/quote/CPA/health review |
| **AD7 · Passphrase practice wallet** | A5.1 | Practice wallet using the exact current device procedure | HOLD — device/custody review |
| **AD8 · Compare and recover a 2-of-3 wallet** | A5.2–A5.3 | Practice wallet, configuration record, intended and alternate recovery combinations | HOLD — provider/device/custody review |
| **AD9 · Trust ownership and authority matrix** | A6.1–A6.2 | Synthetic matrix, redacted documents/provider confirmations and professional review | HOLD — attorney/CPA/custody/provider |

## App-state requirements

When Orange Plan appears, the receipt must name whether the result is:

- saved Baseline,
- unsaved input,
- preview,
- applied strategy,
- separate Scenario,
- manually completed review,
- or read-only output.

The recording must not imply that a preview is the current plan or that an app checkmark proves an external process.

## External-primary demonstrations

For lender, healthcare, custody and trust demonstrations, the receipt identifies the source that owns the fact:

- signed agreement,
- current quote or plan document,
- manufacturer/provider procedure,
- legal document/provider acceptance,
- tax record,
- or real-world recovery/migration test.

Orange Plan records the plan effect and status. It does not replace that proof.

## Acceptance checklist

- [ ] The lesson gate is shown or stated.
- [ ] The concept was already taught before the demonstration.
- [ ] Inputs are synthetic or redacted.
- [ ] Version/date/source are visible.
- [ ] No secret or personal record appears.
- [ ] Saved/preview/Scenario state is named.
- [ ] Important numbers reconcile to their sources.
- [ ] The external evidence owner is named.
- [ ] Professional claims in scope have returned responses.
- [ ] The finish line is proven at the correct level.
- [ ] The accepted result is returned to Core.
- [ ] Austin approved the final recording plan.
