#!/usr/bin/env python3
"""Sync canonical walkthrough/demo sheets into MASTER-COURSE.md.

Walkthrough scripts own the current implementation instructions. This tool keeps
master/module layers from retaining stale routes or product behavior after a
capture sheet changes.

Usage:
    python3 tools/sync-walkthroughs-to-master.py 1.4 6.4 9.3
    python3 tools/sync-walkthroughs-to-master.py --all
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "MASTER-COURSE.md"
SCRIPTS = ROOT / "scripts"


def lesson_number(path: Path) -> str | None:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    match = re.match(r"^#\s+(\d+\.\d+)\s+·\s+", first)
    return match.group(1) if match else None


def script_for(num: str) -> Path | None:
    stem = f"{int(num.split('.')[0]):02d}-{num.split('.')[1]}"
    for path in sorted(SCRIPTS.glob(f"{stem}_*.md")):
        if "WALKTHROUGH" in path.name or "DEMO" in path.name:
            return path
    return None


def sync_section(master: str, path: Path, num: str) -> str:
    raw = path.read_text(encoding="utf-8")
    first, _, body = raw.partition("\n")
    title_match = re.match(r"^#\s+\d+\.\d+\s+·\s+(.+)$", first.strip())
    if not title_match:
        raise RuntimeError(f"Cannot parse title from {path.relative_to(ROOT)}")
    title = title_match.group(1).strip()

    start_match = re.search(rf"^## {re.escape(num)} .+$", master, re.M)
    if not start_match:
        raise RuntimeError(f"Lesson {num} is missing from MASTER-COURSE.md")
    after = master[start_match.end():]
    next_match = re.search(r"\n#{1,2} (?:\d+\.\d+|Unit )", after)
    end = start_match.end() + (next_match.start() + 1 if next_match else len(after))
    section = master[start_match.start():end]

    if "\n---\n" not in section:
        raise RuntimeError(f"Lesson {num} has no master header/body divider")
    header, _ = section.split("\n---\n", 1)
    header_lines = header.splitlines()
    header_lines[0] = f"## {num} {title}"
    words = len(body.split())
    header = "\n".join(header_lines)
    header = re.sub(
        r"· [\d,~]+ words · ~[\d.]+ min",
        f"· ~{words:,} words · ~{words / 155:.0f} min",
        header,
    )

    replacement = header + "\n---\n\n" + body.strip() + "\n\n"
    return master[:start_match.start()] + replacement + master[end:]


def main() -> None:
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if "--all" in sys.argv:
        numbers = [
            num for path in sorted(SCRIPTS.glob("*.md"))
            if ("WALKTHROUGH" in path.name or "DEMO" in path.name)
            and (num := lesson_number(path))
        ]
    else:
        numbers = args
    if not numbers:
        raise SystemExit(__doc__)

    master = MASTER.read_text(encoding="utf-8")
    for num in numbers:
        path = script_for(num)
        if path is None:
            raise RuntimeError(f"No walkthrough/demo script found for {num}")
        master = sync_section(master, path, num)
        print(f"synced {num} from {path.relative_to(ROOT)}")
    MASTER.write_text(master, encoding="utf-8")


if __name__ == "__main__":
    main()
