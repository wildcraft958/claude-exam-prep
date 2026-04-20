# Diagram conventions

All figures in a claude-exam-prep exam should look like they came from one author. The conventions below are the ones that proved durable during the prototype run. Change them only with deliberate reason.

## Palette

Six colours, used consistently across every figure, every module, every professor.

| Role | Hex | Matplotlib import |
|---|---|---|
| Positive / hot / aggressor / emphasis | `#c0392b` | `POS` |
| Negative / cold / victim / secondary | `#2980b9` | `NEG` |
| Electrolyte / warning / highlight | `#f1c40f` | `ELC` |
| Default text / ink | `#2c3e50` | `TXT` |
| Arrows / "good" / positive reinforcement | `#27ae60` | `ARR` |
| Muted / de-emphasis | `#7f8c8d` | `MUTED` |

These colours also match the `md_to_pdf.py` stylesheet, so headings in the PDF and shapes in the figures share a visual language. Import them via `from figure_helpers import POS, NEG, ELC, TXT, ARR, MUTED`.

## Figure sizing

- Default `figsize=(10, 6)`, `dpi=140`, `facecolor="white"`.
- Multi-panel figures scale proportionally: 8 units of width per panel.
- For full-page diagrams (cutaways, architectures), `(12, 8)` is acceptable.
- Never use `dpi=72`; it looks bad in print.

## Spacing

- No label overlaps anywhere. Leave at least 0.3 axis units of breathing room around every label.
- Titles bold, 12 to 14 pt.
- Arrow labels outside the boxes, offset at least 0.2 axis units.
- Legend whenever colour coding is used.
- `bbox_inches='tight'` on every savefig so labels near edges are not clipped.

## Library per diagram type

| Diagram | Library | Reason |
|---|---|---|
| Plot, waveform, curve | `matplotlib` | Native support, good control. |
| Gantt chart, timeline | `matplotlib` | Patches API gives rectangles for tasks. |
| Custom cross section (battery cutaway, PCB stackup, smartphone triangle) | `matplotlib.patches` | Flexible geometry with `Rectangle`, `FancyBboxPatch`, `Polygon`, `Circle`. |
| Circuit schematic (RLGC, CMOS, SPI, I2C) | `schemdraw` | Designed for schematics, clean output. |
| Flow diagram (BMS, pipeline, signal chain) | `schemdraw.flow` | Built-in flow elements. |
| FSM, state machine | `graphviz` (Digraph) | Automatic layout, clean nodes. |
| Reachability graph, state space | `graphviz` | Same. |
| Graph computation (SCC, condensation) | `networkx` + `graphviz` | Compute with networkx, render with graphviz. |
| Topology (MQTT, LoRa, IoT stack) | `graphviz` | Clean cloud-to-device layout. |
| UML activity / composite / state | `graphviz` | Same. |

## File names and output path

- Store PNGs under `<exam>/_prep_notes/images/`.
- Name each PNG `<module_code>_<descriptive_name>.png`, for example `R1_cell_anatomy.png`.
- Store generator scripts under `<exam>/_prep_notes/code/gen_<module>_figs.py`.

## No em dashes anywhere

Figures embed in PDFs that the student reads. Em dashes (code point U+2014) and en dashes (code point U+2013) are forbidden in titles, labels, annotations, and legends. Use commas, colons, semicolons, periods, parentheses, or plain hyphens. After generating, grep any embedded titles for `\u2014` and `\u2013` and replace.

## matplotlib MathText traps

`matplotlib` MathText is not full LaTeX. It knows `\pi`, `\mu`, `\omega`, `\sqrt`, `\sum`, but it does **not** know `\Box` or `\Diamond`. If you need "always" or "eventually" for LTL diagrams, write them as plain text `[]` and `<>`. Safer symbols: `\psi`, `\phi`, `\Gamma`, `\Delta` all work.

## Verify every figure

After generating, open the PNG (the Read tool can display images) and verify:

- Labels do not overlap any shape or each other.
- Every arrow has its label.
- Colours match the palette.
- No em dashes sneaked into the title.
