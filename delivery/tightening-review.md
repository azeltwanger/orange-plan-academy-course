# Tightening review — focused teaching and cumulative implementation

Austin approved the proposed repetition pass, then clarified that not every lesson needs an example. This revision preserves conversational introductions and handoffs while giving each explanation one primary home. The current deliverable is [all filming scripts in one file](../ALL-FILMING-SCRIPTS.md).

## Measured change

Comparison with commit `10e5529493ec6cd03c2ee51d73f2dbbd3b38049a`, the generic-label version immediately before this pass. Counts include spoken text only.

| Recording text | Before this pass | Current | Reduction |
|---|---:|---:|---:|
| Main teaching | 25,587 words | 18,209 words | 7,378 words (28.8%) |
| Conditional teaching | 6,112 words | 5,636 words | 476 words (7.8%) |
| Walkthrough narration | 11,248 words | 9,005 words | 2,243 words (19.9%) |
| All spoken text | 42,947 words | 32,850 words | 10,097 words (23.5%) |

The inventory remains 25 main and eight conditional teaching scripts, with 72 takes across ten app walkthroughs and one device demonstration. Word counts describe the manuscript, not recorded delivery or the time a member needs to implement the plan. Original and current long-term counts remain available in [the generated metrics](../COURSE-METRICS.md).

## Changes a member will notice

- The starting lesson teaches the baseline and account/holding distinction. Connection gaps, missing holdings and relevant history are handled by their W01 branches. Cash Flow uses the established result and checks it against ordinary spending instead of teaching the whole calculation again.
- Life Events follows one useful event rather than touring every possible transaction. The implementation handles special funding and completed-event records.
- The main financing and borrowing-rules lessons are shorter. Nonborrowers can proceed without creating a proposal. A3.2 owns offer structures; A3.1 owns Bitcoin collateral sizing, posted-versus-dedicated Bitcoin and contract responses. W03 chapter 6 owns ordinary repayment, exit and fallback; chapter 5 is Bitcoin-conditional.
- Contribution routing carries earlier cash decisions forward. It no longer detours into a separate lump-sum timing calculation or market indicators. Tax lessons have distinct jobs: fundamentals, multiyear comparison and transaction preparation.
- Walkthroughs use the reviewed inputs, interpret the actual result and finish the decision. They do not replay the full allocation, Traditional/Roth, tax-lot or annual-spending teaching examples. No hypothetical result is substituted for an actual app calculation.
- The household keeps one custody map. W07 prepares the family starting route; W08 completes one rehearsal with the necessary authority and access distinctions.
- Maintenance teaches monthly facts, annual choices and immediate changes. W09 owns the detailed review and reminders. The finale follows the retirement question, important funding years, response rules and next action in one saved plan.
- Examples are selective. Removed examples include the contribution timing detour, duplicate tax arithmetic, sample family letter and final cash-flow replay. Worked examples remain where the calculation explains a consequential decision.

## Preservation and review

Generic [Client] / [Partner] screen labels remain, with natural household references in speech. Teaching 4 remains focused on result interpretation; Ask guidance is in the walkthrough. Financial amounts, source assumptions and original/reduced/post-payoff timing retain their meaning. Source data, historical archives, the member toolkit and the capture register are preserved.

The isolated-wallet D07 script is unchanged. Existing tests for collateral boundaries, debt growth, insurance resources, account-security order and the annual spending cap remain. The test for the 25%/50% collateral comparison now checks A3.1, where the user-authorized relocation puts that explanation; all three interpretation assertions are preserved.

Independent continuity review checked the first-plan prerequisites, ordinary-debt versus Bitcoin-loan routing and the relocated collateral examples. Its small route corrections were applied: W01 skips missing-holdings work when it is complete; A3.2 returns to the borrowing-rules lesson before ordinary repayment capture; W03 chapter 5 explicitly describes the Bitcoin loan's exit.

Actual redesigned-app capture, model-specific device evidence, Austin's final recording delivery and independent learner completion remain separate from manuscript completion.

Independent middle-course review also checked current versus future cash, conversions versus withdrawals, the spending cap and Reserve refill. The final corrections give conversion users their own W05 packet route and let W06 users finish without a borrowing comparison when it does not apply.

## Completed validation

- All 38 unit tests passed on the final regenerated manuscript.
- Generator build/check: 44 components, 188 synchronized outputs and 194 arithmetic checks.
- The mutation suite passed; historical recovery verified 264 retired files and all 65 predecessor mappings.
- Exact teaching cues and all quoted walkthrough cues match their spoken text. The bundle contains all 33 teaching scripts and 72 takes with 177 teaching overlays.
- No fictional person names remain in active scripts. Source data, toolkit, historical material, capture evidence and the D07 script have no changes.
- Independent early and middle continuity reviews found no blocking omissions; their route clarifications are included. Whitespace checks passed.
