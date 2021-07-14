from math import sin, cos

p, a, b, c, d, n = list(map(int, input().split()))
arr = [p * (sin(a * i + b) + cos(c * i + d) + 2) for i in range(1, n + 1)]

diff = 0
mx = arr[0]
# linear scan looking for maximum difference
for i in range(1, len(arr)):
  mx = max(mx, arr[i])
  diff = max(diff, mx - arr[i])

print(diff)
