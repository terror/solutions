from math import sqrt

while True:
  d, N = list(map(str, input().split()))

  if int(N) == 0:
    break

  sweet = int(N)
  x = []
  y = []

  for i in range(int(N)):
    x1, y1 = list(map(float, input().split()))
    x.append(x1)
    y.append(y1)

  for i in range(int(N)):
    for j in range(int(N)):
      if i == j:
        continue
      if sqrt(abs(x[i] - x[j])**2 + abs(y[i] - y[j])**2) <= float(d):
        sweet -= 1
        break

  sour = int(N) - sweet
  print("{0} sour, {1} sweet".format(sour, sweet))
