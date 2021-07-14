n, l, ans = int(input()), sorted(list(map(int, input().split()))), 2e5

for i in range(n):
  if l[i] > i + 1:
    print("impossible")
    exit()
  ans = min(ans, l[i] / (i + 1))
print(ans)
