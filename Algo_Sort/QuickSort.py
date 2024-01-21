def quick_sort(nums, low, high):
    if low < high:
        nums, index = partition(nums, low, high)
        quick_sort(nums, low, index - 1)
        quick_sort(nums, index + 1, high)
    return nums


def partition(nums, low, high):
    pivot, i = high, low
    for j in range(low, high):
        if nums[j] < nums[pivot]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return nums, i

quick_sort([2, 1, 3], 0, 2)