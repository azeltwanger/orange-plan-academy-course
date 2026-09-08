#!/usr/bin/env python3
"""Build the guided Academy from canonical scripts. Standard library only.

promote: one-time, exact-input migration; preserves all prior active material.
build: derive reading copies, orders and manifests from scripts (never reverse).
check: check structure, arithmetic, links and byte-for-byte derived-file parity.
test: prove missing lessons, stale copies and fixture changes are rejected.
No network, app, credential, financial-account, or deployment operations.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, tempfile
from pathlib import Path
from decimal import Decimal as D

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b'
APP_SHA = 'dccf0fedaeef6bd767c20fb9af0fe74f1cd4454f'
CORE_COUNTS = [2,5,5,6,7,5,8,4,4,3,2]
CORE_IDS = [f'{m}.{n}' for m,c in enumerate(CORE_COUNTS) for n in range(1,c+1)]
ADV_IDS = ['A1.1','A3.1','A3.2','A4.1','A5.1','A5.2','A5.3','A6.1','A6.2','A6.3','A7.1','A7.2','A7.3','A7.4','A8.1']
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

def promote(root: Path) -> None:
    if (root/'COURSE-MANIFEST.json').exists(): raise ValueError('Already promoted; edit scripts/ and use build/check.')
    spec=load_json(root/'tools/guided-support.json')
    texts={}
    for path,expected in spec['input_hashes'].items():
        data=(root/path).read_bytes()
        if digest(data)!=expected: raise ValueError(f'Source changed; review before promotion: {path}')
        texts[path]=data.decode('utf-8')
    amendments=load_json(root/'tools/editorial-amendments.json')
    for a in amendments:
        if texts[a['file']].count(a['old'])!=1: raise ValueError('Ambiguous amendment: '+a['reason'])
        texts[a['file']]=texts[a['file']].replace(a['old'],a['new'])
    archive=root/'archive/pre-guided-promotion'
    archive.mkdir(parents=True,exist_ok=False)
    old=[]
    for p in list(root.glob('*.md')):
        old.append((p,archive/p.name))
    for directory in ['scripts','modules','lesson-text','visuals','alignment-pass','research']:
        p=root/directory
        if p.exists(): old.extend((f,archive/f.relative_to(root)) for f in p.rglob('*') if f.is_file())
    keep={'guided_course.py','guided-support.json','editorial-amendments.json'}
    old.extend((p,archive/'tools'/p.name) for p in (root/'tools').glob('*') if p.is_file() and p.name not in keep)
    old.extend((p,archive/p.relative_to(root)) for p in (root/'course-v2').rglob('*') if p.is_file())
    preservation=[]
    for p,dest in old:
        preservation.append({'old_path':str(p.relative_to(root)),'archive_path':str(dest.relative_to(root)),'sha256':digest(p.read_bytes())})
        dest.parent.mkdir(parents=True,exist_ok=True); shutil.move(str(p),str(dest))
    # Empty legacy directories are harmless, but no old active files remain.
    for path,text in texts.items():
        if '/sessions/' not in path and '/advanced/' not in path and not path.endswith('WALKTHROUGHS.md'): continue
        for heading,body in blocks(text):
            lid,title=heading.split(' — ',1)
            header=f'# {heading}\n\nStatus: PRE_DICTATION — editorial review complete; Austin approval pending.\n'
            header+=f'Adapted source: `{path}` at `{SOURCE_SHA}`.\n'
            header+='App references: accepted redesign direction; final screen behavior requires capture evidence.\n\n'
            if lid in PRACTICAL_IDS:
                header=header.replace('PRE_DICTATION — editorial review complete; Austin approval pending.','CAPTURE_HOLD — reviewed run sheet and narration cues; no recording approved.')
                body+='\n### Spoken cues (use with the matching chapters)\n\n'
                for i,cue in enumerate(spec['narration'][lid],1): body+=f'**Chapter {i}.** {cue}\n\n'
            write(root,script_path(lid,title),header+body.strip())
    fixture=json.loads(texts['course-v2/demo-household.json'])
    fixture['scope_notice']='Simplified teaching balance sheet. Vehicle/equipment/business values are omitted; related debts remain included. This is not a complete household valuation or a calibrated app fixture.'
    fixture['education_example']={'combined_resources':58000,'oldest_assignment':29000,'younger_assignment':29000,'annual_parent_commitment':20000,'years_supported':4,'months_to_prefund':60,'growth_assumed':0,'cost_inflation_assumed':0,'scope':'Arithmetic benchmark only. Actual account beneficiaries, inflation, tax, timing, returns and future cash flow require review. No immediate $850 surplus is asserted.'}
    fixture['future_routing_example']={'available_after_card':1605,'personally_held_bitcoin':1000,'taxable_stock_fund':605,'scope':'Illustrative future comparison, not an engine recommendation or current contribution.'}
    write(root,'fixtures/reed-household.json',json.dumps(fixture,indent=2,ensure_ascii=False))
    write(root,'fixtures/REED-HOUSEHOLD.md',texts['course-v2/DEMO-HOUSEHOLD.md']+'\n\n## Calculation scope\n\n'+fixture['scope_notice']+' See `reed-household.json` for the exact holdings, payment conventions and explicitly hypothetical examples. The JSON controls arithmetic when the prose is abbreviated.\n')
    write(root,'archive/pre-guided-promotion/ARCHIVE-NOT-FOR-RECORDING.md','# Historical material\n\nThese files preserve the preceding course, including prior dictation. They are not the recording order. Start at the repository README and DICTATION-ORDER.md.\n')
    write(root,'PROMOTION-RECORD.json',json.dumps({'source_commit':SOURCE_SHA,'app_contract_commit':APP_SHA,'inputs':spec['input_hashes'],'preserved':preservation,'amendments':[{'file':a['file'],'reason':a['reason']} for a in amendments]},indent=2))
    for path,content in spec['documents'].items(): write(root,path,content)
    write(root,'course-v2/README.md','# Guided draft workspace retired\n\nThe reviewed course is now canonical in `scripts/`. Begin with `../DICTATION-ORDER.md`. The exact former grouped source is preserved in `../archive/pre-guided-promotion/course-v2/`. Do not regenerate active scripts from this historical workspace.\n')
    build(root)
    check(root)

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

def outputs(root: Path) -> dict[str,str]:
    rows=catalog(root); by={r['id']:r for r in rows}; result={}
    manifest={'canonical':'scripts/','source_commit':SOURCE_SHA,'app_contract_commit':APP_SHA,'counts':{'core':51,'advanced':15,'working_sessions':10,'device_demos':1},'lessons':[{k:v for k,v in r.items() if k not in ('read','text','checkpoint')} for r in rows]}
    result['COURSE-MANIFEST.json']=json.dumps(manifest,indent=2,ensure_ascii=False)
    for ids,title,path in [(CORE_IDS,'Core course','MASTER-COURSE.md'),(ADV_IDS,'Advanced library','MASTER-ADVANCED.md')]:
        result[path]=f'# {title}\n\nGenerated from canonical `scripts/`. New prose is a pre-dictation draft, not a claim Austin already said it. Production notes and member checkpoints are not spoken.\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in ids)
    result['ALL-SCRIPTS.md']='# Read-aloud course — core, then optional Advanced\n\nGenerated from scripts. Only the text under each lesson title is spoken. See DICTATION-ORDER.md for working-session placement and publication gates.\n\n'+'\n\n---\n\n'.join(f"## {x} — {by[x]['title']}\n\n{by[x]['read']}" for x in CORE_IDS+ADV_IDS)
    for r in rows:
        dest='lesson-text/'+r['path'].split('scripts/',1)[1]
        result[dest]=r['text']
        if r['read']:
            subgroup='advanced' if r['id'].startswith('A') else 'core'
            result[f"teleprompter/{subgroup}/{r['id'].replace('.','-')}.txt"]=r['read']
    for m in range(11):
        result[f'modules/{m:02d}.md']=f'# Session {m} — {NAMES[m]}\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in CORE_IDS if x.startswith(str(m)+'.'))
    for ids,title,path in [(CORE_IDS,'Core dictation order','DICTATION-ORDER.md'),(ADV_IDS,'Advanced dictation order','ADVANCED-DICTATION-ORDER.md')]:
        intro=f'# {title}\n\nRead chronologically. Edit the canonical script when dictating; `teleprompter/` and masters are generated copies. Every clip remains an Austin-approval draft. A listed publication gate does not prevent dictating its durable explanation. Final product-dependent, tax, legal, insurance and device content requires the evidence described in FINALIZATION-STATUS.md.\n\n'
        table='| Lesson | Read-aloud copy | Canonical script | Words | Publication gate |\n|---|---|---|---:|---|\n'
        for x in ids:
            r=by[x]; group='advanced' if x.startswith('A') else 'core'
            table+=f"| {x} · {r['title']} | [Read](teleprompter/{group}/{x.replace('.','-')}.txt) | [Edit]({r['path']}) | {r['words']} | {r['gate']} |\n"
        result[path]=intro+table+'\nThe core has 51 clips (including optional college); the conditional Advanced library has 15. Working sessions and the device demonstration are listed separately in FILM-ORDER.md.\n'
    film='# Learning and filming order\n\nConcept clips may be recorded as talking head with graphics added in editing. App chapters are separate, replaceable recordings. The member watches the relevant explanation, completes its working chapter, and continues. No requirement to show the original slide deck live.\n\n'
    for m in range(11):
        film+=f'## Session {m} — {NAMES[m]}\n\n'
        for x in CORE_IDS:
            if not x.startswith(str(m)+'.'):continue
            film+=f"**{x} — [{by[x]['title']}]({by[x]['path']})**\n\n"
            film+=('Then '+CHAPTERS[x]+'.\n\n') if x in CHAPTERS else 'The Ask demonstration follows the populated first plan in W01 chapter 10.\n\n' if x=='0.2' else 'Orientation; no app entry required.\n\n'
    film+='## Working-session files\n\n'+''.join(f"- [{x} — {by[x]['title']}]({by[x]['path']}) — CAPTURE HOLD\n" for x in PRACTICAL_IDS)
    result['FILM-ORDER.md']=film
    result['CIRCLE-STRUCTURE.md']=film.replace('# Learning and filming order','# Member playback structure',1)
    result['SCREEN-SHOOT-LIST.md']='# Screen and device production list\n\nAll eleven practical recordings remain unapproved until a matching entry in CAPTURE-RECEIPTS.md is completed. Each source includes the run sheet, evidence checks and spoken cues.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n[Run sheet and cues]({by[x]['path']})\n\n{by[x]['checkpoint']}\n\n" for x in PRACTICAL_IDS)
    result['MODULE-CHECKPOINTS.md']='# Member completion checks\n\nA decision, a saved choice and an outside action are separate states. Funding a reserve or obtaining legal documents can remain an honest dated action; do not label it complete prematurely.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n{by[x]['checkpoint']}\n\n" for x in ALL_IDS)
    result['PRODUCTION-CHECKLIST.md']='# Production checklist\n\nEditorial pass completed over every listed script. Owner dictation/approval, professional review and capture evidence are separate. No professional sign-off or successful app/device run is asserted by these files.\n\n| ID | Script | Text review | Austin approval | Remaining publication gate |\n|---|---|---|---|---|\n'+''.join(f"| {r['id']} | [{r['title']}]({r['path']}) | Reviewed | Pending | {r['gate']} |\n" for r in rows)
    total=sum(r['words'] for r in rows if r['id'] in CORE_IDS)
    adv=sum(r['words'] for r in rows if r['id'] in ADV_IDS)
    result['COURSE-METRICS.md']=f'# Current course inventory\n\n51 core teaching clips, including one optional college lesson; 15 conditional Advanced clips; 10 app working sessions; 1 external device demonstration.\n\nCore spoken draft: {total:,} whitespace-delimited words. Advanced: {adv:,}. Approximate narration only at 150 words/minute: {total/150:.0f} core minutes and {adv/150:.0f} Advanced minutes. These are reading estimates, not promised runtimes; working sessions and pauses are additional.\n'
    return {p:t.rstrip()+'\n' for p,t in result.items()}

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
    return {'scope':'Arithmetic teaching checks only; no retirement forecast, tax opinion, lender assurance or model acceptance.', 'checks':asserts,'current_dta_percent':float(debt/assets*100),'partial_stress_dta_percent':float(debt/stressed*100)}

def check(root: Path) -> None:
    expected=outputs(root)
    for path,text in expected.items():
        if not (root/path).exists() or (root/path).read_text(encoding='utf-8')!=text: raise ValueError('Generated layer differs: '+path)
    actual=arithmetic(root)
    if load_json(root/'ARITHMETIC-CHECKS.json')!=actual: raise ValueError('Stale arithmetic report')
    record=load_json(root/'PROMOTION-RECORD.json')
    for row in record['preserved']:
        if digest((root/row['archive_path']).read_bytes())!=row['sha256']: raise ValueError('Historical material changed: '+row['archive_path'])
    alltext='\n'.join(x['read'] for x in catalog(root))
    for phrase in ['Foundation','Integration','Optimization','Sovereign','eight hundred fifty','six hundred five','seventy percent stocks','fifty-nine and a half']:
        if phrase not in alltext: raise ValueError('Required teaching missing: '+phrase)
    for path in ['README.md','DICTATION-ORDER.md','ADVANCED-DICTATION-ORDER.md','FILM-ORDER.md','CIRCLE-STRUCTURE.md','SCREEN-SHOOT-LIST.md','PRODUCTION-CHECKLIST.md']:
        for link in re.findall(r'\]\(([^)]+)\)',(root/path).read_text()):
            if '://' in link or link.startswith('#'):continue
            if not (root/Path(path).parent/link.split('#')[0]).exists():raise ValueError(f'Broken link in {path}: {link}')
    print(f'PASS: {len(ALL_IDS)} components; {len(expected)} synchronized outputs; {len(actual["checks"])} arithmetic checks; {len(record["preserved"])} preserved files.')

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

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['promote','build','check','test'])
    args=parser.parse_args()
    {'promote':promote,'build':build,'check':check,'test':tests}[args.command](ROOT)
