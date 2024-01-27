def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    else:
        if index < 0:
            return False
        if nums[index] > target:
            return find_subset_sum(nums, target, index - 1)
        else:
            result  = find_subset_sum(nums, target, index - 1)
            alt_result = find_subset_sum(nums, target - nums[index], index - 1)
            if result or alt_result:
                return True
            return False
