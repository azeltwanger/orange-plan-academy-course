#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def extract(text: str, start_pattern: str, next_pattern: str) -> str:
    start = re.search(start_pattern, text, re.M)
    if not start:
        raise RuntimeError(f"Missing module start: {start_pattern}")
    tail = text[start.start():]
    nxt = re.search(next_pattern, tail[start.end() - start.start():], re.M)
    if not nxt:
        return tail.strip() + "\n"
    end = (start.end() - start.start()) + nxt.start()
    return tail[:end].strip() + "\n"


core = (ROOT / "MASTER-COURSE.md").read_text(encoding="utf-8")
core_module = extract(
    core,
    r"^# Unit 8 · Module 7 — Custody$",
    r"^# Unit 9 · Module 8 — Estate \+ Inheritance$",
)
(ROOT / "modules/07-custody.md").write_text(core_module, encoding="utf-8")

advanced = (ROOT / "MASTER-ADVANCED.md").read_text(encoding="utf-8")
advanced_module = extract(
    advanced,
    r"^# Advanced Module 7 — Custody$",
    r"^# Advanced Module 8 — Estate \+ Inheritance$",
)
(ROOT / "modules/advanced/A07-custody.md").write_text(advanced_module, encoding="utf-8")

print("Synced Module 7 core and Advanced generated module files.")
