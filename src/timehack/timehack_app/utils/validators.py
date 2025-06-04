import re


def validate_email(email):
    basic_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(basic_pattern, email):
        return False
    return True
