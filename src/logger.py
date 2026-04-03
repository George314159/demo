import logging
import os
from datetime import datetime

class SystemLogger:
    """
    Provides centralized logging for the information retrieval pipeline.
    Essential for 'System Auditing' and 'Error Diagnostics.'
    """
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
        # Create a unique log file for each run or a daily log
        log_filename = f"pipeline_{datetime.now().strftime('%Y%m%d')}.log"
        log_path = os.path.join(self.log_dir, log_filename)

        # Configure the logging format
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler() # Also prints to console
            ]
        )
        self.logger = logging.getLogger("DataPipeline")

    def get_logger(self):
        return self.logger