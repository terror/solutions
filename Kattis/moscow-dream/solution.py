def main():
    *problems, n = list(map(int, input().split()))
    print(solve(problems, n))


def solve(problems, n):
    if n >= 3 and 0 not in problems:
        if n <= sum(problems):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


main()
