def count_chars(s):
    if not s:
        return 0
    else:
        return 1 + count_chars(s[1:])

text = "Recursive"
result = count_chars(text)
print("Number of characters in the string:", result)
