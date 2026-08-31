#!/usr/bin/env python3
"""Write the active V1 cross-layer claim registry."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTENT = r'''# Claim registry — Orange Plan V1 course contract

This registry is executable. `tools/check-layer-parity.py` verifies that the
load-bearing V1 teaching appears in every listed active layer and that retired
product language does not return.

## Current human-readable policies

- Permanent customer destinations are Home, Plan, Cash Flow, and Protect.
- Plan uses Overview, Build & improve, and Scenarios.
- Customer-facing Monte Carlo results lead with successful simulations out of
  1,000 and the through-age.
- The normal Orange Plan standard is 800 successful simulations out of 1,000.
- Planned retirement date and earliest modeled retirement date remain distinct.
- Every result is truthfully Preliminary, Current, Stale, or Unavailable.
- Material strategy changes remain in Current versus Preview until saved.
- Core spending guardrails show lower portfolio guardrail, current retirement
  portfolio, upper portfolio guardrail, and whether a review is needed.
- Exact provable activity is recorded with provenance; ambiguity becomes one
  focused Needs Attention question.
- An internal transfer preserves quantity and lot history and never becomes a
  sale plus purchase.
- Teach lessons explain decisions. Walkthroughs own final click paths and remain
  gated on the approved Preview commit used for recording.
- Spoken prose states the useful affirmative fact first. A negative remains only
  when the exclusion itself carries safety, legal, tax, custody, or model risk.

## MUST — V1 cross-layer claims

| id | lesson | pattern | layers | why |
|---|---|---|---|---|
| V1-COUNT-1 | `1.3` | `800 of 1,000` | master, script, lesson-text, module, visual | The normal standard is fixed and visible. |
| V1-FRESH-1 | `1.3` | `Preliminary.{0,160}Current.{0,160}Stale.{0,160}Unavailable` | master, script, lesson-text, module, visual | Every displayed result has a truthful state. |
| V1-DATES-1 | `1.3` | `planned retirement date.{0,180}earliest modeled retirement date` | master, script, lesson-text, module | The two dates have different jobs. |
| V1-DIRECT-1 | `3.1` | `The four paths describe where you are today` | master, script, lesson-text, module | The allocation framework is stated directly. |
| V1-COUNT-6 | `6.3` | `800 of 1,000` | master, script, lesson-text, module | Retirement Income uses the same normal standard. |
| V1-GUARD-6 | `6.3` | `lower guardrail.{0,240}current retirement.{0,240}upper guardrail` | master, script, lesson-text, module, visual | Core guardrails use portfolio levels. |
| V1-HOME-9 | `9.1` | `Home answers` | master, script, lesson-text, module | Home owns the current financial truth review. |
| V1-CASHFLOW-9 | `9.1` | `Cash Flow answers` | master, script, lesson-text, module | Cash Flow owns the monthly system review. |
| V1-PLAN-9 | `9.1` | `Plan answers` | master, script, lesson-text, module | Plan owns the future-plan review. |
| V1-PROTECT-9 | `9.1` | `Protect answers` | master, script, lesson-text, module | Protect owns family execution. |
| V1-NAV-VISUAL-9 | `9.1` | `Home.{0,500}Cash Flow.{0,500}Plan.{0,500}Protect` | visual | The annual-lap graphic follows the four destinations. |
| V1-CVP-9 | `9.2` | `Current versus Preview` | master, script, lesson-text, module, visual | Proposed decisions remain separate until saved. |
| V1-YOURPLAN-9 | `9.2` | `Your Plan` | master, script, lesson-text, module, visual | The final artifact uses the V1 name and role. |
| V1-ASK-0 | `0.2` | `Ask is available from the header` | master, script, lesson-text, module | Ask is a global contextual utility. |
| V1-ASK-VISUAL | `0.2` | `Ask` | visual | The edit graphic matches the product model. |
| V1-ACTIVITY-1 | `1.4` | `Needs Attention` | master, script, module | Ambiguity becomes one focused question. |
| V1-TRANSFER-1 | `1.4` | `internal transfer preserves total quantity` | master, script, module | Transfers preserve accounting continuity. |

## MUST NOT — retired V1 language

| id | lesson | pattern | layers | unless | why |
|---|---|---|---|---|---|
| V1-NO-TARGET | `*` | `(?:choose\|set\|select\|saved\|saving\|point out).{0,50}confidence target\|confidence target choices\|target confidence` |  |  | Normal users do not choose the standard. |
| V1-NO-FIRST-WAIT | `*` | `first (?:saved )?full.{0,50}confidence\|first full 1,000-path confidence\|first full confidence run` |  |  | Foundation may show a preliminary simulation result. |
| V1-NO-OLD-NAV | `*` | `Build Your Plan\|Strategy →\|Account menu → Report\|Open Report\|Report → Print` |  |  | Retired navigation and artifact paths stay out of active layers. |
| V1-NO-APPLY | `*` | `Apply to plan\|apply to plan\|Run confidence\|run confidence` |  |  | V1 uses Preview, Save to plan, and recalculate. |
| V1-NO-PLAN-GUIDE | `*` | `Plan Guide\|orange AI Review button` |  |  | Ask replaced the old product framing. |
| V1-NO-RING | `*` | `confidence ring\|confidence number` |  |  | Customer teaching leads with a simulation count. |
| V1-NO-CORE-6095 | `6.3` | `60.{0,20}80.{0,20}95` | master, script, lesson-text, module, visual |  | The core guardrail view uses portfolio levels. |
| V1-NO-RECOMMENDATION-SETUP | `3.1` | `The four paths on the screen are not recommendations` | master, script, lesson-text, module |  | The lesson says the affirmative fact directly. |

## Verification

Run:

```text
python3 tools/check-layer-parity.py -v
python3 tools/check-v1-course-alignment.py
python3 tools/direct-voice-audit.py
```
'''

(ROOT / "CLAIM-REGISTRY.md").write_text(CONTENT, encoding="utf-8")
print("wrote CLAIM-REGISTRY.md")
