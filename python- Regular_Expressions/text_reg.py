import re

text = "Python is great. Java is okay. C++ is awesome."
pattern = r'Java|C\+\+'
replacement = "JavaScript"
new_text = re.sub(pattern, replacement, text)
print(new_text)
