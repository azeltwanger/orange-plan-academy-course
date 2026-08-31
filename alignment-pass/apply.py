#!/usr/bin/env python3
from __future__ import annotations

import re
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


def parse_section(section: str) -> tuple[str, str, str]:
    lines = section.strip().splitlines()
    match = re.match(r"^## ([A0-9.]+) (.+)$", lines[0])
    if not match:
        raise RuntimeError(f"Bad section heading: {lines[0]}")
    number, title = match.groups()
    i = 1
    while i < len(lines) and (not lines[i].strip() or lines[i].strip().startswith("*`")):
        i += 1
    return number, title, "\n".join(lines[i:]).strip()


def spoken_word_count(body: str) -> int:
    kept: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("🎬 VISUAL —"):
            continue
        if stripped.startswith("> **Production hold:**"):
            continue
        if stripped.startswith("> **Professional and product gate:**"):
            continue
        if stripped.startswith("> **V1 FILMING HOLD:**"):
            continue
        kept.append(line)
    return len(re.findall(r"\b[\w’'-]+\b", "\n".join(kept)))


def masterize(body: str) -> str:
    return re.sub(
        r"(?m)^🎬 VISUAL — (.+)$",
        lambda m: f"> **Visual:** {m.group(1)}",
        body,
    )


def studentize(body: str) -> str:
    out: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("🎬 VISUAL —"):
            continue
        if stripped.startswith("> **Production hold:**"):
            continue
        if stripped.startswith("> **Professional and product gate:**"):
            continue
        if stripped.startswith("> **V1 FILMING HOLD:**"):
            continue
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def replace_numbered_section(text: str, number: str, section: str) -> str:
    start = re.search(rf"(?m)^## {re.escape(number)} .+$", text)
    if not start:
        raise RuntimeError(f"Could not find section {number}")
    tail = text[start.end():]
    nxt = re.search(
        r"(?m)^(?:## [A0-9]+\.[0-9]+ |## Module checkpoint$|## Related advanced lessons$|# Unit |# Advanced Module )",
        tail,
    )
    end = start.end() + (nxt.start() if nxt else len(tail))
    new = section.strip()
    if not new.endswith("---"):
        new += "\n\n---"
    remainder = text[end:].lstrip("\n")
    remainder = re.sub(r"^(?:---\s*)+", "", remainder)
    return text[: start.start()] + new + "\n\n" + remainder


def make_script(number: str, title: str, body: str, source: str) -> str:
    words = spoken_word_count(body)
    return (
        f"TELEPROMPTER SCRIPT — segment {number}\n"
        f"{number} {title}\n"
        f"{words:,} words · ~{words / 155:.1f} min at 155 wpm · PRE-DICTATION FILMING DRAFT — V1 aligned and rewritten for direct delivery\n"
        f"SOURCE: {source}\n"
        + "=" * 60
        + "\n\n"
        + body.strip()
        + "\n"
    )


def update_teach(payload_name: str, script_path: str, lesson_path: str, source: str) -> None:
    number, title, body = parse_section(payload(payload_name))
    write(script_path, make_script(number, title, body, source))
    write(lesson_path, f"# {number} · {title}\n\n{studentize(body)}")
    master = read("MASTER-COURSE.md")
    section = f"## {number} {title}\n\n{masterize(body)}"
    write("MASTER-COURSE.md", replace_numbered_section(master, number, section))


def update_walkthrough(payload_name: str, script_path: str, lesson_path: str) -> None:
    number, title, body = parse_section(payload(payload_name))
    write(script_path, f"# {number} · {title}\n\n{body}")
    write(lesson_path, f"# {number} · {title}\n\n{studentize(body)}")
    master = read("MASTER-COURSE.md")
    section = f"## {number} {title}\n\n{masterize(body)}"
    write("MASTER-COURSE.md", replace_numbered_section(master, number, section))


# ---------------------------------------------------------------------------
# 1. Replace the five V1-sensitive teaching lessons and three key walkthroughs.
# ---------------------------------------------------------------------------
update_teach(
    "core-0.2.md",
    "scripts/00-2_how-to-use-orange-plan-ai.md",
    "lesson-text/00-2_how-to-use-orange-plan-ai.md",
    "PR #227 Ask, Current-versus-Preview, Build & improve, and AI safety contracts",
)
update_teach(
    "core-1.3.md",
    "scripts/01-3_what-the-onboarding-retirement-age-actually-means.md",
    "lesson-text/01-3_what-the-onboarding-retirement-age-actually-means.md",
    "Foundation flow plus PR #227 fixed-standard, result-state, and retirement-date contracts",
)
update_teach(
    "core-6.3.md",
    "scripts/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md",
    "lesson-text/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md",
    "PR #227 simulation-count and spending-guardrail decisions; current annual-policy semantics",
)
update_teach(
    "core-9.1.md",
    "scripts/09-1_keep-the-plan-current-without-rebuilding-it.md",
    "lesson-text/09-1_keep-the-plan-current-without-rebuilding-it.md",
    "Maintenance deck plus PR #227 Home, Cash Flow, Plan, Protect, activity, and Needs Attention contracts",
)
update_teach(
    "core-9.2.md",
    "scripts/09-2_test-decisions-and-read-the-finished-plan.md",
    "lesson-text/09-2_test-decisions-and-read-the-finished-plan.md",
    "Plan-review deck plus PR #227 Current-versus-Preview, Scenarios, fixed-standard, and Your Plan contracts",
)
update_walkthrough(
    "walkthrough-1.4.md",
    "scripts/01-4_WALKTHROUGH_foundation.md",
    "lesson-text/01-4_walkthrough-foundation.md",
)
update_walkthrough(
    "walkthrough-6.4.md",
    "scripts/06-4_WALKTHROUGH_retirement-paycheck.md",
    "lesson-text/06-4_walkthrough-retirement-paycheck.md",
)
update_walkthrough(
    "walkthrough-9.3.md",
    "scripts/09-3_WALKTHROUGH_finish-test-review-and-save.md",
    "lesson-text/09-3_walkthrough-finish-test-review-and-save.md",
)


# ---------------------------------------------------------------------------
# 2. Narrow pickups in Austin's 0.1 dictation for the approved V1 language.
# ---------------------------------------------------------------------------
PICKUPS = {
    "It gives you the ability to run simulations on how likely your plan is to succeed.":
        "It runs the plan through 1,000 simulations and shows how often the money lasts through the age you planned for.",
    "3. What level of confidence you can have in that plan.\n4. How many future scenarios your plan's going to hold up in.":
        "3. How many of the 1,000 simulations fund the plan through your planning age.\n4. What needs to improve when the plan falls short of the Orange Plan standard.",
    "Your date is also going to move with that confidence level.":
        "Your earliest modeled date moves as the facts, assumptions, and simulation result change.",
    "3. You'll learn how to read the retirement date and confidence number, but the first full confidence run happens after the plan is built in Module 9.":
        "3. You'll learn how to read the planned retirement date, the earliest modeled date, and the first preliminary simulation result. Each module makes that result more accurate, and Module 9 saves the completed-plan baseline.",
    "ways to optimize this to reduce your tax liability":
        "ways to improve the plan and reduce your tax liability",
    "Build Your Plan is the checklist underneath both of them.":
        "Build & improve is the implementation roadmap underneath both of them.",
}

SOURCE_LAYERS = [
    "MASTER-COURSE.md",
    "MASTER-ADVANCED.md",
]
SOURCE_LAYERS += [str(p.relative_to(ROOT)) for p in (ROOT / "scripts").rglob("*.md")]
SOURCE_LAYERS += [str(p.relative_to(ROOT)) for p in (ROOT / "lesson-text").rglob("*.md")]

for rel in SOURCE_LAYERS:
    text = read(rel)
    changed = text
    for old, new in PICKUPS.items():
        changed = changed.replace(old, new)
    if changed != text:
        write(rel, changed)


# ---------------------------------------------------------------------------
# 3. Align common V1 product language across active teaching layers.
# ---------------------------------------------------------------------------
TERM_REPLACEMENTS = {
    "Build Your Plan": "Build & improve",
    "Apply to plan": "Save to plan",
    "Apply To Plan": "Save to plan",
    "apply to the plan": "save to the plan",
    "apply it to the plan": "save it to the plan",
    "confidence ring": "simulation result",
    "Confidence ring": "Simulation result",
    "confidence result": "simulation result",
    "Confidence result": "Simulation result",
    "confidence number": "simulation result",
    "Confidence number": "Simulation result",
    "confidence percentage": "simulation count",
    "Confidence percentage": "Simulation count",
    "confidence check": "simulation run",
    "Confidence check": "Simulation run",
    "full confidence run": "completed-plan simulation run",
    "first full confidence check": "first completed-plan simulation run",
    "confidence target": "retirement test standard",
    "Confidence target": "Retirement test standard",
    "optimize your plan": "improve your plan",
    "Optimize your plan": "Improve your plan",
    "optimization action": "improvement action",
    "optimization copy": "improvement copy",
}

for rel in SOURCE_LAYERS:
    text = read(rel)
    changed = text
    for old, new in TERM_REPLACEMENTS.items():
        changed = changed.replace(old, new)
    if changed != text:
        write(rel, changed)


# ---------------------------------------------------------------------------
# 4. Direct-language pass: remove rhetorical denial and lead with the point.
# ---------------------------------------------------------------------------
DIRECT_REPLACEMENTS = {
    "I do not think the honest answer is a percentage I hand you.":
        "The right Bitcoin allocation depends on the person and the rest of the plan.",
    "The four paths on the screen are not recommendations. They are a way to describe where somebody actually is.":
        "Use the four paths to identify where you are today.",
    "The important question is which description is true today, not which one sounds most like the identity you want.":
        "Choose the description that matches your life today.",
    "Those are not forecasts. They are a way to make the emotional risk visible.":
        "Those numbers make the emotional risk visible.",
    "And I do not only mean whether you believe Bitcoin eventually recovers.":
        "The household still has to operate while Bitcoin is down.",
    "That does not mean every concentrated position is wrong. A large Bitcoin allocation can be completely intentional.":
        "A large Bitcoin allocation can be completely intentional.",
    "Not because price tells you what to do, but because it tells you which emotion is in the room.":
        "Price context tells you which emotion is in the room.",
    "In today's lesson, we're going to build a debt strategy instead of just making a list of what you owe.":
        "In today's lesson, we're going to give every debt a job.",
    "The interest rate matters, but it is not the only thing that matters. I would look at:":
        "Start with the interest rate, then look at:",
    "Those are not the same risk.":
        "Each decision carries a different risk.",
    "I do not mean one universal percentage that everybody copies. I mean the point where":
        "Your debt ceiling is the point where",
    "The goal is not to predict the future. The goal is to build a plan that can adapt.":
        "The goal is a plan that can adapt as the future unfolds.",
    "The goal is not perfection. The goal is an honest starting point.":
        "The goal is an honest starting point.",
    "The question is not whether the number is perfect. The question is whether it is honest enough to plan from.":
        "The question is whether the number is honest enough to plan from.",
    "This is not a budget. It is a forward-looking cash-flow plan.":
        "This is a forward-looking cash-flow plan.",
    "The account is not the investment. It is the wrapper around the investments.":
        "The account is the wrapper around the investments.",
    "The checklist is not the work. It records whether the work is complete.":
        "The checklist records whether the real work is complete.",
    "The app is not making the decision for you. It is showing you the trade-offs.":
        "The app shows you the trade-offs so you can make the decision.",
    "The plan is not changing its mind. It is using better information.":
        "The plan is using better information.",
    "The result is not a forecast. It is a stress test.":
        "Use the result as a stress test.",
    "The purpose is not to maximize the score. The purpose is to find a plan you actually want that works.":
        "The purpose is to find a plan you actually want that works.",
}

PROTECTED = re.compile(
    r"financial advice|guarantee|promise|seed phrase|private key|passphrase|password|PIN|secret|tax law|legal document|insurance contract|unsupported|not eligible|cannot|never|do not|must not",
    re.I,
)


def collapse_pair(match: re.Match[str]) -> str:
    whole = match.group(0)
    negative = match.group("negative")
    if PROTECTED.search(negative):
        return whole
    subject = match.group("subject")
    positive = match.group("positive")
    return f"{subject} is {positive}."


def direct_rewrite(text: str) -> str:
    changed = text
    for old, new in DIRECT_REPLACEMENTS.items():
        changed = changed.replace(old, new)

    # Repeated rhetorical pairs. Preserve explicit safety and legal boundaries.
    changed = re.sub(
        r"(?P<subject>The (?:goal|point|question|purpose|job|answer)) is not (?P<negative>[^.\n]+)\.\s+(?P=subject) is (?P<positive>[^.\n]+)\.",
        collapse_pair,
        changed,
    )
    changed = re.sub(
        r"(?P<subject>This|That) is not (?P<negative>[^.\n]+)\.\s+It is (?P<positive>[^.\n]+)\.",
        collapse_pair,
        changed,
    )
    changed = re.sub(
        r"(?P<subject>These|Those) are not (?P<negative>[^.\n]+)\.\s+They are (?P<positive>[^.\n]+)\.",
        lambda m: m.group(0) if PROTECTED.search(m.group("negative")) else f"{m.group('subject')} are {m.group('positive')}.",
        changed,
    )
    changed = re.sub(
        r"\bnot only ([^,.;\n]+), but also ([^.;\n]+)",
        r"\1 and \2",
        changed,
        flags=re.I,
    )
    changed = re.sub(
        r"\bnot because ([^,.;\n]+), but because ([^.;\n]+)",
        r"because \2",
        changed,
        flags=re.I,
    )
    return changed


for rel in SOURCE_LAYERS:
    text = read(rel)
    changed = direct_rewrite(text)
    if changed != text:
        write(rel, changed)


# ---------------------------------------------------------------------------
# 5. Advanced modeling pickup: fixed normal standard, custom Advanced override.
# ---------------------------------------------------------------------------
ADV_NOTE = """
The normal Orange Plan experience uses one standard: 800 successful simulations out of 1,000. Customer-facing results lead with the count and the age the money was tested through. A custom retirement test standard belongs in Advanced model settings and changes the earliest date that qualifies; it does not change the simulated market paths themselves. Current and Preview must use the same paths so the comparison remains fair.
""".strip()


def append_to_section(text: str, number: str, addition: str) -> str:
    start = re.search(rf"(?m)^## {re.escape(number)} .+$", text)
    if not start:
        raise RuntimeError(f"Missing {number}")
    tail = text[start.end():]
    nxt = re.search(r"(?m)^(?:## A\d+\.\d+ |# Advanced Module )", tail)
    end = start.end() + (nxt.start() if nxt else len(tail))
    section = text[start.start():end].rstrip()
    if addition in section:
        return text
    section = re.sub(r"\n---\s*$", "", section).rstrip() + "\n\n" + addition + "\n\n---\n"
    return text[: start.start()] + section + text[end:].lstrip("\n")

advanced = read("MASTER-ADVANCED.md")
write("MASTER-ADVANCED.md", append_to_section(advanced, "A1.1", ADV_NOTE))
for rel in (
    "scripts/advanced/A1-1_how-orange-plan-models-bitcoin.md",
    "lesson-text/advanced/A1-1_how-orange-plan-models-bitcoin.md",
):
    text = read(rel)
    if ADV_NOTE not in text:
        write(rel, text.rstrip() + "\n\n" + ADV_NOTE)


# ---------------------------------------------------------------------------
# 6. Put every app walkthrough on an explicit V1 filming hold.
# ---------------------------------------------------------------------------
for path in sorted((ROOT / "scripts").glob("*WALKTHROUGH*.md")):
    rel = str(path.relative_to(ROOT))
    if rel in {
        "scripts/01-4_WALKTHROUGH_foundation.md",
        "scripts/06-4_WALKTHROUGH_retirement-paycheck.md",
        "scripts/09-3_WALKTHROUGH_finish-test-review-and-save.md",
    }:
        continue
    text = path.read_text(encoding="utf-8")
    if "V1 FILMING HOLD" in text:
        continue
    lines = text.splitlines()
    insert_at = 1
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1
    hold = (
        "> **V1 FILMING HOLD:** The decision order is approved. Recheck the exact "
        "Home / Plan / Cash Flow / Protect path, labels, and save behavior against "
        "the corresponding V1 slice before screen capture. Do not record the legacy path."
    )
    lines[insert_at:insert_at] = [hold, ""]
    write(rel, "\n".join(lines))


# ---------------------------------------------------------------------------
# 7. Replace the affected visual briefs.
# ---------------------------------------------------------------------------
VISUALS = {
    "visuals/0-2_ask.md": """# 0.2 · Ask explains, guides, and deep-links

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
Ask is a global second set of eyes. Orange Plan owns the calculations and saved data; Ask explains the result and routes the user to the canonical workspace.

## The visual
A restrained header-level Ask button opens a drawer beside a Plan screen.

Three actions branch from the drawer:

- Explain this result
- Show what needs attention
- Compare a change in Preview

The proposed change flows into a Current-versus-Preview surface. It never writes directly to Current.

## Labels
Use `790 of 1,000` in the example. Show one deep link to Build & improve. Include a small footer: **No seeds, passwords, account numbers, or recovery secrets.**
""",
    "visuals/1-3a_thousand-paths.md": """# 1.3 · Quick estimate versus simulation result

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
The quick retirement estimate and the 1,000-simulation Plan result answer different questions.

## The visual
Left: one deterministic path labeled **Quick estimate**.

Right: 1,000 thin paths resolving into:

**790 of 1,000 worked**  
**Money lasted through age 95**

A footer reads: **Orange Plan standard · 800 of 1,000**.

## Motion
Build the single path first, then expand into the 1,000 paths. Keep planned retirement date and earliest modeled date as separate labels.
""",
    "visuals/1-3b_number-flow.md": """# 1.3 · Result status and date labels

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
A precise result still needs a freshness state, and the two retirement dates have different jobs.

## The visual
Top row:

- Planned retirement date
- Earliest modeled retirement date

Bottom row, four status cards:

- Preliminary — important facts remain
- Current — facts and calculation are current
- Stale — a modeled fact changed
- Unavailable — calculation or source data failed

Use concise provenance below: **Based on 14 accounts · 4 details could change this result.**
""",
    "visuals/6-3_guardrails.md": """# 6.3 · Simulation result and portfolio guardrails

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
The Plan result is a count out of 1,000. Spending guardrails are year-specific portfolio levels that trigger a separate review.

## The visual
Top:

**820 of 1,000 simulations worked**  
**Money lasted through age 95**

Bottom:

Lower guardrail                 Current                  Upper guardrail  
$1.45M ─────────────────────────●──────────────────────── $2.40M

State label: **Within your guardrails · No spending review needed**

## Important constraint
Do not draw 60 / 80 / 95 percentages as dollar guardrails. The values require the validated inverse portfolio-threshold calculation.
""",
    "visuals/9-1b_annual-lap.md": """# 9.1 · The four-destination review

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
The monthly and annual routines use the same four permanent destinations.

## The visual
A clean clockwise loop:

1. Home — current facts and Needs Attention
2. Cash Flow — income, spending, reserve, and saving
3. Plan — result, strategy, Scenarios, and Preview
4. Protect — custody, family, legal, and insurance

Center label: **Choose 1–3 actions**.

Show a small monthly badge and a deeper annual badge without creating two separate diagrams.
""",
    "visuals/9-2a_stress-vs-choice.md": """# 9.2 · Current versus Preview

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
A scenario answers one question. A real proposed change moves into Preview and stays separate from the saved plan until the user saves it.

## The visual
Two equal columns:

**Current**  
790 of 1,000  
Planned retirement · May 2030  
Earliest modeled · November 2030

**Preview**  
824 of 1,000  
Planned retirement · September 2030  
Earliest modeled · September 2030

Below them show one changed input and two materially changed outcomes. Avoid generic insight cards.
""",
    "visuals/9-2b_reading-order.md": """# 9.2 · Read Your Plan in four passes

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
Your Plan is a read-only document generated from Current. Fix facts and strategy at their source.

## The visual
Four large numbered sections:

1. Position — what is true now
2. Trajectory — result, dates, spending, and funding
3. Risk — what could break the plan
4. Actions — the next one to three moves

Footer: **Current plan · recalculated today · 790 of 1,000 through age 95**.
""",
}
for rel, content in VISUALS.items():
    write(rel, content)


# ---------------------------------------------------------------------------
# 8. Add the durable voice rule and V1 authority notes.
# ---------------------------------------------------------------------------
voice = read("scripts/VOICE-GUIDE.md")
VOICE_RULE = """
## Lead with the point

Say the affirmative conclusion first. Avoid building sentences around a rejected idea when the positive statement can stand on its own.

Prefer:

- **Use the four paths to identify where you are today.**
- **The account is the wrapper around the investments.**
- **The simulation result is a stress test of the saved plan.**
- **The goal is a plan the household wants that reaches the Orange Plan standard.**

Avoid repetitive structures such as:

- “This is not X. It is Y.”
- “The goal is not X. The goal is Y.”
- “Not because X, but because Y.”
- “This does not mean…” when the next sentence can state the actual point.

Keep direct negatives when they protect the student from a real mistake: security rules, legal and tax boundaries, unsupported app behavior, guarantees, execution limits, and facts the model cannot infer. A safety prohibition should sound like a prohibition, not a copywriting contrast.
""".strip()
if VOICE_RULE not in voice:
    write("scripts/VOICE-GUIDE.md", voice.rstrip() + "\n\n" + VOICE_RULE)

for rel in ("AUSTIN-AUTHORITY.md", "SOURCE-MATERIAL-POLICY.md", "CLAIM-REGISTRY.md"):
    text = read(rel)
    addition = """
## V1 plan-result and customer-language authority

- Normal users use the Orange Plan standard of 800 successful simulations out of 1,000.
- Customer-facing results lead with the count, through-age, planned retirement date, earliest modeled date, and truthful result state.
- A custom retirement test standard belongs in Advanced model settings.
- Spending guardrails are presented as lower, current, and upper portfolio levels only after the validated inverse calculation exists.
- Ask explains, guides, reviews, and deep-links. Financial calculations remain authoritative in the app, every material change stays in Preview until saved, and Ask never silently changes Current.
- Customer copy uses **Improve your plan**, **Build & improve**, **Save to plan**, and **Your Plan**.
- Spoken scripts lead with the direct point. Rhetorical “not X, but Y” framing is reserved for a genuine safety or accuracy boundary.
""".strip()
    if addition not in text:
        write(rel, text.rstrip() + "\n\n" + addition)


# ---------------------------------------------------------------------------
# 9. Update release status and production instructions.
# ---------------------------------------------------------------------------
status = read("FINALIZATION-STATUS.md")
status_add = """
## PR #227 V1 alignment — 2026-08-31

- Replaced normal-user confidence-target teaching with the fixed Orange Plan standard of 800 successful simulations out of 1,000.
- Reframed customer results around counts, through-age, planned versus earliest modeled retirement dates, and Preliminary / Current / Stale / Unavailable states.
- Rebuilt 0.2, 1.3, 6.3, 9.1, and 9.2 around Ask, Build & improve, Current versus Preview, portfolio guardrails, the four permanent destinations, and Your Plan.
- Rebuilt the Foundation, Retirement Income, and final-plan walkthrough sheets for the V1 contracts.
- Put every app walkthrough on a filming hold until its V1 slice is visually stable.
- Applied the direct-language pass across core and Advanced teaching layers and added the rule to the voice guide.

The remaining editorial step is Austin's chronological dictation and approval. Concept A-roll can be recorded after dictation. App captures remain blocked by the corresponding V1 UI slice, and professional publication gates remain unchanged.
""".strip()
if status_add not in status:
    write("FINALIZATION-STATUS.md", status.rstrip() + "\n\n" + status_add)

CHECKLIST = """# Production checklist

## Before filming a teaching lesson

- [ ] Read the script status: Austin dictation or pre-dictation filming draft.
- [ ] Confirm the lesson leads with the direct point rather than a rhetorical “not X, but Y” setup.
- [ ] Confirm customer-facing simulation language uses counts out of 1,000.
- [ ] Normal users use the Orange Plan standard of 800 of 1,000; no normal confidence-target control is taught.
- [ ] Planned retirement date and earliest modeled retirement date are labeled separately.
- [ ] Preliminary, Current, Stale, and Unavailable are used honestly.
- [ ] App navigation is excluded from A-roll unless the corresponding V1 slice is visually stable.
- [ ] Visual cue checked in `SCREEN-SHOOT-LIST.md`.
- [ ] Current figures and provider terms are kept out of evergreen spoken material when possible.

## App-capture gates

- [ ] Foundation and first-result capture waits for V1 Slices 2–3.
- [ ] Cash Flow capture waits for Slice 4.
- [ ] Scenarios and Current-versus-Preview capture waits for Slice 5 and the owning strategy workspace.
- [ ] Protect capture waits for Slice 6.
- [ ] Debt, Allocation, Tax, Retirement Income/guardrails, and Borrowing wait for Slices 7–11.
- [ ] Ask, Your Plan, Settings, Connections, and external-AI export wait for Slice 12.
- [ ] Every walkthrough path is rechecked against the exact Preview build immediately before recording.

## Product-language checks

- [ ] Home = current facts and attention.
- [ ] Cash Flow = income, spending, taxes, debt payments, reserve, and saving.
- [ ] Plan = result, Build & improve, strategy, Scenarios, Current, and Preview.
- [ ] Protect = custody, family, beneficiaries, legal readiness, and insurance.
- [ ] Customer verbs are Build, Make accurate, Improve, Preview, Save, and Keep current.
- [ ] The final read-only artifact is Your Plan.
- [ ] Guardrail summary shows lower/current/upper portfolio levels only after the validated inverse model exists.
- [ ] Exact linked facts may record with provenance; ambiguity becomes one question in Needs Attention.

## Professional gates

- [ ] CPA or EA reviews current-year tax execution guidance.
- [ ] Exact device, firmware, provider, descriptor, and recovery process verified before custody footage.
- [ ] Licensed insurance professional reviews policy mechanics and contract-specific claims.
- [ ] State-licensed estate attorney reviews state-specific authority, trust, and executor material.
"""
write("PRODUCTION-CHECKLIST.md", CHECKLIST)
write("FILMING-CHECKLIST.md", CHECKLIST)


# ---------------------------------------------------------------------------
# 10. Generate the direct-language audit.
# ---------------------------------------------------------------------------
PATTERNS = [
    re.compile(r"\bnot\b[^.\n]{0,120}\bbut\b", re.I),
    re.compile(r"\bThe (?:goal|point|question|purpose|job|answer) is not\b", re.I),
    re.compile(r"\bThis (?:does not|doesn't) mean\b", re.I),
    re.compile(r"\bI (?:do not|don't) think\b", re.I),
]
SAFETY = re.compile(
    r"financial advice|guarantee|promise|seed|private key|passphrase|password|PIN|secret|tax|legal|insurance|unsupported|eligible|automatic|provider|withdrawal|sale|purchase|transfer|basis|security|recovery",
    re.I,
)
remaining: list[tuple[str, int, str, str]] = []
for path in sorted((ROOT / "scripts").rglob("*.md")):
    if path.name in {"README.md", "VOICE-GUIDE.md"}:
        continue
    if "WALKTHROUGH" in path.name or "DEMO" in path.name:
        continue
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if any(pattern.search(line) for pattern in PATTERNS):
            kind = "retained boundary" if SAFETY.search(line) else "remaining contrast"
            remaining.append((str(path.relative_to(ROOT)), number, kind, line.strip()))

contrast_count = sum(1 for item in remaining if item[2] == "remaining contrast")
boundary_count = len(remaining) - contrast_count
report = [
    "# Direct-language audit",
    "",
    "The active teach scripts were reviewed for rhetorical denial patterns such as `not X, but Y`, `the goal is not`, `this does not mean`, and `I do not think`.",
    "",
    f"- Remaining high-confidence contrasts: **{contrast_count}**",
    f"- Retained safety / accuracy boundaries: **{boundary_count}**",
    "",
    "The editing rule is affirmative-first. Direct negatives remain where removing them would weaken a security, legal, tax, execution, eligibility, or modeling boundary.",
]
if remaining:
    report += ["", "## Reviewed remaining lines", "", "| File | Line | Classification | Text |", "|---|---:|---|---|"]
    for rel, line_no, kind, line in remaining:
        safe_line = line.replace("|", "\\|")
        report.append(f"| `{rel}` | {line_no} | {kind} | {safe_line} |")
write("DIRECT-LANGUAGE-AUDIT.md", "\n".join(report))

alignment_report = """# V1 course alignment report

## Authority

This pass aligns the course to the accepted PR #227 V1 product contracts while preserving Austin's course order and planning philosophy.

## Substantive rewrites

- 0.2 — Ask explains, guides, reviews, and deep-links; changes remain in Preview.
- 1.3 — quick deterministic estimate, preliminary simulation result, fixed standard, date labels, and freshness states.
- 6.3 — count-first simulation teaching and lower/current/upper portfolio guardrails.
- 9.1 — monthly and annual review through Home, Cash Flow, Plan, and Protect.
- 9.2 — Scenarios, Current versus Preview, Save to plan, and Your Plan.

## Narrow pickups

- 0.1 now uses the fixed-standard, preliminary-result, Build & improve, and improve-language contracts.
- A1.1 explains the Advanced custom retirement test standard.
- All app walkthroughs carry a V1 filming hold.

## Stable for A-roll after Austin dictation

The planning concepts, examples, decision frameworks, and approved graphics can be filmed after the chronological dictation pass.

## Held for later capture

Exact navigation, first-result choreography, account activity and Needs Attention, portfolio guardrail levels, Current-versus-Preview UI, Ask, Your Plan, Settings, and Connections wait for their corresponding V1 slices.
"""
write("V1-COURSE-ALIGNMENT.md", alignment_report)


# ---------------------------------------------------------------------------
# 11. Regenerate dependent layers.
# ---------------------------------------------------------------------------
commands = [
    ["python3", "tools/split-modules.py"],
    ["python3", "tools/split-modules.py", "--advanced"],
    ["python3", "tools/build-onefile.py"],
    ["python3", "tools/build-circle-structure.py"],
    ["python3", "tools/build-dictation-order.py"],
    ["python3", "tools/build-film-order.py"],
    ["python3", "tools/build-shoot-list.py"],
]
for command in commands:
    subprocess.run(command, cwd=ROOT, check=True)

# Normalize generated-file endings.
for rel in ("ALL-SCRIPTS.md", "CIRCLE-STRUCTURE.md", "DICTATION-ORDER.md", "FILM-ORDER.md", "SCREEN-SHOOT-LIST.md"):
    p = ROOT / rel
    if p.exists():
        p.write_text(p.read_text(encoding="utf-8").rstrip() + "\n", encoding="utf-8")

print("V1 course alignment and direct-language pass applied.")
