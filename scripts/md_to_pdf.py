"""Convert a module markdown file (with embedded images) to a styled A4 PDF.

Usage
-----
    python3 scripts/md_to_pdf.py path/to/notes.md [more.md ...]

Behavior
--------
- Input can sit anywhere. Output always lands in a sibling `pdf/` folder
  next to the input file, creating it if missing.
  exam_dir/_prep_notes/R1_Batteries.md  ->  exam_dir/_prep_notes/pdf/R1_Batteries.pdf
  exam_dir/CLAUDE.md                    ->  exam_dir/pdf/CLAUDE.pdf
- Images referenced with relative paths (for example ![x](images/foo.png))
  resolve because the HTML base_url is set to the markdown file's folder.
- Uses `markdown` for md -> HTML and `weasyprint` for HTML -> PDF.

Styling
-------
- A4, 18 mm top/bottom, 16 mm left/right margins.
- Colour-coded headings matching the shared framework palette.
- Justified body text at 11 pt, line height 1.55.
- Monospace code with a subtle background.
- Images and tables set to avoid page breaks.
- Blockquotes rendered as soft-yellow callouts.
- Page numbers centered in the footer.

Dependencies
------------
    pip install markdown weasyprint pygments
"""
import sys
from pathlib import Path

import markdown
from weasyprint import HTML, CSS

CSS_STYLE = """
@page {
    size: A4;
    margin: 18mm 16mm;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #888;
    }
}
body {
    font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #2c3e50;
}
h1 {
    color: #c0392b;
    font-size: 22pt;
    border-bottom: 2px solid #c0392b;
    padding-bottom: 4pt;
    page-break-before: auto;
}
h2 {
    color: #2980b9;
    font-size: 16pt;
    margin-top: 18pt;
    border-bottom: 1px solid #d0d8e0;
    padding-bottom: 3pt;
}
h3 { color: #27ae60; font-size: 13pt; margin-top: 14pt; }
h4 { color: #7f8c8d; font-size: 11.5pt; }
p  { margin: 6pt 0; text-align: justify; }
code {
    font-family: 'Fira Code', 'Consolas', monospace;
    background: #f4f6f8;
    padding: 1pt 4pt;
    border-radius: 3px;
    font-size: 10pt;
}
pre {
    background: #f4f6f8;
    border-left: 3px solid #2980b9;
    padding: 8pt 10pt;
    font-size: 10pt;
    line-height: 1.4;
    page-break-inside: avoid;
}
pre code { background: transparent; padding: 0; }
blockquote {
    border-left: 3px solid #f39c12;
    padding: 4pt 10pt;
    background: #fffbea;
    color: #7d6608;
    margin: 8pt 0;
}
table {
    border-collapse: collapse;
    margin: 8pt 0;
    font-size: 10pt;
    page-break-inside: avoid;
}
th, td { border: 1px solid #ccd2d9; padding: 4pt 8pt; }
th { background: #eef2f5; color: #2c3e50; }
img { max-width: 100%; display: block; margin: 10pt auto; page-break-inside: avoid; }
hr { border: none; border-top: 1px dashed #bdc3c7; margin: 14pt 0; }
strong { color: #c0392b; }
em { color: #7f8c8d; }
ul, ol { margin: 4pt 0 6pt 16pt; }
li { margin: 2pt 0; }
"""


def pdf_target(md_path: Path) -> Path:
    """Return the PDF output path: <md_parent>/pdf/<stem>.pdf."""
    out_dir = md_path.parent / "pdf"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / (md_path.stem + ".pdf")


def convert(md_path: Path) -> Path:
    md_path = Path(md_path).resolve()
    if not md_path.exists():
        raise FileNotFoundError(md_path)

    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "toc", "codehilite", "attr_list"],
    )
    html = (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{md_path.stem}</title></head><body>{html_body}</body></html>"
    )

    out_pdf = pdf_target(md_path)
    HTML(string=html, base_url=str(md_path.parent)).write_pdf(
        target=str(out_pdf), stylesheets=[CSS(string=CSS_STYLE)]
    )
    return out_pdf


def main(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return 1
    for arg in args:
        out = convert(Path(arg))
        print(f"wrote  {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
