from src.scraper import WebScraper
from src.data_handler import DataHandler

def main():
    # Configuration
    target_url = "https://news.ycombinator.com/" 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"--- Information Systems Pipeline Started ---")
    
    # 1. Extraction (The Scraper)
    bot = WebScraper()
    raw_html = bot.fetch_page(target_url)
    processed_data = bot.parse_data(raw_html)
    
    # 2. Management (The Handler)
    if processed_data:
        handler = DataHandler()
        
        # Save in multiple formats to demonstrate versatility
        handler.save_as_json(processed_data, f"headlines_{timestamp}.json")
        handler.save_as_csv(processed_data, f"headlines_{timestamp}.csv")
        
        print(f"Pipeline Complete: {len(processed_data)} records managed.")
    else:
        print("Pipeline Failed: No data retrieved.")

if __name__ == "__main__":
    main()