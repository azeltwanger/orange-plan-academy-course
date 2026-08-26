# Austin dictation voice pass

**Completed:** 2026-08-26  
**Authority:** `source-material/2026-08-25-module-0-1-dictation.md` and `source-material/2026-08-26-f20-and-voice-pass.md`

## What the source says about Austin's voice

Austin explains the plain-language meaning first, tells the viewer why it affects the plan, gives a concrete example or source of truth, and then restates the practical decision. He marks judgment with phrases such as **I think**, **I would**, and **personally**. Useful repetition stays when it makes the action clearer. App clicks stay in walkthroughs.

## Scope

Every core and Advanced teach script was scanned. Actual Austin dictation, direct numbered teaching, app labels, and required factual qualifications were deliberately left alone. The pass changed the editor-shaped lines that were trying to sound finished rather than trying to explain the decision.

## Spoken scripts changed

- `scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md`
- `scripts/01-2_set-your-growth-and-inflation-assumption.md`
- `scripts/02-3_fund-a-known-future-cost-the-six-questio.md`
- `scripts/02-4_optional-college-is-a-funding-stack.md`
- `scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md`
- `scripts/05-2_taxable-tax-deferred-and-roth-bracket-wi.md`
- `scripts/07-1_choose-the-custody-setup-that-matches-you.md`
- `scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md`
- `scripts/07-3_single-points-of-failure-account-hardeni.md`
- `scripts/08-2_split-access-dual-control-and-redundancy.md`
- `scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md`
- `scripts/09-2_test-a-decision-and-read-the-finished-plan.md`
- `scripts/advanced/A3-1_borrow-against-bitcoin-without-getting-l.md`
- `scripts/advanced/A5-1_rmd-risk-and-roth-conversions.md`
- `scripts/advanced/A5-3_state-taxes-and-relocation.md`
- `scripts/advanced/A6-2_sell-borrow-or-hold-funding-a-year-of-sp.md`
- `scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md`
- `scripts/advanced/A7-2_what-self-custody-actually-asks-of-you.md`
- `scripts/advanced/A7-3_concentration-one-institution-one-vendor.md`
- `scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md`

## Representative changes

- **Benefit first:** the AI lesson now opens with how the tool helps, matching Austin's direction, instead of using a clever cannot-do reversal.
- **Explain instead of sloganize:** short lines such as *"That's the whole product"*, *"Three documents, three jobs"*, and repeated *"The goal is..."* constructions were replaced with the actual mechanism or action.
- **Mark judgment:** college, assumptions, custody complexity, and concentration decisions now use Austin's **I think / I would** framing where the statement is a planning judgment.
- **Keep technical precision:** tax, custody, insurance, and estate qualifications from the primary-source audit remain intact, but formal transitions were rewritten into plain explanations.
- **Resolve F20:** Bitcoin can remain part of the funding plan five years out. The committed amount becomes less dependent on Bitcoin as the date approaches. No fixed percentage was added.

## Deliberately unchanged

- 0.1 and the genuine 1.1 / 1.2 dictation, except for already-documented factual or lifecycle corrections.
- Walkthrough narration, which remains a DO / SEE / warning sheet rather than a teleprompter script.
- Lesson 4.3's planning order. F22 is still Austin's decision and is the only remaining authorship blocker.
- Current-law qualifications and professional publication gates.

## Final repository gates

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

53 lessons · 23 registry rules · 179 files scanned · 0 failures, 0 notes
```

### PASS · Voice/slop scan

```text
24 candidates · 36 adjudicated in SLOP-ACCEPTED.md · 0 UNADJUDICATED
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
  "core_min": 218,
  "core_h": 3.6,
  "core_w": 33823,
  "core_caps": 11,
  "core_walkthroughs": 10,
  "core_demos": 1,
  "core_capture_sessions": 10,
  "adv_n": 14,
  "adv_min": 83,
  "adv_w": 12879
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
