def main():
    print(sum([int(x) for x in list(str(fac(100)))]))


def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)


main()
