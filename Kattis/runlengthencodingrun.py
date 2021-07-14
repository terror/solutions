q, s = map(str, input().split())

if q == "E":
  curr, c = s[0], 1
  for i in range(1, len(s) + 1):
    if i == len(s):
      print(curr + str(c), end="")
      break
    if curr != s[i]:
      print(curr + str(c), end="")
      curr, c = s[i], 1
    else:
      c += 1
else:
  for i in range(1, len(s), 2):
    print(s[i - 1] * int(s[i]), end="")
