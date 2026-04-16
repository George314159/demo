from src.maintenance import SystemMaintenance
# ... (existing imports)

def main():
    # ... (existing pipeline logic)
    
    # Run maintenance every time, or based on a condition
    janitor = SystemMaintenance()
    janitor.cleanup(max_age_days=7)
    
    logger.info("--- End of Operations ---")

if __name__ == "__main__":
    main()