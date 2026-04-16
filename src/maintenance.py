import os
import time
from src.logger import SystemLogger

class SystemMaintenance:
    """
    Automates the cleanup of stale logs and expired cache files.
    Demonstrates 'System Hygiene' and 'Storage Optimization.'
    """
    def __init__(self):
        self.logger = SystemLogger().get_logger()
        self.directories = ['logs', 'cache', 'data']

    def cleanup(self, max_age_days=7):
        """Removes files older than max_age_days."""
        self.logger.info(f"Starting System Maintenance (Threshold: {max_age_days} days)")
        now = time.time()
        files_removed = 0

        for directory in self.directories:
            if not os.path.exists(directory):
                continue
                
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                
                # Check file age
                file_age_seconds = now - os.path.getmtime(file_path)
                if file_age_seconds > (max_age_days * 86400):
                    try:
                        os.remove(file_path)
                        self.logger.info(f"Deleted stale file: {file_path}")
                        files_removed += 1
                    except Exception as e:
                        self.logger.error(f"Failed to delete {file_path}: {e}")

        self.logger.info(f"Maintenance Complete. Total files cleared: {files_removed}")
        return files_removed