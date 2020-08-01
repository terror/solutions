import sys


def main():
    for i in sys.stdin:
        if len(i.split()) == 1:
            break
        a, b, c = list(map(int, i.split()))
        b, c = int(str(b), a), int(str(c), a)
        ans = x(int(b) % int(c), a)
        print(ans)


def x(n, b):
    s = "0123456789"
    return s[n] if n < b else x(n//b, b)+s[n % b]


main()
