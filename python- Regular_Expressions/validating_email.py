import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+$'
    return bool(re.match(pattern, email))

emails = ["example@example.com", "invalid-email", "john@example.org"]
for email in emails:
    if is_valid_email(email):
        print(email, "is a valid email.")
    else:
        print(email, "is not a valid email.")
