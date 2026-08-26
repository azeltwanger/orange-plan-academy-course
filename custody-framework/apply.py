#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = Path(__file__).resolve().parent


def read(path: str | Path) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def payload(name: str) -> str:
    return (PAYLOAD / name).read_text(encoding="utf-8").strip()


def replace_numbered_section(text: str, number: str, new_section: str) -> str:
    start = re.search(rf"(?m)^## {re.escape(number)} .+$", text)
    if not start:
        raise RuntimeError(f"Could not find lesson {number}")
    tail = text[start.end():]
    nxt = re.search(
        r"(?m)^(?:## A?\d+\.\d+ |## Module checkpoint$|## Related advanced lessons$|# Unit |# Advanced Module )",
        tail,
    )
    end = start.end() + (nxt.start() if nxt else len(tail))
    section = new_section.strip()
    if not section.endswith("---"):
        section += "\n\n---"
    return text[: start.start()] + section + "\n\n" + text[end:].lstrip("\n")


def masterize(section: str) -> str:
    return re.sub(
        r"(?m)^🎬 VISUAL — (.+)$",
        lambda m: f"> **Visual:** {m.group(1)}",
        section,
    )


def parse_section(section: str) -> tuple[str, str, str | None]:
    lines = section.strip().splitlines()
    m = re.match(r"^## (A?\d+\.\d+) (.+)$", lines[0])
    if not m:
        raise RuntimeError(f"Bad section heading: {lines[0]}")
    number, title = m.group(1), m.group(2)
    gate = None
    i = 1
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("*`TEACH`") or line.startswith("*`WALKTHROUGH"):
            i += 1
            continue
        if line.startswith("> **Gate.**"):
            gate = line.replace("> **Gate.**", "").strip()
            i += 1
            continue
        break
    body_lines = lines[i:]
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    if body_lines and body_lines[-1].strip() == "---":
        body_lines.pop()
    body = "\n".join(body_lines).strip()
    return title, body, gate


def strip_visuals(body: str) -> str:
    out = []
    for line in body.splitlines():
        if line.startswith("🎬 VISUAL —") or line.startswith("> **Visual:**"):
            continue
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def write_core_script(number: str, section: str, path: str, source: str) -> None:
    title, body, _ = parse_section(section)
    words = len(body.split())
    content = (
        f"TELEPROMPTER SCRIPT — segment {number}\n"
        f"{number} {title}\n"
        f"{words} words · ~{words / 155:.1f} min at 155 wpm · PRE-DICTATION FILMING DRAFT — rebuilt from Austin's custody direction, research, and the current app\n"
        f"SOURCE: {source}\n"
        + "=" * 60
        + "\n\n"
        + body
        + "\n"
    )
    write(path, content)


def write_advanced_script(number: str, section: str, path: str) -> None:
    title, body, gate = parse_section(section)
    words = len(body.split())
    content = (
        f"ADVANCED TELEPROMPTER SCRIPT — segment {number}\n"
        f"{number} {title}\n"
        f"{words} words · ~{words / 155:.1f} min at 155 wpm · PRE-DICTATION FILMING DRAFT\n"
        f"PUBLICATION GATE: {gate or 'Verify exact implementation before setup-specific footage.'}\n"
        + "=" * 60
        + "\n\n"
        + body
        + "\n"
    )
    write(path, content)


CHECKPOINT = """## Module checkpoint

- [ ] Custody direction is one method or an intentional split, chosen on purpose.
- [ ] Direct-control preference and the risk being reduced are stated.
- [ ] Every meaningful Bitcoin pool has a no-secrets job, scale, method, remaining failure, and family path.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The One-Failure Test identified the largest current weakness.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, PIN, password, descriptor contents, or exact recovery location is stored in the app, map, or course notes.
- [ ] An encrypted backup of the plan data exists."""


# ---------------------------------------------------------------------------
# 1. Replace the core and advanced masters.
# ---------------------------------------------------------------------------
core_71 = payload("core-7.1.md")
core_73 = payload("core-7.3.md")
core_75 = payload("core-7.5.md")
adv_71 = payload("advanced-A7.1.md")
adv_72 = payload("advanced-A7.2.md")
adv_73 = payload("advanced-A7.3.md")

core = read("MASTER-COURSE.md")
old_intro = """# Unit 8 · Module 7 — Custody

*Choose a custody level, prove recovery, harden the accounts, and remove the largest single point of failure without storing secrets in the plan.*

**You will build:** A tested custody process, one major failure point fixed, and a no-secrets checklist with an encrypted plan backup."""
new_intro = """# Unit 8 · Module 7 — Custody

*Choose which custody risks to keep or transfer, prove every recovery path, and make sure one device, method, provider, or person cannot materially damage the family's plan.*

**You will build:** A custody direction, a no-secrets map of the meaningful Bitcoin pools, a proven recovery path, and one major failure point fixed."""
if old_intro not in core:
    raise RuntimeError("Module 7 intro changed; refusing a blind replacement")
core = core.replace(old_intro, new_intro, 1)
core = replace_numbered_section(core, "7.1", masterize(core_71))
core = replace_numbered_section(core, "7.3", masterize(core_73))
core = replace_numbered_section(core, "7.5", masterize(core_75))
old_checkpoint = """## Module checkpoint

- [ ] Custody level is chosen for the amount and household.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The top single point of failure has an owner and deadline.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, or PIN is stored in the app or course notes.
- [ ] An encrypted backup of the plan data exists."""
if old_checkpoint not in core:
    raise RuntimeError("Old Module 7 checkpoint not found")
core = core.replace(old_checkpoint, CHECKPOINT, 1)
write("MASTER-COURSE.md", core)

advanced = read("MASTER-ADVANCED.md")
advanced = replace_numbered_section(advanced, "A7.1", adv_71)
advanced = replace_numbered_section(advanced, "A7.2", adv_72)
advanced = replace_numbered_section(advanced, "A7.3", adv_73)
write("MASTER-ADVANCED.md", advanced)


# ---------------------------------------------------------------------------
# 2. Replace / rename the filming scripts and student text.
# ---------------------------------------------------------------------------
old_paths = [
    "scripts/07-1_choose-a-custody-setup-your-household-can-recover.md",
    "lesson-text/07-1_choose-a-custody-setup-your-household-can-recover.md",
    "scripts/07-5_WALKTHROUGH_document-custody-status.md",
    "lesson-text/07-5_walkthrough-document-custody-status.md",
    "scripts/advanced/A7-1_advanced-custody.md",
    "lesson-text/advanced/A7-1_advanced-custody.md",
    "scripts/advanced/A7-3_avoid-custody-concentration.md",
    "lesson-text/advanced/A7-3_avoid-custody-concentration.md",
]
for rel in old_paths:
    (ROOT / rel).unlink(missing_ok=True)

core71_script = "scripts/07-1_self-custody-professional-custody-and-when-a-split-makes-sense.md"
core73_script = "scripts/07-3_fix-single-points-of-failure-and-harden-accounts.md"
core75_script = "scripts/07-5_WALKTHROUGH_document-the-custody-decision-and-status.md"
write_core_script(
    "7.1",
    core_71,
    core71_script,
    "Austin custody decision-framework notes, current Protect flow, and the technical custody audit",
)
write_core_script(
    "7.3",
    core_73,
    core73_script,
    "Austin custody decision-framework notes, account-security guidance, and the current Protect flow",
)

# Capture sheet: preserve the DO / SEE / warning format, not a teleprompter header.
_, core75_body, _ = parse_section(core_75)
write(core75_script, f"# 7.5 · WALKTHROUGH — Document the custody decision and current status without storing secrets\n\n{core75_body}")

module_checkpoint_md = CHECKPOINT.replace("## Module checkpoint", "## Module checkpoint")
for number, section, path in (
    ("7.1", core_71, "lesson-text/07-1_self-custody-professional-custody-and-when-a-split-makes-sense.md"),
    ("7.3", core_73, "lesson-text/07-3_fix-single-points-of-failure-and-harden-accounts.md"),
):
    title, body, _ = parse_section(section)
    student = (
        f"# {number} · {title}\n\n"
        + strip_visuals(body)
        + "\n\n## Apply it\n\nUse `CUSTODY-DECISION-MAP.md` to record the decision without secrets, then complete walkthrough 7.5 to reflect the implementation status in Protect.\n\n"
        + module_checkpoint_md
    )
    write(path, student)

write(
    "lesson-text/07-5_walkthrough-document-the-custody-decision-and-status.md",
    """# 7.5 · Walkthrough — Document the custody decision and current status without storing secrets

Use this walkthrough after making the custody decision in Lesson 7.1 and completing the operational work from Lessons 7.2–7.3.

You will use the no-secrets Custody Decision Map to record the job, rough scale, method, remaining failure, and family path for each meaningful Bitcoin pool. Then Protect records which implementation items are actually complete.

The walkthrough ends with one failure assigned to an owner and deadline, the annual custody review scheduled, and an encrypted backup of the Orange Plan data.

""" + CHECKPOINT,
)

adv_files = (
    (
        "A7.1",
        adv_71,
        "scripts/advanced/A7-1_compare-passphrase-multisig-institutional-custody-and-an-intentional-split.md",
        "lesson-text/advanced/A7-1_compare-passphrase-multisig-institutional-custody-and-an-intentional-split.md",
    ),
    (
        "A7.2",
        adv_72,
        "scripts/advanced/A7-2_what-self-custody-asks-of-you.md",
        "lesson-text/advanced/A7-2_what-self-custody-asks-of-you.md",
    ),
    (
        "A7.3",
        adv_73,
        "scripts/advanced/A7-3_run-the-one-failure-test-across-methods-and-providers.md",
        "lesson-text/advanced/A7-3_run-the-one-failure-test-across-methods-and-providers.md",
    ),
)
for number, section, script_path, text_path in adv_files:
    write_advanced_script(number, section, script_path)
    title, body, _ = parse_section(section)
    write(text_path, f"# {number} · {title}\n\n{strip_visuals(body)}")


# ---------------------------------------------------------------------------
# 3. Add the no-secrets decision map and preserve Austin's source direction.
# ---------------------------------------------------------------------------
shutil.copyfile(PAYLOAD / "CUSTODY-DECISION-MAP.md", ROOT / "CUSTODY-DECISION-MAP.md")
shutil.copyfile(
    PAYLOAD / "source-notes.md",
    ROOT / "source-material/2026-08-26-custody-decision-framework.md",
)


# ---------------------------------------------------------------------------
# 4. Replace the relevant visuals.
# ---------------------------------------------------------------------------
write(
    "visuals/7-1a_five-questions.md",
    """# 7.1 · The five-step custody decision

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That the decision begins with the job and failure being solved, not with a product or wealth level.

## The visual
Five numbered cards in a vertical flow:

1. Name the Bitcoin's job
2. Name the failure being protected against
3. Decide how much direct control matters
4. Run the One-Failure Test
5. Choose the simplest architecture that passes

A thin footer reads: **Every additional setup must solve a named risk.**

## Labels and data
Use one example pool: long-term family wealth · life-changing · direct control important, not absolute · provider failure and family recovery are the top concerns.

Never show balances, secrets, provider names, or a product recommendation.

## Motion
The cards appear one at a time. The final card expands into two possible outcomes: one well-run method or an intentional split.
""",
)
write(
    "visuals/7-1b_levels-and-trust.md",
    """# 7.1 · Every custody method trades risk

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That custody methods are not a wealth ladder. Each method protects against one failure by accepting another.

## The visual
Four equal columns:

- Direct self-custody
- Collaborative multisig
- Institutional custody
- Intentional split

Each column has two rows: **Protects against** and **You accept**.

Under the columns, show the direct-control preference as three selectable positions:

- Non-negotiable
- Important, not absolute
- Support and simplicity matter more

At the bottom, replace the old levels with four readiness outcomes:

1. Accounts secured
2. Direct custody proven
3. Family continuity established
4. Catastrophic concentration removed

## Labels and data
Direct self-custody: provider failure / recovery and physical risk.
Collaborative multisig: one-key loss / setup, provider, and coordination risk.
Institutional custody: personal key loss and administration / counterparty and withdrawal risk.
Intentional split: one method destroying the whole plan / more systems to maintain.

## Motion
Columns reveal their protection first and accepted risk second. The readiness outcomes then build left to right with no arrow suggesting one custody product is the final destination.
""",
)
write(
    "visuals/7-3_only-one.md",
    """# 7.3 · The One-Failure Test

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That several devices or accounts can still share one catastrophic failure domain.

## The visual
Top: ten short “only one…” chips in a grid:

Device · recovery backup · location · person who knows · email/login · custody method · institutional provider · family process · wallet policy/descriptor · legal/technical alignment.

Middle: seven failure-event cards:

Lost recovery material · frozen account · provider failure · home disaster · coercion · incapacity · family cannot execute.

Bottom: one large question:

**If this entire pool became inaccessible, would the financial plan still survive?**

Use three rough scale labels beside the example pool: Replaceable · Meaningful · Life-changing.

## Motion
The illustrative household's shared dependencies light up. Several apparently separate boxes collapse into one red failure domain, then the final survival question appears.
""",
)
write(
    "visuals/A7-1_passphrase-multisig.md",
    """# A7.1 · Advanced custody methods and remaining failures

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That passphrase, multisig, collaborative custody, institutional custody, and an intentional split remove different failures. None removes every failure.

## The visual
Top row, three technical panels:

**Passphrase single-sig:** one compatible mnemonic feeds a standard wallet and, with the exact passphrase, a different derived wallet. A typo reaches another valid but unintended wallet.

**2-of-3 multisig:** three signing keys surround a separate policy/descriptor card. Any two keys sign; one cannot. The policy card has a clear **CANNOT SIGN** label.

**Institutional custody:** the institution controls keys and withdrawals; the household receives support and administration but accepts counterparty and access risk.

Bottom row, a comparison table with two rows:

- What one failure can no longer do
- What can still fail

A final strip shows an **intentional split** across distinct failure domains and the warning: **Every extra method must solve a named risk.**

## Labels and data
Do not imply “None” under single point of failure. Use exact language:

- Passphrase: seed alone cannot spend the intended wallet; seed/passphrase recovery and family process can still fail.
- Multisig: one lost key does not lose the wallet; policy data, key distribution, software, provider, and family process can still fail.
- Institutional: personal key loss is transferred; provider, withdrawal, jurisdiction, identity, and family administration can still fail.

Never render an actual mnemonic, passphrase, key, descriptor, fingerprint, address, provider name, or account number.

## Motion
Each panel first removes one failure, then reveals the remaining failures. The intentional-split strip only appears after the trade-offs are visible.
""",
)


# ---------------------------------------------------------------------------
# 5. Update authority, checkpoints, production maps, and release gates.
# ---------------------------------------------------------------------------
checkpoints = read("MODULE-CHECKPOINTS.md")
old_cp_block = """## Module 7 — Custody

**You will build:** A tested custody process, one major failure point fixed, and a no-secrets checklist with an encrypted plan backup.

- [ ] Custody level is chosen for the amount and household.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The top single point of failure has an owner and deadline.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, or PIN is stored in the app or course notes.
- [ ] An encrypted backup of the plan data exists."""
new_cp_block = """## Module 7 — Custody

**You will build:** A custody direction, a no-secrets map of the meaningful Bitcoin pools, a proven recovery path, and one major failure point fixed.

- [ ] Custody direction is one method or an intentional split, chosen on purpose.
- [ ] Direct-control preference and the risk being reduced are stated.
- [ ] Every meaningful Bitcoin pool has a no-secrets job, scale, method, remaining failure, and family path.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The One-Failure Test identified the largest current weakness.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, PIN, password, descriptor contents, or exact recovery location is stored in the app, map, or course notes.
- [ ] An encrypted backup of the plan data exists."""
if old_cp_block not in checkpoints:
    raise RuntimeError("Module checkpoint source changed")
write("MODULE-CHECKPOINTS.md", checkpoints.replace(old_cp_block, new_cp_block, 1))

screen_map = read("SCREEN-SHOOT-LIST.md")
screen_map = screen_map.replace(
    """## 7.1 · Choose a custody setup your household can recover

- Five custody questions
- Custody levels 1–4""",
    """## 7.1 · Self-custody, professional custody, and when a split makes sense

- Five-step custody decision
- Direct self-custody / collaborative multisig / institutional custody / intentional split
- Direct-control preference
- Four readiness outcomes, not a wealth ladder""",
)
screen_map = screen_map.replace(
    """## 7.3 · Fix the single points of failure and harden the accounts

- The only-one single-points-of-failure list""",
    """## 7.3 · Fix the single points of failure and harden the accounts

- Expanded only-one list, including one custody method and one institutional provider
- Replaceable / meaningful / life-changing scale
- One-Failure Test and plan-survival question""",
)
write("SCREEN-SHOOT-LIST.md", screen_map)

authority = read("AUSTIN-AUTHORITY.md")
anchor = "No universal college split, contribution priority exception, loan amount, Bitcoin allocation, insurance amount, trust clause, or custody-key split may be invented and attributed to Austin."
replacement = anchor + "\n\nCustody is not a wealth ladder. Institutional custody and an intentional split can be legitimate planning choices; no custody method is prescribed solely by balance, sophistication, or status."
if anchor not in authority:
    raise RuntimeError("Austin authority anchor changed")
write("AUSTIN-AUTHORITY.md", authority.replace(anchor, replacement, 1))

policy = read("SOURCE-MATERIAL-POLICY.md")
policy = policy.replace(
    "custody is not a purity test · document the process, never the secrets",
    "custody is not a purity test · custody methods are not a wealth ladder · institutional custody and intentional splits can be legitimate · document the process, never the secrets",
    1,
)
insert_anchor = "- **Collaborative custody as the default advanced setup.**\n"
insert_text = (
    insert_anchor
    + "- **A custody wealth ladder.** A larger balance does not automatically prescribe passphrase, multisig, or one increasingly advanced self-custody setup. Compare direct control, recovery, support, recourse, provider risk, and concentration.\n"
)
if insert_anchor not in policy:
    raise RuntimeError("Source-material policy anchor changed")
write("SOURCE-MATERIAL-POLICY.md", policy.replace(insert_anchor, insert_text, 1))

registry = read("CLAIM-REGISTRY.md")
registry = registry.replace(
    "| Custody | Document the process, never the secrets. No universal seed/passphrase/key split is taught. |",
    "| Custody | Document the process, never the secrets. No universal seed/passphrase/key split is taught. Custody methods are not a wealth ladder; institutional custody belongs in the trade-off comparison, and one method or provider belongs in the One-Failure Test. |",
    1,
)
registry_anchor = "- One universal Bitcoin allocation, loan amount, LTV, UTXO threshold, insurance amount, trust clause, or inheritance key split.\n"
registry_insert = (
    registry_anchor
    + "- A custody wealth ladder that treats institutional custody as a beginner option or multisig as the automatic destination for a larger balance.\n"
    + "- A claim that multisig has no remaining single point of failure; state the exact failure removed and what can still fail.\n"
)
if registry_anchor not in registry:
    raise RuntimeError("Claim registry anchor changed")
write("CLAIM-REGISTRY.md", registry.replace(registry_anchor, registry_insert, 1))

source_map = read("DICTATION-SOURCE-MAP.md")
source_anchor = "### Contribution waterfall\n\nThe old slide deck supplies the base order and reasoning. The current 3.3 draft treats Extra Debt as provisional until Module 4. Austin can refine the exact exceptions while dictating; there is no structural blocker and no generated exception is represented as his prior wording.\n"
source_insert = source_anchor + """
### Custody decision framework

Austin established that custody is not a progression from institution to increasingly advanced self-custody. The current Module 7 and Advanced A7 drafts compare direct self-custody, collaborative multisig, institutional custody, and an intentional split by the risks each method removes and creates. The One-Failure Test now includes concentration in one custody method and one provider. These are Austin's planning directions, not line-by-line dictation, so the scripts remain labeled PRE-DICTATION FILMING DRAFT until he dictates or approves them.
"""
if source_anchor not in source_map:
    raise RuntimeError("Dictation source-map anchor changed")
write("DICTATION-SOURCE-MAP.md", source_map.replace(source_anchor, source_insert, 1))

final_status = read("FINALIZATION-STATUS.md")
final_status = final_status.replace(
    "- All 14 Advanced lessons have been renumbered, rewritten as pre-dictation drafts, and attached to the correct core module.\n",
    "- All 14 Advanced lessons have been renumbered, rewritten as pre-dictation drafts, and attached to the correct core module.\n- Module 7 now uses a custody trade-off and One-Failure framework instead of a wealth ladder; institutional custody and intentional splits are treated as legitimate planning choices.\n",
    1,
)
final_status = final_status.replace(
    "- Replaced stale Advanced numbering, gate, source-map, claim-registry, college-authority, and research-verification documents.\n",
    "- Replaced stale Advanced numbering, gate, source-map, claim-registry, college-authority, and research-verification documents.\n- Added the no-secrets Custody Decision Map and synchronized the revised core, Advanced, visual, checkpoint, and production layers.\n",
    1,
)
write("FINALIZATION-STATUS.md", final_status)

rebuild = read("COURSE-REBUILD-REPORT.md")
rebuild = rebuild.replace(
    "- Rebuilt and renumbered all Advanced lessons.\n",
    "- Rebuilt and renumbered all Advanced lessons.\n- Reframed custody around risk trade-offs, direct-control preference, rough scale, and the One-Failure Test; removed the implicit exchange-to-multisig wealth ladder.\n- Added institutional custody to the main comparison and an optional intentional split across distinct failure domains.\n",
    1,
)
write("COURSE-REBUILD-REPORT.md", rebuild)

signoff = read("TARGETED-PROFESSIONAL-SIGNOFF.md")
old_questions = """5. Are the provider claims conditional on the actual key distribution, exported recovery data, compatible recovery software, and provider terms?
6. Does the authentication order accurately distinguish phishing-resistant security keys/passkeys, TOTP, SMS, and recovery procedures?
7. Does the UTXO lesson distinguish protocol dust from an economically uneconomic output and disclose consolidation’s privacy cost?"""
new_questions = """5. Are the provider claims conditional on the actual key distribution, exported recovery data, compatible recovery software, and provider terms?
6. Does the course correctly present institutional custody as a distinct trade-off rather than a beginner rung, including support, recourse, counterparty, withdrawal, jurisdiction, identity, and family-administration risks?
7. Does the One-Failure Test correctly include concentration in one custody method, one institution, one provider, and correlated device/software dependencies without implying that every household needs a split?
8. Does the authentication order accurately distinguish phishing-resistant security keys/passkeys, TOTP, SMS, and recovery procedures?
9. Does the UTXO lesson distinguish protocol dust from an economically uneconomic output and disclose consolidation’s privacy cost?"""
if old_questions not in signoff:
    raise RuntimeError("Custody signoff questions changed")
write("TARGETED-PROFESSIONAL-SIGNOFF.md", signoff.replace(old_questions, new_questions, 1))


# ---------------------------------------------------------------------------
# 6. Regenerate dependent layers without running build-scripts.py, which would
#    erase the explicit pre-dictation provenance headers.
# ---------------------------------------------------------------------------
commands = [
    ["python3", "tools/build-module-gates.py"],
    ["python3", "tools/split-modules.py"],
    ["python3", "tools/split-modules.py", "--advanced"],
    ["python3", "tools/build-onefile.py"],
    ["python3", "tools/build-circle-structure.py"],
    ["python3", "tools/build-dictation-order.py"],
    ["python3", "tools/build-film-order.py"],
    ["python3", "tools/build-production-checklist.py"],
    ["python3", "tools/course-metrics.py"],
]
for command in commands:
    subprocess.run(command, cwd=ROOT, check=True)

print("Custody decision-framework pass applied.")
