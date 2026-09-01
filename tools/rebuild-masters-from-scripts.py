#!/usr/bin/env python3
"""Rebuild every lesson section in the master files from canonical scripts.

The scripts are the spoken/capture authority. Unit introductions remain in the
masters; lesson bodies, titles, runtimes, and active gates come from scripts.
This removes stale duplicate prose left by older one-way sync tools.
"""
from __future__ import annotations

import glob
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIVIDER = "=" * 60


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
    # Preserve order while removing duplicates.
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


def rebuild(master_path: Path, lessons: dict[str, Lesson]) -> None:
    master = master_path.read_text(encoding="utf-8")
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
    rebuild(ROOT / "MASTER-COURSE.md", script_lessons(False))
    rebuild(ROOT / "MASTER-ADVANCED.md", script_lessons(True))


if __name__ == "__main__":
    main()
