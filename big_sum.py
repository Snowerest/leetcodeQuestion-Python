def big_sum(first: str, second: str) -> str:
    flag = 0
    result = ""
    i = 0
    while i < len(first) and i < len(second):
        tmp_num = int(first[::-1][i]) + int(second[::-1][i])
        if flag:
            tmp_num += flag
            flag = 0
        if tmp_num >= 10:
            tmp_num = tmp_num % 10
            flag = 1
        result = "%d%s" % (tmp_num, result)
        i += 1
    if i >= len(first):
        while i < len(second):
            tmp_num = int(second[::-1][i])
            if flag:
                tmp_num += flag
                flag = 0
            if tmp_num >= 10:
                tmp_num = tmp_num % 10
                flag = 1
            result = "%d%s" % (tmp_num, result)
            i += 1
    if i >= len(second):
        while i < len(first):
            tmp_num = int(first[::-1][i])
            if flag:
                tmp_num += flag
                flag = 0
            if tmp_num >= 10:
                tmp_num = tmp_num % 10
                flag = 1
            result = "%d%s" % (tmp_num, result)
            i += 1
    if flag:
        result = "1%s" % result
    return result
