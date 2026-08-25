#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "MASTER-ADVANCED.md"
OUT = ROOT / "ADVANCED-DICTATION-AUDIT.md"

FLAG_RE = re.compile(
    r"(?i)(🔴|❓|⚠|HOLD|BLOCKER|TODO|DECISION NEEDED|NOT YET|PLACEHOLDER|LIVE BUG|DO NOT FILM|NOT SCHEDULED)"
)
STALE_PATTERNS = {
    "old onboarding flow": re.compile(r"(?i)onboarding (wizard|flow|gave you a plan|entered|built your baseline)"),
    "premature confidence": re.compile(r"(?i)(first confidence read|confidence ring.*module 1|baseline you just entered)"),
    "retired module": re.compile(r"(?i)module 10\b"),
    "old baseline claim": re.compile(r"(?i)onboarding gave you a plan"),
    "unapplied-plan ambiguity": re.compile(r"(?i)(preview|sandbox).{0,100}(plan has changed|is your plan)"),
}


def run(command: list[str]) -> tuple[int, str]:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def clean_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def lesson_sections(text: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"(?m)^## (A\d+\.\d+) ([^\n]+)$", text))
    lessons: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        lessons.append({
            "num": match.group(1),
            "title": clean_title(match.group(2)),
            "body": text[match.start():end],
        })
    return lessons


def one(pattern: str) -> Path | None:
    matches = sorted(ROOT.glob(pattern))
    return matches[0] if len(matches) == 1 else None


def provenance(text: str) -> str:
    head = text[:1200]
    if "AUSTIN DICTATION" in head:
        return "Austin dictation"
    if "SPOKEN-PROSE VERSION" in head:
        return "spoken-prose calibrated"
    if head.startswith("TELEPROMPTER SCRIPT"):
        return "generated teleprompter"
    return "unlabelled"


def extract_gate(body: str) -> str:
    for line in body.splitlines()[:35]:
        if re.search(r"(?i)\bgate\b|watch this if|only if", line):
            return re.sub(r"^[>*\s-]+", "", line).strip()
    return "MISSING"


def title_from_script(text: str) -> str:
    for line in text.splitlines()[:8]:
        m = re.match(r"A\d+\.\d+\s+(.+)", line.strip())
        if m:
            return clean_title(m.group(1))
    return ""


def flags_for(path: Path, text: str) -> list[str]:
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        if FLAG_RE.search(line):
            found.append(f"`{path.relative_to(ROOT)}:{number}` — {line.strip()}")
    return found


def main() -> None:
    master_text = MASTER.read_text(encoding="utf-8")
    lessons = lesson_sections(master_text)
    rows = []
    blockers: list[str] = []
    flags: list[str] = []
    stale: list[str] = []
    app_refs: list[str] = []
    total_words = 0

    for lesson in lessons:
        num = lesson["num"]
        prefix = num.replace(".", "-")
        script = one(f"scripts/advanced/{prefix}_*.md")
        lesson_text = one(f"lesson-text/advanced/{prefix}_*.md")
        module = one(f"modules/advanced/{prefix}_*.md")
        script_text = script.read_text(encoding="utf-8") if script else ""
        lesson_words = len(script_text.split('=' * 60, 1)[-1].split()) if script else 0
        total_words += lesson_words
        prov = provenance(script_text) if script else "MISSING"
        gate = extract_gate(lesson["body"])
        script_title = title_from_script(script_text) if script else ""
        title_ok = bool(script_title and clean_title(script_title) == lesson["title"])
        homework = bool(re.search(r"(?im)^###? HOMEWORK\b|^== HOMEWORK ==|^### Your decision", script_text))
        layers = [
            "M" if lesson["body"] else "-",
            "S" if script else "-",
            "T" if lesson_text else "-",
            "G" if module else "-",
        ]

        lesson_flags: list[str] = []
        for path, text in [
            (MASTER, lesson["body"]),
            *(([(script, script_text)] if script else [])),
            *(([(lesson_text, lesson_text.read_text(encoding="utf-8"))] if lesson_text else [])),
            *(([(module, module.read_text(encoding="utf-8"))] if module else [])),
        ]:
            lesson_flags.extend(flags_for(path, text))
            for label, pattern in STALE_PATTERNS.items():
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    stale.append(f"**{num} · {label}** — `{path.relative_to(ROOT)}:{line}` — `{match.group(0)}`")

        if any(token in (lesson["body"] + script_text).lower() for token in (
            "plan →", "strategy →", "settings →", "protect →", "scenarios →", "cash flow →", "dashboard →"
        )):
            app_refs.append(f"{num} · {lesson['title']}")

        reasons = []
        if not all((script, lesson_text, module)):
            reasons.append("missing live layer")
        if gate == "MISSING":
            reasons.append("missing gate")
        if not title_ok:
            reasons.append("master/script title drift")
        if not homework:
            reasons.append("no clear homework/finish line in script")
        if lesson_flags:
            reasons.append(f"{len(lesson_flags)} visible flag(s)")
            flags.extend(lesson_flags)
        if prov in {"generated teleprompter", "unlabelled", "MISSING"}:
            reasons.append(f"provenance: {prov}")
        if reasons:
            blockers.append(f"- **{num} · {lesson['title']}** — " + "; ".join(reasons))

        rows.append(
            f"| {num} | {lesson['title']} | {prov} | {lesson_words:,} | {'/'.join(layers)} | "
            f"{'yes' if title_ok else 'NO'} | {'yes' if homework else 'NO'} | {gate.replace('|', '/')} |"
        )

    authority = (ROOT / "AUTHORITY-FLAGS.md").read_text(encoding="utf-8")
    advanced_authority = []
    for number, line in enumerate(authority.splitlines(), 1):
        if re.search(r"\bA\d+\.\d+\b", line):
            advanced_authority.append(f"- `AUTHORITY-FLAGS.md:{number}` — {line.strip()}")

    production = (ROOT / "PRODUCTION-CHECKLIST.md").read_text(encoding="utf-8")
    production_lines = []
    for number, line in enumerate(production.splitlines(), 1):
        if re.search(r"(?i)advanced|A\d+\.\d+|publication blocker|not scheduled", line):
            production_lines.append(f"- `PRODUCTION-CHECKLIST.md:{number}` — {line.strip()}")

    checks = []
    commands = [
        ("Cross-references", ["python3", "tools/check-crossrefs.py"]),
        ("Layer parity", ["python3", "tools/check-layer-parity.py"]),
        ("Slop scan", ["python3", "tools/slop-scan.py", "--all"]),
        ("Visual coverage", ["python3", "tools/check-visuals.py"]),
        ("Metrics", ["python3", "tools/course-metrics.py", "--check"]),
    ]
    for label, command in commands:
        code, output = run(command)
        checks.append((label, code, output[-6000:]))

    report = [
        "# Advanced Library + dictation readiness audit",
        "",
        "Generated from the merged `main` course before the finalization pass.",
        "",
        "## Bottom line",
        "",
        f"- Advanced lessons found: **{len(lessons)}**.",
        f"- Advanced teleprompter words: **{total_words:,}** (~{total_words / 155:.0f} minutes).",
        f"- Lessons needing an editorial or production pass under this audit: **{len(blockers)}**.",
        f"- Stale core-lifecycle phrases found in Advanced live layers: **{len(stale)}**.",
        "",
        "## Lesson inventory",
        "",
        "`M/S/T/G` = master / script / lesson-text / generated module.",
        "",
        "| # | Lesson | Script provenance | Words | Layers | Title match | Finish line | Gate |",
        "|---|---|---:|---:|---|---|---|---|",
        *rows,
        "",
        "## Items that prevent a clean final-dictation claim",
        "",
        *(blockers or ["None."]),
        "",
        "## Visible flags inside Advanced live content",
        "",
        *(flags or ["None."]),
        "",
        "## Advanced authority flags",
        "",
        *(advanced_authority or ["None."]),
        "",
        "## Current production-checklist references",
        "",
        *(production_lines or ["None."]),
        "",
        "## Stale lifecycle wording",
        "",
        *(stale or ["None."]),
        "",
        "## Lessons with app click paths or UI-dependent wording",
        "",
        *(f"- {item}" for item in app_refs),
        "",
        "## Repository gates",
        "",
    ]
    for label, code, output in checks:
        report += [f"### {'PASS' if code == 0 else 'FAIL'} · {label}", "", "```text", output or "(no output)", "```", ""]

    OUT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
