# visuals/ — one graphic per teach lesson

39 prompts covering 33 of the 41 teach lessons. Each is written to be
pasted into Claude with `00-STYLE.md` in front of it.

**Filenames encode the lesson number**, matching the course exactly:
`4-1a_four-tiers.md` serves lesson 4.1, `A3-2_four-plays.md` serves A3.2.
An `a`/`b` suffix means one lesson has two graphics.

⚠ **Run `python3 tools/check-visuals.py` after any renumber.** This library
was excluded from the 2026-08-08 renumber and went stale by two structural
changes at once (its 04-x were allocation, its 05-x were debt — the numbering
from before Debt moved ahead of Allocation — and it still held 11-x files for
a module that no longer exists). Nothing broke, because no script cites a
visual filename, which is exactly why nobody noticed. That checker is the
tripwire.

## How to use

1. Open `00-STYLE.md`, copy the whole STYLE BLOCK.
2. Open the lesson's prompt file, copy it.
3. Paste style block first, then the prompt. Ask for a static 16:9 frame.
4. For the animated version, add the MOTION section from the style block
   and describe it as a build for an explainer template.

## What each prompt contains

- **What it has to make obvious** — the one idea. If the picture doesn't
  land this, it failed, however nice it looks.
- **The visual** — the actual composition.
- **Labels and data** — the exact numbers, and which figures are banned.
- **Motion** — the build order, matched to how the narration lands.

## Rules baked in

Colors are the app's real tokens, so course graphics and product screens
match. Orange is Bitcoin and nothing else. No law-set figure (bracket,
contribution limit, exemption, RMD age) is ever drawn into artwork — those
change, and the course points at them on screen instead. No vendor names.
No dollar figure that implies a promise.

## Not yet drawn (8 lessons)

Core: **0.2** how the AI works · **8.3** the heir letter and the switch.
Advanced: **A1.1** · **A4.1** · **A5.3** · **A7.2** · **A7.3** · **A7.4**.

Lesson **1.2** also gained a second graphic in the script (preview vs. the
Plan page) that has no prompt file yet.

## Priority if you're not doing all of them

These carry the most explanatory weight, in order:

1. `A3-1a_ltv-drift` — the one animation that makes leverage click
2. `1-3_thousand-paths` — what the confidence number counts
3. `4-1b_drawdown-math` — same crash, four different lives
4. `6-1_gap-and-bridge` — the shape of the whole retirement problem
5. `A5-1_rmd-spike` — why conversions matter, in two bars
6. `4-2_three-buckets` — the mental model the rest of the course reuses
