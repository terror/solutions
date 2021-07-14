import sys

s = set()
for i in sys.stdin:
  i = i.split()
  line = []
  for j in i:
    if j.lower() in s:
      line.append('.')
    else:
      line.append(j)
      s.add(j.lower())
  print(*line)
