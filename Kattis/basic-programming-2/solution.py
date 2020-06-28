from collections import Counter


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n = a[0]
    t = a[1]
    if t == 1:
        print(compute_xy(b))
    if t == 2:
        print(compute_duplicates(b))
    if t == 3:
        print(compute_int(b, n))
    if t == 4:
        compute_median(b)
    if t == 5:
        compute_nums_between(b)


def compute_xy(b):
    b.sort()
    for i in range(1, 7777):
        if i in b and (7777 - i) in b:
            return "Yes"
    return "No"


def compute_duplicates(b):
    if len(b) == len(set(b)):
        return "Unique"
    else:
        return "Contains duplicate"


def compute_int(b, n):
    x, y = Counter(b).most_common(1)[0]
    if y > n/2:
        return x
    else:
        return -1


def compute_median(b):
    a = sorted(b)
    index = len(b) // 2

    if len(b) % 2 == 1:
        print(a[index])
    else:
        print("{0} {1}".format(a[index - 1], a[index]))


def compute_nums_between(b):
    a = list(filter(lambda x: x >= 100 and x <= 999, sorted(b)))
    print(*a, sep=' ')


main()
