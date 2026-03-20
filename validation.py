import re

def validate_email(email: str) -> list:
    errors = []
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email or not re.match(email_regex, email):
        errors.append("INVALID_EMAIL")
    return errors