def binary_search(arr, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)

array = [1, 2, 3, 4, 5, 6, 7, 8]
result = binary_search(array, 5, 0, len(array) - 1)
print("Index of 5:", result)
