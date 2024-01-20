def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(first, second):
    i, j = 0, 0
    sorted_merge = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            sorted_merge.append(first[i])
            i += 1
        else:
            sorted_merge.append(second[j])
            j += 1

    while i<len(first):
        sorted_merge.append(first[i])
        i += 1

    while j<len(second):
        sorted_merge.append(second[j])
        j += 1
    return sorted_merge

merge_sort([3, 2, 1])