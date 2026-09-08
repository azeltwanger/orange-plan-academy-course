#!/usr/bin/env python3
"""One-use synchronization preparation for already-written Debt scripts.

No external requests, app execution, financial accounts or teaching generation.
Remove this helper and its branch-specific workflow before integration.
"""
from pathlib import Path
import hashlib
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = '8f04e681e21506a6ea428a6c2a1a984f63a0eaca'
EXPECTED = {
    'scripts/03-1_measure-the-payment-pressure-you-actually-carry.md',
    'scripts/03-2_measure-leverage-before-and-after-a-drawdown.md',
    'scripts/03-3_give-every-existing-debt-a-job.md',
    'scripts/03-4_decide-whether-new-financing-improves-the-plan.md',
    'scripts/03-5_compare-financing-on-equal-terms.md',
    'scripts/03-6_write-the-rules-before-using-leverage.md',
    'scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md',
}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode()

def put(path, text):
    (ROOT/path).write_text(text.rstrip()+'\n', encoding='utf-8')

def replace_once(text, before, after):
    if text.count(before) != 1:
        raise ValueError('Bounded edit source differs')
    return text.replace(before, after, 1)

actual = set(git('diff', BASE, '--name-only', '--', 'scripts').splitlines())
if actual != EXPECTED:
    raise ValueError('Unexpected canonical change set')
for path in EXPECTED:
    text = (ROOT/path).read_text()
    label = 'WALKTHROUGH_REWRITE_REVIEW' if '/working/' in path else 'TEACHING_REWRITE_REVIEW'
    if 'Status: '+label not in text:
        raise ValueError('Missing accurate review state')
# Preserve all other script bytes, including the accepted Reserve and repaired Session 2.
for p in (ROOT/'scripts').rglob('*.md'):
    rel = str(p.relative_to(ROOT))
    if rel not in EXPECTED and p.read_bytes() != subprocess.check_output(['git','show',BASE+':'+rel],cwd=ROOT):
        raise ValueError('Untargeted script changed')

# Keep narrow factual references in production notes, not in spoken text.
p = 'scripts/03-3_give-every-existing-debt-a-job.md'
t = (ROOT/p).read_text()
t = replace_once(t, '### Member checkpoint', 'Additional mechanism reference, read September 8, 2026: Chase mortgage recast explanation, https://www.chase.com/personal/mortgage/education/managing-your-mortgage/what-is-mortgage-recast . This supports the distinction between principal reduction and a recalculated payment; eligibility and lender terms vary. It is not a recommendation to use that lender.\n\n### Member checkpoint')
put(p,t)
p = 'scripts/03-5_compare-financing-on-equal-terms.md'
t = (ROOT/p).read_text()
t = replace_once(t, '### Member checkpoint', 'Additional tax mechanism references, read September 8, 2026: IRS Topic 505, https://www.irs.gov/taxtopics/tc505 ; IRS Publication 550 (allocation of interest by use of loan proceeds, not collateral), https://www.irs.gov/publications/p550 ; IRS Topic 431 on canceled debt, https://www.irs.gov/taxtopics/tc431 . These checks are separate from Austin\'s planning judgment and do not establish a real household\'s deduction, liability or eligibility.\n\n### Member checkpoint')
put(p,t)

# Extend the existing arithmetic checks; retain their implementation and source fixture.
p = ROOT/'tools/guided_course.py'
data = p.read_bytes()
blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
if blob != '560ac30d8162388762c837928d102475426fca4d':
    raise ValueError('Generator source differs from reviewed base')
t = data.decode()
anchor = "    eq('generic recurring bill full-year saving',D(40)*12,480)"
addition = """    eq('generic recurring bill full-year saving',D(40)*12,480)
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
    eq('fixed debt 50 percent LTV after collateral halves',D('.5')/D('.5'),1)"""
t = replace_once(t, anchor, addition)
put('tools/guided_course.py', t)

# Update existing review entry points without another master, workbook or quality system.
p = 'README.md'; t = (ROOT/p).read_text()
t = replace_once(t,
    'Full replacement drafts for 2.1, 2.2, 2.4 and 2.5, plus matching W02 narration, are now ready for voice/judgment review. The rest still needs individual repair—not just final approval of the old prose.',
    'Full replacement drafts for 2.1, 2.2, 2.4 and 2.5 and all six Debt lessons (3.1–3.6), plus matching W02 and W03 narration, are ready for voice/judgment review. Other sessions and the conditional Advanced library still need individual repair—not just final approval of the old prose.')
t = replace_once(t,
    'Start with [Session 2](modules/02.md), or use the [Core reading order](DICTATION-ORDER.md) for clean spoken copies.',
    'The newest replacement session is [Debt](modules/03.md), following [Cash Flow, Reserve and Life Events](modules/02.md). Use the [Core reading order](DICTATION-ORDER.md) for clean spoken copies.')
t = replace_once(t,
    '| Review the current repaired session | [Cash Flow, Reserve and Life Events](modules/02.md) · [Paired W02](scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md) |',
    '| Review the latest replacement drafts | [Debt](modules/03.md) · [Paired W03](scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md) |\n| Review the preceding session | [Cash Flow, Reserve and Life Events](modules/02.md) · [Paired W02](scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md) |')
put(p,t)

p = 'FINALIZATION-STATUS.md'; t = (ROOT/p).read_text()
t = replace_once(t,
    '| All other Core and Advanced lessons, and W01/W03–W10/D07 | Individual teaching/voice repair still needed. Their substantive prose was not rewritten by this batch; only the misleading status header was corrected. |',
    '| 3.1–3.6 | All six Debt explanations have full individual replacements; voice/judgment review is still pending. |\n| W03 chapters 1–6 | Matching narration and one recording plan per chapter replace the duplicate short cues. Actual contract inputs, app behavior and results remain unverified. |\n| All other Core and Advanced lessons, and W01/W04–W10/D07 | Individual teaching/voice repair still needed. Their prose and status headers were not changed by the Debt repair. |')
t = replace_once(t,
    'Next is Debt; the opening sessions and all other unrepaired components also remain on the repair list.',
    'Next is Allocation and W04; the opening sessions, conditional Advanced debt lessons and all other unrepaired components also remain on the repair list.')
t = replace_once(t,
    'Source-based editing here is not a new independent professional verification.',
    'The Debt replacement includes narrow current primary-source checks of definitions and loan mechanisms, separate from Austin\'s teaching framework. They are not independent professional sign-off or transaction-specific approval.')
put(p,t)

p = 'HANDOFF.md'; t = (ROOT/p).read_text()
t = replace_once(t,
    'Every other canonical script is unchanged except its status line, which now says individual repair is still needed. The existing generator regenerates reading copies and no longer labels every lesson Reviewed. No new quality-scoring framework or competing master is created.',
    'That Session 2 repair also corrected the status line in then-unrepaired scripts. The subsequent Debt repair replaces 3.1–3.6 and W03 only; all other canonical bytes, including all of Session 2 and the Reserve, remain unchanged. The existing generator regenerates reading copies and no longer labels every lesson Reviewed. No new quality-scoring framework or competing master is created.')
new_section = '''## Debt replacement — Session 3 and W03

Six full explanations now work through required versus extra payments, interest-only principal, DTI versus spendable cash, current and stressed DTA, loan-specific LTV, each existing debt's job, financing purpose, equal-purpose financing comparisons, and the repayment/response rules. W03 has one narrated recording plan for each of its six existing chapters. Its former duplicate short-cue and summary versions are removed.

Teaching sources actually consulted were relevant text and speaker-note passages from `OrangePlan-Week4-Debt-Strategy.pptx`, the older detailed Debt outline, the Global Brain debt playbook, and original March 17 / April 8 call dialogue. These establish the strategic uses of debt, debt tolerance, rate versus household capacity, required/extra-payment confusion, released cash after payoff, and the need to check an interest-only maturity. No raw private dialogue, names, client amounts, personal investment assurances or old app behavior are committed. Full-deck visual inspection and original audio listening are not claimed.

Source distinctions are explicit. The older deck and outline use different ratio bands; neither is a universal safety rule in the current course. The deck's margin-call wording differs from its liquidation graphic; the current 80% example is hypothetical liquidation only, with warning/call triggers separately checked. Its universal structure ladder, unsecured-no-forced-sale claim and interest-only superiority are not reinstated over the current Core's contract/repayment analysis. The owner's later liquidity judgment qualifies categorical card-first language. Historical STRC/reserve and confident-return recommendations in the calls are not imported over the accepted Reserve framework. No new personal rule is attributed to Austin to resolve these differences.

The fictional source data remains unchanged. New arithmetic explanations derive from its card balance/rate/minimum, and from the existing separate $20,000, 8%, five-year repayment illustration. Approximate card interest is not a daily-billing statement; hypothetical amortization is not a quote or Reed payoff forecast. The $30,000 project stays a separate comparison. No new security, tax basis, model result, maturity, lender threshold, current offer or household debt job is invented. Other non-card debt choices are comparisons until a reviewed fictional decision is supplied.

Narrow outside checks were limited to CFPB DTI/HELOC/loan-comparison/home-equity-contract mechanisms, FINRA SBLOC restrictions and collateral rights, IRS plan loans/use-of-proceeds/canceled debt, and a lender's explanation of mortgage recasting. The URLs are in production notes, not spoken narration. They support those mechanisms, not current loan pricing, suitability, guaranteed outcomes or professional sign-off. Material product and contract inputs still wait for the actual demonstration.

'''
t = replace_once(t,'## Next\n',new_section+'## Next\n')
t = replace_once(t,
    'Continue with Debt, one complete lesson and its matching working chapter at a time. Preserve the larger strategic-debt scope.',
    'Continue with Allocation and W04, one complete lesson and its matching working chapter at a time. Keep the Debt replacement and the accepted Reserve reasoning intact; the conditional Advanced debt lessons still need their own individual repair.')
put(p,t)
print('Prepared six Debt replacement drafts, W03 and existing review status; no blanket course acceptance.')
