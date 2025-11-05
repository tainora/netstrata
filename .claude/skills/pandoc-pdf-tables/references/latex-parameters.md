# LaTeX Table Spacing Parameters - Comprehensive Reference

This document provides detailed explanations of all LaTeX table spacing parameters used for controlling table appearance and page break behavior in Pandoc-generated PDFs.

## Table of Contents

1. [Row Spacing Parameters](#row-spacing-parameters)
2. [Cell Padding Parameters](#cell-padding-parameters)
3. [Column Spacing Parameters](#column-spacing-parameters)
4. [Page Break Control](#page-break-control)
5. [Table Margins](#table-margins)
6. [Rule Thickness](#rule-thickness)
7. [Parameter Interactions](#parameter-interactions)
8. [Common Pitfalls](#common-pitfalls)

---

## Row Spacing Parameters

### `\arraystretch`

**Purpose**: Controls vertical spacing between rows in tables (multiplier on normal line height)

**Syntax**:
```latex
\renewcommand{\arraystretch}{value}
```

**Default**: 1.0

**Recommended ranges**:
- **Loose** (1.3-1.5): Maximum readability, generous breathing room
- **Moderate** (1.1-1.2): Balanced readability and compactness
- **Standard** (1.0): Default LaTeX spacing
- **Compact** (0.9): Tight spacing to fit more rows

**Effect on table height**:
- 1.0 → 1.2: +20% taller
- 1.2 → 1.0: -17% shorter
- 1.0 → 0.9: -10% shorter

**Visual example**:
```
arraystretch=1.5               arraystretch=1.0
┌────────┬────────┐           ┌────────┬────────┐
│ Cell 1 │ Cell 2 │           │ Cell 1 │ Cell 2 │
│        │        │           ├────────┼────────┤
├────────┼────────┤           │ Cell 3 │ Cell 4 │
│ Cell 3 │ Cell 4 │           └────────┴────────┘
│        │        │
└────────┴────────┘
(More breathing room)          (More compact)
```

**Trade-offs**:
- ✅ Higher values: More readable, professional appearance
- ❌ Higher values: Taller tables, more likely to break
- ✅ Lower values: Compact tables fit on single page
- ❌ Lower values: Dense appearance, harder to scan

**Common mistake**: Setting too low (< 0.9) makes tables cramped and hard to read

---

## Cell Padding Parameters

### `\extrarowheight`

**Purpose**: Adds extra padding at the **top** of cells (does not affect bottom)

**Syntax**:
```latex
\setlength{\extrarowheight}{value}
```

**Default**: 0pt

**Recommended ranges**:
- **Loose** (6-8pt): Generous padding, clean look
- **Moderate** (4pt): Balanced padding
- **Compact** (2pt): Minimal padding
- **Minimal** (0pt): No extra padding

**Effect on table height**:
- 0pt → 4pt: +4pt per row
- 4pt → 2pt: -2pt per row
- For 10-row table: 4pt → 2pt saves 20pt total

**Visual cross-section**:
```
extrarowheight=6pt     extrarowheight=0pt
┌───────────────┐      ┌───────────────┐
│               │      │Text starts    │
│               │      │immediately    │
│Text starts    │      └───────────────┘
│here           │
└───────────────┘
```

**Trade-offs**:
- ✅ Higher values: Cleaner appearance, text doesn't touch top border
- ❌ Higher values: Taller table cells
- ✅ Lower values: Compact tables
- ❌ Lower values: Text may feel cramped near top border

**Interaction with arraystretch**: These work together - arraystretch affects total row height, extrarowheight shifts content down within that height

---

## Column Spacing Parameters

### `\tabcolsep`

**Purpose**: Horizontal padding on **both sides** of each column (total spacing = 2 × tabcolsep)

**Syntax**:
```latex
\setlength{\tabcolsep}{value}
```

**Default**: 6pt

**Recommended ranges**:
- **Loose** (10-12pt): Wide spacing, generous margins
- **Moderate** (8pt): Balanced spacing
- **Standard** (6pt): Default LaTeX spacing
- **Compact** (4-5pt): Tight spacing

**Effect on table width**:
- For 3-column table: Each column has 2 × tabcolsep padding
- 6pt → 10pt: +8pt per column = +24pt total width
- 10pt → 6pt: -8pt per column = -24pt total width

**Visual example**:
```
tabcolsep=12pt                tabcolsep=4pt
┌──────────┬──────────┐      ┌─────┬─────┐
│   Col1   │   Col2   │      │Col1 │Col2 │
└──────────┴──────────┘      └─────┴─────┘
(More breathing room)         (More compact)
```

**Trade-offs**:
- ✅ Higher values: Easier to distinguish columns, professional look
- ❌ Higher values: Wider tables, may not fit page width
- ✅ Lower values: Narrower tables, more content fits
- ❌ Lower values: Columns may feel cramped

**Common mistake**: Going too low (< 4pt) makes columns run together visually

---

## Page Break Control

### `\usepackage{needspace}`

**Purpose**: Ensures minimum vertical space available before starting a table

**Syntax**:
```latex
\usepackage{needspace}
```

**Behavior**:
- If insufficient space at current page position, starts table on new page
- Prevents awkward single-row orphans at bottom of page
- Works automatically - no manual intervention needed

**Example scenario**:
```
Without needspace:          With needspace:
Page 1:                    Page 1:
[content]                  [content]
[content]                  [content]
┌────────┬────────┐        [content]
│Row 1   │Data    │
└────────┴────────┘        Page 2:
Page 2:                    ┌────────┬────────┐
┌────────┬────────┐        │Row 1   │Data    │
│Row 2   │Data    │        ├────────┼────────┤
├────────┼────────┤        │Row 2   │Data    │
│Row 3   │Data    │        ├────────┼────────┤
└────────┴────────┘        │Row 3   │Data    │
                           └────────┴────────┘
(Orphan row at bottom)     (Clean placement)
```

---

### `\LTchunksize`

**Purpose**: Number of rows processed together before considering a page break

**Syntax**:
```latex
\LTchunksize=value
```

**Default**: Typically 20

**Recommended values**:
- **Standard** (20): Default LaTeX behavior
- **Higher** (50-100): Encourages keeping tables together
- **Very high** (500+): Almost never breaks mid-table

**Effect**:
- Higher values = LaTeX processes more rows before considering page break
- Makes LaTeX "try harder" to keep tables on one page
- Not a guarantee - if table genuinely too tall, will still break

**Trade-off**:
- ✅ Higher: Fewer awkward breaks, better table continuity
- ❌ Higher: May create very unbalanced pages (large white space)

---

### `\widowpenalty` and `\clubpenalty`

**Purpose**: Discourage orphaned lines at top/bottom of pages

**Syntax**:
```latex
\widowpenalty=10000
\clubpenalty=10000
```

**Definitions**:
- **Widow**: Single line at **top** of page from previous paragraph
- **Club (Orphan)**: Single line at **bottom** of page from next paragraph

**Penalty scale**:
- 0 = No penalty (breaks freely)
- 150 = Default LaTeX penalty (slight discouragement)
- 10000 = Infinite penalty (avoid at all costs)

**Effect on tables**:
- Discourages page breaks that would leave single rows isolated
- Works with needspace and LTchunksize for better table placement
- Applies to text around tables as well

**Example**:
```
widowpenalty=0              widowpenalty=10000
Page 1:                     Page 1:
[paragraph]                 [paragraph]
[paragraph]                 [paragraph]
Last line of paragraph      [moved to next page]

Page 2:                     Page 2:
┌────────┬────────┐         Last line of paragraph
│Table   │Data    │         ┌────────┬────────┐
└────────┴────────┘         │Table   │Data    │
                            └────────┴────────┘
(Widow at bottom)           (Clean page break)
```

---

## Table Margins

### `\LTpre` and `\LTpost`

**Purpose**: Vertical space before and after entire table

**Syntax**:
```latex
\setlength{\LTpre}{value}   % Before table
\setlength{\LTpost}{value}  % After table
```

**Default**: Variable (typically 6-12pt)

**Recommended ranges**:
- **Loose** (12-16pt): Clear separation from surrounding text
- **Moderate** (8-12pt): Balanced spacing
- **Compact** (6-8pt): Tight integration with text

**Visual example**:
```
LTpre=16pt, LTpost=16pt     LTpre=6pt, LTpost=6pt
[paragraph text]            [paragraph text]
                            ┌────────┬────────┐
                            │Table   │Data    │
┌────────┬────────┐         └────────┴────────┘
│Table   │Data    │         [paragraph text]
└────────┴────────┘

[paragraph text]
(More separation)            (More compact)
```

**Trade-offs**:
- ✅ Higher values: Tables stand out, clear visual hierarchy
- ❌ Higher values: More vertical space consumed
- ✅ Lower values: Compact documents, more content per page
- ❌ Lower values: Tables may blend into text

---

### `\LTcapwidth`

**Purpose**: Width of table caption

**Syntax**:
```latex
\setlength{\LTcapwidth}{\textwidth}
```

**Recommended**: Set to `\textwidth` to ensure captions stay with table content

**Effect**: Prevents caption on one page and table on next page

---

## Rule Thickness

### `\heavyrulewidth`, `\lightrulewidth`, `\cmidrulewidth`

**Purpose**: Control thickness of table borders (requires `booktabs` package)

**Syntax**:
```latex
\setlength{\heavyrulewidth}{1.0pt}    % Top and bottom rules
\setlength{\lightrulewidth}{0.4pt}    % Middle rules
\setlength{\cmidrulewidth}{0.4pt}     % Partial horizontal rules
```

**Recommended values**:
- **Heavy rules** (top/bottom): 0.8-1.2pt
- **Light rules** (middle): 0.3-0.5pt
- **Ratio**: Heavy should be 2-3× thicker than light

**Trade-off**:
- ✅ Thicker rules: Clearer visual separation
- ❌ Thicker rules: Heavier appearance, more ink

**booktabs philosophy**: Minimal vertical lines, strong horizontal rules for clean professional tables

---

## Parameter Interactions

### How Parameters Work Together

**Height of single table row** =
```
(font size) × (arraystretch) + (extrarowheight) + (rule thickness)
```

**Total table height** =
```
(number of rows) × (row height) + LTpre + LTpost
```

**Total table width** =
```
(sum of column widths) + (number of columns) × 2 × (tabcolsep)
```

### Combined Effects Example

**Loose configuration**:
```latex
\renewcommand{\arraystretch}{1.3}
\setlength{\extrarowheight}{6pt}
\setlength{\tabcolsep}{12pt}
```
**Effect**: +30% row height, +6pt per row, +6pt per column side
**10-row, 3-column table**: ~40% taller, ~30% wider

**Compact configuration**:
```latex
\renewcommand{\arraystretch}{1.0}
\setlength{\extrarowheight}{2pt}
\setlength{\tabcolsep}{6pt}
```
**Effect**: Standard row height, +2pt per row, +6pt per column side (default)
**10-row, 3-column table**: Baseline dimensions

**Reduction from loose → compact**: ~25-30% shorter, ~15% narrower

---

## Common Pitfalls

### 1. Expecting Penalties to Reduce Table Height

**Mistake**:
```latex
\LTchunksize=100
\widowpenalty=10000
% Expecting: table will fit on one page
```

**Reality**: These parameters only affect page break **decisions**, not table **size**

**Solution**: Reduce spacing parameters to actually make table smaller

---

### 2. Going Too Compact

**Mistake**:
```latex
\renewcommand{\arraystretch}{0.7}  % Too tight!
\setlength{\extrarowheight}{0pt}
\setlength{\tabcolsep}{2pt}
```

**Problem**: Table becomes unreadable, cramped appearance

**Solution**: Stay within reasonable ranges (arraystretch ≥ 0.9, tabcolsep ≥ 4pt)

---

### 3. Inconsistent Column Spacing

**Mistake**:
```latex
\setlength{\tabcolsep}{3pt}  % 6pt total per column
% But wide column margins elsewhere create visual inconsistency
```

**Problem**: Tables look inconsistent with rest of document

**Solution**: Maintain consistent spacing across all tables in document

---

### 4. Forgetting booktabs Package

**Mistake**:
```latex
\setlength{\heavyrulewidth}{1.0pt}
% Error: \heavyrulewidth undefined
```

**Solution**: Always include `\usepackage{booktabs}` before setting rule widths

---

### 5. Not Testing with Real Content

**Mistake**: Assuming parameter changes will work without regenerating PDF

**Solution**: Always test with actual document content - table breaking depends on:
- Number of rows
- Text length in cells
- Column widths
- Overall page layout

---

## Quick Reference Table

| Parameter | Default | Loose | Moderate | Compact | Minimal |
|-----------|---------|-------|----------|---------|---------|
| **arraystretch** | 1.0 | 1.3-1.5 | 1.1-1.2 | 1.0 | 0.9 |
| **extrarowheight** | 0pt | 6-8pt | 4pt | 2pt | 0pt |
| **tabcolsep** | 6pt | 10-12pt | 8pt | 6pt | 4pt |
| **LTchunksize** | 20 | 50 | 75 | 100 | 200+ |
| **widow/club penalty** | 150 | 10000 | 10000 | 10000 | 10000 |
| **LTpre/LTpost** | 6pt | 12-16pt | 8-12pt | 6-8pt | 4pt |

---

## Progressive Tuning Strategy

1. **Start moderate** (arraystretch=1.2, extrarowheight=4pt, tabcolsep=10pt)
2. **Add page break control** (needspace, LTchunksize=100, penalties=10000)
3. **If still breaking**, tighten spacing incrementally:
   - arraystretch 1.2 → 1.0 (-17% height)
   - extrarowheight 4pt → 2pt (-2pt per row)
   - tabcolsep 10pt → 6pt (-4pt per column)
4. **If still breaking**, consider:
   - Font size reduction (`\footnotesize`)
   - Splitting table
   - Adjusting margins
5. **Always verify readability** after each change
