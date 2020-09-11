def main():
    for _ in range(int(input())): print(solve(int(input())))


def solve(n):
    nums = sorted([input() for i in range(n)])
    for i in range(len(nums)-1):
        if nums[i+1].startswith(nums[i]): return "NO"
    return "YES"


if __name__ == '__main__':
    main()
