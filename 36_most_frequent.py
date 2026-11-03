def most_frequent(nums):
    if not nums:
        return None

    return max(nums, key=nums.count)
