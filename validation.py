"""Data validation module.

This module provides utility functions for validating user input and
defines standard error constants to prevent magic string occurrences.
"""

import re

# Constant representing an invalid email format error.
INVALID_EMAIL = "INVALID_EMAIL"

def validate_email(email: str) -> list:
    """Validates the format of an email address.

    This function checks if the provided email string matches a standard
    email regular expression. It handles empty inputs and invalid patterns.

    Args:
        email (str): The email address string to be validated.

    Returns:
        list: A list containing error strings if validation fails.
              Returns an empty list if the email is perfectly valid.
    """
    errors = []
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email or not re.match(email_regex, email):
        errors.append(INVALID_EMAIL)
    return errors