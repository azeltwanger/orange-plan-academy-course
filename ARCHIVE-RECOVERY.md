# Historical course recovery

The obsolete course versions have been removed from the current file tree. They remain in Git at commit `a7be495e670078cd44ea4e0792538b0eaa32dd95`. No branch, commit history or original supplied dictation was deleted.

The four verified historical scripts containing Austin dictation also remain as byte-identical copies in `source-material/historical-dictation/`. Their older app/factual edits are historical, not current recording instructions.

`production/repository-cleanup.json` identifies every removed file by path, Git blob and SHA-256. `PROMOTION-RECORD.json` remains unchanged and records the preceding preservation chain.

To read an old file without changing the current checkout:

```sh
git show a7be495e670078cd44ea4e0792538b0eaa32dd95:archive/pre-guided-promotion/MASTER-COURSE.md
```

To verify all removed bytes against the pinned history after fetching full history:

```sh
python tools/guided_course.py history
```

A shallow export/ZIP can run the normal course checks, but cannot independently verify Git recovery. Use a full-history checkout for that command. The current course starts at DICTATION-ORDER.md; do not restore an old master over the active scripts.

Removed obsolete files: **264**. Current canonical lessons, read-aloud copies, member documents, fictional data and live approval/capture requirements are retained. The one-shot synchronization workflow and migration machinery have been retired; normal verification is read-only.
