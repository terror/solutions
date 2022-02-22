d = {}
for i in range(int(input())):
  team = tuple(map(str, input().split()))
  if team[0] not in d:
    d[team[0]] = team[1]

c = 0
for key, val in d.items():
  print(key, val)
  c += 1
  if c == 12:
    break
