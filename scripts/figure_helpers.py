"""Reusable figure helpers for claude-exam-prep.

Import from a per-module generator:

    from claude_exam_prep.figure_helpers import (
        POS, NEG, ELC, TXT, ARR, MUTED,
        setup, arrow, box, save,
    )

Palette matches the one used during the prototype run. These colours also
match the `md_to_pdf.py` stylesheet, so figures and body text share a visual
language.
"""
from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mp


# Palette. Use these constants in every figure so the whole deck looks
# like it came from one author.
POS = "#c0392b"   # positive electrode, hot signal, aggressor, emphasis
NEG = "#2980b9"   # negative electrode, cold signal, victim, secondary
ELC = "#f1c40f"   # electrolyte, warning, highlight
TXT = "#2c3e50"   # default text, neutral ink
ARR = "#27ae60"   # arrows, positive reinforcement, "good"
MUTED = "#7f8c8d"  # muted text, de-emphasis


def setup(size=(10, 6), title: str | None = None, xlim=None, ylim=None,
          equal: bool = True):
    """Boilerplate for a matplotlib canvas.

    Returns (fig, ax). Caller draws shapes, saves via `save(fig, ...)`.
    """
    fig, ax = plt.subplots(figsize=size, dpi=140, facecolor="white")
    if equal:
        ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=13, color=TXT, pad=12, weight="bold")
    if xlim is not None:
        ax.set_xlim(*xlim)
    if ylim is not None:
        ax.set_ylim(*ylim)
    return fig, ax


def arrow(ax, x1, y1, x2, y2, color=ARR, lw: float = 1.8,
          label: str | None = None, label_pos=None, fontsize: int = 10):
    """Draw a solid -|> arrow from (x1,y1) to (x2,y2), optionally labelled."""
    ax.annotate(
        "",
        xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=16),
    )
    if label is not None:
        if label_pos is None:
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 + 0.4
        else:
            lx, ly = label_pos
        ax.text(lx, ly, label, color=color, fontsize=fontsize,
                ha="center", weight="bold")


def box(ax, x, y, w, h, fc=TXT, label: str = "", ec="black",
        tc="white", fs: int = 10, boxstyle: str = "round,pad=0.05", lw: float = 1.2):
    """Filled rounded rectangle with a centered label."""
    ax.add_patch(mp.FancyBboxPatch((x, y), w, h,
                                   boxstyle=boxstyle, fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            color=tc, fontsize=fs, weight="bold")


def save(fig, out_path: str | Path) -> Path:
    """Save with the standard flags (tight bbox, dpi 140, white background)."""
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


def images_dir(from_file: str | Path) -> Path:
    """Resolve the canonical `_prep_notes/images/` directory relative to a
    figure generator script.  Typical use in a generator:

        OUT = images_dir(__file__)
        ...
        save(fig, OUT / "R1_cell_anatomy.png")
    """
    src = Path(from_file).resolve()
    # Generator scripts live in _prep_notes/code/, so images/ is its sibling.
    return src.parent.parent / "images"
