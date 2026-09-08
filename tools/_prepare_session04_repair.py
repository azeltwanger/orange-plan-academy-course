#!/usr/bin/env python3
"""One-use synchronization of already-written Allocation review scripts.

No teaching generation, network access, app execution or financial operations.
Remove this helper and its dedicated write workflow before integration.
"""
from pathlib import Path
import hashlib
import subprocess

ROOT=Path(__file__).resolve().parents[1]
BASE='3e54ae3fe2249d588e29d74646c9fae01d1655f9'
EXPECTED={
 'scripts/04-1_read-the-same-portfolio-in-four-useful-ways.md',
 'scripts/04-2_set-a-bitcoin-target-the-household-can-hold.md',
 'scripts/04-3_match-the-money-to-when-you-will-use-it.md',
 'scripts/04-4_build-the-contribution-waterfall-from-one-pool.md',
 'scripts/04-5_choose-the-account-that-can-do-the-job.md',
 'scripts/04-6_choose-traditional-roth-or-a-deliberate-mix.md',
 'scripts/04-7_tell-each-account-what-to-buy-and-finish-the-outside-actions.md',
 'scripts/working/W04_route-contributions-into-usable-accounts-and-intended-holdings.md',
}

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode()

def put(path,text):
    (ROOT/path).write_text(text.rstrip()+'\n',encoding='utf-8')

def replace_once(text,before,after):
    if text.count(before)!=1:
        raise ValueError('Bounded edit source differs')
    return text.replace(before,after,1)

actual=set(git('diff',BASE,'--name-only','--','scripts').splitlines())
if actual!=EXPECTED:
    raise ValueError('Unexpected Allocation canonical change set')
for p in (ROOT/'scripts').rglob('*.md'):
    rel=str(p.relative_to(ROOT))
    if rel not in EXPECTED:
        original=subprocess.check_output(['git','show',BASE+':'+rel],cwd=ROOT)
        if p.read_bytes()!=original:
            raise ValueError('Untargeted script changed')
    else:
        label='WALKTHROUGH_REWRITE_REVIEW' if '/working/' in rel else 'TEACHING_REWRITE_REVIEW'
        if 'Status: '+label not in p.read_text():
            raise ValueError('Missing accurate review status')

# Final read-through correction: tax on a withdrawal is not a spending rate.
p='scripts/04-6_choose-traditional-roth-or-a-deliberate-mix.md';t=(ROOT/p).read_text()
t=replace_once(t,'At a 10% withdrawal rate of tax, Traditional leaves $1,800 instead.','If the tax on that withdrawal is 10%, Traditional leaves $1,800 instead.')
t=replace_once(t,"For the spoken phrase '10% withdrawal rate of tax', the screen must say '10% tax on the withdrawal', never portfolio withdrawal rate. This is a tax comparison, not a retirement spending-rate lesson.","The 10% and 30% figures are tax rates applied to the withdrawal, not portfolio spending rates.")
put(p,t)
# Use the source that was actually retrieved, not the unavailable DOL page.
p='scripts/04-4_build-the-contribution-waterfall-from-one-pool.md';t=(ROOT/p).read_text()
t=replace_once(t,'Employer benefit mechanics reference: US Department of Labor, What You Should Know About Your Retirement Plan, https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/what-you-should-know-about-your-retirement-plan .','Employer benefit mechanics checked September 8, 2026: IRS Retirement topics — Vesting, https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-vesting .')
put(p,t)

# Extend only the existing arithmetic checker for calculations actually taught.
p=ROOT/'tools/guided_course.py';data=p.read_bytes()
blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
if blob!='126e494836a6c2790c31b004c78f4ed1ca7cd8b8':
    raise ValueError('Generator differs from reviewed source')
t=data.decode()
anchor="    eq('fixed debt 50 percent LTV after collateral halves',D('.5')/D('.5'),1)"
addition="""    eq('fixed debt 50 percent LTV after collateral halves',D('.5')/D('.5'),1)
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
    eq('80 percent Bitcoin group isolated 70 percent decline',D('.8')*D('.7'),D('.56'))"""
t=replace_once(t,anchor,addition)
put('tools/guided_course.py',t)

p='README.md';t=(ROOT/p).read_text()
t=replace_once(t,'Full replacement drafts for 2.1, 2.2, 2.4 and 2.5 and all six Debt lessons (3.1–3.6), plus matching W02 and W03 narration, are ready for voice/judgment review.','Full replacement drafts for 2.1, 2.2, 2.4 and 2.5, all six Debt lessons (3.1–3.6), and all seven Allocation lessons (4.1–4.7), plus matching W02–W04 narration, are ready for voice/judgment review.')
t=replace_once(t,'The newest replacement session is [Debt](modules/03.md), following [Cash Flow, Reserve and Life Events](modules/02.md).','The newest replacement session is [Allocation and the next dollar](modules/04.md), following [Debt](modules/03.md) and [Cash Flow, Reserve and Life Events](modules/02.md).')
t=replace_once(t,'| Review the latest replacement drafts | [Debt](modules/03.md) · [Paired W03](scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md) |','| Review the latest replacement drafts | [Allocation](modules/04.md) · [Paired W04](scripts/working/W04_route-contributions-into-usable-accounts-and-intended-holdings.md) |\n| Review Debt | [Debt](modules/03.md) · [Paired W03](scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md) |')
put(p,t)

p='FINALIZATION-STATUS.md';t=(ROOT/p).read_text()
t=replace_once(t,'| All other Core and Advanced lessons, and W01/W04–W10/D07 | Individual teaching/voice repair still needed. Their prose and status headers were not changed by the Debt repair. |','| 4.1–4.7 | Seven full Allocation replacements written; integrated voice/judgment review remains pending. |\n| W04 chapters 1–8 | One narrated recording plan per chapter; exact account, tax, calculation and save behavior remain pending. |\n| All other Core and Advanced lessons, and W01/W05–W10/D07 | Individual teaching/voice repair still needed. Their prose and status headers were not changed by the Allocation repair. |')
t=replace_once(t,'Next is Allocation and W04; the opening sessions, conditional Advanced debt lessons and all other unrepaired components also remain on the repair list.','Next is Tax and W05; the opening sessions, conditional Advanced lessons and all other unrepaired components also remain on the repair list.')
t=replace_once(t,"The Debt replacement includes narrow current primary-source checks of definitions and loan mechanisms, separate from Austin's teaching framework.","The Debt and Allocation replacements include narrow current primary-source checks of definitions, loan mechanisms and account/tax treatment, separate from Austin's teaching framework.")
put(p,t)

p='HANDOFF.md';t=(ROOT/p).read_text()
t=replace_once(t,'The subsequent Debt repair replaces 3.1–3.6 and W03 only; all other canonical bytes, including all of Session 2 and the Reserve, remain unchanged.','The subsequent Debt repair replaced 3.1–3.6 and W03. The current Allocation repair replaces 4.1–4.7 and W04 only; all other canonical bytes, including all of Sessions 2 and 3 and the Reserve, remain unchanged.')
section='''## Allocation replacement — Session 4 and W04

Seven complete spoken replacements now connect current exposure, a reasoned Bitcoin target, intended use and account access, the affordable contribution sequence, relevant account choice, Traditional/Roth tax timing and the actual investment instruction. W04 has one narrated recording plan for each of its eight existing chapters, replacing the old duplicate summaries and short cues. Nothing in this pass marks an app result, account configuration or outside trade complete.

Source work used retrieved text and speaker-note excerpts from `OrangePlan-Week3-Accounts-Allocation.pptx`, the Global Brain V18.8 allocation/account/contribution reasoning, the older protocol Module 4A/4B framework and the current canonical lessons/fixture. The current user-provided Reserve remains the voice/teaching reference. This pass did not read a complete original call or listen to original audio, and it did not inspect every slide visually. Private search snippets and older generated masters were not treated as fresh voice evidence. Generic explanations about old fund elections, uninvested transfers or different household needs are editorial examples, not client facts.

The existing source distinctions are stated explicitly rather than silently blended. The deck's named Bitcoin paths remain, while its indicative percentages are not imposed as mandatory ranges over the current course. Reserve/Bridge/Forever spending horizons remain different from age-based account access. HSA/education money retains its qualified/dedicated job instead of becoming unrestricted early-retirement cash. The current Debt-before-Allocation order and owner liquidity judgment remain. HSA→IRA→additional workplace contributions is a conditional longer-term comparison, not a requirement to finish every tax shelter before building accessible money.

The current same-budget Traditional/Roth example is preserved and explained step by step: $1,000 pretax resources, $1,000 Traditional or $800 Roth after 20% tax, both doubling, then $1,600 spendable at equal rates. The 10%/30% future-tax variants change that result; high growth alone does not establish a universal winner. New contributions remain separate from conversions. Actual Reed payroll tax treatment is still unknown and may change the available cash when compared. No favorable tax rate or permanent election is invented.

The unchanged $1,307,000 allocation subset, $728,000 total Bitcoin exposure, 60/34/6 target comparison and future-only $1,000/$605 route are used throughout. The newly explicit $575,000 taxable and $732,000 retirement subtotals are sums of the original fixture, not certificates of access or sufficiency. Different account sizes require dollar-weighted exposure. A target gap is not an order, and a new contribution also changes the portfolio total. Current Reserve/debt/employee claims still use the same available money once.

Narrow outside checks, separate from the user-derived teaching framework, used current IRS retirement/Roth/RMD/vesting, IRA contribution/deduction/distribution, HSA and business-plan references. Publication 550 supports investment-income and sale mechanics. The expanded-HSA notice and current original-owner Roth RMD guidance were checked so older eligibility or workplace-Roth statements were not silently repeated. Production notes identify the URLs. No current dollar contribution limit, provider menu, tax saving, product recommendation or professional sign-off is asserted. An unavailable DOL page was not used as evidence; the retrieved IRS vesting reference supplies that limited mechanism check instead.

The existing generator and arithmetic checks are extended only for amounts actually discussed; no new writing-quality framework is added. A passed check verifies arithmetic/synchronization/preservation, not Austin's approval or learner comprehension. All Session 2/3 scripts and W02/W03, original dictation, fixture, toolkit, capture receipts and cleanup history remain protected.

'''
t=replace_once(t,'## Next\n',section+'## Next\n')
t=replace_once(t,'Continue with Allocation and W04, one complete lesson and its matching working chapter at a time. Keep the Debt replacement and the accepted Reserve reasoning intact; the conditional Advanced debt lessons still need their own individual repair.','Continue with Tax and W05, one complete lesson and its matching working chapter at a time. Keep the Allocation, Debt and Cash Flow replacements and accepted Reserve reasoning intact; the conditional Advanced lessons still need their own individual repair.')
put(p,t)
print('Prepared seven Allocation replacement drafts, W04 and bounded current progress updates; no blanket course approval.')
