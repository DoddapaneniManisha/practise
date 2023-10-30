def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(48, 18)
print("GCD of 48 and 18:", result)
