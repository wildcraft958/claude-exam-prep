# End-to-end workflow

The repo is designed to run from first dump of source PDFs to a bound set of study PDFs in one overnight session.

## 0. Environment setup (once)

```bash
git clone <this-repo> claude-exam-prep
cd claude-exam-prep
python3 -m pip install -r requirements.txt

# system Graphviz for FSM and topology diagrams
sudo apt-get install graphviz      # Debian / Ubuntu
# or: brew install graphviz         # macOS
```

Verify:

```bash
python3 -c "import matplotlib, schemdraw, graphviz, networkx, weasyprint; print('ok')"
which dot
```

## 1. Scaffold a new exam

```bash
python3 scripts/setup_exam.py --name "EE_EndSem_2026"
```

This creates `exams/EE_EndSem_2026/` with the standard subfolders and copies the templates into place.

## 2. Move source material

Dump every source PDF, PPT, image, and past paper into the new exam's `raw/` folder. Keep file names meaningful. If you have a message from the professor listing the syllabus, save it as `raw/syllabus.txt` or similar.

```bash
cp -r /path/to/source/* exams/EE_EndSem_2026/raw/
```

## 3. Open Claude Code inside the exam

```bash
cd exams/EE_EndSem_2026
claude
```

Claude will read the master `claude-exam-prep/CLAUDE.md` and this exam's `CLAUDE.md`. It asks a few short questions to fill in the tracker: student name and roll, exam date and duration, professors and marks split, grading model per professor. Answer them once; after that Claude owns the workflow.

## 4. Phase 1, reconnaissance

Claude launches parallel Explore agents to summarise the source pile. Outcome: a short paragraph per source category (lectures, homework, class tests, past papers, lab manuals). At the end of this phase you know what is on the paper.

## 5. Phase 2, build the module tracker

Claude writes the full tracker into the exam's `CLAUDE.md`. Every module and every submodule listed explicitly. Every homework question and class-test question mapped to a submodule. Priorities 🔴 / 🟡 / 🟢 per submodule. You review and approve.

## 6. Phase 3, diagram stack plan

Claude lists the figures it plans to generate per module, picks the right library for each (matplotlib for plots, schemdraw for circuits, graphviz for FSMs and topology, networkx for graph computation). The plan is appended to `CLAUDE.md`.

## 7. Phase 4, module writing

For each module in priority order:

1. `_prep_notes/code/gen_<module>_figs.py` written, run, figures rendered to `_prep_notes/images/`.
2. `_prep_notes/<module>.md` written in natural prose with embedded figures.
3. `_prep_notes/code/md_to_pdf.py _prep_notes/<module>.md` builds the module PDF into `_prep_notes/pdf/`.
4. Claude summarises in chat with one paragraph and points you at the PDF.

Repeat until every module is done.

## 8. Phase 5, cheat sheets per professor

Two PDFs built, one per professor, each a full exam-answer key. The style is tuned to the professor's grading model (volume grader vs precision grader, see `prof_grading_modes.md`).

## 9. Phase 6, audit

```bash
python3 /path/to/claude-exam-prep/scripts/audit.py .
```

This checks submodule coverage, em-dash contamination, and PDF presence. Any gap is reported; patch and rebuild.

## 10. Phase 7, revision mode

In the last hour before the exam, ask Claude to produce a single-page memory-trigger cheat sheet per professor. No new content; a compression of what exists.

## Common commands while working

```bash
# rebuild a single module PDF
python3 _prep_notes/code/md_to_pdf.py _prep_notes/R1_Batteries.md

# rebuild every module PDF
python3 _prep_notes/code/md_to_pdf.py _prep_notes/*.md

# rerun figures for one module
python3 _prep_notes/code/gen_R1_figs.py

# rebuild the tracker CLAUDE.md as a PDF you can scan
python3 _prep_notes/code/md_to_pdf.py CLAUDE.md

# audit from the repo root
python3 /path/to/claude-exam-prep/scripts/audit.py exams/EE_EndSem_2026/
```
