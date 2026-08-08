# Claim registry — the load-bearing positions, and the ones that were reverted

**Read by `tools/check-layer-parity.py`. Editing this file changes what that gate
enforces, so treat it as course policy, not configuration.**

Three review rounds in a row found the same failure shape: one layer teaching a
position another layer had already replaced. Every time, it was found by a human
reading carefully, and every time it was found *again* in a different lesson.
This file turns that from an audit into a gate.

Two kinds of entry:

- **MUST** — a position Austin has stated. If it is missing from a layer that
  should carry it, that layer has drifted.
- **MUST NOT** — a position that was tried and reverted. If it reappears
  anywhere, something has regressed. `AUTHORITY-FLAGS.md` records why each one
  was reverted; this file stops it coming back.

**`unless` is not an escape hatch.** It exists for the one legitimate case: a
lesson that deliberately *quotes* a wrong phrasing in order to correct it. Every
`unless` needs a reason, and adding one is a decision to be argued for, not a way
to quiet the checker.

`scope` is a substring matched against the file path. Empty means every layer:
masters, `scripts/`, `lesson-text/`, `modules/`, `MODULE-CHECKPOINTS.md`.

⚠ **Historical files are never scanned** — `AUTHORITY-FLAGS.md`,
`COURSE-IMPROVEMENT-ANALYSIS.md`, `FILMING-CHECKLIST.md`, `HANDOFF.md` and this
file itself all quote retired positions on purpose, and that is the record.

---

## MUST — positions that have to be present

| id | pattern | scope | why |
|---|---|---|---|
| transfer-threshold | `0\.01 to 0\.02` | `A7-4` | Austin's per-transfer rule of thumb. Deleted once and replaced with a principle of my own (F1). The revert is the reason this registry exists |
| ltv-range | `between 10 and 20% LTV` | `A3-1` | 10–20% depending on risk tolerance. Narrowed to 10–15% once and reverted (F5). The band is his, and the arithmetic downstream is derived from it |
| beneficiary-qualified | `generally controls instead of the will` | `08-1` | The qualified form. The flat version is listed as MUST NOT below |
| beneficiary-qualified-cp | `generally controls instead of the will` | `MODULE-CHECKPOINTS` | The checkpoint carried the flat version after every other layer had been qualified |
| college-not-prepay | `(?i)not (a bill you prepay\|have to be solved entirely)` | `02-4` | College is a funding stack against a defined commitment, never a sticker price to pre-fund |
| known-cost-rule | `(?i)does not automatically need to be fully funded` | `02-3` | A future expense needs a plan; it does not outrank Bitcoin accumulation by default. This is the AUSTIN-AUTHORITY worked example |
| not-applicable-complete | `(?i)not applicable` | `MODULE-CHECKPOINTS` | "Not applicable is a completed line" is the rule that makes the checkpoint system work |

## MUST NOT — positions that were reverted

| id | pattern | scope | unless | why |
|---|---|---|---|---|
| no-fixed-number | `(?i)not going to give you a fixed number` | | | The principle I substituted for Austin's 0.01–0.02 rule (F1). Reverted |
| fee-test-instead | `(?i)fee test rather than a fixed amount` | | | Same substitution, second phrasing (F1). Reverted |
| ltv-narrowed | `10 to 15% LTV\|10–15% LTV` | | | The narrowed band I derived arithmetic from (F5). Reverted |
| form-overrides-flat | `(?i)the form overrides the will` | | `blunt version\|dangerous` | The flat version is "right often enough to be dangerous." 8.1 quotes it in order to correct it, which is the one legitimate use |
| old-lane-table | `3 to 10 years.*Bitcoin\|3–10 year` | `02-3` | | The retired timeframe table that put Bitcoin out of every lane under ten years. Replaced by the current dictation |
| college-prefund-example | `\$100,000 college\|100k college` | | | The old pre-fund-the-sticker-price worked example. Contradicts the funding-stack position |
| stop-buying-btc | `(?i)stop buying bitcoin` | | `(?i)not to stop buying\|goal is not to stop\|does not automatically mean` | The exact conversion AUSTIN-AUTHORITY forbids: turning "a known cost needs a plan" into "stop accumulating until it is funded". The `unless` covers the two legitimate inverses the course actually uses — *"the goal is not to stop buying Bitcoin"* and *"does not automatically mean you stop buying Bitcoin until…"*. Both assert the opposite of the retired position |
| eight-trigger-gate | `(?i)eight[- ]trigger\|all eight triggers` | | | A8.1's competing estate gate. There is one gate, in the core walkthrough |
| rebuild-banner | `FLAGGED FOR REBUILD` | | | The 2.3 do-not-film banner. The lesson was rebuilt; the banner outlived it by nine days |
| module-ten | `Module 10\b` | | | Modules run 0–9. A tenth module has not existed since the renumber |

---

## Three-beat closure

Every **core teach lesson** closes with the same three beats, and the module
checkpoint is the sum of them:

> **YOUR DECISION** · **PUT IT IN ORANGE PLAN** · **YOU ARE DONE WHEN**

This is what makes a module produce one finished part of the plan rather than
nine watched videos. A lesson missing a beat cannot contribute its line to the
checkpoint.

**Exempt, deliberately:**

| Lesson | Why |
|---|---|
| 0.1 | Course orientation. There is no planning decision to record yet |
| 0.2 | How the AI works. Its one rule is a safety rule, and it is already a Module 0 checkpoint line |
| Every `A*` lesson | The Advanced Library closes with **Homework** instead. Advanced lessons are optional and are not summed into a module checkpoint |
| Walkthroughs and demos | They are capture sheets. The beats belong to the teach lesson |

**A beat present in some layers but not others is a PARITY FAILURE and fails the
gate.** A beat missing from all three layers is a coverage gap: reported, and
listed above if it is deliberate.
