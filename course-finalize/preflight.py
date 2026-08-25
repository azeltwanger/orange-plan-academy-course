#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name('apply.py')
text = path.read_text(encoding='utf-8')
replacements = {
    'Then zoom out to 2 to 5 years.': 'Next, use the 2-to-5-year window.',
    'Write the move in one sentence without mentioning the recent Bitcoin price.': 'Write a plain explanation of the move without mentioning the recent Bitcoin price.',
    'Write the move in one sentence without mentioning recent price action.': 'Write a plain explanation of the move without mentioning recent price action.',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'preflight phrase missing: {old}')
    text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
