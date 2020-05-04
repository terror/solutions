from collections import Counter

n = int(input())
for i in range(n):
    a = int(input())
    b = list(map(str, input().split()))
    c = ([item for item, count in Counter(b).items() if count > 1])
    d = list(filter(lambda a: a not in c, b))
    print("Case #{0}: {1}".format(i+1, int(d[0])))
