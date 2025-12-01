#!/usr/bin/env python3
"""
PDF to GitHub Flavored Markdown Extractor

Extracts PDFs to clean GFM with images placed INLINE at their correct
reading positions (chronologically matching the PDF flow).

Features:
- Images appear where they belong in the document flow
- Clean whitespace (no excessive blank lines)
- GFM-compliant formatting (- bullets, proper headers)
- Removes PDF page number artifacts

Usage:
    uv run extract_pdf_to_gfm.py <input.pdf> [output_dir]

Examples:
    uv run extract_pdf_to_gfm.py ~/Downloads/report.pdf
    uv run extract_pdf_to_gfm.py ~/Downloads/report.pdf ./materials-for-ted/ss-it-smp-q3-2025/
"""

# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf", "rich"]
# ///

import re
import sys
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF
from rich.console import Console

console = Console()


def extract_pdf_to_gfm(pdf_path: Path, output_dir: Path) -> tuple[Path, int]:
    """
    Extract PDF to GFM markdown with inline images at correct positions.

    Returns:
        Tuple of (markdown_path, image_count)
    """
    doc = fitz.open(pdf_path)

    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)

    base_name = output_dir.name
    md_path = output_dir / f"{base_name}.md"

    markdown_lines = []
    image_count = 0

    # YAML front matter
    markdown_lines.append("---")
    markdown_lines.append(f'title: "{pdf_path.stem}"')
    markdown_lines.append(f'date: "{datetime.now().strftime("%Y-%m-%d")}"')
    markdown_lines.append("---")
    markdown_lines.append("")
    markdown_lines.append(f"# {pdf_path.stem}")
    markdown_lines.append("")
    markdown_lines.append(f"**Source:** `{pdf_path.name}`")
    markdown_lines.append(f"**Pages:** {len(doc)}")
    markdown_lines.append("")
    markdown_lines.append("---")
    markdown_lines.append("")

    for page_num, page in enumerate(doc, 1):
        console.print(f"  Processing page {page_num}/{len(doc)}...", end="\r")

        # Get all blocks (text and images) with their positions
        blocks = page.get_text("dict")["blocks"]

        # Sort blocks by vertical position (top to bottom = reading order)
        sorted_blocks = sorted(blocks, key=lambda b: b.get("bbox", [0, 0, 0, 0])[1])

        page_content = []

        for block in sorted_blocks:
            if block["type"] == 0:  # Text block
                text = extract_text_from_block(block)
                if text.strip():
                    page_content.append(text)

            elif block["type"] == 1:  # Image block
                # Extract and save image
                bbox = block["bbox"]
                try:
                    # Get image from this region
                    clip = fitz.Rect(bbox)
                    pix = page.get_pixmap(clip=clip, dpi=150)

                    if pix.width > 50 and pix.height > 50:  # Skip tiny images
                        image_count += 1
                        img_filename = f"page{page_num:02d}_img{image_count:02d}.png"
                        img_path = images_dir / img_filename
                        pix.save(str(img_path))

                        # Add image reference inline
                        page_content.append(f"\n![Page {page_num} Figure {image_count}](images/{img_filename})\n")
                except Exception as e:
                    console.print(f"  [yellow]Warning: Could not extract image on page {page_num}: {e}[/yellow]")

        # Combine page content
        if page_content:
            markdown_lines.append(f"## Page {page_num}")
            markdown_lines.append("")

            for content in page_content:
                markdown_lines.append(content)

            markdown_lines.append("")
            markdown_lines.append("---")
            markdown_lines.append("")

    doc.close()

    # Join and clean up
    raw_md = "\n".join(markdown_lines)
    cleaned_md = clean_markdown_for_gfm(raw_md)

    # Write output
    md_path.write_text(cleaned_md, encoding="utf-8")

    return md_path, image_count


def extract_text_from_block(block: dict) -> str:
    """Extract text from a PyMuPDF text block, preserving structure."""
    lines = []

    for line in block.get("lines", []):
        line_text = ""
        for span in line.get("spans", []):
            text = span.get("text", "")
            line_text += text

        if line_text.strip():
            lines.append(line_text.strip())

    return "\n".join(lines)


def clean_markdown_for_gfm(md_text: str) -> str:
    """
    Clean up markdown for GitHub Flavored Markdown compliance.

    Fixes:
    - Excessive blank lines (max 2 consecutive)
    - PDF page number artifacts
    - Unicode bullets to GFM dashes
    - Trailing whitespace
    """
    # 1. Remove PDF page number artifacts (standalone "Page N" or "Page NN" lines)
    md_text = re.sub(r'^Page \d+\s*$', '', md_text, flags=re.MULTILINE)

    # 2. Convert Unicode bullets to GFM dashes
    md_text = re.sub(r'^(\s*)•\s*', r'\1- ', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^(\s*)◦\s*', r'\1  - ', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^(\s*)▪\s*', r'\1- ', md_text, flags=re.MULTILINE)

    # 3. Collapse multiple blank lines to max 2
    md_text = re.sub(r'\n{4,}', '\n\n\n', md_text)

    # 4. Remove trailing whitespace from each line
    lines = [line.rstrip() for line in md_text.split('\n')]
    md_text = '\n'.join(lines)

    # 5. Clean up excessive spaces within lines (but preserve indentation)
    md_text = re.sub(r'([^\s])  +([^\s])', r'\1 \2', md_text)

    # 6. Ensure single blank line after headers
    md_text = re.sub(r'^(#{1,6} .+)\n{3,}', r'\1\n\n', md_text, flags=re.MULTILINE)

    # 7. Remove blank lines at start of document (after front matter)
    md_text = re.sub(r'^(---\n\n)\n+', r'\1', md_text)

    return md_text


def main() -> None:
    """Main extraction workflow."""
    if len(sys.argv) < 2:
        console.print("[red]Usage: uv run extract_pdf_to_gfm.py <input.pdf> [output_dir][/red]")
        console.print("\nExamples:")
        console.print("  uv run extract_pdf_to_gfm.py ~/Downloads/report.pdf")
        console.print("  uv run extract_pdf_to_gfm.py ~/Downloads/report.pdf ./output/")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)

    # Determine output directory
    if len(sys.argv) > 2:
        output_dir = Path(sys.argv[2]).expanduser().resolve()
    else:
        output_dir = Path.cwd() / pdf_path.stem.lower().replace(" ", "-")

    console.print(f"\n[bold]PDF to GFM Extractor (Inline Images)[/bold]")
    console.print(f"Input:  {pdf_path}")
    console.print(f"Output: {output_dir}/\n")

    console.print("[blue]Extracting with inline image placement...[/blue]")
    md_path, image_count = extract_pdf_to_gfm(pdf_path, output_dir)

    console.print(f"\n[bold green]✓ Extraction complete![/bold green]")
    console.print(f"  Markdown: {md_path}")
    console.print(f"  Images:   {image_count} files in {output_dir}/images/")
    console.print(f"\nFeatures:")
    console.print(f"  - Images placed inline at correct reading positions")
    console.print(f"  - Clean GFM formatting (no PDF artifacts)")
    console.print(f"  - Ready for GitHub viewing")


if __name__ == "__main__":
    main()
