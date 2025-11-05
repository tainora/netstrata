# Pandoc PDF Tables Skill

## Summary

This skill captures the sophisticated PDF formatting and LaTeX table spacing techniques developed through v1.0.5 and v1.0.6 of the Netstrata strategic proposal project.

**Created**: 2025-11-04
**Location**: `/Users/terryli/own/netstrata/.claude/skills/pandoc-pdf-tables/`

## What This Skill Provides

### Core Knowledge
- Professional PDF generation from Markdown using Pandoc with XeLaTeX
- LaTeX table spacing parameter control to prevent awkward page breaks
- Progressive refinement strategy (moderate → compact spacing)
- Trade-offs between readability and compactness

### Key Insights Captured
1. **longtable design**: Pandoc uses longtable by default, which is designed to break across pages for multi-page tables
2. **Height reduction approach**: Penalties and needspace don't reduce table height - only spacing parameter adjustments do
3. **Progressive tuning**: Start moderate (arraystretch 1.2), tighten to compact (arraystretch 1.0) if needed
4. **Combined effects**: arraystretch, extrarowheight, and tabcolsep work together for 20-25% height reduction

### Real-World Example
The "Key Findings from Comprehensive Analysis" table was breaking across pages in v1.0.5 despite needspace and penalties. Reducing spacing parameters in v1.0.6 made the table 20-25% shorter, allowing it to fit on a single page.

## Skill Structure

```
pandoc-pdf-tables/
├── SKILL.md                           # Main skill documentation (workflow, usage)
├── references/
│   └── latex-parameters.md            # Comprehensive LaTeX parameter reference
└── assets/
    ├── table-spacing-template.tex     # Ready-to-use LaTeX preamble templates
    └── build-pdf-example.sh           # Example Pandoc build script
```

### SKILL.md
- **When to use**: Generating PDFs with tables that break awkwardly
- **Core workflow**: 5-step process from basic generation to progressive refinement
- **Trade-offs**: Readability vs compactness explained
- **Example**: Real-world problem/solution from this project

### references/latex-parameters.md (9,000+ words)
- **Comprehensive reference**: All LaTeX parameters with visual examples
- **Parameter interactions**: How arraystretch, extrarowheight, tabcolsep work together
- **Common pitfalls**: 5 common mistakes and solutions
- **Quick reference table**: Parameter ranges (loose, moderate, compact, minimal)
- **Progressive tuning strategy**: Step-by-step refinement process

### assets/table-spacing-template.tex
Ready-to-use LaTeX preamble with 4 configurations:
1. **COMPACT** (default): Prevents page breaks, ~20-25% reduction
2. **MODERATE**: Balanced readability and compactness
3. **LOOSE**: Maximum readability, may break across pages
4. **MINIMAL**: Maximum compactness for very large tables

### assets/build-pdf-example.sh
Example Pandoc build script demonstrating:
- XeLaTeX engine usage
- Custom font specification
- LaTeX preamble inclusion with `-H` flag
- Optional landscape orientation

## How Claude Code Will Use This Skill

When a user mentions:
- "PDF generation from Markdown"
- "Tables breaking across pages"
- "LaTeX table spacing"
- "Pandoc PDF formatting"

Claude Code will automatically load this skill and use:
1. **SKILL.md** for workflow guidance
2. **references/latex-parameters.md** for detailed parameter explanations
3. **assets/** files as templates to copy and customize

## Skill Metadata

**Name**: `pandoc-pdf-tables`

**Description**:
> Generate professional PDFs from Markdown using Pandoc with sophisticated LaTeX table spacing control to prevent awkward page breaks. Use when creating PDFs with tables that need to stay on single pages, or when fine-tuning table appearance for readability and professional formatting.

## Evolution of This Knowledge

### Version History
- **v1.0.5**: Attempted needspace package and penalties (didn't reduce table height)
- **v1.0.6**: Reduced spacing parameters for 20-25% height reduction (successful)

### Key Learning
The critical insight was understanding that **penalties control page break decisions, not table dimensions**. To actually make tables fit on one page, you must reduce the physical size through spacing parameters, not just discourage breaks.

## Validation Checklist

✅ **SKILL.md requirements**:
- [x] YAML frontmatter with name and description
- [x] Clear "When to Use" section
- [x] Step-by-step workflow
- [x] References to bundled resources
- [x] Real-world example

✅ **Bundled resources**:
- [x] references/ - Comprehensive LaTeX parameter documentation
- [x] assets/ - Ready-to-use templates and examples
- [x] No scripts/ directory (not needed for this skill)

✅ **Documentation quality**:
- [x] Progressive disclosure (SKILL.md lean, references/ detailed)
- [x] Imperative/infinitive writing style
- [x] Concrete examples with visual diagrams
- [x] Trade-offs and pitfalls explained

## Testing Recommendations

To verify this skill works in practice:

1. **Test trigger**: Ask Claude Code "How do I prevent tables from breaking across pages in Pandoc PDFs?"
2. **Expected behavior**: Claude loads this skill and references table-spacing parameters
3. **Verify**: Claude suggests starting with moderate spacing, then tightening if needed
4. **Verify**: Claude references assets/table-spacing-template.tex for ready-to-use code

## Future Enhancements

Potential additions if users report needing them:
- Font size reduction techniques (`\footnotesize`, `\small`)
- Custom Pandoc Lua filters for forcing tabular instead of longtable
- Landscape page orientation examples
- Multi-page table handling with headers on each page
- Table splitting strategies
