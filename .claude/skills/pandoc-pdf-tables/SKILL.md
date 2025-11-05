---
name: pandoc-pdf-tables
description: Generate professional PDFs from Markdown using Pandoc with sophisticated LaTeX table spacing control to prevent awkward page breaks. Use when creating PDFs with tables that need to stay on single pages, or when fine-tuning table appearance for readability and professional formatting.
---

# Pandoc PDF Tables

## Overview

This skill provides techniques for generating professional PDFs from Markdown using Pandoc with XeLaTeX, focusing on sophisticated LaTeX table spacing control to prevent awkward page breaks while maintaining readability.

## When to Use This Skill

Use this skill when:
- Generating PDFs from Markdown that contain tables
- Tables are breaking awkwardly across pages (single rows orphaned, poor placement)
- Need to balance table compactness with readability
- Creating professional documents requiring tight table control
- Working with Pandoc's default longtable output and need better spacing

## Core Workflow

### 1. Basic Pandoc PDF Generation

Build PDFs from Markdown using Pandoc with XeLaTeX and custom LaTeX preamble:

```bash
pandoc document.md \
  -o document.pdf \
  --pdf-engine=xelatex \
  -V mainfont="DejaVu Sans" \
  -V geometry:margin=1in \
  -H table-spacing.tex
```

**Key parameters**:
- `--pdf-engine=xelatex`: Modern LaTeX engine with better font support
- `-H table-spacing.tex`: Include custom LaTeX preamble for table formatting
- `-V geometry:margin=1in`: Set page margins

### 2. Understanding Pandoc's Table Conversion

**Default behavior**: Pandoc converts Markdown tables → LaTeX `longtable` package

**longtable characteristics**:
- ✅ Designed to break across pages (for multi-page tables)
- ✅ Handles very long tables gracefully
- ❌ Cannot easily force tables to stay on single page
- ❌ May create awkward breaks (single-row orphans at bottom of page)

**Alternative**: `tabular` package prevents all breaks but requires custom Pandoc Lua filters (complex)

**Pragmatic approach**: Improve longtable page break behavior through spacing parameters

### 3. LaTeX Table Spacing Parameters

Create a `table-spacing.tex` LaTeX preamble file to control table appearance. See `assets/table-spacing-template.tex` for a starting template.

**Key parameters** (see `references/latex-parameters.md` for detailed explanations):

#### Row Spacing
```latex
\renewcommand{\arraystretch}{1.0}
```
- Controls vertical spacing between rows
- Default: 1.0, Loose: 1.2-1.5, Compact: 0.9-1.0
- **Trade-off**: Higher = more readable, Lower = more compact

#### Cell Padding
```latex
\setlength{\extrarowheight}{2pt}
```
- Extra padding at top of cells
- Default: 0pt, Loose: 4-6pt, Compact: 2pt
- **Trade-off**: More padding = cleaner look, Less padding = shorter tables

#### Column Spacing
```latex
\setlength{\tabcolsep}{6pt}
```
- Horizontal spacing between columns
- Default: 6pt, Loose: 10-12pt, Compact: 4-6pt
- **Trade-off**: Wider = easier to read, Narrower = fits more content

#### Page Break Control
```latex
\usepackage{needspace}
\LTchunksize=100
\widowpenalty=10000
\clubpenalty=10000
```

- `needspace`: Ensures minimum space before starting table (prevents orphans at bottom)
- `LTchunksize=100`: Processes more rows before considering page break (default ~20)
- `widowpenalty`/`clubpenalty`: Discourages single lines at top/bottom of pages

### 4. Progressive Refinement Strategy

**Phase 1: Start with moderate spacing** (balance readability and compactness)
```latex
\renewcommand{\arraystretch}{1.2}
\setlength{\extrarowheight}{4pt}
\setlength{\tabcolsep}{10pt}
```

**Phase 2: If tables still break awkwardly, tighten spacing**
```latex
\renewcommand{\arraystretch}{1.0}
\setlength{\extrarowheight}{2pt}
\setlength{\tabcolsep}{6pt}
```

**Phase 3: If still breaking, consider additional measures**
- Reduce font size: `\footnotesize` or `\small` before longtable
- Split table into multiple smaller tables
- Adjust page margins to give more vertical space
- Custom Lua filter (most complex option)

### 5. Testing and Iteration

After each spacing adjustment:

1. **Regenerate PDF**:
   ```bash
   pandoc document.md -o document.pdf --pdf-engine=xelatex -H table-spacing.tex
   ```

2. **Check table placement**: Look for tables breaking across pages

3. **Measure impact**: Compare page count, readability, table density

4. **Iterate**: Adjust parameters based on results

**Important**: Always test with actual content - table breaking depends on:
- Number of rows
- Column widths
- Text length in cells
- Page margins
- Font size

## Trade-offs and Considerations

### Readability vs Compactness

**Looser spacing** (arraystretch 1.2+, extrarowheight 4pt+, tabcolsep 10pt+):
- ✅ More readable (breathing room between rows)
- ✅ Professional appearance
- ❌ Tables may be too tall to fit on single page
- ❌ More likely to break across pages

**Tighter spacing** (arraystretch 1.0, extrarowheight 2pt, tabcolsep 6pt):
- ✅ Tables more compact (fit on single page)
- ✅ Reduced page breaks
- ❌ Denser appearance (less breathing room)
- ❌ May feel cramped if too tight

### When Complete Prevention Isn't Possible

**Reality**: Some tables are legitimately too tall for one page

**Signs**:
- Table has 20+ rows with detailed content
- Even with tightest spacing, table exceeds page height
- Splitting table would break logical grouping

**Options**:
1. **Accept the break**: longtable is designed for this
2. **Split table**: Create two tables with clear headings
3. **Reduce content**: Abbreviate text, remove columns
4. **Landscape orientation**: Use `\usepackage{pdflscape}` for wide tables

## Resources

### references/latex-parameters.md

Comprehensive reference for all LaTeX table spacing parameters, including:
- Detailed parameter explanations
- Visual diagrams of spacing effects
- Default values and recommended ranges
- Interaction between parameters
- Common pitfalls and solutions

### assets/table-spacing-template.tex

Ready-to-use LaTeX preamble templates:
- **Loose spacing**: Maximum readability (arraystretch 1.3, extrarowheight 6pt)
- **Moderate spacing**: Balanced approach (arraystretch 1.2, extrarowheight 4pt)
- **Compact spacing**: Prevent page breaks (arraystretch 1.0, extrarowheight 2pt)
- **Minimal spacing**: Maximum compactness (arraystretch 0.9, extrarowheight 1pt)

## Example Workflow: Fixing Page-Breaking Table

### Problem
"Key Findings" table breaking across pages with awkward single-row orphan at bottom.

### Solution Progression

**Attempt 1: Add page break penalties**
```latex
\usepackage{needspace}
\LTchunksize=100
\widowpenalty=10000
\clubpenalty=10000
```
**Result**: Improved placement but table still breaks (didn't reduce table height)

**Attempt 2: Reduce spacing to make table physically smaller**
```latex
\renewcommand{\arraystretch}{1.0}    % Was 1.2
\setlength{\extrarowheight}{2pt}     % Was 4pt
\setlength{\tabcolsep}{6pt}          % Was 10pt
```
**Result**: ~20-25% reduction in table height → table fits on single page

### Key Insight

**The problem wasn't longtable's breaking behavior** - the table was physically too tall. Penalties and needspace can't change table height, only placement decisions. Making the table more compact through spacing reduction solved the root cause.
