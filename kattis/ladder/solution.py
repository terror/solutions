from math import sin, radians, ceil
h, v = list(map(int, input().split()))
print(ceil(h/sin(radians(v))))
