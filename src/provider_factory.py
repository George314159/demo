from src.scraper import WebScraper
from src.api_client import HackerNewsAPI

class DataProviderFactory:
    @staticmethod
    def get_provider(mode="api"):
        if mode == "api":
            return HackerNewsAPI().get_top_stories
        else:
            # Wrap the scraper to return a similar format
            scraper = WebScraper()
            def scraper_wrapper():
                html = scraper.fetch_page("https://news.ycombinator.com/")
                data = scraper.parse_data(html)
                for item in data:
                    item["source"] = "Web Scraper"
                return data
            return scraper_wrapper