#!/usr/bin/env python3
"""One-time, source-pinned editorial application. Removed after successful use.
Only the reviewed lesson edits and matching production notes are applied.
No model, provider, network, customer data or deployment operation.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEMP=['tools/_completion_edits_02_05.json','tools/_completion_edits_06_10.json','tools/_completion_edits_advanced.json','tools/_completion_working.json','tools/_complete_source_led.py']
HISTORY='45b34d923779b0936a8a906217255850c377dfa4'
def sha(data):return hashlib.sha256(data).hexdigest()
def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def section_span(text,name):
    m=re.search(r'^### '+re.escape(name)+r'\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S)
    if not m:raise ValueError('Missing section '+name)
    return m

manifest=json.loads((ROOT/'COURSE-MANIFEST.json').read_text())
rows={r['id']:r for r in manifest['lessons']}
counts=[2,5,5,6,7,5,8,4,4,3,2]
core={f'{m}.{n}' for m,c in enumerate(counts) for n in range(1,c+1) if m>=2}-{ '2.3' }
advanced={k for k in rows if k.startswith('A')}
expected=core|advanced
edits=[]
for p in TEMP[:3]:edits.extend(json.loads((ROOT/p).read_text()))
assert len(edits)==58 and {e['id'] for e in edits}==expected
working=json.loads((ROOT/TEMP[3]).read_text())
assert {w['id'] for w in working}=={'W02','W03','W04','W05','W06','W07','W08','W09','W10','D07'}
protected={str(p.relative_to(ROOT)):sha(p.read_bytes()) for base in ['source-material','archive','fixtures','toolkit'] for p in (ROOT/base).rglob('*') if p.is_file()}
for lid in ['0.1','0.2','1.1','1.2','1.3','1.4','1.5','2.3','W01']:
    p=rows[lid]['path'];protected[p]=sha((ROOT/p).read_bytes())
prepared={};evidence=[];errors=[]
for e in edits:
    row=rows[e['id']];p=row['path'];old=(ROOT/p).read_text()
    assert sha((ROOT/p).read_bytes())==row['source_sha256'], 'Source changed: '+p
    m=section_span(old,'Read aloud');body=m.group(1).strip();parts=re.split(r'\n\s*\n',body)
    replacement={0:e['opening']}
    for change in e.get('changes',[]):
        candidates=[i for i,part in enumerate(parts) if part.startswith(change['starts'])]
        if len(candidates)!=1:
            errors.append((e['id'],change['starts'],[part[:110] for part in parts]))
        else:
            i=candidates[0]
            if i in replacement:raise ValueError('Overlapping edit: '+e['id'])
            replacement[i]=change['new']
    last=len(parts)-1
    if last in replacement:replacement[last]+='\n\n'+e['finish']
    else:replacement[last]=e['finish']
    if e.get('insert_before_finish'):
        replacement[last]=e['insert_before_finish']+'\n\n'+replacement[last]
    newbody='\n\n'.join(replacement.get(i,part) for i,part in enumerate(parts))
    assert newbody!=body and len(newbody.split())>=250
    new=old[:m.start(1)]+newbody+'\n\n'+old[m.end(1):]
    new=re.sub(r'^Status:.*$',"Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.",new,count=1,flags=re.M)
    new+='\n### Source-led visual and teaching notes — not spoken\n\n'+e['visual']+'\n\nEditorial reason: '+e['reason']+'\n\nSee `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.\n'
    if e.get('demo'):
        new+='\n### Advanced demonstration plan — not spoken\n\n'+e['demo']+'\n\nUse this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.\n'
    prepared[p]=new
    evidence.append({'id':e['id'],'path':p,'before_sha256':sha(old.encode()),'after_sha256':sha((new.rstrip()+'\n').encode()),'reason':e['reason']})
if errors:
    for lid,prefix,starts in errors:
        print('ANCHOR_MISMATCH',lid,repr(prefix));print('\n'.join('  '+s for s in starts))
    raise SystemExit('No files changed: resolve all editorial anchors first.')
for w in working:
    row=rows[w['id']];p=row['path'];old=(ROOT/p).read_text()
    assert sha((ROOT/p).read_bytes())==row['source_sha256'],'Working source changed: '+p
    title='### Source-led recording detail — not spoken\n\n'
    detail=title+w['intro']+'\n\n'
    for b in w['beats']:
        detail+='**Chapter '+b['chapter']+'**\n\n'
        detail+='Prepare and demonstrate: '+b['rehearse']+'\n\n'
        detail+='Reusable narration: “'+b['say']+'”\n\n'
        detail+='Final screen/procedure insert: '+b['verify']+'\n\n'
        detail+='Member finish: '+b['finish']+'\n\n'
    detail+='The existing run sheet and these chapter details describe the same recording. No actual model result, provider/device operation, legal authority, listener test or publication approval is established by this written preparation. Any absent promised behavior remains held and reported; it is not silently replaced with a fabricated screen.\n\n'
    marker='### Readback and finish'
    assert old.count(marker)==1
    new=old.replace(marker,detail+marker,1)
    if w['id']!='W02':
        new=re.sub(r'^Status:.*$','Status: CAPTURE_HOLD — complete written recording plan prepared; exact build/procedure, actual results, tests and footage remain unverified.',new,count=1,flags=re.M)
    else:
        for a,b in [('**Chapter 4,','**Chapter 6,'),('### Reserve recording plan','### Readback and finish')]:
            original=old.split(a,1)[1].split(b,1)[0]
            assert original in new,'Accepted Reserve section altered'
    prepared[p]=new
    evidence.append({'id':w['id'],'path':p,'before_sha256':sha(old.encode()),'after_sha256':sha((new.rstrip()+'\n').encode()),'reason':'Prepared chapter-specific inputs, interpretation, reusable narration, exact remaining inserts and member finish.'})
# Primary sources support mechanisms only. Exact current examples and execution still need review.
primary_append='''\n## Source-led completion: targeted rechecks — 2026-09-08\n\nThis is targeted primary-source verification of the distinctions preserved in the edit, not a blanket legal/tax/device sign-off. No new provider quote, current market price or modeled household result is certified. Recheck at recording/execution.\n\n- IRS 2026-15 IRB, Notice 2026-20: eligible 2026 broker-held digital-asset identification relief is conditional; it does not make any app ordering setting automatically compliant. https://www.irs.gov/irb/2026-15_IRB\n- IRS Publication 590-B: Roth contribution/conversion/earnings ordering and distinct clocks; actual distribution facts matter. https://www.irs.gov/publications/p590b\n- IRS early-distribution exception table: IRA versus employer-plan exceptions, qualifying separation and governmental 457(b) distinctions. https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions\n- IRS SEPP guidance: rigid duration/method and improper-modification consequences require account-specific review. https://www.irs.gov/retirement-plans/substantially-equal-periodic-payments\n- IRS 2026-02 IRB, Notice 2026-5: current HSA coverage changes; no assumption every high-deductible or low-premium plan qualifies. https://www.irs.gov/irb/2026-02_IRB\n- IRS premium-tax-credit FAQ: use coverage-year income/eligibility and current advance-credit reconciliation, not a prior year's expanded terms. https://www.irs.gov/affordable-care-act/individuals-and-families/questions-and-answers-on-the-premium-tax-credit\n- FINRA SBLOC guidance: non-purpose use restrictions, variable rates, collateral changes and demand/forced-sale risk. https://www.finra.org/investors/insights/securities-backed-lines-credit\n- CFPB HELOC guidance: draw/repayment terms, rate and credit-availability conditions. https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-line-of-credit-heloc-en-107/\n- CFPB home-equity-contract overview: contingent future settlements can remain even with no monthly payment. https://www.consumerfinance.gov/data-research/research-reports/issue-spotlight-home-equity-contracts-market-overview/\n- Bitcoin developer block-chain guide and Bitcoin fee guide: UTXOs, spending and transaction size/fee-rate distinction; no current fee or universal dust threshold adopted. https://developer.bitcoin.org/devguide/block_chain.html and https://bitcoin.org/fees/\n- Trezor passphrase explanation: an exact different passphrase can lead to a different valid wallet; this is semantic verification, not approval of a device or recovery demonstration. https://trezor.io/guides/backups-recovery/advanced-wallets/what-is-a-passphrase\n- Microsoft primary passkey documentation: phishing-resistant, relying-party-bound credentials; no guarantee against every takeover or weak recovery path. https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless\n- NAIC disability consumer guidance: definition, limits, offsets, waiting period and duration differ by policy. No standard replacement percentage or waiting period is prescribed in the script. https://content.naic.org/article/consumer-insight-simplifying-complications-disability-insurance\n\nEstate authority, trust design, actual insurance contracts, loan agreements, program eligibility and manufacturer/model-specific recovery remain subject to their existing targeted professional/device gates. Historical provider claims in source decks are not treated as current endorsements.\n'''
primary=(ROOT/'PRIMARY-SOURCES.md').read_text()
assert '## Source-led completion: targeted rechecks' not in primary
prepared['PRIMARY-SOURCES.md']=primary.rstrip()+'\n'+primary_append
report='''# Source-led course completion\n\n## What is complete\n\nThe remaining 43 core explanations, all 15 conditional Advanced explanations, nine app working-session plans and the device demonstration plan received this targeted source-led editorial pass. Earlier 0.1–0.2, 1.1–1.5, W01 and the approved Reserve reference remain preserved. This completes the written editorial pass across the current 51 core, 15 Advanced and 11 practical components. It is not Austin's blanket voice approval, a successful student pilot, an app/device recording or launch readiness.\n\nThis pass retains good explanatory paragraphs and makes specific changes to the opening question, decision example, trade-off, finish and visual/recording guidance. It does not claim every sentence was rewritten. Advanced demonstrations remain conditional and return to their core lessons.\n\n## Source basis\n\nCurrent source checkpoint: `45b34d923779b0936a8a906217255850c377dfa4`. All remaining canonical lesson bodies and working run sheets were read before this edit. Original source-material and the approved September 8 Reserve judgment remain unchanged. Relevant uploaded source passages were retrieved from the Global Brain, Master Protocol Outline, Cash Flow + Reserve, Debt Strategy, Accounts + Allocation, Tax Strategy, updated Retirement Income, Custody, Estate/Inheritance and final Maintenance decks. Private call passages informed the learner's reserve, income/deduction and retracing-the-money questions; names, raw dialogue, personal balances and medical stories are not included here. Text and speaker-note access is not a claim of having listened to original audio or reviewed every slide visually.\n\nCurrent explicit owner direction and the accepted course structure govern conflicts. Old defaults, rigid priority/rate bands, blanket interest-only preferences, unconditional Roth claims, wealth-based custody ladders, universal inheritance secret splits, and claims that a failed simulation only needs a harmless spending cut are not restored from older sources. Primary references were rechecked for selected tax, financing, custody and healthcare mechanisms; details are in PRIMARY-SOURCES.md. Exact current-year execution and setup-specific claims retain their professional/capture reviews.\n\n## Important decisions now followed through\n\n- Current $500 cash flow, reduced-spending $1,700, and conditional post-card $1,605 remain separate; contributions and employer money are counted once.\n- Austin's conditional liquidity judgment carries into extra-debt and income-interruption decisions without rewriting the Reeds as single-income or making required payments optional.\n- The $850 college benchmark must compete with the same already-assigned money; a later start requires recalculation.\n- The $30,000 project leaves only $2,000 of a $32,000 reserve assignment if funded there; smaller/delay is a valid result, and a new payment needs a real source.\n- Asset-class fixture amounts are not verified security names or an actually available employer menu.\n- Conversions, spending cash and tax funding stay separate; current liquidity and after-tax resources inform the choice.\n- Account withdrawal and asset sale are separate decisions; meaningful retirement years explain the result.\n- A practice-wallet recovery proves that practice setup, not a different funded wallet's backup. Actual relevant recovery status remains open until verified.\n- The Family Custody Map, Heir Letter, Executor Packet, insurance audit, Household Plan Summary and Annual Plan Refresh now appear directly in the matching teaching and recording plans.\n- Standing portfolio guardrails are not spending amounts, and repeatedly saving an annual adjustment is not a way around a policy limit.\n- The final summary describes one saved plan phase; it cannot combine current debt with future released money or use illustrative landing-page results.\n\n## Recording and publication remain separate\n\nExact navigation, source/holdings/history behavior, save/reload, tax/model outcomes, guardrails, reports, Ask and optional communication/export features require the approved build and actual results. The fixed source household remains a simplified arithmetic fixture, not a calibrated saved plan. Missing capture dates, benefits, tax mapping, full debt schedules and security identities need a reviewed fictional extension before the relevant run.\n\nDevice footage requires the exact official procedure, setup and safe test. Family/listener tests, member pilot, professional sign-offs and live support setup remain unperformed unless separate evidence establishes them. No app repository, financial engine, provider, hosted record, wallet, Production, rollout, commercial term or merge operation is authorized by this edit.\n\n## Per-component editorial record\n\n| ID | Canonical file | Specific improvement |\n|---|---|---|\n'''
for r in evidence:report+=f"| {r['id']} | `{r['path']}` | {r['reason']} |\n"
report+='\nThe existing generator, arithmetic, mutation and member-deliverable checks must pass before a completion handoff. Actual run evidence belongs in the PR; this report does not assume a run succeeded. Repository cleanup is separately recorded in its recovery manifest.\n'
prepared['delivery/source-led-completion.md']=report
for p,text in prepared.items():write(p,text)
for p,h in protected.items():assert sha((ROOT/p).read_bytes())==h,'Protected source changed: '+p
for p in TEMP:(ROOT/p).unlink()
print('APPLIED: 43 core, 15 Advanced, 9 app plans and 1 device plan; approved reference and original sources unchanged.')
print('Prepared-file count:',len(prepared))
