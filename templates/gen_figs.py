"""Generate figures for Module MODULE_CODE.

Conventions
-----------
- Palette and helpers imported from `figure_helpers.py`.
- Output written to the exam's `_prep_notes/images/` directory.
- Figure names follow  MODULE_CODE_descriptive_name.png .
- No em dashes in titles or labels.

Run from the exam directory root:

    python3 _prep_notes/code/gen_MODULE_CODE_figs.py
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mp

# helpers live next to this script inside _prep_notes/code/
import sys
sys.path.insert(0, str(Path(__file__).parent))
from figure_helpers import (
    POS, NEG, ELC, TXT, ARR, MUTED,
    setup, arrow, box, save, images_dir,
)

OUT = images_dir(__file__)

# Replace "MODULE_CODE" with the actual short code for this module
# (for example "R1", "S2", "P3") before running.


def fig_first():
    """Figure 1. Short description."""
    fig, ax = setup((10, 6), title="Replace with your title (no em dashes)",
                    xlim=(0, 12), ylim=(0, 8))
    # Example content to show usage; replace with your own diagram.
    box(ax, 1, 3, 2, 2, fc=POS, label="anode")
    box(ax, 8, 3, 2, 2, fc=NEG, label="cathode")
    arrow(ax, 3, 4, 8, 4, label="electron flow")
    save(fig, OUT / "MODULE_CODE_first_figure.png")


def fig_second():
    """Figure 2. Short description."""
    fig, ax = plt.subplots(figsize=(8, 5), dpi=140, facecolor="white")
    x = np.linspace(0, 10, 200)
    ax.plot(x, np.sin(x), color=POS, lw=2)
    ax.set_xlabel("time", color=TXT)
    ax.set_ylabel("signal", color=TXT)
    ax.set_title("Replace with your title", color=TXT, weight="bold")
    ax.grid(True, linestyle=":", alpha=0.4)
    save(fig, OUT / "MODULE_CODE_second_figure.png")


if __name__ == "__main__":
    fig_first()
    fig_second()
    print(f"figures written to {OUT}")
