#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from tax_replacements import FILES as TAX_FILES
from custody_replacements import FILES as CUSTODY_FILES
from estate_insurance_replacements import FILES as ESTATE_INSURANCE_FILES

ROOT = Path(__file__).resolve().parents[1]
DIVIDER = "=" * 60


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one exact match, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    text, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one regex match, found {count}")
    return text


def add_script_header(path: str, line: str) -> None:
    text = read(path)
    if line in text:
        return
    if DIVIDER not in text:
        raise RuntimeError(f"{path}: no teleprompter divider")
    head, body = text.split(DIVIDER, 1)
    write(path, head.rstrip() + "\n" + line + "\n" + DIVIDER + body)


# Write all researched script and student-text replacements.
for path, content in {**TAX_FILES, **CUSTODY_FILES, **ESTATE_INSURANCE_FILES}.items():
    write(path, content)

# The short A7.2 script was already calibrated; add the research provenance without
# changing its planning position.
add_script_header(
    "scripts/advanced/A7-2_what-self-custody-actually-asks-of-you.md",
    "RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md",
)

# Fix the sync tool so the last lesson in an Advanced module cannot swallow the
# next module heading when the researched script is pushed back into the master.
sync_tool = read("tools/sync-master-from-script.py")
sync_tool = sync_tool.replace(
    "r'\\n## (?:A?\\d+\\.\\d+|✂)|\\n# Unit '",
    "r'\\n## (?:A?\\d+\\.\\d+|✂)|\\n# Unit |\\n# Advanced Module '",
)
write("tools/sync-master-from-script.py", sync_tool)

# Safe hardware-wallet demonstration: backup check / spare restore first; a
# destructive reset remains an optional throwaway demonstration, not the default
# proof a student is told to run on the only live device.
write("scripts/07-4_DEMO_hardware-wallet-exchange.md", r'''
# 7.4 · DEMO — Hardware wallet setup + exchange hardening

**External screen record · 3 beats · ~10 min final** — NOT Orange Plan. Vendor tools only.

> **DO** = do this on camera · **SEE** = point at this · **⚠** = don't get this wrong
> Narrate in your own words. Nothing here is scripted.

---

## Before you record

- [ ] Exact device, firmware, official setup guide, and backup standard documented
- [ ] Manufacturer or authorized-source device; throwaway demo wallet only
- [ ] Spare compatible device or vendor-supported backup-check feature ready
- [ ] Demo exchange account with no real personal data
- [ ] Camera/reflection plan tested; no backup, passphrase, PIN, private key, QR, descriptor, or account secret can enter frame

**⚠ PRODUCTION SAFETY IS THE JOB.** Review the finished footage frame by frame before publication.

---

## □ 1 · Hardware wallet: prove recovery safely (~6:00)

**DO 1** Verify the device source, authenticity procedure, official software, and firmware path.

**DO 2** Generate a new throwaway wallet on the device. Never use words or a PIN supplied in the package.

**DO 3** Record the backup offline and name the actual standard. Show only the physical act, never the words or shares.

**DO 4** Use the manufacturer's backup-check feature when available.

**DO 5** Send a trivial test transaction and verify the receive address on the device's trusted display.

**DO 6** Restore on a spare compatible device or approved recovery environment. Verify the intended wallet fingerprint/address and the test transaction.

**OPTIONAL DESTRUCTIVE BEAT** On a throwaway device only, after the backup has already passed the non-destructive check, demonstrate factory reset and recovery under the exact vendor procedure.

**⚠** Destructive wiping is not the student's first backup test and never happens on the only working copy of a meaningful balance.

**⚠** For passphrase or multisig, the demo is incomplete until the exact passphrase or wallet policy/descriptor is restored and the intended wallet is verified.

---

## □ 2 · Exchange and email hardening (~3:00)

**DO 1** Secure the primary email with a unique password and a passkey or hardware security key where supported. Show a backup key or recovery-code plan stored separately.

**DO 2** Secure the exchange with a unique password.

**DO 3** Use a passkey/security key when supported; otherwise use an authenticator app. SMS is the last choice.

**⚠** TOTP is stronger than SMS but is not phishing-resistant merely because it is an app.

**DO 4** Review active sessions, recovery methods, withdrawal allowlists/delays, and secondary approval where the provider supports them.

**⚠** Name vendors as examples, not endorsements. Controls and recovery paths change.

---

## □ 3 · The never-list (~1:00) — camera, no screen

- Never type or photograph wallet recovery material for a website, chat, support form, ordinary computer, phone note, or AI.
- Never use a pre-generated backup supplied with a device.
- Never approve a destination shown only on the computer or phone.
- Never respond to an urgent recovery message through the link it supplied.
- No legitimate support person needs the wallet backup, private key, passphrase, or PIN.

---

## □ WRAP

- [ ] Backup check and spare-device recovery shown
- [ ] Optional destructive reset clearly labeled throwaway-only
- [ ] Intended wallet/address verified, not merely words accepted
- [ ] Passkey/security-key option shown before TOTP and SMS
- [ ] Recovery codes / backup authenticator stored separately
- [ ] Footage reviewed for reflections and hidden screens

**END**
''')

write("lesson-text/07-4_demo-hardware-wallet-exchange.md", r'''
# External demo: hardware wallet setup and exchange hardening

Use a throwaway wallet, the exact current manufacturer guide, and no personal data.

## Hardware-wallet proof

1. Verify source, official software, firmware, and backup standard.
2. Generate the backup on the clean device; never use supplied recovery words.
3. Run the vendor-supported backup check first.
4. Send a trivial test and verify the receive address on the hardware display.
5. Restore on a spare compatible device or approved environment and verify the intended wallet.
6. A destructive reset is optional throwaway footage only after a non-destructive check—not the first test on the only live device.

For passphrase or multisig, restore the exact passphrase or wallet policy/descriptor too.

## Account hardening

Use passkey or hardware security key where supported, TOTP second, SMS last. Secure the email first, store backup keys/recovery codes separately, and review withdrawal controls and support recovery.

**Complete when:** recovery was proved without exposing a secret or risking the only working copy of a meaningful balance.
''')

# Tax walkthrough corrections.
path = "scripts/05-3_WALKTHROUGH_model-it-tax.md"
text = read(path)
text = text.replace(
    "**SEE** Neighbors: **Add transaction** (single buy/sell/transfer) · **Transfer** (moves holding + basis, NOT a sale, no taxable event)",
    "**SEE** Neighbors: **Add transaction** (single buy/sell/transfer) · **Transfer** (moves holding + basis and is generally not a disposition when both wallets belong to the taxpayer; Bitcoin used as a transaction fee can still have tax consequences)",
)
old = '''**⚠ Say this slowly. Every client gets stuck here.**

**⚠** The conversion tax is **not** paid out of the account you converted. You do not "withdraw to pay it," and there's no penalty involved. It's an ordinary tax bill, due at tax time, paid like any other tax bill — from cash, or by selling from your taxable account.

**SEE** Point at the two pots on screen: the retirement account (moving) · the taxable account / checking (paying)

**⚠ Pay it from OUTSIDE.** Convert $30,000, owe $3,600. Pay from taxable or checking and the full $30,000 compounds tax-free. Pay it out of the conversion and only $26,400 lands.

**⚠ Say this out loud:** "so we'd be selling from the taxable Bitcoin, not from the account we just converted."'''
new = '''**⚠ Say this slowly. Every client gets stuck here.**

**⚠** A Roth conversion generally creates ordinary income. The tax can be covered from checking, taxable assets, withholding, or estimated payments, but those paths are not economically identical.

**SEE** Point at the two pots on screen: the retirement account being converted · the outside cash or taxable account used to cover the tax.

**⚠** Paying from outside keeps the full conversion in Roth. Withholding or distributing part of the retirement account leaves less in Roth and, before age 59½, the amount not converted may also be an early distribution unless an exception applies.

**⚠** Use the app to size a proposed conversion; use the current return and tax professional to decide payment timing, withholding, estimates, and filing treatment.'''
text = replace_once(text, old, new, "tax walkthrough conversion funding")
text = text.replace(
    "- [ ] Conversion fills the bracket, doesn't spill",
    "- [ ] Conversion is sized from the all-in marginal cost: bracket, gains, ACA/IRMAA, NIIT, state, deductions, and credits",
)
text = text.replace(
    "**⚠** Hand-off: your CPA doesn't need the app. They need the 8949, the one-page conversion schedule, and your question list.",
    "**⚠** Hand-off: give the tax professional the 8949 export, the conversion schedule, basis-status list, state assumption, healthcare interaction, and exact questions. The app is the model; the return position still needs substantiation.",
)
write(path, text)

path = "lesson-text/05-3_walkthrough-model-it-tax.md"
text = read(path)
text = text.replace(
    "A transfer moves the holding and its basis. It is not a sale and has no tax consequence.",
    "A transfer between the taxpayer's own wallets generally is not a disposition, but Bitcoin used to pay a transaction fee can have tax consequences. Carry the lot history with the transfer.",
)
text = text.replace(
    "Pay conversion tax from outside the converted account.",
    "Model conversion tax from outside cash versus withholding. Outside payment keeps the full conversion in Roth; withholding can create a separate distribution and possible early-distribution issue.",
)
text = text.replace(
    "Fill the bracket without spilling into the next one.",
    "Size the move from the all-in marginal cost, including gains, ACA/IRMAA, NIIT, state tax, deductions, and credits.",
)
write(path, text)

# Custody walkthrough language must match the researched recovery sequence.
path = "scripts/07-5_WALKTHROUGH_custody-map.md"
text = read(path)
text = text.replace(
    "**⚠ The honesty beats, verbatim from the app:** *\"Full recovery process tested end-to-end\"* and *\"Backup seed verified readable.\"* Check these ONLY if the wipe-and-restore actually happened. Checked-but-fabricated means the plan believes something untrue.",
    "**⚠ The honesty beats, verbatim from the app:** *\"Full recovery process tested end-to-end\"* and *\"Backup seed verified readable.\"* Treat the app's word seed as the actual wallet backup standard. Check these only after a vendor backup check or spare-device recovery verified the intended wallet; a destructive wipe is not required and is not the first test.",
)
text = text.replace(
    "- [ ] Hardware items honest — leave unchecked anything you haven't actually done",
    "- [ ] Hardware items honest — recovery proof matched the exact setup and did not rely on the only working copy",
)
write(path, text)

path = "lesson-text/07-5_walkthrough-custody-map.md"
text = read(path)
text = text.replace(
    "Check recovery-tested only after a real wipe-and-restore.",
    "Check recovery-tested only after the intended wallet was verified through the exact backup check or spare-device recovery process. A destructive reset is optional, not the default first test.",
)
write(path, text)

# Replace the trust gate chapter in the estate walkthrough. It is now a scoped
# professional-conversation gate, not a mechanical trust diagnosis.
path = "scripts/08-5_WALKTHROUGH_estate.md"
text = read(path)
pattern = r"(?ms)^## □ G1 · Run the gate, then stop or continue\n.*?(?=^---\n\n## □ G2)"
replacement = r'''## □ G1 · Run the conversation gate, then record the answer

**⚠** Net worth is one input, not a diagnosis. Minor or vulnerable beneficiaries, blended family, business ownership, multi-state property, incapacity, probate/privacy concerns, advanced custody, possible estate tax, and a fiduciary expected to retain concentrated Bitcoin can each create a real attorney question.

**DO** Read the trigger list and name the actual problem it raises.

**⚠** Do not count triggers and mechanically assign a trust type. One trigger can justify a consultation; five triggers can still end with a will and beneficiary cleanup rather than a trust.

**DO** Record one of these outcomes with a date:

1. **Core cleanup is the next step** — provider beneficiary records, executor acceptance, attorney-supervised will/POA/directive, heir letter, and access map.
2. **Revocable-trust conversation** — incapacity or probate administration may improve if assets are properly titled to it.
3. **Advanced trust/tax/custody conversation** — ownership, estate tax, basis, business or beneficiary complexity, or concentrated-asset fiduciary duties require coordinated counsel.
4. **No trust currently indicated** — a finished answer with a future review trigger.

**⚠** A signed trust is not funded automatically. A revocable trust generally remains in the estate. An irrevocable trust does not automatically remove assets, preserve basis, or create creditor protection. A8.1 explains those limits.

**⚠** If concentrated Bitcoin is involved, the question is not one universal prudent-investor waiver. Ask which tools this state's law allows—express retention authority, diversification modification, directed trust, special trustee/protector, trustee selection, or another structure—and how that legal authority matches the multisig policy.

**DO** Point to **Advanced Estate Planning → A8.1** only when the problem is real.

'''
text = sub_once(text, pattern, replacement, "estate walkthrough trust gate", flags=re.M | re.S)
text = text.replace(
    "- [ ] Estate-complexity triggers counted, level named (1-4), and the answer written down with a date — including \"trust not currently indicated,\" which counts as done",
    "- [ ] Estate-complexity problem named and dated outcome recorded — including \"trust not currently indicated,\" which counts as done",
)
write(path, text)

path = "lesson-text/08-5_walkthrough-estate.md"
text = read(path)
text = re.sub(
    r"(?ms)^## Trust gate.*?(?=^## |\Z)",
    "## Trust conversation gate\n\nName the problem raised by minor/vulnerable beneficiaries, blended family, business, multi-state property, incapacity, probate/privacy concerns, advanced custody, possible estate tax, or concentrated-asset fiduciary duties. Do not assign a trust type by counting triggers. Record core cleanup, a revocable-trust conversation, coordinated advanced planning, or no trust currently indicated.\n\n",
    text,
    count=1,
)
write(path, text)

# Sync the researched spoken bodies back into both masters. --force is deliberate:
# the student-text layer now owns current reference detail, while the master and
# protected script must not disagree on the rule being taught.
core_nums = ["5.1", "5.2", "7.1", "7.2", "7.3", "8.1", "8.2", "8.3", "8.4"]
adv_nums = ["A5.1", "A5.2", "A5.3", "A6.1", "A6.2", "A7.1", "A7.3", "A7.4", "A8.1"]
subprocess.run(
    ["python3", "tools/sync-master-from-script.py", "--force", *core_nums],
    cwd=ROOT,
    check=True,
)
subprocess.run(
    ["python3", "tools/sync-master-from-script.py", "--advanced", "--force", *adv_nums],
    cwd=ROOT,
    check=True,
)

# Header/outcome corrections that the body sync deliberately preserves.
master = read("MASTER-COURSE.md")
master = master.replace(
    "- Never leave basis blank",
    "- Label every material lot verified, estimated for planning, or unproven",
)
master = master.replace(
    "- Prove the recovery by wiping and restoring the device",
    "- Prove the intended wallet through the exact backup-check or spare-device recovery path",
)
write("MASTER-COURSE.md", master)

master_adv = read("MASTER-ADVANCED.md")
master_adv = master_adv.replace(
    "> ⚖ **PUBLICATION BLOCKER — pending estate-attorney review.** Do not publish\n> this lesson until `LEGAL-REVIEW-PACKET.md` is signed off.",
    "> ⚖ **PUBLICATION BLOCKER — targeted state-attorney signoff.** General research is complete. Do not publish this lesson until the A8.1 section of `TARGETED-PROFESSIONAL-SIGNOFF.md` is approved for the governing state.",
)
write("MASTER-ADVANCED.md", master_adv)

# Claim-registry guardrails for the exact high-risk errors this audit removed.
registry = read("CLAIM-REGISTRY.md")
anchor = "| module-ten | | `Module 10\\b` | | | Modules run 0–9. A tenth module has not existed since the renumber |"
rows = """| basis-safe-harbor | | `(?i)IRS standard is reasonable and documented` | | | There is no general substantiation safe harbor with this wording |\n| seed-universal-portability | | `(?i)(seed|backup).{0,50}works? in any hardware wallet` | | | Recovery depends on backup standard, passphrase, script/derivation data, and wallet policy |\n| wipe-first-proof | | `(?i)check these only if the wipe-and-restore` | | | Destructive wiping is not the default first recovery test |\n| loan-tax-free-flat | | `(?i)borrowing.{0,40}no taxable event` | | `(?i)not a universal|does not make|too broad` | Loan proceeds are generally not income; liquidation, sale, or cancellation can create tax consequences |\n| irrevocable-auto | | `(?i)irrevocable.{0,50}(automatically|means).{0,50}(outside|leave).{0,30}estate` | | `(?i)does not|not automatically` | Trust results depend on retained powers, completed transfers, terms, and state law |"""
if "basis-safe-harbor" not in registry:
    registry = registry.replace(anchor, anchor + "\n" + rows)
write("CLAIM-REGISTRY.md", registry)

# Research and signoff documents quote retired language intentionally. Keep them
# out of regression scans just like the authority history.
checker = read("tools/check-layer-parity.py")
checker = checker.replace(
    "'FAQ-AND-AI-BACKLOG.md', 'VOICE-GUIDE.md'}",
    "'FAQ-AND-AI-BACKLOG.md', 'VOICE-GUIDE.md',\n              'PROFESSIONAL-RESEARCH-AUDIT.md',\n              'TARGETED-PROFESSIONAL-SIGNOFF.md',\n              'PRIMARY-SOURCE-REGISTER.md'}",
)
write("tools/check-layer-parity.py", checker)

# Module checkpoints: proof and tax-basis status must match the corrected lessons.
checkpoints = read("MODULE-CHECKPOINTS.md")
checkpoints = checkpoints.replace(
    "- [ ] Your cost basis is reconstructed and **the records exist to prove it** — no records means a basis of zero, which means tax on the entire sale price",
    "- [ ] Every material lot is labeled **verified, estimated for planning, or unproven**; the source records are retained, and an unproven lot is not silently assigned return basis",
)
checkpoints = re.sub(
    r"- \[ \] \*\*Recovery is proven by the path your setup actually has\.\*\*.*?institutional path completes this line\*\*",
    "- [ ] **Recovery is proven by the path your setup actually has.** *Self-custody:* a vendor-supported backup check or spare-device recovery verified the intended wallet, including passphrase or multisig policy when used; a destructive reset is optional and never the first test on the only live device. *Institutional custody:* login recovery and the provider's death-claim process were verified. **The setup-specific proof completes this line.**",
    checkpoints,
    count=1,
    flags=re.S,
)
checkpoints = checkpoints.replace(
    "- [ ] The trust gate has been run once and given an actual answer. **Most households stop at \"no\", and that is complete**",
    "- [ ] The trust conversation gate has produced a dated answer: core cleanup, revocable-trust discussion, coordinated advanced planning, or **no trust currently indicated**",
)
write("MODULE-CHECKPOINTS.md", checkpoints)

# F6 was an editor-authored universal Level 2 recommendation. Research cannot
# choose the holder for every family, so the unsafe prescription is removed and
# the lesson now teaches the factual tests without inventing a replacement.
authority = read("AUTHORITY-FLAGS.md")
authority = sub_once(
    authority,
    r"(?ms)^### F6 · The Level 2 access design\n.*?(?=^### F7 )",
    """### F6 ✅ RESOLVED BY REMOVING THE UNAUTHORIZED DEFAULT · Level 2 access design\n\nThe earlier course prescribed one universal Level 2 arrangement even though Austin had not dictated it. The professional research audit confirmed that a single-signature wallet cannot honestly be presented as dual control merely by naming an executor and heir.\n\nThe prescription has been removed. Lesson 8.2 now teaches the two factual tests—one-person spend and one-loss recovery—and requires the household and state attorney to align legal authority, backup holders, and accepted trade-offs. It does not invent a new universal holder arrangement. If Austin later wants a preferred Level 2 default, that becomes new dictation rather than an editor's recommendation.\n\n""",
    "resolve F6",
    flags=re.M | re.S,
)
write("AUTHORITY-FLAGS.md", authority)

# Advanced production order: research is complete; only exact operational proof
# or targeted publication signoff remains.
order = read("ADVANCED-DICTATION-ORDER.md")
order = order.replace("CPA review before recording", "Research-complete; targeted CPA/EA signoff before publication")
order = order.replace("Custody-professional review before recording", "Research-complete; exact setup proof before device/provider-specific footage")
order = order.replace("Ready to dictate; estate-attorney review before publication", "Research-complete; state-attorney signoff before publication")
write("ADVANCED-DICTATION-ORDER.md", order)

# Production generator: replace blanket professional filming gates with the
# narrow release/operational gates the audit supports.
producer = read("tools/build-production-checklist.py")
producer = sub_once(
    producer,
    r"(?ms)^REVIEW_GATES = \[.*?^\]\n",
    r'''REVIEW_GATES = [
    ('Current-year seeded examples in Module 5 and A5.1, A5.2, A5.3, A6.1, A6.2',
     'Bitcoin-aware CPA or enrolled agent', 'publication',
     'research is complete; signoff is limited to the seeded household, current-year interactions, incomplete-basis treatment, and state assumptions'),
    ('7.4 hardware-wallet demo and provider-specific recovery claims',
     'custody technical peer plus exact device/provider operational test', 'filming',
     'concept scripts are research-complete; the footage must prove the exact firmware, backup standard, threshold, descriptor, and provider-independent recovery path it claims'),
    ('8.4 Coverage Audit and policy-category examples',
     'licensed insurance producer or fee-only insurance reviewer', 'publication',
     'research is complete; signoff is limited to policy mechanics, contract interpretation, and whether the first-pass worksheet could be mistaken for a recommendation'),
    ('A8.1 and state-specific executor/digital-asset materials',
     'estate attorney licensed in the governing state', 'publication',
     'general research is complete; state law controls drafting, RUFADAA consent, fiduciary-duty modification, probate, and trust funding'),
    ('Course terms, disclaimer, live-call and community boundaries',
     'qualified counsel', 'publication',
     'the delivery model must remain education rather than personalized legal, tax, insurance, or investment advice'),
]
''',
    "replace review gates",
    flags=re.M | re.S,
)
producer = producer.replace(
    "> ⚠ **The CPA review is the one to start now.** Module 5 is Wave 2, so it\n> looks distant — but it is the review most likely to produce an\n> arithmetic correction, and arithmetic corrections are what force\n> re-records. It also touches 2.4 and 4.3, which are Wave 1.",
    "> **Research-complete scripts may be dictated.** The rows above are narrow operational or publication gates. Give each reviewer `TARGETED-PROFESSIONAL-SIGNOFF.md`; do not ask them to redesign the course or replace Austin's planning position.",
)
write("tools/build-production-checklist.py", producer)

# Archive the old broad review packet, then replace the current packet with the
# researched release policy.
archive = ROOT / "archive/LEGAL-REVIEW-PACKET-pre-research-2026-08-25.md"
if not archive.exists():
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(read("LEGAL-REVIEW-PACKET.md"), encoding="utf-8")

write("LEGAL-REVIEW-PACKET.md", r'''
# Legal and professional review packet — current release gate

**Research audit completed:** 2026-08-25

The broad “review every sensitive lesson before recording” policy is retired. The primary-source audit and script corrections are complete.

Use these files:

1. `PROFESSIONAL-RESEARCH-AUDIT.md` — claim-by-claim findings and corrections.
2. `research/PRIMARY-SOURCE-REGISTER.md` — official sources.
3. `TARGETED-PROFESSIONAL-SIGNOFF.md` — only the state-, policy-, provider-, taxpayer-, and delivery-model questions that still require a credential or exact operational test.
4. `COURSE-LEGAL-COPY.md` — terms, disclaimer, and course-delivery language.

## Current gates

- **Dictation:** research-complete scripts may be dictated, except F20 and F22 still require Austin's words.
- **Custody demo:** 7.4 and provider/device-specific footage require the exact operational proof in the targeted packet before recording.
- **Tax publication:** current-year seeded household examples, incomplete-basis treatment, integrated ACA/IRMAA/NIIT/state effects, and state-relocation assumptions require targeted CPA/EA signoff.
- **Insurance publication:** 8.4 and the Coverage Audit require targeted licensed review of policy mechanics and the first-pass math.
- **Estate publication:** A8.1 and state-specific executor/digital-asset materials require counsel licensed in the governing state.
- **Commercial release:** course terms and the boundary for live calls/community replies require qualified counsel.

The pre-research packet is retained at `archive/LEGAL-REVIEW-PACKET-pre-research-2026-08-25.md` for provenance.

A reviewer may correct law, tax mechanics, policy mechanics, or technical behavior. A reviewer may not silently replace Austin's planning recommendation. Any judgment change returns through `AUSTIN-AUTHORITY.md`.
''')

write("FINALIZATION-STATUS.md", r'''
# Course finalization status

## Editorial and research status

- The ten-module core structure is locked.
- Austin's original source for 0.2, 1.1, and 1.2 remains preserved and mapped; this audit does not alter it.
- All 14 Advanced Library lessons retain protected spoken-ready scripts.
- Primary-source research is complete for tax, healthcare, custody, insurance, estate, trusts, and digital-asset access.
- Scripts, student text, walkthroughs, master files, and production policy are being regenerated from the researched corrections.
- Module 2 order remains final: 2.4 optional college, 2.5 walkthrough.

## Ready to dictate

Every research-complete teach script may be dictated unless named below as an Austin content blocker.

The old blanket CPA/custody/insurance/attorney **before recording** rule is retired. Exact device/provider footage still requires operational proof before it is filmed. State-, policy-, taxpayer-, and delivery-specific issues use targeted signoff before publication.

## Austin dictation still required

- **F20:** the 7-to-10-year future-cost lane.
- **F22:** the next-dollar default order, overrides, and deliberate-split rule.

The prompts remain in `DICTATION-PICKUPS.md`.

## Targeted gates after dictation

- CPA/EA: seeded current-year tax examples, incomplete-basis return position, integrated thresholds, and state assumptions.
- Custody: exact device/firmware/provider recovery proof for 7.4 and provider-specific footage.
- Insurance: policy mechanics and Coverage Audit before publication.
- Estate attorney: A8.1, state-specific documents, RUFADAA consent, fiduciary-duty drafting, and trust funding before publication.
- Counsel: terms/disclaimer and live education-versus-personalized-advice boundaries before commercial release.

See `TARGETED-PROFESSIONAL-SIGNOFF.md`.

## Important corrected claims

- A planning basis estimate is not automatically a substantiated return basis.
- Specific identification is made no later than the transaction and is wallet/account specific.
- Roth tax treatment depends on qualified-distribution rules; RMD age is cohort specific.
- Loan proceeds are generally not income, but collateral disposition or cancellation can create tax consequences.
- A wallet backup is not universally portable to every device; multisig recovery also needs the policy/descriptor.
- A descriptor cannot sign and one key plus a descriptor remains one key.
- Destructive wiping is not the default first recovery test.
- Insurance gap math is a first-pass range, not a recommendation.
- Revocable and irrevocable trust results depend on funding, retained powers, terms, and state law.
- A trust trigger creates an attorney question; it does not mechanically choose a trust type.

## Verification

Final generator and repository gate output is recorded in `PROFESSIONAL-RESEARCH-VERIFICATION.md`.
''')

# Handoff: make the current source of truth obvious.
handoff = read("HANDOFF.md")
insert = r'''## Professional research audit — 2026-08-25

- The tax, custody, insurance, and estate first-pass research is complete against primary sources.
- Use `PROFESSIONAL-RESEARCH-AUDIT.md` for findings and `TARGETED-PROFESSIONAL-SIGNOFF.md` for the narrow remaining reviews.
- The old blanket “professional before recording” rule is retired. Research-complete scripts may be dictated; exact custody footage needs setup proof; state/policy/taxpayer-specific signoffs happen before publication.
- The only Austin dictation blockers remain F20 and F22.
- Do not reintroduce the retired claims guarded in `CLAIM-REGISTRY.md`.

'''
if "## Professional research audit — 2026-08-25" not in handoff:
    handoff = handoff.replace("---\n\n## Final dictation package", "---\n\n" + insert + "## Final dictation package", 1)
write("HANDOFF.md", handoff)
