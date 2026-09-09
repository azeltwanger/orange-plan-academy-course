#!/usr/bin/env python3
"""One-use, bounded technical corrections. No network/app/financial operations.
Remove this helper and its branch-write workflow before merge.
"""
from pathlib import Path
from decimal import Decimal as D, getcontext
import hashlib,json,re,runpy,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
BASE='62b79a0121ab663a39cb9b269f2ca07e87c8590b'
GENERATOR='100dff910e320e37ea5091391917e603b3dab895'
EDITS=[
{'id':'4.5','sha256':'ded407e8412f7c0411f7fdd499fce15a63806c890a657c5e2a3655c101b82766','mode':'append','text':"For an IRA, don't use the Bitcoin as collateral for a personal loan or sell your personally owned Bitcoin to your own IRA. Those transactions can trigger distributions or loss of IRA tax treatment. Direct control does not turn retirement assets into unrestricted personal property.",'finding':'P01'},
{'id':'4.5','sha256':'558b6d9596c337f343e4601e00c29abce960e9261a238825f7cd567abe0ced48','mode':'append','text':'For tax-free reimbursement, the medical expense must qualify, have been incurred after the HSA was established, and not already have been reimbursed or deducted. After 65, nonmedical withdrawals are still income-taxable, but the additional 20% tax no longer applies. The account is not limited to medical spending forever.','finding':'P03'},
{'id':'4.5','sha256':'6f7dcfdbd0f772f31e0486b96c3e54db1e9c3c417a800ff51cdc7f971f1e1a60','mode':'replace','text':"Then check what the HSA can invest in. A limited menu doesn't automatically make the account bad, but it changes the comparison. You might hold appropriate stock exposure there and Bitcoin elsewhere. Or you might decide that more accessible Bitcoin is a more useful next contribution than additional HSA saving. Compare the tax benefit, menu, access, and purpose together.",'finding':'P03'},
{'id':'4.6','sha256':'52623c0b536af46b6b5719ac15408dc710e8d1258961a1c987d57a1f7a5008e6','mode':'append','text':"For ordinary retirement use, qualified Roth IRA earnings generally require both age 59½ and the five-tax-year period beginning with the first tax year for which you contributed to any Roth IRA. Other qualifying circumstances exist. This is separate from withdrawing regular contributions or checking a conversion's five-year rule.",'finding':'P02'},
{'id':'4.6','sha256':'2acb98984b030671bf327171ae6fe082023c1c085b5389a2473c57aa8c6a467e','mode':'replace','text':'Check the paycheck as well. Suppose Alex keeps contributing $775 a month but changes a pretax workplace contribution to Roth. He may take home less, even though the same amount reaches the retirement account. That difference needs to come from somewhere. This is a comparison, not a statement about his current election.','finding':'P02'},
{'id':'5.4','sha256':'2474cb1bd7d1b46f28db93d8a22f9daea72127bc79cafc98946b0ee00ac0c309','mode':'append','text':'Withholding tax from the IRA changes this comparison. Money withheld does not reach Roth unless you replace it through a valid rollover. Any taxable amount left out can also face the 10% additional early-distribution tax before 59½ unless an exception applies. Compare what actually reaches Roth and how the tax is paid.','finding':'P04'},
{'id':'5.4','sha256':'f8316e89627551bc1ed81b360226f3b621dba3beea07589f5b0867e55cd9c515','mode':'replace','text':'Required distributions must be satisfied separately; that amount cannot be converted. If you have nondeductible IRA basis, the tax calculation generally combines your own Traditional, SEP and SIMPLE IRAs, including their year-end values. You cannot isolate the after-tax money just by choosing one IRA to convert. Use Form 8606 and the complete records. Access to converted amounts has its own timing rules.','finding':'P04'},
{'id':'A5.2','sha256':'20cb7b80c7a81a2c592d99db0dd9f47c31f857355767e45b7c8619f2e0669583','mode':'append','text':'Be especially careful about replacement purchases in your own IRA or Roth IRA. A securities loss disallowed because of that purchase does not receive the usual replacement-basis adjustment. The deduction can be lost permanently, not merely postponed. Check automatic purchases before harvesting the taxable loss.','finding':'P05'},
{'id':'6.2','sha256':'84dd516fb336b5484693ed42209e3114c09dc01645545811c7aea2b025f1fd7b','mode':'append','text':'For your own Social Security retirement benefit, delayed retirement credits stop at 70. Waiting past that age does not earn more of those credits. Spousal and survivor benefits follow different rules.','finding':'P06'},
{'id':'6.3','sha256':'68ee1122dc240daf8012b44c2b1820070f067b553307b5b7445ba74f1259fd55','mode':'append','text':"Once you're Medicare-eligible, COBRA or retiree coverage does not extend the normal employment-based Part B enrollment window. Check the deadline when active employment or its coverage ends, not when COBRA runs out.\n\nApplying for premium-free Part A after 65 can backdate coverage by up to six months, but not before eligibility. Check that effective date before funding an HSA. Include employer contributions when working out the permitted amount.",'finding':'P07'},
{'id':'A6.1','sha256':'cbf37e71822db1828849fabc876a45cb1978830af10dab6d55b2b55ffe72d102','mode':'append','text':"For Marketplace coverage, start with adjusted gross income and add tax-exempt interest, nontaxable Social Security, and excluded foreign income. The standard deduction does not reduce this income measure. Include the relevant household members under the program's rules.",'finding':'P08'},
{'id':'A6.1','sha256':'76ac342a63a6a43bbdf130f1467df6e97707188d008bc29bfdc39974285c5261','mode':'append','text':'A conversion or gain late in the year can also require you to repay premium assistance already received. Include that potential repayment in the cash needed for the decision, not just the premium shown today.','finding':'P08'},
{'id':'A6.1','sha256':'80efeaa6d5664bcd849907b1ea17ac8bb8f698b6dd86f48342a2c999cafecf5b','mode':'replace','text':"Medicare's income-related premium calculation generally uses adjusted gross income plus tax-exempt interest from two tax years earlier. That is a different income definition and timing from Marketplace assistance. Identify both the income year and the premium year, and check whether a qualifying life event permits reconsideration.",'finding':'P08'},
{'id':'A6.3','sha256':'72da8c2a258c6c205a225af7f8d469bac8d82876c2858d4c3e5e114e0d5ae240','mode':'append','text':'For this exception through an employer plan, the payments must begin after separation from that employer. An IRA does not have that employment-separation requirement. Verify the route for the account you intend to use before starting the series.','finding':'P09'},
{'id':'A7.4','sha256':'9f1849504e3b5502826cc54a18051d80ad213c8c8409c41e0940e85a6c80b616','mode':'append','text':'Coin control selects transaction outputs; it does not, by itself, establish which tax lots you have legally identified. A consolidation can combine several purchase histories into one output. Keep the acquisition records and any required timely identification alongside the transaction history.','finding':'P10'},
{'id':'8.1','sha256':'ffdee9804fbcd4fb7fcfc0fcd1b7be58b4e76893f4162b4205b84313f0b5b1cb','mode':'replace','text':'A financial power of attorney names someone to act under its terms while you are alive. For incapacity planning, confirm that it is durable, when it takes effect, and which powers it actually grants. Healthcare decisions use separate authority. After death, the estate, trust and beneficiary processes apply instead. One person can hold several roles, but each role needs its own authority.','finding':'P11'}]

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode()
def original(path):
    return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)
def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def once(text,before,after):
    if text.count(before)!=1: raise ValueError('Unexpected bounded edit source: '+before[:60])
    return text.replace(before,after,1)
def put(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def catalog():
    return runpy.run_path(str(ROOT/'tools/guided_course.py'))['catalog'](ROOT)
def chapter_note(text,num,note):
    pattern=r'(^#### Chapter '+str(num)+r' — [^\n]+\n)(.*?)(?=^#### |^### |\Z)'
    found=list(re.finditer(pattern,text,re.M|re.S))
    if len(found)!=1:raise ValueError('Chapter owner differs: '+str(num))
    m=found[0]
    return text[:m.start()]+m.group(0).rstrip()+'\n\n**Technical check before filming:** '+note+'\n\n'+text[m.end():]

CHAPTER_NOTES={
'W04':{
3:'Desk review supports the instrument distinctions, not an exact cash-access promise. When TreasuryDirect is the chosen route, verify new-issue transfer holding requirements and the sale route; distinguish deposit insurance from money-market-fund protection. See report S15–S17.',
5:'P01/P03: Verify that IRA assets are not used for a personal borrowing transaction. Distinguish HSA contribution eligibility, substantiated medical reimbursement and later nonmedical distributions. Do not assume every expense predating the HSA is reimbursable, or that age 65 makes nonmedical distributions tax-free. Apply current 2026 coverage rules when relevant; no new member account or transaction is assumed.',
6:'P02: Confirm the qualified Roth condition and actual account type. Workplace pretax deferral is not an additional personal IRA deduction. Preserve equal-household-cost versus equal-contribution comparisons and the existing current cash-flow reconciliation.'},
'W05':{
2:'P10: A UTXO choice or consolidation does not alone establish tax-lot identification. Preserve acquisition histories and the current quantity. Use the actual asset/custody/year identification rules; do not treat the 2026 broker relief as an unhosted-wallet default.',
4:'P04: Show gross distribution, amount actually reaching Roth, withholding and external replacement/tax cash separately. For IRA basis, gather the owner\'s combined relevant Traditional/SEP/SIMPLE IRA values and Form 8606 history; do not aggregate spouses or substitute one selected account. Preserve RMD exclusion and actual early-access conditions. Unsupported calculations remain a labeled reviewed worksheet, not a claimed app result.',
5:'P05: Check substantially identical replacement activity in the owner\'s IRA/Roth IRA and other relevant accounts before a securities harvest. The IRA replacement exception can permanently lose the loss deduction. Preserve the distinction between directly held Bitcoin, funds and other securities; no universal immediate-repurchase rule.'},
'W06':{
2:'P06/P09: Own Social Security delayed credits stop at 70; household/survivor rules are separate. Employer-plan SEPP begins after separation from that employer; IRA SEPP has no such employment condition. Verify the exact person, dates, plan permission, method, modification rules and RMD applicability before claiming a funded access route.',
3:'P07/P08: Use actual active-employment coverage end, Part B window, Part A effective date and HSA-eligible months. COBRA/retiree coverage does not extend the usual active-employment enrollment protection. Marketplace MAGI and IRMAA use different definitions/timing. For 2026, apply actual eligibility and full excess-APTC reconciliation without an old repayment cap. Do not reuse expired enhanced-assistance assumptions. Verify the new HSA coverage provisions separately. None of this establishes that the app calculates an unmodeled credit or premium.'},
'W08':{
1:'P11: Verify durability, effective authority and granted powers of the actual POA under applicable law. Keep nominations, executed documents, appointment, provider acceptance, beneficiary directions and technical access separate; this script and the family worksheet confer no legal authority.'}}
REFS={
'4.5':'P01/P03; S1, S3, S4. Distinguish a pledged-portion deemed distribution from the separate loss-of-IRA-status rule. HSA later nonmedical use is taxable; Medicare eligibility months and 2026 coverage changes need the exact facts.',
'4.6':'P02; S1, S14. The ordinary Roth IRA qualification description does not replace other qualifying events or IRA contribution/conversion ordering. Workplace nonqualified Roth distributions follow their own rules.',
'5.4':'P04; S2, S8. Verify Form 8606 definitions/year-end values per owner, relevant distribution amounts, withholding, valid rollover replacement and additional-tax exceptions. Source illustrations are not actual tax liabilities.',
'A5.2':'P05; S5–S7. Securities IRA replacement losses differ from the normal taxable replacement-basis deferral. Temporary 2026 broker identification relief is conditional and does not validate a later app dropdown selection.',
'6.2':'P06; S11. Own-benefit delayed credits do not continue past 70. Separate current household, survivor, pension, Medicare and access rules.',
'6.3':'P07; S4, S12. Verify the normal eight-month Part B window and any applicable other enrollment route, actual Part A effective date and HSA eligibility. Never prescribe six months before every person\'s 65th birthday as a universal HSA stop date.',
'A6.1':'P08; S13. Use actual household composition and coverage-year MAGI. IRMAA generally uses AGI plus tax-exempt interest from two years before. The 2026 PTC review must include full excess-advance-credit repayment and current eligibility; no app coverage calculation is certified.',
'A6.3':'P09; S10. SEPP method, actual dates, account identity and employer separation must be verified. The existing exact-birthday examples demonstrate duration only, not an approved distribution schedule.',
'A7.4':'P10; S7, S26. This is a cross-check between output selection and tax identification; not a claim that each output is a unique tax lot or that a self-transfer resets basis. Preserve metadata privacy and the actual device procedure.',
'8.1':'P11; S28. Durability and scope need applicable state law and the actual instrument. No estate document, authority or institution acceptance was created or approved.'}

def apply():
    if blob((ROOT/'tools/guided_course.py').read_bytes())!=GENERATOR:raise ValueError('Generator moved')
    rows=catalog();by={r['id']:r for r in rows}
    if len(rows)!=76:raise ValueError('Inventory moved')
    prior={r['path']:(ROOT/r['path']).read_bytes() for r in rows}
    for path,data in prior.items():
        if data!=original(path):raise ValueError('Unexpected canonical pre-edit')
    for edit in EDITS:
        row=by[edit['id']];path=row['path'];text=(ROOT/path).read_text()
        m=re.search(r'^### Read aloud\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S)
        if not m:raise ValueError('Missing speech')
        candidates=[p.strip() for p in m.group(1).strip().split('\n\n') if hashlib.sha256(p.strip().encode()).hexdigest()==edit['sha256']]
        if len(candidates)!=1:raise ValueError('Speech hash mismatch '+edit['id']+' '+edit['finding'])
        before=candidates[0];after=before+'\n\n'+edit['text'] if edit['mode']=='append' else edit['text']
        text=text[:m.start(1)]+once(m.group(1),before,after)+text[m.end(1):]
        put(path,text)
    for lid,note in REFS.items():
        path=by[lid]['path'];t=(ROOT/path).read_text();link='../../delivery/professional-topic-review.md' if '/advanced/' in path else '../delivery/professional-topic-review.md'
        block='### Source-based technical check — not spoken\n\nSeptember 8, 2026: '+note+' See [the technical review]('+link+'). These are source-backed clarifications; licensed sign-off, actual inputs and execution remain separate.\n\n'
        t=once(t,'### Member checkpoint',block+'### Member checkpoint');put(path,t)
    for lid,notes in CHAPTER_NOTES.items():
        path=by[lid]['path'];t=(ROOT/path).read_text()
        for num,note in notes.items():t=chapter_note(t,num,note)
        put(path,t)
    expected={by[x]['path'] for x in set(REFS)|set(CHAPTER_NOTES)}
    actual={p for p in prior if (ROOT/p).read_bytes()!=prior[p]}
    if actual!=expected:raise ValueError('Targeted scope mismatch')
    for p in prior:
        before=prior[p].decode();after=(ROOT/p).read_text()
        for field in ('Gate','Kind','After lesson','Use when','Complete before','Return to'):
            pat=r'^'+re.escape(field)+r':.*$'
            if re.findall(pat,before,re.M)!=re.findall(pat,after,re.M):raise ValueError('Metadata or approval changed: '+field)
    for lid in ('2.3','W02','D07','W03'):
        if (ROOT/by[lid]['path']).read_bytes()!=prior[by[lid]['path']]:raise ValueError('Protected reference changed')
    for path in ('README.md','FINALIZATION-STATUS.md','HANDOFF.md'):
        t=(ROOT/path).read_text();lines=t.splitlines(keepends=True)
        notice='\n**Source-based technical review — September 8, 2026:** The tax, account-access, healthcare, lending, custody and estate/insurance topic check is documented in [the review packet](delivery/professional-topic-review.md). Sixteen bounded edits clarify ten lessons, with paired recording checks. The factual desk review is complete; licensed sign-off, actual app/device evidence and service-scope classification are not claimed. Existing publication gates remain unchanged.\n'
        put(path,lines[0]+notice+''.join(lines[1:]))
    t=(ROOT/'PRIMARY-SOURCES.md').read_text()
    t+='\n\n## Full topic desk review — September 8, 2026\n\n[Technical accuracy and professional-review packet](delivery/professional-topic-review.md) records the current source version, topic coverage, P01–P11 clarifications, dated 2026 checks, source applicability conflicts, independent arithmetic and exact remaining review requests. It distinguishes sources from editorial inference and actual licensed approval. Earlier timestamps above remain historical; they are not silently refreshed as evidence of newly checked content. No professional gate is marked passed by this addition.\n'
    put('PRIMARY-SOURCES.md',t)
    print('Applied 16 bounded speech edits in 10 lessons and chapter checks in 4 walkthroughs; no gate/route/inventory changes.')

def arithmetic():
    getcontext().prec=40;rows=[]
    def c(name,v,w,t=D('.01')):
        assert abs(v-D(str(w)))<=t,(name,v,w)
        rows.append({'check':name,'result':str(v),'expected':str(w),'tolerance':str(t),'status':'PASS'})
    c('Reserve target',D(7200)*6,43200);c('Reserve gap',D(43200)-32000,11200);c('Reserve months',D(11200)/500,22.4)
    c('Employee annual',D(155000)*D('.06'),9300);c('Employee monthly',D(9300)/12,775);c('Employer monthly',D(775)/2,387.5)
    c('Available claims',D(500)+1200,1700);c('Total card payment',D(405)+1200,1605)
    c('Current DTA',D(444500)/1996000,D('.222695390781563126'),D('.000000000001'))
    c('Partial stress DTA',D(444500)/1217200,D('.3651823858034834'),D('.000000000001'))
    c('Down-first sequence',((D(1000000)-50000)*D('.8')-50000)*D('1.25'),887500)
    c('Up-first sequence',((D(1000000)-50000)*D('1.25')-50000)*D('.8'),910000)
    rate=D('.08')/12;payment=D(20000)*rate/(1-(1+rate)**(-60))
    c('Amortizing payment',payment,'405.52788576827365');c('Amortizing interest',payment*60-20000,'4331.673146096419');c('Interest-only total',D(20000)*D('.08')*5,8000)
    for cost,gain in [(58000,8400),(16000,16800),(52000,9600)]:c('Same BTC sale '+str(cost),D(20000)-D('.2')*cost,gain)
    c('Traditional equal-budget',D(1000)*2*D('.8'),1600);c('Roth equal-budget',D(1000)*D('.8')*2,1600)
    for rate,want in [('.2',60000),('.3',54000),('.1',66000)]:c('No-conversion total '+rate,D(30000)*2*(1-D(rate))+D(6000)*2,want)
    c('Cash jobs',D(60000)+40000,100000);c('Revised stock residual',D(1000000)-500000-200000,300000)
    c('Accrued LTV',D(25000)*D('1.12')/50000,D('.56'))
    c('Price room',1-(D(25000)*D('1.12')/D('.8'))/100000,D('.65'))
    c('Repayment response',D(28000-3000)/50000,D('.5'));c('Collateral response',D(28000)/(50000+6000),D('.5'))
    c('Repeated debt',(D(20000)*D('1.1')+20000)*D('1.1'),46200)
    c('Combined health cost',D(2000)+1500,3500);c('Combined health rate',D(3500)/10000,D('.35'))
    c('UTXO fee lower',D(500)*2,1000);c('UTXO fee higher',D(500)*20,10000)
    assert len(rows)==34
    return {'scope':'Independent recomputation of 34 selected teaching identities; no financial-model or professional certification.','precision':40,'checks':rows}

def package(out):
    out.mkdir(parents=True,exist_ok=True)
    for name in ('ALL-SCRIPTS.md','DICTATION-ORDER.md','ADVANCED-DICTATION-ORDER.md','FILM-ORDER.md','FINALIZATION-STATUS.md','PRODUCTION-CHECKLIST.md','PRIMARY-SOURCES.md'):
        shutil.copy2(ROOT/name,out/name)
    shutil.copy2(ROOT/'delivery/professional-topic-review.md',out/'Professional_Topic_Review.md')
    (out/'independent-arithmetic.json').write_text(json.dumps(arithmetic(),indent=2)+'\n')
    work=out/'Walkthroughs';work.mkdir(exist_ok=True)
    for p in (ROOT/'scripts/working').glob('*.md'):shutil.copy2(p,work/p.name)
    (out/'BUILD-IDENTITY.json').write_text(json.dumps({'commit':git('rev-parse','HEAD').strip(),'tree':git('rev-parse','HEAD^{tree}').strip(),'source_base':BASE,'scope':'Source-checked educational material; not licensed sign-off or app/device certification.'},indent=2)+'\n')
    print('Packaged current reading sources, topic report, all walkthroughs and 34 independent arithmetic checks.')
if __name__=='__main__':
    if sys.argv[1]=='apply':apply();arithmetic()
    elif sys.argv[1]=='package':package(Path(sys.argv[2]))
    else:raise ValueError('Unknown action')
