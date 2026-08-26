#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "I would not automatically stop buying Bitcoin for seven years because your child may go to college."
NEW = "I would not automatically pause Bitcoin purchases for seven years because your child may go to college."

for relative in [
    "scripts/02-4_optional-college-is-a-funding-stack.md",
    "MASTER-COURSE.md",
]:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if OLD not in text:
        raise RuntimeError(f"voice phrase not found in {relative}")
    path.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
