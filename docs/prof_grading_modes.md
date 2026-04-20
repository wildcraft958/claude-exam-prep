# Professor grading modes, volume vs precision

Two distinct grading styles emerged during the prototype run and have held up across follow-ups. Every professor in every exam falls somewhere on the spectrum between them, usually close to one of the two poles. Identifying which one a professor prefers, early in Phase 1, is worth 10 to 15 percent of the final mark compared to writing a neutral answer.

## Volume grader

Marks scale with the amount of correct content on the page. A neat, tightly-optimised answer leaves marks on the table. A long, diagram-heavy, citation-rich answer collects them.

**Signals that a professor grades by volume.**

- Past-paper solutions from the professor themselves run to multiple pages per 10-mark question.
- The professor explicitly says "write as much as you remember" or "show me what you know".
- The student's peers with higher marks consistently wrote longer answers.
- The professor gives partial credit for any reasonable-looking content adjacent to the question.
- Homework assignments weight long essay-style answers.

**How to write for a volume grader.**

- Name the physical principle at the start of every answer, in words, before any formula.
- Include the derivation in full, even if the question only asks for the result.
- Draw at least one figure per 10-mark question. Two figures for 20-mark questions.
- Explain every symbol on its own line (`F = Faraday constant = 96485 C/mol`).
- Quote numerical ranges (`9 mm at 50 Hz, 66 µm at 1 MHz, 2 µm at 1 GHz`) rather than saying "falls with frequency".
- Cite an international standard at the end of every answer (CISPR 22, FCC Part 15, IEC 61000, IEEE 802.11, OASIS MQTT, 3GPP TS).
- Cite an Indian regulation if applicable (Battery Waste Management Rules 2022, E-Waste Rules 2022, WPC spectrum allocation, BIS IS number).
- Append a "practical notes" paragraph: named ICs, typical component values, known failure modes.
- Append a "trade-offs / alternatives" paragraph when possible.
- Do not leave any sub-part blank; partial wrong beats blank.
- Time budget: 1 minute per mark is correct; do not finish early.

In the prototype run, Professor A fit the volume-grader profile exactly. The cheat sheet built for that paper averaged a full A4 side per 10-mark question and scored well above the cohort average.

## Precision grader

Marks scale with technical correctness and with clean, complete steps. Volume is not rewarded and can actually hurt if it introduces sloppy errors. Every step you write is expected to be correct.

**Signals that a professor grades by precision.**

- Past-paper solutions are tight, one to two tight paragraphs per 10-mark question, with every step justified.
- The professor explicitly says "show your working" or "step by step".
- Numerical errors and off-by-one mistakes are penalised heavily.
- Past students report that "the marks are in the steps, not the story".
- The professor uses formal tuples and definitions in lecture.

**How to write for a precision grader.**

- Start every answer with the formal definition: FSM 5-tuple, TTM 6-tuple, task model triple, LTL formula.
- Show every iteration of any fixed-point computation. For response-time analysis, write `R_i(0), R_i(1), R_i(2), ...` until convergence.
- Draw each FSM separately, then the composed one, then the reachability graph. Three figures, not one crammed one.
- Label every edge with its event name, guard, and time bounds.
- Write LTL formulas exactly. `[]` always, `<>` eventually, `U` strong until, `W` weak until, `<` precedence.
- Classify a property (invariance, liveness, or real-time response) before applying the decision procedure.
- End every answer with a one-line conclusion: "Property holds because every reachable node satisfies it"; "Task set is RM-schedulable because U = 0.75 ≤ 0.779".
- Time-box strictly. Do not pad.
- No hand-waving. Every claim must be backed by a formula, an iteration, or a reachability check.

In the same prototype run, Professor B fit the precision-grader profile. The cheat sheet built for that paper was about a third the length of the volume-grader one but carried the same weight of marks.

## How to identify the grading mode early

In Phase 1 (reconnaissance), ask the student directly: "In past papers from this professor, which kind of answer scored higher: longer-with-more-content, or tighter-and-more-correct?" If the student has a past solved paper from the professor, read it and count the average length per mark.

If the student is unsure, default to writing the first module as precision-graded (cheaper error) and after the first draft ask the student to show it to the professor or a TA. Adjust from their feedback.

## Mixed graders

Some professors mix modes: volume for essay questions, precision for numerical. The prototype run was the clean case where a single paper was split between two graders at opposite ends of the spectrum. In a mixed-grader case, segment the answer by question type: essay answers in volume style, numerical answers in precision style, even in the same paper.
