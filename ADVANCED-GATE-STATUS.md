# Orange Plan Academy — Advanced quality-gate status

**Status:** internally complete for Austin's voice-and-judgment review  
**Scope:** 18 current lessons in `scripts/advanced/current/` and matching student lessons  
**Final approval:** still blocked by the named UI, agreement, quote, device/provider, and outside-professional evidence

## Gate summary

| Gate | Status | Evidence / remaining work |
|---|---|---|
| Current architecture | **PASS** | Six conditional sections and 18 distinct lessons in `ADVANCED-CURRENT.md` |
| Script / student-text parity | **PASS** | 18 scripts and 18 matching lesson texts; `tools/advanced_course_audit.py` |
| Plan-visible gate | **PASS** | Every lesson opens with `Watch this only if…` and is mapped in `curriculum/advanced-learner-questions.json` |
| Real learner question | **PASS** | `review/advanced/LEARNER-QUESTION-MAP.md` |
| Worked example before demonstration | **PASS** | 18 of 18; `research/ADVANCED-WORKED-EXAMPLE-AUDIT.md` |
| One decision / finish line / return to Core | **PASS** | Enforced by the Advanced course audit |
| Internal judgment review | **PASS** | `review/advanced/JUDGMENT-REVIEW.md` |
| Voice / AI-slop guardrail | **PASS WITH AUSTIN AUTHORITY** | Automated lint blocks forbidden phrasing; Austin's spoken read remains final |
| Duplication / runtime ownership | **PASS WITH FOUR TIGHTEN FLAGS** | `research/ADVANCED-DUPLICATION-AND-RUNTIME-AUDIT.md` |
| App alignment and source ownership | **PASS WITH RECEIPT HOLDS** | `research/ADVANCED-APP-ALIGNMENT-AUDIT.md` |
| Number provenance | **PASS** | `ADVANCED-NUMBER-PROVENANCE-REGISTRY.md` and audit |
| Current authoritative-source verification | **PASS — NOT PROFESSIONAL SIGN-OFF** | `research/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md` |
| Professional claim mapping | **PASS** | `research/ADVANCED-PROFESSIONAL-CLAIM-MATRIX.md` |
| Send-ready professional packets | **PASS — NOT SENT** | Lending, CPA, healthcare, custody, and estate packets in `professional-review/` |
| Demonstration plan | **PASS — RECORDING HELD** | Nine demo groups in `research/ADVANCED-DEMO-AND-WALKTHROUGH-PLAN.md` |
| Demonstration receipt contract | **PASS** | `demo/ADVANCED-DEMO-RECEIPTS.md` and JSON schema |
| Visual briefs | **PASS — PRODUCTION HELD WHERE FACTS CHANGE** | `research/ADVANCED-VISUAL-BRIEFS.md` |
| Learner comprehension pilot | **PASS — NOT RUN** | `research/ADVANCED-PILOT-TEST-PLAN.md` |
| Stale-claim regression control | **PASS** | Advanced stale-claim audit and workflow |
| Austin voice-and-judgment review | **READY** | `review/advanced/DICTATION-ORDER.md` |
| `AUSTIN APPROVED` / filming | **HOLD BY LESSON** | Apply named evidence, reconcile script/text, then complete one clean final read |

## What “same quality as Core” means

Advanced now uses the same production discipline as Core, with one additional requirement: **the learner must have a plan-visible reason to enter the lesson.**

> **Gate → learner question → worked example → Austin judgment → honest trade-off or failure mode → one decision → app/professional implementation boundary → return to Core**

The screen or provider demonstration implements a decision that the concept lesson already taught. It is never the first useful example.

## Four lessons with an explicit compression gate

Austin prefers shorter teaching. These lessons are valid but should receive the hardest `TIGHTEN` review:

- A2.4 · Evaluate the lender and write the exit rules
- A3.4 · Evaluate state relocation
- A4.3 · Test account access, tax, and healthcare together
- A6.2 · Coordinate the trust, beneficiaries, and Bitcoin custody

Keep the learner question, worked example, decision, and stop signs. Move clause-by-clause, state-specific, quote-specific, or document-specific detail into lesson text, maintained reference, or the versioned demonstration.

## Evidence still outside the repository

Internal research cannot replace:

- the signed lender agreement and collateral structure,
- current tax records and CPA conclusions,
- the employer-plan document and Roth/HSA records,
- current Marketplace, COBRA, and Medicare facts for the household,
- the exact device, coordinator, and custody-provider process,
- Colorado attorney design and provider acceptance,
- or successful real-world recovery, migration, titling, and family tests.

The repository is now ready to receive those answers without restructuring or re-dictating the full Advanced Library.
