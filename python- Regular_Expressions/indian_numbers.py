import re

text = "Call me at +91 (9123) 456-7890"
pattern = r'\+?\d{1,3} \(\d{3}\) \d{3}-\d{4}|\d{3}-\d{4}'
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)
