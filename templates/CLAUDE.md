# &lt;EXAM_NAME&gt;, session instructions

This file specialises the master `claude-exam-prep/CLAUDE.md` rules to this specific exam. The master rules always apply; overrides below win only where they conflict. If you are opening Claude Code here for the first time, fill in the placeholder blocks before you start Phase 1 (reconnaissance).

## Context

- Student: &lt;STUDENT_NAME&gt; (&lt;STUDENT_ID&gt;).
- Exam: &lt;EXAM_TITLE&gt; on &lt;EXAM_DATE&gt;, &lt;DURATION&gt;, &lt;TOTAL_MARKS&gt; marks.
- Split: &lt;PROF1_MARKS&gt; marks for Professor &lt;PROF1_NAME&gt;, &lt;PROF2_MARKS&gt; marks for Professor &lt;PROF2_NAME&gt;.
- Syllabus scope: &lt;pre-midsem / post-midsem / full&gt;.
- Sources available in `raw/`: list here after Phase 1.
- Prior prep: how much the student has already studied.

## Grading model per professor

Claude adapts the style of each professor's cheat sheet and module answers to the professor's grading model. Fill in one bullet per professor.

- **&lt;PROF1_NAME&gt;** grades as a &lt;volume-grader / precision-grader&gt; (evidence: &lt;past-paper patterns, professor's statements, student's own reports&gt;).
- **&lt;PROF2_NAME&gt;** grades as a &lt;volume-grader / precision-grader&gt; (evidence: &lt;...&gt;).

See `../../docs/prof_grading_modes.md` for definitions.

## Exam evidence map

List every piece of evidence that tells us what will be on the paper. This becomes the priority map for the tracker.

- Syllabus announcement (email, portal post): &lt;location in raw/&gt;.
- Class test / quiz questions: &lt;filename&gt; contains &lt;N&gt; questions, topics: &lt;list&gt;.
- Submitted homeworks: &lt;filenames&gt;, topics: &lt;list&gt;.
- Past papers: &lt;years&gt;, recurring themes: &lt;list&gt;.
- Lab manuals: &lt;filenames&gt;.

High-probability items get 🔴, moderate 🟡, revision-only 🟢.

## Directory layout (already created by setup_exam.py)

```
exams/<EXAM_NAME>/
├── CLAUDE.md                 this file
├── README.md                 one-paragraph description
├── raw/                      source material lives here
├── pdf/                      CLAUDE.pdf and master summary PDFs
├── Professor1_<CODE>/        (create after Phase 1)
│   ├── lectures/
│   ├── homework/
│   ├── datasheets/
│   ├── question_papers/
│   └── class_test/
├── Professor2_<CODE>/        (same)
└── _prep_notes/
    ├── code/
    │   ├── md_to_pdf.py       copied from ../../../scripts/
    │   ├── figure_helpers.py  copied from ../../../scripts/
    │   └── gen_<module>_figs.py  one per module
    ├── images/
    ├── pdf/
    ├── <module>.md            per-module notes
    └── <prof>_Cheatsheet.md   per-professor cheat sheet
```

## Module tracker

Fill in after Phase 1 and Phase 2. One module per major topic. Under each module, list every submodule explicitly, and rank by priority using 🔴 / 🟡 / 🟢.

### Professor &lt;PROF1_NAME&gt; (&lt;PROF1_MARKS&gt; marks, approx &lt;hours&gt; h)

- [ ] **P1. &lt;MODULE NAME&gt;** 🔴 HIGH &lt;reason, e.g. CT direct hits confirmed&gt;. Budget &lt;N&gt; h.
  - P1.1 &lt;submodule, one line&gt;
  - P1.2 &lt;submodule, one line&gt;
  - ...

- [ ] **P2. &lt;MODULE NAME&gt;** 🔴 HIGH. Budget &lt;N&gt; h.
  - ...

### Professor &lt;PROF2_NAME&gt; (&lt;PROF2_MARKS&gt; marks, approx &lt;hours&gt; h)

- [ ] **Q1. &lt;MODULE NAME&gt;** 🔴 HIGH. Budget &lt;N&gt; h.
  - Q1.1 ...

## Diagram stack plan

Paste the diagram-library mapping here after Phase 3. Every module's figures are listed with the chosen library. Follow `../../docs/diagram_conventions.md` for palette and spacing.

| Module | Figure | Library |
|---|---|---|
| P1 | &lt;figure name&gt; | matplotlib / schemdraw / graphviz |
| ... | ... | ... |

## Recommended order

Teach in priority order. Highest-impact module first. Save 🟢 modules for the last hour.

## Build commands

```bash
# regenerate figures for a single module
python3 _prep_notes/code/gen_P1_figs.py

# build a single module PDF
python3 _prep_notes/code/md_to_pdf.py _prep_notes/P1_&lt;module&gt;.md

# build this CLAUDE.md into a readable plan PDF
python3 _prep_notes/code/md_to_pdf.py CLAUDE.md  # writes to pdf/CLAUDE.pdf

# audit coverage from the repo root
python3 ../../scripts/audit.py .
```

## Source of truth

- **CLAUDE.md** (this file): session controller, rules, tracker, diagram stack.
- **`_prep_notes/<module>.md`**: canonical teaching notes per module with embedded images.
- **`_prep_notes/pdf/<module>.pdf`**: rendered PDF of each module.
- **`_prep_notes/images/*.png`**: every rendered figure.
- **`_prep_notes/code/gen_<module>_figs.py`**: per-module figure generator.

Everything else in `raw/` or under the prof folders is evidence, not teaching substrate.
