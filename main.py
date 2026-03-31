from src.scraper import WebScraper
import json

def main():
    target_url = "https://news.ycombinator.com/" # Change to your target site
    print(f"Starting Information Retrieval for: {target_url}...")
    
    bot = WebScraper()
    html = bot.fetch_page(target_url)
    data = bot.parse_data(html)
    
    if data:
        # Save results to a JSON file (Data Management)
        with open('data/results.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully extracted {len(data)} records.")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()