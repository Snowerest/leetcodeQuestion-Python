def hano(h: int, s: int, e: int) -> None:
    if h == 1:
        print("%d --> %d" % (s, e))
        return
    if h == 2:
        m = 6 - s -  e
        print("%d --> %d" % (s, m))
        print("%d --> %d" % (s, e))
        print("%d --> %d" % (m, e))
        return
    hano(h-1, s, 6 - s - e)
    print("%d --> %d" % (s, e))
    hano(h-1, 6 - s - e, e)
