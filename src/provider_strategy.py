from src.provider_factory import DataProviderFactory
from src.cache_manager import CacheManager
from src.logger import SystemLogger

class InformationStrategy:
    def __init__(self, preferred_mode="api"):
        self.mode = preferred_mode
        self.cache = CacheManager()
        self.logger = SystemLogger().get_logger()

    def fetch_current_data(self):
        # 1. Check Cache First
        cached = self.cache.get_cached_data("hn_top_stories")
        if cached:
            return cached

        # 2. If no cache, try the Preferred Mode (API/Scraper)
        provider = DataProviderFactory.get_provider(self.mode)
        data = provider()

        # 3. Fallback logic if Preferred Mode fails
        if not data and self.mode == "api":
            self.logger.warning("Falling back to Web Scraper.")
            fallback_provider = DataProviderFactory.get_provider("scraper")
            data = fallback_provider()
            
        # 4. Save to Cache if we finally got data
        if data:
            self.cache.set_cache("hn_top_stories", data)
            
        return data