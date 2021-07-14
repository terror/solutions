import sys

x = 1
for n in sys.stdin:
  if int(n) == 0:
    break
  print("SET", x)
  s = [input() for i in range(int(n))]
  for i in range(len(s)):
    if i % 2 == 0:
      print(s[i])
  for i in range(len(s))[::-1]:
    if i % 2 != 0:
      print(s[i])
  x += 1
