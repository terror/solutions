s = input()
n = 13
d = {}
c = 0

for i in range(0, len(s), 3):
  if s[i:i + 3] in d:
    d[s[i:i + 3]] += 1
  else:
    d[s[i:i + 3]] = 1

ok = True
for key, val in d.items():
  if val > 1:
    ok = False
    break

if not ok:
  print("GRESKA")
else:
  keys = ['P', 'K', 'H', 'T']
  ans = []
  for i in keys:
    found = False
    diff = 0
    for key, val in d.items():
      key = list(key)
      if key[0] == i:
        diff += 1
        found = True
    if not found:
      ans.append(13)
    else:
      ans.append(n - diff)
  print(*ans)
