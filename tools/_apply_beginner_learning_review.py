#!/usr/bin/env python3
"""One-use literal teaching edit and simulated-review documentation.

No model calls, live app, financial operations or learner outcomes are produced.
Remove this file and its two data modules and branch-write workflow before merge.
"""
from pathlib import Path
import collections, hashlib, json, re, runpy, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
BASE='0f26cbd5556664776531b50ff11735ae5860c8b0'
GUIDED_BLOB='100dff910e320e37ea5091391917e603b3dab895'
RESERVE='scripts/02-3_size-the-reserve-for-the-job-it-has-to-do.md'
PROTECTED=[RESERVE,'scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md','scripts/working/D07_prove-a-wallet-backup-with-a-safe-test-setup.md']

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode()
def old(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT).decode()
def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def put(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def replace_section(text,name,new):
 pattern=r'(^### '+re.escape(name)+r'\s*\n)(.*?)(?=^### |\Z)'
 if len(re.findall(pattern,text,re.M|re.S))!=1:raise ValueError('Missing section '+name)
 return re.sub(pattern,lambda m:m.group(1)+'\n'+new.strip()+'\n\n',text,count=1,flags=re.M|re.S).rstrip()+'\n'
def once(text,before,after):
 if text.count(before)!=1:raise ValueError('Ambiguous source '+before[:90])
 return text.replace(before,after,1)

def report(changes,practice,rows):
 text='''# Decision-learning review — simulated adult beginner

**September 9, 2026. This is an author-assisted simulation and editorial review, not a participant study or an app test.** The audience is an adult Bitcoin holder who prefers roughly sixth-grade reading complexity, uses a calculator and does not already know financial-planning vocabulary. This is not a child persona, an intelligence judgment or a verified reading-grade score.

## What was actually tested

The current spoken reading copy was matched to GitHub main at `0f26cbd5556664776531b50ff11735ae5860c8b0`: ALL-SCRIPTS blob `4867cb32100811861a9c5be31a093b6e68a4c7a8`. Its 65 lesson texts and the 11 practical plans were available for the review. The main learning order and situation routes are unchanged.

The review asks whether a beginner has the information needed to understand a decision, apply it with different facts and explain a sensible next step. Thirteen constructed practice cases cover the main decision chain and high-impact distinctions. They are not thirteen participants or observed attempts. The explanations in the answer checks are authored examples of supported reasoning, not quotes from a real learner. The same assistant edited and reviewed the material; this is not blind or independent evaluation.

A simulated beginner question is useful for finding a skipped step. It cannot establish what an actual person will understand, finish or do. No percentage pass rate, comprehension score, completion time, participant testimony or claim of sixth-grade accessibility is reported.

## Main finding

The course often already explains why decisions differ. Its remaining weakness was the transition from a fully supplied example to the member's own information: some words appeared before their meaning, some percentages were given without showing the simple operation, and some closing tasks checked a completed record more than the reasoning behind the choice. The answer is a targeted edit and short practice, not another full rewrite or stripping out material qualifications.

The user should learn how to choose, not learn to reproduce the Reeds. A current plan that fits, a different allocation, a smaller conversion and a decision not to borrow can all be sensible outcomes. Essential bills without funding, the same cash assigned twice, an unsupported tax cost or unverified account access are not matters of preference to wave away.

## Constructed beginner questions and the response

| Possible beginner question — not participant testimony | Finding in the prior text | Edit or retained support |
|---|---|---|
| “Do I need the same accounts and percentages as Alex and Morgan?” | The orientation said follow the reasoning, but applying the example could still sound like matching its result. | 0.1 now states that answers may differ and calculator use is expected. 4.3 asks for the member's purpose and comparison, not a copied mix. |
| “What are gross pay, an IRA and a contribution?” | Several terms arrived before the later detailed explanation. | Introduce the short meaning at the relevant first task. Existing account rules remain in place; there is no long prerequisite glossary. |
| “How did six percent become $775?” | The monthly answer appeared without all calculation steps. | 1.3 shows percent-of-salary, annual contribution and division by twelve. 1.5 also explains the simulation percentage without treating it as a guarantee. |
| “Why does 50% LTV reach 80% after a 37.5% price fall?” | The result was stated more readily than the steps. | 3.2 uses $50,000 debt, $100,000 collateral and the $62,500 threshold value to show the arithmetic. Actual contract thresholds are still separate. |
| “Do I open Reserve, Bridge and Forever accounts?” | The timeframes could be mistaken for tax account categories. | 4.3 explicitly separates when money is used from where it is held. The same account can contain different spending jobs. |
| “If early years are short, do you mean few years or too little money?” | 4.4 used an ambiguous phrase. | It now says not enough usable money. The task is to address that funding shortage, not always maximize retirement contributions. |
| “Is the gain the tax bill?” | 5.1 already said no, but led with three fractional Bitcoin lots. | Put the existing simple sale-minus-basis example first, define proceeds, then keep the three-lot comparison. The new $8,000/$5,000 task checks the distinction with different numbers. |
| “Does a higher bracket raise tax on all my money?” | The explanation used layers without a numerical step. | Add a clearly invented two-step tax example, not current tax brackets. Preserve the actual interactions and source checks. |
| “The Roth is bigger. Why isn't that enough?” | The opportunity-cost example is already useful. | Keep the example and technical safeguards. Add a current-cash limit case so the learner must count the money paying tax and accept a smaller/no-conversion choice when appropriate. |
| “Which health cost is the premium and which one changes when I need care?” | The coverage lesson named several costs at once. | Define premium, deductible, copayment, coinsurance and network next to the comparison. Keep all Medicare, HSA and coverage limitations. |
| “What does terminal balance or assumption sensitivity mean?” | These phrases make a useful comparison sound more technical than it is. | 6.7 uses money left at the end and dependence on assumed returns. 6.8 separates the review trigger from the spending choice. |
| “I copied the example. How do I know I learned the method?” | Existing checks often asked for the finished record. | Add thirteen changed-facts/self-check exercises in the existing checkpoints and connect nine walkthroughs to them. 10.2 ends with a new circumstance and asks the member how to begin the next decision. |

## How to use the practice

Read the lesson first. Attempt the small case with the reasoning hidden. A calculator is allowed. Then open the explanation and compare the reasoning, not just the number. The changed circumstance is a second opportunity to apply the principle. Finally, use the member's own facts in the existing worksheet or actual app task.

These cases deliberately separate a calculable limit from a personal preference. A $1,000 budget with $300 assigned leaves $700; that arithmetic is fixed. Whether $300 is the right Reserve contribution is a household decision requiring the facts taught in the unchanged Reserve lesson. Likewise, a toy tax example explains layers but supplies no actual tax advice or forecast.

The answer check states when information is deliberately insufficient. It is correct to say that proceeds and basis alone do not determine a tax bill, or that a proposed earlier retirement cannot be declared funded without the actual result. That does not make “ask a professional” the answer to every question. The learner still completes the comparison, identifies the missing fact and knows why it matters.

## What remains harder than the simple exercises

The financing menu, account rules, early-retirement access and combined tax/healthcare effects still need paced visuals and the situation-specific lessons when applicable. A fifth or sixth unfamiliar term in a spoken block may overload a real learner even after a clear definition. Do not force all sentences to the same short length or delete a consequential condition to lower a score.

An actual member must be able to identify the decision, find the relevant source, use the app and interpret the result. This pass does not exercise the redesigned UI, connect an account, save a plan, calculate a real tax liability, test a wallet, prove notification delivery or create a member's retirement plan. W01–W10 and D07 retain their actual capture holds. The fixed Reed fixture remains uncalibrated for those purposes.

## Targeted source checks for the new plain-language definitions

Read September 9, 2026. These checks support meanings, not an actual policy, product recommendation or a refreshed audit of every professional rule:

- IRS, Federal income tax rates and brackets: https://www.irs.gov/filing/federal-income-tax-rates-and-brackets . The numerical two-step example in 5.3 is invented; no actual bracket amount is taken from it.
- HealthCare.gov glossary: https://www.healthcare.gov/glossary/deductible/ ; https://www.healthcare.gov/glossary/co-payment/ ; https://www.healthcare.gov/glossary/co-insurance/ ; https://www.healthcare.gov/glossary/out-of-pocket-maximum-limit/ . Policy-specific exceptions and limits still need the actual documents.
- Investor.gov, Exchange-Traded Products Providing Exposure to Bitcoin and Ether: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/ETPBulletinSeptember2024 . A spot product's shares and directly controlled Bitcoin are different holdings; no new fund recommendation or Investment Company Act protection is implied.

All prior source-based technical-review sections remain byte-identical. The current IRA prohibited-transaction, qualified Roth, conversion withholding/pro-rata, HSA, Medicare, Social Security, securities loss, early-access, custody and legal-authority qualifications are preserved. The accepted Reserve, W02, D07, original sources, fixed fixture, toolkit, existing tests and capture register are not changed.

## Interpretation of this review

The written course now gives a more explicit route from the example to a member's own decision. The arithmetic and the presence of that explanation can be checked. Actual sixth-grade-level comprehension and successful independent plan building cannot be established by this simulation. The next real trial should use the same hidden-answer prompts with adults who did not help write the course, then the approved app, recording where help is needed.

There is no claim that 65 lessons each passed a measured comprehension test. The coverage table below records the current lesson and whether this pass changed its wording or practice. Unchanged means retained, not certified. Specific practice cases follow; they remain illustrative and do not alter the Reed dataset.

## Coverage of the current manuscript

| Lesson | Review focus / lesson | Change in this pass |
|---|---|---|
'''
 for r in rows:
  if r['id'] in ('W01','W02','W03','W04','W05','W06','W07','D07','W08','W09','W10'):continue
  kinds=[]
  if r['id'] in changes:kinds.append('Targeted spoken edit')
  if r['id'] in practice:kinds.append('Different-case practice')
  if r['id']=='2.3':kinds=['Accepted reference; byte-identical']
  text+=f"| {r['id']} | [{r['title']}](../{r['path']}) | {'; '.join(kinds) if kinds else 'Existing explanation retained; real learner evidence pending'} |\n"
 text+='\n## Constructed practice cases and reasoning\n\nThese are authored prompts and explanations, not recorded participant dialogue. Each case is intentionally separate unless it explicitly reuses a lesson example.\n'
 for lid,(problem,task,reason,changed,apply) in practice.items():
  text+=f'\n### {lid}\n\n**Practice facts:** {problem}\n\n**Attempt before reading the explanation:** {task}\n\n**Reasoning check:** {reason}\n\n**Change one circumstance:** {changed}\n\n**Apply to your own decision:** {apply}\n'
 return text

def apply():
 tool=runpy.run_path(str(ROOT/'tools/guided_course.py'));rows=tool['catalog'](ROOT);by={r['id']:r for r in rows}
 if len(rows)!=76:raise ValueError('Active inventory changed')
 if blob((ROOT/RESERVE).read_bytes())!='2c107a394a93cc877c73f011dfe37fb5ad3d94b1':raise ValueError('Reserve differs')
 for r in rows:
  if r['text']!=old(r['path']):raise ValueError('Preexisting canonical edits')
 edits=runpy.run_path(str(ROOT/'tools/_beginner_learning_edits.py'))['EDITS']
 p=runpy.run_path(str(ROOT/'tools/_beginner_learning_practice.py'));practice=p['PRACTICE'];walk=p['WALKTHROUGH_PRACTICE']
 changes=collections.Counter();new_reads={r['id']:r['read'] for r in rows}
 for lid,before,after in edits:
  if lid not in by or not by[lid]['read'] or lid=='2.3':raise ValueError('Invalid target')
  try:new_reads[lid]=once(new_reads[lid],before,after)
  except ValueError as e:raise ValueError(lid+': '+str(e))
  changes[lid]+=1
 for lid in set(changes)|set(practice):
  r=by[lid];t=replace_section(r['text'],'Read aloud',new_reads[lid]) if lid in changes else r['text']
  if lid in practice:
   problem,task,reason,changed,own=practice[lid]
   extra='''\n\n#### Try a different case\n\nThese are practice facts, not another part of the Reeds' plan. Use a calculator as needed. Try the question before opening the reasoning.\n\n'''+problem+'\n\n**Your question:** '+task+'\n\n<details>\n<summary>Check the reasoning</summary>\n\n'+reason+'\n\n</details>\n\n<details>\n<summary>Now change one circumstance</summary>\n\n'+changed+'\n\n</details>\n\n**Use your own plan:** '+own
   t=replace_section(t,'Member checkpoint',r['checkpoint']+extra)
  t=re.sub(r'^Status: [^\n]*','Status: SPOKEN_EDIT_REVIEW — targeted decision-learning edit and/or member practice; owner review, real learner testing and capture remain separate.',t,count=1,flags=re.M)
  put(r['path'],t)
 for lid,(lesson,note) in walk.items():
  r=by[lid]
  add='\n\n### Apply the lesson with different facts — production guidance\n\n'+note+'\n\nUse the existing Member checkpoint in the linked teaching script; no second workbook is needed. Let the learner attempt the question before showing its explanation. A valid alternative needs a reason and workable funding, not the example household\'s settings. Do not record a simulated attempt as a real member outcome.\n\nPrepared narration cue: “Before we copy any numbers, explain the choice you are making. Which facts in your situation matter? Compare the alternative you would actually consider, then read what it changes.”\n\nPrimary checkpoint: ['+lesson+'](../../'+by[lesson]['path']+'). The app\'s actual fields, results, access and saved-state behavior retain their existing checks.'
  put(r['path'],r['text']+add)
 # Verify every previous nonspoken technical-check section and especially sensitive paragraphs survive.
 for r in rows:
  now=(ROOT/r['path']).read_text()
  prior=tool['section'](r['text'],'Source-based technical check — not spoken')
  if prior and tool['section'](now,'Source-based technical check — not spoken')!=prior:raise ValueError('Technical review changed '+r['id'])
  for para in r['read'].split('\n\n'):
   if any(s in para for s in ["For an IRA, don't use",'Withholding tax from the IRA','Required distributions must be satisfied separately','For ordinary retirement use, qualified Roth IRA','For tax-free reimbursement','Once you\'re Medicare-eligible','Applying for premium-free Part A','delayed retirement credits stop at 70','For incapacity planning, confirm that it is durable']):
    if para not in now:raise ValueError('Consequential qualification changed '+r['id'])
 for path in PROTECTED:
  if (ROOT/path).read_text()!=old(path):raise ValueError('Protected reference changed')
 actual=set(git('diff',BASE,'--name-only','--','scripts').splitlines())
 expected={by[x]['path'] for x in set(changes)|set(practice)|set(walk)}
 if actual!=expected:raise ValueError('Canonical scope differs')
 g=ROOT/'tools/guided_course.py'
 if blob(g.read_bytes())!=GUIDED_BLOB:raise ValueError('Generator moved')
 text=g.read_text()
 anchor="    return {'scope':'Arithmetic teaching checks only; no retirement forecast, tax opinion, lender assurance or model acceptance.'"
 checks="""    # Separate beginner practice cases. These are not Reed facts or app outputs.
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
"""
 if text.count(anchor)!=1:raise ValueError('Arithmetic return moved')
 put('tools/guided_course.py',text.replace(anchor,checks+anchor,1))
 put('delivery/decision-learning-review.md',report(changes,practice,rows))
 for path in ['README.md','FINALIZATION-STATUS.md']:
  t=(ROOT/path).read_text();title,rest=t.split('\n',1)
  notice='\n\n**Decision-learning pass — September 9, 2026:** Targeted plain-language explanations and thirteen different-case practice exercises now support applying the lessons to a member\'s own facts. [Simulated beginner review](delivery/decision-learning-review.md). This is an author-assisted written review, not a real participant study, verified sixth-grade reading score, live app test or claim that someone completed a retirement plan. Existing source-based technical corrections and actual capture holds remain.\n'
  put(path,title+notice+rest)
 t=(ROOT/'HANDOFF.md').read_text();title,rest=t.split('\n',1)
 notice='''\n\n## Current continuation — decision learning, not copying the example

Austin asked to move forward with teaching how to decide and to simulate an adult beginner at roughly a sixth-grade reading level. This pass changes specific explanations, adds thirteen practice cases with reasoning checks and changed circumstances in existing Member checkpoints, and connects nine practical plans to their use. The first-pass facts and the answer checks are clearly authored, not a transcript of real participants. No simulated result is entered as member validation or app evidence.

The [decision-learning review](delivery/decision-learning-review.md) records scope, concerns, exact case assumptions, source checks and remaining limitations. It does not reset the course or add a workbook. Different justified choices, including keeping the current plan, are acceptable. The accepted Reserve, W02, D07, original sources, fixed fixture, toolkit, technical review sections and existing capture register stay unchanged. The YouTube script remains a delivery reference only; no return, withdrawal, tax or account-lockup formula is imported.

Read the revised section and its Member checkpoint together. Explanations should supply the reasoning before a task asks the member to apply it. Hidden-answer questions in the reading artifact are practice, not a certification exam. When tested with actual learners later, record assistance and errors rather than infer understanding from matching a sample allocation. Actual app routes, financial calculations, safe device procedures and owner voice approval remain separate.

### Earlier completed passes, retained as history
'''
 put('HANDOFF.md',title+notice+rest)
 # Persist a factual change list for subsequent local QA; no grading of human ability.
 record={'base':BASE,'kind':'author-assisted simulated written review; not participant or live app evidence','spoken_replacements':sum(changes.values()),'spoken_lesson_ids':list(changes),'practice_lesson_ids':list(practice),'walkthrough_ids':list(walk),'protected':PROTECTED,'inventory_teaching':65,'inventory_practical':11}
 put('delivery/decision-learning-changes.json',json.dumps(record,indent=2))
 print(json.dumps(record,indent=2))

def export(out):
 out.mkdir(parents=True,exist_ok=True)
 tool=runpy.run_path(str(ROOT/'tools/guided_course.py'));rows=tool['catalog'](ROOT)
 p=runpy.run_path(str(ROOT/'tools/_beginner_learning_practice.py'))
 data={'identity':{'commit':git('rev-parse','HEAD').strip(),'tree':git('rev-parse','HEAD^{tree}').strip(),'base':BASE},'rows':rows,'member_order':tool['member_order'](rows),'practical_ids':tool['PRACTICAL_IDS'],'situational_ids':tool['ADV_IDS'],'practice':p['PRACTICE']}
 (out/'REVIEW-DATA.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
 for name in ['ALL-SCRIPTS.md','DICTATION-ORDER.md','FILM-ORDER.md','COURSE-MANIFEST.json','ARITHMETIC-CHECKS.json','FINALIZATION-STATUS.md','CAPTURE-RECEIPTS.md','PRODUCTION-CHECKLIST.md','delivery/decision-learning-review.md','delivery/decision-learning-changes.json']:
  d=out/name;d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes((ROOT/name).read_bytes())
 for r in rows:
  d=out/r['path'];d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes((ROOT/r['path']).read_bytes())
 print('Exported exact course sources and review data; no secrets, external assets or fonts.')

if __name__=='__main__':
 if sys.argv[1:] == ['apply']:apply()
 elif len(sys.argv)==3 and sys.argv[1]=='export':export(Path(sys.argv[2]))
 else:raise SystemExit('Use apply or export OUTPUT_DIR')
