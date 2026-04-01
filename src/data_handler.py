import json
import csv
import os
from datetime import datetime

class DataHandler:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        # Ensure the data directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_as_json(self, data, filename="results.json"):
        """Saves data to a JSON file for structured web use."""
        path = os.path.join(self.output_dir, filename)
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Successfully saved JSON to {path}")
        except Exception as e:
            print(f"Error saving JSON: {e}")

    def save_as_csv(self, data, filename="results.csv"):
        """Saves data to a CSV file for business intelligence/Excel use."""
        if not data:
            return
            
        path = os.path.join(self.output_dir, filename)
        # Extract headers from the keys of the first dictionary
        headers = data[0].keys()
        
        try:
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            print(f"Successfully saved CSV to {path}")
        except Exception as e:
            print(f"Error saving CSV: {e}")