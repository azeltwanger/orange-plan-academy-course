# Slop candidates, adjudicated

**Read by `tools/slop-scan.py`. Every row is a candidate that was read and
accepted, with the reason it is not slop.**

The scanner reports SHAPES, and a good number of those shapes are legitimate:
Austin's attested speech, a factual three-item list, a "not X" clause that
carries real information, a production note on a capture sheet. Before this file
existed the scan printed a constant count of candidates that nobody re-read —
which meant a genuinely new slop line would have hidden inside the noise.

**A candidate is either fixed or adjudicated here. `slop-scan.py` exits non-zero
while any remain unadjudicated**, so "all gone" is checkable rather than a claim.

⚠ **An adjudication is keyed to the sentence, not the line number.** Edit
anything above it and the row still holds; reword the sentence itself and the
row lapses and the candidate comes back — which is exactly when it deserves
another read. Get the key from the scanner's output.

⚠ **This file is not a mute button.** A row with a weak reason is worse than a
slop line, because it launders one. If you cannot write the reason, fix the
sentence instead.

| key | where | why it is not slop |
|---|---|---|
| `A:9c2fbd6076a8` | scripts/01-2_set-your-growth-and-inflation-assumption.md · MASTER-COURSE.md | "keep in mind" is attested in Austin's own 2.2 dictation |
| `A:ce577ed57f90` | scripts/01-3_read-your-retirement-date-and-confidence.md · MASTER-COURSE.md | "I think" is one of his attested markers; this is personal framing, not an usher |
| `A:42cd376b9842` | scripts/01-3_read-your-retirement-date-and-confidence.md · MASTER-COURSE.md | "keep in mind" is attested in Austin's own 2.2 dictation |
| `A:b8a5101fce21` | scripts/02-2_size-your-cash-reserve-in-months-of-spen.md | AUSTIN DICTATION — his own recorded words |
| `A:addd3873330d` | scripts/02-2_size-your-cash-reserve-in-months-of-spen.md | AUSTIN DICTATION — his own recorded words |
| `B:82692c4d9e81` | scripts/advanced/A5-1_rmd-risk-and-roth-conversions.md | Arithmetic contrast carrying real growth information |
| `B:86e92f986370` | scripts/advanced/A6-1_health-insurance-between-retiring-and-me.md | A real product limitation, stated plainly |
| `B:c4f8977e81a6` | scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md | Legal mechanism of probate avoidance. Informational |
| `B:b9f03043f25f` | lesson-text/02-4_optional-college-is-a-funding-stack.md | Carries the actual reason. A "not X" that informs |
| `B:98e55746febb` | MASTER-ADVANCED.md | Legal mechanism of probate avoidance. Informational |
| `D:aef682a50eca` | scripts/01-3_read-your-retirement-date-and-confidence.md · MASTER-COURSE.md | Names the actual UI control. Informational, not a payoff |
| `D:47df11b82a52` | scripts/02-2_size-your-cash-reserve-in-months-of-spen.md | MODULE-CHECKPOINTS' own completion wording — an instruction to the student, not an aphorism |
| `D:5c866551ef23` | scripts/04-5_WALKTHROUGH_route-it.md | Production instruction to Austin on a capture sheet, not narration |
| `D:7173daace197` | scripts/06-3_guardrails-how-much-you-can-spend-each-y.md · MASTER-COURSE.md | States what the app does. Informational |
| `D:2faf19f33900` | scripts/06-3_guardrails-how-much-you-can-spend-each-y.md · MASTER-COURSE.md | Factual — the guardrail response really is that short. One payoff in this lesson |
| `D:24962f784414` | scripts/08-1_the-executor-the-four-legal-documents-an.md · scripts/advanced/A5-1_rmd-risk-and-roth-conversions.md | Attested in Austin's own dictation as a conversational close after a list |
| `D:6d68dc33e700` | scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md | One payoff line in this lesson, which is the guide's budget |
| `D:5db3dc4864f3` | scripts/09-1_keep-the-plan-current-monthly-and-annual.md · MASTER-COURSE.md | Normalises a zero-action month. Informational |
| `D:42c5397cd107` | scripts/advanced/A3-1_borrow-against-bitcoin-without-getting-l.md | One payoff line in this lesson, which is the guide's budget |
| `D:8839e5d0c607` | scripts/advanced/A7-4_wallet-operations-utxos-dust-and-address.md · MASTER-ADVANCED.md | One payoff line in this lesson, which is the guide's budget |
| `D:e8cdf2c9870f` | lesson-text/02-2_size-your-cash-reserve-in-months-of-spen.md · MASTER-COURSE.md | MODULE-CHECKPOINTS' own completion wording — an instruction to the student, not an aphorism |
| `D:79592ef80e81` | lesson-text/03-2_walkthrough-debt.md | Carries the teaching point of the walkthrough. One payoff in this file |
| `D:82191bc90f88` | lesson-text/07-2_set-up-a-hardware-wallet-and-test-recove.md | One payoff line in this lesson, which is the guide's budget |
| `D:dba30d4f56b0` | MASTER-COURSE.md | Informational — names which figure the student manages |
| `E:604837d0f331` | scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md | Factual list of what cost basis consists of, not a rhetorical triad |
| `E:92aa77ee4a64` | scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md | Factual list of the three trust roles, not a rhetorical triad |
| `E:0ebe9d495bc4` | MASTER-COURSE.md | Em-dash appositive in the DOC layer, not narration |
| `E:1ed535086c77` | MASTER-COURSE.md | Em-dash appositive in the DOC layer, not narration |
| `E:ebb4c333828d` | MASTER-COURSE.md | Em-dash appositive in the DOC layer, not narration |
| `E:f4f5f9cd9cd8` | MASTER-COURSE.md | Factual list of what cost basis consists of, not a rhetorical triad |
| `E:eb9f57b8d7ad` | MASTER-COURSE.md | Em-dash appositive in a module blurb, not narration |
| `E:422241920eb2` | MASTER-COURSE.md | Em-dash appositive in the DOC layer, not narration |
| `E:3e9b6c69500c` | MASTER-COURSE.md | Quotes the dangerous phrasing in order to correct it — the lesson's whole point |
| `E:7721e1f22f82` | MASTER-ADVANCED.md | Em-dash appositive inside arithmetic, not narration |
| `G:1049119bd766` | MASTER-COURSE.md | An instruction inside a worked example, not a textbook example opener |
