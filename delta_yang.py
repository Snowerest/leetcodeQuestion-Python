def delta_yang(line: int) -> None:
    if not line:
        print(None)
        return
    if line == 1:
        print([1])
        return
    if line == 2:
        print([1, 1])
        return
    queue = [1, 1]
    for i in range(line):
        tmp_q = [1]
        if i == 0:
            print([1])
            continue
        if i == 1:
            print([1, 1])
            continue
        for j in range(1, len(queue)):
            tmp_q.append(queue[j-1]+queue[j])
        tmp_q.append(1)
        print(tmp_q)
        queue = tmp_q
        
        
if __name__ == "__main__":
    delta_yang(10)
  
