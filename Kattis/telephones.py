op = lambda a, b: any((a[0] <= b[0] < a[1], b[0] < a[0] and b[1] > a[1], a[0] < b[1] <= a[1]))

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  v = [list(map(int, input().split()))[2:] for _ in range(n)]
  for _ in range(m):
    a = list(map(int, input().split()))
    print(sum([op([a[0], a[0] + a[1]], [b[0], b[0] + b[1]]) for b in v]))
