def final_sum(num: int) -> list:
    if num < 10:
        return [num]
    s = sum([int(i) for i in str(num)])
    return [num] + final_sum(s)
