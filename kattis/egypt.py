import sys

for i in sys.stdin:
  i = sorted(list(map(int, i.split())))
  if i[0] == 0:
    break
  print("right" if i[0]**2 + i[1]**2 == i[2]**2 else "wrong")
