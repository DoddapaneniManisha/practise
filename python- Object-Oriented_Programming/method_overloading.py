class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math = MathOperations()
result1 = math.add(1, 2)
result2 = math.add(1, 2, 3)

print(result1)
print(result2)
