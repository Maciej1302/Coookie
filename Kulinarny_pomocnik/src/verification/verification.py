import re
from datetime import datetime

def date_verification(v1):
    input_date = v1.strip()
    if is_valid_date(input_date):
        return True
    else:
        return False

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def email_verification(e1):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, e1) or e1 == " ":
        return False
    else:
        return True

def name_verification(data):
    if data == "":
        return False

    if not data[0].isupper() or data[1:].isupper():
        return False
    for char in data[1:]:
        if not char.isalpha() or char.isupper():
            return False

    return True

def password_verification(password):
    if len(password) < 8 or password == " ":
        return False

    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
        return False

    return True