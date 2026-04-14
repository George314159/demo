import json
import os
import time
from src.logger import SystemLogger

class CacheManager:
    """
    Manages local data caching to optimize system performance.
    Demonstrates 'Latency Reduction' and 'Resource Management.'
    """
    def __init__(self, cache_dir="cache", ttl_seconds=3600):
        self.cache_dir = cache_dir
        self.ttl = ttl_seconds
        self.logger = SystemLogger().get_logger()
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_cached_data(self, cache_key):
        """Retrieves data if it exists and hasn't expired."""
        path = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        if os.path.exists(path):
            file_age = time.time() - os.path.getmtime(path)
            if file_age < self.ttl:
                self.logger.info(f"Cache Hit for '{cache_key}'. Serving local data.")
                with open(path, 'r') as f:
                    return json.load(f)
            else:
                self.logger.info(f"Cache Expired for '{cache_key}'.")
        
        self.logger.info(f"Cache Miss for '{cache_key}'.")
        return None

    def set_cache(self, cache_key, data):
        """Stores fresh data in the cache."""
        path = os.path.join(self.cache_dir, f"{cache_key}.json")
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        self.logger.info(f"Updated cache for '{cache_key}'.")