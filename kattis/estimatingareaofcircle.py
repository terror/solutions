from math import pi
while True:
  r, m, c = list(map(float, input().split()))
  if r == 0:
    break
  a = pi * (r**2)
  e = c / m * (4 * (r**2))
  print("{0} {1}".format(a, e))
