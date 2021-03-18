def final_sum(num: int) -> int:
    if num < 10:
        return num
    return final_sum(sum([int(i) for i in str(num)]))
        

def final_sum2(num: int) -> int:
    return num if num < 10 else final_sum(sum([int(i) for i in str(num)]))
