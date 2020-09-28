import sys


def main():
    for i in sys.stdin:
        n, s = int(i), list(input())
        for _ in range(n):
            idx, r = [j for j in range(len(s)) if check(s[j])], 0
            for j in idx:
                s.insert(j+r, '\\')
                r += 1
        print(*s, sep="")


def check(ch):
    if '[' <= ch and ch <= ']' or '!' <= ch and ch <= '*':
        return 1
    return 0


if __name__ == '__main__':
    main()
