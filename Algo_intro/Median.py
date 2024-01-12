def median_followers(nums):
    nums = sorted(nums)
    if len(nums) % 2:
        return nums[len(nums)//2]
    return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2