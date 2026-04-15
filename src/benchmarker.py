import time
from src.provider_factory import DataProviderFactory
from src.cache_manager import CacheManager
from src.logger import SystemLogger

class SystemBenchmarker:
    """
    Evaluates the latency of different information retrieval tiers.
    Provides empirical evidence for system optimization.
    """
    def __init__(self):
        self.logger = SystemLogger().get_logger()
        self.cache = CacheManager()

    def run_benchmark(self):
        results = {}

        # 1. Measure Cache Speed
        start = time.perf_counter()
        _ = self.cache.get_cached_data("hn_top_stories")
        results['Cache'] = time.perf_counter() - start

        # 2. Measure API Speed
        api_provider = DataProviderFactory.get_provider("api")
        start = time.perf_counter()
        _ = api_provider()
        results['Official API'] = time.perf_counter() - start

        # 3. Measure Scraper Speed
        scraper_provider = DataProviderFactory.get_provider("scraper")
        start = time.perf_counter()
        _ = scraper_provider()
        results['Web Scraper'] = time.perf_counter() - start

        self.display_report(results)
        return results

    def display_report(self, results):
        print("\n--- PERFORMANCE BENCHMARK REPORT ---")
        for source, duration in results.items():
            print(f"{source:15} | {duration:.4f} seconds")
        print("------------------------------------\n")