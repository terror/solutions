scores = {}
d = {}
time = 0
solved = 0

while True:
  n = list(map(str, input().split()))
  if int(n[0]) == -1:
    break
  if n[2] == 'right':
    scores[n[1]] = int(n[0])
    solved += 1
  if n[1] in d:
    d[n[1]] += 1
  else:
    d[n[1]] = 1

for key, val in scores.items():
  if key in d:
    if d[key] == 1:
      time += val
    else:
      time += (val + (20 * (d[key] - 1)))

print("{0} {1}".format(solved, time))
