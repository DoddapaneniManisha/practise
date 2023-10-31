import re

text = "Contact me at example@example.com or john@example.org."
pattern = r'\S+@\S+'
matches = re.findall(pattern, text)
print("Email addresses found:", matches)
