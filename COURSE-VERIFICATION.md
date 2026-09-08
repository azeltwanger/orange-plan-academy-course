# Course verification

The current compiler checks the 77-component inventory, exact generated-copy parity, fictional arithmetic, preserved original dictation and historical-copy hashes, plus complete recovery-manifest coverage of the prior 255-file preservation chain. Existing mutation tests also reject a missing history entry or changed retained source copy. Member-deliverable tests remain part of the same verification.

`python tools/guided_course.py history` independently reads every removed file from the pinned Git commit and checks both its Git blob and SHA-256. It requires a full-history checkout and does not pretend the old files are still in the current tree.

Exact successful runs and tested final heads are recorded on PR #15 only after actual readback. A prepared workflow or this description is not itself a passing result. The one-shot writer/migration workflows are retired; normal verification has read-only repository permissions.

These checks verify structure, preservation, calculation examples and synchronization. They do not establish Austin's voice approval, a usable app demonstration, legal/tax/insurance advice, device recovery or learner success. Those gates remain in FINALIZATION-STATUS.md and CAPTURE-RECEIPTS.md.
