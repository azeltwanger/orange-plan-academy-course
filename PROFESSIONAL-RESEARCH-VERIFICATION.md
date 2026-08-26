# Professional research verification

**Completed:** 2026-08-25

## Scope

- Tax and healthcare: Module 5, A5.1–A5.3, A6.1–A6.2
- Custody: Module 7 and A7.1–A7.4
- Insurance and estate: 8.1–8.5 and A8.1
- Production policy, checkpoints, legal packet, source registry, and regression claims

## Result

- Primary-source audit completed.
- Unsafe or overstated claims removed from spoken, master, student, walkthrough, and generated module layers.
- Blanket professional-before-recording gates replaced with targeted operational or publication signoffs.
- Austin's original dictation source remains retained and unchanged.
- F20 is resolved by Austin's five-year funding ruling. F22 remains the only Austin dictation blocker.

## Generation

### PASS · Build module gates

```text
gate blocks written for 7 core modules
```

### PASS · Build core scripts

```text
protected: 40 files / 38 lesson numbers
wrote 0 scripts to scripts/
```

### PASS · Build Advanced scripts

```text
protected: 14 files / 14 lesson numbers
wrote 0 scripts to scripts/
```

### PASS · Split core modules

```text
wrote modules/00-module-0-start-here.md
wrote modules/01-module-1-foundation-replace-the-estimate-wit.md
wrote modules/02-module-2-cash-flow-reserve.md
wrote modules/03-module-3-debt-strategy.md
wrote modules/04-module-4-allocation-next-dollar.md
wrote modules/05-module-5-tax-strategy.md
wrote modules/06-module-6-retirement-income.md
wrote modules/07-module-7-custody.md
wrote modules/08-module-8-estate-inheritance.md
wrote modules/09-module-9-run-maintain-test-and-read-the-plan.md
```

### PASS · Split Advanced modules

```text
wrote modules/advanced/00-advanced-module-1-modeling-and-assumptions.md
wrote modules/advanced/01-advanced-module-2-cash-flow-optimization.md
wrote modules/advanced/02-advanced-module-3-debt-and-bitcoin-backed-lo.md
wrote modules/advanced/03-advanced-module-4-allocation-and-asset-locat.md
wrote modules/advanced/04-advanced-module-5-tax-strategies.md
wrote modules/advanced/05-advanced-module-6-retirement-strategies.md
wrote modules/advanced/06-advanced-module-7-advanced-custody.md
wrote modules/advanced/07-advanced-module-8-advanced-estate-planning.md
```

### PASS · Build one-file scripts

```text
ALL-SCRIPTS.md — 38 files, 49,237 words
```

### PASS · Build Circle structure

```text
CIRCLE-STRUCTURE.md regenerated — 10 modules, 14 advanced lessons routed
```

### PASS · Build core dictation order

```text
DICTATION-ORDER.md regenerated — 28 teach lessons, 217 min
```

### PASS · Build film order

```text
FILM-ORDER.md regenerated
```

### PASS · Build screen-shoot list

```text
SCREEN-SHOOT-LIST.md regenerated — 10 captures, ~162 min; 1 missing sheet(s): ['7.4 External demo: hardware wallet setup + exchange hardening']
```

### PASS · Build production checklist

```text
PRODUCTION-CHECKLIST.md regenerated — 2 filming blocker(s): 2.3 F20, 4.3 F22 · 0 publication blocker(s) · 0 not scheduled
```

### PASS · Update metrics

```text
{
  "core_n": 28,
  "core_min": 217,
  "core_h": 3.6,
  "core_w": 33690,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 83,
  "adv_w": 12812
}
stamped: README.md, MASTER-COURSE.md
note: ['README.md', 'MASTER-COURSE.md']
```

## Repository gates

### PASS · Cross-references

```text
DEAD LESSON REFERENCE  —  0

MODULE NUMBER OUT OF RANGE  —  0

WALKTHROUGH NAMING ANOTHER MODULE'S LESSON  —  0

0 problems. Valid lessons: 53. Modules: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### PASS · Layer parity

```text
NOTES (reported, do not fail)  —  0

FAILURES  —  0

53 lessons · 22 registry rules · 177 files scanned · 0 failures, 0 notes
```

### PASS · Slop scan

```text
25 candidates · 36 adjudicated in SLOP-ACCEPTED.md · 0 UNADJUDICATED
```

### PASS · Visual coverage

```text
visuals: 41 prompts covering 34 of 42 teach lessons

ORPHAN  —  0

H1 DRIFT  —  0

GAP (lesson with no visual)  —  8
  0.2  How to use Orange Plan AI
  8.3  The heir letter and the dead man's switch
  A1.1  How Orange Plan models Bitcoin: fat tails, correlations,
  A4.1  The price context check: naming the emotion before a big
  A5.3  State taxes and relocation: what the lever is actually w
  A7.2  What self-custody actually asks of you
  A7.3  Concentration: one institution, one vendor, one firmware
  A7.4  Wallet operations: UTXOs, dust, consolidation, and addre
```

### PASS · Metrics freshness

```text
{
  "core_n": 28,
  "core_min": 217,
  "core_h": 3.6,
  "core_w": 33690,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 83,
  "adv_w": 12812
}
STALE: none
```

### PASS · Layer-parity mutation harness

```text
baseline clean · running 7 mutation classes

1. retired phrasing returns in the master                     CAUGHT
2. silent omission from the MASTER only                       CAUGHT
3. paraphrase in LESSON-TEXT only                             CAUGHT
4. stale GENERATED module only                                CAUGHT
5. duplicate module file left by a rename                     CAUGHT
6. retired cost-lane table reinserted into the MASTER only    CAUGHT
7. flat beneficiary claim inserted into the VISUAL only       CAUGHT

all 7 mutations caught · tree restored clean
```
