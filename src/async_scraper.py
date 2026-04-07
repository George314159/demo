import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
from src.logger import SystemLogger

class AsyncScraper:
    def __init__(self):
        self.logger = SystemLogger().get_logger()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Professional-Consultant/1.0'
        }

    async def fetch_page(self, session, url):
        """Asynchronously fetches a single page."""
        try:
            async with session.get(url, headers=self.headers, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    self.logger.info(f"Successfully retrieved: {url}")
                    return html
                else:
                    self.logger.warning(f"Failed {url} with status: {response.status}")
                    return None
        except Exception as e:
            self.logger.error(f"Async error fetching {url}: {e}")
            return None

    async def run_pipeline(self, urls):
        """Orchestrates multiple concurrent requests."""
        self.logger.info(f"Initiating Concurrent Retrieval for {len(urls)} targets.")
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_page(session, url) for url in urls]
            pages = await asyncio.gather(*tasks)
            return [p for p in pages if p]