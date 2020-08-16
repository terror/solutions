N, K = map(int, input().split())
d, ans = {}, set()


for i in range(N):
    d[i] = list(map(int, input().split()))

seen = {0: set(), 1: set(), 2: set()}
for _ in range(K):
    for i in range(3):
        mx = id = 0
        for k, v in d.items():
            if v[i] > mx and k not in seen[i]:
                id, mx = k, v[i]
        ans.add(id)
        seen[i].add(id)

print(len(ans))
