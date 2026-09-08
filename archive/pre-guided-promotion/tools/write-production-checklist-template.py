#!/usr/bin/env python3
"""Write the stable hand-edited head of PRODUCTION-CHECKLIST.md.

The generator appends status and lesson lists below the ONE-TIME SETUP marker.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTENT = '''# Production checklist

## Before filming any lesson

- [ ] Read the script status line: Austin dictation or pre-dictation filming draft.
- [ ] Complete Austin's spoken approval pass before treating a generated draft as final.
- [ ] Confirm the graphic cue in `SCREEN-SHOOT-LIST.md`.
- [ ] Remove current figures from spoken video when they belong in lesson text or the app.
- [ ] Confirm the teach lesson explains the decision and leaves exact clicks to the walkthrough.
- [ ] Read the line out loud once and replace any remaining copywriting reversal with the useful fact.

## V1 filming boundary

- [ ] Camera-facing concept lessons may be recorded after Austin's dictation pass.
- [ ] Graphics are added in editing; Austin does not need to present a slide deck.
- [ ] App walkthroughs wait for the owning V1 Preview slice and final labels to stabilize.
- [ ] Every walkthrough is verified against the exact approved Preview commit used on camera.
- [ ] PR #227 remains Preview-only until a separate cutover; do not use unfinished Preview behavior as a production promise.

## Professional gates

- [ ] Targeted CPA or EA review before publishing current-year tax examples and execution guidance.
- [ ] Exact device, firmware, provider, and recovery process verified before setup-specific custody footage.
- [ ] Licensed insurance professional reviews policy mechanics and contract-specific claims before publication.
- [ ] State-licensed estate attorney reviews state-specific authority, trust, and executor material before publication.

## Course flow checks

- [ ] Module 2 is Cash Flow + Reserve.
- [ ] Module 3 is Allocation + Next-Dollar.
- [ ] Module 4 is Debt, followed by a return to Cash Flow Routing.
- [ ] Foundation replaces rough onboarding data and reads the first preliminary Plan result.
- [ ] Module 5 owns historical transactions and cost basis.
- [ ] Module 6 teaches the simulation count and portfolio guardrails.
- [ ] Module 9 confirms the completed current baseline, tests one scenario, and saves Your Plan.

## V1 product checks

- [ ] Permanent destinations are Home, Plan, Cash Flow, and Protect.
- [ ] Plan uses Overview, Build & improve, and Scenarios.
- [ ] Normal customer results lead with simulations worked out of 1,000 and the through-age.
- [ ] The normal Orange Plan standard is 800 of 1,000; normal users do not choose it.
- [ ] Planned retirement date and earliest modeled retirement date are labeled separately.
- [ ] Result state is Preliminary, Current, Stale, or Unavailable.
- [ ] Material changes stay in Current versus Preview until saved.
- [ ] Guardrails show lower portfolio level, current retirement portfolio, upper portfolio level, and review status.
- [ ] Your Plan is the read-only printable and shareable plan document.
- [ ] Ask explains, guides, reviews, and deep-links; it does not silently change the saved plan.

## ☐ ONE-TIME SETUP

- [ ] Seed one consistent demo household and reuse it across every module.
- [ ] Use a clean browser profile with notifications off and no real customer data.
- [ ] Prepare a separate throwaway wallet and trivial funds for any custody demo.
- [ ] Keep 5 seconds of stillness before the first click and after the final click.
- [ ] Capture the final approved Preview commit SHA in the recording notes for every app session.
'''

(ROOT / "PRODUCTION-CHECKLIST.md").write_text(CONTENT, encoding="utf-8")
print("wrote PRODUCTION-CHECKLIST.md template")
