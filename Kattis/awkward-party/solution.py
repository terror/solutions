def main():
    n = int(input())
    nums = map(int, input().split())
    print(find_min(n, nums))


def find_min(n, nums):
    a = {}
    for index, val in enumerate(nums):
        if val in a:
            # get min val between duplicates
            n = min(n, abs(a[val] - index))
            a[val] = index
        else:
            a[val] = index
    return n


main()
