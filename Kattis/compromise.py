t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    grid = [list(map(int, input())) for i in range(N)]
    ans = ""
    for i in range(M):
        curr = []
        for j in range(N):
            curr.append(grid[j][i])
        if curr.count(0) == curr.count(1):
            ans += "0"
        elif curr.count(0) > curr.count(1):
            ans += "0"
        else:
            ans += "1"
    print(ans)
