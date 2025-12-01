#!/usr/bin/env python3
"""
GFM Post-Processor for PDF-Extracted Markdown

Fixes common issues from PDF extraction:
- Joins wrapped lines (PDF text flow → proper paragraphs)
- Removes duplicate paragraphs
- Cleans bullet point continuation lines
- Normalizes whitespace

Usage:
    uv run postprocess_gfm.py <input.md> [output.md]
"""

# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import re
import sys
from pathlib import Path


def join_wrapped_lines(text: str) -> str:
    """
    Join lines that were wrapped in PDF but should be continuous paragraphs.

    Heuristic: If a line doesn't end with a sentence terminator and the next
    line doesn't start with a markdown element, join them.
    """
    lines = text.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines, headers, list items, images, horizontal rules
        if (not line.strip() or
            line.startswith('#') or
            line.startswith('---') or
            line.startswith('![') or
            line.startswith('**') and line.endswith('**') or  # Bold metadata
            re.match(r'^-\s', line)):  # List item
            result.append(line)
            i += 1
            continue

        # Check if this line should be joined with next
        # Line doesn't end with sentence terminator and next line exists
        if (not line.rstrip().endswith(('.', ':', '!', '?', ')', '"', "'")) and
            i + 1 < len(lines)):
            next_line = lines[i + 1].strip()

            # Next line should be continuation (not a new element)
            if (next_line and
                not next_line.startswith('#') and
                not next_line.startswith('-') and
                not next_line.startswith('!') and
                not next_line.startswith('**') and
                not next_line.startswith('---') and
                not re.match(r'^\d+\.', next_line)):  # Not numbered list

                # Join with next line
                joined = line.rstrip() + ' ' + next_line
                lines[i + 1] = joined  # Replace next line with joined
                i += 1  # Skip current line (it's now part of next)
                continue

        result.append(line)
        i += 1

    return '\n'.join(result)


def fix_bullet_continuations(text: str) -> str:
    """
    Fix bullet points that wrap across multiple lines.

    Before:
        - This is a bullet point that wraps
        across multiple lines.

    After:
        - This is a bullet point that wraps across multiple lines.
    """
    lines = text.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a bullet point
        if re.match(r'^-\s', line):
            # Collect continuation lines
            bullet_content = [line]

            while i + 1 < len(lines):
                next_line = lines[i + 1]

                # Check if next line is a continuation (not a new element)
                if (next_line.strip() and
                    not next_line.startswith('-') and
                    not next_line.startswith('#') and
                    not next_line.startswith('!') and
                    not next_line.startswith('---') and
                    not next_line.startswith('**') and
                    not re.match(r'^\d+\.', next_line.strip())):
                    # This is a continuation
                    bullet_content.append(next_line.strip())
                    i += 1
                else:
                    break

            # Join the bullet content
            joined_bullet = ' '.join(bullet_content)
            # Normalize whitespace
            joined_bullet = re.sub(r'\s+', ' ', joined_bullet)
            result.append(joined_bullet)
        else:
            result.append(line)

        i += 1

    return '\n'.join(result)


def remove_duplicate_paragraphs(text: str) -> str:
    """
    Remove near-duplicate paragraphs (80%+ word overlap).
    Keeps the longer version.
    """
    # Split into paragraphs (separated by blank lines)
    paragraphs = re.split(r'\n\s*\n', text)
    seen = []
    result = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # Skip short lines (headers, metadata, etc.)
        if len(para) < 100:
            result.append(para)
            continue

        # Check for similarity with seen paragraphs
        para_words = set(para.lower().split())
        is_duplicate = False

        for i, (seen_para, seen_words) in enumerate(seen):
            # Calculate word overlap
            if not para_words or not seen_words:
                continue

            overlap = len(para_words & seen_words) / min(len(para_words), len(seen_words))

            if overlap > 0.8:  # 80% overlap = duplicate
                # Keep the longer one
                if len(para) > len(seen_para):
                    # Replace with longer version
                    seen[i] = (para, para_words)
                    # Find and replace in result
                    for j, r in enumerate(result):
                        if r == seen_para:
                            result[j] = para
                            break
                is_duplicate = True
                break

        if not is_duplicate:
            seen.append((para, para_words))
            result.append(para)

    return '\n\n'.join(result)


def normalize_whitespace(text: str) -> str:
    """Final whitespace cleanup."""
    # Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove trailing whitespace
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)

    # Ensure blank line before headers
    text = re.sub(r'([^\n])\n(## Page)', r'\1\n\n\2', text)

    # Ensure single blank line after ---
    text = re.sub(r'---\n{3,}', '---\n\n', text)

    return text


def postprocess(input_path: Path, output_path: Path) -> dict:
    """
    Apply all post-processing steps and return statistics.
    """
    original = input_path.read_text(encoding='utf-8')
    original_lines = len(original.split('\n'))
    original_chars = len(original)

    # Apply transformations
    text = original
    text = fix_bullet_continuations(text)
    text = join_wrapped_lines(text)
    text = remove_duplicate_paragraphs(text)
    text = normalize_whitespace(text)

    # Write output
    output_path.write_text(text, encoding='utf-8')

    final_lines = len(text.split('\n'))
    final_chars = len(text)

    return {
        'original_lines': original_lines,
        'final_lines': final_lines,
        'line_reduction': original_lines - final_lines,
        'original_chars': original_chars,
        'final_chars': final_chars,
        'char_reduction_pct': (1 - final_chars / original_chars) * 100 if original_chars else 0
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run postprocess_gfm.py <input.md> [output.md]")
        sys.exit(1)

    input_path = Path(sys.argv[1]).expanduser().resolve()
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Default output: overwrite input (or specify output)
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2]).expanduser().resolve()
    else:
        output_path = input_path

    print(f"Post-processing: {input_path}")

    stats = postprocess(input_path, output_path)

    print(f"\n✓ Post-processing complete!")
    print(f"  Lines: {stats['original_lines']} → {stats['final_lines']} (-{stats['line_reduction']})")
    print(f"  Size: {stats['original_chars']:,} → {stats['final_chars']:,} chars ({stats['char_reduction_pct']:.1f}% reduction)")
    print(f"  Output: {output_path}")


if __name__ == "__main__":
    main()
