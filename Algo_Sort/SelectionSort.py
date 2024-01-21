def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j
        nums[smallest], nums[i] = nums[i], nums[smallest]
    return nums
