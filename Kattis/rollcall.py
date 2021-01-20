import sys

d, n = [], {}
for i in sys.stdin:
    if i.rstrip() == "":
        break
    a, b = map(str, i.split())
    d.append([a, b])
    if a in n:
        n[a] += 1
    else:
        n[a] = 1

d = sorted(d, key=lambda x: (x[1], x[0]))
for k, v in d:
    if n[k] > 1:
        print(k, v)
    else:
        print(k)
