#!/usr/bin/env python3
"""Rebuild every lesson section in the master files from canonical scripts.

The scripts are the spoken/capture authority. Unit introductions remain in the
masters; lesson bodies, titles, runtimes, and active gates come from scripts.
The durable V1 preambles are normalized on every run so stale product framing
cannot survive above the first lesson.
"""
from __future__ import annotations

import glob
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIVIDER = "=" * 60

CORE_PREAMBLE = """# Orange Plan Academy — filming master

**Aligned to the committed Orange Plan V1 product contracts in PR #227.** Exact walkthrough routes, labels, and screen hierarchy are verified against the same approved Preview commit used on camera.

This master uses the following authority order:

1. Austin's dictation for voice, examples, and planning judgment.
2. Austin's slide decks for teaching sequence and required visuals.
3. Committed Orange Plan V1 product contracts for customer-facing concepts and ownership.
4. The final approved V1 Preview commit for walkthrough labels, routes, and on-screen behavior.
5. Primary-source research for factual accuracy.
6. Older generated scripts only as disposable reference.

A script labeled **AUSTIN DICTATION** preserves Austin's words with only factual, app-flow, or walkthrough-separation edits. A script labeled **PRE-DICTATION FILMING DRAFT** is editorially prepared to make dictation and filming fast, but it does not become Austin-authored merely because it passes automated checks.

The teach lesson explains the concept and helps the student make a decision. The walkthrough performs the clicks, shows what the app calculates, and returns to Build & improve. The app's Build & improve panel may list tasks in a different order; the course intentionally teaches **Module 3 Allocation + Next-Dollar** before **Module 4 Debt**, then returns the final Extra Debt amount to the contribution waterfall.

Foundation reads the first preliminary Plan result. Module 9 confirms the completed current baseline after the major facts and strategy decisions are in place.

## Professional publication gates

- Targeted CPA or EA review before publishing current-year tax examples and execution guidance.
- Exact device, firmware, provider, and recovery process verified before setup-specific footage.
- Licensed insurance professional reviews policy mechanics and contract-specific claims before publication.
- State-licensed estate attorney reviews state-specific authority, trust, and executor material before publication.

---

"""

ADVANCED_PREAMBLE = """# Orange Plan Academy — Advanced Library

The Advanced Library extends the core course under the same Orange Plan V1 product contracts. Every lesson is optional and keeps the condition or professional review stated at the top. Exact app paths and provider-specific mechanics are verified against the same approved Preview or provider version used on camera.

"""


@dataclass
class Lesson:
    num: str
    title: str
    kind: str
    minutes: float
    status: str
    gate: str | None
    body: str


def master_body(body: str) -> str:
    out: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        match = re.match(r"^== (.+) ==$", stripped)
        if match:
            words = match.group(1).lower()
            out += ["", "### " + words[:1].upper() + words[1:], ""]
        elif stripped.startswith("🎬 VISUAL"):
            out.append("> 🎬 **" + stripped[len("🎬 "):].strip() + "**")
        else:
            out.append(line.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def parse_script(path: Path) -> Lesson:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if text.startswith(("TELEPROMPTER SCRIPT", "ADVANCED TELEPROMPTER SCRIPT")):
        title_line = next(line for line in lines[:10] if re.match(r"^A?\d+\.\d+\s+\S", line))
        num, title = title_line.split(" ", 1)
        divider = next(i for i, line in enumerate(lines) if line.strip() == DIVIDER)
        body = master_body("\n".join(lines[divider + 1:]).strip())
        gate_line = next((line for line in lines[:divider] if line.startswith("PUBLICATION GATE:")), None)
        gate = gate_line.split(":", 1)[1].strip() if gate_line else None
        status = "AUSTIN DICTATION" if "AUSTIN DICTATION" in "\n".join(lines[:divider]) else "PRE-DICTATION FILMING DRAFT"
        return Lesson(num, title, "TEACH", len(body.split()) / 155, status, gate, body)

    first, _, body = text.partition("\n")
    match = re.match(r"^#\s+(A?\d+\.\d+)\s+·\s+(.+)$", first.strip())
    if not match:
        raise RuntimeError(f"Cannot parse {path.relative_to(ROOT)}")
    num, title = match.group(1), match.group(2).strip()
    kind = "DEMO" if "DEMO" in path.name else "WALKTHROUGH"
    minutes_match = re.search(r"\*\*Screen capture · about ([\d.]+) minutes\*\*", body)
    minutes = float(minutes_match.group(1)) if minutes_match else len(body.split()) / 155
    return Lesson(num, title, kind, minutes, "IMPLEMENTATION SHEET", None, body.strip())


def script_lessons(advanced: bool) -> dict[str, Lesson]:
    pattern = "scripts/advanced/*.md" if advanced else "scripts/*.md"
    paths = [Path(p) for p in glob.glob(str(ROOT / pattern))]
    paths = [p for p in paths if p.name not in {"README.md", "VOICE-GUIDE.md"}]
    return {lesson.num: lesson for lesson in (parse_script(p) for p in sorted(paths))}


def section_end(master: str, start_end: int) -> int:
    match = re.search(r"\n#{1,2} (?:A?\d+\.\d+|Unit |Advanced Module )", master[start_end:])
    return start_end + (match.start() + 1 if match else len(master) - start_end)


def carry_markers(old_section: str) -> list[str]:
    markers: list[str] = []
    patterns = (
        r"^.*FILMING BLOCKER.*$",
        r"^.*PUBLICATION BLOCKER.*$",
        r"^.*NO FILMING PLANNED.*$",
        r"^.*HOLD FOR REDICTATION.*$",
        r"^.*FLAGGED FOR REBUILD.*$",
        r"^.*pending estate-attorney review.*$",
        r"^.*CPA-blocking.*$",
    )
    for pattern in patterns:
        markers.extend(m.group(0).rstrip() for m in re.finditer(pattern, old_section, re.M | re.I))
    return list(dict.fromkeys(markers))


def render(lesson: Lesson, markers: list[str]) -> str:
    if lesson.kind == "TEACH":
        meta = f"*`TEACH` · ~{lesson.minutes:.1f} min · {lesson.status}*"
    else:
        meta = f"*`{lesson.kind}` · ~{lesson.minutes:.0f} min · {lesson.status}*"
    lines = [f"## {lesson.num} {lesson.title}", "", meta]
    if lesson.gate:
        lines += ["", f"> **Publication gate:** {lesson.gate}"]
    if markers:
        lines += ["", *markers]
    lines += ["", lesson.body, "", "---", ""]
    return "\n".join(lines)


def normalize_preamble(master: str, advanced: bool) -> str:
    marker = "# Advanced Module " if advanced else "# Unit "
    index = master.find(marker)
    if index < 0:
        raise RuntimeError(f"Cannot find first module marker: {marker}")
    preamble = ADVANCED_PREAMBLE if advanced else CORE_PREAMBLE
    return preamble + master[index:]


def rebuild(master_path: Path, lessons: dict[str, Lesson], advanced: bool) -> None:
    master = normalize_preamble(master_path.read_text(encoding="utf-8"), advanced)
    sections = list(re.finditer(r"^## (A?\d+\.\d+) .+$", master, re.M))
    found: set[str] = set()
    for match in reversed(sections):
        num = match.group(1)
        lesson = lessons.get(num)
        if lesson is None:
            raise RuntimeError(f"{master_path.name} has {num} but no canonical script")
        end = section_end(master, match.end())
        old = master[match.start():end]
        master = master[:match.start()] + render(lesson, carry_markers(old)) + master[end:]
        found.add(num)

    missing = sorted(set(lessons) - found)
    if missing:
        raise RuntimeError(f"{master_path.name} is missing script sections: {', '.join(missing)}")

    master_path.write_text(master.rstrip() + "\n", encoding="utf-8")
    print(f"rebuilt {master_path.name}: {len(found)} lessons")


def main() -> None:
    rebuild(ROOT / "MASTER-COURSE.md", script_lessons(False), False)
    rebuild(ROOT / "MASTER-ADVANCED.md", script_lessons(True), True)


if __name__ == "__main__":
    main()
