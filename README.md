# Orange Plan Academy

**Teaching repair is in progress. The earlier course-wide pass did not meet Austin's standard for natural, direct teaching.** Lesson 2.3 (Reserve) is the accepted reference. Full replacement drafts for 2.1, 2.2, 2.4 and 2.5, all six Debt lessons (3.1–3.6), and all seven Allocation lessons (4.1–4.7), plus matching W02–W04 narration, are ready for voice/judgment review. Other sessions and the conditional Advanced library still need individual repair—not just final approval of the old prose.

The newest replacement session is [Allocation and the next dollar](modules/04.md), following [Debt](modules/03.md) and [Cash Flow, Reserve and Life Events](modules/02.md). Use the [Core reading order](DICTATION-ORDER.md) for clean spoken copies. The [production checklist](PRODUCTION-CHECKLIST.md) distinguishes the accepted reference, replacement drafts and unrepaired components.

| Work | Start here |
|---|---|
| Read the teaching | [Core](DICTATION-ORDER.md) · [Conditional Advanced](ADVANCED-DICTATION-ORDER.md) |
| Review the latest replacement drafts | [Allocation](modules/04.md) · [Paired W04](scripts/working/W04_route-contributions-into-usable-accounts-and-intended-holdings.md) |
| Review Debt | [Debt](modules/03.md) · [Paired W03](scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md) |
| Review the preceding session | [Cash Flow, Reserve and Life Events](modules/02.md) · [Paired W02](scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md) |
| Read the whole working draft | [Spoken text](ALL-SCRIPTS.md) · [Core with notes](MASTER-COURSE.md) · [Advanced with notes](MASTER-ADVANCED.md) |
| Prepare demonstrations | [Learning and filming order](FILM-ORDER.md) |
| Use member materials | [Toolkit](toolkit/README.md) · [Named deliverables](toolkit/deliverables/README.md) |
| Check remaining work | [Current status](FINALIZATION-STATUS.md) · [Capture evidence](CAPTURE-RECEIPTS.md) |

The course structure remains Start Here plus ten sessions: 51 core clips including optional college, 15 conditional Advanced clips, ten app working sessions and one device demonstration. Debt precedes Allocation. There is no 150-minute cap and no word-count target that substitutes for teaching.

## One editing source

Edit `scripts/`. Narration is under `### Read aloud`; visual and production notes are not spoken. `teleprompter/`, `lesson-text/`, `modules/`, reading orders and masters are generated views of those same scripts. Availability on GitHub is for review, not a student release or filming approval.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p test_member_deliverables.py -v
python tools/guided_course.py history
```

These checks verify synchronization, arithmetic and preservation—not Austin's voice or learner comprehension. The last command needs full Git history. Normal CI remains read-only; temporary authoring automation is removed before integration into main.

## Original sources and old versions

Original dictation is unchanged in `source-material/`. Four historical dictation-containing scripts remain in its marked historical folder. Retired versions stay out of the working tree and are recoverable through [the pinned history](ARCHIVE-RECOVERY.md) and [hash manifest](production/repository-cleanup.json). Do not restore an old master over current scripts.

[Current handoff](HANDOFF.md) · [App alignment](V1-COURSE-ALIGNMENT.md) · [Landing-page alignment](LANDING-PAGE-ALIGNMENT.md) · [Primary references](PRIMARY-SOURCES.md).

Raw client transcripts, identifying financial records, secrets and credentials do not belong in this repository. The accepted Reserve text and its conditional liquidity judgment remain unchanged.
