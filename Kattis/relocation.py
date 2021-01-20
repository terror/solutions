N, Q = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(Q):
    x, y, z = list(map(int, input().split()))
    if x == 1:
        c[y-1] = z
    else:
        print(abs(c[y-1] - c[z-1]))
