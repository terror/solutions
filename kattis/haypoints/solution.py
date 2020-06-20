import sys
from collections import Counter
n, m = list(map(int, input().split()))

d = {}

for i in range(n):
    w, amount = list(map(str, input().split()))
    d[w] = int(amount)

ans = []
c = 0
for _ in range(m):
    money = 0
    while True:
        i = sys.stdin.readline()
        if i.rstrip() == '.':
            ans.append(money)
            break
        else:
            i = i.split()
            i = Counter(i)
            for key, val in i.items():
                if key in d:
                    money += val*d[key]

print(*ans, sep='\n')
