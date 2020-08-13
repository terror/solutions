n, d, w, freq = int(input()), {}, {}, {}

for _ in range(n):
    name, *words = list(map(str, input().split()))
    if name in d:
        for i in words:
            d[name].append(i)
            w[name].add(i)
    else: d[name], w[name] = words, set(words)

common = set.intersection(*w.values())
if not common:
    print("ALL CLEAR")
    exit()

for k, v in d.items():
    for i in v:
        if i in freq: freq[i] += 1
        else: freq[i] = 1

freq = sorted(freq.items())
for k, v in sorted(dict(freq).items(), key=lambda x: x[1], reverse=True):
    if k in common: print(k)
