import sys

speed = 0
d = 0
prev = 0
for i in sys.stdin:
  i = list(map(str, i.split()))
  t = i[0].split(':')
  h = 0
  m = 0
  s = 0
  for j in range(len(t)):
    if j == 0:
      h += int(t[0])
    if j == 1:
      m += int(t[1])
    if j == 2:
      s += int(t[2])
  time = (h) + (m / 60) + (s / 3600)
  if time < prev:
    prev += time

  d += (time - prev) * speed
  if len(i) == 2:
    speed = int(i[1])
  else:
    print('{} {:.2f} km'.format(i[0], d))
  prev = time
