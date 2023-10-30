def list_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + list_sum(arr[1:])

numbers = [1, 2, 3, 4, 5]
result = list_sum(numbers)
print("Sum of list elements:", result)
