from src.provider_factory import DataProviderFactory
from src.validator import DataValidator
from src.logger import SystemLogger

def main():
    logger = SystemLogger().get_logger()
    
    # Switch between 'api' and 'scraper' easily
    MODE = "api" 
    logger.info(f"System operating in {MODE} mode.")

    fetch_data = DataProviderFactory.get_provider(mode=MODE)
    raw_data = fetch_data()

    validator = DataValidator()
    clean_data = validator.validate_batch(raw_data)
    
    # ... rest of your persistence logic ...
    logger.info("Pipeline finalized using Factory Pattern logic.")

if __name__ == "__main__":
    main()