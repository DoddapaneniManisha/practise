def reverse_string(s):
    if not s:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

text = "Python"
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
