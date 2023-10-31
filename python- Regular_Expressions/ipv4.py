import re

text = "192.168.1.1 10.0.0.1 256.256.256.256"
pattern = r'^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
matches = re.findall(pattern, text)
print("Valid IPv4 addresses:", matches)
