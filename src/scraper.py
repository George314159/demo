import requests
from bs4 import BeautifulSoup
import time
import random

class WebScraper:
    def __init__(self):
        # Professional scrapers use headers to avoid being blocked
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def fetch_page(self, url):
        """Fetches HTML content with error handling."""
        try:
            # Respectful scraping: add a small random delay
            time.sleep(random.uniform(1, 3))
            
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status() # Raises an error for 4xx/5xx responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_data(self, html):
        """Extracts specific information (Example: News Headlines)."""
        if not html:
            return []
            
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Adjust these selectors based on your Week 1 target site analysis
        for item in soup.find_all('h2'): 
            text = item.get_text(strip=True)
            if text:
                results.append({"title": text, "timestamp": time.ctime()})
        
        return results