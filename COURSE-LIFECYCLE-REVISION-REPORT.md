# Course plan-lifecycle revision report

## Locked implementation

- Ten-module order retained.
- Lessons 1.4 and 1.5 retained as two published lessons from one recording.
- Onboarding is a rough estimate, not the baseline.
- Data entry is distributed to the module that owns it.
- Full 1,000-run confidence check moved to Module 9.
- Austin's 1.1 and 1.2 dictation incorporated.

## Generation and checks

### PASS · build module gates

```text
gate blocks written for 7 core modules
```

### PASS · build scripts

```text
protected: 40 files / 38 lesson numbers
wrote 0 scripts to scripts/
```

### PASS · build one-file

```text
ALL-SCRIPTS.md — 38 files, 52,924 words
```

### PASS · split modules

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
  removed stale modules/01-module-1-foundation-baseline-assumptions-and.md
  removed stale modules/09-module-9-maintain-test-and-read-the-plan.md
```

### PASS · build Circle structure

```text
CIRCLE-STRUCTURE.md regenerated — 10 modules, 14 advanced lessons routed
```

### PASS · build dictation order

```text
!! PARITY: the "which modules are US-shaped" breakdown is in scripts/00-1_how-to-use-this-course.md (0.1) but NOT in MASTER-COURSE.md
DICTATION-ORDER.md regenerated — 28 teach lessons, 242 min
```

### PASS · build film order

```text
FILM-ORDER.md regenerated
```

### PASS · build shoot list

```text
SCREEN-SHOOT-LIST.md regenerated — 10 captures, ~161 min
```

### PASS · build production checklist

```text
PRODUCTION-CHECKLIST.md regenerated — 3 filming blocker(s): 2.3 F20, 4.3 F22, Module 2 F23 · 1 publication blocker(s) · 1 not scheduled
```

### PASS · update metrics

```text
{
  "core_n": 28,
  "core_min": 242,
  "core_h": 4.0,
  "core_w": 37485,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 106,
  "adv_w": 16398
}
stamped: README.md, MASTER-COURSE.md
note: ['README.md', 'MASTER-COURSE.md']
```

### PASS · check crossrefs

```text
DEAD LESSON REFERENCE  —  0

MODULE NUMBER OUT OF RANGE  —  0

WALKTHROUGH NAMING ANOTHER MODULE'S LESSON  —  0

0 problems. Valid lessons: 53. Modules: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### PASS · check metrics

```text
{
  "core_n": 28,
  "core_min": 242,
  "core_h": 4.0,
  "core_w": 37485,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 106,
  "adv_w": 16398
}
STALE: none
```

### PASS · check visuals

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

### FAIL · check layer parity

```text
NOTES (reported, do not fail)  —  0

FAILURES  —  6
  [BEATS] 1.1 What to gather before you build the plan
          "YOUR DECISION" in ['master', 'script'] but NOT in ['lesson-text']
  [BEATS] 1.1 What to gather before you build the plan
          "PUT IT IN ORANGE PLAN" in ['master', 'script'] but NOT in ['lesson-text']
  [BEATS] 1.2 The three layers of a plan, and setting 
          "YOUR DECISION" in ['master', 'script'] but NOT in ['lesson-text']
  [BEATS] 1.2 The three layers of a plan, and setting 
          "PUT IT IN ORANGE PLAN" in ['master', 'script'] but NOT in ['lesson-text']
  [BEATS] 1.3 Read your starting retirement date and t
          "YOUR DECISION" in ['master', 'script'] but NOT in ['lesson-text']
  [BEATS] 1.3 Read your starting retirement date and t
          "PUT IT IN ORANGE PLAN" in ['master', 'script'] but NOT in ['lesson-text']

53 lessons · 17 registry rules · 170 files scanned · 6 failures, 0 notes
```

### PASS · slop scan

```text
40 candidates · 36 adjudicated in SLOP-ACCEPTED.md · 0 UNADJUDICATED
```

## Stale onboarding-language audit

No blocked stale phrases remain in the live core layers.

## Follow-up

The revision was generated, but these repository gates need a final editorial pass: check layer parity.

## Final parity and generator pass

### PASS · split modules

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

### PASS · build dictation order

```text
DICTATION-ORDER.md regenerated — 28 teach lessons, 242 min
```

### PASS · check layer parity

```text
NOTES (reported, do not fail)  —  0

FAILURES  —  0

53 lessons · 17 registry rules · 171 files scanned · 0 failures, 0 notes
```

### PASS · slop scan

```text
40 candidates · 36 adjudicated in SLOP-ACCEPTED.md · 0 UNADJUDICATED
```

### PASS · check crossrefs

```text
DEAD LESSON REFERENCE  —  0

MODULE NUMBER OUT OF RANGE  —  0

WALKTHROUGH NAMING ANOTHER MODULE'S LESSON  —  0

0 problems. Valid lessons: 53. Modules: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### PASS · check metrics

```text
{
  "core_n": 28,
  "core_min": 242,
  "core_h": 4.0,
  "core_w": 37485,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 106,
  "adv_w": 16398
}
STALE: none
```
