import sys
from collections import Counter

d = Counter()

for i in sys.stdin:
  if i.rstrip() == '': break
  d[str(i).replace('\n', '')] += 1

tot = sum(d.values())

for i in sorted([key for key, val in d.items()]):
  print('{} {:.6f}'.format(i, (100 * d[i]) / tot))
