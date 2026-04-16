from src.provider_strategy import InformationStrategy
from src.validator import DataValidator
from src.data_handler import DataHandler
from src.logger import SystemLogger
from src.maintenance import SystemMaintenance

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
    # Run maintenance every time, or based on a condition
    janitor = SystemMaintenance()
    janitor.cleanup(max_age_days=7)
    
    logger.info("--- End of Operations ---")

if __name__ == "__main__":
    main()