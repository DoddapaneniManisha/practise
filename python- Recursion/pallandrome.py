import re

def is_palindrome(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = "A man, a plan, a canal, Panama"
result = is_palindrome(text)
print(f'"{text}" is a palindrome:', result)
