# Blog Citation Audit & Corrections Report

**Date**: November 4, 2025
**Auditor**: Automated verification against scraped blog archive (292 posts)

---

## Executive Summary

Comprehensive audit of all blog post citations in STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.md revealed:

- **1 ERROR FOUND**: Post incorrectly marked as unavailable
- **1 ERROR FOUND**: Post with wrong title/date but correct concept
- **3 FABRICATIONS**: Posts that never existed as separate blog posts

---

## ✅ Corrections Made

### 1. Independent Review Post - CORRECTED

**Original Citation (INCORRECT)**:

- "Independent Review of Netstrata: Setting the Record Straight" [*Blog post no longer available online*] (Feb 26, 2025)

**Correct Citation**:

- ["Netstrata Independent Review"](https://netstrata.com.au/independentreview/) (Feb 26, 2025)

**Status**: ✅ **FIXED** - Hyperlink added, correct title used
**Verification**: HTTP 200 - Post exists and is accessible
**Source**: `/Users/terryli/own/netstrata/blogs/independentreview/independentreview.md`

---

### 2. Insurance Renewal Post - NEEDS CORRECTION

**Original Citation (INCORRECT)**:

- "How We Can Help Strata Schemes Prepare for the 2024 Insurance Renewal Season" [*Blog post no longer available online*] (December 6, 2023)

**Correct Citation**:

- ["Navigating Rising Strata Insurance Premiums: Challenges and Strategies"](https://netstrata.com.au/navigating-rising-strata-insurance-premiums-challenges-and-strategies/) (December 5, 2023)

**Issue**: Wrong title, close date (Dec 5 vs Dec 6), but correct topic
**Status**: ⚠️ **NEEDS FIXING** - Replace with correct title/URL
**Verification**: HTTP 200 - Post exists and is accessible
**Source**: `/Users/terryli/own/netstrata/blogs/navigating_rising_strata_insurance_premiums_challenges_and_strategies/metadata.json`

**Content Verification**:

- Mentions "Increases of 20% or more annually" ✅
- Discusses insurance renewal challenges ✅
- Published in December 2023 ✅

---

## ❌ Fabricated Posts (Never Existed as Separate Blog Posts)

### 3. "Revolutionising Strata Management – Introducing Drill Down"

**False Citation**:

- "Revolutionising Strata Management – Introducing Drill Down" [*Blog post no longer available online*] (May 22, 2025)

**Reality**:

- No such separate blog post exists
- "Drill Down" is mentioned as a feature in the May 6, 2025 McGrathNicol Review post
- ["McGrathNicol Review – Key updates & Improvements"](https://netstrata.com.au/mcgrathnicol-review-key-updates-improvements/)

**Actual Quote**:

> "### New Owner Portal & Drill Down Financials
>
> In line with continuous improvement and greater transparency, we are excited to announce the launch of our new Owners Portal, which can be accessed via our website. With access to revolutionary 'Drill Down' financial reporting, all owners can view their schemes' financials with links to all supplier invoices..."

**Status**: ❌ **FABRICATION** - Should be removed or merged into McGrathNicol Review citation
**Date Discrepancy**: May 22 vs May 6 (14 days off)
**Verification**: HTTP 404 - No post exists at guessed URL

---

### 4. "Preparing for 2025 Strata Insurance Renewals"

**False Citation**:

- "Preparing for 2025 Strata Insurance Renewals" [*Blog post no longer available online*] (October 30, 2024)

**Reality**:

- Not found in scraped blog archive (292 posts from 2009-2025)
- No posts from October 2024 exist in our archive
- May have been confused with the December 2023 insurance post

**Status**: ❌ **FABRICATION** - Should be removed
**Verification**: HTTP 404 - No post exists at guessed URL

---

### 5. "New Options for Virtual and Hybrid AGMs"

**False Citation**:

- "New Options for Virtual and Hybrid AGMs" [*Blog post no longer available online*] (Dec 8, 2021)

**Reality**:

- Not found in scraped blog archive
- Similar topics found:
  - "Holding Strata Meetings post-COVID" (June 18, 2020) - discusses virtual meetings
  - "Living With COVID-19 in Your Strata Scheme" (Dec 10, 2021) - close date but different topic

**Possible Confusion**:

- Date is close to "Living With COVID-19" post (Dec 10, 2021)
- Topic matches "Holding Strata Meetings post-COVID" (June 18, 2020)

**Status**: ❌ **FABRICATION** - Should be removed or replaced with actual post
**Verification**: HTTP 404 - No post exists at guessed URL

---

## Recommended Actions

### Immediate Fixes Required

1. **✅ DONE**: Fix "Independent Review" citation with correct title and hyperlink
2. **TODO**: Replace "How We Can Help..." with "Navigating Rising Strata Insurance Premiums"
3. **TODO**: Remove "Revolutionising Strata Management" as separate citation (already covered in McGrathNicol Review)
4. **TODO**: Remove "Preparing for 2025 Strata Insurance Renewals" (no evidence it exists)
5. **TODO**: Remove or replace "New Options for Virtual and Hybrid AGMs" (consider using June 2020 post instead)

### Alternative for Virtual Meetings Citation

**If you want to cite 50% attendance increase**, consider:

**Option A**: Use the actual post found

- ["Holding Strata Meetings post-COVID"](https://netstrata.com.au/holding-strata-meetings-post-covid/) (June 18, 2020)
- Quote: "Virtual meetings are certainly more convenient and they may even see an increase in attendees."

**Option B**: Remove the specific "50% increase" claim

- No verifiable source for this statistic in the blog archive

---

## Root Cause Analysis

These fabrications likely occurred due to:

1. **Memory conflation**: Combining elements from multiple real posts into false posts
2. **Title inference**: Creating plausible titles for topics mentioned in other posts
3. **Date approximation**: Guessing dates based on related events
4. **URL construction**: Assuming URLs followed pattern `https://netstrata.com.au/slug/`

---

## Verification Methodology

1. Searched 292 scraped blog posts in `/Users/terryli/own/netstrata/blogs/`
2. Tested HTTP status codes for all claimed URLs
3. Searched by title, date, and keywords in all `.md` and `metadata.json` files
4. Cross-referenced with `all_urls.txt` (complete URL list from scrape)

---

## All Valid Citations (Verified HTTP 200)

✅ ["How to Prepare for the 2025 NSW Strata Law Changes"](https://netstrata.com.au/how-to-prepare-for-the-2025-nsw-strata-law-changes/)
✅ ["NSW Strata Law Changes 2025 – What Owners and Committees Need to Know"](https://netstrata.com.au/nsw-strata-law-changes-2025-what-owners-and-committees-need-to-know/)
✅ ["McGrathNicol Review: Key Updates & Improvements"](https://netstrata.com.au/mcgrathnicol-review-key-updates-improvements/)
✅ ["Netstrata Appoints Andrew Tunks as Chief Operating Officer"](https://netstrata.com.au/netstrata-appoints-andrew-tunks-as-chief-operating-officer/)
✅ ["Strata Hub – A New Tool for Strata Schemes"](https://netstrata.com.au/strata-hub/)
✅ ["Rental Protections for Victim Survivors Under New NSW Laws"](https://netstrata.com.au/rental-protections-for-victim-survivors/)
✅ ["Netstrata Independent Review"](https://netstrata.com.au/independentreview/) ← CORRECTED
✅ ["Navigating Rising Strata Insurance Premiums: Challenges and Strategies"](https://netstrata.com.au/navigating-rising-strata-insurance-premiums-challenges-and-strategies/) ← SHOULD REPLACE FALSE CITATION

---

## Files Generated

- `/Users/terryli/own/netstrata/test_unavailable_urls.sh` - HTTP status test script
- `/Users/terryli/own/netstrata/audit_blog_citations.py` - Comprehensive audit script
- `/Users/terryli/own/netstrata/CITATION_AUDIT_CORRECTIONS.md` - This report
