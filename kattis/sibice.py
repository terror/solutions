import math

n, w, h = list(map(int, input().split()))
tot = math.sqrt(w**2 + h**2)

for i in range(n):
  length = int(input())
  if length <= tot:
    print("DA")
  else:
    print("NE")
