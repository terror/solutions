b = []

for i in range(int(input())):
    n = list(map(int, input().split()))
    for j in range(n[0], n[1] + 1):
        b.append(j)

print(len(set((b))))
