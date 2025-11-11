# PDF Bullet Rendering Failure - Root Cause Analysis

## Problem Statement

In the generated PDF `01-technical-competencies.pdf`, bullet lists were rendering as inline text with dashes instead of proper bullets (•):

**Bad Rendering:**

```
Multi-layer validation frameworks for production data pipelines: - HTTP/API layer validation (status codes, rate limits,
authentication) - Schema validation (Pydantic, type checking) - Sanity checks...
```

**Expected Rendering:**

```
Multi-layer validation frameworks for production data pipelines:
• HTTP/API layer validation (status codes, rate limits, authentication)
• Schema validation (Pydantic, type checking)
• Sanity checks (database constraints, business rule validation)
```

## Root Cause

**LaTeX's justified text alignment** (default behavior) was causing Pandoc-generated bullet lists to render incorrectly when converting markdown to PDF via XeLaTeX.

### Technical Details

**Old LaTeX Preamble** (table-spacing.tex):

- Used default LaTeX text alignment (justified)
- No `\raggedright` directive
- Lists were sometimes collapsed into inline text by the justification algorithm

**New LaTeX Preamble** (table-spacing-template.tex):

- Added `\raggedright` command (lines 89-90)
- Switches from justified to left-aligned (ragged-right) text
- Preserves bullet list formatting correctly

### Why Justified Text Breaks Lists

LaTeX's justification algorithm tries to make every line the same width by:

1. Adding/removing inter-word spaces
2. Hyphenating words
3. Sometimes **reflow line breaks** in ways that break Pandoc's list structures

When a list appears after a paragraph ending with a colon (common pattern), the justification algorithm may:

- Merge list items onto previous lines
- Convert bullet markers (`-`) into inline dashes
- Collapse vertical list structure into horizontal flow

**The `\raggedright` command disables justification**, allowing lists to preserve their intended structure.

## Why Test Case Worked But Main Document Failed

### Test Document (test-bullets.md)

- Built with NEW LaTeX preamble (table-spacing-template.tex)
- Included `\raggedright` directive
- Bullets rendered correctly (•)

### Main Document (01-technical-competencies.md) - Old Build

- Built with OLD LaTeX preamble (table-spacing.tex)
- Missing `\raggedright` directive
- Bullets collapsed into inline text

### Main Document - New Build (After Fix)

- Rebuilt with NEW LaTeX preamble (table-spacing-template.tex)
- Includes `\raggedright` directive
- Bullets render correctly (•)
- Page count increased from 7 to 8 (ragged-right uses slightly more vertical space)

## Prevention Measures

### 1. LaTeX Preamble - Robust Configuration

**ALWAYS include `\raggedright` in LaTeX preambles for Pandoc PDF generation:**

```latex
% ==============================================================================
% Text Alignment
% ==============================================================================
% Use ragged-right (left-aligned) instead of justified text
% Justified text can create awkward spacing and break list structures
\raggedright
```

**Location:**

- `~/.claude/skills/pandoc-pdf-generation/assets/table-spacing-template.tex` (canonical version)
- Any project-specific LaTeX preambles

### 2. Markdown Linting - Optional Patterns

While `\raggedright` solves the problem at the LaTeX level, these markdown patterns reduce risk:

**Robust Pattern (Already Used):**

```markdown
**Multi-layer validation frameworks** for production data pipelines:

- HTTP/API layer validation (status codes, rate limits, authentication)
- Schema validation (Pydantic, type checking)
```

**Even More Robust (Bold Items):**

```markdown
Created workflow automation systems that:

- **Eliminate Manual Data Entry**: Bulk operations
- **API Orchestration**: Coordinating services
```

However, with `\raggedright` enabled, both patterns work correctly - no markdown linting required.

### 3. Build Script Verification

**Always use canonical build script:**

```bash
~/.claude/skills/pandoc-pdf-generation/assets/build-pdf.sh
```

**Symlink in project directories:**

```bash
cd /project/directory
ln -s ~/.claude/skills/pandoc-pdf-generation/assets/build-pdf.sh build-pdf.sh
```

**Never create ad-hoc build scripts** - they may use outdated LaTeX preambles.

### 4. Post-Generation Verification

**Automated check for broken bullets:**

```bash
pdftotext output.pdf - | grep -E '^\w.*: -'
```

Expected: 0 matches (if matches found, lists may be rendering inline)

**Manual visual inspection:**

- Open PDF in viewer
- Scan for sections with bullet lists
- Verify bullets (•) appear, not inline dashes

### 5. Skills Documentation Updates

Update all PDF generation skills to document this issue:

1. **`~/.claude/skills/pandoc-pdf-generation/references/document-patterns.md`**
   - Add warning about justified text breaking lists
   - Document `\raggedright` as required practice

2. **`netstrata/.claude/skills/pdf-generation-verification/SKILL.md`**
   - Add verification step checking for inline dashes

3. **`netstrata/.claude/skills/pdf-generation-verification/references/pdf-best-practices.md`**
   - Add LaTeX preamble requirement

## Summary

**Root Cause:** LaTeX's justified text alignment breaks Pandoc-generated bullet lists

**Solution:** Use `\raggedright` in LaTeX preamble (ragged-right/left-aligned text)

**Prevention:**

1. Always use canonical build script with updated LaTeX preamble
2. Include `\raggedright` in all LaTeX preambles for Pandoc
3. Verify PDFs after generation (visual + automated checks)

**No Markdown Changes Required:** With proper LaTeX configuration, all markdown list patterns work correctly.
