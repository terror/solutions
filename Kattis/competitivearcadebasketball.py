n, p, m = list(map(int, input().split()))

d = {}
for _ in range(n):
    d[input()] = 0

w = set()
for _ in range(m):
    name, points = list(map(str, input().split()))
    d[name] += int(points)
    if d[name] >= p:
        w.add(name)

w = list(w)
if w:
    for i in w:
        print(i, "wins!")
else:
    print("No winner!")
