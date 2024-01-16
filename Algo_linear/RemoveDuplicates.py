def remove_duplicates(nums):
    # unique = []
    # for num in nums:
    #     if num not in unique:
    #         unique.append(num)
    # return unique

    # Dictionary is order inserted
    return list(dict.fromkeys(nums))