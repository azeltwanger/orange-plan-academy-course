# Orange Plan Academy

**The written teaching and paired walkthrough pass is complete for review.** The course now follows a recognized problem through explanation and a worked example to a usable decision. The accepted Reserve lesson is unchanged. Owner voice approval, real app/device footage, targeted professional checks and learner evidence are still separate.

## Read the course

| Reading task | Open |
|---|---|
| Clean Core scripts, in order | [Core reading order](DICTATION-ORDER.md) |
| All spoken text in one document | [ALL-SCRIPTS](ALL-SCRIPTS.md) |
| Conditional advanced teaching | [Advanced reading order](ADVANCED-DICTATION-ORDER.md) |
| Whole-portfolio Allocation section | [Session 4](modules/04.md) |
| Paired application and filming sequence | [Learning and filming order](FILM-ORDER.md) |
| Existing member materials | [Toolkit](toolkit/README.md) · [Named deliverables](toolkit/deliverables/README.md) |
| Actual scope and unfinished evidence | [Current status](FINALIZATION-STATUS.md) · [Production checklist](PRODUCTION-CHECKLIST.md) |

There are 51 Core teaching clips (including optional college), 15 conditional Advanced lessons, ten app working sessions and one device demonstration. This is one course, not a set of competing outlines. The Advanced lessons are used when relevant; every member is not required to watch every variation.

The 40 new Core replacements and all 15 new Advanced replacements are integrated into the existing scripts. Nine previously repaired full Core explanations are retained; 3.3 receives a targeted repetition cut; 2.3 remains the accepted reference. Nine practical files are rewritten into one narrated chapter plan each. The already-detailed W02 and W03 are retained unchanged. All have been checked for their place in the connected learning sequence, not presented as new rewrites merely because a status changed.

## Edit one source

Edit `scripts/`. Only `### Read aloud` is spoken in a teaching clip. The teleprompter files, modules, lesson text and masters are generated reading views. Visual/production notes, references and member checkpoints are not narration. The uploaded YouTube video supplies teaching structure only, not its return assumptions or retirement formulas.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p test_member_deliverables.py -v
python tools/guided_course.py history
```

These commands verify structure, arithmetic, synchronization and preservation. They do not prove teaching quality, owner approval, a student outcome or release readiness. Historical recovery needs a full checkout.

## Sources, review and repository cleanup

[Source and revision record](delivery/teaching-revision.md) distinguishes original teaching, new illustrative reasoning and narrow primary-source checks. [Current handoff](HANDOFF.md) records what is finished in writing and what still needs real evidence.

Original dictation in `source-material/`, the fixed household, toolkit and capture records remain unchanged. Obsolete working versions remain retired, with [pinned recovery](ARCHIVE-RECOVERY.md) and the existing [hash manifest](production/repository-cleanup.json). No temporary authoring helper or branch-writing workflow should remain at merge.

Publication to main is for Austin to read. No app deployment, provider operation, financial transaction, pricing change or student launch is implied. Do not place real client records, credentials or signing secrets in this repository.
