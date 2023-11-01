import re

text = "Hello, my email is example@example.com."
pattern = r'\S+@\S+'
match = re.search(pattern, text)
if match:
    print("Email found:", match.group())
