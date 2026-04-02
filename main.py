from src.scraper import WebScraper
from src.data_handler import DataHandler
from src.validator import DataValidator
from datetime import datetime

def main():
    target_url = "https://news.ycombinator.com/" 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"--- Information Systems Pipeline: Day 3 ---")
    
    # 1. Extraction
    bot = WebScraper()
    raw_html = bot.fetch_page(target_url)
    raw_data = bot.parse_data(raw_html)
    
    # 2. Validation & Cleaning (NEW)
    validator = DataValidator()
    clean_data = validator.validate_batch(raw_data)
    
    # 3. Management & Persistence
    if clean_data:
        handler = DataHandler()
        handler.save_as_json(clean_data, f"clean_data_{timestamp}.json")
        handler.save_as_csv(clean_data, f"clean_data_{timestamp}.csv")
        print(f"Pipeline Success.")
    else:
        print("Pipeline Stopped: No valid data after cleaning.")

if __name__ == "__main__":
    main()