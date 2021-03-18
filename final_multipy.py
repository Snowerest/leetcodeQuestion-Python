def final_multipy(num: int) -> int:
    if num < 10:
        return num
    n = 1
    for i in str(num):
        n *= int(i)
    return final_multipy(n)


def final_multipy2(num: int) -> int:
    return num if num < 10 else final_multipy2(reduce(lambda x, y: x*y, [int(i) for i in str(num)]))
