#!/usr/bin/env python3
"""Build the guided Academy from canonical scripts. Standard library only.

history: verify retired files against the pinned Git history (full checkout required).
build: derive reading copies, orders and manifests from scripts (never reverse).
check: check structure, arithmetic, links and byte-for-byte derived-file parity.
test: prove missing lessons, stale copies and fixture changes are rejected.
No network, app, credential, financial-account, or deployment operations.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, tempfile, subprocess, posixpath
from pathlib import Path
from decimal import Decimal as D
from filming_pack import revision as filming_revision, outputs as filming_outputs, chapters as filming_chapters

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b'
APP_SHA = '21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2'
# Owner-approved 25 main / 8 situation-specific recordings; stable source IDs.
CORE_IDS = ['0.1', '1.2', '1.4', '1.5', '2.1', '2.3', '2.4', '3.1', '3.4', '3.6', '4.3', '4.5', '4.7', '5.1', '5.4', '6.1', '6.3', '6.6', '6.8', '7.1', '7.2', '8.1', '8.4', '9.1', '10.1']
ADV_IDS = ['2.5', 'A3.1', 'A3.2', 'A5.1', 'A5.2', 'A6.3', 'A7.1', 'A8.1']
PRACTICAL_IDS = ['W01','W02','W03','W04','W05','W06','W07','D07','W08','W09','W10']
ALL_IDS = CORE_IDS + ADV_IDS + PRACTICAL_IDS
NAMES = ['Start here','First working plan','Cash flow, reserve and life events','Debt and leverage','Allocation and the next dollar','Tax strategy','Retirement paycheck','Custody','Family handoff','Maintenance','Read and share your plan']
CHAPTERS = {'0.1': 'Orientation; begin your own plan', '1.2': 'W01 chapters 1–7', '1.4': 'W01 chapter 8', '1.5': 'W01 chapters 9–10, including Ask when available', '2.1': 'W02 chapters 1–3', '2.3': 'W02 chapters 4–5', '2.4': 'W02 chapter 6', '3.1': 'W03 chapters 1 and 3', '3.4': 'W03 chapter 4', '3.6': 'W03 chapters 2 and 5–6', '4.3': 'W04 chapters 1–3', '4.5': 'W04 chapters 5–6', '4.7': 'W04 chapters 4 and 7–8', '5.1': 'W05 chapter 1; chapter 2 only when records need repair', '5.4': 'W05 chapters 3–4; chapters 5–6 for a relevant transaction', '6.1': 'W06 chapters 1–2 and 4', '6.3': 'W06 chapter 3', '6.6': 'W06 chapter 6', '6.8': 'W06 chapters 5 and 7–8', '7.1': 'W07 chapter 1', '7.2': 'W07 chapters 2–3 and D07 only for the applicable safe setup', '8.1': 'W07 chapter 4 and W08 chapters 1–4', '8.4': 'W08 chapter 5', '9.1': 'W09 chapters 1–5', '10.1': 'W10 chapters 1–5'}
CONSOLIDATION_PIN = 'c4c55601dfdaa893343623a75f478cbbfef120ad'
CHAPTERS.update({
    '0.1': 'Choose age and spending now; enter them in W01 chapter 7 after the starting facts',
    '1.2': 'W01 chapters 1–7; chapter 5 is conditional history/transfer work',
    '2.5': 'W02 chapter 7',
    'A3.1': 'W03 chapter 5; chapters 4 and 6 supply financing and cash-flow context',
    'A3.2': 'W03 chapters 4–5',
    'A5.1': 'W05 chapter 4; chapter 6 for the professional handoff',
    'A5.2': 'W05 chapters 2 and 5–6; chapter 1 for the gain comparison',
    'A6.3': 'W06 chapter 2',
    'A7.1': 'W07 chapter 1; D07 only for its separately reviewed isolated setup',
    'A8.1': 'W08 chapters 1–2',
})
CONSOLIDATION_MAPPING_DIGEST = '1a61726e67a15447c50eebe218b10177c23136a66efdb03c8dd7b0693ea2240d'

# Only these owner-authorized wording changes may differ from the accepted Reserve.
RESERVE_LANGUAGE_EDITS = [
    ['An investment you cannot readily use', "An investment you can't readily use", 1],
    ['We cannot assign the same monthly surplus to both.', "We can't assign the same monthly surplus to both.", 1],
    ['genuinely available', 'actually available', 1],
    ["Three, six, and twelve months or more are starting points for comparison. They aren't automatic answers.",
     'Three, six, or twelve months or more are starting points. None of them is the automatic answer.', 1],
    ['They are also working on expensive debt.', "They're also working on expensive debt.", 1],
]

def accepted_reserve_bytes(data: bytes) -> bytes:
    text = data.decode('utf-8')
    for old, new, count in reversed(RESERVE_LANGUAGE_EDITS):
        if text.count(new) != count:
            raise ValueError('Reserve language edit does not match its approved scope')
        text = text.replace(new, old)
    return text.encode('utf-8')

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write(root: Path, path: str, content: str) -> None:
    p = root/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content.rstrip()+'\n',encoding='utf-8',newline='\n')

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def section(text: str, heading: str) -> str:
    m=re.search(r'^### '+re.escape(heading)+r'\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S)
    return m.group(1).strip() if m else ''

def blocks(text: str):
    return re.findall(r'^## ((?:A?\d+\.\d+|[WD]\d+) — [^\n]+)\n(.*?)(?=^## (?:A?\d+\.\d+|[WD]\d+) — |\Z)',text,re.M|re.S)

def script_path(lid: str, title: str) -> str:
    slug = re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
    if lid.startswith('A'): return f'scripts/advanced/{lid.replace(".","-")}_{slug}.md'
    if lid.startswith(('W','D')): return f'scripts/working/{lid}_{slug}.md'
    m,n=lid.split('.'); return f'scripts/{int(m):02d}-{n}_{slug}.md'

def catalog(root: Path) -> list[dict]:
    records={}
    for p in sorted((root/'scripts').rglob('*.md')):
        text=p.read_text(encoding='utf-8')
        match=re.match(r'# ((?:A?\d+\.\d+|[WD]\d+)) — ([^\n]+)',text)
        if not match: raise ValueError('Unrecognized active script: '+str(p))
        lid,title=match.groups()
        if lid in records: raise ValueError('Duplicate lesson '+lid)
        read=section(text,'Read aloud'); checkpoint=section(text,'Member checkpoint') or section(text,'Readback and finish') or section(text,'Readback and finish — not spoken')
        if not checkpoint: raise ValueError('Missing completion check '+lid)
        if lid not in PRACTICAL_IDS and len(read.split())<50: raise ValueError('Empty or placeholder narration '+lid)
        gate=re.search(r'^Gate: (.+)$',text,re.M)
        sources=re.search(r'^Sources: (.+)$',text,re.M)
        if not gate or not sources: raise ValueError('Missing gate/source '+lid)
        if re.search(r'\b(?:TODO|TBD|INSERT SCRIPT)\b',read): raise ValueError('Unfinished spoken placeholder '+lid)
        if re.search(r'canonical owner|hold that screen capture|the demonstration is gated|We are not using a personal family story',read,re.I): raise ValueError('Production language in narration '+lid)
        records[lid]={'id':lid,'title':title,'path':p.relative_to(root).as_posix(),'gate':gate.group(1),'sources':sources.group(1),'words':len(read.split()),'spoken_sha256':digest(read.encode()),'source_sha256':digest(p.read_bytes()),'read':read,'text':text,'checkpoint':checkpoint}
    if set(records)!=set(ALL_IDS): raise ValueError('Lesson set differs: '+str(set(records)^set(ALL_IDS)))
    return [records[x] for x in ALL_IDS]

MERGED_LESSON = {
    'id':'A7.2',
    'path':'scripts/advanced/A7-2_decide-which-custody-responsibilities-the-household-can-maintain.md',
    'source_commit':'f6392a6341c23c557e605506dab3530b67efa146',
    'blob':'0443c4640a4f4b431429eab204f5fe9dc0b67413',
    'original_destinations':['7.1','7.4','W07'],
    'destinations':['7.1','8.1','W07'],
}

def situation_route(row: dict) -> dict:
    values={}
    for key,heading in [('after','After lesson'),('when','Use when'),('before','Complete before'),('return','Return to')]:
        found=re.findall(r'^'+re.escape(heading)+r': (.+)$',row['text'],re.M)
        if len(found)!=1 or not found[0].strip():
            raise ValueError('Missing or duplicate situation route '+row['id']+': '+heading)
        values[key]=found[0].strip()
    if values['after'] not in CORE_IDS:
        raise ValueError('Invalid parent lesson '+row['id'])
    if not re.search(r'^Kind: conditional$',row['text'],re.M):
        raise ValueError('Situational lesson is not marked conditional '+row['id'])
    return values

def member_order(rows: list[dict]) -> list[str]:
    by={r['id']:r for r in rows}; ordered=[]
    routes={lid:situation_route(by[lid]) for lid in ADV_IDS}
    for lid in CORE_IDS:
        ordered.append(lid)
        ordered.extend(x for x in ADV_IDS if routes[x]['after']==lid)
    if len(ordered)!=len(CORE_IDS)+len(ADV_IDS) or set(ordered)!=set(CORE_IDS+ADV_IDS):
        raise ValueError('Member sequence duplicates or omits a lesson')
    return ordered

def read_link(row: dict) -> str:
    group='advanced' if row['id'] in ADV_IDS else 'core'
    return f"teleprompter/{group}/{row['id'].replace('.','-')}.txt"

def situation_card(row: dict) -> str:
    r=situation_route(row)
    return (f"> **For your situation — [{row['title']}]({read_link(row)})**\n>\n"
            f"> {r['when']}\n>\n> {r['before']}\n>\n> **Return to:** {r['return']}.\n\n")

def review_state(row: dict) -> str:
    if section(row['text'], 'Do this'):return 'Step-by-step manuscript and overlays prepared'
    if row['id'] in PRACTICAL_IDS:return 'Separate walkthrough manuscript; capture pending'
    if 'Status: RECORDING_DRAFT_REVIEW' in row['text']:return 'Consolidated recording draft; owner review pending'
    if 'Status: SPOKEN_EDIT_REVIEW' in row['text']:return 'Spoken-language edit; owner review pending'
    if 'Status: TEACHING_RETAINED_REVIEW' in row['text']:return 'Existing explanation retained; owner review pending'
    if 'Status: WALKTHROUGH_REWRITE_REVIEW' in row['text']:return 'Prepared narration; review and capture pending'
    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:return 'Written draft; owner review pending'
    return 'Review status requires attention'

def consolidation(root: Path) -> dict:
    c=load_json(root/'production/consolidation.json')
    if c['base_commit']!=CONSOLIDATION_PIN or c['main_ids']!=CORE_IDS or c['situation_ids']!=ADV_IDS:
        raise ValueError('Consolidation identity or counts changed')
    mapping=c['mapping']
    if len(mapping)!=65 or len({x['old_id'] for x in mapping})!=65:
        raise ValueError('Consolidation loses an original lesson')
    if digest(json.dumps(mapping,sort_keys=True,separators=(',',':')).encode())!=CONSOLIDATION_MAPPING_DIGEST:
        raise ValueError('Source/destination mapping changed without review')
    refs=set(c['reference_files'].values())
    for row in mapping:
        if not row['destinations'] or not set(row['destinations']).issubset(set(CORE_IDS+ADV_IDS)|refs):
            raise ValueError('Unmapped teaching '+row['old_id'])
        if row['retired_active_file'] and (root/row['old_path']).exists():
            raise ValueError('Retired source restored as active script '+row['old_path'])
    revision=filming_revision(root)
    originals={r['path']:r['archive'] for r in revision['preserved_originals']}
    for path,h in c['protected'].items():
        data=(root/originals[path]).read_bytes()
        if path=='scripts/02-3_size-the-reserve-for-the-job-it-has-to-do.md':
            data=accepted_reserve_bytes(data)
        if digest(data)!=h:raise ValueError('Protected original Reserve/capture changed '+path)
    for path in refs:
        if not (root/path).is_file():raise ValueError('Missing retained task reference '+path)
    return c

def render_links(text: str, source: str, target: str) -> str:
    """Keep relative source-note links valid in masters and section views."""
    def relocate(match):
        link=match.group(1)
        if '://' in link or link.startswith(('#','mailto:')): return match.group(0)
        path,sep,anchor=link.partition('#')
        destination=posixpath.normpath(posixpath.join(posixpath.dirname(source),path))
        relative=posixpath.relpath(destination,posixpath.dirname(target) or '.')
        return ']('+relative+(sep+anchor if sep else '')+')'
    return re.sub(r'\]\(([^)]+)\)',relocate,text)

def outputs(root: Path) -> dict[str,str]:
    c=consolidation(root);rows=catalog(root);by={r['id']:r for r in rows};result={}
    routes={x:situation_route(by[x]) for x in ADV_IDS};order=member_order(rows)
    records=[]
    for r in rows:
        record={k:v for k,v in r.items() if k not in ('read','text','checkpoint')}
        if r['id'] in PRACTICAL_IDS:
            scenes=filming_chapters(r['text'])
            record['words']=sum(len(s['Narration'].split()) for s in scenes)
            record['spoken_sha256']=digest('\n\n'.join(s['Narration'] for s in scenes).encode())
            record['chapter_takes']=[f"{r['id']}-{s['number']:02d}" for s in scenes]
        if r['id'] in routes:record['member_route']=routes[r['id']]
        record['member_group']='For your situation' if r['id'] in ADV_IDS else 'Main path' if r['id'] in CORE_IDS else 'Separate capture'
        if r['id'] in CORE_IDS:record['recording_number']=CORE_IDS.index(r['id'])+1
        records.append(record)
    result['COURSE-MANIFEST.json']=json.dumps({'canonical':'scripts/','source_commit':SOURCE_SHA,'consolidation_base_commit':CONSOLIDATION_PIN,'app_contract_commit':APP_SHA,
        'counts':{'core':25,'advanced':8,'working_sessions':10,'device_demos':1},
        'member_labels':{'core':'Main path','advanced':'For your situation'},'member_order':order,
        'merged_lessons':[MERGED_LESSON],'consolidation_record':'production/consolidation.json','lessons':records},indent=2,ensure_ascii=False)
    intro='Generated from `scripts/`. Each lesson states the task, explains the decision, and hands off to a separate walkthrough. Only Read aloud is teaching speech; overlays and production notes are not spoken. The slide steps supply the sequence.\n\n'
    result['MASTER-COURSE.md']='# Main course — 25 recording scripts and source notes\n\n'+intro+'\n\n---\n\n'.join(render_links(by[x]['text'].strip(),by[x]['path'],'MASTER-COURSE.md') for x in CORE_IDS)
    result['MASTER-ADVANCED.md']='# For your situation — eight focused recordings\n\n'+intro+'Use only the lesson relevant to your decision, before depending on that strategy. This is not a second course.\n\n'+'\n\n---\n\n'.join(render_links(by[x]['text'].strip(),by[x]['path'],'MASTER-ADVANCED.md') for x in ADV_IDS)
    spoken='# Recording scripts — one main path\n\n25 main scripts, with eight For your situation scripts routed beside the relevant decision. Titles and navigation are not spoken. Individual teleprompter files contain only narration.\n\n'
    for x in order:
        r=by[x]; label=f"{CORE_IDS.index(x)+1:02d}" if x in CORE_IDS else 'For your situation'
        if x in routes:
            rr=routes[x];spoken+=f"*{rr['when']} {rr['before']} Return to {rr['return']}.*\n\n"
        spoken+=f"## {label} — {r['title']}\n\n{r['read']}\n\n---\n\n"
    result['ALL-SCRIPTS.md']=spoken
    for r in rows:
        result['lesson-text/'+r['path'].split('scripts/',1)[1]]=r['text']
        if r['read']:result[read_link(r)]=r['read']
    reading='# Recording order — 25 main lessons\n\nEach lesson gives the action and the judgment needed to complete it. Film teaching and its walkthrough separately. The eight For your situation lessons appear beside the decision they support. [Start filming](START-FILMING.md) · [Slide-step map](COURSE-STEP-MAP.md) · [Teaching overlays](TEACHING-OVERLAYS.md).\n\n'
    film='# Teaching and separate walkthrough pairing\n\nRecord the teaching from its clean teleprompter file; use the source script for overlay cues. Film each paired app chapter as a separate take once the future PR #227 workflow is verified. Keep both recordings together on the lesson page.\n\n[All walkthrough scripts](WALKTHROUGH-SCRIPTS.md) · [Capture dependencies](WALKTHROUGH-CAPTURE-DEPENDENCIES.md).\n\n'
    for m in range(11):
        selected=[x for x in CORE_IDS if x.startswith(str(m)+'.')]
        if not selected:continue
        reading+=f'## {NAMES[m]}\n\n';film+=f'## {NAMES[m]}\n\n'
        module=f'# {NAMES[m]}\n\n'+intro
        for x in selected:
            r=by[x];number=CORE_IDS.index(x)+1
            reading+=f"### {number:02d} — [{r['title']}]({r['path']})\n\n{section(r['text'],'Do this')}\n\n[Clean teaching teleprompter]({read_link(r)})\n\n**Separate walkthrough:** {CHAPTERS[x]}.\n\n"
            film+=f"### {number:02d} — [{r['title']}]({r['path']})\n\n**Separate app capture:** {CHAPTERS[x]}.\n\n"
            module+=render_links(r['text'],r['path'],f'modules/{m:02d}.md')+'\n\n---\n\n'
            for a in ADV_IDS:
                if routes[a]['after']==x:
                    card=situation_card(by[a])+f"**Separate walkthrough:** {CHAPTERS[a]}. [Script and overlay cues]({by[a]['path']}).\n\n"
                    reading+=card;film+=card;module+=render_links(by[a]['text'],by[a]['path'],f'modules/{m:02d}.md')+'\n\n---\n\n'
        result[f'modules/{m:02d}.md']=module
    reading+='## Recording and source notes\n\n[Situation-specific recordings](ADVANCED-DICTATION-ORDER.md) · [Walkthrough pairing](FILM-ORDER.md) · [Earlier consolidation](delivery/consolidation.md). Internal IDs are source references, not extra videos. [Austin’s current direction](reference/owner-stepwise-direction-20260910.md) governs this step-by-step revision.\n'
    result['DICTATION-ORDER.md']=reading
    extra='# For your situation — eight recordings\n\nUse the relevant instruction when your plan needs it. No separate course, homework or required reading for unrelated situations.\n\n'
    for x in ADV_IDS:
        r=by[x];rr=routes[x]
        extra+=f"## [{r['title']}]({r['path']})\n\n{rr['when']} {rr['before']}\n\n[Clean teaching teleprompter]({read_link(r)})\n\n**Separate walkthrough:** {CHAPTERS[x]}.\n\n**Return to:** {rr['return']}.\n\n"
    extra+='## Task references, not extra recording assignments\n\nExisting material on [custom assumptions](reference/custom-assumptions.md), [state moves](reference/state-move.md) and [Bitcoin output management](reference/bitcoin-output-management.md) is retained for those particular tasks. It is not part of the 33-video filming list or a requirement for every member.\n'
    result['ADVANCED-DICTATION-ORDER.md']=extra
    film+='## Working files\n\n'+''.join(f"- [{x} — {by[x]['title']}]({by[x]['path']})\n" for x in PRACTICAL_IDS)
    film+='\nW04 pairs chapters 1–3, then 5–6, then 4/7–8 with the teaching sequence. W06 pairs 1–2/4, then 3, then 6, then 5/7–8. The older accepted Reserve, W02 and D07 remain preserved as historical references. The active files implement Austin’s new step-by-step direction. No filming evidence is created by this edit.\n'
    result['FILM-ORDER.md']=film
    result['CIRCLE-STRUCTURE.md']=film.replace('# Teaching and separate walkthrough pairing','# Member playback — teaching followed by implementation',1)
    result['SCREEN-SHOOT-LIST.md']='# Separate app and device capture\n\nThe 33 teaching scripts are separate from these ten working sessions and one device demonstration. Use FILM-ORDER.md for the current grouping. Existing capture evidence is still required; no screen, result or operation is staged to match a script.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n[Run sheet]({by[x]['path']})\n\n{by[x]['checkpoint']}\n\n" for x in PRACTICAL_IDS)
    result['MODULE-CHECKPOINTS.md']='# Apply the teaching in your own Orange Plan\n\nThese are the actual planning actions, not homework, a quiz, a submission or another practice household. Keeping a current choice is valid when it fits.\n\n'+''.join(f"## {by[x]['title']}\n\n"+(f"For your situation: {routes[x]['when']}\n\n" if x in routes else '')+by[x]['checkpoint']+'\n\n' for x in order)
    result['PRODUCTION-CHECKLIST.md']='# Recording status\n\n25 main and eight situational teaching manuscripts with overlays, plus ten app walkthroughs and one device walkthrough. The editorial pass is separate from Austin’s read-through and actual capture evidence. Historical gate labels below identify the subject to verify, not additional generic approval requests. Use the specific [capture dependencies](WALKTHROUGH-CAPTURE-DEPENDENCIES.md) for app/device takes.\n\n| Recording | Script | Text status | Applicable review / capture subject |\n|---|---|---|---|\n'+''.join(f"| {CORE_IDS.index(r['id'])+1 if r['id'] in CORE_IDS else r['id']} | [{r['title']}]({r['path']}) | {review_state(r)} | {r['gate']} |\n" for r in rows)
    main=sum(by[x]['words'] for x in CORE_IDS);extra_words=sum(by[x]['words'] for x in ADV_IDS);before=c['baseline_words']['main'];before_all=sum(c['baseline_words'].values())
    result['COURSE-METRICS.md']=f'# Consolidated course\n\n25 main teaching scripts, eight For your situation scripts. Ten app working-session files and one device demonstration remain separate production work.\n\nMain narration: {main:,} words, compared with {before:,} in the prior owner-delivered 50-script main path: {(1-main/before)*100:.1f}% shorter. Situational narration: {extra_words:,} words. Total: {main+extra_words:,}, compared with {before_all:,} across the prior 65 scripts.\n\nAt an illustrative 140 words/minute, the main text is about {main/140:.0f} minutes; situational text adds about {extra_words/140:.0f} minutes if every extra were used. These are estimates from written words, not measured runtime, including no pauses or app footage. Do not publish a runtime promise before recording.\n\nThe earlier planning target was approximately 22,000–25,000 main words. This draft is longer because some combined decisions retain their technical conditions; it still reduces total narration rather than only renaming files. Lesson count alone is not a comprehension or value claim.\n'
    result.update(filming_outputs(root,rows,CORE_IDS,ADV_IDS,PRACTICAL_IDS,CHAPTERS))
    return {p:s.replace('\\n','\n').rstrip()+'\n' for p,s in result.items()}


def merged_history(root: Path) -> None:
    item=MERGED_LESSON
    data=subprocess.check_output(['git','show',item['source_commit']+':'+item['path']],cwd=root)
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual!=item['blob']:raise ValueError('Merged A7.2 source history differs')
    if (root/item['path']).exists():raise ValueError('Merged A7.2 restored as duplicate active lesson')
    print('PASS: merged A7.2 recovered byte-for-byte; current destinations are 7.1, 8.1 and W07.')

def build(root: Path) -> None:
    expected=outputs(root)
    for directory in ['teleprompter','lesson-text','modules']:
        d=root/directory
        if d.exists():
            for p in d.rglob('*'):
                if p.is_file() and p.relative_to(root).as_posix() not in expected: raise ValueError('Unexpected file in generated area: '+str(p))
    for path,content in expected.items(): write(root,path,content)
    write(root,'ARITHMETIC-CHECKS.json',json.dumps(arithmetic(root),indent=2))

def arithmetic(root: Path) -> dict:
    f=load_json(root/'fixtures/reed-household.json'); c=f['cash_flow']; a=f['accounts']; debts=f['debts']
    num=lambda x:D(str(x))
    pay=sum(num(d['monthly_payment']) if 'monthly_payment' in d else num(d['balance'])*num(d['apr'])/12 for d in debts)
    gross=(num(c['alex_annual_gross'])+num(c['morgan_annual_income']))/12
    available=gross-num(c['monthly_tax_provision'])-num(c['original_monthly_living'])-pay
    employee=num(c['alex_annual_gross'])*num(c['alex_employee_percent'])/12
    reduced=available+num(c['adopted_monthly_spending_reduction'])
    asserts=[]
    def eq(label,value,want):
        if abs(num(value)-num(want))>D('0.000001'): raise ValueError(f'Arithmetic failed: {label}: {value} != {want}')
        asserts.append({'check':label,'value':float(value),'status':'PASS'})
    eq('starting pool before employee contribution',available,1275)
    eq('employee contribution',employee,775)
    eq('separate employer match',employee*num(c['employer_match_per_employee_dollar']),387.5)
    eq('starting unassigned monthly cash',available-employee,500)
    eq('adopted reduced-spending pool',reduced,2475)
    eq('funded waterfall residual',reduced-employee-num(c['reduced_spending_monthly_reserve_build'])-num(c['reduced_spending_monthly_extra_card']),0)
    for acc in a:
        if 'holdings' in acc:eq(acc['id']+' holdings sum',sum(map(num,acc['holdings'].values())),acc['value'])
        if 'btc_quantity' in acc:eq(acc['id']+' fixed-price value',num(acc['btc_quantity'])*num(f['price']['btc_usd']),acc['value'])
    assets=sum(num(x['value']) for x in a); debt=sum(num(x['balance']) for x in debts)
    general=sum(num(x['value']) for x in a if x['general_portfolio'])
    bitcoin=sum(num(v) for x in a if x['general_portfolio'] for k,v in x.get('holdings',{}).items() if k in ('bitcoin','bitcoin_spot_fund'))
    stocks=sum(num(x.get('holdings',{}).get('stocks',0)) for x in a if x['general_portfolio'])
    eq('included balance-sheet assets',assets,1996000); eq('total debt',debt,444500); eq('scoped net worth',assets-debt,1551500)
    eq('general portfolio',general,1307000);eq('Bitcoin exposure',bitcoin,728000);eq('stock exposure',stocks,504000);eq('cash and Treasury teaching category',general-bitcoin-stocks,75000)
    eq('Bitcoin-only stress loss',bitcoin*num(f['stress']['bitcoin_decline']),509600)
    stressed=assets-bitcoin*num(f['stress']['bitcoin_decline'])-stocks*num(f['stress']['selected_stocks_decline'])-sum(num(x['value']) for x in a if x['id']=='home')*num(f['stress']['home_decline'])
    eq('partial combined-stress assets',stressed,1217200)
    eq('target sums to one',sum(num(f['target_example'][k]) for k in ('bitcoin','stocks','cash')),1)
    eq('target Bitcoin difference',general*num(f['target_example']['bitcoin'])-bitcoin,56200)
    res=f['reserve']; target=num(res['essential_monthly_outflow'])*num(res['target_months']); gap=target-num(res['assigned_current_value'])
    eq('reserve target',target,43200);eq('reserve gap',gap,11200);eq('reserve build months before interest',gap/num(res['monthly_build']),22.4)
    e=f['education_example'];eq('education assignment once',num(e['oldest_assignment'])+num(e['younger_assignment']),e['combined_resources'])
    egap=num(e['annual_parent_commitment'])*num(e['years_supported'])-num(e['oldest_assignment']);eq('college pre-funding gap',egap,51000);eq('flat-cost zero-growth benchmark',egap/num(e['months_to_prefund']),850)
    rt=f['future_routing_example'];eq('future routing sum',num(rt['personally_held_bitcoin'])+num(rt['taxable_stock_fund']),rt['available_after_card']);eq('card payoff releases',num(405)+num(c['reduced_spending_monthly_extra_card']),1605)
    lot=f['lot_example']; proceeds=num(lot['sale_quantity'])*num(lot['sale_unit_price']);eq('illustrative sale proceeds',proceeds,20000)
    for i,(entry,want) in enumerate(zip(lot['lots'],[8400,16800,9600]),1):eq(f'sale gain using lot {i}',proceeds-num(lot['sale_quantity'])*num(entry['unit_cost']),want)
    eq('sequence down then up',((D(1000000)-50000)*D('.8')-50000)*D('1.25'),887500)
    eq('sequence up then down',((D(1000000)-50000)*D('1.25')-50000)*D('.8'),910000)
    eq('equal pretax Traditional end',D(1000)*2*D('.8'),1600);eq('equal pretax Roth end',D(1000)*D('.8')*2,1600)
    eq('50 percent initial LTV fixed-debt drop to 80',1-D('.5')/D('.8'),D('.375'))
    eq('25 percent initial LTV fixed-debt drop to 80',1-D('.25')/D('.8'),D('.6875'))
    eq('reserve after hypothetical project',D(32000)-D(30000),2000)
    eq('same sale gain illustration',D(20000)-D(16000),4000)
    eq('generic annual premium monthly allowance',D(1200)/12,100)
    eq('generic recurring bill full-year saving',D(40)*12,480)
    eq('required debt service annualized',pay*12,40100)
    card=next(x for x in debts if x['id']=='card')
    first_interest=num(card['balance'])*num(card['apr'])/12
    eq('rough card first-month interest before fees or new charges',first_interest,D('235.125'))
    eq('rough card principal portion of illustrated minimum',num(card['monthly_payment'])-first_interest,D('169.875'))
    generic_principal=D(20000); monthly_rate=D('.08')/12; months=60
    generic_payment=generic_principal*monthly_rate/(1-(1+monthly_rate)**(-months))
    eq('separate generic amortizing monthly payment',generic_payment,D('405.52788576827365'))
    eq('separate generic amortizing total interest',generic_payment*months-generic_principal,D('4331.673146096419'))
    eq('separate generic interest-only monthly payment',generic_principal*monthly_rate,D('133.33333333333333'))
    eq('separate generic interest-only five-year interest',generic_principal*monthly_rate*months,8000)
    eq('fixed debt 50 percent LTV after collateral halves',D('.5')/D('.5'),1)
    taxable_general=sum(num(x['value']) for x in a if x['general_portfolio'] and x['tax']=='taxable')
    eq('Allocation taxable subset includes bills and reserve',taxable_general,575000)
    eq('Allocation retirement subset is not unrestricted cash',general-taxable_general,732000)
    direct_value=sum(num(x.get('holdings',{}).get('bitcoin',0)) for x in a)
    eq('Allocation native Bitcoin value',direct_value,410000)
    eq('Allocation spot-fund exposure remains a security',bitcoin-direct_value,318000)
    pair=[x for x in a if x['id'] in ('alex_traditional_401k','alex_roth_ira')]
    eq('two differently sized Alex accounts total',sum(num(x['value']) for x in pair),555000)
    eq('two Alex accounts combined spot-fund exposure',sum(num(x['holdings']['bitcoin_spot_fund']) for x in pair),239000)
    eq('Allocation hypothetical target cash dollars',general*num(f['target_example']['cash']),78420)
    eq('Allocation group after isolated Bitcoin decline',general-bitcoin*num(f['stress']['bitcoin_decline']),797400)
    eq('same-budget Traditional after illustrative 30 percent tax',D(1000)*2*(1-D('.3')),1400)
    eq('same-budget Traditional after illustrative 10 percent tax',D(1000)*2*(1-D('.1')),1800)
    eq('half-Bitcoin group isolated 70 percent decline',D('.5')*D('.7'),D('.35'))
    eq('80 percent Bitcoin group isolated 70 percent decline',D('.8')*D('.7'),D('.56'))
    # Separate 4.3 sizing illustration: never mutate or calibrate the Reed fixture.
    near=(D(0),D(0),D(50000)); bridge=(D(20000),D(50000),D(30000)); long=(D(280000),D(70000),D(0))
    eq('timeframe example near-term assigned',sum(near),50000)
    eq('timeframe example Bridge assigned',sum(bridge),100000)
    eq('timeframe example long-runway assigned',sum(long),350000)
    combined=tuple(near[i]+bridge[i]+long[i] for i in range(3))
    eq('timeframe example counted once',sum(combined),500000)
    for i,(asset,amount,weight) in enumerate([('Bitcoin',300000,'.60'),('stocks',120000,'.24'),('cash',80000,'.16')]):
        eq('timeframe example '+asset+' dollars',combined[i],amount)
        eq('timeframe example '+asset+' weight',combined[i]/sum(combined),D(weight))
    revised_long=(D(210000),D(140000),D(0))
    revised=tuple(near[i]+bridge[i]+revised_long[i] for i in range(3))
    eq('timeframe alternate total unchanged',sum(revised),500000)
    eq('timeframe alternate Bitcoin weight',revised[0]/sum(revised),D('.46'))
    eq('timeframe alternate stock weight',revised[1]/sum(revised),D('.38'))
    eq('timeframe alternate cash unchanged',revised[2],80000)
    eq('timeframe isolated long-runway reallocation',long[0]-revised_long[0],70000)
    # New explicitly hypothetical teaching mechanisms; not Reed inputs or engine outputs.
    eq('whole portfolio cash jobs',D(60000)+40000,100000)
    eq('whole portfolio longer runway residual',D(1000000)-500000-100000,400000)
    eq('whole portfolio initial Bitcoin weight',D(500000)/1000000,D('.5'))
    eq('whole portfolio initial stock weight',D(400000)/1000000,D('.4'))
    eq('whole portfolio initial cash weight',D(100000)/1000000,D('.1'))
    eq('additional two-year cash choice',D(50000)*2,100000)
    eq('whole portfolio revised stock amount',D(1000000)-500000-200000,300000)
    eq('whole portfolio revised cash weight',D(200000)/1000000,D('.2'))
    eq('conversion example qualified Roth ending',D(30000)*2,60000)
    eq('no conversion example outside ending',D(6000)*2,12000)
    for rate,want in [(D('.2'),60000),(D('.3'),54000),(D('.1'),66000)]:
        eq('conversion comparison total after '+str(rate),D(30000)*2*(1-rate)+D(6000)*2,want)
    eq('generic harvest gain',D(20000)-16000,4000)
    eq('generic harvest loss',D(16000)-20000,-4000)
    eq('retirement rough example before other costs',D(96000)+12000-40000,68000)
    eq('separate complete cash-outflow example',D(96000)+12000+12000+6000,126000)
    eq('separate complete portfolio gap example',D(126000)-40000,86000)
    eq('coverage ordinary year A',D(12000)+3000,15000)
    eq('coverage ordinary year B',D(8000)+8000,16000)
    eq('sequence example ending difference',D(910000)-887500,22500)
    eq('same sequence no withdrawal both orders',D(1000000)*D('.8')*D('1.25'),1000000)
    eq('one-year simple interest illustration',D(20000)*D('.1'),2000)
    eq('one-year capitalized debt illustration',D(20000)*D('1.1'),22000)
    eq('practical annual spending reduction example',D(100000)-95000,5000)
    eq('insurance gap scale only',D(40000)*10,400000)
    eq('advanced annual debt example',D(25000)*D('1.12'),28000)
    eq('advanced debt against lower collateral',D(28000)/50000,D('.56'))
    eq('hypothetical liquidation collateral',D(28000)/D('.8'),35000)
    eq('hypothetical liquidation price decline',1-D(35000)/100000,D('.65'))
    eq('repayment response illustration',D(28000-3000)/50000,D('.5'))
    eq('additional collateral response illustration',D(28000)/(50000+6000),D('.5'))
    eq('lump sum units example',D(20000)/100000,D('.2'))
    eq('staged declining price units example',D(10000)/100000+D(10000)/50000,D('.3'))
    eq('staged rising price units example',D(10000)/100000+D(10000)/200000,D('.15'))
    eq('incremental conversion first cost',D(4000)/20000,D('.2'))
    eq('incremental conversion next cost',D(6000)/20000,D('.3'))
    eq('incremental conversion combined average',D(4000+6000)/40000,D('.25'))
    eq('move recurring improvement illustration',D(10000)-8000,2000)
    eq('health tax combined cost illustration',D(2000)+1500,3500)
    eq('health tax combined rate illustration',D(3500)/10000,D('.35'))
    eq('recurring loan second year ending',(D(22000)+20000)*D('1.1'),46200)
    eq('recurring loan two-year accumulated interest',D(46200)-40000,6200)
    eq('SEPP birthday example age54 duration',D('59.5')-54,D('5.5'))
    eq('SEPP birthday example age58 later end',D(58)+5,63)
    eq('shared custodian exposure not loss probability',D('.3')+D('.3'),D('.6'))
    eq('hypothetical fee lower rate',D(500)*2,1000)
    eq('hypothetical fee higher rate',D(500)*20,10000)
    # Separate beginner practice cases. These are not Reed facts or app outputs.
    eq('learning percentage annual contribution',D(155000)*D('.06'),9300)
    eq('learning contribution monthly step',D(9300)/12,775)
    eq('learning hypothetical LTV threshold',D(50000)/62500,D('.8'))
    eq('learning hypothetical collateral price fall',(D(100000)-62500)/100000,D('.375'))
    eq('learning toy tax first layer',D(10000)*D('.1'),1000)
    eq('learning toy tax next layer',D(1000)*D('.2'),200)
    eq('learning toy tax total not actual brackets',D(1000)+200,1200)
    eq('practice annual allowance',D(1200)/12,100)
    eq('practice cash available deposit already after payroll saving',D(6000)-4500-100,1400)
    eq('practice remove duplicate annual allowance',D(6000)-4500,1500)
    eq('practice debt proposal exceeds budget',D(300)+900-1000,200)
    eq('practice debt after reserve',D(1000)-300,700)
    eq('practice more reserve leaves less extra debt',D(1000)-600,400)
    eq('practice portfolio initial cash',D(30000)+10000,40000)
    eq('practice portfolio remaining',D(400000)-200000-40000,160000)
    eq('practice portfolio changed cash',D(40000)+60000,100000)
    eq('practice portfolio changed remainder',D(400000)-200000-100000,100000)
    eq('practice portfolio changed other weight',D(100000)/400000,D('.25'))
    eq('practice later contribution not yet available',D(500)-300,200)
    eq('practice sale gain not tax',D(8000)-5000,3000)
    eq('practice conversion tax cash shortage',D(6000)-4000,2000)
    eq('practice coverage A',D(6000)+4000,10000)
    eq('practice coverage B',D(4000)+7000,11000)
    eq('practice retirement annual gap',D(72000)-24000,48000)
    eq('practice retirement monthly gap',D(48000)/12,4000)
    eq('practice retirement finite cash months',D(72000)/4000,18)
    eq('practice retirement changed annual gap',D(72000)-36000,36000)
    eq('practice retirement changed monthly gap',D(36000)/12,3000)
    eq('practice retirement changed cash months',D(72000)/3000,24)
    eq('practice changed income available',D(500)-400,100)
    eq('practice unchanged transfer shortage',D(500)-100,400)
    eq('consolidated recurring loan second opening',D(28000)+25000,53000)
    eq('consolidated recurring loan second ending',(D(28000)+25000)*D('1.12'),59360)
    eq('consolidated recurring loan added interest',D(59360)-50000,9360)
    # September 10 owner-framework examples: hypothetical, not live model results.
    eq('downside BTC price at 80 percent decline',D(100000)*(1-D('.8')),20000)
    eq('loan initial posted BTC',D(50000)/D('.5')/100000,1)
    eq('loan reserved BTC',D('3.5')-1,D('2.5'))
    eq('loan stressed total collateral',D('3.5')*20000,70000)
    eq('loan BTC at liquidation equality',D(50000)/D('.8')/20000,D('3.125'))
    eq('loan extra BTC at equality not sufficient',D('3.125')-1,D('2.125'))
    eq('loan stressed LTV with posted reserve',D(50000)/70000,D('0.7142857142857142857'))
    eq('loan total value boundary fraction',(1-D('.8'))*D('.8'),D('.16'))
    eq('loan balance at boundary',D('3.5')*100000*D('.16'),56000)
    eq('loan remaining debt headroom',D(56000)-50000,6000)
    eq('loan headroom fraction of principal',D(6000)/50000,D('.12'))
    eq('loan upfront all supporting BTC LTV',D(50000)/(D('3.5')*100000),D('0.1428571428571428571'))
    eq('loan interest can erase stress cushion',D(56000)/70000,D('.8'))
    eq('loan stricter 65 percent cure BTC',D(50000)/D('.65')/20000,D('3.846153846153846154'))
    eq('annual spending inflation first',D(100000)*D('1.03'),103000)
    eq('annual spending correction cap',D(103000)*D('.1'),10300)
    eq('annual spending capped lower suggestion',max(D(86000),D(103000)*D('.9')),92700)
    eq('annual spending change from prior',D(100000)-92700,7300)
    eq('annual spending remaining target gap',D(92700)-86000,6700)
    eq('annual lifestyle gap after change',D(92700)-40000,52700)
    eq('annual lifestyle gap before change',D(103000)-40000,63000)
    eq('annual reserve twelve month target',D(52700)/12*12,52700)
    eq('annual reserve six month review floor',D(52700)/12*6,26350)
    eq('annual reserve refill gap',D(52700)-45000,7700)
    eq('insurance support need zero real return',D(40000)*10,400000)
    eq('insurance remaining coverage gap',D(400000)-100000-200000,100000)
    eq('insurance covered liability residual',D(2000000)-500000-1000000,500000)
    return {'scope':'Arithmetic teaching checks only; no retirement forecast, tax opinion, lender assurance or model acceptance.', 'checks':asserts,'current_dta_percent':float(debt/assets*100),'partial_stress_dta_percent':float(debt/stressed*100)}

CLEANUP_PIN = 'a7be495e670078cd44ea4e0792538b0eaa32dd95'

def preservation(root: Path) -> dict:
    recovery=load_json(root/'production/repository-cleanup.json')
    if recovery.get('history_commit')!=CLEANUP_PIN: raise ValueError('Unexpected history pin')
    retired=recovery['retired_files']; by={r['path']:r for r in retired}
    if len(by)!=len(retired) or recovery['retired_count']!=len(retired): raise ValueError('Invalid cleanup inventory')
    if digest(json.dumps(retired,sort_keys=True,separators=(',',':')).encode())!='45a3bf61d7913417597bc9063c3663b2c3ba66a3e22dba4459aef4796c3bb8ba': raise ValueError('Historical recovery inventory changed')
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
        git_hash=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if digest(data)!=row['sha256'] or git_hash!=row['git_blob']: raise ValueError('Historical recovery mismatch: '+row['path'])
    print('PASS: recovered and byte-verified',len(recovery['retired_files']),'retired files from pinned Git history; original dictation retained.')
    merged_history(root)
    c=consolidation(root)
    for row in c['mapping']:
        data=subprocess.check_output(['git','show',CONSOLIDATION_PIN+':'+row['old_path']],cwd=root)
        if digest(data)!=row['source_sha256']:raise ValueError('Consolidated source history differs '+row['old_id'])
    print('PASS: all 65 pre-consolidation scripts recovered from pinned history; all destinations recorded.')

def check(root: Path) -> None:
    expected=outputs(root)
    for path,text in expected.items():
        if not (root/path).exists() or (root/path).read_text(encoding='utf-8')!=text: raise ValueError('Generated layer differs: '+path)
    actual=arithmetic(root)
    if load_json(root/'ARITHMETIC-CHECKS.json')!=actual: raise ValueError('Stale arithmetic report')
    record=load_json(root/'PROMOTION-RECORD.json')
    preservation(root)
    alltext='\n'.join(x['read'] for x in catalog(root))
    for phrase in ['Foundation','Integration','Optimization','Sovereign','$850','$605','Form 8606','COBRA','Part A','five-tax-year','principal']:
        if phrase not in alltext: raise ValueError('Required teaching missing: '+phrase)
    for phrase in ['on this slide','the slide shows','submit your answer','complete the practice case','INSERT SCRIPT']:
        if phrase.lower() in alltext.lower():raise ValueError('Production or homework wording in narration: '+phrase)
    for path in sorted(set(['README.md','HANDOFF.md','DICTATION-ORDER.md','ADVANCED-DICTATION-ORDER.md','FILM-ORDER.md','CIRCLE-STRUCTURE.md','SCREEN-SHOOT-LIST.md','PRODUCTION-CHECKLIST.md','MASTER-COURSE.md','MASTER-ADVANCED.md']) | {x for x in expected if x.endswith('.md')} | {r['path'] for r in catalog(root)}):
        for link in re.findall(r'\]\(([^)]+)\)',(root/path).read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):continue
            if not (root/Path(path).parent/link.split('#')[0]).exists():raise ValueError(f'Broken link in {path}: {link}')
    print(f'PASS: {len(ALL_IDS)} components; {len(expected)} synchronized outputs; {len(actual["checks"])} arithmetic checks; {len(record["preserved"])} historical preservation records (Git recovery checked separately).')

def tests(root: Path) -> None:
    check(root)
    with tempfile.TemporaryDirectory() as tmp:
        copy=Path(tmp)/'course';shutil.copytree(root,copy,ignore=shutil.ignore_patterns('.git','__pycache__'))
        cases=[]
        p=copy/'ALL-SCRIPTS.md';old=p.read_bytes();p.write_text('stale')
        cases.append(('stale generated script',p,old))
        for name,p,old in cases:
            try:check(copy)
            except ValueError:print('PASS mutation:',name)
            else:raise ValueError('Mutation escaped: '+name)
            p.write_bytes(old)
        p=copy/catalog(copy)[0]['path'];old=p.read_bytes();p.unlink()
        try:check(copy)
        except ValueError:print('PASS mutation: missing lesson')
        else:raise ValueError('Missing lesson escaped')
        p.write_bytes(old)
        p=copy/'fixtures/reed-household.json';old=p.read_bytes();f=load_json(p);f['cash_flow']['monthly_tax_provision']=4001;p.write_text(json.dumps(f))
        try:arithmetic(copy)
        except ValueError:print('PASS mutation: changed fixture arithmetic')
        else:raise ValueError('Fixture mutation escaped')
        p.write_bytes(old)
        p=copy/'teleprompter/core/0-1.txt';old=p.read_bytes();p.write_text(old.decode()+'\nPRODUCTION NOTE LEAK\n')
        try:check(copy)
        except ValueError:print('PASS mutation: spoken-copy contamination')
        else:raise ValueError('Teleprompter mutation escaped')
        p.write_bytes(old)
        check(copy)
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
        r=next(x for x in catalog(copy) if x['id']==ADV_IDS[0])
        p=copy/r['path']; saved=p.read_bytes()
        p.write_text(re.sub(r'^After lesson: .+$','After lesson: 99.99',saved.decode(),flags=re.M),encoding='utf-8',newline='\n')
        try: check(copy)
        except ValueError: print('PASS mutation: invalid situational parent')
        else: raise ValueError('Invalid route escaped')
        p.write_bytes(saved)
        p.write_text(re.sub(r'^Return to: .+$','',saved.decode(),flags=re.M),encoding='utf-8',newline='\n')
        try: check(copy)
        except ValueError: print('PASS mutation: missing return route')
        else: raise ValueError('Missing return route escaped')
        p.write_bytes(saved)
        check(copy)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','check','test','history'])
    args=parser.parse_args()
    {'build':build,'check':check,'test':tests,'history':history}[args.command](ROOT)
