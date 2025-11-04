#!/usr/bin/env python3
"""
Extract ALL historical Netstrata blog posts using AJAX pagination.

This script clicks the "Next" button repeatedly to load all historical posts.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "playwright",
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import asyncio
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Set
import httpx

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


class NetstrataHistoricalExtractor:
    """Extract all historical Netstrata blog posts using AJAX pagination."""

    def __init__(self, output_dir: str = "blogs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.base_url = "https://netstrata.com.au"
        self.blog_url = f"{self.base_url}/news-blog/"

    async def discover_all_urls_ajax(self) -> List[str]:
        """Discover ALL blog URLs by clicking Next button repeatedly."""
        print("🔍 Discovering ALL historical blog URLs using AJAX pagination...", flush=True)
        all_urls: Set[str] = set()

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            )
            page = await context.new_page()

            # Load first page
            print(f"   Loading {self.blog_url}...", flush=True)
            await page.goto(self.blog_url, timeout=60000)
            await page.wait_for_load_state('domcontentloaded')

            page_num = 1
            while True:
                print(f"   Page {page_num}...", end=" ", flush=True)

                # Extract URLs from current view
                html = await page.content()
                soup = BeautifulSoup(html, 'html.parser')
                urls = self._extract_urls_from_page(soup)

                new_urls = urls - all_urls
                all_urls.update(new_urls)
                print(f"found {len(new_urls)} new posts (total: {len(all_urls)})", flush=True)

                # Check if Next button exists and is enabled
                next_button = await page.query_selector('#more_blog_posts')
                if not next_button:
                    print(f"   ✅ No more pages (Next button not found)", flush=True)
                    break

                # Check if button is disabled
                is_disabled = await next_button.get_attribute('disabled')
                if is_disabled:
                    print(f"   ✅ Reached end (Next button disabled)", flush=True)
                    break

                # Click Next and wait for new content
                try:
                    await next_button.click()
                    # Wait for page number to change or new content to load
                    await asyncio.sleep(2)  # Wait for AJAX to load
                    await page.wait_for_load_state('networkidle', timeout=10000)
                    page_num += 1

                    # Rate limiting
                    await asyncio.sleep(2)

                except Exception as e:
                    print(f"   ⚠️  Error clicking Next: {e}", flush=True)
                    break

                # Safety limit
                if page_num > 20:
                    print(f"   ⚠️  Safety limit reached (20 pages)", flush=True)
                    break

            await browser.close()

        urls_list = sorted(list(all_urls))
        print(f"\n✅ Discovered {len(urls_list)} total blog posts across {page_num} pages", flush=True)
        return urls_list

    def _extract_urls_from_page(self, soup: BeautifulSoup) -> Set[str]:
        """Extract blog post URLs from current page content."""
        urls = set()

        # Find blog post containers
        post_containers = soup.select('.news_blog_module_list')

        for container in post_containers:
            links = container.select('a[href]')
            for link in links:
                href = link.get('href', '')
                if not href:
                    continue

                # Make absolute URL
                if href.startswith('/'):
                    href = self.base_url + href
                elif not href.startswith('http'):
                    continue

                # Filter to blog posts only
                if self.base_url in href:
                    if href in [self.blog_url, self.blog_url.rstrip('/')]:
                        continue
                    if '/news-blog/page/' in href or href.endswith('/news-blog/'):
                        continue
                    if '/category/' in href or '/tag/' in href:
                        continue

                    urls.add(href)

        return urls

    async def extract_article(self, url: str) -> Dict[str, Any]:
        """Extract a single blog post (copied from original script)."""
        print(f"📄 Extracting: {url}", flush=True)

        result = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "success": False,
            "content": {
                "title": None,
                "date": None,
                "category": None,
                "author": None,
                "main_content": None,
                "images": []
            }
        }

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            try:
                await page.goto(url, timeout=30000)
                await page.wait_for_load_state('domcontentloaded')

                html = await page.content()
                soup = BeautifulSoup(html, 'html.parser')

                self._extract_title(soup, result)
                self._extract_metadata(soup, result)
                self._extract_images(soup, result)
                self._extract_content(soup, result)

                result["success"] = True

            except Exception as e:
                print(f"   ❌ Error: {e}", flush=True)
                result["error"] = str(e)

            finally:
                await browser.close()

        return result

    def _extract_title(self, soup: BeautifulSoup, result: Dict):
        """Extract title."""
        title = None
        for selector in ['h1.entry-title', 'h1', 'article h1', '.post-title']:
            elem = soup.select_one(selector)
            if elem:
                title = elem.get_text().strip()
                break

        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text().strip()
                title = re.sub(r'\s*[-–|]\s*Netstrata.*$', '', title)

        result["content"]["title"] = title or "Untitled"

    def _extract_metadata(self, soup: BeautifulSoup, result: Dict):
        """Extract date, category, author."""
        # Date
        for selector in ['time', '.entry-date', '.post-date', 'meta[property="article:published_time"]']:
            elem = soup.select_one(selector)
            if elem:
                date_text = elem.get('datetime') or elem.get('content') or elem.get_text()
                result["content"]["date"] = date_text.strip()
                break

        # Category
        for selector in ['.category', '.post-category', 'a[rel="category tag"]']:
            elem = soup.select_one(selector)
            if elem:
                result["content"]["category"] = elem.get_text().strip()
                break

        # Author
        for selector in ['.author', '.post-author', 'meta[name="author"]', 'a[rel="author"]']:
            elem = soup.select_one(selector)
            if elem:
                text = elem.get('content') or elem.get_text()
                result["content"]["author"] = text.strip()
                break

    def _extract_images(self, soup: BeautifulSoup, result: Dict):
        """Extract images."""
        content_area = soup.select_one('article') or soup.select_one('.entry-content') or soup.select_one('main')

        if content_area:
            for img in content_area.select('img'):
                src = img.get('src') or img.get('data-src')
                if src:
                    if src.startswith('//'):
                        src = 'https:' + src
                    elif src.startswith('/'):
                        src = self.base_url + src

                    result["content"]["images"].append({
                        'url': src,
                        'alt': img.get('alt', ''),
                        'local_path': None,
                        'filename': None
                    })

    def _extract_content(self, soup: BeautifulSoup, result: Dict):
        """Extract main content."""
        content_elem = None
        for selector in ['.single_article_content', '.entry-content', 'article .content', '.post-content', 'article']:
            content_elem = soup.select_one(selector)
            if content_elem:
                break

        if not content_elem:
            print("   ⚠️  Could not find content area", flush=True)
            return

        # Replace images with placeholders
        for i, img in enumerate(content_elem.find_all('img')):
            img.replace_with(f"\n\n[IMAGE_{i}]\n\n")

        # Convert to markdown
        markdown = self._html_to_markdown(content_elem)
        markdown = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown)
        markdown = markdown.strip()

        result["content"]["main_content"] = markdown

    def _html_to_markdown(self, element) -> str:
        """Convert HTML to markdown."""
        for tag in element.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            level = int(tag.name[1])
            text = tag.get_text().strip()
            tag.replace_with(f"\n\n{'#' * level} {text}\n\n")

        for p in element.find_all('p'):
            text = p.get_text().strip()
            if text:
                p.replace_with(f"\n\n{text}\n\n")

        for ul in element.find_all('ul'):
            items = []
            for li in ul.find_all('li', recursive=False):
                text = li.get_text().strip()
                if text:
                    items.append(f"- {text}")
            if items:
                ul.replace_with(f"\n\n" + "\n".join(items) + "\n\n")

        for a in element.find_all('a'):
            text = a.get_text().strip()
            href = a.get('href', '')
            if text and href:
                a.replace_with(f"[{text}]({href})")

        for br in element.find_all('br'):
            br.replace_with('\n')

        return element.get_text()

    def _create_slug(self, url: str) -> str:
        """Create slug from URL."""
        path = url.replace(self.base_url, '').strip('/')
        slug = re.sub(r'[^\w\s-]', '', path)
        slug = re.sub(r'[-\s]+', '_', slug)
        return slug[:100] or "untitled"

    async def save_article(self, result: Dict):
        """Save article to markdown."""
        if not result["success"]:
            return

        slug = self._create_slug(result["url"])
        article_folder = self.output_dir / slug
        article_folder.mkdir(exist_ok=True)

        # Save metadata
        metadata_file = article_folder / "metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        # Save markdown
        md_file = article_folder / f"{slug}.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# {result['content']['title']}\n\n")
            if result['content'].get('date'):
                f.write(f"**Date:** {result['content']['date']}\n")
            if result['content'].get('author'):
                f.write(f"**Author:** {result['content']['author']}\n")
            f.write(f"**Source:** {result['url']}\n\n")
            f.write("---\n\n")

            main_content = result["content"]["main_content"] or ""

            # Replace image placeholders
            for i, img in enumerate(result["content"]["images"]):
                placeholder = f"[IMAGE_{i}]"
                if img.get("local_path"):
                    alt = img.get("alt", f"Image {i+1}")
                    main_content = main_content.replace(placeholder, f"![{alt}]({img['local_path']})")
                else:
                    main_content = main_content.replace(placeholder, "")

            f.write(main_content)

        print(f"   ✅ Saved to: {article_folder}/", flush=True)

    async def extract_all(self):
        """Discover and extract all historical blog posts."""
        # Discover URLs
        urls = await self.discover_all_urls_ajax()

        # Save URL list
        urls_file = self.output_dir / "all_urls.txt"
        with open(urls_file, 'w') as f:
            for url in urls:
                f.write(url + '\n')
        print(f"📝 Saved URL list to {urls_file}\n", flush=True)

        # Extract each article
        print(f"📥 Starting extraction of {len(urls)} articles...\n", flush=True)

        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] ", end="", flush=True)
            result = await self.extract_article(url)
            if result["success"]:
                await self.save_article(result)

            # Rate limiting
            await asyncio.sleep(4)

            # Breaks
            if i % 10 == 0:
                print(f"   ⏸️  Taking a 10-second break after {i} articles...", flush=True)
                await asyncio.sleep(10)

        print(f"\n✅ Extraction complete! {len(urls)} articles saved to {self.output_dir}/", flush=True)


async def main():
    """Main entry point."""
    extractor = NetstrataHistoricalExtractor()
    await extractor.extract_all()


if __name__ == "__main__":
    asyncio.run(main())
