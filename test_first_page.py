#!/usr/bin/env python3
"""Quick test to extract URLs from first page only."""

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
    """Test extraction from first page."""
    url = "https://netstrata.com.au/news-blog/"

    print(f"📄 Fetching {url}...", flush=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("   Loading page...", flush=True)
        await page.goto(url, timeout=60000)
        print("   Waiting for network idle...", flush=True)
        await page.wait_for_load_state('networkidle')

        print("   Parsing HTML...", flush=True)
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Find blog posts
        posts = soup.select('.news_blog_module_list')
        print(f"   Found {len(posts)} post containers", flush=True)

        # Extract URLs
        urls = set()
        for post in posts:
            links = post.select('a[href]')
            for link in links:
                href = link.get('href', '')
                if 'netstrata.com.au' in href and '/news-blog/' not in href:
                    urls.add(href)

        print(f"\n✅ Found {len(urls)} unique blog post URLs:\n", flush=True)
        for i, u in enumerate(sorted(urls)[:10], 1):
            print(f"   {i}. {u}", flush=True)

        if len(urls) > 10:
            print(f"   ... and {len(urls) - 10} more", flush=True)

        await browser.close()

    print(f"\n✅ Test complete!", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
