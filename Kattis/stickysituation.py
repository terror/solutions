def main():
    n = int(input())
    s = sorted(list(map(int, input().split())))
    print("possible" if check(s) else "impossible")


def check(s):
    for i in range(len(s)-2):
        if s[i] + s[i+1] > s[i+2]:
            return True
    return False


main()
