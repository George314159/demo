import requests
from src.logger import SystemLogger

class HackerNewsAPI:
    """
    Official API Client for Hacker News.
    Demonstrates 'Integration Engineering' skills.
    """
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.logger = SystemLogger().get_logger()

    def get_top_stories(self, limit=10):
        try:
            # 1. Fetch IDs of top stories
            response = requests.get(f"{self.base_url}/topstories.json")
            ids = response.json()[:limit]
            
            stories = []
            for item_id in ids:
                # 2. Fetch details for each ID
                item_data = requests.get(f"{self.base_url}/item/{item_id}.json").json()
                stories.append({
                    "title": item_data.get("title"),
                    "timestamp": item_data.get("time"),
                    "source": "Official API"
                })
            
            self.logger.info(f"API successfully retrieved {len(stories)} stories.")
            return stories
        except Exception as e:
            self.logger.error(f"API retrieval failure: {e}")
            return []