#!/usr/bin/env python3
"""
Format-Aware PDF to GFM Extractor

Enhanced extraction that preserves formatting by analyzing font metadata:
- Font sizes → Markdown headers (# ## ###)
- Bold text → **bold**
- Bullet characters → - list items
- Intelligent line joining that respects formatting boundaries

Usage:
    uv run extract_pdf_formatted.py <input.pdf> [output_dir]
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


def analyze_font_hierarchy(doc: fitz.Document) -> dict[float, str]:
    """
    Analyze document to build font size → markdown level mapping.

    Returns dict like: {36.0: '#', 24.0: '##', 13.9: '###', 12.0: ''}
    """
    from collections import Counter

    size_counts: Counter[float] = Counter()

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        text = span.get("text", "").strip()
                        if text and len(text) > 2:
                            size = round(span.get("size", 0), 1)
                            size_counts[size] += 1

    # Sort sizes descending
    sizes = sorted(size_counts.keys(), reverse=True)

    # Find body text (most common size)
    body_size = size_counts.most_common(1)[0][0] if size_counts else 12.0

    # Build hierarchy: sizes larger than body become headers
    hierarchy = {}
    header_level = 1
    for size in sizes:
        if size > body_size + 1:  # Significantly larger than body
            hierarchy[size] = '#' * min(header_level, 4)  # Max ####
            header_level += 1
        else:
            hierarchy[size] = ''  # Body text or smaller

    return hierarchy


def extract_line_content(line: dict, font_hierarchy: dict[float, str]) -> tuple[str, bool, bool]:
    """
    Extract text from a line with formatting markers.

    Returns: (text, is_header, is_bold_line)
    """
    spans = line.get("spans", [])
    if not spans:
        return "", False, False

    parts = []
    is_header = False
    header_prefix = ""
    all_bold = True
    has_text = False

    for span in spans:
        text = span.get("text", "")
        if not text.strip():
            continue

        has_text = True
        size = round(span.get("size", 0), 1)
        flags = span.get("flags", 0)
        font = span.get("font", "")
        is_bold = bool(flags & 16) or "Bold" in font

        # Check if this is a header size
        if size in font_hierarchy and font_hierarchy[size]:
            is_header = True
            header_prefix = font_hierarchy[size]

        # Track if entire line is bold
        if not is_bold:
            all_bold = False

        # Handle bullet characters
        if font == "SymbolMT" or text.strip() in ["•", "●", "○", "◦", "▪"]:
            parts.append("- ")
        else:
            parts.append(text)

    line_text = "".join(parts).strip()

    return line_text, is_header, (all_bold and has_text and not is_header)


def is_section_boundary(text: str, is_bold: bool) -> bool:
    """
    Detect if text represents a section boundary (should not be joined to previous).

    Section boundaries include:
    - Bold headings like "Top 3 Wins", "Looking Ahead"
    - ALL CAPS headers
    - Text ending with colon
    """
    if not text:
        return False

    # Bold text at start of logical section
    if is_bold and len(text) < 60:
        return True

    # ALL CAPS (but not single words like "MYOB")
    if text.isupper() and len(text.split()) > 1:
        return True

    # Common section markers
    section_patterns = [
        r"^Top \d+",
        r"^Looking Ahead",
        r"^What's Coming",
        r"^Key dates",
        r"^\d+[-–]\d+ Day Focus",
        r"^COMPLETED$",
        r"^IN PROGRESS$",
        r"^PLANNED",
        r"^EXECUTIVE SUMMARY$",
    ]
    for pattern in section_patterns:
        if re.match(pattern, text, re.IGNORECASE):
            return True

    return False


def extract_pdf_formatted(pdf_path: Path, output_dir: Path) -> tuple[Path, int]:
    """
    Extract PDF to GFM with proper formatting preservation.
    """
    doc = fitz.open(pdf_path)

    # Analyze font hierarchy
    console.print("[blue]Analyzing document font hierarchy...[/blue]")
    font_hierarchy = analyze_font_hierarchy(doc)
    console.print(f"  Found {len([s for s in font_hierarchy.values() if s])} header levels")

    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)

    base_name = output_dir.name
    md_path = output_dir / f"{base_name}.md"

    markdown_lines = []
    image_count = 0

    # YAML front matter
    markdown_lines.extend([
        "---",
        f'title: "{pdf_path.stem}"',
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "---",
        "",
        f"# {pdf_path.stem}",
        "",
        f"**Source:** `{pdf_path.name}`",
        f"**Pages:** {len(doc)}",
        "",
        "---",
        "",
    ])

    for page_num, page in enumerate(doc, 1):
        console.print(f"  Processing page {page_num}/{len(doc)}...", end="\r")

        blocks = page.get_text("dict")["blocks"]
        sorted_blocks = sorted(blocks, key=lambda b: b.get("bbox", [0, 0, 0, 0])[1])

        page_content = []

        for block in sorted_blocks:
            if block["type"] == 0:  # Text block
                block_lines = []

                for line in block.get("lines", []):
                    line_text, is_header, is_bold = extract_line_content(line, font_hierarchy)

                    if not line_text:
                        continue

                    # Skip page number artifacts
                    if re.match(r"^Page \d+$", line_text):
                        continue

                    # Format the line
                    if is_header:
                        # Headers get their own line
                        if block_lines:
                            page_content.append(" ".join(block_lines))
                            block_lines = []
                        page_content.append("")  # Blank before header
                        page_content.append(f"### {line_text}")
                        page_content.append("")  # Blank after header
                    elif is_bold and is_section_boundary(line_text, is_bold):
                        # Bold section headings
                        if block_lines:
                            page_content.append(" ".join(block_lines))
                            block_lines = []
                        page_content.append("")
                        page_content.append(f"**{line_text}**")
                        page_content.append("")
                    elif line_text.startswith("- "):
                        # Bullet items - don't join with previous
                        if block_lines:
                            page_content.append(" ".join(block_lines))
                            block_lines = []
                        page_content.append(line_text)
                    else:
                        # Regular text - collect for joining
                        block_lines.append(line_text)

                # Flush remaining block lines
                if block_lines:
                    page_content.append(" ".join(block_lines))

            elif block["type"] == 1:  # Image block
                bbox = block["bbox"]
                try:
                    clip = fitz.Rect(bbox)
                    pix = page.get_pixmap(clip=clip, dpi=150)

                    if pix.width > 50 and pix.height > 50:
                        image_count += 1
                        img_filename = f"page{page_num:02d}_img{image_count:02d}.png"
                        img_path = images_dir / img_filename
                        pix.save(str(img_path))
                        page_content.append("")
                        page_content.append(f"![Page {page_num} Figure {image_count}](images/{img_filename})")
                        page_content.append("")
                except Exception as e:
                    console.print(f"  [yellow]Warning: Could not extract image on page {page_num}: {e}[/yellow]")

        # Add page content
        if page_content:
            markdown_lines.append(f"## Page {page_num}")
            markdown_lines.append("")
            markdown_lines.extend(page_content)
            markdown_lines.append("")
            markdown_lines.append("---")
            markdown_lines.append("")

    doc.close()

    # Join and clean up
    raw_md = "\n".join(markdown_lines)
    cleaned_md = clean_markdown(raw_md)

    md_path.write_text(cleaned_md, encoding="utf-8")

    return md_path, image_count


def join_wrapped_lines(md_text: str) -> str:
    """
    Join lines that were wrapped in PDF but should be continuous.

    Handles:
    - Bullet items that wrap across lines
    - Paragraph text that wraps
    """
    lines = md_text.split('\n')
    result = []
    i = 0
    in_frontmatter = False

    while i < len(lines):
        line = lines[i]

        # Track YAML front matter
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result.append(line)
            i += 1
            continue

        # Skip YAML front matter content
        if in_frontmatter:
            result.append(line)
            i += 1
            continue

        # Skip structural elements
        if (not line.strip() or
            line.startswith('#') or
            line.startswith('![') or
            line.startswith('**') and line.rstrip().endswith('**')):
            result.append(line)
            i += 1
            continue

        # Check if line continues on next (doesn't end with sentence terminator)
        current = line
        while i + 1 < len(lines):
            next_line = lines[i + 1].strip()

            # Stop joining if next line is structural
            if (not next_line or
                next_line.startswith('#') or
                next_line.startswith('-') or
                next_line.startswith('![') or
                next_line.startswith('**') or
                next_line.startswith('---')):
                break

            # Check if current line needs continuation
            current_stripped = current.rstrip()
            if current_stripped.endswith(('.', ':', '!', '?', ')')):
                # Ends with terminator - don't join unless next starts lowercase
                if next_line and next_line[0].isupper():
                    break

            # Join with next line
            current = current.rstrip() + ' ' + next_line
            i += 1

        result.append(current)
        i += 1

    return '\n'.join(result)


def clean_markdown(md_text: str) -> str:
    """Final markdown cleanup."""
    # Join wrapped lines first
    md_text = join_wrapped_lines(md_text)

    # Collapse 3+ blank lines to 2
    md_text = re.sub(r"\n{4,}", "\n\n\n", md_text)

    # Remove blank lines at start of sections
    md_text = re.sub(r"(## Page \d+)\n\n\n+", r"\1\n\n", md_text)

    # Ensure blank line before headers
    md_text = re.sub(r"([^\n])\n(###)", r"\1\n\n\2", md_text)

    # Remove trailing whitespace
    lines = [line.rstrip() for line in md_text.split("\n")]
    md_text = "\n".join(lines)

    # Clean up multiple spaces
    md_text = re.sub(r"  +", " ", md_text)

    return md_text


def main() -> None:
    if len(sys.argv) < 2:
        console.print("[red]Usage: uv run extract_pdf_formatted.py <input.pdf> [output_dir][/red]")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)

    if len(sys.argv) > 2:
        output_dir = Path(sys.argv[2]).expanduser().resolve()
    else:
        output_dir = Path.cwd() / pdf_path.stem.lower().replace(" ", "-")

    console.print(f"\n[bold]Format-Aware PDF to GFM Extractor[/bold]")
    console.print(f"Input:  {pdf_path}")
    console.print(f"Output: {output_dir}/\n")

    md_path, image_count = extract_pdf_formatted(pdf_path, output_dir)

    console.print(f"\n[bold green]Extraction complete![/bold green]")
    console.print(f"  Markdown: {md_path}")
    console.print(f"  Images:   {image_count} files")
    console.print(f"\nFormatting preserved:")
    console.print(f"  - Headers detected by font size")
    console.print(f"  - Bold section headings marked")
    console.print(f"  - Bullet lists properly formatted")
    console.print(f"  - Images inline at reading positions")


if __name__ == "__main__":
    main()
