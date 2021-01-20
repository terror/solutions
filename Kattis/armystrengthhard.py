n = int(input())

for _ in range(n):
    x = input()
    g, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)

    w = 0
    q = 0

    while w < g and q < m:
        if a[w] < b[q]:
            w += 1
        else:
            q += 1

    if w == g:
        print("MechaGodzilla")
    else:
        print("Godzilla")
