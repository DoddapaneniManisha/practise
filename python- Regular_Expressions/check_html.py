import re

html = "<p>This is a <strong>bold</strong> statement.</p>"
pattern = r'<.*?>'
tags = re.findall(pattern, html)
print("HTML tags:", tags)
