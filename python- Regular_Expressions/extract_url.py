import re

text = "Visit my website at https://www.example.com or http://example.org."
pattern = r'https?://\S+'
urls = re.findall(pattern, text)
print("URLs found:", urls)
