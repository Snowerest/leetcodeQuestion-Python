def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    mid = nums[0]
    return quick_sort([i for i in nums if i < mid]) + [mid] + quick_sort([i for i in nums if i > mid])
