import pytest
from validation import validate_email

def test_valid_email():
    assert validate_email("test@knu.ac.kr") == []

def test_invalid_email_format():
    assert validate_email("invalid-email.com") == ["INVALID_EMAIL"]

def test_empty_email():
    assert validate_email("") == ["INVALID_EMAIL"]