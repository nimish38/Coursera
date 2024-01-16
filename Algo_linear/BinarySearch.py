def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False