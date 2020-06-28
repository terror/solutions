import sys

d = {}
for i in sys.stdin:
    if i.rstrip() == '':
        break
    i = str(i).replace('\n', '')
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
names = sorted([key for key, val in d.items()])
tot = 0
for key, val in d.items():
    tot += val
for i in names:
    print('{} {:.6f}'.format(i, (100*d[i])/tot))
