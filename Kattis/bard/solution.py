v, n, s, d = int(input()), int(input()), 0, [set() for i in range(110)]

for i in range(n):
    y = list(map(int, input().split()))[1:]

    if 1 in y:
        s += 1
        for i in y: d[i].add(s)
        continue

    for i in range(1, s+1):
        for j in y: d[j].add(i)

for i in range(len(d)): print("{}\n".format(i) if len(d[i]) == s else "", end="")