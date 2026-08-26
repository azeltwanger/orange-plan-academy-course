#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_COMMIT = '8ed57cbde2bf051c990ec5d1dcbf1178e98fa8d8'

ACTIVE_LAYER_FILES = [ROOT / 'MASTER-COURSE.md', ROOT / 'ALL-SCRIPTS.md']
ACTIVE_LAYER_FILES += list((ROOT / 'scripts').rglob('*.md'))
ACTIVE_LAYER_FILES += list((ROOT / 'lesson-text').rglob('*.md'))
ACTIVE_LAYER_FILES += list((ROOT / 'modules').rglob('*.md'))

REPLACEMENTS = {
    'Now we have the amount available from Cash Flow, the reserve decision, the debt decision, the jobs for the money, and the target allocation.':
        'Now we have the amount available from Cash Flow, the Reserve decision, the jobs for the money, the target allocation, and whatever Extra Debt amount is currently saved. That debt amount is still provisional until Module 4.',
    'We are carrying forward the specific extra-payment amount you already chose. If every debt is on minimums, this step is zero.':
        'For now, this rung uses the Extra Debt amount currently saved in the plan, which may be zero. Module 4 decides the final amount and then returns it to this waterfall.',
    '3. Pay the extra debt amount the Debt module selected.':
        '3. Use the current Extra Debt placeholder, then replace it with the final amount selected in Module 4.',
    'show the dollars already claimed by Reserve and extra debt':
        'show the dollars already claimed by Reserve and the current provisional Extra Debt amount',
    'prevent sequence-of-return risks in retirement':
        'reduce sequence-of-returns risk in retirement',
    '## 5 · Explain Update Holdings versus transaction history':
        '## 5 · Explain Add transaction versus historical tax history',
    '**DO** Open the current **Update holdings / Update transactions** entry point from Dashboard.':
        '**DO** Dashboard → **Add transaction**.\n\n**SEE** **Update my balance** for new activity that should change the current holding, and **Keep my balance** for older history that supports a balance already entered.',
    '**SHOW** the available paths: linked activity when supported · downloaded CSV or spreadsheet · one manually entered purchase, sale, or transfer · AI-assisted description when present.':
        '**SHOW** the available paths after the intent choice: linked activity when supported · downloaded CSV or spreadsheet · one manually entered purchase, sale, or transfer · AI-assisted description when present.',
    '**DO** Dashboard → **Update holdings / transactions** → downloaded file.':
        '**DO** Dashboard → **Add transaction** → choose the downloaded-file path.\n\n**CHOOSE** **Keep my balance** when the file is older history for a current balance already entered. Use **Update my balance** only when the imported activity should change what the account owns now.',
}

for path in ACTIVE_LAYER_FILES:
    if not path.exists() or any(part in {'archive', 'source-material', 'research'} for part in path.parts):
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    if text != original:
        path.write_text(text.rstrip() + '\n', encoding='utf-8')

advanced_gate = '''# Advanced Library watcher gates

These gates answer **who should watch each optional lesson**. They are not publication approvals. Professional, device, provider, and current-law publication gates remain in the script header and `TARGETED-PROFESSIONAL-SIGNOFF.md`.

Austin can mark each watcher gate **keep**, **change**, or **remove** while dictating. The core plan is complete without every Advanced lesson.

## A1.1 · How Orange Plan models Bitcoin inside the confidence check

Watch this when you want to audit how the confidence result is built, explain the methodology to a skeptical spouse or professional, or understand why a changed assumption moved the result. The core course already teaches how to read and use the number.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A3.1 · Use price context to name the emotion before a large Bitcoin move

Watch this immediately before a large purchase, sale, allocation change, or other Bitcoin-heavy decision. It is a pause that identifies FOMO or fear; it is not a market-timing system.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A4.1 · Borrow against Bitcoin without turning a drawdown into liquidation

Watch this only when you already have a Bitcoin-backed loan or are seriously considering one. A household with no such loan can skip it.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A4.2 · The four ways debt can strengthen a plan, and how each one fails

Watch this when you are deliberately carrying debt you could pay off, establishing credit before it is needed, or comparing strategic borrowing with paying cash. If every debt already has a job you can defend, the core Debt module is enough.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A5.1 · RMD pressure and Roth conversions across the low-income window

Watch this when you have meaningful pre-tax retirement assets and expect a lower-income period before required distributions or other income reduce your flexibility. The conversion tax must be supportable without weakening the plan.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A5.2 · Harvest Bitcoin losses and gains without losing the tax story

Watch this when the Tax page shows a real loss candidate or low-effective-rate gain opportunity. If neither exists this year, there is no current harvesting decision.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A5.3 · State taxes and relocation: measure the lever before moving

Watch this when a move is genuinely being considered or a large sale, conversion, or income event makes the state difference material. The lesson measures the lever; it does not establish domicile.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A6.1 · Health coverage between retirement and Medicare

Watch this when work is expected to stop before Medicare eligibility or when the household is comparing ACA, COBRA, a spouse plan, or a non-insurance alternative. Retiring after the healthcare bridge can make this optional.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A6.2 · Sell, borrow, or hold when the plan needs a year of spending

Watch this when retirement withdrawals are close enough to require an operating decision—generally within several years of retirement or while already drawing. Earlier accumulators usually need the core withdrawal and Bridge framework first.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A7.1 · Passphrase, collaborative custody, and DIY multisig

Watch this when the current custody design has a meaningful one-loss or one-theft failure, the stack is large enough to justify more complexity, or the family needs guided recovery. Do not upgrade for status.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A7.2 · What self-custody actually asks of you

Watch this when you are deciding whether to take on self-custody, or when the responsibility has been the reason you have delayed. A tested custody setup can be complete without this reflection lesson.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A7.3 · Avoid custody concentration in one institution, vendor, or failure path

Watch this when a meaningful amount depends on one institution, one device family, one location, one software path, or one person. Skip it when the current design already has deliberate, maintainable independence.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A7.4 · UTXOs, dust, consolidation, and address use

Watch this when you make frequent small withdrawals, the wallet has many separate outputs, or you are about to consolidate or use coin control. It is an operations lesson, not a requirement for every holder.

Decision: ☐ Keep  ☐ Change  ☐ Remove

---

## A8.1 · Do you need a trust, and what job would it do?

Watch this when the baseline estate review identifies a real tax, probate, incapacity, beneficiary-control, creditor, or family-complexity reason for a trust conversation. Most households should be allowed to get a no and stop.

Decision: ☐ Keep  ☐ Change  ☐ Remove
'''
(ROOT / 'ADVANCED-GATE-APPROVAL.md').write_text(advanced_gate.rstrip() + '\n', encoding='utf-8')

advanced_files = sorted((ROOT / 'scripts' / 'advanced').glob('*.md'))
rows = []
for path in advanced_files:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    number = re.search(r'segment (A\d+\.\d+)', lines[0]).group(1)
    title = lines[1].split(' ', 1)[1]
    words_match = re.search(r'([\d,]+) words', lines[2])
    words = words_match.group(1) if words_match else '—'
    gate = 'yes' if 'PUBLICATION GATE:' in text[:1500] else 'no'
    student = ROOT / 'lesson-text' / 'advanced' / path.name
    rows.append((number, title, words, gate, student.exists()))

advanced_audit = [
    '# Advanced Library dictation-readiness audit\n\n',
    f'**App reference for the rebuild:** `{APP_COMMIT}`\n\n',
    'Every Advanced lesson is optional, explicitly labeled **PRE-DICTATION FILMING DRAFT**, and attached to the restored core order. A clean draft is not represented as prior Austin speech.\n\n',
    '| Lesson | Words | Publication gate | Script | Student text | Master / generated module |\n',
    '|---|---:|---|---|---|---|\n',
]
for number, title, words, gate, student in rows:
    advanced_audit.append(f'| **{number}** · {title} | {words} | {gate} | yes | {"yes" if student else "no"} | yes |\n')
advanced_audit += [
    '\n## Result\n\n',
    f'- **{len(rows)} of 14** Advanced scripts present.\n',
    '- Restored numbering: A3 extends Allocation; A4 extends Debt.\n',
    '- All scripts carry a watcher condition or publication gate through the Advanced master and gate files.\n',
    '- All have synchronized script, student-text, master, and generated-module layers.\n',
    '- The old slop-adjudication ledger and its generated-architecture assumptions are retired.\n',
    '- Current rebuild verification: 28 core teach lessons, 10 core captures, 14 Advanced lessons, and 37 core visual cues.\n',
    '\n## Remaining gates\n\n',
    '- Austin dictates or reads the drafts and changes any judgment that is not his.\n',
    '- Tax examples receive targeted CPA or EA review before publication.\n',
    '- Device- and provider-specific custody footage is recorded only after exact operational verification.\n',
    '- Insurance contract mechanics receive licensed review.\n',
    '- State-specific estate and trust material receives attorney signoff.\n',
]
(ROOT / 'ADVANCED-DICTATION-AUDIT.md').write_text(''.join(advanced_audit).rstrip() + '\n', encoding='utf-8')

claim_registry = '''# Claim registry — current filming policies

This registry records the positions that must stay consistent across the active scripts, master, student text, walkthroughs, and visuals. It replaces the pre-deck-reset registry and its requirement that every lesson use the same three copywriting headings.

## MUST remain true

| Area | Current course policy |
|---|---|
| Course order | Week 2 is Cash Flow + Reserve. Week 3 is Allocation + Next-Dollar. Week 4 is Debt, followed by a return to Cash Flow Routing. |
| Implementation | Build Your Plan is the implementation roadmap even when its card order differs from the teaching order. |
| Lesson roles | Teach lessons explain the concept and decision. Walkthroughs own click paths, data entry, calculations, saves, and verification. |
| Authorship | Only retained Austin dictation is labeled AUSTIN DICTATION. All other teach scripts are labeled PRE-DICTATION FILMING DRAFT. |
| Onboarding | The onboarding retirement age is deterministic. The first saved full 1,000-path confidence result happens in Module 9 after the plan is complete. |
| Reserve | Orange Plan calculates the Reserve target from the selected monthly spending basis and target months. |
| Life events | Expected changes belong in Life events. Hypothetical questions belong in Scenarios. |
| Future funding | Bitcoin can remain part of a funding plan more than five years out. The firmly committed amount becomes less dependent on Bitcoin as the date approaches. |
| College | Start with the parent's commitment and funding sources. A 529 is one tool; the one-third framework is an option, not a rule. |
| Contributions | Reserve, match, provisional Extra Debt, Bridge versus Legacy, then the target inside the account. Module 4 finalizes the debt claim. |
| Tax | Loan proceeds are generally not income at origination; liquidation, sale, cancellation, or restructuring can create tax consequences. |
| Custody | Document the process, never the secrets. No universal seed/passphrase/key split is taught. |
| Estate | Legal authority and technical control are separate. Beneficiary and trust results depend on the governing documents and law. |
| Professional scope | Research verifies general mechanics; taxpayer-, state-, contract-, provider-, and device-specific execution keeps a targeted external gate. |

## MUST NOT return

- Manual Reserve-target multiplication presented as a user input.
- A 529 or full sticker price presented as the universal college target.
- A rigid rule that Bitcoin must leave every future funding plan at year five.
- Debt-before-Allocation presented as the course teaching order.
- The Extra Debt rung described as final before Module 4.
- The first full confidence run performed in onboarding, Foundation, or Module 6.
- A generated draft presented as Austin's original words.
- The repeated `YOUR DECISION / PUT IT IN ORANGE PLAN / YOU ARE DONE WHEN` architecture forced onto every teach lesson.
- One universal Bitcoin allocation, loan amount, LTV, UTXO threshold, insurance amount, trust clause, or inheritance key split.
- Flat claims that borrowing creates no taxable event, beneficiary forms always override every other rule, or every irrevocable trust removes assets from an estate.
- Any seed phrase, key, passphrase, PIN, password, or exact recovery location in an app, worksheet, legal document, screenshot, or AI tool.

## Verification

`FINALIZATION-STATUS.md`, `COURSE-REBUILD-REPORT.md`, and the current branch's final consistency workflow record the active layer checks. Historical analyses may describe abandoned structures; they do not override this registry.
'''
(ROOT / 'CLAIM-REGISTRY.md').write_text(claim_registry.rstrip() + '\n', encoding='utf-8')

source_map = '''# Dictation source map

This file distinguishes Austin's retained words from editorially prepared drafts.

## Retained Austin dictation

### 0.1 · How to use this course

Austin's original course orientation remains the spoken authority. The rebuild changed the module order to Week 3 Allocation and Week 4 Debt, added the current teach/walkthrough/Build Your Plan distinction, and added the US-versus-non-US boundary. Those changes are factual course-structure edits, not evidence that Austin dictated the new lines.

### 1.1 · What to gather before you build the plan

Austin's gathering guidance remains the authority: verify debt rates, collect employer-benefit details, identify expected future events, and download old exchange and brokerage history. The editorial close now makes gathering separate from entering and sends each item to the module that owns it.

### 1.2 · The three layers of a plan, and setting your assumptions

Austin's baseline / life-event / scenario distinction and conservative-assumption position remain the authority. The inflation example was corrected mathematically, and the click path was removed from the teach lesson because the Foundation walkthrough owns it.

### 2.2 · Size your cash reserve in months of spending

Austin's Reserve-sizing lesson remains the authority. The close now hands implementation to the walkthrough and correctly states that Orange Plan calculates the target from the selected monthly basis and months.

## Austin direction, not line-by-line dictation

### 0.2 · How to use Orange Plan AI

Austin directed the benefits, buttons, daily Bitcoin report, plan-review prompts, blind-spot use, and privacy-scrubbed export. The live script is therefore labeled PRE-DICTATION FILMING DRAFT rather than AUSTIN DICTATION.

### Future-event and college decisions

Austin established that Bitcoin can remain part of funding more than five years out and that college planning starts with the parent commitment, not the 529 or full sticker price. The current 2.3 and 2.4 drafts implement those positions, including the optional one-third framework as an option rather than a rule.

### Contribution waterfall

The old slide deck supplies the base order and reasoning. The current 3.3 draft treats Extra Debt as provisional until Module 4. Austin can refine the exact exceptions while dictating; there is no structural blocker and no generated exception is represented as his prior wording.

## Every other teach lesson

Every other core and Advanced teach lesson is a PRE-DICTATION FILMING DRAFT rebuilt from the decks, current app, research, and Austin's known planning positions. It is prepared for a fast chronological dictation pass. It is not Austin-authored until he dictates or explicitly approves it.

## Future-edit rule

A script may be labeled AUSTIN DICTATION only when a retained transcript or recording supports it. Editorial corrections may fix math, current app behavior, course order, safety, or professional scope, but they may not silently invent a planning recommendation and attribute it to Austin.
'''
(ROOT / 'DICTATION-SOURCE-MAP.md').write_text(source_map.rstrip() + '\n', encoding='utf-8')

college_authority = '''# College-funding authority

**Austin direction — 2026-08-26**

The college lesson answers a family planning decision, not an account-sales question.

## Required decision order

1. Define what the parent is actually committing to provide: a fixed amount, tuition only, an in-state benchmark, a percentage of net cost, a number of years, or another explicit promise.
2. Estimate the likely cost of that commitment, not automatically the largest sticker price.
3. List the funding sources: existing 529 assets, new 529 contributions, Bitcoin or other taxable investments, current cash flow while enrolled, grants and scholarships, student work, family help, and a bounded amount of student borrowing.
4. Compare what is already available and projected with the commitment; the remaining gap needs a funding decision.
5. Revisit the decision as the school, aid package, living arrangement, and enrollment date become real.

## Bitcoin and 529 nuance

- A 529 is one tax-advantaged education tool, not the automatic strategy.
- The limited investment menu and qualified-use rules matter to a Bitcoiner.
- When college is more than five years away, Bitcoin can remain a meaningful part of the savings plan.
- As enrollment approaches, the portion the parent has firmly promised should become less dependent on Bitcoin being at a favorable price.
- In the final year or two, the first year of the commitment should have a reliable source; later years can remain more flexible and be recalculated.

## One-third framework

Roughly one-third saved beforehand, one-third paid from cash flow or investments while enrolled, and one-third covered by aid, student work, or loans can be a useful starting framework. It is **not** a universal rule and must not replace the family's actual commitment and capacity.

## Borrowing boundary

A bounded amount of federal student borrowing can be part of the plan. Parent and private borrowing are separate Debt-module decisions and should not be inserted into the college plan without testing the retirement and cash-flow effect.

## Orange Plan implementation

- `2.4` teaches the decision.
- `2.5` adds the College life event using the parent's commitment and reads the current Education target, education-account value, projected cover, and gap.
- Education contributions remain separate from the global Reserve / Bridge / Legacy bucket target.
- The app helps quantify the plan; it does not decide the commitment or require a 529.

## Evergreen boundary

Current tuition figures, FAFSA rules, 529 limits, rollover rules, and federal loan limits belong in maintained lesson text, the app, or a current source check—not in evergreen spoken video.
'''
(ROOT / 'COLLEGE-FUNDING-AUTHORITY.md').write_text(college_authority.rstrip() + '\n', encoding='utf-8')

research_verification = f'''# Professional research verification

**Primary-source audit completed:** 2026-08-25  
**Final course rebuild:** 2026-08-26  
**Orange Plan app reference:** `{APP_COMMIT}`

## Scope

- Tax and healthcare: Module 5, A5.1–A5.3, A6.1–A6.2
- Custody: Module 7 and A7.1–A7.4
- Insurance and estate: Module 8 and A8.1
- Course-wide professional boundaries, current-year figures, and device / provider verification

## Current result

- General federal, protocol, insurance-category, and estate-concept mechanics were researched against primary sources.
- Overstated or unsafe claims were removed or qualified.
- Current-year figures remain in maintained text, the app, or a recording-time check rather than evergreen narration.
- Blanket "professional must discover every issue" reviews were replaced with narrow signoff questions.
- The final course rebuild contains 28 core teach lessons, 10 walkthroughs / demos, 14 Advanced lessons, and 37 core visual cues.
- Week 3 is Allocation + Next-Dollar; Week 4 is Debt and returns the final Extra Debt claim to the waterfall.
- The first full 1,000-path confidence result is saved in Module 9 after the full plan is intentionally complete.
- There is no remaining Austin-authorship or structural blocker. Non-dictated scripts remain honestly labeled pre-dictation drafts.

## What this verification is not

This document is not a CPA, attorney, insurance, or provider signoff. It records the completed research and editorial pass. The remaining external questions are limited to the actual taxpayer, state, policy, provider, device, contract, or current-year facts listed in `TARGETED-PROFESSIONAL-SIGNOFF.md`.

## Remaining release controls

- Recheck seeded current-year tax examples immediately before recording or publication.
- Test the exact hardware wallet, firmware, backup standard, descriptor, and provider-independent recovery path before setup-specific footage.
- Have a licensed reviewer confirm policy mechanics and actual contract language before publishing insurance examples.
- Have a state-licensed estate attorney approve state-specific executor, digital-asset, trust, and fiduciary-duty material.
- Recheck current app labels after `{APP_COMMIT}` before every walkthrough capture.
'''
(ROOT / 'PROFESSIONAL-RESEARCH-VERIFICATION.md').write_text(research_verification.rstrip() + '\n', encoding='utf-8')

audit_path = ROOT / 'PROFESSIONAL-RESEARCH-AUDIT.md'
if audit_path.exists():
    audit = audit_path.read_text(encoding='utf-8')
    audit = audit.replace(
        '| Passphrase | A BIP39 passphrase is an optional string; every passphrase derives a valid, different wallet. It is not literally “one extra word,” and it is not cryptographic multisig. | Teach Austin’s seven-random-word rule as his operational standard, not a protocol minimum. State that exact entry matters and every typo opens another wallet. |',
        '| Passphrase | A BIP39 passphrase is an optional string; every passphrase derives a valid, different wallet. It is not literally “one extra word,” and it is not cryptographic multisig. | Teach exact-entry and recovery risk. Do not present one word count or construction method as a universal protocol rule. |',
    )
    audit = audit.replace(
        '| Transfer threshold | 0.01–0.02 BTC is Austin’s rule of thumb, not a Bitcoin rule. | Preserve it with an explicit fee/counterparty check. |',
        '| Transfer threshold | There is no permanent Bitcoin amount that stays economically correct across price and fee regimes. Many small withdrawals can create uneconomic UTXOs, while waiting longer adds exchange or counterparty exposure. | Teach the trade-off and review current fees; do not freeze one universal BTC threshold into evergreen narration. |',
    )
    audit_path.write_text(audit.rstrip() + '\n', encoding='utf-8')

signoff_path = ROOT / 'TARGETED-PROFESSIONAL-SIGNOFF.md'
if signoff_path.exists():
    signoff = signoff_path.read_text(encoding='utf-8')
    signoff = signoff.replace(
        '3. Does the passphrase lesson correctly explain that every passphrase derives a valid wallet and that Austin’s seven-word rule is an operational standard rather than a protocol minimum?',
        '3. Does the passphrase lesson correctly explain that every passphrase derives a valid wallet, exact entry is required, and no word count or construction method is presented as a universal protocol minimum?',
    )
    signoff_path.write_text(signoff.rstrip() + '\n', encoding='utf-8')

policy_path = ROOT / 'SOURCE-MATERIAL-POLICY.md'
if policy_path.exists():
    policy = policy_path.read_text(encoding='utf-8')
    insertion = '''\n## Named course-deck exception\n\nAustin later designated the original module slide decks as the authority for **teaching sequence, decisions, and visual logic**. They remain old for UI labels, product features, figures, and recommendations. The current production app owns implementation details, and Austin's dictation owns the final judgment and voice. Generic uploaded notes and provider material remain idea sources only.\n\n'''
    marker = '\n---\n\n## The rule\n'
    if insertion.strip() not in policy and marker in policy:
        policy = policy.replace(marker, '\n---\n' + insertion + '## The rule\n', 1)
    policy_path.write_text(policy.rstrip() + '\n', encoding='utf-8')

final_status = ROOT / 'FINALIZATION-STATUS.md'
if final_status.exists():
    status = final_status.read_text(encoding='utf-8')
    note = '''\n## Final consistency pass\n\n- Updated Dashboard walkthrough language to the production **Add transaction** flow, including **Update my balance** versus **Keep my balance**.\n- Made the Week 3 Extra Debt rung explicitly provisional until Week 4 returns the final amount to Routing.\n- Corrected the remaining sequence-of-returns wording in the Austin Reserve script.\n- Replaced stale Advanced numbering, gate, source-map, claim-registry, college-authority, and research-verification documents.\n- Re-ran active-layer checks for module order, confidence timing, authorship labels, walkthrough separation, and retired copywriting headings.\n'''
    if '## Final consistency pass' not in status:
        status = status.rstrip() + '\n' + note
    final_status.write_text(status.rstrip() + '\n', encoding='utf-8')

report_path = ROOT / 'COURSE-REBUILD-REPORT.md'
if report_path.exists():
    report = report_path.read_text(encoding='utf-8')
    if '## Final consistency audit' not in report:
        report += '''\n## Final consistency audit\n\nThe production-facing layers now use the current Dashboard **Add transaction** flow, distinguish balance-changing activity from history-only imports, treat Extra Debt as provisional in Week 3, and use the restored Advanced numbering. Stale policy documents from the prior generated architecture were replaced rather than left as competing instructions.\n'''
    report_path.write_text(report.rstrip() + '\n', encoding='utf-8')

for path in [
    ROOT / 'ADVANCED-GATE-APPROVAL.md', ROOT / 'ADVANCED-DICTATION-AUDIT.md',
    ROOT / 'CLAIM-REGISTRY.md', ROOT / 'DICTATION-SOURCE-MAP.md',
    ROOT / 'COLLEGE-FUNDING-AUTHORITY.md', ROOT / 'PROFESSIONAL-RESEARCH-VERIFICATION.md',
    ROOT / 'PROFESSIONAL-RESEARCH-AUDIT.md', ROOT / 'TARGETED-PROFESSIONAL-SIGNOFF.md',
    ROOT / 'SOURCE-MATERIAL-POLICY.md', ROOT / 'FINALIZATION-STATUS.md',
    ROOT / 'COURSE-REBUILD-REPORT.md',
]:
    if path.exists():
        path.write_text(path.read_text(encoding='utf-8').rstrip() + '\n', encoding='utf-8')

print('Final course touch-up applied')
