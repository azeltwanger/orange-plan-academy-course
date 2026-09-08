# Orange Plan Academy — guided course

**Start with [the dictation order](DICTATION-ORDER.md).** The current course has 51 core teaching clips, 15 conditional Advanced clips, ten app working sessions and one device demonstration. Debt is Session 3; Allocation is Session 4.

The reviewed lessons are now in **`scripts/`**, not the former `course-v2/` workspace. [ALL-SCRIPTS.md](ALL-SCRIPTS.md) is the complete read-aloud copy. [MASTER-COURSE.md](MASTER-COURSE.md) includes production notes and checkpoints. [FILM-ORDER.md](FILM-ORDER.md) places the replaceable working-session chapters between the explanations that prepare them.

**Current status: ready for Austin's dictation and editorial approval.** This is not a claim of final recording, professional sign-off, or app-capture approval. The [remaining gates](FINALIZATION-STATUS.md) are explicit. This branch's content does not prove a merge to `main`.

[Advanced dictation](ADVANCED-DICTATION-ORDER.md) · [Member worksheets](toolkit/README.md) · [Visual/edit map](visuals/GUIDED-EDIT-MAP.md) · [Capture receipts](CAPTURE-RECEIPTS.md) · [App alignment](V1-COURSE-ALIGNMENT.md) · [Landing alignment](LANDING-PAGE-ALIGNMENT.md).

## Edit one source

Dictation edits go into the matching canonical file under `scripts/`. Read-aloud material goes only under `### Read aloud`; directions and qualifications for the editor stay in `### Production notes`. Never edit a generated teleprompter copy and assume the change reached the source.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
```

These commands synchronize and check the reading copies, masters, member playback order and production lists. They do not run the financial engine, access customer accounts or deploy anything.

## Preserved sources

Original permitted dictation remains in `source-material/`. The preceding scripts, masters, tools, supporting records and full grouped guided draft are preserved under `archive/pre-guided-promotion/`. Historical files are not recording instructions. [PROMOTION-RECORD.json](PROMOTION-RECORD.json) records their hashes and the exact amendments.

Raw client calls, private financial records, secrets and font files are not included in this course promotion.
