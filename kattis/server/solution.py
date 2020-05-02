a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a[1]
d = 0
sum = 0

for i in range(a[0]):
    sum += b[i]
    if sum <= c:
        d += 1
    else:
        break

print(d)
