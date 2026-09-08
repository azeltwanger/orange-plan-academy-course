# A1.1 — Test an assumption without making the model tell you what you want

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: APP_CAPTURE
Sources: FOUNDATION, BRAIN, APP, PRIMARY
Use when: a preset or holding-specific assumption materially changes a decision.

### Read aloud

Use this lesson when the standard assumption choices do not express the question you are trying to test. Start by writing that question. “What happens if Bitcoin's growth slows after the first decade?” is specific enough to model. “How do I get the earliest retirement date?” invites the wrong experiment.

Separate expected growth from uncertainty around the path. Two models can have similar long-term growth and very different drawdowns or sequences. A deterministic projection applies one path. A simulation samples paths under its distribution, correlation, and other rules. Those design choices matter alongside the return assumption you choose.

A power-law model, a declining growth schedule, and a flat annual rate express different assumptions. A fitted historical relationship is not a guarantee that future adoption or price follows it. Compare the decision under a lower or slower path rather than relying on one model name as proof of conservatism.

Use the same starting assets, spending, taxes, and timing when comparing return models. Then identify exactly what changed. A higher return, lower volatility, lower inflation, and a later retirement date changed together make it difficult to understand the source of improvement.

Holding overrides deserve particular care. A spot Bitcoin fund can reasonably inherit a supported Bitcoin return rule while remaining a security for tax and custody. A Bitcoin operating company, leveraged fund, futures product, or covered-call structure needs its own treatment. An unsupported override should not make its leverage, operating costs, or distribution risk disappear.

For the Reed household, test one slower-growth alternative and inspect the first funding shortfall or difficult year. If the retirement plan only works under a highly favorable path, the useful response may be more saving, later timing, less spending, or different financing. Improving the assumption to make the number recover does not improve the household's resources.

Record the model, the reason for using it, the most important limitation, and a less favorable comparison. Use the current methodology documentation to understand what the engine actually tests. Avoid claiming a simulation proves risks it does not model, such as a lender's failure probability.

Return to the core plan with one defensible baseline and a saved sensitivity test. Advanced settings should make the decision more transparent, not create a collection of hidden adjustments you cannot explain next year.

### Production notes

Use APP model/methodology as sole source for actual implementation. No unsupported claims of median calibration, correlation, fat tails, deterministic replay, or exact volatility schedule. Exact custom-period UI is capture-gated. Return to 1.4 and 6.7.

### Member checkpoint

- State the modeling question and one changed assumption.
- Compare the same plan under a less favorable path.
- Record the baseline, sensitivity, and limitations.
