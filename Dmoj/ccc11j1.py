n, m, d = int(input()), int(input()), {
    "TroyMartian": [3, -4, 0, 0],
    "VladSaturnian": [-6, 2, 0, 0],
    "GraemeMercurian": [-2, -3, 0, 0]
}

for i in range(2):
  curr = n if i == 0 else m
  for k, v in d.items():
    if i == 0:
      if v[0] < 0:
        if curr <= abs(v[0]):
          v[2] = 1
      else:
        if curr >= v[0]:
          v[2] = 1
    else:
      if v[1] < 0:
        if curr <= abs(v[1]):
          v[3] = 1
      else:
        if curr >= v[1]:
          v[3] = 1

for k, v in d.items():
  if v[2] == 1 and v[3] == 1:
    print(k)
