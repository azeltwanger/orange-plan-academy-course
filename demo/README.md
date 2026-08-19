# Academy demo fixture

This directory contains the machine-readable version of the fictional household used throughout Orange Plan Academy.

## Current file

- [`demo-v1-inputs.json`](demo-v1-inputs.json)

The JSON is **course-owned input data**, not an Orange Plan encrypted export and not a production import file.

Its purpose is to:

- prevent one number from drifting across scripts, lesson text, slides, and walkthroughs,
- give the app fixture issue a stable source contract,
- separate approved inputs from pending decisions,
- make invariant checks explicit,
- and keep app-calculated outputs null until Orange Plan produces them.

## Authority order

1. `DEMO-HOUSEHOLD.md` — human-readable planning explanation and decision context
2. `demo/demo-v1-inputs.json` — machine-readable mirror of the source inputs
3. approved canonical app fixture / saved demo account — actual app rows
4. checkpoint receipts — app-calculated outputs and reconciliation evidence

When the Markdown and JSON disagree, stop and reconcile them before another recording or fixture run.

## What this file is not

- Not client data
- Not Austin's household
- Not an Orange Plan restore backup
- Not a seed phrase, custody record, or secret map
- Not a second projection engine
- Not permission to hardcode the output shown in a lesson

## Change rule

A demo input change requires:

1. reason for the change,
2. affected lesson list,
3. Markdown and JSON reconciliation,
4. fixture/checkpoint rerun,
5. update to scripts, lesson text, slides, and walkthroughs using the changed value,
6. `demo-account update` classification in the app PR when app behavior or fixtures change.
