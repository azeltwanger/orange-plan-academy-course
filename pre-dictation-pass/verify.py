#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "pre-dictation-pass-manifest.json"
REPORT = ROOT / "PRE-DICTATION-PLAIN-DRAFT-PASS.md"


def run(label: str, command: list[str], results: list[tuple[str, int, str]]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    results.append((label, proc.returncode, output))
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    converted = manifest["converted"]
    protected = manifest["protected"]

    if len(converted) < 25:
        raise RuntimeError(f"Expected a course-wide pass; only {len(converted)} scripts were converted")
    if len(protected) < 4:
        raise RuntimeError(f"Expected at least four protected dictation scripts; found {len(protected)}")

    for item in converted:
        path = ROOT / item["path"]
        text = path.read_text(encoding="utf-8")
        header = text.split("=" * 60, 1)[0]
        body = text.split("=" * 60, 1)[1]
        if "PRE-DICTATION PLAIN DRAFT" not in header:
            raise RuntimeError(f"Missing pre-dictation provenance: {item['path']}")
        if "DICTATION NOTE:" not in header:
            raise RuntimeError(f"Missing dictation note: {item['path']}")
        for heading in (
            "== YOUR DECISION ==",
            "== PUT IT IN ORANGE PLAN ==",
            "== YOU ARE DONE WHEN ==",
        ):
            if heading in body:
                raise RuntimeError(f"Generated closing structure remains in {item['path']}: {heading}")
        if not re.search(r"\[\[(?:OPEN|BEAT|CLOSE|HOMEWORK)", body):
            raise RuntimeError(f"No plain speaking cues found in {item['path']}")

    one_three = (ROOT / "scripts/01-3_read-your-retirement-date-and-confidence.md").read_text(encoding="utf-8")
    required = [
        "The technical word for this is deterministic",
        "It is not an average of 1,000 different market outcomes",
        "finds the earliest age where that projection can keep funding",
        "82% confidence",
        "Then watch the Foundation walkthrough below this video",
    ]
    for phrase in required:
        if phrase not in one_three:
            raise RuntimeError(f"1.3 manual rebuild is missing: {phrase}")
    for retired in (
        "one average projection",
        "Treat it as the first draft of the headline",
        "The date tells you when. The confidence number tells you how sturdy",
    ):
        if retired in one_three:
            raise RuntimeError(f"1.3 still contains retired generated copy: {retired}")

    active_text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in [ROOT / "MASTER-COURSE.md", ROOT / "lesson-text/01-3_read-your-retirement-date-and-confidence.md", ROOT / "scripts/01-3_read-your-retirement-date-and-confidence.md"]
        if p.exists()
    )
    if "one average projection" in active_text:
        raise RuntimeError("Stale onboarding calculation language remains in an active 1.3 layer")

    if not (ROOT / "PRE-DICTATION-ORDER.md").exists():
        raise RuntimeError("PRE-DICTATION-ORDER.md was not generated")
    if not (ROOT / "archive/pre-dictation-copywriting-scripts-2026-08-26/README.md").exists():
        raise RuntimeError("Original generated scripts were not archived")

    results: list[tuple[str, int, str]] = []
    checks = [
        ("Cross-references", ["python3", "tools/check-crossrefs.py"]),
        ("Layer parity", ["python3", "tools/check-layer-parity.py"]),
        ("Voice/slop scan", ["python3", "tools/slop-scan.py", "--all"]),
        ("Visual coverage", ["python3", "tools/check-visuals.py"]),
        ("Metrics freshness", ["python3", "tools/course-metrics.py", "--check"]),
        ("Layer-parity mutation harness", ["python3", "tools/test-layer-parity-mutations.py"]),
    ]
    for label, command in checks:
        run(label, command, results)

    report = REPORT.read_text(encoding="utf-8").rstrip()
    lines = [report, "", "## Final verification", ""]
    for label, code, output in results:
        lines.extend([
            f"### {'PASS' if code == 0 else 'FAIL'} · {label}",
            "",
            "```text",
            output[-6000:] or "(no output)",
            "```",
            "",
        ])
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"plain-draft verification passed for {len(converted)} converted scripts")


if __name__ == "__main__":
    main()
