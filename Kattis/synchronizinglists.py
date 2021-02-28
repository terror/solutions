while True:
    n = int(input())
    if n == 0:
        break
    a, b, ret = (
        [int(input()) for i in range(n)],
        sorted([int(input()) for i in range(n)]),
        [0] * n,
    )
    d = {a[i]: i for i in range(n)}
    a.sort()
    for i in range(n):
        ret[d[a[i]]] = b[i]
    print(*ret, "\n", sep="\n")
