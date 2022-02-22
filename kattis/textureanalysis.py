import sys

x = 1
for i in sys.stdin:
  if i.strip() == "END":
    break
  c, arr, p = 0, [], False
  for j in i:
    if j == "*" and p:
      arr.append(c)
      c = 0
    if j == "*": p = True
    if j == "." and p: c += 1
  print(x, "EVEN" if len(set(arr)) == 1 or sum(arr) == 0 else "NOT EVEN")
  x += 1
