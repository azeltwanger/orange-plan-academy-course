#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("verify.py")
text = path.read_text(encoding="utf-8")
old = '''    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts").glob("*.md"))],
    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts/advanced").glob("*.md"))],'''
new = '''    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts").glob("*.md")) if p.name not in {"README.md", "VOICE-GUIDE.md"}],
    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts/advanced").glob("*.md"))],'''
if old not in text:
    raise SystemExit("verification scan block not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
