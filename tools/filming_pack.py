"""Separate spoken teaching, overlays and walkthrough takes for filming."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

REVISION_BASE = 'c3e08387c03e6c7236ec5ea798931ace81d4c1f5'
ORIGINALS = {
    'scripts/02-3_size-the-reserve-for-the-job-it-has-to-do.md': 'bcf42a95d1ee40e7e5164cf1e259a59ccc1d939d897af16cbcafa63a3728b8f7',
    'scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md': '89113d92de60787c8c8740fd9a129ea221c501c43e6c38fd5e3bcc991bc1db33',
    'scripts/working/D07_prove-a-wallet-backup-with-a-safe-test-setup.md': 'd6d3c952667f25383b19a9b8151a0c099f8a2bf257fcbf67c8263d1edbb28fa2',
    'teleprompter/core/8-4.txt': '393118d5c8d582b77927138a5014e7ba2c41aa7e438574f287c5b314a8f96f1b',
}
CHAPTER_COUNTS = {'W01': 10, 'W02': 7, 'W03': 6, 'W04': 8, 'W05': 6,
                  'W06': 8, 'W07': 4, 'D07': 8, 'W08': 5, 'W09': 5, 'W10': 5}
SLIDE_STEPS = {
    '0.1': 'Foundation 1–2: begin a working plan',
    '1.2': 'Foundation 3: verify baseline data',
    '1.4': 'Foundation 5, 12: starting assumptions and their limits',
    '1.5': 'Foundation 6–8, 11–12: scenarios, working date, update triggers',
    '2.1': 'Cash Flow 4–6, 17–18: income, Keep / Cut / Reduce, usable surplus',
    '2.3': 'Cash Flow 7–8, 12–14: target, gap, funding, automation',
    '2.4': 'Foundation 4; Cash Flow 10–11: expected events and spending dates',
    '2.5': 'Foundation 4; Cash Flow 11: the education commitment; expanded in the existing college script',
    '3.1': 'Debt 3, 5, 10: existing terms, debt tolerance, payment decisions',
    '3.4': 'Debt 4, 8: purpose and financing structure',
    '3.6': 'Debt 6–10: leverage, stress, collateral, repayment rules',
    'A3.1': 'Debt 9 plus Austin’s September 10 sizing and collateral clarification',
    'A3.2': 'Debt 8: financing structure; existing unusual-terms reference',
    '4.3': 'Allocation 3–7: current position, conviction, purpose, target, stress',
    '4.5': 'Allocation 9–11: account access, Traditional / Roth, permitted holdings',
    '4.7': 'Allocation 8, 12: next-dollar order and scheduled contribution instructions',
    '5.1': 'Tax 3–4, 8–10: basis, account treatment, relevant tax action',
    '5.4': 'Tax 5–7, 10: timing, future distributions, conversion comparison',
    'A5.1': 'Tax 5–7: extend the comparison across multiple years',
    'A5.2': 'Tax 3, 8: records and instructions for an actual sale',
    '6.1': 'Retirement Income 3–8: spending, income, gap, dates, access, funding',
    '6.3': 'Retirement Income 3: price healthcare; existing healthcare lesson supplies the detail',
    '6.6': 'Retirement Income 10: compare sale, borrowing and other funding',
    '6.8': 'Retirement Income 9, 11–12: annual spending and reserve refill, with accepted corrections',
    'A6.3': 'Retirement Income 7: verify access before the relevant account date',
    '7.1': 'Custody 3–4: arrangement, responsibilities and recoverability',
    '7.2': 'Custody 5–7: secure access, test recovery, remove a single point of failure',
    'A7.1': 'Custody 8–10: passphrase, multisig and support; corrected key/configuration distinctions',
    '8.1': 'Estate 3–8, 15: people, authority, access, heir letter, check-in and actions',
    '8.4': 'Existing insurance material and Austin’s September 10 needs/resources decision; no insurance deck supplied',
    'A8.1': 'Estate 9–13: whether a trust has a job, trade-offs and implementation questions',
    '9.1': 'Foundation 8; Estate 14; Maintenance SOPs M8S01–M8S05: changes, actions, next review',
    '10.1': 'Foundation 9; Retirement Income 13; Estate 14–15; existing final-plan review',
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def revision(root: Path) -> dict:
    data = json.loads((root/'production/stepwise-revision.json').read_text(encoding='utf-8'))
    if data.get('version') != 1 or data.get('base_commit') != REVISION_BASE:
        raise ValueError('Unrecognized filming revision')
    if data.get('authority') != 'reference/owner-stepwise-direction-20260910.md':
        raise ValueError('Missing owner direction for filming revision')
    entries = data.get('preserved_originals', [])
    if len(entries) != len(ORIGINALS) or {x['path'] for x in entries} != set(ORIGINALS):
        raise ValueError('Filming revision loses a protected original')
    for item in entries:
        expected_archive = 'source-material/pre-stepwise/'+Path(item['path']).name
        if item['archive'] != expected_archive or item['sha256'] != ORIGINALS[item['path']]:
            raise ValueError('Protected original identity changed')
        original = (root/item['archive']).read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(original)).encode()+b'\0'+original).hexdigest()
        if sha(original) != item['sha256'] or blob != item['git_blob']:
            raise ValueError('Protected pre-stepwise source changed: '+item['path'])
    protected = set(ORIGINALS) - {'teleprompter/core/8-4.txt'}
    if set(data.get('active_protected', {})) != protected:
        raise ValueError('Active revised protected scripts have not been pinned')
    for path, expected in data['active_protected'].items():
        if not re.fullmatch('[0-9a-f]{64}', expected) or sha((root/path).read_bytes()) != expected:
            raise ValueError('Revised protected script changed: '+path)
    return data


def section(text: str, name: str) -> str:
    found = re.search(r'^### '+re.escape(name)+r'\s*\n(.*?)(?=^### |\Z)', text, re.M|re.S)
    return found.group(1).strip() if found else ''


def clean_cell(text: str) -> str:
    return text.strip().strip('`').strip('“”"')


def overlays(text: str) -> list[tuple[str, str, str]]:
    table = section(text, 'Text overlays — not spoken')
    entries = []
    for line in table.splitlines():
        if not line.startswith('|'):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells) != 3 or all(re.fullmatch(r'[-: ]+', x) for x in cells):
            continue
        if cells[0].lower().startswith(('cue', 'spoken', 'exact')):
            continue
        entries.append(tuple(clean_cell(x) for x in cells))
    return entries


def chapters(text: str) -> list[dict]:
    headings = list(re.finditer(r'^#### Chapter (\d+)[^\n]*', text, re.M))
    result = []
    for i, heading in enumerate(headings):
        end = headings[i+1].start() if i+1 < len(headings) else len(text)
        block = text[heading.end():end]
        fields = {}
        for name in ['Show', 'Narration', 'Overlay', 'Verify', 'Capture dependency']:
            matches = re.findall(r'^\*\*'+re.escape(name)+r':\*\*\s*(.*?)(?=^\*\*[^\n]+:\*\*|^### |\Z)', block, re.M|re.S)
            if len(matches) != 1 or not matches[0].strip():
                raise ValueError(f"Chapter {heading.group(1)} needs one complete {name} field")
            fields[name] = matches[0].strip()
        result.append({'number': int(heading.group(1)), 'title': heading.group().removeprefix('#### '), **fields})
    return result


def validate(rows: list[dict], practical: list[str]) -> dict:
    overlay_count = scene_count = 0
    for row in rows:
        if row['id'] in practical:
            scenes = chapters(row['text'])
            expected = CHAPTER_COUNTS[row['id']]
            if [x['number'] for x in scenes] != list(range(1, expected+1)):
                raise ValueError('Missing, duplicated or renumbered filming chapter: '+row['id'])
            for scene in scenes:
                speech = scene['Narration']
                if len(speech.split()) < 15 or re.search(r'\bTODO\b|\bTBD\b|\[INSERT|\[VERIFY|\*\*Show:', speech, re.I):
                    raise ValueError('Unfinished or contaminated walkthrough speech: '+row['id'])
            scene_count += len(scenes)
        else:
            for name in ['Do this', 'Text overlays — not spoken', 'Walkthrough handoff — not spoken']:
                if not section(row['text'], name):
                    raise ValueError('Missing '+name+': '+row['id'])
            cards = overlays(row['text'])
            if not cards:
                raise ValueError('No usable overlay cues: '+row['id'])
            for cue, copy, treatment in cards:
                if cue not in row['read'] or not copy or not treatment:
                    raise ValueError('Overlay cue does not match spoken text: '+row['id']+' / '+cue)
            overlay_count += len(cards)
    return {'teaching_overlays': overlay_count, 'walkthrough_chapters': scene_count}


def outputs(root: Path, rows: list[dict], core: list[str], advanced: list[str], practical: list[str], pairings: dict) -> dict[str, str]:
    validate(rows, practical)
    by = {x['id']: x for x in rows}
    result = {}
    stepmap = '# Course steps and slide sources\n\nThe slide steps organize the teaching. Their older financial wording does not override current owner decisions, corrected facts or the future app contracts. Teaching and implementation are separate recordings on the same lesson page.\n\n'
    stepmap += '| Recording | Do this | Source steps | Separate walkthrough |\n|---|---|---|---|\n'
    overlay_master = '# Teaching overlays and editor cues\n\nOnly the teleprompter text is spoken. Use these short overlays when the matching line is heard. Source scripts contain the full context and example labels.\n\n'
    for lid in core+advanced:
        row = by[lid]
        number = f'{core.index(lid)+1:02d}' if lid in core else lid
        task = section(row['text'], 'Do this').replace('\n', ' ').replace('|', '/')
        target = pairings.get(lid, 'See the lesson’s conditional handoff')
        stepmap += f"| [{number} — {row['title']}]({row['path']}) | {task} | {SLIDE_STEPS[lid]} | {target} |\n"
        overlay_master += f"## {number} — [{row['title']}]({row['path']})\n\n"+section(row['text'], 'Text overlays — not spoken')+'\n\n'
    result['COURSE-STEP-MAP.md'] = stepmap
    result['TEACHING-OVERLAYS.md'] = overlay_master
    walk_master = '# Separate walkthrough recording scripts\n\nThese are future-design scripts, prepared against PR #227. Capture each chapter separately after its screen/procedure is verified. Only each Narration block is spoken. The clean files linked below exclude directions, overlays and verification notes.\n\n'
    capture = '# Walkthrough capture dependencies\n\nWritten scripts and filming evidence are separate. Every row remains unverified until the actual redesigned flow or exact device procedure has been checked. The historical CAPTURE-RECEIPTS.md is preserved unchanged.\n\n| Take | Paired recording script | Capture dependency | Finish evidence |\n|---|---|---|---|\n'
    walk_words = 0
    for lid in practical:
        row = by[lid]
        scenes = chapters(row['text'])
        complete_speech = []
        walk_master += f"## {lid} — [{row['title']}]({row['path']})\n\n"
        for scene in scenes:
            take = f"{lid}-{scene['number']:02d}"
            path = f'teleprompter/walkthrough/{take}.txt'
            result[path] = scene['Narration']
            complete_speech.append(scene['Narration'])
            walk_words += len(scene['Narration'].split())
            walk_master += f"### {scene['title']}\n\n[Clean teleprompter take]({path})\n\n"
            for field in ['Show', 'Narration', 'Overlay', 'Verify', 'Capture dependency']:
                walk_master += f"**{field}:**\n\n{scene[field]}\n\n"
            safe = lambda value: value.replace('\n', ' ').replace('|', '/')
            capture += f"| {take} | [{row['title']}]({row['path']}) | {safe(scene['Capture dependency'])} | {safe(scene['Verify'])} |\n"
        result[f'teleprompter/walkthrough/{lid}.txt'] = '\n\n'.join(complete_speech)
    result['WALKTHROUGH-SCRIPTS.md'] = walk_master
    result['WALKTHROUGH-CAPTURE-DEPENDENCIES.md'] = capture
    rev = json.loads((root/'production/stepwise-revision.json').read_text(encoding='utf-8'))
    original_main = sum(rev['baseline_spoken_words'][by[x]['path']] for x in core)
    original_extra = sum(rev['baseline_spoken_words'][by[x]['path']] for x in advanced)
    main = sum(by[x]['words'] for x in core); extra = sum(by[x]['words'] for x in advanced)
    stats = validate(rows, practical)
    change = abs(1-main/original_main)*100
    direction = 'shorter' if main <= original_main else 'longer'
    result['COURSE-METRICS.md'] = f'''# Filming manuscript lengths

25 main teaching scripts, eight conditional teaching scripts, ten separate app walkthroughs and one device walkthrough.

| Written speech | Before this revision | Revised |
|---|---:|---:|
| Main teaching | {original_main:,} words | {main:,} words |
| Conditional teaching | {original_extra:,} words | {extra:,} words |
| All teaching | {original_main+original_extra:,} words | {main+extra:,} words |

Main teaching is {change:.1f}% {direction} than the September 10 starting manuscript. At an illustrative 140 words/minute it is about {main/140:.0f} minutes; conditional teaching adds about {extra/140:.0f} minutes when all branches apply. Separate walkthrough speech is {walk_words:,} words across {stats['walkthrough_chapters']} chapter takes. Editing directions and {stats['teaching_overlays']} teaching overlays are excluded from spoken counts.

These are manuscript estimates, not a published runtime promise. App use, pauses, recording delivery and outside implementation add time. Completion is the member's usable plan and decisions, not the lesson count or a particular simulation percentage.
'''
    return result
