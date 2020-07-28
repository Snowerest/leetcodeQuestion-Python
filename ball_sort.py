def ball_sort(nums: list) -> list:
    ln = len(nums)
    if ln <= 1:
        return nums
    i = 0
    while i < ln:
        j = i
        while j < ln:
            if nums[j] <= nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        i += 1
    return nums
