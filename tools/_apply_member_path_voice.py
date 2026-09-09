#!/usr/bin/env python3
"""Apply the approved navigation and authored line edits to the existing course.

Temporary authoring helper. No model calls, external data, app operations,
financial transactions or quality scores. Remove with its staging inputs.
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, html, json, re, runpy, subprocess

ROOT=Path(__file__).resolve().parents[1]
BASE='f6392a6341c23c557e605506dab3530b67efa146'
GENERATOR='01d3d69c06ea73dd140fc67436bd199f52ba1455'
RESERVE='2c107a394a93cc877c73f011dfe37fb5ad3d94b1'
A72='scripts/advanced/A7-2_decide-which-custody-responsibilities-the-household-can-maintain.md'
A72_BLOB='0443c4640a4f4b431429eab204f5fe9dc0b67413'
STAGING=['_voice_edits_main.py','_voice_edits_later.py','_voice_edits_situations.py','_course_navigation.py','_apply_member_path_voice.py']


def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode()
def hashblob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def put(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def once(text,before,after):
    if text.count(before)!=1:raise ValueError('Expected one bounded edit: '+before[:100])
    return text.replace(before,after,1)
def spoken(text):
    m=re.search(r'^### Read aloud\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S)
    if not m:raise ValueError('No speech boundary')
    return m,m.group(1).strip()
def add_production(text,body):
    marker='### Production notes'
    return once(text,marker,marker+'\n\n'+body.rstrip())

TITLES={
 '4.4':'Decide where the next dollar goes',
 '4.7':'Set up contributions and investment purchases',
 '5.2':'Rebuild the purchase records you need',
 '5.5':"Choose this year's tax actions",
 '6.8':'Decide what to spend next year',
 '7.3':'Secure your accounts',
 '7.4':'Make the family custody map',
 '8.1':'Choose who can act for your family',
 '8.3':"Write your family's first instructions",
 '10.2':'Explain your plan and set the next actions',
 'A3.1':'Plan how to manage a Bitcoin-backed loan',
 'A5.3':'Compare the full cost of moving states',
 'A6.3':'Check access to retirement accounts before 59½',
 'A7.3':'Check what your custody arrangements share',
}

# Exact quoted narration replacements. Non-spoken safeguards stay in their original sections.
WORKING_EDITS={
'W01':[
('“A connection can supply part of the picture. This source has provided the balance. Now check whether it also supplied the investments and history. If it did not identify the holdings, that money is not automatically cash. We know exactly which part still needs attention.”',
 '“The connection supplied this balance. Did it also identify the investments and purchase history? If the holdings are missing, don\'t call the balance cash. Check the statement to find what belongs inside the account.”'),
],
'W04':[
('“First we found the dollars needed for actual commitments. That produced the cash amount. Then we chose what the remaining long-term money should provide. The stock allocation is a choice to own businesses alongside Bitcoin, not an automatic destination for every spare dollar.”',
 '“The Reserve and purchase need this amount in cash. That is where the cash percentage came from. This household chose stocks for the remaining long-term money because it wanted business ownership alongside Bitcoin.”'),
('“Changing the contribution and changing what it buys may be two instructions. When the first contribution happens, check both. Did the money reach the intended account, and did it buy the investment? The confirmation is what lets us update the plan from an intention to something actually done.”',
 '“Check both instructions when the first contribution arrives. Did the right amount reach the account, and did it buy the intended investment? If it is still cash, check whether the purchase instruction is missing.”'),
],
'W05':[
('“This export supports preparation and review. It is not the filed return, and exporting successfully does not prove every record is complete. Here is the question we want answered, the evidence behind it, and the part still needing verification.”',
 '“Give the tax professional the relevant records and the question you need answered. Check what this export includes and what is missing. It is tax data for preparation and review, not a filed return.”'),
],
'W06':[
('“Move to the year when the next income source begins. The account balance did not suddenly become a different portfolio; the job we are asking it to do changed.”',
 '“Now open the year this income begins. How much less do investments need to provide, after updating taxes and the other costs?”'),
('“Which source pays for this period before later income begins? The total assets are not enough of an answer. Point to the account and the rule that makes it usable. If we wait for the benefit, show the extra funding needed before it starts as well as the later income it provides.”',
 '“Which account pays for these early years, and can you use it at that time? If the benefit starts later, compare the extra withdrawals needed before it begins with the income it provides afterward.”'),
],
'W08':[
('“The letter gets the reader started. The packet supports the follow-up. Let\'s read the first page without my explanation: whom would you contact, how would you verify the contact, and what should not be rushed? Fix the confusing sentence before adding another page.”',
 '“Read the first page without my help. Whom would you contact, and how would you check that you have the right person? If a step is unclear, let\'s fix it and try again.”'),
],
'W09':[
('“Next year starts from this record: what we chose, why, and what remains to be done. The readable summary helps us review the decisions. The backup has a different job, and its restore process needs its own verification.”',
 '“Save this summary so the next review starts with the decisions and reasons in front of you. Keep the plan backup separately and check that its restore process works before relying on it.”'),
],
'W10':[
('“Every statement here needs to describe the same plan. Start with the life it is funding, then trace the important numbers back to their source. A result is useful when you can explain what supports it and what still needs to change.”',
 '“Start with the life you want to fund. Check the important numbers against the accounts and the years they pay for. Which part works as intended, and what still needs changing?”'),
('“This is the plan we intend to follow. These actions are completed, these still need doing, and these begin only after their condition occurs. The next review starts with these reasons intact, not with a blank page.”',
 '“Record what you have completed and what you still need to do. Keep future transfers tied to the date or event that makes their money available. Save the reasons too, so you know what to review next time.”'),
],
}


def apply():
    g=ROOT/'tools/guided_course.py'
    if hashblob(g.read_bytes())!=GENERATOR:raise ValueError('Generator differs from reviewed base')
    original_tool=runpy.run_path(str(g));rows=original_tool['catalog'](ROOT);by={r['id']:r for r in rows}
    if len(rows)!=77:raise ValueError('Unexpected active inventory')
    for r in rows:
        data=(ROOT/r['path']).read_bytes()
        if data!=subprocess.check_output(['git','show',BASE+':'+r['path']],cwd=ROOT):raise ValueError('Canonical base changed: '+r['id'])
    if hashblob((ROOT/by['2.3']['path']).read_bytes())!=RESERVE:raise ValueError('Reserve changed')
    if hashblob((ROOT/A72).read_bytes())!=A72_BLOB:raise ValueError('A7.2 retirement source changed')
    all_edits={};moves={};modules={}
    for filename in STAGING[:3]:
        module=runpy.run_path(str(ROOT/'tools'/filename));modules[filename]=module
        for lid,edits in module['EDITS'].items():
            if lid in all_edits:raise ValueError('Duplicate edit group')
            all_edits[lid]=edits
        moves.update(module.get('MOVE_TO_NOTES',{}))
    expected=set(original_tool['CORE_IDS']+original_tool['ADV_IDS'])-{'2.3','A7.2'}
    if set(all_edits)!=expected:raise ValueError('Unreviewed spoken inventory: '+str(expected^set(all_edits)))
    count=0;note_count=0;changed=[]
    for lid,edits in all_edits.items():
        row=by[lid];text=row['text'];m,read=spoken(text);paras=read.split('\n\n');moved=[]
        for prefix,replacement in edits:
            # Correct the authored selector to the exact source sentence, not a broad text search.
            if lid=='4.4' and prefix=='That is the contribution waterfall:':prefix='This is the contribution waterfall:'
            matches=[i for i,p in enumerate(paras) if p.startswith(prefix)]
            if len(matches)!=1:raise ValueError('Paragraph selector '+lid+' '+repr(prefix)+' matched '+str(len(matches)))
            i=matches[0];prior=paras[i]
            if prefix in moves.get(lid,[]):moved.append(prior)
            paras[i]=replacement.strip();count+=1
        if lid=='7.1':
            module=modules['_voice_edits_later.py']
            positions=[i for i,p in enumerate(paras) if p.startswith(module['CUSTODY_INSERT_AFTER'])]
            if len(positions)!=1:raise ValueError('Custody integration point missing')
            extra=module['CUSTODY_INSERT'].replace('maintain secure sign-in and backup access, check the recovery instructions, and keep the family contact list current.','maintain secure sign-in and backup access, follow appropriate device and software updates, review provider changes, check the recovery instructions, and keep the family contact list current.')
            paras[positions[0]+1:positions[0]+1]=extra.split('\n\n')
        updated='\n\n'.join(p for p in paras if p)
        if updated==read:raise ValueError('Claimed unchanged edit '+lid)
        text=text[:m.start(1)]+updated+'\n\n'+text[m.end(1):]
        text=re.sub(r'^Status: [^\n]*','Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.',text,count=1,flags=re.M)
        if lid in TITLES:text=re.sub(r'^(# [^ ]+ — )[^\n]+',lambda m:m.group(1)+TITLES[lid],text,count=1)
        if moved:
            note_count+=len(moved)
            text=add_production(text,'**Moved out of narration in the language pass:** The following source wording records production/evidence limits, not instructions to read to members. Its substantive limits remain in force.\n\n'+'\n\n'.join(moved)+'\n')
        if lid=='7.1':
            text=add_production(text,'**A7.2 folded into this section:** operating-task assignment, willingness and backup responsibility, safe practice of ordinary tasks, recognizing a need to simplify, and the cost/support trade-off are now taught here. The absence rehearsal and agreement of contacts are in 7.4 and W07. No separate responsibility worksheet or extra lesson is required. The original is pinned in MERGED_LESSON in the generator.\n')
            text=text.replace('Advanced7.1–7.3 own detailedcomparisons.','The related architecture and shared-dependency lessons provide their distinct situational comparisons; former A7.2 is merged here and into 7.4/W07.')
        if lid=='7.4':
            text=add_production(text,'**A7.2 rehearsal integration:** use the existing custody map. The helper must consent to the role; let them attempt the non-secret starting steps without coaching every answer, record the actual gap, correct it and try again. No successful rehearsal is claimed by writing this instruction.\n')
        put(row['path'],text);changed.append(lid)
    # Canonical conditional routing. Internal IDs and surviving file paths remain stable.
    routes=modules['_voice_edits_situations.py']['ROUTES']
    if set(routes)!=set(original_tool['ADV_IDS'])-{'A7.2'}:raise ValueError('Missing situational placement')
    for lid,(after,when,before,back) in routes.items():
        p=ROOT/by[lid]['path'];t=p.read_text()
        t=once(t,'Kind: advanced','Kind: conditional')
        t,n=re.subn(r'^Use when: [^\n]*','Use when: '+when,t,count=1,flags=re.M)
        if n!=1:raise ValueError('Missing original Use when '+lid)
        t=t.replace('Use when: '+when,'Use when: '+when+'\nAfter lesson: '+after+'\nComplete before: '+before+'\nReturn to: '+back,1)
        put(by[lid]['path'],t)
    for lid,pairs in WORKING_EDITS.items():
        text=(ROOT/by[lid]['path']).read_text()
        for before,after in pairs:text=once(text,before,after)
        put(by[lid]['path'],text)
    # Merge the practical responsibility work into the existing W07, not an extra worksheet.
    p=by['W07']['path'];t=(ROOT/p).read_text()
    t=once(t,'**Member finish:** An intentional direction for every meaningful holding and a specific first protection action.',
        '**Responsibility check — show and discuss:** Use the existing custody map to assign the ordinary tasks and a backup: address verification, secure sign-in and recovery access, appropriate device/software updates, provider changes and current family instructions. Ask who is willing to do each task and where suitable help is needed. Practice technical steps only on the separately reviewed safe setup; do not risk funded holdings.\n\n**Narration:**\n\n“Who will keep each part working, and who can help when that person is unavailable? Ask them before assigning the role. If an ordinary task is too difficult to repeat reliably, simplify it, practice it safely, or arrange suitable help.”\n\n**Member finish:** An intentional arrangement, agreed operating responsibilities and backups, and the first protection action.')
    t=once(t,'**Member finish:** A usable dated map and truthful protection status with the relevant family starting process.',
        '**Rehearsal detail — not spoken:** Fold the former A7.2 operator-absent exercise into this existing chapter. Let a consented helper attempt the non-secret first steps without coaching each response; verify the primary and backup contacts have agreed, record any missing instruction, correct it and repeat the affected step. No actual transfer, credential guessing, impersonation or legal authority is inferred from the exercise.\n\n**Member finish:** A dated custody map the intended helper can use, with actual rehearsal evidence or clearly recorded gaps and agreed tasks.')
    put(p,t)
    # Put the relevant branch reminders in the working file before its run sheet.
    for lid in ['W01','W03','W04','W05','W06','W07','W08']:
        subset=[(a,v) for a,v in routes.items() if lid in v[3]]
        if lid=='W07' and 'A7.4' not in [a for a,v in subset]:subset.append(('A7.4',routes['A7.4']))
        if not subset:continue
        p=by[lid]['path'];t=(ROOT/p).read_text()
        block='### For your situation — recording route, not spoken\n\n'
        for a,(parent,when,before,back) in subset:
            target='../'+by[a]['path'].split('scripts/',1)[1]
            block+=f'- After {parent}, [{a}]({target}): {when} {before} Return to {back}.\n'
        t=once(t,'### Run sheet',block+'\n### Run sheet')
        put(p,t)
    # Remove the duplicated lesson and only its generated representations.
    for p in [A72,'lesson-text/'+A72.split('scripts/',1)[1],'teleprompter/advanced/A7-2.txt']:
        target=ROOT/p
        if not target.is_file():raise ValueError('Missing exact retirement target '+p)
        target.unlink()
    # Integrate the navigation into the existing generator; preserve arithmetic/preservation logic.
    t=g.read_text();t=once(t,"'A7.1','A7.2','A7.3'","'A7.1','A7.3'")
    payload=(ROOT/'tools/_course_navigation.py').read_text().split('\n',1)[1]
    start=t.index('def review_state(');end=t.index('def build(',start)
    t=t[:start]+payload.strip()+'\n\n'+t[end:]
    hist="    print('PASS: recovered and byte-verified',len(recovery['retired_files']),'retired files from pinned Git history; original dictation retained.')"
    t=once(t,hist,hist+'\n    merged_history(root)')
    # Actual route omission is a structural failure, not a measure of teaching quality.
    at="        q.write_bytes(saved_source)\n        check(copy)"
    tests="""        q.write_bytes(saved_source)
        check(copy)
        r=next(x for x in catalog(copy) if x['id']==ADV_IDS[0])
        p=copy/r['path']; saved=p.read_bytes()
        p.write_text(re.sub(r'^After lesson: .+$','After lesson: 99.99',saved.decode(),flags=re.M))
        try: check(copy)
        except ValueError: print('PASS mutation: invalid situational parent')
        else: raise ValueError('Invalid route escaped')
        p.write_bytes(saved)
        p.write_text(re.sub(r'^Return to: .+$','',saved.decode(),flags=re.M))
        try: check(copy)
        except ValueError: print('PASS mutation: missing return route')
        else: raise ValueError('Missing return route escaped')
        p.write_bytes(saved)
        check(copy)"""
    t=once(t,at,tests)
    put('tools/guided_course.py',t)
    # No changes to numbers, assumptions, member templates, source files or device procedure.
    for lid in ['2.3','W02','D07']:
        if (ROOT/by[lid]['path']).read_text()!=by[lid]['text']:raise ValueError('Protected script changed '+lid)
    if original_tool['arithmetic'](ROOT)!=runpy.run_path(str(g))['arithmetic'](ROOT):raise ValueError('Arithmetic changed')
    if section_content(original_tool['arithmetic']) is not None:pass
    put('README.md',readme())
    put('FINALIZATION-STATUS.md',status())
    put('HANDOFF.md',handoff(count,note_count))
    record=ROOT/'delivery/teaching-revision.md';text=record.read_text()
    notice='> Revision history: the original complete-draft counts below describe the earlier pass. The latest approved structure and spoken-language edit are recorded in the final section, One main path and spoken-language cleanup. Current counts and routes are in the reading order and manifest.\n\n'
    first,rest=text.split('\n',1);text=first+'\n\n'+notice+rest.lstrip()
    text+='\n\n'+revision(count,note_count)
    put('delivery/teaching-revision.md',text)
    print(f'APPLIED: {len(changed)} spoken lesson edits, {count} targeted paragraph edits, {note_count} production/evidence passages moved out of speech; A7.2 merged; 14 contextual routes. Owner review remains open.')


def section_content(_):
    # A no-op is intentionally not a quality signal; actual arithmetic equality is checked above.
    return None


def readme():
    return '''# Orange Plan Academy

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
'''

def status():
    return '''# Course status — one main path, written drafts under review

The approved structure is one complete main path with For your situation lessons beside the relevant decision. The extra work is required when the member’s chosen strategy depends on it, not because the member identifies as advanced. Each placement includes when to use it, what must be completed before relying on it, and where to return.

There are 65 active teaching lessons: 50 shared-path lessons, the conditional college lesson, and 14 other situational lessons. A7.2 is merged into 7.1, 7.4 and W07. Ten app working sessions and the device demonstration remain. The internal identifiers and surviving file paths are stable.

## This editorial pass

The 64 surviving teaching scripts other than the accepted Reserve receive individually selected paragraph edits. The explanations, mathematical examples, account distinctions and trade-offs are retained; this is not another full rewrite or a uniform shortening exercise. Production commentary is moved to production notes instead of being read to members. Useful responsibility assignment and rehearsal work from A7.2 is integrated, not discarded.

The Reserve script, W02 including its accepted Reserve block, and the exact safe D07 run sheet are unchanged. Other walkthrough changes tighten selected speech, route applicable extra lessons before the relevant decisions, and integrate the custody-responsibility exercise into W07. Non-spoken safety and verification requirements remain.

## Still needs evidence

Austin has not approved every new line. Read the section and paired walkthrough together and correct the specific voice or judgment issue in the canonical script. No word count, automated check or new navigation establishes learner comprehension.

Actual approved-build inputs, calculations, account/source behavior, Ask, exports, save/reload and communication features remain recording prerequisites. Device demonstrations require the exact current procedure, a safe authorized test and actual scoped evidence. The fixed fictional household is not an already-calibrated engine result.

Professional tax, access, lending, coverage, insurance and estate review remains separate. This pass edits the supplied course; it does not introduce a new financial research conclusion, current rate, tax rule or product recommendation. The retirement video remains a voice/structure reference only.

The main-path structure is applied to repository reading and playback instructions, not a live course-platform configuration. Student release, pricing, service operations and renewal value are not validated or changed. Original sources, fixture, toolkit, tests and capture records are preserved; exact implementation and verification evidence belongs in the PR handoff.
'''

def handoff(count,note_count):
    return f'''# Current handoff — member path and spoken-language cleanup

Austin accepted one main learning path with situation-specific lessons placed where the decision occurs, and asked for an AI-slop pass. This implements that decision without another curriculum reset or importing the retirement video’s financial assumptions.

## Actual changes

- The reading order, section files, combined spoken copy, playback/filming order and reference index now use Main path and For your situation. Each additional lesson owns its use condition, parent lesson, prerequisite timing and return route in its canonical metadata. No separate advanced progression is required.
- A7.2’s distinct operating tasks, agreed responsibility/backup, maintainability and support-cost discussion are in 7.1. Its uncoached absence rehearsal and contact agreement are in 7.4/W07. The duplicate script and its two generated copies are removed; the exact source commit/blob is pinned and verified.
- All 64 surviving non-Reserve teaching scripts received individually authored paragraph edits: {count} selected replacements/deletions, with {note_count} producer/evidence passages retained outside spoken text. Existing reasoning, numbers and useful qualifications remain. This is a copyedit, not a claim every script was rewritten from scratch or approved.
- Selected walkthrough narration is tightened. Applicable extra-lesson reminders are in the relevant run sheets, and W07 includes the merged responsibility work. D07 and W02 remain byte-identical. The accepted 2.3 remains byte-identical.

The course now has 65 active teaching lessons: 50 shared-path lessons, one conditional college lesson and 14 additional situational lessons, plus 11 practical files. Internal A IDs and surviving paths are stable for references. The former A7.2 is recoverable at `{BASE}` with blob `{A72_BLOB}`.

## Scope and review

No new financial principles, product preferences, legal conclusions, formula assumptions or source household facts were introduced. Original source-material, fixture, toolkit, tests, capture register and the original 264-file recovery inventory are unchanged. This pass uses the actual current scripts and the owner-supplied speaking reference, not a new complete deck/audio audit.

The temporary authoring scripts and branch-writing workflow must be removed before integration. Read-only CI must pass on the cleaned candidate and the exact head must be checked before normal merge for owner reading. No force push, history rewrite, branch deletion or app/financial/Production operation is part of this work.

## What remains

Owner read-through and specific wording/judgment corrections; actual approved-build and device demonstrations; relevant professional review; and a real member’s ability to complete and explain the decisions. Do not confuse the written pass, a GitHub merge or structural test with proof of those outcomes. There is no promise of unattended continuation or changed student access.
'''

def revision(count,note_count):
    return f'''## One main path and spoken-language cleanup

Following Austin’s acceptance, the member structure is one main path with For your situation lessons at their relevant decisions. Each has a concrete use condition, completion timing and return to the working chapter. The existing separate index is a reference view, not a second or higher-level course. The core/advanced file paths remain technical identifiers for stable links.

A7.2 was genuinely redundant with the core custody discussion. Its distinctive task assignment, operator willingness, backup responsibility, safe practice, simplification and support-cost reasoning were integrated into 7.1. The uncoached operator-absence rehearsal, actual gaps and agreement of contacts were incorporated into 7.4 and W07 using the existing custody map. No responsibility worksheet or second map was added. The original script is recoverable from commit `{BASE}`, blob `{A72_BLOB}`; the existing history command now verifies that additional merged source. The old 264-entry historical-cleanup manifest remains unchanged.

The language pass makes {count} individually selected paragraph replacements or deletions across all 64 surviving non-Reserve teaching scripts. {note_count} passages containing production/evidence instructions are retained in production notes rather than read aloud. Examples include removing “the fixture does not establish,” “without inventing a completed recovery test,” “the approved build,” and instructions not to borrow landing-page results from narration. Those evidence constraints still apply to production. Hypothetical examples remain identified; necessary account, tax, custody and execution qualifications are not treated as filler.

The edit replaces abstract directions and repeated lesson-completion speeches with specific actions. Several titles become plainer; the main explanations and calculations stay. This is not a global ban on words such as actual or evidence, a length target, or a quality score. The original voice reference supplies directness and progression only, not its rates, retirement formula or assurances.

Current active counts are 50 shared-path lessons, one college lesson for the relevant household, 14 other situational lessons, ten app working sessions and one device demonstration. The accepted Reserve, the entire W02 and the safe D07 procedure are byte-identical. Original financial data, member documents, source files and capture receipts are unchanged. No new outside financial research, individual recommendation or price claim is made in this copyedit.

The course-level approval and real-world evidence boundaries above remain. Actual run, candidate and merge identities are posted only after they are verified in the PR conversation.
'''


def reader(out):
    tool=runpy.run_path(str(ROOT/'tools/guided_course.py'));rows=tool['catalog'](ROOT);by={r['id']:r for r in rows};order=tool['member_order'](rows)
    out.mkdir(parents=True,exist_ok=True)
    nav=[];body=[]
    for lid in order:
        r=by[lid];target='lesson-'+lid.replace('.','-');conditional=lid in tool['ADV_IDS'] or lid=='2.5'
        label='For your situation' if conditional else 'Main path'
        nav.append(f'<a class="{"extra" if conditional else "main"}" href="#{target}">{html.escape(lid+" · "+r["title"])}</a>')
        paragraphs=''.join('<p>'+html.escape(p).replace('\n','<br>')+'</p>' for p in r['read'].split('\n\n'))
        if conditional:
            route=tool['situation_route'](r) if lid!='2.5' else {'when':'You intend to help fund education.','before':'Otherwise continue to Debt.','return':'W02 chapter 7, then lesson 3.1'}
            body.append(f'<details id="{target}"><summary><span class="eyebrow">For your situation</span><span>{html.escape(r["title"])}</span></summary><div class="route"><p>{html.escape(route["when"]+" "+route["before"])}</p><p><strong>Return to:</strong> {html.escape(route["return"])}.</p></div>{paragraphs}<a class="back" href="#top">Back to contents</a></details>')
        else:
            scope='Accepted Reserve reference — unchanged' if lid=='2.3' else 'Spoken draft for owner review'
            body.append(f'<section id="{target}"><p class="eyebrow">{scope}</p><h2>{html.escape(lid+" — "+r["title"])}</h2>{paragraphs}<a class="back" href="#top">Back to contents</a></section>')
    css='''body{margin:0;background:#fbfaf7;color:#25221e;font-family:system-ui,-apple-system,Segoe UI,sans-serif;line-height:1.75}header{max-width:73rem;margin:auto;padding:2.5rem 2rem 1rem}h1,h2{line-height:1.25}main{max-width:73rem;margin:auto;display:grid;grid-template-columns:19rem minmax(0,47rem);gap:3rem;padding:1rem 2rem 5rem}nav{position:sticky;top:1rem;height:94vh;overflow:auto;padding-right:1rem;font-size:.85rem}nav a{display:block;margin:.7rem 0;color:inherit;text-decoration:none}.extra{padding-left:1rem;color:#706456}article{min-width:0}p{font-size:1.08rem;margin:1.05rem 0}section{padding:1rem 0 3rem;border-bottom:1px solid #ded8cf}.eyebrow{display:block;font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:#766b60}details{margin:1.4rem 0 2rem;padding:1.2rem 1.5rem;background:#f1ede6;border:1px solid #d7cfc2;border-radius:.35rem}summary{cursor:pointer;font-weight:600;line-height:1.5}summary span:last-child{display:block;font-size:1.15rem}.route{border-bottom:1px solid #d7cfc2;margin-bottom:1.5rem;padding-bottom:.5rem}.route p{font-size:.95rem}.back{color:inherit;font-size:.85rem}header p{max-width:56rem;font-size:1rem}@media(max-width:850px){main{display:block;padding:1rem 1.2rem}nav{position:static;height:auto;max-height:24rem;border:1px solid #ded8cf;padding:1rem;margin-bottom:2rem}header{padding:1.5rem 1.2rem}h2{font-size:1.45rem}details{padding:1rem}}@media print{nav,.back{display:none}main{display:block;padding:0}details{background:none;border:0}section{break-before:page}p{font-size:11pt}}'''
    js='''function openTarget(){const id=decodeURIComponent(location.hash.slice(1));const e=document.getElementById(id);if(e&&e.tagName==='DETAILS'){e.open=true;e.scrollIntoView();}}window.addEventListener('hashchange',openTarget);window.addEventListener('DOMContentLoaded',openTarget);window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(e=>e.open=true));'''
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orange Plan — course reading copy</title><style>'+css+'</style></head><body><header id="top"><p class="eyebrow">Orange Plan Academy</p><h1>Build your plan, one decision at a time</h1><p>Follow the main lessons in order. Open a <strong>For your situation</strong> lesson when its condition applies, complete it before relying on that strategy, then return to the indicated walkthrough. This copy contains spoken text; production notes remain in GitHub. Owner voice review and actual recordings are still separate.</p></header><main><nav>'+''.join(nav)+'</nav><article>'+''.join(body)+'</article></main><script>'+js+'</script></body></html>'
    (out/'Orange_Plan_Course_Reading_Copy.html').write_text(page,encoding='utf-8')
    for name in ['ALL-SCRIPTS.md','DICTATION-ORDER.md','ADVANCED-DICTATION-ORDER.md','FILM-ORDER.md','FINALIZATION-STATUS.md']:(out/name).write_bytes((ROOT/name).read_bytes())
    (out/'Walkthroughs').mkdir(exist_ok=True)
    for r in rows:
        if r['id'] in tool['PRACTICAL_IDS']:(out/'Walkthroughs'/Path(r['path']).name).write_bytes((ROOT/r['path']).read_bytes())
    (out/'BUILD-IDENTITY.json').write_text(json.dumps({'commit':git('rev-parse','HEAD').strip(),'tree':git('rev-parse','HEAD^{tree}').strip(),'teaching_lessons':len(order),'conditional_including_college':len(tool['ADV_IDS'])+1,'notice':'Source-matched reading copy. A later cleanup-only commit removes staging files without changing these contents.'},indent=2)+'\n')
    # Artifacts include exact authoring inputs for local diff/selector review, not another repo master.
    proof=out/'review-evidence';proof.mkdir(exist_ok=True)
    (proof/'edit-log.txt').write_text('Canonical source: '+BASE+'; unchanged arithmetic, fixture, Reserve, W02, D07 and original sources verified by the run. No automated test certifies voice or learner success.\n')
    print('Reader: 65 lesson targets, 50 main sections and 15 conditional cards; no external assets or font files.')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('command',choices=['apply','reader']);ap.add_argument('--out',type=Path,default=Path('/tmp/orange-plan-member-reading'));args=ap.parse_args()
    if args.command=='apply':apply()
    else:reader(args.out)
