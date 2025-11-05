#!/bin/bash
# Example Pandoc PDF build script with table spacing control
# Customize as needed for your project

set -e

# Configuration
INPUT_FILE="document.md"
OUTPUT_FILE="document.pdf"
TABLE_SPACING_FILE="table-spacing.tex"

# Optional: Set custom font (requires font to be installed)
FONT="DejaVu Sans"

# Optional: Landscape or portrait
# ORIENTATION="landscape"  # Uncomment for landscape
ORIENTATION=""

# Build PDF with XeLaTeX and custom table spacing
echo "Generating PDF with LaTeX table spacing control..."

pandoc "$INPUT_FILE" \
  -o "$OUTPUT_FILE" \
  --pdf-engine=xelatex \
  -V mainfont="$FONT" \
  -V geometry:${ORIENTATION} \
  -V geometry:margin=1in \
  -H "$TABLE_SPACING_FILE"

echo "✅ PDF generated: $OUTPUT_FILE"

# Optional: Show file info
if command -v pdfinfo &> /dev/null; then
  ls -lh "$OUTPUT_FILE"
  pdfinfo "$OUTPUT_FILE" | grep Pages
else
  ls -lh "$OUTPUT_FILE"
fi
