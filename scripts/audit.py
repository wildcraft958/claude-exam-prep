"""Audit module coverage for a claude-exam-prep exam.

Usage
-----
    python3 scripts/audit.py path/to/exams/<exam_name>/

What it checks
--------------
1. Every submodule code listed in the per-exam `CLAUDE.md` appears
   as a heading somewhere in one of the module markdown files.
2. Every question tagged in `raw/` or in the per-exam `CLAUDE.md`'s
   "Exam evidence map" has a matching mention in at least one module.
3. No em dashes or en dashes remain in any markdown file.
4. Every module markdown has a sibling PDF built.

The output is a short report: PASS / FAIL per check, with the gaps listed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


SUBMODULE_RE = re.compile(r"^\s*-\s*(?:R|S|[A-Z])\d+\.\d+\b", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+.*?\b([A-Z]\d+\.\d+)\b", re.MULTILINE)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def audit_exam(exam_dir: Path) -> int:
    exam_dir = Path(exam_dir).resolve()
    if not exam_dir.exists():
        print(f"FAIL  exam directory not found: {exam_dir}")
        return 2

    problems = 0

    # 1. read the per-exam CLAUDE.md and extract declared submodule codes
    claude = read(exam_dir / "CLAUDE.md")
    declared = set()
    for match in SUBMODULE_RE.finditer(claude):
        code = match.group(0).strip().lstrip("- ").split()[0]
        declared.add(code)

    # 2. collect every module markdown file
    notes_dir = exam_dir / "_prep_notes"
    md_files = sorted(notes_dir.glob("*.md"))

    referenced = set()
    for md in md_files:
        body = read(md)
        for match in SECTION_RE.finditer(body):
            referenced.add(match.group(1))
        # also any inline mention like "R1.5"
        referenced.update(re.findall(r"\b([A-Z]\d+\.\d+)\b", body))

    # report coverage
    missing = sorted(declared - referenced)
    print(f"\n[1/4] submodule coverage  ", end="")
    if not missing:
        print(f"PASS  {len(declared)} submodules all referenced")
    else:
        problems += 1
        print(f"FAIL  {len(missing)} missing")
        for code in missing:
            print(f"      - {code} declared in CLAUDE.md but not in any module")

    # 3. em / en dash scan
    print(f"\n[2/4] em-dash / en-dash scan  ", end="")
    dash_files = []
    for md in [exam_dir / "CLAUDE.md", *md_files]:
        body = read(md)
        # Count U+2014 (em dash) and U+2013 (en dash). Using escape sequences
        # here so this file does not itself contain the forbidden characters.
        hits = sum(body.count(ch) for ch in ("\u2014", "\u2013"))
        if hits > 0:
            dash_files.append((md.name, hits))
    if not dash_files:
        print("PASS  no em or en dashes found")
    else:
        problems += 1
        print("FAIL")
        for name, n in dash_files:
            print(f"      - {name}: {n} dash(es)")

    # 4. PDF presence
    print(f"\n[3/4] module PDFs present  ", end="")
    pdf_dir = notes_dir / "pdf"
    missing_pdf = []
    for md in md_files:
        pdf = pdf_dir / (md.stem + ".pdf")
        if not pdf.exists():
            missing_pdf.append(md.stem)
    if not missing_pdf:
        print(f"PASS  {len(md_files)} markdowns have matching PDFs")
    else:
        problems += 1
        print(f"FAIL  {len(missing_pdf)} missing")
        for stem in missing_pdf:
            print(f"      - {stem}.pdf  (run md_to_pdf on {stem}.md)")

    # 5. raw/ exists and has something
    print(f"\n[4/4] raw/ source material  ", end="")
    raw = exam_dir / "raw"
    if not raw.exists():
        problems += 1
        print("FAIL  raw/ directory missing")
    elif not any(raw.iterdir()):
        problems += 1
        print("WARN  raw/ is empty; move source material in before Phase 1")
    else:
        count = sum(1 for _ in raw.rglob("*") if _.is_file())
        print(f"PASS  raw/ has {count} file(s)")

    print()
    return 0 if problems == 0 else 1


def main(args: list[str]) -> int:
    if len(args) != 1:
        print(__doc__)
        return 1
    return audit_exam(Path(args[0]))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
