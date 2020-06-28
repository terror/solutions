import sys
d = {}

while True:
    a = list(map(str, input().split()))
    if len(a) == 0:
        break
    else:
        d[a[1]] = a[0]

for i in sys.stdin:
    b = i.split()
    if b[0] in d:
        print(d[b[0]])
    else:
        print("eh")
