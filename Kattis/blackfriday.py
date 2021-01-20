n = int(input())
lst = list(map(int, input().split()))

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

m = 0
for key, val in d.items():
    if val == 1:
        if key > m:
            m = key

if m != 0:
    print(lst.index(m)+1)
else:
    print('none')
