import sys

Max = 0
lines = []
for i in sys.stdin:
  if i.strip() == '':
    break
  lines.append(i)
  if len(i) > Max:
    Max = len(i)
P = 0
for i in range(len(lines)):
  if len(lines[i]) != Max and i != len(lines) - 1:
    P += (Max - len(lines[i]))**2

print(P)
