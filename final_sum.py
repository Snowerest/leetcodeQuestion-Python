def final_sum(num: int) -> int:
    if num < 10:
        return num
    return final_sum(sum([int(i) for i in str(num)]))
        
