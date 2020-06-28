N, M = list(map(int, input().split()))
arr = [list(map(str, input())) for i in range(N)]

c = 0
for i in range(M):
    t = 0
    for j in range(N):
        if arr[j][i] == '_':
            t += 1
        if t == N:
            c += 1

print(c+1)
