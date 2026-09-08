# A1.1 — Test an assumption without making the model tell you what you want

Status: TEACHING_REPAIR_NEEDED — the prior course-wide pass was rejected for voice and teaching clarity. This component still needs individual repair; it is not approved.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: APP_CAPTURE
Sources: FOUNDATION, BRAIN, APP, PRIMARY
Use when: a preset or holding-specific assumption materially changes a decision.

### Read aloud

Use an advanced assumption when it answers a specific question the normal starting choices do not express. Write that question first. Then change one thing so you can explain what caused the different result.

Separate expected growth from uncertainty around the path. Two models can have similar long-term growth and very different drawdowns or sequences. A deterministic projection applies one path. A simulation samples paths under its distribution, correlation, and other rules. Those design choices matter alongside the return assumption you choose.

A power-law model, a declining growth schedule, and a flat annual rate express different assumptions. A fitted historical relationship is not a guarantee that future adoption or price follows it. Compare the decision under a lower or slower path rather than relying on one model name as proof of conservatism.

Use the same starting assets, spending, taxes, and timing when comparing return models. Then identify exactly what changed. A higher return, lower volatility, lower inflation, and a later retirement date changed together make it difficult to understand the source of improvement.

Holding overrides deserve particular care. A spot Bitcoin fund can reasonably inherit a supported Bitcoin return rule while remaining a security for tax and custody. A Bitcoin operating company, leveraged fund, futures product, or covered-call structure needs its own treatment. An unsupported override should not make its leverage, operating costs, or distribution risk disappear.

For the Reed household, test one slower-growth alternative and inspect the first funding shortfall or difficult year. If the retirement plan only works under a highly favorable path, the useful response may be more saving, later timing, less spending, or different financing. Improving the assumption to make the number recover does not improve the household's resources.

Record the model, the reason for using it, the most important limitation, and a less favorable comparison. Use the current methodology documentation to understand what the engine actually tests. Avoid claiming a simulation proves risks it does not model, such as a lender's failure probability.

For the Reeds, an early year and a later year can reveal whether the chosen declining path says what they thought it said. Keep their spending, contributions and intended retirement timing fixed while comparing slower growth. Then inspect the first difficult funding year. The useful result is knowing which household decision depends on that assumption—not finding enough hidden adjustments to produce a preferred date.

Return to the main plan with a starting model you can explain, one useful comparison, and the limitation that matters most. If the comparison answers the question, stop. More settings do not automatically make the plan more reliable.

### Production notes

Use APP model/methodology as sole source for actual implementation. No unsupported claims of median calibration, correlation, fat tails, deterministic replay, or exact volatility schedule. Exact custom-period UI is capture-gated. Return to 1.4 and 6.7.

### Member checkpoint

- State the modeling question and one changed assumption.
- Compare the same plan under a less favorable path.
- Record the baseline, sensitivity, and limitations.

### Source-led visual and teaching notes — not spoken

Show the written question, one changed assumption, unchanged household choices, and the affected funding year. Actual rates, methodology and outputs require the approved build.

Editorial reason: Make advanced modeling a bounded sensitivity question with a clear return to the core plan.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Prepare the current saved assumptions and one reviewed lower-growth alternative. Show the early/later rates, compare the same household inputs, and inspect the funding year that explains the difference. Verify exact custom-period/override controls, unchanged baseline and result identity before recording. Do not manufacture volatility, correlation, replay or provider-failure claims. Return to 1.4 and 6.7.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
