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

**A MUST rule names a lesson and the layers that must each carry the claim
independently.** Not "appears somewhere in the matching files" — that was the
first version of this gate, and it was too weak to describe as parity: a claim
could vanish from the master while surviving in the script and still pass. Every
listed layer is now resolved and checked on its own, and the report prints one
line per layer.

`layers` is drawn from `master` · `script` · `lesson-text` · `module`, or the
single token `file` for a rule that pins text in a specific document rather than
a lesson. Use `file:NAME.md` in the lesson column for those.

A MUST NOT rule keeps a `scope` substring matched against the file path. Empty
means everywhere, which is the right default for language that was retired.

**Matching is done on normalised text**: markdown emphasis is stripped and
whitespace is collapsed before the pattern is applied. Without that, a claim
written `between **10 and 20% LTV**` in the master and plainly in the script
looks like a parity failure when the two layers actually agree — which is exactly
what the first version of this registry reported.

⚠ **Historical files are never scanned** — `AUTHORITY-FLAGS.md`,
`COURSE-IMPROVEMENT-ANALYSIS.md`, `FILMING-CHECKLIST.md`, `HANDOFF.md` and this
file itself all quote retired positions on purpose, and that is the record.

---

## MUST — positions that have to be present

| id | lesson | pattern | layers | why |
|---|---|---|---|---|
| transfer-threshold | A7.4 | `0\.01 to 0\.02` | master,script,lesson-text,module | Austin's per-transfer rule of thumb. Deleted once and replaced with a principle of my own (F1). The revert is the reason this registry exists |
| ltv-range | A3.1 | `between 10 and 20% LTV` | master,script,lesson-text,module | 10–20% depending on risk tolerance. Narrowed to 10–15% once and reverted (F5). The band is his, and the arithmetic downstream is derived from it |
| beneficiary-qualified | 8.1 | `generally controls instead of the will` | master,script,lesson-text,module | The qualified form. The flat version is listed as MUST NOT below |
| beneficiary-qualified-cp | file:MODULE-CHECKPOINTS.md | `generally controls instead of the will` | file | The checkpoint carried the flat version after every other layer had been qualified |
| college-not-prepay | 2.4 | `(?i)not (a bill you prepay\|have to be solved entirely)` | master,script,lesson-text,module | College is a funding stack against a defined commitment, never a sticker price to pre-fund |
| known-cost-rule | 2.3 | `(?i)does not automatically need to be fully funded` | master,script,lesson-text,module | A future expense needs a plan; it does not outrank Bitcoin accumulation by default. This is the AUSTIN-AUTHORITY worked example |
| not-applicable-complete | file:MODULE-CHECKPOINTS.md | `(?i)not applicable` | file | "Not applicable is a completed line" is the rule that makes the checkpoint system work |

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

## Proving the gate

A gate that has never failed is not a gate. Five mutation classes are run against
this registry, and **all five must fail the build**:

| # | Mutation | What it proves |
|---|---|---|
| 1 | Reintroduce a retired phrasing in the master | MUST NOT works |
| 2 | Remove every instance of a MUST claim from the **master only**, introducing no forbidden phrase | A silent omission in one layer is caught |
| 3 | **Paraphrase** a MUST claim in **lesson-text only**, keeping the meaning | Rewording one layer is caught, not just deletion |
| 4 | Corrupt the **generated module only**, leaving every hand-edited layer correct | A stale generated layer is caught |
| 5 | Add a second module file containing the same lesson | A stale copy from a rename cannot hide behind "the first match" |

⚠ **Mutations 2–4 must remove or reword EVERY instance in the target layer.** A
claim usually appears more than once per layer — in the prose and again in the
homework — so changing one instance proves nothing. An early version of test 2
did exactly that, passed, and looked like evidence the gate worked.

⚠ **Mutation 5 is why `split-modules.py` prunes.** Renaming a module used to
leave the old slug in the tree forever, and one such orphan held a copy of A3.1
from before the LTV revert. The generated directory is a mirror of its source,
not an accumulation of every name it has ever had.

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
