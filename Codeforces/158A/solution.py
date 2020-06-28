n = list(map(int, input().split()))
c = list(map(int, input().split()))
k = c[n[1] - 1]
count = 0
for i in range(len(c)):
    if c[i] >= k and c[i] > 0:
        count += 1

print(count)
