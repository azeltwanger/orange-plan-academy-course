#!/usr/bin/env python3
"""Apply the literal recording copyedit and export plain narration. Temporary helper."""
from pathlib import Path
from decimal import Decimal as D
import argparse, hashlib, html, json, re, runpy, shutil, subprocess
BASE='c4c55601dfdaa893343623a75f478cbbfef120ad'
MANIFEST_BLOB='d7e2a2d8f470ed00bfaf14b48d5055157b55e750'
PATCH_HASH='d2b56b20a45cf59268e8cbdb79c6e5ee78289b6581ce5847b49dbe5935a5a10e'
RESERVE_BLOB='2c107a394a93cc877c73f011dfe37fb5ad3d94b1'

def sha(b): return hashlib.sha256(b).hexdigest()
def git(root,*args): return subprocess.check_output(['git',*args],cwd=root).decode().strip()
def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def match(t):
    m=re.search(r'^### Read aloud\s*\n(.*?)(?=^### |\Z)',t,re.M|re.S)
    if not m: raise ValueError('Missing spoken section')
    return m

def once(t,a,b):
    if t.count(a)!=1: raise ValueError('Source mismatch: '+a[:80])
    return t.replace(a,b,1)

def apply(root):
    mp=root/'COURSE-MANIFEST.json'; assert blob(mp.read_bytes())==MANIFEST_BLOB
    manifest=json.loads(mp.read_text()); by={x['id']:x for x in manifest['lessons']}
    edits=runpy.run_path(str(root/'tools/_recording_edits.py'))['EDITS']
    assert sha(json.dumps(edits,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())==PATCH_HASH
    assert len(edits)==59 and sum(len(v) for v in edits.values())==162
    assert len(by)==76 and len(manifest['member_order'])==65
    assert not set(edits)&{'2.3','W02','D07'}
    originals={}
    for lid,row in by.items():
        p=root/row['path']; originals[lid]=p.read_bytes()
        assert sha(originals[lid])==row['source_sha256'],lid
        assert subprocess.check_output(['git','show',BASE+':'+row['path']],cwd=root)==originals[lid],lid
    report=[]
    for lid,changes in edits.items():
        row=by[lid]; p=root/row['path']; text=originals[lid].decode(); m=match(text)
        prior=m.group(1).strip(); paragraphs=prior.split('\n\n')
        assert min(changes)>=0 and max(changes)<len(paragraphs)
        for n,new in changes.items(): assert paragraphs[n]!=new,(lid,n)
        current='\n\n'.join(changes.get(n,s) for n,s in enumerate(paragraphs) if changes.get(n,s).strip())
        revised=text[:m.start(1)]+'\n'+current+'\n\n'+text[m.end(1):]
        p.write_text(revised,encoding='utf-8')
        after=match(revised)
        assert text[:m.start(1)]==revised[:after.start(1)]
        assert text[m.end(1):]==revised[after.end(1):]
        report.append((lid,len(changes),len(prior.split()),len(current.split())))
    for lid in set(by)-set(edits): assert (root/by[lid]['path']).read_bytes()==originals[lid],lid
    assert blob((root/by['2.3']['path']).read_bytes())==RESERVE_BLOB
    # Show the missing arithmetic operations without changing existing assumptions/endpoints.
    assert D(25000)/D('.8')==D(31250)
    assert (D(100000)-D(31250))/100000==D('.6875')
    assert (D(1000000)-50000)*D('.8')==760000
    assert (D(760000)-50000)*D('1.25')==887500
    assert D(950000)*D('1.25')==1187500
    assert (D(1187500)-50000)*D('.8')==910000
    assert D(10000)/100000+D(10000)/50000==D('.3')
    assert D(10000)/100000+D(10000)/200000==D('.15')
    dependency=re.compile(r'\b(slides?|deck|on (?:the )?screen|on the left|on the right|source\x27s|source example|fixture|receipt of the inputs|closing presentation|final presentation|near-term column|original example range)\b',re.I)
    for lid in manifest['member_order']:
        spoken=match((root/by[lid]['path']).read_text()).group(1).strip()
        assert not dependency.search(spoken),lid
    p=root/'README.md';t=p.read_text()
    prior=next(x for x in t.split('\n\n') if x.startswith('**Allocation filming package'))
    intro='**Recording scripts first — September 9, 2026:** Open the clean scripts in [reading order](DICTATION-ORDER.md) or [all spoken text](ALL-SCRIPTS.md). Record the teaching first; add text and graphics during editing. The current pass makes examples understandable without slides and tightens selected narration across the course. App walkthroughs remain separate recordings. No slide presentation, homework, quiz, submission or new workbook is required. [Recording-pass scope](delivery/recording-script-pass.md).'
    p.write_text(once(t,prior,intro))
    p=root/'HANDOFF.md';t=p.read_text()
    t=once(t,'# Current handoff — member path and spoken-language cleanup','# Current handoff — record the scripts, then edit the video')
    note='''## Current production direction — scripts first

Austin records the spoken lessons first. Text, graphics and supporting footage are added afterward to match the recorded explanation. There is no slide-design, slide-approval or presentation rehearsal prerequisite. The Allocation slide package is historical reference only; its old paragraph map no longer defines current narration.

This recording copyedit reviews the existing 65-lesson manuscript and changes 162 selected paragraphs across 59 lessons. Six lessons are retained, including accepted Reserve 2.3. Every practical file remains byte-identical and is recorded separately when its actual app/device prerequisites are met. No new curriculum, exercise, financial rule or desired model outcome is introduced. Source notes, technical checks and conditional app inserts stay outside clean spoken copies.

The clean delivery contains one plain-text file per teaching lesson and a combined reading copy. It does not ask Austin to design visuals before recording. The existing app-dependent qualifications, especially 0.2 and 6.8, still need their actual product wording checked. A copyedit is not an actual read-through by Austin, a participant test, licensed sign-off or recorded app result.

See [recording-pass scope](delivery/recording-script-pass.md). Continue by recording a script or correcting a specific line; do not restart deck production or add member assignments.

'''
    t=once(t,'## Current continuation — the member\'s own plan is the application',note+'## Prior correction still in force — the member\'s own plan is the application')
    p.write_text(t)
    p=root/'FINALIZATION-STATUS.md';t=p.read_text();first=t.split('\n',1)[0]
    t=once(t,first,'# Course status — scripts first, app capture separate')
    note='**Recording pass — September 9, 2026:** The clean spoken scripts are the recording deliverable. 162 targeted paragraph edits across 59 lessons remove slide-dependent narration, clarify spoken calculations and tighten repeated or awkward explanations; six lessons are retained. Record the teaching first, then add text and graphics in the edit. No slide approval or homework is required. All 11 practical files, actual capture holds, the accepted Reserve and prior technical-review records remain unchanged. This is not a claim Austin has read or approved every line.\n\n'
    t=t.split('\n\n',1)[0]+'\n\n'+note+t.split('\n\n',1)[1];p.write_text(t)
    p=root/'AUSTIN-AUTHORITY.md';t=p.read_text();first,rest=t.split('\n\n',1)
    p.write_text(first+'\n\n**Production order:** scripts → Austin records the video → text, graphics and supporting footage are added in editing. No slide deck is a recording prerequisite. Teaching must make sense when spoken without pointing to an unseen slide. App walkthroughs are separate recordings. Members apply the lesson in their own Orange Plan; no homework, quizzes, submitted explanations or new workbooks. Existing real-world custody, legal and provider steps still apply where necessary.\n\n'+rest)
    for name in ['README.md','slide-map.md']:
        p=root/'delivery/allocation-filming'/name;t=p.read_text();first,rest=t.split('\n',1)
        p.write_text(first+'\n\n> Historical reference only. Austin has replaced the slide-first workflow with recording the scripts first and adding graphics during editing. This package and paragraph map belong to the earlier pinned source, not the current narration. Use `scripts/` and the current clean reading copies; no slide rehearsal or approval is required.\n'+rest)
    p=root/'delivery/recording-script-pass.md';p.parent.mkdir(exist_ok=True)
    summary='''# Recording-script pass — September 9, 2026

## Actual deliverable

A clean spoken script for each of the existing 65 teaching lessons. Austin records those videos first; text, graphics and supporting footage are added during editing. App walkthroughs remain separate. No deck, visual approval, quiz, homework, required post, submitted explanation or new workbook is introduced.

This is an individually authored copyedit of the existing manuscript, not a new course or a fixed-length rewrite: 162 selected paragraph changes across 59 lessons. All six other teaching lessons and all 11 practical files remain byte-identical. The accepted Reserve remains the reference at Git blob `2c107a394a93cc877c73f011dfe37fb5ad3d94b1`.

## What changed

- References to slides, deck order and unseen columns are replaced with spoken explanations. The four Bitcoin paths retain their names, ranges and qualifications; the narration explains them directly.
- Existing arithmetic examples now speak the omitted steps where useful: the lower-LTV example, fractional Bitcoin purchase costs, the reversed two-year withdrawal sequence and staged purchases. No result or assumption is changed to improve a retirement outcome.
- Dense blocks are paced in the narration, including cash choices and healthcare cost definitions. Factual distinctions remain.
- Selected openings and endings are more direct. Repeated insurance setup, writer-facing result-identity language and references to a final presentation are removed. App actions remain real decisions in the member's own plan, not written assignments.
- The earlier Allocation slide package remains recoverable as reference, but is no longer promoted as a required production stage. Its paragraph map is not claimed to match the new wording.

## Source and verification boundary

Base: `c4c55601dfdaa893343623a75f478cbbfef120ad`. The mounted no-homework package was verified against current COURSE-MANIFEST blob `d7e2a2d8f470ed00bfaf14b48d5055157b55e750`; each of the 76 canonical files matched its source hash. The retirement YouTube text is a voice/progression reference only; none of its return, withdrawal, price, account-access or tax assumptions is imported.

Edits are restricted to the Read aloud section of the identified lessons. All nonspoken lesson sections, qualification notes, technical checks, situational routing, source materials, fixed household, toolkit, practical plans, generator/test code and existing capture receipts are preserved. No new current-law or product research conclusion is claimed in this editorial pass. Existing specific tax, access, lending, healthcare, security and legal qualifications remain; they have not been replaced with a blanket referral.

The additional spoken arithmetic uses the existing examples: $25,000/0.8=$31,250 and a 68.75% decline from $100,000; $950,000×1.25=$1,187,500, less $50,000=$1,137,500, then ×0.8=$910,000; staged $10,000 purchases at the existing hypothetical prices still total 0.3 or 0.15 BTC. These operations are recomputed alongside the unchanged course checks. They are not a new household dataset or a modeled app result.

The review is a written editorial pass, not an actual recording, blind learner study, measured reading grade or independent professional approval. App-dependent wording and procedures still need the actual product. In particular, 0.2, 6.8 and the W/D captures retain their existing conditions. Do not pretend a design, script or generated file proves an app result, wallet test, provider operation or delivered family message.

The PR records exact run and merge evidence after it exists. No app repository, hosted data, provider account, wallet, commercial term, course-platform access, Production deployment or student release is changed.

## Edited lessons

'''
    summary+=' | '.join(x[0] for x in report)+'\n\nRetained teaching: '+', '.join(x for x in manifest['member_order'] if x not in edits)+'.\n'
    p.write_text(summary,encoding='utf-8')
    print('Applied 162 selected paragraph edits in 59 lessons; six lessons and all 11 practical files preserved. Additional arithmetic passed.')

def export(root,out):
    out.mkdir(parents=True,exist_ok=True)
    package=out/'Orange_Plan_Recording_Scripts';package.mkdir(exist_ok=True)
    for name in ['Teaching','App_Walkthroughs','Device_Demonstration']:(package/name).mkdir(exist_ok=True)
    m=json.loads((root/'COURSE-MANIFEST.json').read_text());by={x['id']:x for x in m['lessons']}
    sections=[];options=[];combined=[];source=[]
    for n,lid in enumerate(m['member_order'],1):
        row=by[lid];b=(root/row['path']).read_bytes();assert sha(b)==row['source_sha256']
        spoken=match(b.decode()).group(1).strip();assert sha(spoken.encode())==row['spoken_sha256']
        file=f'Teaching/{n:02d}_{lid.replace(".","-")}.txt';(package/file).write_text(spoken+'\n',encoding='utf-8')
        title=lid+' — '+row['title'];conditional=lid.startswith('A') or lid=='2.5'
        label=('For your situation · ' if conditional else '')+title
        options.append('<option value="'+str(n-1)+'">'+html.escape(label)+'</option>')
        body=''.join('<p>'+html.escape(v).replace('\n','<br>')+'</p>' for v in spoken.split('\n\n'))
        sections.append('<section data-index="'+str(n-1)+'"'+(' hidden' if n>1 else '')+'><h1>'+html.escape(title)+'</h1><div class="spoken">'+body+'</div></section>')
        combined.append('# '+title+'\n\n'+spoken+'\n')
        source.append({'id':lid,'path':row['path'],'file':file,'source_sha256':row['source_sha256'],'spoken_sha256':row['spoken_sha256']})
    (package/'All_Recording_Scripts.md').write_text('\n\n---\n\n'.join(combined)+'\n',encoding='utf-8')
    css='''*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;background:#faf9f6;color:#24211d}header{position:sticky;top:0;background:#faf9f6;border-bottom:1px solid #dedbd5;padding:14px max(16px,calc((100% - 850px)/2));z-index:2}header label{display:block;font-size:12px;margin-bottom:7px;color:#635e57}select{width:100%;padding:9px;border:1px solid #cbc6bd;border-radius:4px;background:white;font:inherit;font-size:14px}.controls{display:flex;align-items:center;gap:8px;margin-top:10px;flex-wrap:wrap}button{font:inherit;font-size:14px;cursor:pointer;padding:6px 12px;border:1px solid #cbc6bd;border-radius:4px;background:white}button:disabled{opacity:.4;cursor:default}#position{font-size:12px;color:#635e57;margin-left:auto}main{max-width:850px;padding:28px 20px 100px;margin:auto}h1{font-size:24px;line-height:1.35;margin:6px 0 30px}.spoken{font-size:var(--size,24px);line-height:1.8}.spoken p{margin:0 0 1.1em}[hidden]{display:none!important}body.focus header{display:none}body.focus main{padding-top:20px}#restore{display:none;position:fixed;right:10px;top:10px;opacity:.7}body.focus #restore{display:block}@media(max-width:600px){.spoken{font-size:var(--size,22px)}h1{font-size:21px}header{padding:12px}main{padding:22px 16px 80px}}@media print{header,#restore{display:none}main{max-width:none;padding:0}.spoken{font-size:12pt;line-height:1.6}h1{font-size:18pt}}'''
    js='''const sel=document.getElementById('lesson'),sections=[...document.querySelectorAll('main section')];let current=0,size=24;function show(n){current=Math.max(0,Math.min(sections.length-1,n));sections.forEach((s,i)=>s.hidden=i!==current);sel.value=String(current);document.getElementById('position').textContent=(current+1)+' / '+sections.length;document.getElementById('prev').disabled=current===0;document.getElementById('next').disabled=current===sections.length-1;window.scrollTo(0,0)}sel.addEventListener('change',()=>show(Number(sel.value)));document.getElementById('prev').onclick=()=>show(current-1);document.getElementById('next').onclick=()=>show(current+1);document.getElementById('smaller').onclick=()=>{size=Math.max(16,size-2);document.documentElement.style.setProperty('--size',size+'px')};document.getElementById('larger').onclick=()=>{size=Math.min(44,size+2);document.documentElement.style.setProperty('--size',size+'px')};document.getElementById('focus').onclick=()=>document.body.classList.add('focus');document.getElementById('restore').onclick=()=>document.body.classList.remove('focus');document.addEventListener('keydown',e=>{if(e.key==='Escape')document.body.classList.remove('focus');if(['SELECT','INPUT','TEXTAREA'].includes(document.activeElement.tagName))return;if(e.key==='ArrowRight'){e.preventDefault();show(current+1)}if(e.key==='ArrowLeft'){e.preventDefault();show(current-1)}});show(0);'''
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orange Plan — recording scripts</title><style>'+css+'</style></head><body><header><label for="lesson">ORANGE PLAN · RECORDING SCRIPTS</label><select id="lesson">'+''.join(options)+'</select><div class="controls"><button id="prev">Previous</button><button id="next">Next</button><button id="smaller" aria-label="Smaller text">A−</button><button id="larger" aria-label="Larger text">A+</button><button id="focus">Script only</button><span id="position"></span></div></header><button id="restore">Show controls · Esc</button><main>'+''.join(sections)+'</main><script>'+js+'</script></body></html>'
    (package/'Recording_Scripts.html').write_text(page,encoding='utf-8')
    for row in m['lessons']:
        if not row['id'].startswith(('W','D')):continue
        dest='Device_Demonstration' if row['id'].startswith('D') else 'App_Walkthroughs'
        shutil.copy2(root/row['path'],package/dest/Path(row['path']).name)
    guide='''ORANGE PLAN — RECORDING SCRIPTS

Record the spoken teaching first. Add text, graphics and supporting footage during editing.

Open Recording_Scripts.html and choose a lesson, or use its plain-text file in Teaching/. These 65 text files contain narration only. All_Recording_Scripts.md combines them in the existing member learning order. A-prefixed lessons and college are situational, not another difficulty level.

App_Walkthroughs/ and Device_Demonstration/ contain the existing separate recording plans. They include production checks and are not teleprompter copy. Record them only when the relevant app or safe device procedure is verified. App-linked wording, especially Ask (0.2) and annual spending review (6.8), retains its existing product verification requirements.

There is no homework or presentation requirement. Members apply the teaching to their own plan in Orange Plan. Family, security, legal and provider actions still have their real-world purpose; entering a plan does not execute them.

The accepted Reserve script is unchanged. Source notes and technical review records remain in GitHub, outside the spoken copy. This pass has not been read aloud or approved by Austin; no actual learner test or recorded app result is claimed. The earlier slide package is not required and its narration map is superseded.
'''
    (package/'START_HERE.txt').write_text(guide)
    identity={'commit':git(root,'rev-parse','HEAD'),'tree':git(root,'rev-parse','HEAD^{tree}'),'source':'scripts/','teaching':source,'notice':'Recording copy only; not approval, learner evidence or app capture.'}
    (package/'SOURCE-IDENTITY.json').write_text(json.dumps(identity,indent=2)+'\n')
    # Separate evidence is not included in the owner-facing final ZIP.
    qa=out/'_verification';qa.mkdir(exist_ok=True)
    for p in (root/'scripts').rglob('*.md'):
        q=qa/p.relative_to(root);q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(p.read_bytes())
    for name in ['COURSE-MANIFEST.json','delivery/recording-script-pass.md']:
        q=qa/name;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((root/name).read_bytes())
    print('Exported 65 narration-only text files, clean reader, combined text and separate unchanged walkthroughs; no slides or external assets.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['apply','export']);p.add_argument('--root',type=Path,required=True);p.add_argument('--out',type=Path,default=Path('/tmp/recording-export'));a=p.parse_args()
    apply(a.root) if a.command=='apply' else export(a.root,a.out)
