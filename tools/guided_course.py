#!/usr/bin/env python3
"""Build the guided Academy from canonical scripts. Standard library only.

history: verify retired files against the pinned Git history (full checkout required).
build: derive reading copies, orders and manifests from scripts (never reverse).
check: check structure, arithmetic, links and byte-for-byte derived-file parity.
test: prove missing lessons, stale copies and fixture changes are rejected.
No network, app, credential, financial-account, or deployment operations.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, tempfile, subprocess
from pathlib import Path
from decimal import Decimal as D

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b'
APP_SHA = 'dccf0fedaeef6bd767c20fb9af0fe74f1cd4454f'
CORE_COUNTS = [2,5,5,6,7,5,8,4,4,3,2]
CORE_IDS = [f'{m}.{n}' for m,c in enumerate(CORE_COUNTS) for n in range(1,c+1)]
ADV_IDS = ['A1.1','A3.1','A3.2','A4.1','A5.1','A5.2','A5.3','A6.1','A6.2','A6.3','A7.1','A7.3','A7.4','A8.1']
PRACTICAL_IDS = ['W01','W02','W03','W04','W05','W06','W07','D07','W08','W09','W10']
ALL_IDS = CORE_IDS + ADV_IDS + PRACTICAL_IDS
NAMES = ['Start here','First working plan','Cash flow, reserve and life events','Debt and leverage','Allocation and the next dollar','Tax strategy','Retirement paycheck','Custody','Family handoff','Maintenance','Read and share your plan']
CHAPTERS = {'1.1':'W01 chapters 1','1.2':'W01 chapters 2–5','1.3':'W01 chapters 6–7','1.4':'W01 chapters 8','1.5':'W01 chapters 9–10','2.1':'W02 chapters 1–2','2.2':'W02 chapters 3','2.3':'W02 chapters 4–5','2.4':'W02 chapters 6','2.5':'W02 chapters 7 (optional)','3.1':'W03 chapters 1','3.2':'W03 chapters 2','3.3':'W03 chapters 3','3.4':'prepare the financing comparison; continue through 3.5 before W03 chapter 4','3.5':'W03 chapters 4','3.6':'W03 chapters 5–6','4.1':'W04 chapters 1','4.2':'W04 chapters 2','4.3':'W04 chapters 3','4.4':'W04 chapters 4','4.5':'W04 chapters 5','4.6':'W04 chapters 6','4.7':'W04 chapters 7–8','5.1':'W05 chapters 1','5.2':'W05 chapters 2','5.3':'W05 chapters 3','5.4':'W05 chapters 4','5.5':'W05 chapters 5–6','6.1':'W06 chapters 1','6.2':'W06 chapters 2','6.3':'W06 chapters 3','6.4':'W06 chapters 4','6.5':'W06 chapters 5','6.6':'W06 chapters 6','6.7':'W06 chapters 7','6.8':'W06 chapters 8','7.1':'W07 chapters 1','7.2':'D07 then W07 chapters 2','7.3':'W07 chapters 3','7.4':'W07 chapters 4','8.1':'W08 chapters 1','8.2':'W08 chapters 2','8.3':'W08 chapters 3–4','8.4':'W08 chapters 5','9.1':'W09 chapters 1–2','9.2':'W09 chapters 3','9.3':'W09 chapters 4–5','10.1':'W10 chapters 1–2','10.2':'W10 chapters 3–5'}

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write(root: Path, path: str, content: str) -> None:
    p = root/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content.rstrip()+'\n',encoding='utf-8')

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
        read=section(text,'Read aloud'); checkpoint=section(text,'Member checkpoint') or section(text,'Readback and finish')
        if not checkpoint: raise ValueError('Missing completion check '+lid)
        if lid not in PRACTICAL_IDS and len(read.split())<50: raise ValueError('Empty or placeholder narration '+lid)
        gate=re.search(r'^Gate: (.+)$',text,re.M)
        sources=re.search(r'^Sources: (.+)$',text,re.M)
        if not gate or not sources: raise ValueError('Missing gate/source '+lid)
        if re.search(r'\b(?:TODO|TBD|INSERT SCRIPT)\b',read): raise ValueError('Unfinished spoken placeholder '+lid)
        if re.search(r'canonical owner|hold that screen capture|the demonstration is gated|We are not using a personal family story',read,re.I): raise ValueError('Production language in narration '+lid)
        records[lid]={'id':lid,'title':title,'path':str(p.relative_to(root)),'gate':gate.group(1),'sources':sources.group(1),'words':len(read.split()),'spoken_sha256':digest(read.encode()),'source_sha256':digest(p.read_bytes()),'read':read,'text':text,'checkpoint':checkpoint}
    if set(records)!=set(ALL_IDS): raise ValueError('Lesson set differs: '+str(set(records)^set(ALL_IDS)))
    return [records[x] for x in ALL_IDS]

MERGED_LESSON = {
    'id':'A7.2',
    'path':'scripts/advanced/A7-2_decide-which-custody-responsibilities-the-household-can-maintain.md',
    'source_commit':'f6392a6341c23c557e605506dab3530b67efa146',
    'blob':'0443c4640a4f4b431429eab204f5fe9dc0b67413',
    'destinations':['7.1','7.4','W07'],
}

def situation_route(row: dict) -> dict:
    values={}
    for key,heading in [('after','After lesson'),('when','Use when'),('before','Complete before'),('return','Return to')]:
        found=re.findall(r'^'+re.escape(heading)+r': (.+)$',row['text'],re.M)
        if len(found)!=1 or not found[0].strip():
            raise ValueError('Missing or duplicate situation route '+row['id']+': '+heading)
        values[key]=found[0].strip()
    if values['after'] not in CORE_IDS or values['after'].split('.')[0]!=row['id'][1:].split('.')[0]:
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
    if row['id']=='2.3':return 'Accepted reference; unchanged'
    if 'Status: SPOKEN_EDIT_REVIEW' in row['text']:return 'Spoken-language edit; owner review pending'
    if 'Status: TEACHING_RETAINED_REVIEW' in row['text']:return 'Existing explanation retained; owner review pending'
    if 'Status: WALKTHROUGH_REWRITE_REVIEW' in row['text']:return 'Prepared narration; review and capture pending'
    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:return 'Written draft; owner review pending'
    return 'Review status requires attention'

def outputs(root: Path) -> dict[str,str]:
    rows=catalog(root);by={r['id']:r for r in rows};result={}
    routes={x:situation_route(by[x]) for x in ADV_IDS}
    order=member_order(rows)
    records=[]
    for r in rows:
        record={k:v for k,v in r.items() if k not in ('read','text','checkpoint')}
        if r['id'] in routes:record['member_route']=routes[r['id']]
        record['member_group']='For your situation' if r['id'] in ADV_IDS or r['id']=='2.5' else 'Main path' if r['id'] in CORE_IDS else 'Walkthrough'
        records.append(record)
    manifest={'canonical':'scripts/','source_commit':SOURCE_SHA,'app_contract_commit':APP_SHA,
              'counts':{'core':len(CORE_IDS),'advanced':len(ADV_IDS),'working_sessions':10,'device_demos':1},
              'member_labels':{'core':'Main path (includes the conditional college lesson)','advanced':'For your situation'},
              'member_order':order,'merged_lessons':[MERGED_LESSON],'lessons':records}
    result['COURSE-MANIFEST.json']=json.dumps(manifest,indent=2,ensure_ascii=False)
    editor_intro='Generated from `scripts/`. Spoken text is under Read aloud; production notes and checkpoints are not narration. Owner review and actual app/device recording remain separate.\n\n'
    result['MASTER-COURSE.md']='# Main course — teaching and production notes\n\n'+editor_intro+'The main path includes one conditional college lesson. Related situation-specific lessons are placed in the reading and playback orders where their decisions arise.\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in CORE_IDS)
    result['MASTER-ADVANCED.md']='# For your situation — collected teaching notes\n\n'+editor_intro+'This is a reference index, not a second course or a higher level. The A-prefixed IDs and filename are retained for existing links. Use a lesson when its stated situation applies, then return to the indicated walkthrough.\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in ADV_IDS)
    spoken='# Course reading copy\n\nFollow the main path. For your situation lessons appear beside the decision they support. Read their condition: when your plan relies on that strategy, complete the extra lesson before relying on it; otherwise continue. Navigation notes are not spoken.\n\n'
    for x in order:
        r=by[x]
        spoken+='---\n\n'
        if x in routes:
            rr=routes[x]
            spoken+=f"*For your situation — {rr['when']} {rr['before']} Return to {rr['return']}.*\n\n"
        elif x=='2.5':
            spoken+='*For your situation — you intend to help fund education. Otherwise continue to Debt. Return to W02 chapter 7, then lesson 3.1.*\n\n'
        spoken+=f"## {x} — {r['title']}\n\n{r['read']}\n\n"
    result['ALL-SCRIPTS.md']=spoken
    for r in rows:
        result['lesson-text/'+r['path'].split('scripts/',1)[1]]=r['text']
        if r['read']:result[read_link(r)]=r['read']
    for m in range(11):
        module=f'# Session {m} — {NAMES[m]}\n\nMain lessons build the plan in order. Read an additional lesson only when its stated situation applies; then return to the indicated working chapter. These are draft teaching and production notes.\n\n'
        for x in CORE_IDS:
            if not x.startswith(str(m)+'.'):continue
            if x=='2.5':module+='> **For your situation:** You intend to help fund education. Otherwise continue to Debt.\n\n'
            module+=by[x]['text'].strip()+'\n\n'
            for a in ADV_IDS:
                if routes[a]['after']==x:
                    module+='---\n\n## For your situation\n\n'+routes[a]['when']+' '+routes[a]['before']+'\n\n'+by[a]['text'].strip()+'\n\n**Return to:** '+routes[a]['return']+'.\n\n'
            module+='---\n\n'
        result[f'modules/{m:02d}.md']=module
    reading='# Start here — course reading order\n\nWork through each main lesson and its matching walkthrough. **For your situation** identifies extra teaching for a decision you may or may not face. It is not a skill level. When you use that strategy, complete the lesson before relying on it; otherwise carry on. The Reserve remains the accepted reference; other wording is for owner review.\n\n'
    film='# Learning and filming order\n\nOne main path with situation-specific lessons beside the decisions they support. Read the main explanation, complete the relevant additional lesson when needed, then apply the decision in the matching working chapter. These written routes do not approve app/device capture or perform outside actions.\n\n'
    for m in range(11):
        reading+=f'## {m} — {NAMES[m]}\n\n';film+=f'## {m} — {NAMES[m]}\n\n'
        for x in CORE_IDS:
            if not x.startswith(str(m)+'.'):continue
            r=by[x];anchor='lesson-'+x.replace('.','-')
            optional=' — for households funding education' if x=='2.5' else ''
            reading+=f"### {x} — [{r['title']}]({read_link(r)}){optional}\n\n"
            film+=f'<a id="{anchor}"></a>\n\n'+f"### {x} — [{r['title']}]({r['path']}){optional}\n\n"
            if x=='2.5':
                note='No education commitment? Continue to lesson 3.1.\n\n';reading+=note;film+=note
            for a in ADV_IDS:
                if routes[a]['after']==x:
                    reading+=situation_card(by[a]);film+=situation_card(by[a])
            task=CHAPTERS.get(x,'W01 chapter 10 after the first plan is populated' if x=='0.2' else 'Orientation; no app entry')
            reading+='**Apply it:** '+task+'.\n\n'
            film+='**Working chapter:** '+task+'.\n\n'
    reading+='## Reference and recording notes\n\n[All situation-specific lessons](ADVANCED-DICTATION-ORDER.md) · [Paired working-session files](FILM-ORDER.md) · [Production checklist](PRODUCTION-CHECKLIST.md).\n\nThe internal paths retain `core` and `advanced` for link stability. Members follow the sequence above, not two separate courses. The former A7.2 responsibility lesson is included in 7.1, 7.4 and W07; it is not another required video.\n'
    result['DICTATION-ORDER.md']=reading
    reference='# For your situation — reference index\n\nThese lessons are placed beside the relevant main lesson in [the course reading order](DICTATION-ORDER.md). Use the situation, not your experience level, to choose. When a plan depends on the strategy, its extra analysis and safeguards are required for that choice. Otherwise skip it.\n\n'
    for x in order:
        if x not in routes:continue
        r=by[x];rr=routes[x]
        reference+=f"## [{r['title']}]({read_link(r)})\n\nAfter lesson {rr['after']}. {rr['when']}\n\n{rr['before']}\n\n**Return to:** {rr['return']}.\n\n[Teaching and demonstration notes]({r['path']}).\n\n"
    reference+='The college lesson is already beside Life Events in Session 2. Custody responsibilities formerly in A7.2 are now part of 7.1, 7.4 and W07, not a separate lesson. Legacy A IDs and this filename preserve existing references; they do not indicate a second program.\n'
    result['ADVANCED-DICTATION-ORDER.md']=reference
    film+='## Working-session files\n\n'+''.join(f"- [{x} — {by[x]['title']}]({by[x]['path']}) — recording evidence pending\n" for x in PRACTICAL_IDS)
    result['FILM-ORDER.md']=film
    result['CIRCLE-STRUCTURE.md']=film.replace('# Learning and filming order','# Member playback structure',1)
    result['SCREEN-SHOOT-LIST.md']='# Screen and device production list\n\nUse the route in FILM-ORDER.md. Applicable situation-specific instruction comes before relying on the strategy or executing its dependent action. All practical recordings still require actual evidence in CAPTURE-RECEIPTS.md.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n[Run sheet]({by[x]['path']})\n\n{by[x]['checkpoint']}\n\n" for x in PRACTICAL_IDS)
    result['MODULE-CHECKPOINTS.md']='# Member completion checks\n\nMain decisions and situation-specific applications are shown in learning order. A required professional answer or an unverified access route is not a completed action.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n"+(f"For your situation: {routes[x]['when']}\n\n" if x in routes else '')+by[x]['checkpoint']+'\n\n' for x in order+PRACTICAL_IDS)
    result['PRODUCTION-CHECKLIST.md']='# Production checklist\n\nOne main path, with applicable extra lessons routed at the relevant decision. The language pass does not establish Austin approval, instructional effectiveness or capture readiness. A7.2 is merged into 7.1/7.4/W07 and excluded from active recording counts.\n\n| ID | Script | Text review | Austin approval | Remaining publication gate |\n|---|---|---|---|---|\n'+''.join(f"| {r['id']} | [{r['title']}]({r['path']}) | {review_state(r)} | {'Reference accepted; filming separate' if r['id']=='2.3' else 'Pending'} | {r['gate']} |\n" for r in rows)
    main=sum(by[x]['words'] for x in CORE_IDS);extra=sum(by[x]['words'] for x in ADV_IDS)
    result['COURSE-METRICS.md']=f'# Current course inventory\n\n{len(CORE_IDS)} main-path teaching files include one conditional college lesson: 50 shared-path lessons plus college when relevant. There are {len(ADV_IDS)} additional For your situation lessons placed within their sections, ten app working sessions and one device demonstration. Total active teaching lessons: {len(order)}. A7.2 has been merged, not hidden in a second course.\n\nMain-path spoken text including college: {main:,} words. Situation-specific text: {extra:,} words. Approximate narration at 150 words/minute: {main/150:.0f} and {extra/150:.0f} minutes respectively. These are reading estimates, not promised runtimes or proof of value; walkthroughs and pauses are additional. Members do not need every situation-specific lesson.\n'
    return {p:t.rstrip()+'\n' for p,t in result.items()}


def merged_history(root: Path) -> None:
    item=MERGED_LESSON
    data=subprocess.check_output(['git','show',item['source_commit']+':'+item['path']],cwd=root)
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual!=item['blob']:raise ValueError('Merged A7.2 source history differs')
    if (root/item['path']).exists():raise ValueError('Merged A7.2 restored as duplicate active lesson')
    print('PASS: merged A7.2 recovered byte-for-byte; active teaching is in 7.1, 7.4 and W07.')

def build(root: Path) -> None:
    expected=outputs(root)
    for directory in ['teleprompter','lesson-text','modules']:
        d=root/directory
        if d.exists():
            for p in d.rglob('*'):
                if p.is_file() and str(p.relative_to(root)) not in expected: raise ValueError('Unexpected file in generated area: '+str(p))
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

def check(root: Path) -> None:
    expected=outputs(root)
    for path,text in expected.items():
        if not (root/path).exists() or (root/path).read_text(encoding='utf-8')!=text: raise ValueError('Generated layer differs: '+path)
    actual=arithmetic(root)
    if load_json(root/'ARITHMETIC-CHECKS.json')!=actual: raise ValueError('Stale arithmetic report')
    record=load_json(root/'PROMOTION-RECORD.json')
    preservation(root)
    alltext='\n'.join(x['read'] for x in catalog(root))
    for phrase in ['Foundation','Integration','Optimization','Sovereign','eight hundred fifty','six hundred five','seventy percent stocks','fifty-nine and a half']:
        if phrase not in alltext: raise ValueError('Required teaching missing: '+phrase)
    for path in ['README.md','DICTATION-ORDER.md','ADVANCED-DICTATION-ORDER.md','FILM-ORDER.md','CIRCLE-STRUCTURE.md','SCREEN-SHOOT-LIST.md','PRODUCTION-CHECKLIST.md']:
        for link in re.findall(r'\]\(([^)]+)\)',(root/path).read_text()):
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
        check(copy)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','check','test','history'])
    args=parser.parse_args()
    {'build':build,'check':check,'test':tests,'history':history}[args.command](ROOT)
