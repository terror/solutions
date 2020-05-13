n = list(map(int, input().split()))
targ = [1, 1, 2, 2, 2, 8]
new = []

for i in range(len(n)):
    if n[i] != targ[i]:
        new.append(targ[i] - n[i])
    else:
        new.append(0)

print(' '.join(str(i) for i in new))
