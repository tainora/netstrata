#!/usr/bin/env python3
"""Extract just 3 sample blog posts for review."""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "playwright",
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import asyncio
import sys
sys.path.insert(0, '.')
from extract_blogs import NetstrataExtractor


async def main():
    """Extract 3 sample blogs."""
    extractor = NetstrataExtractor()

    # Extract these 3 specific blogs for review
    sample_urls = [
        "https://netstrata.com.au/tax-time-tips/",
        "https://netstrata.com.au/navigating-the-2025-nsw-strata-law-reforms/",
        "https://netstrata.com.au/how-to-prepare-for-the-2025-nsw-strata-law-changes/"
    ]

    print(f"📥 Extracting {len(sample_urls)} sample blog posts for review...\n", flush=True)

    for i, url in enumerate(sample_urls, 1):
        print(f"[{i}/{len(sample_urls)}] {url}", flush=True)
        result = await extractor.extract_article(url)
        if result["success"]:
            await extractor.save_article(result)
        await asyncio.sleep(2)  # Small delay

    print(f"\n✅ Sample extraction complete! Check blogs/ directory", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
