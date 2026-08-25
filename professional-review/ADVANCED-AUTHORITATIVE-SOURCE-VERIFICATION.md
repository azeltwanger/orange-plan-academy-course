# Orange Plan Academy — Advanced authoritative-source verification

**Completed:** 2026-08-25  
**App source checked:** `azeltwanger/orange-plan` at `34f42d94f4e236e6b82bad07e2b7bff0a578835e`  
**Scope:** the 18 current scripts under `scripts/advanced/current/`  
**Status:** primary-source verification complete; actual outside professional sign-off remains incomplete

## What this file does

This pass verifies claims that can be checked directly against current authoritative material and the current Orange Plan code. It also identifies what cannot be cleared from a public source.

This is **not** CPA, attorney, health-insurance, custody-practitioner, or lending sign-off. The named outside packet still has to be returned before a high-stakes implementation claim is finally approved or filmed.

---

# A1 · Modeling and assumptions

## Verified from the current app

Orange Plan's holding editor currently supports:

- Bitcoin assumptions,
- a fixed return,
- a declining return,
- custom return periods,
- and separate income/yield fields where supported.

Spot Bitcoin ETF holdings default to the Plan's Bitcoin assumptions rather than a broad stock return. The current code also preserves the distinction between value return and income yield.

## Course conclusion

- A1.1 may explain the model and comparable-path decision without promising that one assumption is correct.
- A1.2 correctly treats a holding override as a correction to a real classification or economic mismatch—not a way to improve a disappointing result.
- The exact labels, save behavior, and model version remain UI-receipt items.

## Remaining external/UI ownership

- Current deployed labels and save state
- The exact production model version and path controls shown to the learner
- Any claim that one custom assumption is economically reasonable for a specific investment

---

# A2 · Bitcoin-backed borrowing and leverage

## Verified from current tax authority

- Cash from a conventional bona fide loan is generally not included in income because the borrower has an obligation to repay it.
- Cancellation of that repayment obligation can create income, subject to applicable exceptions.
- Acquisition or disposition of secured property can create a separate sale/disposition result.
- Digital assets are property for federal tax purposes, so liquidation or another disposition can create gain or loss.
- The IRS has specifically noted that the substantive tax treatment of digital-asset loans can be unresolved, including an initial transfer of a digital asset for an obligation to return the same or identical asset.

## Applied correction

A2.1 and A2.3 now say explicitly:

- do not assume every product marketed as a Bitcoin loan is automatically a non-taxable pledge,
- inspect title/economic control, reuse, transaction flow, liquidation, cancellation, and repayment,
- and keep the app's loan-tax result provisional until a CPA or tax attorney reviews the signed agreement.

## Verified from the current app

The current Income/Withdrawal Strategy code supports a sell-versus-borrow comparison with concepts including:

- loan windows and LTV choices,
- collateralized-loan records,
- Bitcoin custody split,
- borrow capacity and runway,
- modeled drawdown risk,
- tax difference,
- loan interest,
- Bitcoin retained,
- loan repayment/timing effects,
- and a net result versus sell-only.

The app can compare modeled strategies. It does not interpret the signed agreement, determine legal ownership of collateral, or prove the federal tax character of the transfer.

## Remaining external ownership

The lending/legal reviewer still owns:

- collateral title and control,
- segregation and permitted reuse,
- borrower claim in insolvency,
- price source and valuation timing,
- notice and cure,
- partial versus full liquidation,
- top-up and release mechanics,
- renewal, fees, prepayment, death/incapacity, and dispute process.

The CPA/tax attorney still owns:

- loan-versus-disposition classification,
- interest and tracing,
- liquidation and lot treatment,
- cancellation/refinance,
- entity ownership,
- repayment and estate consequences.

No starting LTV, action line, or liquidation line is described as universally normal or safe.

Primary sources reviewed:

- IRS Topic 432 and IRS debt-cancellation guidance
- IRS final digital-asset reporting regulations, T.D. 10000 / IRB 2024-31
- IRS digital-asset property guidance

---

# A3 · Tax optimization and implementation

## Digital-asset identification

Current IRS rules distinguish assets held by a broker from units outside broker custody.

For units outside broker custody, specific identification is made no later than the date and time of the disposition in the taxpayer's books and records, with adequate records establishing which unit left the wallet/account. Without valid identification, earliest-acquired ordering applies within the applicable wallet/account scope.

For broker-custodied units, adequate identification generally must be supplied to the broker by the date and time of disposition. The broker's actual capability and confirmation still matter.

### Course conclusion

A3.1 correctly separates:

- quantity reconciliation,
- basis reconstruction,
- the app's planned lot,
- and the real executed/documented disposition.

Temporary transition relief is not taught as the permanent procedure.

## Roth conversions

Current IRS authority confirms:

- a taxable conversion generally enters gross income in the conversion year,
- no-conversion, smaller-conversion, and proposed-ceiling comparisons are legitimate planning choices,
- Roth distribution ordering uses regular contributions first, conversions/rollovers next on a FIFO basis, and earnings last,
- and each conversion/rollover can carry a separate five-year additional-tax period.

### Course conclusion

A3.2 correctly treats “room to the ceiling” as a first-pass calculation—not an instruction to fill the bracket automatically. Healthcare, state tax, Social Security, Medicare-related costs, cash used to pay tax, estimated payments, and future rates remain part of the comparison.

## Harvesting

A3.3 correctly requires:

- supported lots,
- comparison with no action and a smaller action,
- a post-transaction exposure plan,
- and current asset-specific repurchase/identification review.

The lesson does not promise that direct Bitcoin and a security such as a spot Bitcoin ETF have identical current repurchase treatment.

## Relocation

A3.4 correctly treats state relocation as a real domicile and life decision rather than changing only a tax-rate field. Exact residency, sourcing, departure/arrival, property, business, and state-law results remain with professionals in the affected states.

Primary sources reviewed:

- IRS IRB 2024-31 and IRB 2026-15 digital-asset identification rules
- IRS Publications 590-A and 590-B
- IRS current early-distribution and conversion guidance

---

# A4 · Early-retirement access and healthcare

## Account-access rules verified

Current federal guidance supports the distinctions used in A4.1:

- a qualified-plan distribution after separation in or after the year the employee reaches 55 can qualify for an exception to the 10% additional tax,
- that separation-from-service exception generally does not apply to an IRA,
- the distribution can remain ordinary taxable income even when the additional-tax exception applies,
- the actual employer plan controls available distribution forms,
- substantially equal periodic payments require a designed series and carry strict account/payment/ modification rules,
- Roth IRA distributions follow contribution/conversion/earnings ordering rules,
- and HSA tax-free treatment depends on qualified expenses and adequate records.

### Course conclusion

A4.1 correctly separates:

1. whether the account can distribute,
2. whether the distribution is taxable,
3. whether an additional tax applies,
4. and whether the plan/provider permits the intended withdrawal.

The Academy identifies the options. The CPA and plan administrator verify the actual source and amount.

## Healthcare rules verified

Current official guidance supports:

- Marketplace savings are based on expected annual household income and use a MAGI measure,
- the application should be updated when income changes,
- COBRA is temporary continuation coverage and commonly lasts 18 months after employment termination/reduction in hours,
- a qualified beneficiary can generally be charged up to 102% of the plan's total cost,
- COBRA is not treated as current-employment group coverage for the Medicare Part B Special Enrollment Period,
- and Medicare generally does not cover long-term/custodial care.

### Course conclusion

A4.2 and A4.3 correctly teach:

- current household quotes rather than national averages,
- full cost rather than premium alone,
- spendable cash versus MAGI,
- conversion/withdrawal/gain interactions,
- qualified HSA use with records,
- and a dated Medicare transition.

The illustrative premium amounts remain examples only. They never become current Colorado quotes.

## Remaining external ownership

- Marketplace-certified or licensed health-insurance reviewer: coverage language, COBRA/Marketplace plan comparison, networks, prescriptions, enrollment and consumer protections
- CPA: MAGI and tax-source interactions
- SHIP/qualified Medicare reviewer: Medicare enrollment and handoff
- Employer plan administrator: actual access and distribution options

Primary sources reviewed:

- IRS current early-distribution guidance and IRB 2026-06
- IRS Publications 590-B and 969
- HealthCare.gov income/MAGI guidance
- U.S. Department of Labor COBRA guides
- Medicare.gov Part B/COBRA and long-term-care guidance

---

# A5 · Advanced custody

## Passphrase mechanics verified

BIP-39 specifies that the mnemonic plus the exact optional passphrase derives the seed. When no passphrase is present, an empty string is used. Every passphrase produces a valid derived seed; a wrong value does not have to produce an obvious error.

### Course conclusion

A5.1 correctly teaches the two-sided risk:

- discovery of backup words may not expose the intended passphrase-protected wallet,
- and loss of the exact passphrase may permanently stop family recovery.

The course does not call a passphrase a mandatory custody level or use memory as the only backup.

## Account authentication verified

Current NIST guidance distinguishes phishing-resistant cryptographic authentication from manually entered OTP methods. OTP and out-of-band codes are not phishing-resistant because an impostor verifier can relay them.

### Course conclusion

Core and Advanced correctly prefer a FIDO security key or properly implemented passkey when supported, while retaining separate recovery methods and provider-specific verification.

## Multisig and migration boundary

The current lessons correctly define 2-of-3 as three keys where any two satisfy the threshold. They also treat key count, configuration/descriptor information, compatible software, physical/human/provider failure domains, and family capability as separate parts of recoverability.

A5.3 correctly requires a practice wallet, small live tranche, spend from the destination, alternate authorized recovery, staged migration, and family practice before the main balance is considered complete.

## Remaining external ownership

- Exact device and coordinator steps
- Passphrase entry/verification and compatibility
- Descriptor/configuration requirements
- PSBT/signing sequence
- Provider-independent collaborative recovery
- Key replacement/migration
- UTXO and privacy implications
- Evidence required before calling the setup family-ready

Primary sources reviewed:

- BIP-39 specification
- NIST SP 800-63B-4
- Current manufacturer/provider documentation remains required for the actual walkthrough

---

# A6 · Trusts and complex estate planning

## Federal tax concepts verified

Current federal authority supports the distinctions used in A6:

- property subject to a decedent's retained power to alter, amend, revoke, or terminate can be included in the gross estate,
- a revocable trust is not automatically an estate-tax shelter,
- trust income-tax ownership, completed-gift status, gross-estate inclusion, and basis adjustment are separate questions,
- and an irrevocable grantor trust asset outside the owner's gross estate does not automatically receive a section 1014 basis adjustment at death.

## Colorado digital-asset authority verified

Colorado enacted the Revised Uniform Fiduciary Access to Digital Assets Act. The course correctly keeps legal authority, provider access, and possession of a Bitcoin key as separate questions.

## Course conclusion

A6.1 correctly uses a problem gate rather than “Bitcoin holder = trust.”

A6.2 correctly teaches that:

- signing a trust does not move an asset,
- legal owner, provider record, tax file, custody threshold, and tested access must agree,
- retirement accounts are not casually retitled to a living trust,
- and a trust-beneficiary designation requires account-specific attorney/CPA review.

## Remaining external ownership

The Colorado estate attorney and CPA still own:

- document and trust selection,
- titling/assignment and funding,
- retained powers and fiduciary roles,
- gift completion and reporting,
- income-tax/grantor-trust result,
- gross-estate inclusion and basis,
- trustee investment/retention/diversification authority,
- minor/special-needs design,
- provider acceptance,
- and any directed-trust or trust-director structure.

The custody practitioner still owns the actual technical threshold and recovery process.

Primary sources reviewed:

- IRS Instructions for Form 706
- IRS Revenue Ruling 2023-2
- Colorado SB16-088, Revised Uniform Fiduciary Access to Digital Assets Act

---

# Overall verdict

The 18 Advanced concept lessons are suitable for Austin's voice-and-judgment review after the applied Bitcoin-loan tax qualification.

They are not yet ready for final approval or filming where a named agreement, quote, provider procedure, plan document, CPA, attorney, healthcare, or custody response remains outstanding.

## Required next evidence

1. Deployed app receipts for A1 and app-supported A2/A3/A4 comparisons
2. A specific synthetic/redacted lender agreement and lending/legal response
3. Core + Advanced CPA response
4. Current healthcare quote worksheet and healthcare/Medicare responses
5. Device/provider-specific custody review and practice evidence
6. Colorado attorney + CPA response for trust/ownership/tax claims
7. Austin's scoped corrections and one clean final read
