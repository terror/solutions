from collections import defaultdict
n, d = int(input()), defaultdict(list)

for i in range(n):
    a, b = map(str, input().split())
    d[a].append(int(b))

for k, v in d.items(): v.sort()

q = int(input())
for i in range(q):
    a, b = map(str, input().split())
    print(d[a][int(b)-1])
