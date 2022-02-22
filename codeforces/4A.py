import math

m, k = map(int, input().split())
a = m * k
if a % 2 == 0:
  print(a // 2)
else:
  print(math.floor(a / 2))
