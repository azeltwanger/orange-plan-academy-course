#!/usr/bin/env python3
"""Regenerate lesson-text/ from the canonical scripts and module checkpoints.

The production scripts are the spoken authority. Student text uses the same
lesson body without filming cues, followed by the module's implementation handoff
and completion checklist. Advanced lessons retain their publication gate and do
not receive a core-module checkpoint. Canonical output names stay stable so
existing course links survive script-label changes.
"""
from __future__ import annotations

import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINTS = ROOT / "MODULE-CHECKPOINTS.md"

WALKTHROUGH = {
    0: None,
    1: "1.4",
    2: "2.5",
    3: "3.5",
    4: "4.2",
    5: "5.3",
    6: "6.4",
    7: "7.5",
    8: "8.5",
    9: "9.3",
}


def parse_checkpoints() -> dict[int, list[str]]:
    text = CHECKPOINTS.read_text(encoding="utf-8")
    blocks = list(re.finditer(r"^## Module (\d+) — .+$", text, re.M))
    out: dict[int, list[str]] = {}
    for i, match in enumerate(blocks):
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(text)
        segment = text[match.start():end]
        out[int(match.group(1))] = [
            line.rstrip() for line in segment.splitlines() if line.startswith("- [ ]")
        ]
    return out


def script_parts(path: Path) -> tuple[str, str, str | None, bool]:
    text = path.read_text(encoding="utf-8")
    advanced = path.parent.name == "advanced"
    gate = None
    if text.startswith(("TELEPROMPTER", "ADVANCED TELEPROMPTER")):
        lines = text.splitlines()
        title_line = next(
            line for line in lines[:8]
            if re.match(r"^A?\d+\.\d+\s+\S", line)
        )
        num, title = title_line.split(" ", 1)
        for line in lines[:10]:
            if line.startswith("PUBLICATION GATE:"):
                gate = line.split(":", 1)[1].strip()
        return num, title, gate, advanced

    first, _, _ = text.partition("\n")
    match = re.match(r"^#\s+(A?\d+\.\d+)\s+·\s+(.+)$", first.strip())
    if not match:
        raise ValueError(f"Cannot parse title from {path}")
    return match.group(1), match.group(2), None, advanced


def clean_body(body: str) -> str:
    out: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("🎬 VISUAL"):
            continue
        match = re.match(r"^== (.+) ==$", stripped)
        if match:
            words = match.group(1).lower()
            out += ["", "## " + words[:1].upper() + words[1:], ""]
            continue
        out.append(line.rstrip())
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def core_lesson_text(path: Path, num: str, title: str, body: str,
                     checkpoints: dict[int, list[str]]) -> str:
    module = int(num.split(".", 1)[0])
    is_capture = "WALKTHROUGH" in path.name or "DEMO" in path.name
    parts = [f"# {num} · {title}", ""]
    if is_capture:
        parts += [
            "Follow the walkthrough video and the matching Build & improve area. "
            "The implementation is complete when the real data and saved decision "
            "exist in Orange Plan.",
            "",
        ]
    else:
        parts += [clean_body(body), ""]
        if WALKTHROUGH.get(module):
            parts += [
                "## Apply it",
                "",
                f"Use walkthrough {WALKTHROUGH[module]} to enter the decision and "
                "confirm what Orange Plan calculated.",
                "",
            ]
    checklist = checkpoints.get(module, [])
    if checklist:
        parts += ["## Module checkpoint", "", *checklist, ""]
    return "\n".join(parts).rstrip() + "\n"


def advanced_lesson_text(num: str, title: str, body: str, gate: str | None) -> str:
    parts = [f"# {num} · {title}", ""]
    if gate:
        parts += [f"**Publication gate:** {gate}", ""]
    parts += [clean_body(body), ""]
    return "\n".join(parts).rstrip() + "\n"


def output_name(path: Path) -> str:
    name = path.name.replace("WALKTHROUGH", "walkthrough").replace("DEMO", "demo")
    return name.replace("_walkthrough_", "_walkthrough-").replace("_demo_", "_demo-")


def main() -> None:
    checkpoints = parse_checkpoints()
    core_files = sorted(Path(p) for p in glob.glob(str(ROOT / "scripts" / "*.md")))
    adv_files = sorted(Path(p) for p in glob.glob(str(ROOT / "scripts" / "advanced" / "*.md")))
    files = [
        p for p in core_files + adv_files
        if p.name not in {"README.md", "VOICE-GUIDE.md"}
    ]

    written: set[Path] = set()
    for path in files:
        num, title, gate, advanced = script_parts(path)
        text = path.read_text(encoding="utf-8")
        if text.startswith(("TELEPROMPTER", "ADVANCED TELEPROMPTER")):
            lines = text.splitlines()
            divider = next(i for i, line in enumerate(lines) if set(line.strip()) == {"="})
            body = "\n".join(lines[divider + 1:]).strip()
        else:
            body = text.partition("\n")[2].strip()

        outdir = ROOT / "lesson-text" / ("advanced" if advanced else "")
        outdir.mkdir(parents=True, exist_ok=True)
        outpath = outdir / output_name(path)
        if advanced:
            rendered = advanced_lesson_text(num, title, body, gate)
        else:
            rendered = core_lesson_text(path, num, title, body, checkpoints)
        outpath.write_text(rendered, encoding="utf-8")
        written.add(outpath)

    for directory in (ROOT / "lesson-text", ROOT / "lesson-text" / "advanced"):
        for path in directory.glob("*.md"):
            if path not in written:
                path.unlink()
                print(f"removed stale {path.relative_to(ROOT)}")

    print(f"wrote {len(written)} lesson-text files")


if __name__ == "__main__":
    main()
