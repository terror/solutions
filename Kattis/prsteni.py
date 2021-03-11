from fractions import Fraction


def main():
    n, x = int(input()), list(map(int, input().split()))
    for i in x[1:]:
        if x[0] % i == 0:
            print("{}/1".format(x[0] // i))
            continue
        print(Fraction(x[0], i))


if __name__ == "__main__":
    main()
