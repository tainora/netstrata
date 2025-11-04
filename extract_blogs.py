#!/usr/bin/env python3
"""
Netstrata Blog Extraction Script

Extracts all blog posts from https://netstrata.com.au/news-blog/ and saves them
as markdown files with images downloaded locally.

Usage:
    uv run extract_blogs.py
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
from typing import Dict, List, Any
import httpx

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


class NetstrataExtractor:
    """Extract Netstrata blog posts to markdown."""

    def __init__(self, output_dir: str = "blogs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.base_url = "https://netstrata.com.au"
        self.blog_url = f"{self.base_url}/news-blog/"

    async def discover_all_urls(self) -> List[str]:
        """Discover all blog post URLs by loading each page directly."""
        print("🔍 Discovering blog post URLs...", flush=True)
        all_urls = set()

        # We know there are 13 pages from earlier analysis
        # Rather than detecting it, let's just scan until we get no more results
        total_pages = 13  # From manual inspection

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            )
            page = await context.new_page()

            print(f"   Scanning up to {total_pages} pages...", flush=True)

            # Scan each page
            for page_num in range(1, total_pages + 1):
                print(f"   Page {page_num}/{total_pages}...", end=" ", flush=True)

                # Construct page URL
                if page_num == 1:
                    page_url = self.blog_url
                else:
                    # Try common pagination patterns
                    page_url = f"{self.blog_url}page/{page_num}/"

                try:
                    await page.goto(page_url, timeout=30000)
                    await page.wait_for_load_state('domcontentloaded')

                    # Get HTML
                    html = await page.content()
                    soup = BeautifulSoup(html, 'html.parser')

                    # Extract URLs
                    urls = self._extract_urls_from_page(soup)

                    if not urls:
                        print(f"no posts found, stopping", flush=True)
                        break

                    all_urls.update(urls)
                    print(f"found {len(urls)} posts (total: {len(all_urls)})", flush=True)

                    # Rate limiting
                    if page_num < total_pages:
                        await asyncio.sleep(3)

                except Exception as e:
                    print(f"error: {e}", flush=True)
                    break

            await browser.close()

        print(f"✅ Discovered {len(all_urls)} total blog posts", flush=True)
        return list(all_urls)

    def _find_total_pages(self, soup: BeautifulSoup) -> int:
        """Find total number of pages from pagination."""
        # Look for .max-page span
        max_page_elem = soup.select_one('.max-page')
        if max_page_elem:
            try:
                return int(max_page_elem.get_text().strip())
            except ValueError:
                pass

        # Fallback: Look for pagination text like "Page 1 of 13"
        pagination_text = soup.find(string=re.compile(r'Page \d+ of \d+'))
        if pagination_text:
            match = re.search(r'Page \d+ of (\d+)', pagination_text)
            if match:
                return int(match.group(1))

        return 1

    def _extract_urls_from_page(self, soup: BeautifulSoup) -> List[str]:
        """Extract blog post URLs from current page."""
        urls = []

        # Find blog post containers
        post_containers = soup.select('.news_blog_module_list')

        for container in post_containers:
            # Find links within each container
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

                # Filter to only blog posts (not category pages, news-blog index, etc.)
                if self.base_url in href:
                    # Skip the main blog page and pagination
                    if href == self.blog_url or href == self.blog_url.rstrip('/'):
                        continue
                    if '/news-blog/page/' in href or href.endswith('/news-blog/'):
                        continue
                    # Skip category/tag pages
                    if '/category/' in href or '/tag/' in href:
                        continue

                    urls.append(href)

        return list(set(urls))  # Deduplicate

    async def extract_article(self, url: str) -> Dict[str, Any]:
        """Extract a single blog post."""
        print(f"📄 Extracting: {url}")

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
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            )
            page = await context.new_page()

            try:
                await page.goto(url, timeout=60000)
                await page.wait_for_load_state('networkidle')

                html = await page.content()
                soup = BeautifulSoup(html, 'html.parser')

                # Extract content
                self._extract_title(soup, result)
                self._extract_metadata(soup, result)
                self._extract_images(soup, result)
                self._extract_content(soup, result)

                result["success"] = True

            except Exception as e:
                print(f"   ❌ Error: {e}")
                result["error"] = str(e)

            finally:
                await browser.close()

        return result

    def _extract_title(self, soup: BeautifulSoup, result: Dict):
        """Extract article title."""
        # Try multiple selectors
        title = None
        for selector in ['h1.entry-title', 'h1', 'article h1', '.post-title']:
            title_elem = soup.select_one(selector)
            if title_elem:
                title = title_elem.get_text().strip()
                break

        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text().strip()
                # Clean up
                title = re.sub(r'\s*[-–|]\s*Netstrata.*$', '', title)

        result["content"]["title"] = title or "Untitled"

    def _extract_metadata(self, soup: BeautifulSoup, result: Dict):
        """Extract date, category, author."""
        # Date
        for selector in ['time', '.entry-date', '.post-date', 'meta[property="article:published_time"]']:
            date_elem = soup.select_one(selector)
            if date_elem:
                date_text = date_elem.get('datetime') or date_elem.get('content') or date_elem.get_text()
                result["content"]["date"] = date_text.strip()
                break

        # Category
        for selector in ['.category', '.post-category', 'a[rel="category tag"]']:
            cat_elem = soup.select_one(selector)
            if cat_elem:
                result["content"]["category"] = cat_elem.get_text().strip()
                break

        # Author
        for selector in ['.author', '.post-author', 'meta[name="author"]', 'a[rel="author"]']:
            author_elem = soup.select_one(selector)
            if author_elem:
                author_text = author_elem.get('content') or author_elem.get_text()
                result["content"]["author"] = author_text.strip()
                break

    def _extract_images(self, soup: BeautifulSoup, result: Dict):
        """Extract images from content."""
        # Find main content area
        content_area = soup.select_one('article') or soup.select_one('.entry-content') or soup.select_one('main')

        if content_area:
            for img in content_area.select('img'):
                src = img.get('src') or img.get('data-src')
                if src:
                    # Make absolute URL
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
        """Extract main article content."""
        # Find main content area
        content_elem = None
        for selector in ['.single_article_content', '.entry-content', 'article .content', '.post-content', 'article']:
            content_elem = soup.select_one(selector)
            if content_elem:
                break

        if not content_elem:
            print("   ⚠️  Could not find content area", flush=True)
            return

        # Clone for processing
        content = content_elem

        # Replace images with placeholders
        for i, img in enumerate(content.find_all('img')):
            img.replace_with(f"\n\n[IMAGE_{i}]\n\n")

        # Convert to markdown
        markdown = self._html_to_markdown(content)

        # Clean up whitespace
        markdown = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown)
        markdown = markdown.strip()

        result["content"]["main_content"] = markdown

    def _html_to_markdown(self, element) -> str:
        """Convert HTML to markdown format."""
        # Headers
        for tag in element.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            level = int(tag.name[1])
            text = tag.get_text().strip()
            tag.replace_with(f"\n\n{'#' * level} {text}\n\n")

        # Paragraphs
        for p in element.find_all('p'):
            text = p.get_text().strip()
            if text:
                p.replace_with(f"\n\n{text}\n\n")

        # Lists
        for ul in element.find_all('ul'):
            items = []
            for li in ul.find_all('li', recursive=False):
                text = li.get_text().strip()
                if text:
                    items.append(f"- {text}")
            if items:
                ul.replace_with(f"\n\n" + "\n".join(items) + "\n\n")

        for ol in element.find_all('ol'):
            items = []
            for i, li in enumerate(ol.find_all('li', recursive=False), 1):
                text = li.get_text().strip()
                if text:
                    items.append(f"{i}. {text}")
            if items:
                ol.replace_with(f"\n\n" + "\n".join(items) + "\n\n")

        # Links
        for a in element.find_all('a'):
            text = a.get_text().strip()
            href = a.get('href', '')
            if text and href:
                a.replace_with(f"[{text}]({href})")

        # Line breaks
        for br in element.find_all('br'):
            br.replace_with('\n')

        return element.get_text()

    async def download_images(self, result: Dict, article_folder: Path) -> List[Dict]:
        """Download all images for an article."""
        if not result["content"]["images"]:
            return []

        images_folder = article_folder / "images"
        images_folder.mkdir(exist_ok=True)

        downloaded = []
        async with httpx.AsyncClient(timeout=30.0) as client:
            for i, img_info in enumerate(result["content"]["images"], 1):
                try:
                    response = await client.get(img_info['url'])
                    response.raise_for_status()

                    # Determine extension
                    content_type = response.headers.get('content-type', '')
                    ext = self._get_extension(content_type, img_info['url'])

                    # Create filename
                    filename = f"image_{i:03d}.{ext}"
                    image_path = images_folder / filename

                    # Save
                    with open(image_path, 'wb') as f:
                        f.write(response.content)

                    img_info['local_path'] = f"images/{filename}"
                    img_info['filename'] = filename
                    downloaded.append(img_info)

                except Exception as e:
                    print(f"   ⚠️  Failed to download image {i}: {e}")
                    img_info['download_error'] = str(e)
                    downloaded.append(img_info)

        return downloaded

    def _get_extension(self, content_type: str, url: str) -> str:
        """Determine file extension from content type or URL."""
        if 'png' in content_type:
            return 'png'
        elif 'jpeg' in content_type or 'jpg' in content_type:
            return 'jpg'
        elif 'gif' in content_type:
            return 'gif'
        elif 'webp' in content_type:
            return 'webp'
        else:
            ext = url.split('.')[-1].lower()
            if ext in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
                return 'jpg' if ext == 'jpeg' else ext
            return 'png'

    def _create_slug(self, url: str) -> str:
        """Create slug from URL."""
        # Extract path from URL
        path = url.replace(self.base_url, '').strip('/')
        # Clean up
        slug = re.sub(r'[^\w\s-]', '', path)
        slug = re.sub(r'[-\s]+', '_', slug)
        return slug[:100] or "untitled"

    async def save_article(self, result: Dict):
        """Save article as markdown with metadata."""
        if not result["success"]:
            return

        # Create folder
        slug = self._create_slug(result["url"])
        article_folder = self.output_dir / slug
        article_folder.mkdir(exist_ok=True)

        # Download images
        if result["content"]["images"]:
            result["content"]["images"] = await self.download_images(result, article_folder)

        # Save metadata
        metadata_file = article_folder / "metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        # Save markdown
        md_file = article_folder / f"{slug}.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            # Front matter
            f.write(f"# {result['content']['title']}\n\n")
            if result['content'].get('date'):
                f.write(f"**Date:** {result['content']['date']}\n")
            if result['content'].get('category'):
                f.write(f"**Category:** {result['content']['category']}\n")
            if result['content'].get('author'):
                f.write(f"**Author:** {result['content']['author']}\n")
            f.write(f"**Source:** {result['url']}\n\n")
            f.write("---\n\n")

            # Main content with images
            main_content = result["content"]["main_content"] or ""

            # Replace image placeholders
            for i, img in enumerate(result["content"]["images"]):
                placeholder = f"[IMAGE_{i}]"
                if img.get("local_path"):
                    alt = img.get("alt", f"Image {i+1}")
                    markdown_img = f"![{alt}]({img['local_path']})"
                    main_content = main_content.replace(placeholder, markdown_img)
                else:
                    main_content = main_content.replace(placeholder, "")

            f.write(main_content)

        print(f"   ✅ Saved to: {article_folder}/")

    async def extract_all(self):
        """Discover and extract all blog posts."""
        # Discover URLs
        urls = await self.discover_all_urls()

        # Save URL list
        urls_file = self.output_dir / "all_urls.txt"
        with open(urls_file, 'w') as f:
            for url in urls:
                f.write(url + '\n')
        print(f"📝 Saved URL list to {urls_file}")

        # Extract each article
        print(f"\n📥 Starting extraction of {len(urls)} articles...\n")

        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}]", end=" ")
            result = await self.extract_article(url)
            if result["success"]:
                await self.save_article(result)
            # Rate limit: 3-5 seconds between articles to avoid being banned
            await asyncio.sleep(4)

            # Extra delay every 10 articles
            if i % 10 == 0:
                print(f"   ⏸️  Taking a 10-second break after {i} articles...")
                await asyncio.sleep(10)

        print(f"\n✅ Extraction complete! {len(urls)} articles saved to {self.output_dir}/")


async def main():
    """Main entry point."""
    extractor = NetstrataExtractor()
    await extractor.extract_all()


if __name__ == "__main__":
    asyncio.run(main())
