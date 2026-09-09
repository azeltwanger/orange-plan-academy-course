# Orange Plan Academy

## [Start reading the course](DICTATION-ORDER.md)

Follow one main path, completing the matching walkthrough as you go. **For your situation** lessons appear beside the decisions they support. Read the condition: if your plan relies on that strategy, complete its lesson before using it. Otherwise continue. These are not basic and advanced versions of the program.

| What you need | Open |
|---|---|
| Main path and related lessons | [Course reading order](DICTATION-ORDER.md) |
| All spoken text, in learning order | [ALL-SCRIPTS](ALL-SCRIPTS.md) |
| Find a particular situation again | [For your situation index](ADVANCED-DICTATION-ORDER.md) |
| Teaching paired with application | [Learning and filming order](FILM-ORDER.md) |
| Existing member documents | [Toolkit](toolkit/README.md) · [Named deliverables](toolkit/deliverables/README.md) |
| Current review and recording status | [Status](FINALIZATION-STATUS.md) · [Production checklist](PRODUCTION-CHECKLIST.md) |

There are 50 shared-path teaching lessons, one college lesson when relevant, and 14 additional situation-specific lessons placed within the sections: 65 teaching lessons in all. Ten app working sessions and one device demonstration provide the paired application. The former A7.2 custody-responsibility lesson is folded into 7.1, 7.4 and W07 rather than repeated as another video.

The spoken-language edit removes repetitive conclusions, abstract task descriptions and production commentary while retaining the explanations, examples and practical qualifications. The accepted Reserve script is unchanged. This remains a draft for Austin’s integrated voice and judgment review, not an assertion that a learner has completed it or that recordings are ready.

## One editing source

Edit `scripts/`. Read-aloud sections are spoken; production notes and checkpoints are not. The indexes, teleprompter files, modules and masters are generated from the same scripts. Internal `core`/`advanced` paths and A-prefixed IDs remain for stable links, not as member-facing difficulty levels. Each additional lesson owns its condition, parent lesson and return instructions in its canonical metadata.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p test_member_deliverables.py -v
python tools/guided_course.py history
```

The checks verify structure, routes, arithmetic, synchronization and preservation—not writing quality or student results. History verification needs a full Git checkout.

Original dictation, the fixed household, toolkit, capture evidence and the previous repository cleanup remain unchanged. The retired A7.2 source is pinned in the generator’s merged-lesson record and verified alongside the previous historical recovery checks. No new duplicate archive or course master was added.

[Current handoff](HANDOFF.md) · [Source and editorial record](delivery/teaching-revision.md) · [Historical recovery](ARCHIVE-RECOVERY.md).

Publishing these files to main is for owner reading. It does not deploy Orange Plan, change pricing or access, publish the course to students, or perform financial, provider, wallet or legal actions.
