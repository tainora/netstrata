#!/usr/bin/env bash
# Comprehensive PDF verification script
# Usage: verify-pdf.sh <pdf-file>

set -euo pipefail

PDF="$1"

if [ ! -f "$PDF" ]; then
    echo "Error: PDF file not found: $PDF"
    exit 1
fi

echo "=== PDF VERIFICATION REPORT ==="
echo "File: $PDF"
echo "Date: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. PDF Metadata
echo "1. PDF METADATA:"
pdfinfo "$PDF" | grep -E "Pages|File size|Producer|Creator" || echo "  Warning: pdfinfo not available"
echo ""

# 2. Extract full text for analysis
FULLTEXT=$(mktemp)
pdftotext -layout "$PDF" "$FULLTEXT" 2>/dev/null || {
    echo "  Warning: pdftotext not available"
    rm -f "$FULLTEXT"
    exit 0
}

# 3. Check for bare URLs
echo "2. BARE URL CHECK:"
BARE_URLS=$((grep -o "https://[^ ]*" "$FULLTEXT" || true) | wc -l | tr -d ' ')
if [ "$BARE_URLS" -eq 0 ]; then
    echo "  ✓ No bare URLs found"
else
    echo "  ✗ Found $BARE_URLS potential bare URLs"
    echo "  First occurrences:"
    grep -n "https://" "$FULLTEXT" | head -5 | sed 's/^/    /'
fi
echo ""

# 4. Table alignment check
echo "3. TABLE FORMATTING:"
TABLE_COUNT=$(grep -c "^[A-Z].*|" "$FULLTEXT" || true)
if [ "$TABLE_COUNT" -gt 0 ]; then
    echo "  Found $TABLE_COUNT potential table rows"
    echo "  Sample table content:"
    grep "^[A-Z].*|" "$FULLTEXT" | head -10 | sed 's/^/    /'
else
    echo "  ✓ No table formatting issues detected"
fi
echo ""

# 5. Check for common formatting issues
echo "4. FORMATTING CHECKS:"

# Check for text wrapping issues (lines ending with single word followed by hyphen)
HYPHEN_BREAKS=$(grep -c -- "-$" "$FULLTEXT" || true)
if [ "$HYPHEN_BREAKS" -gt 5 ]; then
    echo "  ⚠ Warning: $HYPHEN_BREAKS hyphenated line breaks (may indicate text overflow)"
else
    echo "  ✓ Minimal hyphenation ($HYPHEN_BREAKS occurrences)"
fi

# Check for orphaned bullets or list markers
ORPHAN_BULLETS=$(grep -c "^  *[-•]$" "$FULLTEXT" || true)
if [ "$ORPHAN_BULLETS" -gt 0 ]; then
    echo "  ⚠ Warning: $ORPHAN_BULLETS orphaned bullet points"
else
    echo "  ✓ No orphaned bullets detected"
fi
echo ""

# 6. Critical sections verification (customize per document)
echo "5. DOCUMENT STRUCTURE:"
SECTIONS=$(grep -c "^[0-9]\+\." "$FULLTEXT" || true)
echo "  Numbered sections found: $SECTIONS"
TOC_ENTRIES=$(grep -c "\. \. \. \. \." "$FULLTEXT" || true)
echo "  Table of contents entries: $TOC_ENTRIES"
echo ""

# Cleanup
rm "$FULLTEXT"

echo "=== VERIFICATION COMPLETE ==="
echo ""
echo "RECOMMENDATION:"
echo "- Review any warnings above"
echo "- Open PDF in viewer to visually confirm formatting"
echo "- Check critical sections manually for proper rendering"
