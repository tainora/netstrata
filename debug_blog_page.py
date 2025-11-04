#!/usr/bin/env python3
"""Debug script to examine a single blog post structure."""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "playwright",
#     "beautifulsoup4",
# ]
# ///

import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def main():
    """Fetch and examine a blog post."""
    url = "https://netstrata.com.au/tax-time-tips/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"📄 Fetching {url}...", flush=True)
        await page.goto(url, timeout=60000)
        await page.wait_for_load_state('networkidle')

        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Save HTML
        with open('debug_blog.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("✅ Saved to debug_blog.html", flush=True)

        # Try to find content
        print("\n🔍 Looking for content areas...", flush=True)

        for selector in ['.entry-content', 'article .content', '.post-content', 'article', 'main', '.main-content']:
            elements = soup.select(selector)
            if elements:
                print(f"   ✓ Found {len(elements)} elements matching '{selector}'", flush=True)
                if elements[0]:
                    text = elements[0].get_text()[:200]
                    print(f"      Preview: {text[:100]}...", flush=True)
            else:
                print(f"   ✗ No elements found for '{selector}'", flush=True)

        await browser.close()

    print("\n✅ Debug complete!", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
