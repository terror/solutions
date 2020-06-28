n = int(input())

d = {}
k = {}

for i in range(n):
    r = input()
    if r in d:
        d[r] += 1
    else:
        d[r] = 1
for i in range(n):
    r = input()
    if r in k:
        k[r] += 1
    else:
        k[r] = 1

c = 0
for key, val in d.items():
    if key in k:
        c += min(val, k[key])
print(c)
