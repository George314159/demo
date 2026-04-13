from src.provider_factory import DataProviderFactory
from src.logger import SystemLogger

class InformationStrategy:
    """
    Coordinates which data source to use based on system state.
    Demonstrates 'Orchestration' skills in Information Systems.
    """
    def __init__(self, preferred_mode="api"):
        self.mode = preferred_mode
        self.logger = SystemLogger().get_logger()

    def fetch_current_data(self):
        self.logger.info(f"Executing data retrieval strategy: {self.mode}")
        
        provider = DataProviderFactory.get_provider(self.mode)
        data = provider()

        # Fallback Logic: If API fails, try the Scraper automatically
        if not data and self.mode == "api":
            self.logger.warning("API Strategy failed. Falling back to Web Scraper.")
            fallback_provider = DataProviderFactory.get_provider("scraper")
            data = fallback_provider()
            
        return data