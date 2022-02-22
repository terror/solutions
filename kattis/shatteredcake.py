# warm up let's go
w = int(input())
N = int(input())

area = 0
for i in range(N):
  a, b = list(map(int, input().split()))
  area += a * b

print(area // w)
