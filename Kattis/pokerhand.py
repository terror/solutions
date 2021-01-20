n = input().split()
curr = {}

for i in range(len(n)):
    a = n[i]
    if a[0] not in curr:
        curr[a[0]] = 1
    else:
        curr[a[0]] += 1

vals = curr.values()
max_val = max(vals)
print(max_val)
