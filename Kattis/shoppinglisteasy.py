from collections import Counter


def main():
    n, m = map(int, input().split())
    d = Counter()
    for _ in range(n):
        d += Counter(list(map(str, input().split())))
    ans = [k for k in d if d[k] == n]
    print(len(ans), *sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
