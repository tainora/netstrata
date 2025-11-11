# PDF Generation Best Practices

This reference document contains proven best practices for generating professional PDFs from markdown using pandoc and XeLaTeX.

## Font Selection

### Principles

1. **Avoid emoji in professional documents** - Most professional fonts (Helvetica, Times New Roman, Garamond, DejaVu Sans) do not support emoji characters (✅ ❌ ⚠️)
2. **Use ASCII + basic Unicode only** - Stick to arrows (→), multiplication (×), en-dashes (–) which have broad font support
3. **Test font coverage before production** - Generate a test PDF to check for font warnings

### Recommended Fonts

**For Business Documents:**
- **DejaVu Sans** - Excellent Unicode coverage, professional weight, zero warnings for standard characters
- **Source Sans 3** - Modern, clean, but lighter weight
- **Helvetica Neue** - Classic, professional (macOS built-in)
- **Georgia** - Serif option for formal documents

**Font Installation Check:**
```bash
# List available system fonts
fc-list : family | grep -i "font-name"
```

### Common Font Warnings

```
[WARNING] Missing character: There is no ✅ (U+2705) in font DejaVu Sans
```

**Solution:** Remove emoji, replace with text bullets or checkmarks using standard characters.

## Table Formatting

### Avoid Common Pitfalls

1. **Three-column tables with long text** - Causes awkward text wrapping
2. **Date columns that are too wide** - Wastes horizontal space
3. **Topic/description columns with mid-phrase breaks** - Looks unprofessional

### Better Approaches

**❌ Bad: Three-column table with long URLs**
```markdown
| Date | Blog Post Title | Topic |
|------|-----------------|-------|
| Oct 27, 2025 | "Long Title..." | October 2025 reforms |
```

**✓ Good: Hierarchical bullet list with embedded links**
```markdown
**October 2025 Reforms:**
- ["Long Title"](https://...) (Oct 27, 2025)
- ["Another Title"](https://...) (Oct 15, 2025)
```

**✓ Good: Two-column table when necessary**
```markdown
| Metric | Value |
|--------|-------|
| Short text | Short text |
```

## Hyperlinks & Citations

### Best Practices

1. **Never show bare URLs** - Always embed as clickable links
2. **Use descriptive link text** - Title of document/page, not "click here"
3. **Date placement** - After title in parentheses for chronological clarity

**❌ Bad:**
```markdown
**Blog Post**: "Title"
**URL**: https://example.com/very-long-url
```

**✓ Good:**
```markdown
- ["Title"](https://example.com/very-long-url) (Oct 27, 2025)
```

### Verification

```bash
# Check for bare URLs in generated PDF
pdftotext file.pdf - | grep -c "https://"
```

Expected: 0 results (all URLs should be embedded as links)

## Pandoc Command Template

### Standard Business Document

```bash
pandoc INPUT.md -o OUTPUT.pdf \
  --pdf-engine=xelatex \
  -V geometry:a4paper \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V mainfont="DejaVu Sans" \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  --toc \
  --toc-depth=2
```

### Option Reference

- `--pdf-engine=xelatex` - Better Unicode support than pdflatex
- `-V geometry:a4paper` - International standard paper size
- `-V geometry:margin=1in` - Comfortable reading margins
- `-V fontsize=11pt` - Professional body text size
- `-V mainfont="DejaVu Sans"` - Font with broad character support
- `-V colorlinks=true` - Clickable hyperlinks
- `-V linkcolor=blue` - Standard web convention
- `--toc` - Generate table of contents
- `--toc-depth=2` - Include ## and ### headers in TOC

## Verification Checklist

### Pre-Generation

- [ ] Remove all emoji from source markdown
- [ ] Embed all URLs as markdown links `[text](url)`
- [ ] Remove manual section numbering - use `--number-sections` instead
- [ ] Test table formatting with pdftotext before final generation
- [ ] Ensure font is installed and supports characters used

### Post-Generation

- [ ] Run verification script: `scripts/verify-pdf.sh OUTPUT.pdf`
- [ ] Check for font warnings in pandoc output
- [ ] Verify no bare URLs visible: `pdftotext file.pdf - | grep "https://"`
- [ ] Open in PDF viewer to visually confirm formatting
- [ ] Check all tables render without text overflow
- [ ] Verify clickable links work

## Common Issues & Solutions

### Issue: Font Warnings

```
[WARNING] Missing character: There is no → (U+2192) in font Open Sans
```

**Solutions:**
1. Switch to DejaVu Sans (broad Unicode support)
2. Replace special characters with ASCII equivalents
3. Use fallback font configuration

### Issue: Ugly Table Wrapping

**Symptoms:** Date column breaks across lines, topic text has mid-phrase breaks

**Solutions:**
1. Redesign as hierarchical bullet list
2. Use two-column table instead of three
3. Shorten column content
4. Use landscape orientation for wide tables

### Issue: Bare URLs Visible

**Symptoms:** `https://example.com/path` appears in PDF text

**Solutions:**
1. Convert to markdown links: `[Title](https://...)`
2. Verify with: `pdftotext file.pdf - | grep "https://"`
3. Regenerate PDF after fixing

### Issue: Large File Size

**Symptoms:** PDF >1MB for text-only document

**Solutions:**
1. Check for embedded images
2. Use `-V graphics=false` if no images needed
3. Optimize images before including
4. Use `gs` (Ghostscript) to compress: `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed.pdf input.pdf`

## Tools Required

### macOS (Homebrew)

```bash
brew install pandoc
brew install --cask mactex-no-gui  # XeLaTeX engine
brew install poppler  # pdftotext, pdfinfo
```

### Linux (Debian/Ubuntu)

```bash
apt-get install pandoc texlive-xetex poppler-utils
```

### Verification

```bash
# Check installations
pandoc --version
xelatex --version
pdftotext -v
pdfinfo -v
```
