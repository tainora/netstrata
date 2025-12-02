# Doc 04 Revision Implementation Plan

**Document**: `/Users/terryli/own/netstrata/materials-for-ted/04-netstrata-research.md`

**Date**: 2025-12-01

**Scope**: Comprehensive corrections based on Ted's November 30, 2025 call transcript and context notes

---

## Executive Summary

**Total Corrections Required**: 48 items across 8 major categories

**Estimated Impact**:

- **Major Rewrites**: 4 sections (20% of document)
- **Moderate Revisions**: 6 sections (30% of document)
- **Minor Corrections**: 15 sections (40% of document)
- **Text Preserved**: 2 sections (10% of document)

**Critical Risk Areas**:

1. Software timeline (multiple date errors)
2. Richardson/WA customer context (significant mischaracterization)
3. User numbers (off by 10x magnitude)
4. Manila office (incorrect framing)
5. Software name terminology (SMP vs Strata Space confusion)

---

## Phase 1: CRITICAL FACTUAL CORRECTIONS (High Risk)

**Priority**: HIGHEST - These errors could damage credibility if Ted reads them

**Execution Order**: Must be completed FIRST before any other revisions

### 1.1 Software Development Timeline Corrections

**Section**: "Software Strategy & Three-Phase Roadmap" (Lines 92-106)

**Current Errors**:

| Line | Current Text                                                                                    | Correction Needed                                                                                                              | Ted Quote Evidence                                                                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 96   | "approximately 19 years (2006-2025, with ~10 years intensive development)"                      | Change to "approximately 18-19 years (2006/2007-2025)"                                                                         | "That was around 2006, 2007"                                                                                                                             |
| 100  | "2006-2011: External contractor development"                                                    | Change to "2006/2007-2011: External contractor development (commissioned, first use ~2009)"                                    | "commissioned, along with it. That was around 2006, 2007... from about 2009 onwards, we had to support them financially"                                 |
| 101  | "2011: Hostile takeover - acquired the failing software company"                                | Change to "2011: Foreclosed on mortgage - acquired software company and employees"                                             | "We foreclosed on the mortgage" + "all of the employees... elected to come with us"                                                                      |
| 103  | "2015-2016: Decision to completely rebuild"                                                     | Change to "2013: Fully integrated into SMP (legacy software)" + "2016: Decision to completely rebuild (cloud-based)"           | "By 2013, we had essentially fully integrated into that software" + "In 2016, we... concluded that this software platform... just could not be expanded" |
| 104  | "2024: Major milestone - 'very expensive and very disruptive' change, began capitalizing costs" | Change to "2023: Major milestone - moved from 45% to 80% Strata Space (accounting software change, 18 months before Nov 2025)" | "the biggest change we made, we did it about 18 months ago... we went from sort of let's say 45 percent... up to 80 percent"                             |

**Dependencies**: NONE - Start immediately

**Estimated Impact**: 20% rewrite of software history section

**Risk Assessment**: **CRITICAL** - Timeline errors undermine credibility of entire research document

---

### 1.2 Richardson/WA Customer Reframing

**Section**: "Phase 2 (Current Blocker): Western Australia Migration Readiness" (Lines 158-166)

**Current Errors**:

| Issue           | Current Text                                                                   | Correction Needed                                                                                                                                                  | Ted Quote Evidence                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Status | "Former user of old Netstrata software 'hell-bent' to migrate to new platform" | Change to "Current external user of SMP software, gradually being migrated to Strata Space functions"                                                              | "Richardson — A strata management company in Perth, WA that are the only external user of SMP software right now. They are gradually being migrated across to some SS functions" |
| Motivation      | Implies they left and want to return                                           | Remove "former" and "hell-bent" language - they're CURRENT users upgrading                                                                                         | "Richardson's are still operating on what is mostly the original SMP platform"                                                                                                   |
| Progress Level  | "We're not ready for them yet"                                                 | Change to "They're 5 years behind Netstrata's Strata Space adoption (~5 years for Netstrata, quicker for Richardson due to ironed-out wrinkles and smaller scale)" | "they're probably 5 years behind us... It's not really five years. It took us five years to get there. For them, it would probably be a lot quicker"                             |
| Scale Context   | Missing                                                                        | ADD: "Richardson manages ~7-8K strata clients vs Netstrata's ~50K"                                                                                                 | "we've got around 50,000 Strata clients. I think they've got like 7 or 8,000"                                                                                                    |
| Current Blocker | "We're not ready yet"                                                          | Change to "Richardson experiencing 'indigestion' with recent Strata Space components - need time to absorb changes"                                                | "They've had a bit of indigestion with it... it's all shit, you know, there's a lot going on here. We need time to absorb this"                                                  |

**Dependencies**: Timeline corrections (1.1) - uses "5 years" reference

**Estimated Impact**: 30% rewrite of Phase 2 section

**Risk Assessment**: **CRITICAL** - Mischaracterizes existing customer relationship

---

### 1.3 User Numbers Magnitude Correction

**Section**: "Current Operational Status" (Lines 107-112) and transcript discussion

**Current Errors**:

| Line | Current Text                                              | Correction Needed                                       | Ted Quote Evidence                |
| ---- | --------------------------------------------------------- | ------------------------------------------------------- | --------------------------------- |
| 109  | "Fully functional for internal use across 2,000+ schemes" | KEEP (schemes ≠ users)                                  | Schemes are properties, not users |
| N/A  | Missing critical distinction                              | ADD NEW SECTION: "User Base vs Client Base Distinction" | Ted transcript lines 71-86        |

**NEW SECTION NEEDED** (insert after line 112):

```markdown
### User Base vs Client Base Distinction

**Internal Users (Netstrata Staff)**:

- **Strata Space users**: ~120-130 total staff with access
- **Continuous users**: ~100 staff (daily operations)
- **Occasional users**: ~20 staff (less frequent access)
- **Location**: Majority in main office, small number in branch office

**External Users (Client-Facing)**:

- **Netstrata Space mobile app**: Thousands of strata scheme owners/residents
- **Access Level**: Read-only visibility ("look-see access")
- **Functionality**: View documents, scheme information, financial data
- **No data input**: Owners cannot modify records (tight regulatory environment)
- **Platform**: Mobile app (dominant) + desktop access (identical interface, larger screen)
```

**Ted Quote Evidence**:

> "Well, the Stratus software, I'm going to guess 120 to 130, about 150 people. Not everybody uses it... there'd be 100 sort of, let's say, pretty well continuous users, maybe 20 or so that use it less often"

> "They only have access to a well. They do have that online access, but basically it's a look-see access... in that case, yes, the numbers go into thousands. But they don't have any data input."

**Dependencies**: NONE

**Estimated Impact**: NEW section (10 lines), clarifies critical distinction

**Risk Assessment**: **HIGH** - Missing this creates 10x magnitude confusion

---

### 1.4 Manila Office Operations Correction

**Section**: "Business Model - Multiple Divisions" (Lines 19-31) and implicit references

**Current Errors**:

| Issue                | Current Text                                                                        | Correction Needed                                                                                                                                                         | Ted Quote Evidence                                                                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ownership Structure  | "Offshore Operations: Separate company handling non-client-facing operational work" | Change to "Manila Operations: Separate company owned through family relationship of Netstrata director, handles non-client-facing back-office work"                       | "that company... It's actually through the family of one of our directors"                                                                                                                                                                                  |
| Work Type            | "operational work" (vague)                                                          | Specify: "Coding + administrative back-office work"                                                                                                                       | "a lot of our coding is done in Manila. And also, a lot of our administrative work is done in Manila"                                                                                                                                                       |
| Historical Context   | Missing                                                                             | ADD: "Originally started ~15 years ago (circa 2010) as work expected to be automated, but quality led to expanded scope despite software taking over many original tasks" | "we knew that a lot of the work that they were doing would ultimately be taken over by software... They're actually doing such a good job... even though much of the work they used to do has now been taken over software, we've given them other... work" |
| McGrathNicol Context | Missing                                                                             | ADD: "Relationship disclosure became controversial during McGrathNicol review/ABC investigation due to non-disclosure, but work is non-client-facing"                     | "that was one of the things that came in for a lot of caning from the ABC report, that we had this relationship. And that's right, we didn't disclose it"                                                                                                   |

**Dependencies**: NONE

**Estimated Impact**: 15% rewrite of division list + new context paragraph

**Risk Assessment**: **MEDIUM-HIGH** - Important governance/transparency context

---

### 1.5 Software Name Terminology Standardization

**Sections**: Throughout document (multiple references)

**Current Confusion**: Document uses "proprietary software" without distinguishing SMP (legacy) vs Strata Space (new)

**Corrections Needed**:

| Term                         | Usage Rule                                                                                             | Ted's Context Notes                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SMP (Strata Manager Pro)** | Legacy system (2007-2027 retirement), original proprietary software developed ~2007, fully owned 2011  | "Our first proprietary strata management software originally developed from ~2007, the complete ownership of which we assumed in 2011. Due for retirement early 2027." |
| **Strata Space (SS)**        | New proprietary system (development since ~2016, first use ~2019, gradual adoption through 2025+)      | "Our proprietary strata management software system in development since ~2016, first entered use ~2019 and now still assuming/absorbing the functions of... SMP"       |
| **Netstrata Space**          | Client-facing mobile app (hangs off Strata Space)                                                      | "The client-facing mobile app hanging off SS"                                                                                                                          |
| **Parallel Operation**       | Both systems running simultaneously during transition (user sees one interface accessing both systems) | Ted transcript: "the architect of that system then said, look, it's possible for us to build a system, operate the systems in parallel"                                |

**Find-Replace Audit Required**:

- Review every instance of "proprietary software" - specify SMP or Strata Space
- Review every instance of "the software" - add clarity about which system
- Review every instance of "new platform" - confirm refers to Strata Space

**Dependencies**: Timeline corrections (1.1) must be complete first

**Estimated Impact**: 20+ terminology clarifications throughout document

**Risk Assessment**: **MEDIUM** - Clarity issue, not factual error, but affects professional precision

---

## Phase 2: MODERATE REVISIONS (Accuracy Improvements)

**Priority**: HIGH - Complete after Phase 1 critical corrections

**Execution Order**: Can be done in parallel after Phase 1 is complete

### 2.1 Software History Narrative Expansion

**Section**: "The Proprietary Software Investment" (Lines 94-106)

**Additions Needed** (from Ted transcript):

1. **2009-2011: Financial Support Period**
   - ADD: "From 2009 onwards, Netstrata financially supported development as other original investors dropped off"
   - **Quote**: "from about 2009 onwards, we had to support them financially to keep building the software. Eventually, the other operators, other users that contributed to this, most of them dropped off"

2. **2011: Parallel System Use**
   - ADD: "Started using SMP in parallel to legacy systems"
   - **Quote**: "at around 2011... We actually started to use the software, you know, we were using it sort of in parallel to our other systems"

3. **2011: Foreclosure Trigger**
   - ADD: "External developer attempted to sell software from underneath Netstrata; foreclosure on mortgage followed"
   - **Quote**: "Then it came to us that they were trying to sell the software from underneath us. So we foreclosed on the mortgage"

4. **2011: Employee Transition**
   - ADD: "4-5 employees elected to join Netstrata (financial motivation)"
   - **Quote**: "all of the employees, there were only four or five, I think, employees elected to come with us... they realised we were the major financial backer... they were concerned about their own financial well-being"

5. **2013: Full SMP Integration**
   - ADD: "By 2013, fully integrated into SMP, retired original 1996 software"
   - **Quote**: "By 2013, we had essentially fully integrated into that software we we'd gotten rid of the original software"

6. **2015: SMP Maturity Plateau**
   - ADD: "By ~2015, SMP reached developmental limits - doing everything wanted but platform couldn't expand further"
   - **Quote**: "it had probably matured it reached the sort of maybe if not the developmental limits, it was doing everything we wanted to do. In 2016, we, of course, concluded that this software platform... just could not be expanded"

7. **Current (Nov 2025): Parallel Operation Status**
   - ADD: "November 2025 major release: 85% operating in Strata Space, entire system (including SMP components) migrated to cloud"
   - **Quote**: "now with, say, the changes that are happening this month, I'm going to say that we'd be 85% operating in the new system... even though the old system was never designed to operate in the cloud, it has migrated there"

8. **End-2026 Timeline Clarification**
   - REVISE: "End of next year is nominal SMP shutdown, but small elements will continue running in background (low priority items - irritation vs catastrophic)"
   - **Quote**: "the objective... is that the old system will be virtually put to bed by the end of next year... there are still little elements of it... if we didn't have them, it would just be an irritation rather than anything catastrophic"

**Dependencies**: Timeline corrections (1.1) and terminology standardization (1.5)

**Estimated Impact**: 40% expansion of software history section (from 14 lines to ~25 lines)

**Risk Assessment**: **MEDIUM** - Adds valuable context and precision

---

### 2.2 Epi Neto (IT Administrator) Details

**Section**: "IT/Software Leadership" (Lines 62-68)

**Current Text**:

```markdown
- **Epitacio Neto**: Head of IT Infrastructure
  - Manages hardware, cloud systems, office migration
```

**Corrections Needed**:

| Issue          | Add/Change                                                                                                                                                                                                              | Ted Evidence                                                                                                                                                                                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name Spelling  | Change "Epitacio Neto" to "Epi Neto" (nickname used)                                                                                                                                                                    | Ted context notes: "Epi — The name Epi Neto"                                                                                                                                                                                                                                |
| Full Name      | ADD: "(Epitacio Neto)" in parentheses after "Epi Neto"                                                                                                                                                                  | Ted: "Epi Neto is our IT administrator"                                                                                                                                                                                                                                     |
| Title Accuracy | Change "Head of IT Infrastructure" to "IT Administrator"                                                                                                                                                                | Ted context notes: "is our IT administrator"                                                                                                                                                                                                                                |
| Visa History   | ADD: "Originally came to Netstrata on subclass 482 visa (sponsored from previous employer), obtained permanent residency after ~2 years, left for other employers twice, returned most recently on 'ironclad contract'" | Ted transcript: "he was working for another company... we took over his visa... for a couple of years until he got permanent residency... he went and worked for somebody else... After a while, he came back... He did it again... this time he's on an ironclad contract" |
| AI Leadership  | ADD: "Recently completed postgraduate Master's in AI, leading Netstrata's AI initiatives (currently baby steps/internal use only)"                                                                                      | Ted context notes: "Epi recently completed a post-grad masters in AI and is, apart from his routine administrator duties, leading our (baby steps, for now) into the AI environment"                                                                                        |
| Nationality    | ADD: "Brazilian national"                                                                                                                                                                                               | Ted transcript: "He's Brazilian"                                                                                                                                                                                                                                            |

**NEW TEXT**:

```markdown
- **Epi Neto** (Epitacio Neto): IT Administrator
  - Manages hardware, cloud systems, office infrastructure
  - Brazilian national, originally came to Netstrata on subclass 482 visa (sponsored from previous employer ~10-11 years ago)
  - Obtained permanent residency after ~2 years, left for other employers twice, returned on "ironclad contract"
  - Recently completed postgraduate Master's in AI
  - Leading Netstrata's AI initiatives (currently baby steps, internal use only)
```

**Dependencies**: NONE

**Estimated Impact**: 50% expansion of Epi's profile (3 lines → 7 lines)

**Risk Assessment**: **LOW** - Adds helpful context but not critical

---

### 2.3 Tom Bakani Corrections

**Section**: "IT/Software Leadership" (Lines 64-66)

**Current Text**:

```markdown
- **Tom Bakani**: Head of Software Operations
  - Manages proprietary software development team
```

**Corrections Needed**:

| Issue                | Add/Change                                                                                                                                                           | Ted Evidence                                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name Spelling        | Change "Bakani" to "Bacani"                                                                                                                                          | Ted context notes: "Tom Bacani's Q3 2025 Board Report"                                                                                                                                                        |
| Nationality/Location | REMOVE: "Philippines" - Ted never said this                                                                                                                          | Not mentioned in transcript or context notes                                                                                                                                                                  |
| Visa History         | REMOVE: "originally sponsored visa, returned ~2024" - unsupported                                                                                                    | Not mentioned in transcript or context notes                                                                                                                                                                  |
| Team Growth          | ADD: "Team added 8 new people in Q3 2025 (July-September), addressing talent acquisition struggles"                                                                  | Ted transcript: "they put on eight new people in the last quarter. So they had been struggling getting the right talent... they managed to happen upon eight new ones in over a period of a couple of months" |
| Current Focus        | ADD: "November-December 2025: Leading major Strata Space release affecting all 120-130 staff users (company-wide change, tight timeline before December 18 closure)" | Ted transcript: "starting today, they've got a major installation going on... it's supposed to be finished before we finish at Christmas. We finish on the 8th of December [NOTE: later says 18th]"           |

**NEW TEXT**:

```markdown
- **Tom Bacani**: Head of Software Operations
  - Manages proprietary software development team
  - Team added 8 new people in Q3 2025 (July-September), addressing talent acquisition challenges
  - November-December 2025: Leading major Strata Space release affecting all 120-130 staff users (company-wide change, tight timeline before December 18 closure)
```

**Dependencies**: User numbers clarification (1.3)

**Estimated Impact**: 40% expansion of Tom's profile (3 lines → 5 lines)

**Risk Assessment**: **LOW-MEDIUM** - Removes unsupported claims, adds current context

---

### 2.4 Office Migration Cloud Context

**Section**: "Recent Industry Context & Challenges" or new subsection under Software Strategy

**Current Mention**: Brief reference in "AI-Augmented Development" section about cloud migration

**Enhancement Needed**:

ADD new subsection after "Current Operational Status" (after line 112):

```markdown
### Recent Infrastructure Milestones

**Office Migration (October 2024)**:

- Moved to new building, junked all physical servers
- Complete cloud migration required before relocation
- Migration challenges: Some systems didn't work well in cloud initially
- Stabilization took months (issues mostly resolved by November 2025)

**Quote Context**: "when we moved into the new building, which happened in over a year ago now, I think it happened in October last year, everything had to go up to the cloud before we moved because we weren't going to move any old servers... That was also, it didn't go especially smoothly because some of the systems we had had to just, well, didn't work very well in the cloud"
```

**Dependencies**: Timeline corrections (1.1)

**Estimated Impact**: NEW section (8 lines)

**Risk Assessment**: **LOW** - Adds color but not critical

---

### 2.5 AI Initiatives Current Status

**Section**: "AI-Augmented Development as Competitive Advantage" (Lines 192-218)

**Current Tone**: Positions AI-augmented development as opportunity for Netstrata to adopt

**Revisions Needed**:

1. **ADD CONTEXT: Netstrata Already Exploring AI** (insert before line 192):

```markdown
### Netstrata's Current AI Exploration

**Status (November 2025)**: Baby steps, internal use only

**Leadership**: Epi Neto (IT Administrator with recent Master's in AI)

**Approach**:

- Very cautious, phased rollout
- Internal testing before any client-facing applications
- Awareness of AI limitations from existing use
- Timeline uncertain - "could even be years away" for client-facing AI

**Current Reality Check**: Ted encountered ChatGPT-generated board report (88% AI per Grammarly plagiarism checker) from law firm GM that was "50% garbage despite beautiful graphs and charts - would pass muster with someone who knew a little bit about it, but not somebody who knows just about all there is to know." This reinforced skepticism about AI replacing domain expertise.

**Quote**: "Right now, it's very, very baby steps because we know, because we already use AI. We also know its limitations... Knowing how things go in software, that could even be years away."
```

2. **REFRAME "AI-Augmented Development as Competitive Advantage"**:
   - Change from "opportunity to adopt" to "opportunity to accelerate existing exploration"
   - Emphasize "development practices" (not end-user features) alignment with Ted's skepticism
   - Keep focus on "operational efficiency" (matches Andrew Tunks' COO mandate)

3. **ADD TED'S PERSPECTIVE ON INDUSTRY SOPHISTICATION**:
   - Already present (line 184-188) - KEEP as is
   - This quote supports cautious, fundamentals-focused approach

**Dependencies**: Epi Neto corrections (2.2)

**Estimated Impact**: 20% expansion + tone adjustment of AI section

**Risk Assessment**: **MEDIUM** - Shows awareness of Netstrata's existing efforts, avoids appearing presumptuous

---

## Phase 3: MINOR CORRECTIONS (Polish & Precision)

**Priority**: MEDIUM - Complete after Phase 2

**Execution Order**: Can be done quickly in batch

### 3.1 McGrathNicol Timeline & Status Update

**Section**: "Recent Industry Context & Challenges" (Lines 33-48) + later references

**Current References**:

- Line 46: "McGrathNicol deadline: July 1, 2025 (6 remaining recommendations) - **NOW PAST**"

**Additions Needed** (from Ted transcript):

1. **ABC Investigation Context** (ADD before McGrathNicol reference):

```markdown
**ABC Investigation & McGrathNicol Audit (2024-2025)**:

**Trigger**: Early 2024 ABC (Australian Broadcasting Corporation) "hit job" television program featuring disgruntled former employee (failed relationship with associate director)

**Regulatory Response**: Attracted Office of Fair Trading attention due to allegations of wrongdoing

**McGrathNicol Audit**: Independent auditor appointed by Office of Fair Trading

- Timeline: Mid-2024 through end-2024
- Cost: "Incredible expense" (split between Netstrata and OFT)
- Report: 200 pages total, 4-page executive summary highlighting issues
- Findings: "Wasn't too bad" - some areas for improvement, nothing prosecutable ("none of them were hanging offences")
- Office of Fair Trading reaction: "Not happy with audit report," launched their own investigation

**Ongoing Investigation (November 2025)**:

- OFT investigation described as "spectacularly incompetent" and "amateurish" (Ted's assessment)
- Status unclear: "pushed down the line to a very low level of the department... sitting on somebody's desk"
- Impact: "Financially painful and operationally painful" - millions in compliance costs
- New hire: Risk and Compliance Manager (full-time role, ~$150K annually) to ensure regulatory compliance

**Software Compliance Visibility Impact**: Many 2024-2025 software changes focused on increasing compliance visibility for regulators, even when not operationally necessary ("the more information you give people, the less they read")

**Quote**: "we've had to do things just to maintain... transparency and compliance... to go over the top and look, you know, like, outrageously so"
```

2. **UPDATE McGrathNicol Reference**:
   - Change "NOW PAST" to "Audit completed end-2024; OFT investigation ongoing but status unclear (November 2025)"

**Dependencies**: NONE

**Estimated Impact**: NEW section (20 lines) + 1 line update

**Risk Assessment**: **MEDIUM** - Important context for understanding recent company pressures

---

### 3.2 Stephen Brell SCA Leadership Detail

**Section**: "Leadership Structure" (Lines 49-61)

**Current Text** (Lines 54-56):

```markdown
- **Stephen Brell**: Managing Director (oversees all business divisions)
  - Also President of Strata Community Australia (NSW) - industry leadership role
```

**No Changes Needed**: This is accurate per existing research

**Dependencies**: NONE

**Risk Assessment**: **NONE** - Already correct

---

### 3.3 Andrew Tunks COO Mandate Quote Verification

**Section**: "Leadership Structure" (Lines 56-59)

**Current Text**:

```markdown
- **Andrew Tunks**: Chief Operating Officer (promoted 2025)
  - Previously Training & Development
  - Mandate: "operational efficiency, continuous improvement, innovation"
  - Manages strata management, valuations, and trade services divisions
```

**Verification**: Ted transcript does NOT contain this quote. This likely came from November 4, 2025 conversation or blog research.

**Action**: KEEP as is (not contradicted by new transcript, consistent with Ted's description)

**Dependencies**: NONE

**Risk Assessment**: **NONE** - No correction needed

---

### 3.4 MYOB Accounting Engine Detail

**Section**: Could add to "Key 'Impossible' Capabilities Research" or software description

**Enhancement Option** (from Ted context notes):

ADD to software capabilities description:

```markdown
**Accounting Engine**: MYOB Accounting Enterprise integrated into Strata Space

- Professional-grade accounting software with simplified interface for non-accountants
- Enables complex trust accounting without requiring accounting expertise from strata managers
```

**Ted Context Note**: "MYOB (MYOB Accounting Enterprise) — The client accounting engine in SS. This is very powerful professional accounting software where, for SS users, the interface has been simplified (dumbed-down?) for use (even understanding) by non-accountants."

**Dependencies**: Terminology standardization (1.5)

**Estimated Impact**: Optional 3-line addition

**Risk Assessment**: **LOW** - Nice-to-have detail, not critical

---

### 3.5 Document Management System (DMS) Detail

**Section**: Could add to "Key 'Impossible' Capabilities Research"

**Enhancement Option** (from Ted context notes + transcript):

ADD to capabilities list:

```markdown
**Fully Integrated Document Management System**:

- Paperless operations since ~2011
- DMS integrated into SMP (originally), migrating to Strata Space (December 2025)
- Competitive differentiation: Most competitors use separate DMS that opens in different window
- Client visibility: Seamless document access via mobile app/desktop (impossible with separate DMS systems)
```

**Ted Context Note**: "DMS — Document management system. Virtually all our internal operations are paperless (since ~2011) with the DMS incorporated into SMP (originally) which is now (next month) migrating to SS."

**Ted Transcript Quote**: "our document management system is part of the management system. Virtually every other system that uses document management just attaches to a separate document management system... Ours is wholly integrated, which allows us to do a lot of things... the visibility, client visibility... they've got the kind of access that it just would not be possible for anybody else"

**Dependencies**: Terminology standardization (1.5), Timeline corrections (1.1)

**Estimated Impact**: Optional 5-line addition

**Risk Assessment**: **LOW** - Supports competitive differentiation narrative

---

### 3.6 Time-Recording System Detail

**Section**: Could add to software capabilities

**Enhancement Option** (from Ted context notes):

ADD to capabilities list:

```markdown
**Time-Recording System**:

- Integrated into SMP since 2011 for all client-facing activity tracking
- Migrating to Strata Space December 2025 with "quantum increase in accuracy and sophistication"
- Enables precise billing, workload analysis, and resource allocation
```

**Ted Context Note**: "Time-recording — Of every client-facing activity has been a function of SMP since 2011 which will now - with a quantum increase in accuracy and sophistication - migrate to SS next month."

**Dependencies**: Timeline corrections (1.1), Terminology standardization (1.5)

**Estimated Impact**: Optional 3-line addition

**Risk Assessment**: **LOW** - Supporting detail, not critical

---

### 3.7 Learning & Development (L&D) Department

**Section**: Could add to "Business Model - Multiple Divisions" or organizational description

**Enhancement Option** (from Ted context notes):

ADD to divisions list or organizational capabilities:

```markdown
**Learning & Development (L&D)**: Internal training department serving all business operations
```

**Ted Context Note**: "L&D — Our company's Learning & Development department - which does precisely what the name suggests across all our business operations."

**Dependencies**: NONE

**Estimated Impact**: Optional 1-line addition

**Risk Assessment**: **NONE** - Minor organizational detail

---

## Phase 4: STRUCTURAL IMPROVEMENTS (Optional Enhancements)

**Priority**: LOW - Only if time permits after Phases 1-3

### 4.1 Software Timeline Visualization

**Enhancement**: Add chronological table summarizing corrected timeline

**Location**: After "Development Timeline" (after line 106)

**Format**:

```markdown
### Software Development Timeline (Consolidated)

| Year       | SMP (Legacy) Milestones                              | Strata Space (New) Milestones                              |
| ---------- | ---------------------------------------------------- | ---------------------------------------------------------- |
| 2006/2007  | Commissioned external contractor                     | -                                                          |
| 2009       | Financial support begins (other investors drop off)  | -                                                          |
| 2011       | Foreclosed on mortgage, acquired company + employees | -                                                          |
| 2011       | Started parallel use with legacy systems             | -                                                          |
| 2013       | Fully integrated, retired 1996 software              | -                                                          |
| ~2015      | Reached developmental plateau (mature but limited)   | -                                                          |
| 2016       | -                                                    | Decision to rebuild (cloud-based architecture)             |
| ~2019      | -                                                    | First entered use                                          |
| 2023       | -                                                    | Major change: 45% → 80% Strata Space (accounting software) |
| Oct 2024   | Cloud migration (with SMP components)                | Office move forces full cloud migration                    |
| Nov 2025   | 15% still in use (parallel operation)                | 85% operating in Strata Space                              |
| Dec 2025   | -                                                    | Major release (DMS, time-recording migration)              |
| End 2026   | Nominal retirement (small elements remain)           | Expected completion target                                 |
| Early 2027 | Full retirement                                      | -                                                          |
```

**Dependencies**: Timeline corrections (1.1), Terminology standardization (1.5)

**Estimated Impact**: NEW visualization (15 lines)

**Risk Assessment**: **NONE** - Optional enhancement for clarity

---

### 4.2 Moat Analysis Update with Manila Context

**Section**: "GTM Readiness & Competitive Moat Strategy" (Lines 326-472)

**Enhancement**: Add Manila operations to moat discussion

**Location**: Under "Migration Pain Moat" (around line 342)

**Addition**:

```markdown
- **Service Ecosystem Moat**: Vertical integration (insurance, legal, accounting, trade services) + Manila back-office operations create switching costs beyond software - customers become dependent on integrated service bundle
  - Manila operations (15 years, coding + administrative work) enable cost-effective back-office scaling
  - Quality exceeded expectations: Work originally expected to be automated expanded in scope due to performance
  - Governance transparency: Relationship through director's family became controversial (McGrathNicol/ABC investigation) but work remains non-client-facing
```

**Dependencies**: Manila corrections (1.4), McGrathNicol context (3.1)

**Estimated Impact**: Optional 5-line addition to moat analysis

**Risk Assessment**: **NONE** - Optional strategic context

---

## Execution Checklist

### Phase 1: CRITICAL CORRECTIONS (Must Complete)

- [ ] 1.1 Software Timeline Corrections (8 date/milestone fixes)
- [ ] 1.2 Richardson/WA Customer Reframing (5 characterization fixes)
- [ ] 1.3 User Numbers Magnitude Correction (new section on internal vs external users)
- [ ] 1.4 Manila Office Operations Correction (4 context additions)
- [ ] 1.5 Software Name Terminology Standardization (20+ clarifications)

**Estimated Time**: 3-4 hours
**Success Criteria**: Zero factual errors that would damage credibility with Ted

---

### Phase 2: MODERATE REVISIONS (High Priority)

- [ ] 2.1 Software History Narrative Expansion (8 milestones added)
- [ ] 2.2 Epi Neto Details (visa history, AI leadership, nationality)
- [ ] 2.3 Tom Bacani Corrections (name spelling, team growth, current focus)
- [ ] 2.4 Office Migration Cloud Context (new section)
- [ ] 2.5 AI Initiatives Current Status (reframe as acceleration of existing efforts)

**Estimated Time**: 2-3 hours
**Success Criteria**: Document reflects depth of Ted's November 30 context

---

### Phase 3: MINOR CORRECTIONS (Polish)

- [ ] 3.1 McGrathNicol Timeline & Status Update (ABC context, OFT investigation)
- [ ] 3.2 Stephen Brell - No changes needed (already correct)
- [ ] 3.3 Andrew Tunks - No changes needed (already correct)
- [ ] 3.4 MYOB Accounting Engine Detail (optional 3 lines)
- [ ] 3.5 Document Management System Detail (optional 5 lines)
- [ ] 3.6 Time-Recording System Detail (optional 3 lines)
- [ ] 3.7 Learning & Development Department (optional 1 line)

**Estimated Time**: 1-2 hours
**Success Criteria**: Document includes all major context from Ted's call

---

### Phase 4: STRUCTURAL IMPROVEMENTS (Optional)

- [ ] 4.1 Software Timeline Visualization (table)
- [ ] 4.2 Moat Analysis Update with Manila Context

**Estimated Time**: 1 hour
**Success Criteria**: Enhanced clarity and strategic depth

---

## Risk Assessment Summary

### CRITICAL Risks (Must Fix)

1. **Software Timeline Errors** - Multiple date inaccuracies undermine research credibility
2. **Richardson Mischaracterization** - Calling current customer "former" shows lack of understanding
3. **User Numbers Confusion** - Missing 10x magnitude distinction between internal staff and external clients

**Impact if Not Fixed**: Ted reads document and thinks "this person didn't listen to me" or "basic facts are wrong"

---

### HIGH Risks (Should Fix)

1. **Manila Office Framing** - Missing governance context from McGrathNicol controversy
2. **Tom Bacani Name Spelling** - Wrong surname shows inattention to detail
3. **AI Initiatives Tone** - Appears to suggest something Netstrata isn't already doing

**Impact if Not Fixed**: Missed opportunity to show thorough understanding; appears uninformed

---

### MEDIUM Risks (Nice to Fix)

1. **Software History Gaps** - Missing valuable narrative details from Ted's account
2. **Epi Neto Context** - Incomplete profile of key AI leadership person
3. **McGrathNicol Context** - Important for understanding recent company pressures

**Impact if Not Fixed**: Document is accurate but not comprehensive

---

### LOW Risks (Optional)

1. **Technical Details** - MYOB, DMS, time-recording, L&D mentions
2. **Visualization** - Timeline table for clarity

**Impact if Not Fixed**: None - these are enhancements, not corrections

---

## Dependencies Map

```
Phase 1.1 (Timeline) ──┬──> Phase 2.1 (Software History Expansion)
                       ├──> Phase 1.5 (Terminology)
                       └──> Phase 4.1 (Timeline Visualization)

Phase 1.2 (Richardson) ──> (No dependents)

Phase 1.3 (User Numbers) ──> Phase 2.3 (Tom Bacani)

Phase 1.4 (Manila) ──┬──> Phase 3.1 (McGrathNicol Context)
                     └──> Phase 4.2 (Moat Analysis)

Phase 1.5 (Terminology) ──┬──> Phase 2.1 (Software History)
                          ├──> Phase 3.4 (MYOB Detail)
                          ├──> Phase 3.5 (DMS Detail)
                          └──> Phase 3.6 (Time-Recording Detail)

Phase 2.2 (Epi) ──> Phase 2.5 (AI Initiatives)

Phase 3.1 (McGrathNicol) ──> Phase 4.2 (Moat Analysis)
```

**Critical Path**: Phase 1.1 → Phase 1.5 → Phase 2.1 (longest dependency chain)

---

## Quote-Backed Evidence Summary

### Top 10 Most Important Ted Quotes for Corrections

1. **Software Start Date**: "That was around 2006, 2007"
2. **Financial Support**: "from about 2009 onwards, we had to support them financially"
3. **Foreclosure (not hostile takeover)**: "We foreclosed on the mortgage"
4. **2013 Full Integration**: "By 2013, we had essentially fully integrated into that software"
5. **2023 Major Change**: "the biggest change we made, we did it about 18 months ago... 45 percent... up to 80 percent"
6. **Richardson Current Status**: "Richardson... are the only external user of SMP software right now"
7. **Internal Users**: "120 to 130... 100 sort of... continuous users"
8. **External Users**: "the numbers go into thousands. But they don't have any data input"
9. **Manila Ownership**: "It's actually through the family of one of our directors"
10. **November 2025 Status**: "we'd be 85% operating in the new system"

---

## Validation Checklist (Before Finalizing)

### Factual Accuracy

- [ ] All dates cross-checked against Ted transcript + context notes
- [ ] All names spelled correctly (Tom Bacani, Epi Neto)
- [ ] All numbers match Ted's statements (120-130 users, 50K clients, 7-8K Richardson clients)
- [ ] All characterizations match Ted's language (foreclosure not takeover, current not former)

### Terminology Consistency

- [ ] SMP vs Strata Space used correctly throughout
- [ ] Parallel operation concept explained where relevant
- [ ] Timeline references align with corrected dates

### Quote Attribution

- [ ] All new additions traceable to transcript or context notes
- [ ] Paraphrased quotes maintain Ted's meaning
- [ ] No invented details or speculation

### Professional Tone

- [ ] No presumptuous language ("Netstrata should do X")
- [ ] Acknowledges existing efforts (AI exploration, Manila operations)
- [ ] Respects Ted's skepticism (ChatGPT board report anecdote)

---

## Post-Revision Review Questions

1. **If Ted reads this, will he say "this person listened to me"?**
2. **Are there any claims that contradict Ted's November 30 transcript?**
3. **Does the document show awareness of Netstrata's current state (not just November 4 conversation)?**
4. **Are all dates, names, and numbers verifiable against Ted's own words?**
5. **Does the Richardson section accurately reflect their current customer relationship?**

---

## Next Steps After Implementation

1. **Generate clean revision** of Doc 04 with all Phase 1-3 corrections
2. **Create diff/changelog** showing what changed and why (for transparency)
3. **Review against Ted's context notes one final time** (cross-check glossary)
4. **Prepare summary memo** for Ted highlighting key updates based on his November 30 call
5. **Consider whether to regenerate PDF** or send markdown for Ted's review first

---

**End of Implementation Plan**
