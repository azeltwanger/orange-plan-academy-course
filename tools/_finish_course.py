#!/usr/bin/env python3
"""Apply already-authored course manuscripts and derive a reading artifact.

This temporary helper does not generate teaching, call a model, contact a network,
run Orange Plan, touch financial data, or certify instructional effectiveness.
It is removed, with the literal input modules and write workflow, before merge.
"""
from __future__ import annotations
from pathlib import Path
import argparse, collections, hashlib, html, json, re, runpy, subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = '21156d7fcb1c24c51cf07a239a5ff802d10e85c9'
RESERVE_BLOB = '2c107a394a93cc877c73f011dfe37fb5ad3d94b1'
GENERATOR_BLOB = '5834d968818e16211f2f37d24322bcf9f4e9b67f'
MANUSCRIPTS = ['opening','allocation','tax','retirement','protection','maintenance','advanced_finance','advanced_protection']
PRACTICAL = ['practical_early','practical_retirement','practical_protection']
RETAINED = {'2.1','2.2','2.4','2.5','3.1','3.2','3.4','3.5','3.6'}
REVIEWED_PRACTICAL = {'W02','W03'}
COMMON = '''The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.\n\nExact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.'''

def git(*args: str) -> str:
    return subprocess.check_output(['git',*args],cwd=ROOT).decode()

def old(path: str) -> str:
    return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT).decode()

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def put(path: str, text: str) -> None:
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text.rstrip()+'\n',encoding='utf-8')

def once(text: str, before: str, after: str) -> str:
    if text.count(before)!=1:
        raise ValueError('Bounded edit differs from reviewed source: '+before[:65])
    return text.replace(before,after,1)

def section(text: str, name: str) -> str:
    m=re.search(r'^### '+re.escape(name)+r'\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S)
    return m.group(1).strip() if m else ''

def paths() -> dict[str,str]:
    result={}
    for p in sorted((ROOT/'scripts').rglob('*.md')):
        m=re.match(r'# ((?:A?\d+\.\d+|[WD]\d+)) — ',p.read_text())
        if not m or m.group(1) in result: raise ValueError('Invalid canonical inventory')
        result[m.group(1)]=str(p.relative_to(ROOT))
    return result

def header(text: str, status: str, title: str|None=None) -> str:
    h=text.split('### ',1)[0].rstrip()
    h,n=re.subn(r'^Status: [^\n]*','Status: '+status,h,count=1,flags=re.M)
    if n!=1: raise ValueError('Missing status')
    if title:
        h=re.sub(r'^(# [^ ]+ — )[^\n]+',lambda m:m.group(1)+title,h,count=1)
    h=re.sub(r'^Adapted source: [^\n]*','Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.',h,count=1,flags=re.M)
    return h

def load_groups(names: list[str]) -> dict[str,dict]:
    result={}
    for name in names:
        value=runpy.run_path(str(ROOT/'tools'/('_finish_'+name+'.py')))
        for lid,read in value['LESSONS'].items():
            if lid in result: raise ValueError('Duplicate manuscript')
            if lid not in value['NOTES'] or lid not in value['CHECKPOINTS']:raise ValueError('Incomplete authored manuscript')
            result[lid]={'read':read,'notes':value['NOTES'][lid],'finish':value['CHECKPOINTS'][lid],
                         'title':value.get('TITLES',{}).get(lid),'demo':value.get('DEMOS',{}).get(lid)}
    return result

def primary_record() -> str:
    return '''# Teaching revision — source and editorial record

## Scope and owner direction

This pass implements Austin's explicit request to finish all written lessons and paired demonstrations using Problem → Explanation → Example → Solution. The structure is behind the teaching; it is not a requirement for identical headings, lengths or sentence rhythms. The program's existing sequence is retained. The whole-portfolio question in Allocation is answered before contribution and account implementation.

Written preparation is not owner approval, finished app footage, professional sign-off, a learner outcome or validation of a $3,000 annual price. Those claims are not made by this record. The earlier rejected bulk pass is not used as evidence of Austin's voice.

## Actual source basis

| Area | Sources consulted and role |
|---|---|
| Spoken progression | Uploaded `Pasted text(1).txt`, SHA-256 `749d8e1f5ac4c7c5d6913fb56df4bd9be90425c6f4c33b79cc9df0ffad624dfc`; and `Bitcoin Is My Path To Early Retirement.txt`, SHA-256 `7f624fe13fe48ee01516f5999da296e60b76a0913b9f53824bdaaa2855cf5f3c`. Used for question-first explanation, worked reasoning, continuity and action. NOT a financial-authority source. |
| Accepted depth and voice reference | Unchanged 2.3 Reserve, including Austin's September 8 conditional liquidity judgment. |
| Start Here / First Plan | Preserved August 25 dictation, the original orientation record, Foundation deck text/notes, Global Brain and old protocol framework. Current course sequence overrides old module counts and interfaces. |
| Cash Flow / Debt | Earlier individually repaired full explanations and their original Cash Flow + Reserve and Debt Strategy decks, old detailed framework and Global Brain reasoning. Original private-call passages were consulted in those repairs for teaching patterns; no new complete audio review is claimed. |
| Allocation | Accounts + Allocation deck text and notes in sequence: setup, Bitcoin role, timeframe/position sizing, contributions, account menu, tax election and execution. Global Brain and earlier Module 4 framework supply the related planning intent. |
| Tax | Tax Strategy deck text and notes, Global Brain tax reasoning, current lot example and contribution/conversion distinctions. |
| Retirement | Retirement Income deck and detailed notes: spending, income floor, gap, access/benefits, healthcare, account/asset funding, sequence/Reserve, sell/borrow, comparisons and annual review. |
| Custody | Custody deck as context plus the later owner-supplied custody-direction material. Later direction rejects a wealth/complexity ladder and recognizes direct, professional, collaborative and intentional split trade-offs. |
| Family and Maintenance | Estate/Inheritance deck, Maintenance System deck, Global Brain and the existing Heir Letter, Executor Packet, Family Custody Map, insurance audit, Annual Plan Refresh and Household Plan Summary. |
| Scope and constraints | The full current canonical Core/Advanced inventory, the existing practical chapters and unchanged Reed fixture at base `21156d7fcb1c24c51cf07a239a5ff802d10e85c9`. Current scripts provide scope and source distinctions, not proof that generated prose is Austin's own speech. |

Relevant slide text and speaker notes were read. No complete visual slide-deck audit or original-audio listening is asserted. No client name, private balance, transcript, recovery information or personal medical anecdote is committed. The uploaded video itself is not copied into the course repository.

## Explicit source decisions and educational expansions

The new Allocation explanation of cash arrangements, broad stock funds, bonds and existing property/business holdings is an educational expansion requested by Austin's question about the other 50%. The source deck's phrase “balanced mix” does not select an index, geography, fund, provider or weight. The draft explains those comparisons without inventing Austin's preferred products or a universal portfolio. New amounts and hypothetical preferences are labeled.

The video does not supply an 8% withdrawal rule, Forever Number multiplier, guaranteed retirement funding, fixed return path, price forecast, universal taxable-only gap, tax threshold or assurance that a reserve prevents every forced sale. None is imported. The existing model preference is supported by the preserved course dictation independently of the video.

Older slide ratio bands, margin-call/liquidation wording, interest-only superiority, custody-by-wealth ladders and automatic age/timeframe rules are not silently reinstated. The current course and later explicit owner direction control the identified conflicts; remaining transaction-specific judgments are not replaced by general advice.

Generic mathematical examples illustrate mechanisms. They do not supply missing Reed birthdays, source securities, basis, policy terms, tax jurisdiction, benefit quotes, debt schedules, insurance or engine results. The fixed Reed source remains unchanged. The complete app demonstration still requires a separately reviewed fictional capture extension.

## Section completion and repetition edits

| Section | Distinct completed teaching job |
|---|---|
| Start Here / First Plan | Recognized personal question → actual inventory and assumptions → first result literacy → useful next check. Detailed spending repair waits for Cash Flow. |
| Cash Flow / Reserve | Current usable amount → worthwhile spending changes → accepted Reserve target and pace → expected events and optional college commitment. Previous full explanations retained where they already complete that decision. |
| Debt | Payment pressure, household leverage and lender-specific risk → debt jobs → purpose of financing → equal-purpose comparison → repayment/response instructions. 3.3's repeated Reserve explanation is shortened to applying the prior decision. |
| Allocation | Entire portfolio, not another drawdown warning: Bitcoin role → spending jobs and non-Bitcoin investments → justified amounts → affordable contributions → usable accounts → tax election → each purchase instruction. |
| Tax | One sale's proceeds/basis/gain → records → actual income windows → complete conversion/withdrawal/no-change comparison → specific execution and professional packet. Duplicate option-list endings are removed. |
| Retirement | Complete cash need and early access → coverage → account/asset funding → sequence and finite Reserve → borrowing comparison → one real-life decision test → annual spending/refill operating rule. 6.7 uses 1.5's simulation literacy rather than repeating it. |
| Custody / Family | Named failure → manageable architecture → appropriately scoped proof → real account security and family starting process → legal roles and documents → findable letter/packet → retained versus insured risk. Practice recovery never certifies another wallet. |
| Maintenance / Capstone | Quiet monthly facts, actual exceptions and complete annual review → one coherent plan → listener can explain the funding and next action. No promise of fixed review time or claimed successful learner test. |
| Advanced | Fifteen conditional applications add contract, account, timing or operating detail. They are not required detours for every member and do not reopen the Core concepts without a new decision. |

The nine rewritten practical files each contain one chapter plan, not a short summary plus a duplicate cue version. W02 and W03's already-detailed plans are retained; all of W02, including the accepted Reserve block, is byte-identical. Core and Advanced explanations are not assigned a target word count. No sentence-rhythm score or software test certifies their quality.

## New illustrative amounts

These are explicitly separate from the Reed fixture. They are also checked in the existing arithmetic checker, which verifies arithmetic only.

| Lesson | Illustration and limitation |
|---|---|
| 4.3 | $1m; $500k Bitcoin; prior $60k Reserve + distinct $40k purchase = $100k cash; $400k long-runway stocks gives 50/40/10. Two further $50k retirement payments deliberately prefunded in cash gives 50/30/20. Preferences and horizons are assumed, not recommended. Supersedes the earlier $500k weighting-only narration; old checks remain historical arithmetic, not actual plan results. |
| 5.4 | $30k Traditional and $6k outside tax funding; both relevant investments double. Converted qualified Roth $60k; no-conversion after-tax total $60k/$54k/$66k at hypothetical 20/30/10% later Traditional tax. Outside additional tax/fees/return differences omitted explicitly. |
| 5.5 | $20k value/$16k basis produces $4k gain; reversing them gives $4k loss, not a $4k refund. Not an executed harvest or wash-sale conclusion. |
| 6.1 | Existing rough $108k cost less $40k gross income = $68k. Separate extension adds hypothetical $12k tax and $6k debt not already counted to show $86k complete cash gap. Actual tax-dependent withdrawals require the model's full calculation. |
| 6.3 | Hypothetical ordinary-year coverage cost: $12k premium+$3k other=$15k versus $8k+$8k=$16k. No quote, cap or actual coverage promise. |
| 6.6 / 6.8 | $20k at simple 10% for one year adds $2k interest or leaves $22k owed; $100k to $95k proposed spending is a $5k practical reduction, not an actual guardrail output. |
| 8.4 | $40k annual shortfall for ten years is $400k before growth, inflation, tax, changing needs and other resources. Scale only, not a policy recommendation. |
| A3.1 | Source $25k loan becomes $28k under its simplified annual-interest example; $50k collateral means 56% LTV. Repaying $3k or adding $6k collateral each reaches 50% at that instant, with different resource costs. Not a recommended threshold. |
| A4.1 | $20k at $100k/BTC buys 0.2 BTC. Half now plus half at $50k buys 0.3; half now plus half at $200k buys 0.15. No fees, probability or market forecast. |
| A5.1 | First $20k conversion costs hypothetical $4k; second $20k costs $6k. Combined $10k/$40k=25% hides 20% and 30% increments. No actual tax result. |
| A5.3 | $10k annual tax saving less $8k added recurring costs leaves $2k before other differences and a separate $20k moving cost. No jurisdiction conclusion. |
| A6.1 / A6.2 | $10k conversion with $2k tax+$1.5k coverage change costs $3.5k/35%. Two beginning-year $20k borrowings with 10% end-year capitalization leave $22k then $46.2k, including $6.2k interest. No quotes or program rules inferred. |
| A6.3 | First SEPP payment on exact 54th birthday illustrates duration to 59½; on 58th illustrates five years to 63. Actual dates, calculation and compliance require review. |
| A7.3 / A7.4 | Two 30% providers with a verified shared custodian expose 60%, not a 60% loss probability. Hypothetical 500vB transaction at 2/20 sat/vB costs 1,000/10,000 sats; no current fee or universal dust threshold. |

## Narrow primary checks — separate from the teaching source

Checked September 8, 2026 for specific mechanisms, not household suitability or professional approval. Exact plan, policy, provider, jurisdiction, device and transaction rules still need their applicable review before recording or execution. Prior primary references in the course remain accessible through Git history and PRIMARY-SOURCES.md.

- Allocation: https://www.investor.gov/introduction-investing/getting-started/asset-allocation ; https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds ; https://www.fdic.gov/resources/deposit-insurance/financial-products-not-insured ; current Investor.gov money-market and cash-sweep bulletins, bond-fund explanations and TreasuryDirect marketable-security sale guidance.
- Tax: https://www.irs.gov/publications/p550 ; https://www.irs.gov/publications/p590a ; https://www.irs.gov/publications/p590b ; https://www.irs.gov/irb/2026-15_IRB (Notice 2026-20, limited eligible broker-held digital-asset identification relief for 2026, not an all-wallet or after-the-fact election); https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions .
- Retirement access: https://www.irs.gov/retirement-plans/substantially-equal-periodic-payments ; https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions ; https://www.irs.gov/retirement-plans/plan-participant-employee/401k-resource-guide-plan-participants-general-distribution-rules .
- Coverage: https://www.healthcare.gov/income-and-household-information/income/ ; https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-can-i-sign-up-for-medicare ; https://www.ssa.gov/medicare/plan/when-to-sign-up ; https://www.joincrowdhealth.com/resources/member-guide . Noninsurance does not guarantee that bills will be funded.
- Recovery: https://trezor.io/guides/backups-recovery/general-standards/how-to-use-a-wallet-backup ; https://trezor.io/guides/trezor-suite/using-a-passphrase-wallet-in-trezor-suite ; https://trezor.io/learn/security-privacy/personal-security-standards/understanding-trezor-wallet-backups-12-20-or-24-words ; https://trezor.io/guides/trezor-suite/trezor-suite-settings . Exact device procedures remain a recording hold.
- UTXOs: https://trezor.io/learn/supported-assets/bitcoin/coin-control-in-trezor-suite-choose-which-utx-os-to-spend ; https://trezor.io/learn/supported-assets/bitcoin/what-is-a-utxo ; https://coldcard.com/learn/transaction-security/bitcoin-utxo-management . No generic dust value, current fee or future fee guarantee imported.
- Security and family: https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-multifactor-authentication ; https://www.consumerfinance.gov/ask-cfpb/what-is-a-power-of-attorney-poa-en-1149/ ; https://www.consumerfinance.gov/ask-cfpb/what-is-a-revocable-living-trust-en-1775/ ; https://www.consumerfinance.gov/ask-cfpb/i-would-like-to-be-able-to-have-my-friend-or-family-member-help-with-my-bill-paying-and-banking-what-are-my-options-en-1145/ ; https://content.naic.org/publications . Jurisdiction-specific estate and policy conclusions remain outside this generic draft.

## Evidence boundary

The fixed fixture, original source-material, toolkit, capture receipts, tests and historical-recovery manifest are unchanged. No app repository, hosted data, provider account, wallet, financial operation, runtime flag, service entitlement, pricing, student launch or Production deployment is changed. Actual build/test/merge identities are recorded in the PR handoff after they exist, not predicted in advance.
'''

def apply() -> None:
    ps=paths()
    if len(ps)!=77:raise ValueError('Course inventory changed')
    if blob((ROOT/ps['2.3']).read_bytes())!=RESERVE_BLOB:raise ValueError('Reserve differs')
    for path in ps.values():
        if (ROOT/path).read_text()!=old(path):raise ValueError('Unexpected preexisting canonical edit')
    originals={lid:(ROOT/p).read_text() for lid,p in ps.items()}
    groups=load_groups(MANUSCRIPTS)
    if len(groups)!=55 or sum(not x.startswith('A') for x in groups)!=40:raise ValueError('Authored lesson coverage differs')
    expected=set(ps)-set(groups)-RETAINED-{'2.3','3.3'}
    if expected!=set(['W01','W02','W03','W04','W05','W06','W07','D07','W08','W09','W10']):raise ValueError('Coverage gap')
    for lid,row in groups.items():
        prior=originals[lid]
        read=row['read'].strip().replace('a independently verified','an independently verified')
        if len(read.split())<100:raise ValueError('Authored replacement too short or absent')
        h=header(prior,'TEACHING_REWRITE_REVIEW — complete written explanation using the accepted problem, explanation, example and solution approach. Integrated voice/judgment review and actual filming remain open.',row['title'])
        # The individual manuscript notes preserve the relevant distinctions. These are not spoken.
        text=h+'\n\n### Read aloud\n\n'+read+'\n\n### Visual and source notes — not spoken\n\n'+row['notes'].strip()+'\n\n### Production notes\n\n'+COMMON
        if row['demo']:
            text+='\n\n### Demonstration plan — not spoken\n\n'+row['demo'].strip()+'\n\nThe demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.'
        # Preserve existing optional feature speech but not duplicated old cue versions.
        if lid in {'0.2','1.5'}:
            extra=section(prior,'Screen-dependent inserts — record only after verification') or section(prior,'Screen-dependent insert — record only after verification')
            if extra:text+='\n\n### Screen-dependent inserts — record only after verification\n\n'+extra
        text+='\n\n### Member checkpoint\n\n'+row['finish']
        put(ps[lid],text)
    for lid in RETAINED:
        t=originals[lid]
        t=re.sub(r'^Status: [^\n]*','Status: TEACHING_RETAINED_REVIEW — the prior individual full explanation is retained after section-level continuity review. This pass does not claim a new full rewrite or Austin voice approval.',t,count=1,flags=re.M)
        put(ps[lid],t)
        if section(t,'Read aloud')!=section(originals[lid],'Read aloud'):raise ValueError('Retained speech changed')
    # Apply one deliberate redundancy cut; the approved Reserve itself stays byte-identical.
    t=originals['3.3']
    before='''There is a reason we're also building the reserve while expensive debt remains. Paying the card down faster is useful, but we don't want the family to have no cash left when something goes wrong and immediately need to borrow again.

I'd give accessible cash more weight when a household has dependents or relies on one income, especially if essential bills would otherwise depend on getting another loan after that income stops. Required payments still need to be covered. What changes is how much extra goes to debt while the cash cushion is thin.

That can mean more interest for a while. It's a trade-off, not free protection. Revisit the pace as the reserve improves instead of leaving a temporary slower payoff in place forever. Dependents alone don't settle it; the cash already available and any reliable income that would continue matter too.'''
    after='''Bring forward the liquidity decision from the Reserve lesson. If the cash cushion is too thin to support the family during an income interruption, more of the available money may need to build it before accelerating the card. Required payments continue. The cost is more interest for a while, so revisit the split as the cushion improves. We are applying that choice here, not setting a second reserve policy.'''
    t=once(t,before,after)
    t=re.sub(r'^Status: [^\n]*','Status: TEACHING_REWRITE_REVIEW — existing individual explanation retained with a targeted redundancy cut. The prior Reserve decision is applied without reteaching it; voice review remains open.',t,count=1,flags=re.M)
    put(ps['3.3'],t)
    # One individually authored chapter plan per practical; W02 and W03 remain untouched.
    practical={}; setups={}; finishes={}
    for name in PRACTICAL:
        v=runpy.run_path(str(ROOT/'tools'/('_finish_'+name+'.py')))
        for lid,chapters in v['CHAPTERS'].items():
            if lid in practical:raise ValueError('Duplicate walkthrough')
            practical[lid]=chapters;setups[lid]=v['SETUP'][lid];finishes[lid]=v['FINISH'][lid]
    counts={'W01':10,'W04':8,'W05':6,'W06':8,'D07':8,'W07':4,'W08':5,'W09':5,'W10':5}
    if set(practical)!=set(counts):raise ValueError('Practical coverage gap')
    for lid,chapters in practical.items():
        if len(chapters)!=counts[lid]:raise ValueError('Practical chapter count changed')
        h=header(originals[lid],'WALKTHROUGH_REWRITE_REVIEW — complete paired narration and one recording plan per chapter. Final app/device procedures, inputs, outputs and capture evidence remain unverified.')
        text=h+'\n\n### Run sheet\n\n'+setups[lid]+'\n\nRecord chapters separately after their paired lessons. Only the paragraphs labeled Narration are prepared speech. Teaching graphics stay outside app screens. Read actual values and state changes during recording; do not substitute a staged output or unsupported feature.\n'
        for i,(title,show,speech,checks,finish) in enumerate(chapters,1):
            text+=f'\n#### Chapter {i} — {title}\n\n**Show and do:** {show}\n\n**Narration:**\n\n{speech}\n\n**Verify before recording:** {checks}\n\n**Member finish:** {finish}\n'
        text+='\n### Readback and finish\n\n'+finishes[lid]+'\n\n### Production notes\n\n'+COMMON+'\n\nThis file replaces the prior duplicate summary/detail/cue sets with one chapter sequence. Original sources, the fixed household, member documents and the capture register remain unchanged. No real recording, provider action or learner result is certified.'
        text=text.replace('A explainable','An explainable')
        put(ps[lid],text)
    for lid in REVIEWED_PRACTICAL|{'2.3'}:
        if (ROOT/ps[lid]).read_text()!=originals[lid]:raise ValueError('Protected reference/walkthrough changed')
    # Existing checker only: add arithmetic, accurate retained status and current draft wording.
    p=ROOT/'tools/guided_course.py'
    if blob(p.read_bytes())!=GENERATOR_BLOB:raise ValueError('Generator source moved')
    t=p.read_text()
    t=once(t,"    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:","    if 'Status: TEACHING_RETAINED_REVIEW' in row['text']:\n        return 'Individual explanation retained; voice review pending'\n    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:")
    t=once(t,'The earlier course-wide pass was rejected for voice and teaching clarity. Only the Reserve is the accepted reference; replacement drafts and unrepaired components are distinguished below. Recording and professional review remain separate.', 'The written teaching and paired demonstration pass now covers every component. The Reserve remains the accepted reference; all other integrated wording remains for Austin\'s review. New replacements and retained individual explanations are distinguished below. Written preparation, recording, professional review and actual learner evidence remain separate.')
    # Make the Python single-quoted generated prose valid after the apostrophe inserted above.
    t=t.replace("for Austin's review. New replacements", "for Austin\\'s review. New replacements")
    anchor="    return {'scope':'Arithmetic teaching checks only; no retirement forecast, tax opinion, lender assurance or model acceptance.'"
    if t.count(anchor)!=1:raise ValueError('Arithmetic return source differs')
    additions="""    # New explicitly hypothetical teaching mechanisms; not Reed inputs or engine outputs.
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
"""
    t=t.replace(anchor,additions+anchor,1)
    put('tools/guided_course.py',t)
    put('delivery/teaching-revision.md',primary_record())
    put('README.md','''# Orange Plan Academy

**The written teaching and paired walkthrough pass is complete for review.** The course now follows a recognized problem through explanation and a worked example to a usable decision. The accepted Reserve lesson is unchanged. Owner voice approval, real app/device footage, targeted professional checks and learner evidence are still separate.

## Read the course

| Reading task | Open |
|---|---|
| Clean Core scripts, in order | [Core reading order](DICTATION-ORDER.md) |
| All spoken text in one document | [ALL-SCRIPTS](ALL-SCRIPTS.md) |
| Conditional advanced teaching | [Advanced reading order](ADVANCED-DICTATION-ORDER.md) |
| Whole-portfolio Allocation section | [Session 4](modules/04.md) |
| Paired application and filming sequence | [Learning and filming order](FILM-ORDER.md) |
| Existing member materials | [Toolkit](toolkit/README.md) · [Named deliverables](toolkit/deliverables/README.md) |
| Actual scope and unfinished evidence | [Current status](FINALIZATION-STATUS.md) · [Production checklist](PRODUCTION-CHECKLIST.md) |

There are 51 Core teaching clips (including optional college), 15 conditional Advanced lessons, ten app working sessions and one device demonstration. This is one course, not a set of competing outlines. The Advanced lessons are used when relevant; every member is not required to watch every variation.

The 40 new Core replacements and all 15 new Advanced replacements are integrated into the existing scripts. Nine previously repaired full Core explanations are retained; 3.3 receives a targeted repetition cut; 2.3 remains the accepted reference. Nine practical files are rewritten into one narrated chapter plan each. The already-detailed W02 and W03 are retained unchanged. All have been checked for their place in the connected learning sequence, not presented as new rewrites merely because a status changed.

## Edit one source

Edit `scripts/`. Only `### Read aloud` is spoken in a teaching clip. The teleprompter files, modules, lesson text and masters are generated reading views. Visual/production notes, references and member checkpoints are not narration. The uploaded YouTube video supplies teaching structure only, not its return assumptions or retirement formulas.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p test_member_deliverables.py -v
python tools/guided_course.py history
```

These commands verify structure, arithmetic, synchronization and preservation. They do not prove teaching quality, owner approval, a student outcome or release readiness. Historical recovery needs a full checkout.

## Sources, review and repository cleanup

[Source and revision record](delivery/teaching-revision.md) distinguishes original teaching, new illustrative reasoning and narrow primary-source checks. [Current handoff](HANDOFF.md) records what is finished in writing and what still needs real evidence.

Original dictation in `source-material/`, the fixed household, toolkit and capture records remain unchanged. Obsolete working versions remain retired, with [pinned recovery](ARCHIVE-RECOVERY.md) and the existing [hash manifest](production/repository-cleanup.json). No temporary authoring helper or branch-writing workflow should remain at merge.

Publication to main is for Austin to read. No app deployment, provider operation, financial transaction, pricing change or student launch is implied. Do not place real client records, credentials or signing secrets in this repository.
''')
    put('FINALIZATION-STATUS.md','''# Course status — complete written draft; approval and capture remain separate

## Written deliverable

All 51 Core clips, 15 conditional Advanced clips, ten app working sessions and the device demonstration have complete written teaching or paired narration for review. This pass finishes the requested problem → explanation → example → solution treatment across the existing course rather than leaving later sections under an indefinite repair promise.

40 Core and all 15 Advanced scripts are full replacements. Nine previously repaired Core explanations are retained after continuity review; 3.3 is shortened where it repeats the Reserve explanation. Accepted 2.3 is byte-identical. Nine practical files are replaced with one chapter sequence each; the already-detailed W02 and W03 are byte-identical. Generated reading copies are rebuilt from those canonical sources.

The new Allocation lesson explains the whole portfolio, including the non-Bitcoin holdings, instead of offering another drawdown-tolerance lecture. The separate examples show where amounts come from and why a choice changes. Tax now completes an opportunity-cost comparison; Retirement uses first-result literacy instead of redefining simulations. Protection, family documents and maintenance finish actual actions without inventing their completion.

## What has not been established

**Austin approval:** The Reserve is the accepted reference. New or retained integrated wording still needs the owner's voice/judgment review. A complete draft is not evidence that Austin already dictated or approved every line.

**App and device evidence:** Final navigation, field semantics, actual model outputs, source coverage, save/reload, Ask, reports/exports, family communication and device procedures require the approved build and real capture receipts. The fixed household is not a calibrated saved engine result. Complete its separately reviewed capture extension; never invent results to satisfy a script.

**Professional review:** Tax, account access, healthcare, lending, insurance and legal/estate execution require the relevant current and transaction-specific checks. Primary-source mechanism research in this editorial pass is not personalized advice or professional sign-off.

**Learner evidence:** No cold-member completion, listener rehearsal, wallet recovery or full paid program pilot is claimed merely because the instructions exist. Test whether a member can explain and complete the decisions without the author filling every gap. Annual-price and renewal value are not validated by word counts or software tests.

**Production:** Visual directions are prepared; finished graphics, edited video, course-platform publication and actual support operations are not certified. Screen footage can be completed separately without reopening every durable explanation, unless product semantics materially change.

## Repository boundary

Main contains review material under the owner's request to read the current scripts. No app repository, hosted account, runtime flag, provider, wallet, financial operation, legal filing, commercial term, Production deployment or student release is changed. Original sources, the fixture, toolkit, capture receipts and historical cleanup remain preserved. Exact run/head/merge evidence is posted after verification in the implementation PR.
''')
    put('HANDOFF.md','''# Current course handoff — complete written teaching pass

Austin asked to finish all lessons and walkthroughs using the accepted Problem → Explanation → Example → Solution approach. The YouTube retirement script is a reference for simplicity and progression only. The accepted Reserve explanation, including the conditional liquidity judgment, remains unchanged.

## Delivered in writing

The existing 51 Core / 15 Advanced / 11 practical inventory is retained. There are 40 full Core replacements and 15 full Advanced replacements, nine retained individual Core explanations, a targeted repetition cut in 3.3, and the unchanged accepted 2.3. Nine practical files now contain one fully paired chapter plan each; W02 and W03 remain byte-identical because their existing detailed plans already perform their distinct jobs. Clean reading views are regenerated from `scripts/`.

Allocation now answers what the non-Bitcoin money should do and why cash, stock exposure, suitable bonds or existing property/business interests can serve different jobs. The new $1m example derives its cash from stated commitments and explains the long-runway choice. It is not a prescribed portfolio or a Reed fixture extension.

The Tax conversion lesson includes the current cost and the money that otherwise stayed invested, alongside the withdrawal alternative. Retirement follows a complete cash need through access, coverage, account/asset funding, sequence, sale/borrowing and the annual spending decision. Custody and Family connect operational ability, legal authority, no-secrets records and actual scoped evidence. Maintenance does not restart the whole course each month. Advanced work has a specific conditional application and its own demonstration rather than a repeated Core introduction.

See [the source and revision record](delivery/teaching-revision.md) for exact source handling, new illustrations and section-level repetition decisions. No private transcript, identifying client amount or original audio-listening claim is introduced. Earlier blanket completion claims remain historical, not evidence of teaching acceptance.

## Preserve these boundaries

Do not copy the video\'s 8% withdrawal assumption, multipliers, return path, price forecasts, universal account lockup or tax thresholds into this course. Do not change the accepted Reserve, fixture, original dictation, toolkit, capture register or pinned recovery inventory. Historical versions remain in Git; no old alternate master is restored.

Current facts, assumptions, expected events, scenarios, selected strategy and actual outside execution remain distinguishable. A new example does not silently establish a Reed decision, available security, tax result, policy quote or device proof. An app feature is described as demonstrated only after actual approved-build evidence.

## What happens after this written pass

There is no next unstarted manuscript batch in this scope. Review the clean course section by section for Austin\'s integrated voice and judgment, record corrections in the canonical files, and test the actual decision with an appropriate learner. Finish precise screen/procedure inserts and real outputs when the relevant redesign is ready. Material product-semantic changes reopen the affected explanation, not a blanket curriculum redesign.

Written preparation, owner acceptance, professional review, actual capture and student release remain separate states. The implementation PR records the actual checks and remote identities after they run. The temporary integration modules and write workflow must be removed before main integration. No unattended continuation, app/financial operation, changed entitlement or validated annual price is implied.
''')
    # Structural authoring sanity checks, not a model of teaching quality.
    after=paths()
    if after!=ps:raise ValueError('Unexpected path or inventory change')
    for lid in groups:
        read=section((ROOT/ps[lid]).read_text(),'Read aloud')
        if not read or '###' in read:raise ValueError('Broken spoken boundary')
    if blob((ROOT/ps['2.3']).read_bytes())!=RESERVE_BLOB:raise ValueError('Reserve changed')
    for lid in REVIEWED_PRACTICAL:
        if (ROOT/ps[lid]).read_text()!=originals[lid]:raise ValueError('Retained practical changed')
    print('APPLIED: 40 Core + 15 Advanced full replacements; 9 Core retained, 3.3 targeted cut, Reserve unchanged; 9 practical replacements, W02/W03 unchanged. Written review drafts only.')


def reader(out: Path) -> None:
    tool=runpy.run_path(str(ROOT/'tools/guided_course.py'))
    rows=tool['catalog'](ROOT); by={r['id']:r for r in rows}
    out.mkdir(parents=True,exist_ok=True)
    nav=[]; sections=[]
    for group,label in [(tool['CORE_IDS'],'Core course'),(tool['ADV_IDS'],'Conditional Advanced')]:
        nav.append('<h3>'+label+'</h3>')
        for lid in group:
            r=by[lid]; target=lid.replace('.','-')
            nav.append('<a href="#'+target+'">'+html.escape(lid+' · '+r['title'])+'</a>')
            paragraphs='\n'.join('<p>'+html.escape(p.strip()).replace('\n','<br>')+'</p>' for p in r['read'].split('\n\n') if p.strip())
            label2='Accepted Reserve reference' if lid=='2.3' else 'Written draft for voice review'
            sections.append('<section id="'+target+'"><p class="eyebrow">'+label2+'</p><h2>'+html.escape(lid+' — '+r['title'])+'</h2>'+paragraphs+'<a class="back" href="#top">Back to contents</a></section>')
    css='''body{margin:0;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#faf9f6;color:#24211d;line-height:1.75}header{padding:2rem;max-width:70rem;margin:auto}header h1{line-height:1.2}main{display:grid;grid-template-columns:20rem minmax(0,48rem);gap:3rem;max-width:74rem;margin:auto;padding:0 2rem 4rem}nav{position:sticky;top:0;height:96vh;overflow:auto;font-size:.88rem;padding-right:1rem}nav a{display:block;margin:.45rem 0;color:inherit;text-decoration:none}nav a:hover{text-decoration:underline}article{min-width:0}section{padding:1rem 0 4rem;border-bottom:1px solid #ddd}h2{font-size:1.8rem;line-height:1.3}p{font-size:1.1rem;margin:1.1rem 0}.eyebrow{font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:#665e53}.back{font-size:.9rem;color:inherit}header p{font-size:1rem;max-width:54rem}@media(max-width:850px){main{display:block;padding:0 1.2rem}nav{position:static;height:auto;max-height:26rem;border:1px solid #ddd;padding:1rem;margin-bottom:2rem}header{padding:1.2rem}h2{font-size:1.5rem}}@media print{nav,.back{display:none}main{display:block;max-width:none;padding:0}header{padding:0}section{break-before:page;border:0}p{font-size:11pt;line-height:1.6}}'''
    head='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Orange Plan — course reading copy</title><style>'+css+'</style><body><header id="top"><p class="eyebrow">Orange Plan Academy · review copy</p><h1>The complete spoken course</h1><p>Core lessons first; conditional Advanced lessons afterward. This copy contains spoken text only, not production notes. It is generated from the same canonical scripts as GitHub. The Reserve remains the accepted reference. Other wording is for Austin’s voice review; actual app/device recordings and professional checks remain separate.</p></header><main><nav>'+''.join(nav)+'</nav><article>'
    (out/'Orange_Plan_Complete_Reading_Copy.html').write_text(head+''.join(sections)+'</article></main></body></html>',encoding='utf-8')
    (out/'ALL-SCRIPTS.md').write_bytes((ROOT/'ALL-SCRIPTS.md').read_bytes())
    work=out/'Walkthroughs';work.mkdir(exist_ok=True)
    for lid in tool['PRACTICAL_IDS']:
        p=Path(by[lid]['path']);(work/p.name).write_bytes((ROOT/p).read_bytes())
    (out/'SOURCE-AND-SCOPE.md').write_bytes((ROOT/'delivery/teaching-revision.md').read_bytes())
    (out/'BUILD-IDENTITY.json').write_text(json.dumps({'commit':git('rev-parse','HEAD').strip(),'tree':git('rev-parse','HEAD^{tree}').strip(),'notice':'Generated review files; not recording or instructional-effectiveness approval.'},indent=2)+'\n')
    print('Generated source-matched reading artifact without external assets or fonts.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['apply','reader']);parser.add_argument('--out',type=Path,default=Path('/tmp/orange-plan-course-reading'))
    args=parser.parse_args()
    if args.command=='apply':apply()
    else:reader(args.out)
