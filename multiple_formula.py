def multiple_formula() -> None:
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d×%d=%d" % (j, i, i*j), end=" ")
        print()
        

if __name__ == "__main__":
    multiple_formula()
