#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Preprocess markdown for better PDF formatting.

Automatically adds line breaks before bold headers to prevent
text from running together in PDF output.
"""

import re
import sys
from pathlib import Path


def preprocess_markdown(content: str) -> str:
    """
    Add blank lines before bold headers for better PDF formatting.

    Fixes patterns like:
        **Header1**: Value
        **Header2**: Value

    To:
        **Header1**: Value

        **Header2**: Value
    """
    lines = content.split('\n')
    processed = []

    for i, line in enumerate(lines):
        # Check if current line starts with bold and previous line is not blank
        if i > 0 and line.strip().startswith('**') and lines[i-1].strip() != '':
            # Check if previous line also starts with bold (consecutive bold headers)
            prev_line = lines[i-1].strip()
            if prev_line.startswith('**') and not prev_line.endswith('**'):
                # Previous line is a bold header with content, add blank line
                processed.append('')

        processed.append(line)

    return '\n'.join(processed)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.md> <output.md>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    # Read input
    content = input_file.read_text(encoding='utf-8')

    # Preprocess
    processed = preprocess_markdown(content)

    # Write output
    output_file.write_text(processed, encoding='utf-8')

    print(f"✓ Preprocessed {input_file} → {output_file}")


if __name__ == '__main__':
    main()
