def merge(first: list, second: list) -> list:
    i, j = 0, 0
    fl, sl = len(first), len(second)
    result = []
    while True:
        if i >= fl or j >= sl:
            break
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    result.extend(first[i:])
    result.extend(second[j:])
    return result
