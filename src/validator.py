import re

class DataValidator:
    """
    Ensures the integrity of retrieved information before persistence.
    Focuses on 'Data Cleaning' - a core Information Studies concept.
    """
    
    @staticmethod
    def is_valid_record(record):
        """Checks if a record has all required fields and non-empty data."""
        required_fields = ['title', 'timestamp']
        
        # 1. Check for missing keys
        if not all(key in record for key in required_fields):
            return False
            
        # 2. Check for empty strings or null values
        if not record['title'] or len(record['title'].strip()) < 3:
            return False
            
        return True

    @staticmethod
    def clean_text(text):
        """Removes unnecessary whitespace and special characters."""
        if not text:
            return ""
        # Remove extra whitespace and newlines
        cleaned = " ".join(text.split())
        # Example: Filter out non-ASCII characters if needed
        cleaned = re.sub(r'[^\x00-\x7F]+', '', cleaned)
        return cleaned.strip()

    def validate_batch(self, data_list):
        """Processes a list of records, cleaning and filtering them."""
        valid_records = []
        for record in data_list:
            # Clean the title
            record['title'] = self.clean_text(record.get('title', ''))
            
            if self.is_valid_record(record):
                valid_records.append(record)
        
        print(f"Validation Complete: {len(valid_records)}/{len(data_list)} records passed.")
        return valid_records