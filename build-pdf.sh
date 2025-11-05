#!/bin/bash
# Build PDF with improved table spacing and table of contents
# Usage: ./build-pdf.sh

set -e

echo "Generating PDF with table of contents and improved table row spacing..."

pandoc STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.md \
  -o STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  -V mainfont="DejaVu Sans" \
  -V geometry:landscape \
  -V geometry:margin=1in \
  -V toc-title="Table of Contents" \
  -H table-spacing.tex

echo "✅ PDF generated: STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.pdf"
ls -lh STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.pdf
pdfinfo STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.pdf | grep Pages
