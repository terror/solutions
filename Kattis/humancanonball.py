from math import sin, cos, radians
for i in range(int(input())):
  v, theta, x, h1, h2 = list(map(float, input().split()))
  t = x / v / cos(radians(theta))
  yt = v * t * sin(radians(theta)) - (1 / 2 * 9.8 * t**2)
  print("Safe" if h2 - yt >= 1 and yt - h1 >= 1 else "Not safe")
