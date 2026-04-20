"""Scaffold a new exam directory under ``exams/<name>/``.

Usage
-----
    python3 scripts/setup_exam.py --name "DSP_EndSem_2026"

What it does
------------
1. Creates ``exams/<name>/`` with the standard subfolders:
       raw/ pdf/ _prep_notes/{code,images,pdf}
2. Copies the per-exam templates in place:
       CLAUDE.md  (the tracker Claude will fill in)
       README.md  (one-paragraph exam description)
3. Copies ``scripts/md_to_pdf.py`` and ``scripts/figure_helpers.py`` into
   ``_prep_notes/code/`` so they can be run from inside the exam dir.
4. Leaves template slots unfilled. When you open Claude Code inside the
   new exam dir, Claude will ask you the handful of questions needed to
   fill in the tracker.

The script does NOT populate CLAUDE.md with placeholder content; Claude
fills it during Phase 1 (reconnaissance) based on your raw/ material.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent  # claude-exam-prep/
TEMPLATES = REPO / "templates"
EXAMS = REPO / "exams"
SCRIPTS = REPO / "scripts"


def make_subdirs(target: Path) -> None:
    subdirs = [
        "raw",
        "pdf",
        "_prep_notes",
        "_prep_notes/code",
        "_prep_notes/images",
        "_prep_notes/pdf",
    ]
    for sub in subdirs:
        (target / sub).mkdir(parents=True, exist_ok=True)


def copy_templates(target: Path) -> None:
    mapping = {
        TEMPLATES / "CLAUDE.md": target / "CLAUDE.md",
        TEMPLATES / "README.md": target / "README.md",
    }
    for src, dst in mapping.items():
        if not dst.exists():
            shutil.copyfile(src, dst)

    # copy the reusable helpers into _prep_notes/code/ so the generated
    # figure scripts and module markdowns can reach them with a short path
    for name in ("md_to_pdf.py", "figure_helpers.py"):
        src = SCRIPTS / name
        dst = target / "_prep_notes" / "code" / name
        if not dst.exists():
            shutil.copyfile(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True,
                        help="exam directory name, e.g. DSP_EndSem_2026")
    parser.add_argument("--overwrite", action="store_true",
                        help="allow reinitialising an existing exam dir")
    args = parser.parse_args()

    target = EXAMS / args.name
    if target.exists() and not args.overwrite:
        print(f"[error] {target} already exists. Use --overwrite to reinitialise.")
        return 1

    target.mkdir(parents=True, exist_ok=True)
    make_subdirs(target)
    copy_templates(target)

    rel = target.relative_to(REPO)
    print(f"\nScaffolded exam directory at  {rel}/\n")
    print("Next steps")
    print("----------")
    print(f"1. Move source PDFs, images, past papers into  {rel}/raw/")
    print(f"2. cd {rel}")
    print(f"3. Open Claude Code.  Claude will read ../../CLAUDE.md (master rules)")
    print(f"   and ./CLAUDE.md (this exam).  It will ask a few questions to fill")
    print(f"   in the tracker, then start Phase 1 (reconnaissance).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
