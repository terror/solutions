def main():
    P, N = list(map(int, input().split()))
    s = set()
    print(solve(s, P, N))


def solve(s, P, N):
    for i in range(N):
        s.add(input())
        if len(s) == P:
            return i+1
    return "paradox avoided"


main()
