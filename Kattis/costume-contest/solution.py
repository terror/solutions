costumes = []

for i in range(int(input())):
    c = input()
    costumes.append(c)

d = {i: costumes.count(i) for i in costumes}
min_val = 1000
ans = []

for key, val in sorted(d.items(), reverse=True):
    if val <= min_val:
        min_val = val
        ans.append(key)

print(*sorted(ans), sep='\n')
