# Orange Plan Academy

**The written source-led course pass is complete. Start with [the Core reading order](DICTATION-ORDER.md).** Integrated wording still needs Austin's final voice/judgment review. Exact app footage, device tests and professional reviews remain separate from the written scripts. Nothing here implies a launch or merge.

| Work | Start here |
|---|---|
| Read and review the teaching | [Core](DICTATION-ORDER.md) · [Conditional Advanced](ADVANCED-DICTATION-ORDER.md) |
| Prepare the paired demonstrations | [Learning and filming order](FILM-ORDER.md) |
| Read the entire course | [Spoken text](ALL-SCRIPTS.md) · [Core with notes](MASTER-COURSE.md) · [Advanced with notes](MASTER-ADVANCED.md) |
| Use the member documents | [Toolkit](toolkit/README.md) · [Six named deliverables](toolkit/deliverables/README.md) |
| See what remains before publication | [Current status](FINALIZATION-STATUS.md) · [Capture evidence](CAPTURE-RECEIPTS.md) |

The current course is **51 core clips**, including optional college, **15 conditional Advanced clips**, **ten app working sessions** and **one device demonstration**. Keep the approved Start Here plus ten-session sequence. Debt is Session 3 and Allocation is Session 4. There is no arbitrary 150-minute cap.

## One editing source

Edit `scripts/` only. Narration lives under `### Read aloud`; visual, production and screen-dependent notes are not spoken. `teleprompter/`, `lesson-text/`, `modules/`, the reading orders and masters are generated copies of those same scripts, not competing versions.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p test_member_deliverables.py -v
python tools/guided_course.py history
```

The first four commands verify content structure, synchronization, arithmetic and member materials. The last verifies removed historical files from Git and requires full repository history. Normal CI is read-only; there is no retained one-shot migration or branch-writing workflow.

## Original material and old versions

Original supplied dictation remains unchanged in `source-material/`. Four verified historical dictation-containing scripts are retained in its clearly marked historical subfolder. Obsolete outlines, generated scripts, superseded migration files and old workflows have been removed from the current tree, not from Git history. [Recovery instructions](ARCHIVE-RECOVERY.md) and [the exact manifest](production/repository-cleanup.json) preserve access. Do not use historical material as a current recording order.

[What changed in the completed pass](delivery/source-led-completion.md) · [App alignment](V1-COURSE-ALIGNMENT.md) · [Landing-page corrections](LANDING-PAGE-ALIGNMENT.md) · [Sources](PRIMARY-SOURCES.md).

Raw client transcripts, identifying financial records, wallet secrets, credentials and font files stay out of the repository. The approved Reserve explanation and its conditional liquidity judgment remain intact.
