def main():
    x, y = c(input()), c(input())
    if x*y == 0:
        return 0
    return "S"+("(S"*((x*y)-1))+"(0"+(")"*(x*y))


def c(x):
    return x.count('S')


if __name__ == '__main__':
    print(main())
