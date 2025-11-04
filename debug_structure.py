#!/usr/bin/env python3
"""Debug script to examine the HTML structure of Netstrata blog page."""

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
    """Fetch and examine HTML structure."""
    url = "https://netstrata.com.au/news-blog/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )
        page = await context.new_page()

        print(f"📄 Fetching {url}...")
        await page.goto(url, timeout=60000)
        await page.wait_for_load_state('networkidle')

        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Save HTML for inspection
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("✅ Saved HTML to debug_page.html")

        # Find pagination info
        print("\n🔍 Searching for pagination...")
        pagination_texts = soup.find_all(string=lambda text: text and 'page' in text.lower())
        for text in pagination_texts[:10]:
            print(f"   Found: {text.strip()[:100]}")

        # Find all links
        print("\n🔍 Searching for blog post links...")
        all_links = soup.find_all('a', href=True)
        blog_links = [link for link in all_links if 'netstrata.com.au' in str(link.get('href', ''))]

        print(f"\n   Found {len(all_links)} total links")
        print(f"   Found {len(blog_links)} links to netstrata.com.au")

        # Show first 20 unique links
        unique_hrefs = set()
        for link in blog_links[:50]:
            href = link.get('href', '')
            if href not in unique_hrefs:
                unique_hrefs.add(href)
                print(f"   - {href}")
                if len(unique_hrefs) >= 20:
                    break

        # Find articles
        print("\n🔍 Searching for article elements...")
        articles = soup.find_all('article')
        print(f"   Found {len(articles)} <article> elements")

        # Find common blog containers
        for selector in ['.post', '.blog-post', '.entry', '.post-item', '[class*="post"]']:
            elements = soup.select(selector)
            if elements:
                print(f"   Found {len(elements)} elements matching '{selector}'")

        await browser.close()

    print("\n✅ Debug complete! Check debug_page.html for full HTML")


if __name__ == "__main__":
    asyncio.run(main())
