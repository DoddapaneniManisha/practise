import re

text = "Apples,Oranges;Bananas,Cherries"
pattern = r'[,;]'
parts = re.split(pattern, text)
print("Fruits:", parts)
