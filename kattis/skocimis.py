a, b, c = list(map(int, input().split()))

tot = 0

if abs(a - b) < abs(c - b):
  tot = abs(c - b)
else:
  tot = abs(a - b)

print(tot - 1)
