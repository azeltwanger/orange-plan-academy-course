#!/usr/bin/env python3
"""One-time owner-authorized removal of obsolete working-tree files.
Keep original source files, the current course and exact Git recovery evidence.
This tool is removed by its successful application. No external data access.
"""
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PIN='a7be495e670078cd44ea4e0792538b0eaa32dd95'
SELF='tools/_cleanup_course_repo.py'
REC='production/repository-cleanup.json'

def digest(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def put(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def exact(text,old,new):
    if text.count(old)!=1:raise ValueError('Ambiguous cleanup edit: '+old[:100])
    return text.replace(old,new,1)

assert not (ROOT/REC).exists(),'Cleanup already applied'
assert git('cat-file','-t',PIN).strip()==b'commit'
protected={str(p.relative_to(ROOT)):digest(p.read_bytes()) for base in ['scripts','source-material','fixtures','toolkit'] for p in (ROOT/base).rglob('*') if p.is_file()}
protected['PROMOTION-RECORD.json']=digest((ROOT/'PROMOTION-RECORD.json').read_bytes())
# Preserve the four verified historical scripts containing dictated explanations.
# They already contain later editorial/app corrections; do not relabel them raw audio transcripts.
kept={
 '00-1_how-to-use-this-course.md':'b0856eb661e6ece598d6d7b41618ca9b5308a3fe',
 '01-1_what-to-gather-before-you-build-the-plan.md':'e56ea2f1ee03fb5ead7b1dc175b86fd7ea173a3e',
 '01-2_the-three-layers-of-a-plan-and-setting-your-assumptions.md':'713b6c5c0b8e3eaae455f7e590b1a00641123cd7',
 '02-2_size-your-cash-reserve-in-months-of-spending.md':'3c6e856ca5a2db606788ddf6fea0ac7805d5f682'}
source_copies=[]
for name,expected in kept.items():
    old='archive/pre-guided-promotion/scripts/'+name
    data=(ROOT/old).read_bytes()
    assert blob(data)==expected and git('show',PIN+':'+old)==data
    new='source-material/historical-dictation/'+name
    dest=ROOT/new;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    source_copies.append({'old_path':old,'path':new,'sha256':digest(data),'git_blob':expected})
put('source-material/historical-dictation/README.md','''# Historical dictation-containing sources\n\nThese four files are byte-for-byte copies of the prior scripts labeled AUSTIN DICTATION. Their own headers explain that they also contain earlier factual, app-flow and walkthrough-separation edits. They are historical source evidence, **not current recording scripts, raw unedited dictation, or current capability approval**.\n\nOriginal separately supplied dictation remains unchanged in the parent directory. Use the current canonical `scripts/` and the root DICTATION-ORDER.md for review and recording preparation. Older outlines, generated versions and migration records are recovered through the pinned Git history described in ARCHIVE-RECOVERY.md. The exact copy hashes are in production/repository-cleanup.json.\n''')

# Delete only obsolete archives/workspace and explicitly retired build workflows/tools.
paths=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'archive').rglob('*') if p.is_file())
paths+=['course-v2/README.md','tools/guided-support.json','tools/editorial-amendments.json','.github/workflows/export-guided-review.yml','.github/workflows/finish-guided-course.yml','.github/workflows/member-deliverables.yml','.github/workflows/sync-source-led-script-pass.yml']
assert len(paths)==len(set(paths))
retired=[]
for path in paths:
    p=ROOT/path;assert p.is_file(),'Missing cleanup candidate: '+path
    historic=git('show',PIN+':'+path)
    # The active one-shot synchronization workflow is deliberately replaced for this cleanup.
    if path!='.github/workflows/sync-source-led-script-pass.yml':
        assert historic==p.read_bytes(),'Cleanup candidate changed: '+path
    retired.append({'path':path,'sha256':digest(historic),'git_blob':blob(historic)})
# All 255 prior-preservation entries must map exactly into the recovery manifest.
promotion=json.loads((ROOT/'PROMOTION-RECORD.json').read_text())
retired_by={r['path']:r for r in retired}
assert len(promotion['preserved'])==255
for r in promotion['preserved']:
    assert retired_by[r['archive_path']]['sha256']==r['sha256']
for path in paths:(ROOT/path).unlink()

put(REC,json.dumps({'schema_version':1,'history_commit':PIN,'reason':'Owner requested removal of obsolete course files; history and original sources retained. No branch/history deletion or force reset.', 'retired_files':retired,'retained_source_copies':source_copies,'original_source_hashes':{p:h for p,h in protected.items() if p.startswith('source-material/')},'protected_course_hashes':{p:h for p,h in protected.items() if not p.startswith('source-material/')},'retired_count':len(retired)},indent=2))
put('ARCHIVE-RECOVERY.md',f'''# Historical course recovery\n\nThe obsolete course versions have been removed from the current file tree. They remain in Git at commit `{PIN}`. No branch, commit history or original supplied dictation was deleted.\n\nThe four verified historical scripts containing Austin dictation also remain as byte-identical copies in `source-material/historical-dictation/`. Their older app/factual edits are historical, not current recording instructions.\n\n`production/repository-cleanup.json` identifies every removed file by path, Git blob and SHA-256. `PROMOTION-RECORD.json` remains unchanged and records the preceding preservation chain.\n\nTo read an old file without changing the current checkout:\n\n```sh\ngit show {PIN}:archive/pre-guided-promotion/MASTER-COURSE.md\n```\n\nTo verify all removed bytes against the pinned history after fetching full history:\n\n```sh\npython tools/guided_course.py history\n```\n\nA shallow export/ZIP can run the normal course checks, but cannot independently verify Git recovery. Use a full-history checkout for that command. The current course starts at DICTATION-ORDER.md; do not restore an old master over the active scripts.\n\nRemoved obsolete files: **{len(retired)}**. Current canonical lessons, read-aloud copies, member documents, fictional data and live approval/capture requirements are retained. The one-shot synchronization workflow and migration machinery have been retired; normal verification is read-only.\n''')

# Remove the retired migration path while retaining the current compiler and tests.
p=ROOT/'tools/guided_course.py';code=p.read_text()
code,n=re.subn(r'^def promote\(root: Path\) -> None:\n.*?(?=^def catalog\()', '',code, count=1, flags=re.M|re.S)
assert n==1
code=code.replace('promote: one-time, exact-input migration; preserves all prior active material.','history: verify retired files against the pinned Git history (full checkout required).',1)
code=code.replace('import argparse, hashlib, json, re, shutil, tempfile','import argparse, hashlib, json, re, shutil, tempfile, subprocess',1)
old='''    record=load_json(root/'PROMOTION-RECORD.json')
    for row in record['preserved']:
        if digest((root/row['archive_path']).read_bytes())!=row['sha256']: raise ValueError('Historical material changed: '+row['archive_path'])
'''
new='''    record=load_json(root/'PROMOTION-RECORD.json')
    preservation(root)
'''
code=exact(code,old,new)
helpers='''CLEANUP_PIN = 'a7be495e670078cd44ea4e0792538b0eaa32dd95'

def preservation(root: Path) -> dict:
    recovery=load_json(root/'production/repository-cleanup.json')
    if recovery.get('history_commit')!=CLEANUP_PIN: raise ValueError('Unexpected history pin')
    retired=recovery['retired_files']; by={r['path']:r for r in retired}
    if len(by)!=len(retired) or recovery['retired_count']!=len(retired): raise ValueError('Invalid cleanup inventory')
    old=load_json(root/'PROMOTION-RECORD.json')
    for row in old['preserved']:
        stored=by.get(row['archive_path'])
        if not stored or stored['sha256']!=row['sha256']: raise ValueError('Missing historical preservation record')
    for row in retired:
        p=Path(row['path'])
        if p.is_absolute() or '..' in p.parts: raise ValueError('Unsafe recovery path')
        if (root/p).exists(): raise ValueError('Obsolete file restored into current tree: '+str(p))
        if not re.fullmatch('[0-9a-f]{64}',row['sha256']) or not re.fullmatch('[0-9a-f]{40}',row['git_blob']): raise ValueError('Invalid recovery hash')
    for row in recovery['retained_source_copies']:
        data=(root/row['path']).read_bytes()
        if digest(data)!=row['sha256'] or by[row['old_path']]['sha256']!=row['sha256']: raise ValueError('Historical dictation copy changed')
    for path,expected in recovery['original_source_hashes'].items():
        if digest((root/path).read_bytes())!=expected: raise ValueError('Original dictation changed: '+path)
    return recovery

def history(root: Path) -> None:
    recovery=preservation(root)
    for row in recovery['retired_files']:
        data=subprocess.check_output(['git','show',CLEANUP_PIN+':'+row['path']],cwd=root)
        git_hash=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\\0'+data).hexdigest()
        if digest(data)!=row['sha256'] or git_hash!=row['git_blob']: raise ValueError('Historical recovery mismatch: '+row['path'])
    print('PASS: recovered and byte-verified',len(recovery['retired_files']),'retired files from pinned Git history; original dictation retained.')

'''
code=exact(code,'def check(root: Path) -> None:\n',helpers+'def check(root: Path) -> None:\n')
code=code.replace('preserved files.','historical preservation records (Git recovery checked separately).')
code=exact(code,"choices=['promote','build','check','test']","choices=['build','check','test','history']")
code=exact(code,"{'promote':promote,'build':build,'check':check,'test':tests}[args.command](ROOT)","{'build':build,'check':check,'test':tests,'history':history}[args.command](ROOT)")
# Extend the existing arithmetic and mutation checks, rather than introduce a second test framework.
code=exact(code,"    return {'scope':'Arithmetic teaching checks only;", "    eq('reserve after hypothetical project',D(32000)-D(30000),2000)\n    eq('same sale gain illustration',D(20000)-D(16000),4000)\n    return {'scope':'Arithmetic teaching checks only;")
old_end="        check(copy)\n\nif __name__=='__main__':"
new_end='''        check(copy)
        p=copy/'production/repository-cleanup.json'; saved=p.read_bytes(); broken=load_json(p)
        removed=broken['retired_files'].pop(0); broken['retired_count']-=1; p.write_text(json.dumps(broken))
        try: preservation(copy)
        except (ValueError, KeyError): print('PASS mutation: missing history recovery entry')
        else: raise ValueError('Recovery-entry mutation escaped')
        p.write_bytes(saved)
        retained=load_json(p)['retained_source_copies'][0]['path']; q=copy/retained; saved_source=q.read_bytes(); q.write_bytes(saved_source+b'changed')
        try: preservation(copy)
        except ValueError: print('PASS mutation: changed historical dictation copy')
        else: raise ValueError('Source-copy mutation escaped')
        q.write_bytes(saved_source)
        check(copy)

if __name__=='__main__':'''
code=exact(code,old_end,new_end)
put('tools/guided_course.py',code)

# Retire obsolete current-status statements, without changing the lesson source files.
put('README.md','''# Orange Plan Academy\n\n**The written source-led course pass is complete. Start with [the Core reading order](DICTATION-ORDER.md).** Integrated wording still needs Austin's final voice/judgment review. Exact app footage, device tests and professional reviews remain separate from the written scripts. Nothing here implies a launch or merge.\n\n| Work | Start here |\n|---|---|\n| Read and review the teaching | [Core](DICTATION-ORDER.md) · [Conditional Advanced](ADVANCED-DICTATION-ORDER.md) |\n| Prepare the paired demonstrations | [Learning and filming order](FILM-ORDER.md) |\n| Read the entire course | [Spoken text](ALL-SCRIPTS.md) · [Core with notes](MASTER-COURSE.md) · [Advanced with notes](MASTER-ADVANCED.md) |\n| Use the member documents | [Toolkit](toolkit/README.md) · [Six named deliverables](toolkit/deliverables/README.md) |\n| See what remains before publication | [Current status](FINALIZATION-STATUS.md) · [Capture evidence](CAPTURE-RECEIPTS.md) |\n\nThe current course is **51 core clips**, including optional college, **15 conditional Advanced clips**, **ten app working sessions** and **one device demonstration**. Keep the approved Start Here plus ten-session sequence. Debt is Session 3 and Allocation is Session 4. There is no arbitrary 150-minute cap.\n\n## One editing source\n\nEdit `scripts/` only. Narration lives under `### Read aloud`; visual, production and screen-dependent notes are not spoken. `teleprompter/`, `lesson-text/`, `modules/`, the reading orders and masters are generated copies of those same scripts, not competing versions.\n\n```sh\npython tools/guided_course.py build\npython tools/guided_course.py check\npython tools/guided_course.py test\npython -m unittest discover -s tests -p test_member_deliverables.py -v\npython tools/guided_course.py history\n```\n\nThe first four commands verify content structure, synchronization, arithmetic and member materials. The last verifies removed historical files from Git and requires full repository history. Normal CI is read-only; there is no retained one-shot migration or branch-writing workflow.\n\n## Original material and old versions\n\nOriginal supplied dictation remains unchanged in `source-material/`. Four verified historical dictation-containing scripts are retained in its clearly marked historical subfolder. Obsolete outlines, generated scripts, superseded migration files and old workflows have been removed from the current tree, not from Git history. [Recovery instructions](ARCHIVE-RECOVERY.md) and [the exact manifest](production/repository-cleanup.json) preserve access. Do not use historical material as a current recording order.\n\n[What changed in the completed pass](delivery/source-led-completion.md) · [App alignment](V1-COURSE-ALIGNMENT.md) · [Landing-page corrections](LANDING-PAGE-ALIGNMENT.md) · [Sources](PRIMARY-SOURCES.md).\n\nRaw client transcripts, identifying financial records, wallet secrets, credentials and font files stay out of the repository. The approved Reserve explanation and its conditional liquidity judgment remain intact.\n''')
put('FINALIZATION-STATUS.md','''# Course status: written pass complete; recording evidence still open\n\n## Written work completed\n\nAll 51 core explanations and 15 conditional Advanced explanations have received the source-led editorial pass. The ten working-session plans and separate device demonstration include the relevant example inputs, action/interpretation, reusable narration, build/procedure-specific inserts and member finish. Original dictation, the fictional source data, the accepted Reserve reference and the six member deliverables are preserved. Detailed changes are in delivery/source-led-completion.md.\n\nThis is completion of the **written editorial and recording-plan pass**, not blanket voice approval, filmed content or proven student outcomes. Useful existing passages were retained and specific teaching gaps were edited; not every sentence needed replacement.\n\n## Austin's review\n\nRead chronologically from DICTATION-ORDER.md and the conditional Advanced order. Check whether the wording and judgment are yours and whether the learner can make the intended choice. The course structure and teaching approach are already accepted; no further architecture reset is needed. The Reserve pilot's reference approval does not automatically approve all later wording.\n\n## App and device recordings\n\nRecord app screens only against the approved redesign. Complete the fictional capture inputs and use the actual saved plan, results and save/reload evidence. Exact navigation, source coverage, holdings/history reconciliation, tax and withdrawal outputs, annual guardrails, Ask, communication and exports remain capture-dependent. Missing promised behavior remains held and reported, not fabricated or silently excused.\n\nD07 and device-specific footage require the exact manufacturer/model, firmware, backup standard, current official procedure and safe small-value test. A practice-wallet recovery does not prove the backup for a different funded holding. Do not reset a funded primary wallet as a first test or show usable secrets.\n\n## Professional and member proof\n\nTargeted tax, account-access, healthcare, lending, legal/estate and insurance reviews remain necessary before publishing their execution-specific content. Primary references support mechanisms, not licensed sign-off. Real agreements, quotes, program eligibility and provider/device capabilities need verification at use.\n\nThe family/listener rehearsal, member pilot and correction of observed difficulties remain open until performed. The prepared Plan Clinic/community/annual-refresh setup material does not establish an operating service. Pricing, access terms, support cadence and launch cutover are not approved by this edit.\n\n## Repository cleanup\n\nObsolete working-tree versions and one-shot tools/workflows are retired. Original supplied dictation remains unchanged; historical dictation-containing scripts are copied byte-for-byte and the rest is recoverable from the pinned Git history. ARCHIVE-RECOVERY.md and production/repository-cleanup.json explain and verify the boundary.\n\nAll work remains on the draft course branch. No app repository, hosted record, financial transaction, provider connection, runtime setting, Production, course rollout or merge was changed.\n''')
put('HANDOFF.md','''# Current course handoff\n\nThe source-led written pass covers the full current Core, conditional Advanced and paired practical plans. Start at README.md, then DICTATION-ORDER.md and FILM-ORDER.md. Detailed editorial completion is in delivery/source-led-completion.md; the remaining filming/professional/member gates are in FINALIZATION-STATUS.md.\n\nActive work remains Academy Draft PR #15 on `course-source-led-script-pass-20260908`, stacked on the member-deliverables branch from PR #14. PR #13 retains the accepted course architecture. Do not reset or merge any of these as a side effect of reviewing text. Exact tested heads and Actions evidence are in the PR conversation, not an assumed static SHA in this handoff.\n\nOriginal dictation, unique retained historical source copies and Git recovery are documented in ARCHIVE-RECOVERY.md. No obsolete master should be promoted over canonical scripts. Update scripts, regenerate, verify, then read the affected text in context.\n\nNext work is final voice review and approved-build/device recording preparation, not another unfinished editorial batch. Real saved demo outputs, safe recovery tests, professional review, listener/member pilot and verified support operations still need their own evidence.\n''')
put('COURSE-VERIFICATION.md','''# Course verification\n\nThe current compiler checks the 77-component inventory, exact generated-copy parity, fictional arithmetic, preserved original dictation and historical-copy hashes, plus complete recovery-manifest coverage of the prior 255-file preservation chain. Existing mutation tests also reject a missing history entry or changed retained source copy. Member-deliverable tests remain part of the same verification.\n\n`python tools/guided_course.py history` independently reads every removed file from the pinned Git commit and checks both its Git blob and SHA-256. It requires a full-history checkout and does not pretend the old files are still in the current tree.\n\nExact successful runs and tested final heads are recorded on PR #15 only after actual readback. A prepared workflow or this description is not itself a passing result. The one-shot writer/migration workflows are retired; normal verification has read-only repository permissions.\n\nThese checks verify structure, preservation, calculation examples and synchronization. They do not establish Austin's voice approval, a usable app demonstration, legal/tax/insurance advice, device recovery or learner success. Those gates remain in FINALIZATION-STATUS.md and CAPTURE-RECEIPTS.md.\n''')
for path in ['DICTATION-SOURCE-MAP.md','SOURCE-MATERIAL-POLICY.md']:
    text=(ROOT/path).read_text()
    if path=='DICTATION-SOURCE-MAP.md':
        text=exact(text,'The prior active scripts are also preserved byte-for-byte under `archive/pre-guided-promotion/scripts/`.','The prior active scripts are preserved in the pinned Git history described in `ARCHIVE-RECOVERY.md`; four verified historical dictation-containing scripts also remain as byte-identical copies in `source-material/historical-dictation/`.')
    else:
        text=exact(text,'Prior active material is retained in `archive/pre-guided-promotion/` and hash-checked by the build.','Prior active material is retained in pinned Git history, with verified dictation-containing copies under `source-material/historical-dictation/`. The current checks verify the recovery manifest and retained bytes; the history command verifies removed content directly from Git. See `ARCHIVE-RECOVERY.md`.')
    put(path,text)

put('.github/workflows/verify-course.yml','''name: Verify current Academy course\non:\n  pull_request:\n    types: [opened, synchronize, reopened]\npermissions:\n  contents: read\njobs:\n  verify:\n    runs-on: ubuntu-latest\n    timeout-minutes: 5\n    steps:\n      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262\n        with:\n          fetch-depth: 0\n          persist-credentials: false\n      - name: Check current course and member documents\n        run: |\n          python tools/guided_course.py check\n          python tools/guided_course.py test\n          python -m unittest discover -s tests -p test_member_deliverables.py -v\n          python tools/guided_course.py history\n          git diff --exit-code\n''')
for p,h in protected.items():assert digest((ROOT/p).read_bytes())==h,'Current source changed during cleanup: '+p
Path(__file__).unlink()
print('CLEANUP: removed',len(retired),'obsolete working-tree files; retained four byte-identical historical dictation-containing scripts.')
print('Current scripts, accepted Reserve, fixture, toolkit, source-material and promotion record unchanged.')
