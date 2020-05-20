def main():
    nums = sorted(list(map(int, input().split())))
    diff = min(nums[1] - nums[0], nums[2] - nums[1])
    print(solve(nums, diff))


def solve(nums, diff):
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > diff:
            return nums[i-1] + diff
    return nums[len(nums) - 1] + diff


main()
