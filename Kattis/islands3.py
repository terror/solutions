dr, dc = [0, 1, -1, 0], [1, 0, 0, -1]

n, m = map(int, input().split())

g = [list(input()) for i in range(n)]


def solve(grid, r, c, c1, c2):
    if r >= n or r < 0 or c >= m or c < 0:
        return 0

    if grid[r][c] != c1 and grid[r][c] != 'C':
        return 0

    grid[r][c] = c2

    for i in range(4):
        solve(grid, r+dr[i], c+dc[i], c1, c2)

    return 1


def main():
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'L':
                ans += solve(g, i, j, 'L', '#')

    return ans


if __name__ == '__main__':
    print(main())
