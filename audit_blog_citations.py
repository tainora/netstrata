#!/usr/bin/env python3
"""Audit all blog post citations in the strategic proposal."""

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

def extract_blog_citations(proposal_path: Path) -> List[Dict[str, str]]:
    """Extract all blog post citations from the proposal."""
    content = proposal_path.read_text()

    citations = []

    # Pattern 1: Hyperlinked posts: ["Title"](URL) (Date)
    hyperlinked = re.finditer(
        r'\["([^"]+)"\]\((https://netstrata\.com\.au/[^)]+)\)\s*\(([^)]+)\)',
        content
    )
    for match in hyperlinked:
        citations.append({
            'title': match.group(1),
            'url': match.group(2),
            'date': match.group(3),
            'type': 'hyperlinked'
        })

    # Pattern 2: Unavailable posts: "Title" [*Blog post no longer available online*] (Date)
    unavailable = re.finditer(
        r'"([^"]+)"\s*\[\*Blog post no longer available online\*\]\s*\(([^)]+)\)',
        content
    )
    for match in unavailable:
        citations.append({
            'title': match.group(1),
            'url': None,
            'date': match.group(2),
            'type': 'unavailable'
        })

    return citations

def test_url_status(url: str) -> int:
    """Test HTTP status of a URL."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
            capture_output=True,
            text=True,
            timeout=10
        )
        return int(result.stdout.strip())
    except Exception:
        return 0

def find_in_scraped_data(title: str, blogs_dir: Path) -> str | None:
    """Try to find a blog post in scraped data by title."""
    # Search through all .md files in blogs directory
    for md_file in blogs_dir.rglob('*.md'):
        try:
            content = md_file.read_text()
            # Look for the title in the file
            if title.lower() in content.lower():
                # Try to extract the source URL
                source_match = re.search(r'\*\*Source:\*\*\s*(https://[^\s\n]+)', content)
                if source_match:
                    return source_match.group(1)
        except Exception:
            continue
    return None

def main():
    proposal_path = Path('/Users/terryli/own/netstrata/STRATEGIC_TECHNOLOGY_ADVISORY_PROPOSAL.md')
    blogs_dir = Path('/Users/terryli/own/netstrata/blogs')

    print("=" * 80)
    print("BLOG CITATION AUDIT REPORT")
    print("=" * 80)
    print()

    citations = extract_blog_citations(proposal_path)

    # Remove duplicates
    unique_citations = []
    seen = set()
    for cit in citations:
        key = (cit['title'], cit.get('url', ''))
        if key not in seen:
            seen.add(key)
            unique_citations.append(cit)

    print(f"Total citations found: {len(unique_citations)}")
    print()

    errors = []
    warnings = []

    print("HYPERLINKED CITATIONS:")
    print("-" * 80)
    hyperlinked_cits = [c for c in unique_citations if c['type'] == 'hyperlinked']
    for cit in hyperlinked_cits:
        status = test_url_status(cit['url'])
        if status == 200:
            print(f"✅ [{status}] {cit['title']}")
            print(f"    URL: {cit['url']}")
        elif status == 404:
            print(f"❌ [{status}] {cit['title']}")
            print(f"    URL: {cit['url']}")
            errors.append(f"404 error for hyperlinked post: {cit['title']}")
        else:
            print(f"⚠️  [{status}] {cit['title']}")
            print(f"    URL: {cit['url']}")
            warnings.append(f"Unexpected status {status} for: {cit['title']}")
        print()

    print("=" * 80)
    print("UNAVAILABLE CITATIONS:")
    print("-" * 80)
    unavailable_cits = [c for c in unique_citations if c['type'] == 'unavailable']
    for cit in unavailable_cits:
        print(f"📝 {cit['title']}")
        print(f"    Date: {cit['date']}")

        # Try to find in scraped data
        found_url = find_in_scraped_data(cit['title'], blogs_dir)
        if found_url:
            print(f"    Found in scraped data: {found_url}")
            # Test the URL
            status = test_url_status(found_url)
            if status == 200:
                print(f"    🚨 ERROR: This post IS STILL AVAILABLE (HTTP {status})")
                errors.append(f"Post marked unavailable but still exists: {cit['title']} at {found_url}")
            elif status == 404:
                print(f"    ✅ Confirmed unavailable (HTTP 404)")
            else:
                print(f"    ⚠️  Unexpected status: HTTP {status}")
        else:
            print(f"    ⚠️  Not found in scraped data - possible fabrication")
            warnings.append(f"Post not in scraped data: {cit['title']}")
        print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total citations: {len(unique_citations)}")
    print(f"Hyperlinked: {len(hyperlinked_cits)}")
    print(f"Marked unavailable: {len(unavailable_cits)}")
    print(f"Errors found: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print()

    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  ❌ {error}")
        print()

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
        print()

if __name__ == '__main__':
    main()
