# test_validation.py
import pytest
from validation import validate_email

# 1. 정상적인 이메일 입력 (성공 케이스)
def test_valid_email():
    assert validate_email("test@knu.ac.kr") == []

# 2. '@'가 없는 잘못된 형식
def test_invalid_email_format():
    assert validate_email("invalid-email.com") == ["INVALID_EMAIL"]

# 3. 빈 문자열이 들어온 경우
def test_empty_email():
    assert validate_email("") == ["INVALID_EMAIL"]