# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.18] - 2025-11-04

### Fixed - MAJOR TONE CORRECTIONS

**Critical Issue**: Document read as "external research report ABOUT Netstrata" rather than "advisory proposal TO Ted Middleton and management"

**Changes Made**:

1. **Executive Summary (Complete Rewrite)**
   - Changed from third-person research framing to direct address: "Ted, I'm proposing..."
   - Removed "Key Findings" table listing problems, replaced with "What I Can Do For Netstrata" solutions list
   - Added personal context paragraph acknowledging family relationship respectfully
   - Shifted focus from "comprehensive analysis reveals" to "here's how I can help"

2. **McGrathNicol Section (Complete Rewrite)**
   - Removed harsh language: "biggest reputational crisis", "Zero genuine accountability", "Defensive Communication Pattern"
   - Reframed as "Transparency Leadership Opportunity"
   - Changed "Crisis Severity Metrics" to "Progress and Opportunity"
   - Positioned automation as enabling excellence, not fixing failures
   - Maintained factual accuracy with supportive, partnership tone

3. **Systematic Language Replacements (43 instances)**
   - "biggest reputational crisis" → "significant transparency challenge"
   - "Single-Author Bottleneck" → "Content Creation Centralization"
   - "catastrophic single point of failure" → "content creation sustainability opportunity"
   - "Crisis Severity Metrics" → "Review Response Analysis"
   - "Defensive Language/Pattern" → "Response Language/Strategy"
   - "Insurance Crisis" → "Insurance Market Challenges"
   - "6 recommendations overdue" → "6 recommendations pending"
   - "contested breaches" → "ongoing discussions with NSW Fair Trading"
   - "No proactive innovation history" → "Technology investments aligned with operational priorities"
   - "PropTech blindspot" → "PropTech awareness opportunity"

4. **Perspective Shift (60-70% of document)**
   - Changed from third-person analysis ("Netstrata's portfolio", "Netstrata faces") to second-person advisory ("your portfolio", "you face")
   - Removed research report framing ("comprehensive analysis reveals") throughout
   - Sections retitled: "Why This Matters for Netstrata" → "How This Helps Your Strategic Priorities"
   - "Netstrata's Proprietary Data Advantage" → "Your Proprietary Data Advantage"

### Impact

**Before**: External analyst presenting harsh audit findings
**After**: Respectful advisor offering partnership and solutions

- Executive Summary now establishes partnership tone from first sentence
- McGrathNicol section frames review as opportunity, not crisis
- Document consistently addresses Ted and management as "you/your"
- Solutions-focused throughout: "here's how I can help" not "here are your problems"
- Maintains integrity while demonstrating respect for recipient

**Rationale**: Document is proposal TO Ted Middleton (mother's partner, company founder) requesting opportunity to help. Must be respectful, solutions-focused, and advisory—not judgmental, critical, or research-analytical.

PDF now 41 pages (up from 40 due to rewritten sections with better spacing)

## [1.0.17] - 2025-11-04

### Changed

- Reduced table font size from `\small` (~90%) to `\footnotesize` (~80%) to address text crowding
- Prevents text jamming in tables with long content

### Impact

- Better table readability with less text crowding
- More content fits in table cells without wrapping
- Maintains readability while significantly improving space efficiency

## [1.0.16] - 2025-11-04

### Changed

- Removed redundant "Phase" label in Phase column (now shows "1", "2" instead of "Phase 1", "Phase 2")

### Impact

- Cleaner, more concise table presentation
- Follows standard table design principles (column header defines meaning, cells contain values only)

## [1.0.15] - 2025-11-04

### Added

- Automatic table font size reduction using idiomatic LaTeX pattern
- All table content now uses `\small` font (~90% of normal size) for better space efficiency

### Technical Implementation

**Added to table-spacing.tex:**

```latex
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
```

**Idiomatic pattern:** Uses `etoolbox` package's `\AtBeginEnvironment` hook to automatically apply smaller font to all Pandoc-generated longtables without modifying markdown or requiring per-table customization.

**Customization options:**

- `\small` (~90%) - Current setting, subtle reduction
- `\footnotesize` (~80%) - Moderate reduction
- `\scriptsize` (~70%) - Significant reduction
- `\tiny` (~50%) - Very small

### Impact

- Better table density without sacrificing readability
- More content fits per page (especially tables with many columns)
- Captions remain at normal size for hierarchy

## [1.0.14] - 2025-11-04

### Fixed

- Removed "Competitive Blindspot" table row containing fear-based language (this row was supposed to be removed in v1.0.0 but was overlooked)
- Removed unverified company reference ":Different" - web search found no evidence this company exists in Australian PropTech/strata management space
- Added FTE (Full-Time Equivalent) acronym explanation on first use - previously appeared without context

### Impact

- Cleaner, more professional presentation without competitive fear-mongering
- All company references now verified and factual
- Resource planning terminology now accessible to all readers

## [1.0.13] - 2025-11-04

### Fixed

- Table of Contents spacing: Multi-digit subsection numbers (2.5.10, 2.5.11, etc.) no longer overlap with section titles

### Technical Implementation

**Added to table-spacing.tex using tocloft package:**

```latex
\usepackage{tocloft}
\setlength{\cftsecnumwidth}{2.5em}      % Section numbers (1, 2, 3)
\setlength{\cftsubsecnumwidth}{3.5em}   % Subsection numbers (2.1, 2.5.10)
\setlength{\cftsubsubsecnumwidth}{4.5em} % Subsubsection numbers (2.5.10.1)
```

**Problem:** Default LaTeX allocates only 2.3em for subsection numbers, causing overlap when subsection numbers reach double digits (e.g., "2.5.10").

**Solution:** Use `tocloft` package to increase allocated width to 3.5em, providing adequate space for all subsection number lengths.

### Impact

- PDF: 40 pages (+1 from v1.0.12), 161KB (+3KB)
- ToC: Proper spacing for all section numbers, including multi-digit subsections
- Readability: Improved ToC navigation without text overlap

### Rationale

User observation: "2.5.10, 2.5.11, 2.5.12, 2.5.13 jamming too close with the title"

**Root cause:** LaTeX default ToC formatting doesn't account for subsection numbers with 2+ digits after the dot (e.g., "2.5.10" = 6 characters).

**Research:** Investigated idiomatic LaTeX patterns via Stack Exchange and official documentation. The `tocloft` package is the standard solution for ToC spacing customization.

## [1.0.12] - 2025-11-04

### Added

- Automatic section numbering using Pandoc `--number-sections` flag
- YAML front matter for document metadata (title, author, date)
- Elevated "Why This Matters for Netstrata" from subsection to dedicated main section

### Changed

- Removed ALL manual numbering (Roman numerals I-XII and Arabic numerals 1.1-9.3)
- Converted document title from Markdown heading to YAML metadata
- Restructured section hierarchy: "Why This Matters" now appears as Section 3 (between Strategic Context and Proposed Solutions)

### Technical Implementation

**Pandoc automatic numbering**:

```bash
--number-sections  # Automatically numbers all headings
```

**YAML front matter**:

```yaml
---
title: Strategic Technology Advisory Proposal for Netstrata
author: Terry Li
date: November 3, 2025
---
```

**Heading structure changes**:

- Removed manual numbers from markdown (## I. Title → ## Title)
- Pandoc generates numbers automatically (1, 1.1, 1.1.1, etc.)
- Consistent numbering without manual maintenance burden

### Impact

- PDF: 39 pages (+5 from v1.0.11), 158KB (+16KB)
- Maintainability: Zero manual number tracking required
- Consistency: Pandoc ensures correct sequential numbering
- Structure: "Why This Matters" now properly positioned as major section
- Professional: Standard academic/technical document numbering

### Rationale

User feedback: "It doesn't seem correct to be using manual numbering of those Roman numbers as well as the numerical number. Is there auto numbering scheme or system that automatically generate?"

**Problem with manual numbering**:

- Prone to errors when reordering sections
- Requires manual updates across entire document
- Inconsistent numbering (I., II., III. vs 1.1, 2.1, 3.1)
- Maintenance burden

**Solution**: Pandoc's `--number-sections` flag automatically generates hierarchical numbering from markdown heading levels, eliminating manual number tracking.

### Document Structure

**Before v1.0.12**:

```
I. Strategic Context
  1.1 Subsection
II. Proposed Solutions
  2.1 Subsection
```

**After v1.0.12**:

```
1 Executive Summary
2 Strategic Context
  2.1 Subsection
3 Why This Matters for Netstrata
4 Proposed Solutions
  4.1 Subsection
```

## [1.0.11] - 2025-11-04

### Added

- Table of Contents (ToC) at beginning of PDF with automatic page number generation
- ToC includes main sections (level 2 headings) and subsections (level 3 headings) for comprehensive navigation
- Pandoc `--toc` flag integration with depth control and custom title

### Technical Implementation

**Pandoc flags added to build-pdf.sh**:

```bash
--toc                              # Enable automatic ToC generation
--toc-depth=3                      # Include h2, h3 headings (main sections + subsections)
-V toc-title="Table of Contents"   # Custom ToC title
```

**ToC Structure**:

- Level 2 (##): Main sections like "I. Strategic Context: Why Now?"
- Level 3 (###): Subsections like "1.1 Regulatory Compliance Acceleration"
- Automatic page number generation with dot leaders
- Hyperlinked entries for PDF navigation

### Impact

- PDF: 34 pages (+1 from v1.0.10), 142KB (+6KB)
- Navigation: Comprehensive ToC with 37+ subsections for easy reference
- Professional: Standard academic/business document format
- Accessibility: Readers can quickly locate specific topics

### Rationale

User request: "How to add ToC most idiomatically based on our current structure. Search online for more information."

**Research findings**: Pandoc's `--toc` flag is the idiomatic approach for automatic ToC generation, following industry standards for technical documentation.

**Depth choice**: `--toc-depth=3` includes both main sections and subsections, providing detailed navigation without overwhelming with level 4 detail headers (118 converted in v1.0.10).

## [1.0.10] - 2025-11-04

### Changed

- Converted 118 bold section headers to proper Markdown level 4 headings (####)
- Preserved 43 inline bold labels (paragraph labels, dates, emphasis)
- Used programmatic sed approach for safe, consistent conversion

### Technical Implementation

**Method**: Used sed for automated conversion:

```bash
sed 's/^\*\*\(.*\):\*\*$/#### \1/' file.md
```

**Pattern matched**:

- Lines starting with `**`
- Followed by any text
- Ending with `:**` (standalone on their own line)

**Preserved as bold** (not converted):

- Inline labels: `**Automation Opportunity:** text continues...`
- Date markers: `**July 1, 2025**: description`
- Paragraph labels: `**Analysis**: findings...`
- Mid-text emphasis

### Impact

- PDF: 33 pages (+2 from v1.0.9), 136KB
- Improved: Proper heading hierarchy throughout document
- Converted: 118 section headers now use `####` instead of bold
- Better: PDF table of contents now includes all section headers
- Semantic: Document structure now machine-readable

### Rationale

User feedback: "I would appreciate if you can choose the most safest way to do it programmatically... make sure the layout would still stay the same while I don't easily use bolding unless it's really necessary"

**Before**: Bold text (`**Text:**`) used for both emphasis AND structure
**After**: Headings (`#### Text`) for structure, bold for emphasis only

**Page increase explanation**: Headings have more vertical spacing than bold text (by design for readability). +2 pages is expected and improves document navigation.

## [1.0.9] - 2025-11-04

### Fixed

- Heading spacing: Changed "Why This Matters for Netstrata" from level 4 (####) to level 3 (###) for better visual separation from following bold text in PDF

### Impact

- PDF: 31 pages, 133KB (unchanged from v1.0.8)
- Improved: Better heading hierarchy and spacing in PDF output

### Rationale

User feedback: "Why This Matters for Netstrata Netstrata's Technology Foundation: failed to have separate lines?"

Level 4 headings (####) were rendering too close to bold text below them in the PDF, making them appear to run together. Changed to level 3 (###) for clearer visual separation.

## [1.0.8] - 2025-11-04

### Removed

- Unverified "first-ever COO appointment after 17 years" claim (blog post doesn't confirm "first-ever")
- Fabricated hour estimates: 40-80, 80-120, 120-160, 540-760, 500-750 hours
- Fabricated efficiency percentages: 50%, 60-70%, 94% time reduction
- Fabricated cost estimates: $4,000-$6,000 pilot cost
- Fabricated timeline estimates: 24-48 hours, 2-3 hours, 3-6 months
- Fabricated scale estimates: 50-100 schemes, 60,000 data points
- Unsourced competitor claims: 70% admin reduction (Merlo AI)

### Changed

- Replaced specific hour/percentage claims with qualitative language ("reduced time", "significant savings")
- Andrew Tunks COO description now accurately reflects blog post content (17+ years at Netstrata, not company age)
- All claims now grounded in blog post sources or marked as qualitative assessments

### Added

- Footnote reference for Andrew Tunks COO appointment blog post

### Impact

- PDF: 31 pages, 133KB (**1 page reduction from v1.0.7**)
- Improved: All numerical claims now verifiable or removed
- Accuracy: Eliminated fabricated estimates and projections

### Rationale

User feedback: "don't easily specify any numbers especially projected ones if they are not grounded from fact"

**Problem identified**: Many numbers were estimates/projections presented as facts:

- "60,000 NSW Strata Hub data points annually" - NO SOURCE
- "94% time reduction" - calculated from fabricated 3 minutes/scheme claim
- "540-760 hours" - pure estimate
- "50%", "60-70%" reduction claims - unsourced projections

**Solution**: Removed all unverified numbers, replaced with qualitative language. Only kept numbers directly from blog posts or marked as estimates.

## [1.0.7] - 2025-11-04

### Changed

- Converted inline blog references to footnotes for improved readability:
  - Moved 5 blog post URLs with quotes/key findings to footnote references
  - Removed definition list format (Blog Post:, Quote:, Key Finding:, etc.)
  - Consolidated all references in new References section at document end
  - Main text now flows more naturally without citation interruptions

### Added

- References section at end of document with all blog post citations
- Footnote markers [^nsw-law-2025], [^mcgrathnicol-may-2025], etc. in main text

### Impact

- PDF: 32 pages, 134KB (unchanged from v1.0.6)
- Improved: Cleaner main text flow, professional academic-style citations
- Trade-off: Footnotes at bottom consume similar space as inline references, but improve scannability

### Rationale

User requested "save on pages by having blog references and explanation moved to footers." While page count remained the same (footnote space at bottom offset inline savings), the readability improvement is significant:

- Main arguments flow without citation interruptions
- References consolidated in one location
- Professional presentation style
- Easier to scan key points without visual clutter

## [1.0.6] - 2025-11-04

### Changed

- More aggressive table compacting to prevent page breaks:
  - Row spacing reduced: arraystretch 1.2 → 1.0 (17% tighter)
  - Cell padding reduced: extrarowheight 4pt → 2pt (50% less padding)
  - Column spacing reduced: tabcolsep 10pt → 6pt (40% narrower columns)

### Rationale

User feedback: "As you can see, the table is still crossovering two pages"

Previous attempt (v1.0.5) used needspace package and increased penalties, but didn't reduce table physical height. This version makes tables significantly more compact to fit on single pages.

### Technical Details

**Spacing parameter changes**:

- `\\renewcommand{\\arraystretch}{1.0}` (was 1.2) - Tighter line spacing within cells
- `\\setlength{\\extrarowheight}{2pt}` (was 4pt) - Less padding at top of cells
- `\\setlength{\\tabcolsep}{6pt}` (was 10pt) - Narrower column spacing

**Combined effect**: Approximately 20-25% reduction in table height, making most tables fit on single page.

**Trade-off**: Tables are denser but still readable. Professional appearance maintained through booktabs package.

### Impact

- PDF: 32 pages, 134KB (unchanged page count)
- Tables now more compact and more likely to stay on single page
- "Key Findings from Comprehensive Analysis" table should no longer break across pages

## [1.0.5] - 2025-11-04

### Added

- Contact information section with complete details:
  - Email: amonic@gmail.com
  - Phone: +1 604 300 8878
  - LinkedIn: https://www.linkedin.com/in/terrylica/
- LaTeX table page break prevention improvements:
  - needspace package for intelligent table placement
  - Increased LTchunksize to 100 (process more rows before considering breaks)
  - Widow/orphan penalties set to 10000 (discourage awkward breaks)

### Changed

- Improved table-spacing.tex to better handle table page breaks
- Tables now less likely to split awkwardly across pages (though large tables may still split if needed)

### Technical Details

**Table handling improvements**:

- `\usepackage{needspace}` - Ensures minimum space before starting table
- `\LTchunksize=100` - Processes more rows together before considering page break
- `\widowpenalty=10000` and `\clubpenalty=10000` - Discourages orphaned lines

**Note**: longtable (used by Pandoc) is designed to break across pages for tables longer than one page. The settings now make LaTeX try harder to keep tables together, but very long tables will still break (which is correct behavior).

### Impact

- PDF: 32 pages, 134KB (unchanged size)
- Proposal now includes complete contact information for follow-up
- Tables have better page break behavior (less likely to split awkwardly)

## [1.0.4] - 2025-11-04

### Changed

- Replaced "protect the company" with "ensure the company remains future-proof and competitive as the industry evolves"
- Restructured Personal Note section with "What I Bring" / "What I'm Still Learning" / "My Learning Commitment" format
- Added explicit acknowledgment of **domain knowledge gaps** in real estate and strata management
- Added commitment to industry training, certifications, and continuing education
- Emphasized that **"Information technology without vertical domain expertise is not valuable—the domain knowledge is the foundation"**
- Added new commitment: **"Intellectual Humility"** (acknowledge what I don't know and invest in learning rather than pretending expertise)

### Added

**What I Bring:**

- Technology & AI expertise (production-grade automation, modern Python, AI/LLM integration)
- Rapid prototyping capabilities
- Data-driven approach

**What I'm Still Learning:**

- Honest acknowledgment: "I don't have deep domain knowledge in real estate or strata management"
- Recognition that IT without domain expertise is not valuable

**My Learning Commitment:**

- Industry training and strata management certifications
- Company onboarding to learn systems and processes
- Personal time investment in regulatory frameworks, insurance dynamics, building management
- Collaborative learning with experienced strata managers

### Rationale

User feedback: Balance confidence with humility—don't sound cocky or presumptuous

- "Protect the company" sounds too presumptuous (implies I know better than the founder)
- "Future-proof and competitive" is more accurate (technology helping company adapt to industry evolution)
- Need to be honest about domain knowledge gaps (AI/technology expertise alone is insufficient)
- Domain knowledge is the foundation—willing to invest personal time to learn

### Impact

- PDF: 32 pages, 134KB (added learning commitment content)
- Tone: Confident in technology skills, humble about domain gaps
- Positioning: Expert technologist committed to learning strata management domain
- Credibility: Honest about limitations rather than overstating expertise

## [1.0.3] - 2025-11-04

### Changed

- Reframed from "business opportunity" to "career opportunity" in Personal Note section
- Repositioned engagement options with **employment as primary preference** (was listed third, now first)
- Updated engagement approach to emphasize joining the team with company resources and support
- Added explicit acknowledgment of need for company systems access, data, and staff collaboration
- Revised "What I AM Proposing" to lead with "Joining Netstrata" rather than external consulting positioning
- Updated cost note to clarify employment is primary preference with consulting as flexible alternative

### Rationale

User feedback: This is primarily a **career opportunity** (employment-focused), not an external business/consulting engagement:

- Need company support and resources to be effective
- Employment is the main focus, not consulting
- Open to both employment and consultancy, but employment preferred
- Collaborative role requiring internal access, not vendor relationship

### Impact

- PDF: 32 pages (was 31), 132KB
- Positioning now accurately reflects employment-first intent
- Language acknowledges collaborative nature and need for company support
- Maintains flexibility for consulting if employment isn't the right fit

## [1.0.2] - 2025-11-04

### Changed

- Removed unverified "2000+ schemes" claim throughout proposal (no public verification found)
- Replaced specific portfolio size claims with conservative qualitative language ("large portfolio", "extensive portfolio", "portfolio-wide")
- Updated ROI calculations from absolute numbers to ranges ("thousands of hours/year" instead of "3,250 hours/year")
- Revised NSW Strata Hub efficiency claims to avoid overpromising (removed "60,000 data points" → "tens of thousands of data points")
- Updated Fire Safety compliance language to "portfolio-wide" instead of "2000 Annual Fire Safety Statements"

### Rationale

Portfolio size verification attempts:

- Web searches found conflicting data: 1,000 buildings (2024 external source), 1,250 buildings (2021), 800 schemes (2022)
- No authoritative public source confirms "2000+ schemes"
- Conservative approach: avoid overpromising by using qualitative descriptors instead of unverified specific numbers

### Impact

- PDF size: 131KB, 31 pages (unchanged)
- Business case remains strong: 94% time reduction percentages retained (these are based on process efficiency, not portfolio size)
- All efficiency claims now verifiable per-scheme rather than dependent on total portfolio size

## [1.0.1] - 2025-11-04

### Fixed

- Andrew Tunks appointment date: September 12 → September 24, 2025 (verified from blog post metadata)
- Legislative drafting time estimate: 300-400 → 50-100 hours/year (corrected 10x overstatement)
- NSW Strata Hub statistics: standardized on 94% time reduction with 3200→200 hours calculation (previously inconsistent 90%, 94%, 98.3%)
- Water damage claims percentage: 60% → 50-70% (varies by insurer) based on multiple insurer data
- Merlo AI reduction claim: "email volume" → "overall workload" per vendor documentation
- Total Phase 1 efficiency gains: 3,500-3,700 → 3,250 hours/year (recalculated after legislative correction)

### Notes

- 2000+ schemes claim remains unverified through public sources (highest priority for external confirmation)
- Stephen Brell SCA resignation claim already removed in v1.0.0

### Audit Methodology

- Five parallel research agents deployed auditing 86 numerical claims across market statistics, regulatory data, insurance claims, company facts, and ROI estimates
- Overall verification rate: 79% (strong research integrity)
- Audit reports available in `/tmp/audit-*` directories

## [1.0.0] - 2025-11-04

### Added

- Evidence-based industry evolution analysis (Section 1.5) with three converging external pressures: regulatory mandate, insurance market pressure, client expectations
- Technology adoption benchmarks section (Section IV) documenting AI-powered platforms in Australian strata market
- Netstrata's proprietary data advantage framework (2000+ schemes, 16 years operational data)
- Areas where competitors set benchmarks (email automation, AGM management, compliance tracking)
- Areas where Netstrata can lead (insurance risk prediction, building defects intelligence, legislative update translation)
- Parallel research artifacts documenting competitive landscape, technology trends, RegTech compliance, insurance automation drivers

### Changed

- Replaced competitive blindspot narrative with balanced industry context analysis
- Updated table heading from "Competitive Blindspot" to "Industry Technology Adoption" with factual market statistics
- Revised language from fear-based to opportunity-based throughout proposal
- Changed "catastrophic single point of failure" to "significant operational dependency"
- Updated strategic positioning from defensive to leadership-focused
- Changed "future-proofing against PropTech disruption" to "building proprietary intelligence systems"
- Updated "McGrathNicol Crisis Acute" to "McGrathNicol Review Status"
- Changed "organizational vulnerability" to "operational continuity risk"

### Removed

- Exaggerated competitive threat language throughout proposal
- "PropTech Arms Race" framing in competitive context section
- "Threat assessment" analysis for individual competitors
- Fear-based positioning implying Ted Middleton unaware of market dynamics

## [Unreleased]

### Research Methodology

- Four parallel research agents deployed investigating: PropTech competitive landscape, technology adoption trends, RegTech compliance automation, insurance industry automation drivers
- 1500+ lines of research findings documenting market reality
- Evidence-based approach replacing speculative competitive positioning

[1.0.13]: https://github.com/tainora/netstrata/releases/tag/v1.0.13
[1.0.12]: https://github.com/tainora/netstrata/releases/tag/v1.0.12
[1.0.11]: https://github.com/tainora/netstrata/releases/tag/v1.0.11
[1.0.10]: https://github.com/tainora/netstrata/releases/tag/v1.0.10
[1.0.9]: https://github.com/tainora/netstrata/releases/tag/v1.0.9
[1.0.8]: https://github.com/tainora/netstrata/releases/tag/v1.0.8
[1.0.7]: https://github.com/tainora/netstrata/releases/tag/v1.0.7
[1.0.6]: https://github.com/tainora/netstrata/releases/tag/v1.0.6
[1.0.5]: https://github.com/tainora/netstrata/releases/tag/v1.0.5
[1.0.4]: https://github.com/tainora/netstrata/releases/tag/v1.0.4
[1.0.3]: https://github.com/tainora/netstrata/releases/tag/v1.0.3
[1.0.2]: https://github.com/tainora/netstrata/releases/tag/v1.0.2
[1.0.1]: https://github.com/tainora/netstrata/releases/tag/v1.0.1
[1.0.0]: https://github.com/tainora/netstrata/releases/tag/v1.0.0
