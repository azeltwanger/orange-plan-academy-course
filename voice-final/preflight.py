#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("apply.py")
text = path.read_text(encoding="utf-8")
old = '    marker = "## Complete when"'
new = '    marker = "**Done when:**"'
if old not in text:
    raise SystemExit("student walkthrough marker template not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
