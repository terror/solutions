from collections import deque
MXN = int(2e5)


def main():
    for _ in range(int(input())):
        s1, s2, ret = input(), input(), MXN
        for _ in range(3): ret = min(ret, 1+solve(s1, input()))
        print(min(ret, solve(s1, s2)))


def solve(s1, s2):
    a, b = deque(s1), deque(s2)
    while a and b and a[0] == b[0]:
        a.popleft()
        b.popleft()
    return len(a) + len(b)


main()
