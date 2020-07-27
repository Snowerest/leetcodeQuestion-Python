def merge(left: list, right: list) -> list:
    l, r = 0, 0
    ll, rl = len(left) - 1, len(right) - 1
    result = []
    while True:
        if l > ll or r > rl:
            break
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result


def merge_sort(nums: list) -> list:
    l = len(nums)
    if l <= 1:
        return nums
    mid = l // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)
