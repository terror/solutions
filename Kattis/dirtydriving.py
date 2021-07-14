n, p = list(map(int, input().split()))
cars = sorted(list(map(int, input().split())))

Max = 0
for i in range(n):
  if p * (i + 1) - cars[i] > Max:
    Max = p * (i + 1) - cars[i]

print(Max + min(cars))
