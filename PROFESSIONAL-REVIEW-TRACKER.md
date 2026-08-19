# Orange Plan Academy — professional review tracker

**Purpose:** collect narrow, actionable reviews before Austin performs the final voice pass. Reviewers should not rewrite the course or approve the entire financial plan. They should identify inaccurate, overbroad, stale, or professionally unsafe claims in their assigned packet.

The canonical packets live in [`professional-review/`](professional-review/README.md).

## Response codes

Ask each reviewer to mark every flagged claim with one code:

- `OK` — accurate and appropriately qualified for education.
- `QUALIFY` — directionally accurate but needs a stated limitation.
- `CHANGE` — inaccurate or misleading; provide the corrected concept.
- `CURRENT FACT` — accurate now but belongs in maintained lesson text/reference rather than evergreen spoken video.
- `PROFESSIONAL ONLY` — the concept may be named in Core, but implementation belongs with the licensed or specialized professional.
- `REMOVE` — unnecessary or unsafe for the course.

The reviewer may propose exact wording, but Austin retains the spoken voice. The course team applies the factual correction before Austin's final read.

## Reviewer instructions

Send only the assigned packet, not the entire repository.

Ask the reviewer to focus on:

1. factual accuracy,
2. missing qualifications,
3. statements likely to age quickly,
4. implementation steps that should not be taught as universal,
5. the difference between app status and real-world proof,
6. and anything a learner could reasonably misapply.

Ask them not to spend time polishing tone, transitions, lesson order, or app navigation.

---

# Tax and retirement-account review

**Packet:** [`professional-review/CPA.md`](professional-review/CPA.md)  
**Affected lessons:** 4.4, 5.1, 5.2, tax-sensitive portions of 6.1 and 6.2

| Field | Status |
|---|---|
| Reviewer |  |
| Credentials / firm |  |
| State / specialty |  |
| Sent |  |
| Response due |  |
| Returned |  |
| Overall status | NOT SENT |

## Required review outcomes

- [ ] Cost-basis and transfer language is accurate and sufficiently qualified.
- [ ] Lot-identification language distinguishes app comparison from real execution.
- [ ] Taxable, traditional, Roth, HSA, and account-access statements are current.
- [ ] RMD language avoids one universal age while remaining understandable.
- [ ] Roth-conversion and gain/loss-window language stays educational rather than prescriptive.
- [ ] Withdrawal-phase and tax-ceiling language properly assigns execution to the taxpayer and professional.
- [ ] Any changing thresholds, limits, or procedures are moved to maintained reference material.

## Returned changes

| Packet item / lesson | Code | Reviewer correction or qualification | Applied commit | Austin re-review needed? |
|---|---|---|---|---|
|  |  |  |  |  |

---

# Bitcoin custody and account-security review

**Packet:** [`professional-review/CUSTODY.md`](professional-review/CUSTODY.md)  
**Affected lessons:** 7.1, 7.2, 7.3, technical portions of 8.2 and 8.3

| Field | Status |
|---|---|
| Reviewer |  |
| Organization / specialty |  |
| Devices / models within scope |  |
| Sent |  |
| Response due |  |
| Returned |  |
| Overall status | NOT SENT |

## Required review outcomes

- [ ] Hardware-wallet setup remains device-neutral and points to current manufacturer instructions.
- [ ] Backup and recovery testing does not tell a learner to wipe the only meaningful device without a safe fallback.
- [ ] Passphrase risks and compatibility limitations are accurate.
- [ ] Single-signature, collaborative custody, and multisig trade-offs are not presented as a universal ranking.
- [ ] A 2-of-3 design is described correctly as three keys where any two sign.
- [ ] Descriptor/configuration language is accurate without treating it like a private key.
- [ ] Email, passkey/security-key, recovery, carrier, and exchange-hardening claims are current.
- [ ] Orange Plan and every family document remain no-secrets surfaces.

## Returned changes

| Packet item / lesson | Code | Reviewer correction or qualification | Applied commit | Austin re-review needed? |
|---|---|---|---|---|
|  |  |  |  |  |

---

# Estate and incapacity review

**Packet:** [`professional-review/ESTATE-ATTORNEY.md`](professional-review/ESTATE-ATTORNEY.md)  
**Affected lessons:** 8.1, legal/role portions of 8.2 and 8.3

| Field | Status |
|---|---|
| Reviewer |  |
| State(s) licensed |  |
| Digital-asset experience |  |
| Sent |  |
| Response due |  |
| Returned |  |
| Overall status | NOT SENT |

## Required review outcomes

- [ ] Executor/personal representative, agent under power of attorney, healthcare decision-maker, and trustee roles are separated correctly.
- [ ] The course does not imply a named executor has immediate authority merely because the will names them.
- [ ] Power-of-attorney language correctly limits the role to lifetime authority under the document and law.
- [ ] Provider beneficiary/designation language avoids the slogan that one form always overrides a will.
- [ ] Spousal rights, plan terms, state law, validity, and provider procedure are appropriately qualified.
- [ ] Key possession is not confused with legal authority.
- [ ] The heir letter and executor packet are clearly nonbinding process guides containing no secrets.
- [ ] Dead-man-switch language does not present notification as legal authority or an estate plan.

## Returned changes

| Packet item / lesson | Code | Reviewer correction or qualification | Applied commit | Austin re-review needed? |
|---|---|---|---|---|
|  |  |  |  |  |

---

# Insurance review

**Packet:** [`professional-review/INSURANCE.md`](professional-review/INSURANCE.md)  
**Affected lesson:** 8.4

| Field | Status |
|---|---|
| Reviewer |  |
| License / states |  |
| Product specialty |  |
| Sent |  |
| Response due |  |
| Returned |  |
| Overall status | NOT SENT |

## Required review outcomes

- [ ] Life coverage begins with a survivor cash-flow and capital gap rather than a universal income multiple.
- [ ] The demo's $62,000 annual survivor gap is labelled as a first-pass input, not a coverage recommendation.
- [ ] Term and permanent coverage descriptions are balanced and contract-dependent.
- [ ] Disability language addresses cap, waiting period, benefit period, definition, excluded income, and possible tax treatment.
- [ ] Umbrella language acknowledges underlying limits, exclusions, and carrier terms.
- [ ] Long-term-care language frames self-insurance, family support, insurance, public benefits, and review timing without a product recommendation.
- [ ] Existing coverage is not cancelled before replacement and professional confirmation.
- [ ] Beneficiary and ownership records are assigned to the carrier rather than Orange Plan.

## Returned changes

| Packet item / lesson | Code | Reviewer correction or qualification | Applied commit | Austin re-review needed? |
|---|---|---|---|---|
|  |  |  |  |  |

---

# Final clearance rule

A professional response clears only the claims inside that reviewer's scope.

After the returned changes are applied:

1. Reconcile the matching lesson text.
2. Update the packet or mark the reviewed version and date.
3. Run the repository audits.
4. Mark the affected professional gate complete in `FILMING-READINESS.md`.
5. Put the corrected script into Austin's one-pass review queue.

Austin should not have to approve a voice version and then repeat the entire lesson because a professional correction arrived later.