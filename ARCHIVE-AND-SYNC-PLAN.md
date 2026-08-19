# Orange Plan Academy — archive and synchronization plan

**Purpose:** make the repository unambiguous after Austin approves the repaired Core without destroying useful historical source material before it has been migrated.

## Current rule

Until a module is Austin-approved, the current production sources are only:

1. `CURRENT-COURSE.md`
2. the exact files listed there under `scripts/`
3. the matching files under `lesson-text/`
4. the current demo, app-contract, review, and production-control documents linked from `README.md`

Old master files, generated modules, Circle copies, aggregate scripts, prior walkthroughs, and prior production checklists remain migration inputs. They are not filming or publishing sources.

## Why cleanup waits for approval

Moving every old file now would make the repository look cleaner while the repaired content is still changing. It would also make it harder to recover a useful story, example, visual, dictated line, or live-client explanation during Austin's review.

The safer order is:

1. approve one module,
2. synchronize its approved content outward,
3. verify the published forms agree,
4. then archive the superseded forms for that module.

Cleanup follows approval module by module rather than one irreversible repository-wide purge.

---

# What remains current after the migration

## Editing sources

- `scripts/` — one approved spoken source per current lesson
- `lesson-text/` — one approved written reference per current lesson
- `CURRENT-COURSE.md` — exact course map and status
- `DEMO-HOUSEHOLD.md` and `demo/demo-v1-inputs.json` — canonical fictional inputs
- checkpoint receipts — app-owned demo outputs
- `COURSE-APP-CONTRACT.md` and `BUILD-YOUR-PLAN-CROSSWALK.md`
- `professional-review/` plus the review tracker
- visual, pilot, filming, and release controls linked from the README

## Generated or published outputs

These may exist for convenience but are never edited as the source:

- compiled all-scripts document,
- module bundles,
- course-platform/Circle lesson copy,
- PDF or printable lesson-text bundle,
- teleprompter exports,
- slide exports,
- video descriptions and captions.

Every generated output identifies the source commit and generation date.

---

# Module synchronization checklist

Run this after Austin marks a module approved.

## 1. Freeze the approved source

- [ ] Every script header says `AUSTIN APPROVED`.
- [ ] The matching lesson text reflects all factual and structural changes.
- [ ] Demo values match the current fixture and checkpoint receipt.
- [ ] Required professional response is applied and recorded.
- [ ] The repository audits pass.
- [ ] The module row in `FILMING-READINESS.md` is current.

## 2. Build the production assets

- [ ] Concept slides use the approved visual brief.
- [ ] Changing figures are sourced from the checkpoint or maintained reference.
- [ ] Exact walkthrough uses the verified Build Your Plan route and app commit.
- [ ] Walkthrough metadata contains step ID, route, save/apply behavior, app completion rule, human completion rule, demo version, and last verified commit.
- [ ] Course-platform lesson copy is generated from the current lesson text.
- [ ] Any worksheet or capstone field points to the same planning output.

## 3. Run a module parity check

Confirm that the script, lesson text, slides, walkthrough, app crosswalk, checkpoint, and published lesson agree on:

- the decision,
- the important number,
- the source input,
- the app location,
- and the finish line.

A difference in wording is fine. A difference in the actual work or result is not.

## 4. Record the release

Add a short module release record:

| Field | Value |
|---|---|
| Module |  |
| Approved script commit |  |
| Demo fixture version |  |
| Checkpoint receipt / app commit |  |
| Professional review version |  |
| Walkthrough app commit |  |
| Slide version |  |
| Course-platform publish date |  |
| Next review trigger |  |

## 5. Archive the superseded sources

Only after parity is verified:

- move prior scripts and lesson copies into a dated module archive,
- move retired walkthroughs into a dated app-version archive,
- move replaced slide decks into a dated visual archive,
- retire the old master/generated/Circle source for that module,
- and leave a small pointer stating which current file replaced it.

---

# Archive structure

Use a structure that preserves history without making it look current:

```text
/archive
  /course-pre-repair
    README.md
    ...old master and generated materials
  /modules
    /01-baseline
      /2026-08-pre-approval
    /02-cash-flow
      /2026-08-pre-approval
  /walkthroughs
    /<app-commit-or-version>
  /slides
    /<deck-version>
  /professional-review
    /superseded-packets
```

Each archive folder begins with a short `README.md`:

- what the files were,
- why they were retired,
- which current source replaced them,
- and whether anything remains useful as source material.

Do not put the archive directory in generation, publishing, or filming scripts.

---

# Files and layers to retire after the full Core is approved

The exact inventory is generated from the repository at migration time. The likely categories are:

- `MASTER-COURSE.md` as an editing source
- `MASTER-ADVANCED.md` until the Advanced pass is complete
- compiled `ALL-SCRIPTS` variants as editing sources
- generated module copies that do not identify an approved source commit
- Circle/course-platform copy containing the previous course
- walkthrough files tied to retired app routes or save behavior
- production checklists tied to the previous 13-step wizard
- old claim/provenance systems that describe generated prose as Austin-approved voice
- duplicate professional-review packet directories
- prior slide decks containing retired confidence, debt, tax, custody, estate, or contribution models

A compiled master may be regenerated later for convenience. It must carry a banner:

> Generated output. Do not edit. Source: individual approved lesson files at commit `<sha>`.

---

# Do not archive these as “old” merely because they are not spoken lessons

Keep current research and evidence that still performs a real job:

- client-call voice evidence,
- recurring-confusion registry,
- demo reconciliation,
- lesson ownership/runtime audit,
- slide correction map,
- app/course contract,
- professional-review records,
- official-source starters,
- and app-impact history.

These are quality-control evidence rather than competing course prose.

---

# Advanced Library migration

The Advanced Library remains separate from the Core cleanup.

For each Advanced lesson:

1. confirm its plan-visible gate,
2. check whether the current app supports the decision,
3. perform the voice/app/professional pass,
4. link it from the relevant Core area,
5. and archive the prior version only after the replacement is approved.

Do not let incomplete Advanced migration block Core publication when the learner's plan does not trigger the topic.

---

# Final repository acceptance test

The repository is clean when a new contributor can answer these questions from the README without asking Austin:

1. Which file do I edit for spoken Lesson 1.3?
2. Which file owns its student reference text?
3. Which fixture and checkpoint supply the demo numbers?
4. Which app commit was the walkthrough last verified against?
5. Which professional review cleared the claim?
6. Which generated outputs should never be edited?
7. Where did the replaced course go?
8. What product change triggers the next course review?

There should be one obvious answer to each question.