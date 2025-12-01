#!/usr/bin/env python3
"""
PDF to Markdown Extractor with Image Support

Extracts text and images from PDFs using CLI tools (pdftotext, pdfimages)
and combines them into a markdown file with proper image references.

Usage:
    uv run extract_pdf_with_images.py <input.pdf> [output_dir]

Examples:
    uv run extract_pdf_with_images.py ~/Downloads/report.pdf
    uv run extract_pdf_with_images.py ~/Downloads/report.pdf ./materials-for-ted/ss-it-smp-q3-2025/
"""

# /// script
# requires-python = ">=3.11"
# dependencies = ["rich"]
# ///

import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from rich.console import Console

console = Console()


def extract_text(pdf_path: Path, output_txt: Path) -> None:
    """Extract text using pdftotext with layout preservation."""
    console.print(f"[blue]Extracting text...[/blue]")
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), str(output_txt)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        console.print(f"[red]Error: {result.stderr}[/red]")
        raise RuntimeError(f"pdftotext failed: {result.stderr}")
    console.print(f"  [green]✓[/green] Text extracted to {output_txt.name}")


def extract_images(pdf_path: Path, output_dir: Path, prefix: str) -> int:
    """Extract images using pdfimages as PNG with page numbers."""
    console.print(f"[blue]Extracting images...[/blue]")
    output_dir.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["pdfimages", "-png", "-p", str(pdf_path), str(output_dir / prefix)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        console.print(f"[red]Error: {result.stderr}[/red]")
        raise RuntimeError(f"pdfimages failed: {result.stderr}")

    # Count extracted images
    images = list(output_dir.glob(f"{prefix}-*.png"))
    console.print(f"  [green]✓[/green] Extracted {len(images)} images to {output_dir.name}/")
    return len(images)


def get_image_page_mapping(pdf_path: Path) -> dict[int, list[str]]:
    """
    Parse pdfimages -list to map pages to image filenames.

    Returns dict mapping page number to list of image filenames (e.g., "page-007-000.png")
    """
    result = subprocess.run(
        ["pdfimages", "-list", str(pdf_path)],
        capture_output=True,
        text=True,
        check=True,
    )

    page_to_images: dict[int, list[str]] = defaultdict(list)

    # Parse output: "page   num  type   width height ..."
    # Skip first 2 header lines
    for line in result.stdout.strip().split("\n")[2:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            page = int(parts[0])
            img_num = int(parts[1])
            # pdfimages -p creates files like: prefix-PPP-NNN.png
            # where PPP = page number, NNN = image number on that page
            filename = f"page-{page:03d}-{img_num:03d}.png"
            page_to_images[page].append(filename)
        except (ValueError, IndexError):
            continue

    return dict(page_to_images)


def get_pdf_info(pdf_path: Path) -> dict[str, str]:
    """Extract PDF metadata using pdfinfo."""
    result = subprocess.run(
        ["pdfinfo", str(pdf_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {}

    info = {}
    for line in result.stdout.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    return info


def combine_to_markdown(
    text_file: Path,
    images_dir: Path,
    image_prefix: str,
    output_md: Path,
    pdf_name: str,
    page_mapping: dict[int, list[str]],
    pdf_info: dict[str, str],
) -> None:
    """Combine extracted text and image references into markdown."""
    console.print(f"[blue]Generating markdown...[/blue]")

    # Read text and split by page breaks (form feed character)
    text_content = text_file.read_text(encoding="utf-8", errors="replace")
    pages = text_content.split("\f")

    with open(output_md, "w", encoding="utf-8") as out:
        # YAML front matter for Pandoc compatibility
        out.write("---\n")
        out.write(f'title: "{pdf_name}"\n')
        if pdf_info.get("Author"):
            out.write(f'author: "{pdf_info["Author"]}"\n')
        out.write(f'date: "{datetime.now().strftime("%Y-%m-%d")}"\n')
        out.write("---\n\n")

        # Document header
        out.write(f"# {pdf_name}\n\n")
        out.write(f"**Source:** `{pdf_name}.pdf`\n")
        out.write(f"**Converted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        if pdf_info.get("Pages"):
            out.write(f"**Pages:** {pdf_info['Pages']}\n")
        if pdf_info.get("Creator"):
            out.write(f"**Creator:** {pdf_info['Creator']}\n")
        out.write("\n---\n\n")

        # Process each page
        for page_num, page_text in enumerate(pages, start=1):
            page_text = page_text.strip()
            if not page_text:
                continue

            out.write(f"## Page {page_num}\n\n")

            # Insert images for this page (at the top of page content)
            if page_num in page_mapping:
                for img_filename in page_mapping[page_num]:
                    img_path = images_dir / img_filename
                    if img_path.exists():
                        # Use relative path for portability
                        rel_path = f"images/{img_filename}"
                        out.write(f"![Page {page_num} Image]({rel_path})\n\n")

            # Write page text content
            # Clean up excessive blank lines but preserve structure
            lines = page_text.split("\n")
            cleaned_lines = []
            blank_count = 0
            for line in lines:
                if line.strip():
                    cleaned_lines.append(line)
                    blank_count = 0
                else:
                    blank_count += 1
                    if blank_count <= 2:  # Allow max 2 consecutive blank lines
                        cleaned_lines.append("")

            out.write("\n".join(cleaned_lines))
            out.write("\n\n---\n\n")

    console.print(f"  [green]✓[/green] Markdown saved to {output_md.name}")


def main() -> None:
    """Main extraction workflow."""
    # Parse arguments
    if len(sys.argv) < 2:
        console.print("[red]Usage: uv run extract_pdf_with_images.py <input.pdf> [output_dir][/red]")
        console.print("\nExamples:")
        console.print("  uv run extract_pdf_with_images.py ~/Downloads/report.pdf")
        console.print("  uv run extract_pdf_with_images.py ~/Downloads/report.pdf ./output/")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)

    # Determine output directory
    if len(sys.argv) > 2:
        output_dir = Path(sys.argv[2]).expanduser().resolve()
    else:
        # Default: create directory named after PDF (without extension)
        output_dir = Path.cwd() / pdf_path.stem.lower().replace(" ", "-")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Derive output names
    base_name = output_dir.name  # Use directory name as base
    images_dir = output_dir / "images"
    text_file = output_dir / f"{base_name}.txt"
    markdown_file = output_dir / f"{base_name}.md"

    console.print(f"\n[bold]PDF to Markdown Extractor[/bold]")
    console.print(f"Input:  {pdf_path}")
    console.print(f"Output: {output_dir}/\n")

    # Get PDF info
    pdf_info = get_pdf_info(pdf_path)

    # Extract text
    extract_text(pdf_path, text_file)

    # Get image-to-page mapping BEFORE extracting (uses -list, doesn't extract)
    page_mapping = get_image_page_mapping(pdf_path)

    # Extract images
    image_count = extract_images(pdf_path, images_dir, "page")

    # Combine to markdown
    combine_to_markdown(
        text_file=text_file,
        images_dir=images_dir,
        image_prefix="page",
        output_md=markdown_file,
        pdf_name=pdf_path.stem,
        page_mapping=page_mapping,
        pdf_info=pdf_info,
    )

    # Clean up intermediate text file
    text_file.unlink()

    # Summary
    console.print(f"\n[bold green]✓ Extraction complete![/bold green]")
    console.print(f"  Markdown: {markdown_file}")
    console.print(f"  Images:   {image_count} files in {images_dir}/")
    console.print(f"\nNext steps:")
    console.print(f"  1. Review: open {markdown_file}")
    console.print(f"  2. Optionally copy original PDF: cp '{pdf_path}' {output_dir}/")


if __name__ == "__main__":
    main()
