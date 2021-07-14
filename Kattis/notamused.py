import sys

day, d = 1, {}
for i in sys.stdin:
  if i.rstrip() == "":
    break

  i = i.split()

  if i[0] == "OPEN":
    continue

  if i[0] == "CLOSE":
    print("Day {}".format(day))
    ans = {}

    for k, v in d.items():
      tot = 0
      for j in range(len(v)):
        if j % 2 != 0:
          tot += abs(int(v[j]) - int(v[j - 1]))
      ans[k] = tot * 0.10

    for k, v in sorted(ans.items()):
      print("{} ${:.2f}".format(k, v))

    d.clear()
    day += 1

  if i[0] == "ENTER" or i[0] == "EXIT":
    if i[1] not in d:
      d[i[1]] = [i[2]]
    else:
      d[i[1]].append(i[2])
