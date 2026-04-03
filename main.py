from src.scraper import WebScraper
from src.data_handler import DataHandler
from src.validator import DataValidator
from src.logger import SystemLogger
from datetime import datetime

def main():
    # Initialize Logger
    sys_logger = SystemLogger().get_logger()
    sys_logger.info("--- Pipeline Execution Started ---")
    
    target_url = "https://news.ycombinator.com/" 
    
    try:
        # 1. Extraction
        bot = WebScraper()
        sys_logger.info(f"Fetching data from: {target_url}")
        raw_html = bot.fetch_page(target_url)
        raw_data = bot.parse_data(raw_html)
        sys_logger.info(f"Extracted {len(raw_data)} raw records.")

        # 2. Validation
        validator = DataValidator()
        clean_data = validator.validate_batch(raw_data)
        sys_logger.info(f"Validation successful: {len(clean_data)} records kept.")

        # 3. Management
        if clean_data:
            handler = DataHandler()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            handler.save_as_json(clean_data, f"clean_data_{timestamp}.json")
            sys_logger.info("Data persistence layer finalized.")
        
        sys_logger.info("--- Pipeline Execution Completed Successfully ---")

    except Exception as e:
        sys_logger.error(f"Critical System Failure: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()