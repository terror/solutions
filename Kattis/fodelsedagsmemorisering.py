def main():
    n = int(input())
    d = []
    for i in range(n):
        x, y, z = list(map(str, input().split()))
        d.append([x, int(y), z])
    d = sorted(d, key=lambda x: x[1], reverse=True)
    b = set()
    ans = []
    for i in d:
        if i[2] in b:
            continue
        ans.append(i[0])
        b.add(i[2])

    print(len(ans))
    ans.sort()
    print(*ans, sep="\n")


def debug(a):
    for i in reversed(a):
        print(i)


if __name__ == '__main__':
    main()
