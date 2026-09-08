#!/usr/bin/env python3
"""One-use course repair metadata/synchronization preparation; no network calls."""
from pathlib import Path
import subprocess,re,hashlib
BASE='50d88671f2a6dd4e365b3b8a828e3ce03c7f5f3b'
ROOT=Path(__file__).resolve().parents[1]
REWRITTEN={'2.1','2.2','2.4','2.5','W02'}
def old(path):
    return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT).decode()
def put(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n')
def substitute(text,before,after):
    if text.count(before)!=1:raise ValueError('Unexpected source for bounded edit')
    return text.replace(before,after,1)
# Only status lines change in scripts outside the five actual replacement files.
for p in sorted((ROOT/'scripts').rglob('*.md')):
    rel=str(p.relative_to(ROOT));t=p.read_text();lid=re.match(r'# ([^ ]+) — ',t).group(1)
    original=old(rel)
    if lid=='2.3':
        if t!=original:raise ValueError('Accepted Reserve changed')
    elif lid in REWRITTEN:
        expected='WALKTHROUGH_REWRITE_REVIEW' if lid=='W02' else 'TEACHING_REWRITE_REVIEW'
        if 'Status: '+expected not in t:raise ValueError('Missing honest replacement status')
    else:
        if t!=original:raise ValueError('Unexpected substantive change outside this batch')
        kind='WALKTHROUGH_REPAIR_NEEDED' if lid.startswith(('W','D')) else 'TEACHING_REPAIR_NEEDED'
        t,n=re.subn(r'^Status: [^\n]*',f'Status: {kind} — the prior course-wide pass was rejected for voice and teaching clarity. This component still needs individual repair; it is not approved.',t,count=1,flags=re.M)
        if n!=1:raise ValueError('Missing original status')
        put(rel,t)
# Preserve the approved W02 pieces byte-for-byte, including their original prose.
w='scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md'
original=old(w);current=(ROOT/w).read_text()
for start,end in [
 ('**Chapter 4, after 2.3','**Chapter 6, after 2.4'),
 ('### Reserve recording plan — chapters 4–5 only; not spoken','### Source-led recording detail — not spoken')]:
    retained=original.split(start,1)[1].split(end,1)[0]
    if (start+retained).strip() not in current:raise ValueError('Approved W02 Reserve segment changed')
p=ROOT/'tools/guided_course.py';t=p.read_text()
if hashlib.sha1(b'blob '+str(len(p.read_bytes())).encode()+b'\0'+p.read_bytes()).hexdigest()!='80339e3c6e6c9ec73b9829ab8f57950c43f7c025':
    raise ValueError('Generator differs from reviewed source')
t=substitute(t,"def outputs(root: Path) -> dict[str,str]:",'''def review_state(row: dict) -> str:
    if row['id'] == '2.3':
        return 'Accepted teaching reference; filming separate'
    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:
        return 'Replacement written; voice review pending'
    if 'Status: WALKTHROUGH_REWRITE_REVIEW' in row['text']:
        return 'Narration revised; review and capture pending'
    return 'Needs individual teaching/voice repair'

def outputs(root: Path) -> dict[str,str]:''')
t=substitute(t,"Editorial pass completed over every listed script. Owner dictation/approval, professional review and capture evidence are separate.","The earlier course-wide pass was rejected for voice and teaching clarity. Only the Reserve is the accepted reference; replacement drafts and unrepaired components are distinguished below. Recording and professional review remain separate.")
t=substitute(t,"| {r['id']} | [{r['title']}]({r['path']}) | Reviewed | Pending | {r['gate']} |", "| {r['id']} | [{r['title']}]({r['path']}) | {review_state(r)} | {'Reference accepted; filming separate' if r['id']=='2.3' else 'Pending'} | {r['gate']} |")
t=substitute(t,"    eq('same sale gain illustration',D(20000)-D(16000),4000)","    eq('same sale gain illustration',D(20000)-D(16000),4000)\n    eq('generic annual premium monthly allowance',D(1200)/12,100)\n    eq('generic recurring bill full-year saving',D(40)*12,480)")
put('tools/guided_course.py',t)
for path in ('delivery/source-led-completion.md','delivery/source-led-batch-01.md'):
    text=(ROOT/path).read_text();title,body=text.split('\n',1)
    warning='\n\n> Superseded completion claim: Austin rejected the resulting course-wide prose for voice, natural delivery and instructional clarity. This file records earlier edits, not current teaching acceptance. See FINALIZATION-STATUS.md and HANDOFF.md for the individual repair work.\n'
    put(path,title+warning+body)
put('README.md', '''# Orange Plan Academy

**Teaching repair is in progress. The earlier course-wide pass did not meet Austin's standard for natural, direct teaching.** Lesson 2.3 (Reserve) is the accepted reference. Full replacement drafts for 2.1, 2.2, 2.4 and 2.5, plus matching W02 narration, are now ready for voice/judgment review. The rest still needs individual repair—not just final approval of the old prose.

Start with [Session 2](modules/02.md), or use the [Core reading order](DICTATION-ORDER.md) for clean spoken copies. The [production checklist](PRODUCTION-CHECKLIST.md) distinguishes the accepted reference, replacement drafts and unrepaired components.

| Work | Start here |
|---|---|
| Read the teaching | [Core](DICTATION-ORDER.md) · [Conditional Advanced](ADVANCED-DICTATION-ORDER.md) |
| Review the current repaired session | [Cash Flow, Reserve and Life Events](modules/02.md) · [Paired W02](scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md) |
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
''')
put('FINALIZATION-STATUS.md', '''# Course status: individual teaching repair in progress

## Why the course is not marked complete

After reading the September 8 course-wide pass, Austin said the scripts were hard to follow, did not use his voice, had repetitive sentence rhythm, and were confusing rather than direct and educational. He supplied the Reserve lesson as the better reference and asked for the same level of care across the scripts and walkthroughs.

The prior structural checks passed, but that did not establish teaching quality. Earlier completion notices are superseded. Do not treat this as a light polish of already accepted narration.

## Current repair progress

| Components | Current state |
|---|---|
| 2.3 and the accepted Reserve sections of W02 | Reference preserved without changes. Acceptance of the reference is not recording approval. |
| 2.1, 2.2, 2.4, 2.5 | Full spoken replacements written; integrated wording awaits Austin's voice/judgment review. |
| W02 chapters 1–3 and 6–7 | Corresponding narration and demonstration plan rewritten; exact screens, inputs, outputs and save behavior await verification. |
| All other Core and Advanced lessons, and W01/W03–W10/D07 | Individual teaching/voice repair still needed. Their substantive prose was not rewritten by this batch; only the misleading status header was corrected. |

The 51/15/11 inventory, course sequence, member documents and source household remain unchanged. A longer script, a passed check or a new status label does not establish that a learner can follow it.

## Review and continuing work

Read the clean spoken copies and the paired demonstration together. Check whether the explanation reflects Austin's judgment, explains the missing reasoning and leaves the member able to make the choice. Keep the next work in existing scripts rather than create another outline or workbook. Next is Debt; the opening sessions and all other unrepaired components also remain on the repair list.

## App and device recording

Use the approved redesign for exact navigation, source coverage, holdings/history handling, calculations, guardrails, Ask, exports and save/reload. Complete the fictional input gaps and record actual results. Missing promised behavior remains held and reported, not simulated. D07 requires the exact official device/setup procedure and safe recovery proof; a practice wallet does not prove another funded wallet's backup. No recording is approved by this batch.

## Professional and member evidence

Tax, account access, healthcare, lending, legal/estate and insurance execution still require their targeted reviews. Source-based editing here is not a new independent professional verification. Family/listener rehearsal, member pilot and actual support operations remain open until separately demonstrated. No pricing, terms, platform rollout or launch approval is implied.

## Repository state

The preceding working draft was published to main through PR #16 for Austin to read. New replacements remain explicitly review drafts even when integrated for that same purpose. Live merge/check identities belong in the repair PR conversation. Cleanup and pinned historical recovery stay intact. No app-repository, hosted-data, provider, wallet, financial, runtime or Production work is part of this repair.
''')
put('HANDOFF.md', '''# Current course handoff — repair the teaching, not the architecture

Austin rejected the bulk source-led prose after reading it. The accepted model is the complete Reserve explanation he supplied, including the conditional single-income/dependent liquidity judgment. Keep that lesson unchanged. Earlier claims that the entire written course was complete are superseded.

## Actual work in this repair

Full replacements: 2.1 (the previously prepared Cash Flow reading copy), 2.2 (Keep / Cut / Reduce), 2.4 (expected Life Events and funding), 2.5 (optional parent education commitment). W02 chapters 1–3 and 6–7 now contain the matching spoken explanations. The Reserve summaries and seven-beat recording block are unchanged. Duplicate abbreviated W02 cues are removed.

Every other canonical script is unchanged except its status line, which now says individual repair is still needed. The existing generator regenerates reading copies and no longer labels every lesson Reviewed. No new quality-scoring framework or competing master is created.

## Sources and limits

The current cash-flow fixture and prior lesson scopes remain. Original Cash Flow + Reserve slide text and notes supply income reliability, Keep / Cut / Reduce, usable surplus and transfer timing. Retrieved Global Brain passages supply worthwhile spending and recurring savings. The older Module 2 framework supplies larger-cost and withholding topics. August 25 dictation and private April 21 call passages supply the habit of explaining an input, then checking its effect and actual funding. The private material informs teaching patterns only; no names, raw quotations or client amounts are committed. No original audio listening or full visual review of every slide is claimed.

The original college comparison is retained: $80,000 parent commitment, $29,000 assigned to the older child, $51,000 gap and $850/month under flat-cost/zero-growth/full-pre-funding assumptions. No new return, aid, tax result, security, owner/beneficiary decision or saving start date is supplied. The separate $1,200 annual bill/$100 monthly and $40 monthly/$480 yearly illustrations are editorial arithmetic, not extra Reed facts.

Older categorical age/timeframe rules and historical app routes are not silently reinstated. The current accepted Reserve direction and latest course scope control those conflicts. Tax/legal/provider details still require their existing review; this is not a fresh outside-research audit.

## Next

Continue with Debt, one complete lesson and its matching working chapter at a time. Preserve the larger strategic-debt scope. Do not stop at changing the introduction or finish while retaining an unexplained middle. The opening sessions and the remaining Core/Advanced/practical components still need the same individual repair. Do not claim background execution or another whole-course completion.

Use existing `scripts/`, regenerate current reading copies, and keep review drafts visible in GitHub as requested. Do not change the app or record its unfinished screens. Check actual branch/PR state before writes, preserve source/fixture/capture bytes and historical recovery, and remove temporary authoring helpers before integration. A merge for reading is not Austin's approval of every line.
''')
print('Status correction applied; four teaching replacements and one walkthrough rewrite remain review drafts.')
