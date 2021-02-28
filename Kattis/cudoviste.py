from collections import Counter

n, m = map(int, input().split())
grid, d = [list(input()) for _ in range(n)], Counter()
for i in range(n - 1):
    for j in range(m - 1):
        if (
            grid[i][j] == "#"
            or grid[i][j + 1] == "#"
            or grid[i + 1][j] == "#"
            or grid[i + 1][j + 1] == "#"
        ):
            continue
        d[
            int(grid[i][j] == "X")
            + int(grid[i + 1][j] == "X")
            + int(grid[i][j + 1] == "X")
            + int(grid[i + 1][j + 1] == "X")
        ] += 1
print(*[d[i] for i in range(5)], sep="\n")
