def final_multipy(num: int) -> int:
    if num < 10:
        return num
    n = 1
    for i in str(num):
        n *= int(i)
    return final_multipy(n)
