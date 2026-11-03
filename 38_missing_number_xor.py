def missing_number(nums):
    n = len(nums)
    result = n

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result
