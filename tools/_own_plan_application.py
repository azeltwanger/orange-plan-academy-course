#!/usr/bin/env python3
"""Remove the separate homework layer; keep decision teaching and real application.
Temporary repository integration helper. Does not operate the Orange Plan app.
"""
from pathlib import Path
import sys,re,json,subprocess,hashlib,runpy,html,shutil
ROOT=Path.cwd().resolve()
BASE='26be5dbabbfcfa0c95d9bcead8a41684abcf8f76'
PROTECTED=['source-material','fixtures','toolkit','tests','production','CAPTURE-RECEIPTS.md','PROMOTION-RECORD.json','delivery/professional-topic-review.md','scripts/02-3_size-the-reserve-for-the-job-it-has-to-do.md','scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md','scripts/working/D07_prove-a-wallet-backup-with-a-safe-test-setup.md','tools/guided_course.py']
ACTIONS={
'1.5':"Open your current result in Orange Plan and look at the first year you expect to stop or reduce work. Check where the spending money comes from. If a figure is wrong, correct its source; if you want to test a different choice, compare it without replacing your current plan first.",
'2.1':"Review your own income, spending, debt payments and existing saving in Cash Flow. Include annual bills and check that payroll saving and credit-card payments have not been counted twice. Use the amount genuinely left over for the decisions in the next lessons; if there is a shortfall, keep it visible.",
'3.3':"Review each of your debts and choose whether to keep the required payment, pay extra, or compare a change. Check the total extra payments against the money left after the Reserve contribution you chose. Only redirect a payment once it has actually ended.",
'4.3':"Use your own holdings and spending dates to build the portfolio in Orange Plan. Work out what the Bitcoin and non-Bitcoin money needs to provide, then compare the investments and amounts that fit those uses. Keep your current mix when it already fits; change it when the comparison gives you a reason. Timeframes do not require separate accounts or the same mix in every account.",
'4.7':"Review your contribution plan in Orange Plan. Check the amount available now, the receiving account and what each contribution should buy. Keep future contributions tied to the event that frees up their money. Finish any required payroll, transfer or purchase instruction with the actual provider; saving a plan does not execute it.",
'5.1':"When a taxable sale is relevant to your plan, compare its proceeds, supported purchase cost and resulting gain in Orange Plan. Keep the gain separate from the estimated tax and the cash available afterward. Leave missing purchase information unresolved rather than filling it with zero.",
'5.4':"When a conversion is relevant, compare it with your current plan in Orange Plan while keeping the same spending and investment assumptions. Check the money paying the tax, the cash left for the early years and what each version leaves later. Compare a smaller conversion when useful. Keep the current plan if the change does not help or a needed fact is still missing.",
'6.3':"Use the coverage options actually available to you to update healthcare costs and dates in your plan. Compare premiums, other likely costs and a difficult year's potential bills. Check that the household has money for the costs it would still carry. Exact coverage, enrollment and any calculation the app does not support need their actual source, not an invented app result.",
'6.8':"Review next year's spending and Reserve funding in Orange Plan. Read any proposed adjustment beside the income and withdrawals it changes. Choose an amount that fits the life you intend to fund and the adjustments you could actually make; keeping the current amount can be the right decision.",
'7.4':"Update the existing custody map for your own holdings and the people involved. Keep recovery status accurate and secrets out of the map. Make sure the agreed backup person knows where the legitimate starting instructions are. An actual recovery or security check remains a separate action when needed, not something the app can certify.",
'8.3':"Complete the first instructions your own family would use, using the existing Heir Letter, Executor Packet and custody map. Keep only the information relevant to your household, make the safe starting point findable, and connect any outstanding legal or provider action to the plan. Do not put recovery secrets in the ordinary instructions.",
'9.3':"When your life changes or a number does not look right, open the affected part of Orange Plan and check its source and date. Correct an actual fact or compare an idea separately, then read what changed in the result. No new circumstance needs to be invented for this step; a quiet month can end without a strategy change.",
'10.2':"Review your saved plan and settle the next real action. Keep current and future contributions separate, identify anything still needing confirmation, and set the next review. Share the relevant summary when someone needs it. There is no separate case to solve, explanation to submit, community post or course approval required."
}
GUIDANCE={
'W01':"Use the member's own information throughout the existing setup and result review. Show how to find the source of a surprising number and how to compare a real question without silently replacing Current. Continue when the relevant step is understood and completed; do not insert a second household, quiz or answer-reveal task.",
'W03':"Use the member's own debts, current cash flow and chosen Reserve pace. Apply the existing comparisons only when a financing choice is relevant. The work is making a funded repayment choice in their plan, not reproducing the Reeds' split or passing a separate arithmetic test.",
'W04':"Keep the demonstration's teaching examples, then go directly to the member's holdings, spending dates and contribution plan. Show where their chosen mix and routing affect their own plan. Do not add a separate practice portfolio, require two alternatives when no genuine choice is open, or request a written explanation or submission.",
'W05':"Go directly from the explanation to the member's records and the sale, withdrawal or conversion relevant to their plan. Keep current tax funding and later resources visible in the actual comparison. Missing consequential facts remain specific tasks; professional confirmation must not replace teaching the comparison. No practice sale or case worksheet is required.",
'W06':"Build the member's own retirement paycheck from their spending, income, accounts and coverage dates. Use the actual supported result to compare relevant changes and finish the spending/Reserve decision. Do not insert fictional homework or a score to pass. Unsupported healthcare or contract effects stay clearly separate from app outputs.",
'W07':"Apply the custody explanation to the member's actual arrangements and existing map. Preserve the scoped safe-recovery and security requirements. Remove the extra no-secrets case quiz; an actual check needed to protect the household is implementation, not an academic assignment.",
'W08':"Use the member's own family instructions and existing documents, not a second fictional role-and-contact problem. Keep necessary checks that the instructions can be found and used, and any lawful-authority or coverage prerequisites. No additional workbook, written answer or community submission is required.",
'W09':"Use an actual change or discrepancy when one exists. Otherwise demonstrate the ordinary review and leave the strategy unchanged. Do not manufacture a scenario for completion or ask the member to submit an explanation. The saved plan and necessary outside actions are the work.",
'W10':"Finish by reviewing the member's own saved plan, unresolved facts and next actions. Sharing a relevant summary is useful when another person needs it, not a mandatory oral test. No invented new circumstance, submitted answer, homework or approval gate is added. Actual provider, legal and wallet actions still need their own evidence."
}

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode()
def put(p,t):
 q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(t.rstrip()+'\n',encoding='utf-8')
def once(t,a,b):
 if t.count(a)!=1:raise ValueError('Expected one bounded source match: '+a[:100])
 return t.replace(a,b,1)
def sect(t,h):
 m=re.search(r'^### '+re.escape(h)+r'\s*\n(.*?)(?=^### |\Z)',t,re.S|re.M)
 return m.group(1).strip() if m else ''

def apply():
 rows=runpy.run_path(str(ROOT/'tools/guided_course.py'))['catalog'](ROOT);by={r['id']:r for r in rows}
 originals={r['path']:(ROOT/r['path']).read_text() for r in rows}
 for p,t in originals.items():
  if t!=git('show',BASE+':'+p):raise ValueError('Source moved: '+p)
 seen=[];removed_guidance=[]
 for r in rows:
  p=r['path'];t=originals[p]
  if '#### Try a different case' in t:
   if r['id'] not in ACTIONS:raise ValueError('Unexpected practice block')
   checkpoint=t.split('### Member checkpoint',1)[1]
   if checkpoint.count('#### Try a different case')!=1 or '### ' in checkpoint.replace('#### Try a different case',''):
    if re.search(r'^### ',checkpoint,re.M):raise ValueError('Unexpected later checkpoint section')
   t=t.split('### Member checkpoint',1)[0]+'### Member checkpoint\n\n'+ACTIONS[r['id']]+'\n'
   seen.append(r['id'])
  marker='### Apply the lesson with different facts — production guidance'
  if marker in t:
   if r['id'] not in GUIDANCE:raise ValueError('Unexpected practical guidance')
   tail=t.split(marker,1)[1]
   if re.search(r'^### ',tail,re.M):raise ValueError('Unexpected guidance tail')
   t=t.split(marker,1)[0].rstrip()+'\n\n### Application in the member\'s own plan — production guidance\n\n'+GUIDANCE[r['id']]+'\n'
   removed_guidance.append(r['id'])
  t=t.replace('targeted decision-learning edit and/or member practice; owner review, real learner testing and capture remain separate.','plain-language decision teaching with application in the member\'s own plan; owner review and actual capture remain separate.')
  if t!=originals[p]:put(p,t)
 assert set(seen)==set(ACTIONS) and set(removed_guidance)==set(GUIDANCE)
 p=by['0.1']['path'];t=(ROOT/p).read_text()
 t=once(t,"Use a calculator and pause when you need to. This is not a test of mental math. What matters is knowing which numbers to use, what the result means, and what you would do with it.","Keep Orange Plan open as you work through the course. The walkthroughs show you how to use your own numbers, read the results and make the decision. Pause when you need to; you do not need to do the calculations in your head.")
 t=once(t,"Watch each lesson, then do the matching walkthrough before moving on. Some lessons are marked For your situation. Read the question beside them: when your plan uses that strategy, complete the lesson before relying on it. Otherwise, carry on with the main path. Take a section a week or use a pace that fits your life.","Watch the lesson, follow the walkthrough, and apply it to your own plan in Orange Plan. Some lessons are marked For your situation. Read the question beside them: when your plan uses that strategy, complete the lesson before relying on it. Otherwise, carry on with the main path. Go at a pace that fits your life.")
 put(p,t)
 p=by['10.2']['path'];t=(ROOT/p).read_text()
 start="A financial plan becomes more useful when you can explain it to someone else without opening every calculation. That is the final exercise."
 end="Use the existing Household Plan Summary for that conversation. Keep the supporting calculations nearby, but don't make the summary a copy of every table. It should guide someone into the detail when a question needs it."
 a=t.index(start);b=t.index(end)+len(end)
 replacement="""Your plan is now in Orange Plan. Let's finish by checking what you'll do next and how you'll keep it useful.

Start with the life you're planning for. Does the saved plan reflect when you want to reduce work, what you want to spend, and the other commitments you intend to fund?

Look at the money available now and the years when the funding changes. Use your own amounts. Check that the next contribution goes to the account and investment you chose, and that future contributions begin only when their money becomes available.

If something is unclear, open that part of the plan. A withdrawal should have a source. A proposed change should show what it improves and what you give up. You may find that your current choice still fits. There is no need to change it just to finish a lesson.

When you share finances with someone, use the Household Plan Summary to discuss the decisions that affect both of you. Show what funds the early years, why you chose the investment mix, and which spending could change during a difficult period. You don't have to walk through every calculation.

For anyone who needs to help manage the household, make the relevant starting instructions easy to find. The family handoff section already covers those arrangements; this is not a second rehearsal or another document to complete.

Use the existing summary when sharing is useful. Keep the details in Orange Plan rather than copy every table into a separate explanation."""
 t=t[:a]+replacement+t[b:]
 t=once(t,'Originalvideo deliveryproblem→workthrough→useanswer only, nofinancialformulasborrowed. Actual teach-backbylistener remainsunperformeduntilrecorded. Use existing summaryandactionlist; no newworkbook, serviceentitlement,unlimitedsupportor3kvalueclaim. Verifyprivacybeforeexport and current/futureoutsideexecution.',"The video supplies delivery structure only, not financial formulas. Finish in the member's own saved plan. Sharing is for an actual household or professional purpose, not an oral assessment or completion gate. Use existing materials only; retain privacy and actual-execution distinctions.")
 put(p,t)
 p=by['W10']['path'];t=(ROOT/p).read_text()
 t=once(t,'A listener rehearsal, outside implementation, legal review and capture receipt must actually happen before recorded as successful.','Outside implementation, legal review and capture evidence must exist before recorded as successful. No listener test is required to complete the course.')
 a=t.index('#### Chapter 3 — Have the listener explain the plan back');b=t.index('#### Chapter 4 —',a)
 replacement="""#### Chapter 3 — Finish the plan and share only when useful

**Show and do:** With 10.2, open the member's saved plan and existing summary. Review the next contribution, the first retirement funding period and the next real action. Resolve an actual question in the relevant view rather than introduce an invented scenario. Show the summary for a spouse or helper only when sharing serves that household.

**Narration:**

“Use your own plan here. Check where the next contribution goes and what will pay the bills when work changes. If a number doesn't make sense, open the part that produced it. Then settle the next action. You don't need to copy the example's choices or write a separate explanation.”

**Verify before recording:** Use actual supported views and the matching saved result. Do not claim a real learner completed the plan from this prepared recording. Sharing is optional and requires appropriate consent and privacy; no test score, submission or instructor approval is added.

**Member finish:** The member has reviewed their own plan and identified the next real action. The relevant summary can be shared when needed.

"""
 t=t[:a]+replacement+t[b:];put(p,t)
 intro="**Member application — September 9, 2026:** The separate thirteen practice cases and answer checks have been removed at Austin's direction. The clearer explanations remain. Members learn from the teaching, follow the walkthrough and apply the decision to their own plan in Orange Plan. No separate homework, quiz, required post, submitted explanation or course approval step is part of that flow. [Editorial record](delivery/decision-learning-review.md). Actual app and learner evidence still require real use."
 for p in ['README.md','FINALIZATION-STATUS.md']:
  t=(ROOT/p).read_text()
  t,n=re.subn(r'^\*\*Decision-learning pass[^\n]*',lambda m:intro,t,count=1,flags=re.M)
  if n!=1:raise ValueError('Missing current status in '+p)
  put(p,t)
 p='HANDOFF.md';t=(ROOT/p).read_text();a=t.index('## Current continuation');b=t.index('### Earlier completed passes',a)
 current="""## Current continuation — the member's own plan is the application

Austin explicitly rejected the added exercises and homework. Keep the plain-language explanations and instructor-led examples; remove the separate practice households, answer reveals and changed-facts assignments from the member experience. After teaching, go directly to the member's own decision in Orange Plan.

The thirteen practice blocks are removed from the existing checkpoints. Each now points to the relevant work in the member's actual plan. Nine practical plans no longer detour into a practice case. The final review uses the saved plan and next real actions; it does not require a listener exam, made-up circumstance, written justification, community post or approval to proceed.

Do not replace the removed work with a new workbook or another checklist outside Orange Plan. Use existing member materials only where they do an actual job, such as family instructions. Actual wallet recovery, account security, legal authority and provider instructions still require their appropriate real-world steps; they cannot be certified merely by editing a plan.

The [editorial review](delivery/decision-learning-review.md) keeps the useful beginner-language findings and makes the removed exercise layer historical. The previous PR and commit retain that history; there is no current exercise library. Internal arithmetic checks can remain, but are not assigned to members. Testing should follow a member applying the teaching to their own app plan and identify where the explanation or software blocks progress. No real-user success or sixth-grade accessibility claim is established by this edit.

The accepted Reserve, W02, D07, source materials, fixed fixture, toolkit, source-based technical review and existing tests/capture holds remain unchanged. No app behavior, financial assumption, product preference, provider action or course-platform release is changed.

"""
 t=t[:a]+current+t[b:];put(p,t)
 p='delivery/decision-learning-review.md';t=(ROOT/p).read_text()
 a=t.index('## Targeted source checks for the new plain-language definitions');b=t.index('## Interpretation of this review',a)
 primary=t[a:b].rstrip()
 table=t[t.index('## Constructed beginner questions and the response'):t.index('## How to use the practice')]
 table=table.replace('The new $8,000/$5,000 task checks the distinction with different numbers.','The member applies that distinction to the actual sale being considered in their plan.')
 table=table.replace('Add a current-cash limit case so the learner must count the money paying tax and accept a smaller/no-conversion choice when appropriate.','Use the actual available cash in the member\'s comparison, including a smaller or no-conversion choice when appropriate.')
 table=table.replace('Add thirteen changed-facts/self-check exercises in the existing checkpoints and connect nine walkthroughs to them. 10.2 ends with a new circumstance and asks the member how to begin the next decision.','The separate exercises proposed in PR #24 were rejected and removed. The existing walkthroughs now take the member directly into their own facts, comparison and next action in Orange Plan.')
 review="""# Decision-learning review — application in the member's own plan

## Current owner direction

On September 9, 2026, Austin clarified that applying the teaching in Orange Plan is the exercise. Separate homework, made-up practice cases, hidden answers and submitted explanations add friction and are not part of the program. The thirteen added exercise blocks and the nine walkthrough detours are removed. The final review no longer requires a listener test or a new invented circumstance.

Keep the useful beginner explanations and the instructor's worked examples. Then guide the member to the relevant part of their own plan: enter the facts, compare a choice when needed, understand the result and record the decision. Keeping a current choice is valid when it fits. No separate written rationale, mandatory community post or instructor sign-off is required.

## What the earlier review actually established

PR #24 reviewed the written 65-lesson/11-practical inventory from base `0f26cbd5556664776531b50ff11735ae5860c8b0`. It was an author-assisted editorial simulation, not a real participant study, reading-grade certification or live app test. The same assistant wrote and reviewed the changes. No measured comprehension, completion time or successful personal retirement plan was established.

The useful finding was that some terms and calculations needed clearer first explanations. Those edits remain. The separate exercise proposal is retained only in Git history, including commit `26be5dbabbfcfa0c95d9bcead8a41684abcf8f76`; it is not a current member deliverable.

"""+table+"""## How application works now

The instructor explains a decision and demonstrates how to compare it. The member follows in their own Orange Plan account with their own facts. The existing checkpoint describes that plan-building step; it is not another activity to submit. Actual app fields, calculations and saved-state behavior must be verified in the finished walkthrough. Unsupported behavior is not invented to make a lesson look complete.

Testing the program means observing whether an adult beginner can follow this actual flow, find their information, make a relevant comparison and use the result. Reviewers can record problems internally; members are not given an extra testing curriculum. No score or classroom-style task is required to continue.

The account-access, financing and combined tax/healthcare material still needs paced delivery and appropriate visuals. Keep qualifications that change the decision or prevent a consequential mistake. Necessary real-world actions, such as a safe wallet check, account instruction or family document, remain implementation rather than academic homework. Do not make the member duplicate their financial plan in another worksheet.

"""+primary+"""\n\n## Preservation and evidence

The accepted Reserve, W02 and D07 are unchanged. Prior source-based technical-check sections, original materials, fixed fixture, toolkit, existing tests and capture records remain unchanged. The generator's historical arithmetic identities are internal checks, not student questions. No source-based correction is replaced with unsupported advice or a blanket professional referral.

The current revision removes a layer of work; it does not claim the app was tested, a real learner finished, or a retirement plan was validated. The current member task is their own plan in Orange Plan.
"""
 put(p,review)
 p='delivery/decision-learning-changes.json';rec=json.loads((ROOT/p).read_text())
 rec['historical_practice_lesson_ids']=rec.pop('practice_lesson_ids')
 rec['active_practice_lesson_ids']=[]
 rec['owner_correction']={'base':BASE,'direction':'Remove separate homework; the member applies teaching in their own Orange Plan plan.','removed_exercise_blocks':len(seen),'removed_walkthrough_detours':len(removed_guidance),'keep':'Plain-language explanations, instructor worked examples, technical safeguards and actual implementation tasks.','capstone':'Review the own saved plan and next actions; no listener exam or submission.','internal_checks':'Historical arithmetic identities remain internal, never member homework.'}
 put(p,json.dumps(rec,indent=2,ensure_ascii=False))
 for r in rows:
  old=originals[r['path']];new=(ROOT/r['path']).read_text()
  for h in re.findall(r'^### (.*[Tt]echnical.*)$',old,re.M):
   if sect(old,h)!=sect(new,h):raise ValueError('Technical review changed: '+r['id'])
  for line in old.splitlines():
   if line.startswith('**Technical check before filming:') and line not in new:raise ValueError('Lost filming safeguard')
  if re.search(r'^#### Try a different case|^### Apply the lesson with different facts|<summary>Check the reasoning|<summary>Now change one circumstance',new,re.M):raise ValueError('Exercise remains')
 for p in PROTECTED:
  if git('diff',BASE,'--name-only','--',p).strip():raise ValueError('Protected content changed: '+p)
 changed=[r['id'] for r in rows if (ROOT/r['path']).read_text()!=originals[r['path']]]
 changed_speech=[r['id'] for r in rows if sect(originals[r['path']],'Read aloud')!=sect((ROOT/r['path']).read_text(),'Read aloud')]
 if set(changed_speech)!={'0.1','10.2'}:raise ValueError('Unexpected spoken changes: '+str(changed_speech))
 print(json.dumps({'removed_cases':seen,'removed_detours':removed_guidance,'changed_canonical':changed,'changed_spoken':changed_speech,'course_inventory':len(rows),'notice':'Existing own-plan application only; no app, financial or learner operation performed.'},indent=2))

def export(out):
 tool=runpy.run_path(str(ROOT/'tools/guided_course.py'));rows=tool['catalog'](ROOT);by={r['id']:r for r in rows};order=tool['member_order'](rows)
 out.mkdir(parents=True,exist_ok=True)
 nav=[];sections=[]
 for lid in order:
  r=by[lid];ident='lesson-'+lid.replace('.','-');situ=lid in tool['ADV_IDS'] or lid=='2.5'
  label='For your situation' if situ else 'Main path'
  nav.append('<a href="#'+ident+'">'+html.escape(lid+' · '+r['title'])+'</a>')
  route=''
  if lid in tool['ADV_IDS']:
   v=tool['situation_route'](r);route='<aside>'+html.escape(v['when']+' '+v['before']+' Return to '+v['return'])+'</aside>'
  elif lid=='2.5':route='<aside>Use this lesson when you intend to help fund education. Otherwise continue to Debt.</aside>'
  paras=''.join('<p>'+html.escape(s.strip()).replace('\n','<br>')+'</p>' for s in r['read'].split('\n\n') if s.strip())
  sections.append('<section id="'+ident+'"><div class="label">'+label+'</div><h2>'+html.escape(lid+' — '+r['title'])+'</h2>'+route+paras+'<a class="back" href="#top">Back to contents</a></section>')
 css='''*{box-sizing:border-box}body{margin:0;background:#faf9f6;color:#24211d;font:16px/1.75 system-ui,-apple-system,Segoe UI,sans-serif}header{max-width:74rem;margin:auto;padding:2rem}h1{font-size:2.3rem;line-height:1.2;margin:.5rem 0 1rem}header p{max-width:52rem}main{display:grid;grid-template-columns:19rem minmax(0,48rem);gap:3rem;max-width:74rem;margin:auto;padding:0 2rem 4rem}nav{height:95vh;position:sticky;top:1rem;overflow:auto;font-size:.86rem;padding-right:1rem}nav a{display:block;margin:.5rem 0;color:inherit;text-decoration:none}nav a:hover{text-decoration:underline}article{min-width:0}section{padding:1rem 0 3rem;border-bottom:1px solid #ddd}h2{font-size:1.65rem;line-height:1.3}p{font-size:1.08rem;margin:1rem 0}aside{padding:1rem;background:#f0ede7;font-size:.95rem}.label{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:#655b50}.back{color:inherit;font-size:.9rem}@media(max-width:850px){header{padding:1.2rem}main{display:block;padding:0 1.2rem 3rem}nav{position:static;height:auto;max-height:22rem;border:1px solid #ddd;padding:1rem;margin-bottom:2rem}h1{font-size:1.9rem}h2{font-size:1.4rem}}@media print{nav,.back{display:none}main{display:block;padding:0}section{break-before:page;border:0}header{padding:0}p{font-size:11pt}}'''
 content='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orange Plan — Course Reading Copy</title><style>'+css+'</style></head><body><header id="top"><div class="label">Orange Plan Academy · owner reading copy</div><h1>Learn the decision. Build your plan.</h1><p>Follow the teaching and its walkthrough, then apply it to your own plan in Orange Plan. This copy contains the spoken lessons and situation-specific routing. There are no separate exercises or answer checks.</p><p>Written review copy. Exact app demonstrations, device procedures and owner voice approval remain separate.</p></header><main><nav aria-label="Lesson contents">'+''.join(nav)+'</nav><article>'+''.join(sections)+'</article></main></body></html>'
 (out/'Orange_Plan_Course_Reading_Copy.html').write_text(content)
 for p in ['ALL-SCRIPTS.md','DICTATION-ORDER.md','FILM-ORDER.md','COURSE-MANIFEST.json','HANDOFF.md']:
  (out/p).write_bytes((ROOT/p).read_bytes())
 for r in rows:
  p=out/r['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/r['path']).read_bytes())
 (out/'BUILD-IDENTITY.json').write_text(json.dumps({'commit':git('rev-parse','HEAD').strip(),'tree':git('rev-parse','HEAD^{tree}').strip(),'source':'scripts/','notice':'No separate homework. Source-matched review copy; no app or learner test performed.'},indent=2)+'\n')
 (out/'README.txt').write_text('Open Orange_Plan_Course_Reading_Copy.html for the spoken course. Apply the teaching in your own Orange Plan plan through the existing walkthroughs. No separate practice cases, answer reveals, quizzes or required submissions. scripts/ contains canonical teaching and production notes; it is not additional member homework.\n')
 print('Exported 65 spoken lessons and 11 practical plans without the removed exercise layer.')

if __name__=='__main__':
 if sys.argv[1]=='apply':apply()
 elif sys.argv[1]=='export':export(Path(sys.argv[2]))
 else:raise SystemExit('Expected apply or export')
