import sys
n = int(input())
d = {}
c = {}

for i in range(n):
    topic, num, *words = list(map(str, input().split()))
    d[topic] = words
    c[topic] = 0

while True:
    i = sys.stdin.readline()
    if i.rstrip() == '':
        break
    i = i.split()
    for word in i:
        for key, val in d.items():
            if word in val:
                c[key] += 1

m = 0
for key, val in c.items():
    if val > m:
        m = val

ans = []
for key, val in sorted(c.items(), reverse=True):
    if val == m:
        ans.append(key)

print(*sorted(ans), sep='\n')
