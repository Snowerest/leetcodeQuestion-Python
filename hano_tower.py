def hano_tower(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 3
    return 2*hano_tower(n-1) + 1
