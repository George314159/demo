from src.provider_strategy import InformationStrategy
from src.validator import DataValidator
from src.data_handler import DataHandler
from src.logger import SystemLogger

def main():
    logger = SystemLogger().get_logger()
    
    # The system now handles the "How" behind the scenes
    strategy = InformationStrategy(preferred_mode="api")
    raw_data = strategy.fetch_current_data()

    if raw_data:
        # Reusing our Week 2 & 3 modules
        clean_data = DataValidator().validate_batch(raw_data)
        DataHandler().save_as_json(clean_data)
        logger.info("Pipeline finalized successfully.")
    else:
        logger.error("All data retrieval strategies exhausted.")

if __name__ == "__main__":
    main()