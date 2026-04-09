import pytest
from src.validator import DataValidator
from src.scraper import WebScraper

def test_data_validation_clean_text():
    """Tests if the validator correctly removes extra whitespace and non-ASCII."""
    validator = DataValidator()
    raw_text = "  Hello   World! \n  "
    cleaned = validator.clean_text(raw_text)
    assert cleaned == "Hello World!"

def test_is_valid_record_pass():
    """Tests if a valid record passes the schema check."""
    validator = DataValidator()
    record = {"title": "Valid News Title", "timestamp": "Wed Apr 8 10:00:00 2026"}
    assert validator.is_valid_record(record) is True

def test_is_valid_record_fail_missing_key():
    """Tests if a record with a missing key is rejected."""
    validator = DataValidator()
    record = {"title": "Missing Timestamp"}
    assert validator.is_valid_record(record) is False

def test_is_valid_record_fail_short_title():
    """Tests if a record with a too-short title is rejected."""
    validator = DataValidator()
    record = {"title": "Hi", "timestamp": "2026-04-08"}
    assert validator.is_valid_record(record) is False