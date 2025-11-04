# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.0.5]: https://github.com/tainora/netstrata/releases/tag/v1.0.5
[1.0.4]: https://github.com/tainora/netstrata/releases/tag/v1.0.4
[1.0.3]: https://github.com/tainora/netstrata/releases/tag/v1.0.3
[1.0.2]: https://github.com/tainora/netstrata/releases/tag/v1.0.2
[1.0.1]: https://github.com/tainora/netstrata/releases/tag/v1.0.1
[1.0.0]: https://github.com/tainora/netstrata/releases/tag/v1.0.0
