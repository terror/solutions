def main():
    p, q, s = list(map(int, input().split()))
    print("yes" if lcm(p, q) <= s else "no")


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b / gcd(a, b)


main()
