t = int(input())
for i in range(t):
  n, mx, ans = int(input()), 0, 0
  for j in range(n):
    a, b, c = map(int, input().split())
    res = -a * (b / (2 * a)) + b * (b / (2 * a)) + c
    if res > mx: mx, ans = res, j + 1
  print(ans)
