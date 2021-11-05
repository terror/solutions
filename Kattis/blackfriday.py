from collections import Counter

n = int(input())
l = list(map(int, input().split()))
m = max([k for k, v in Counter(l).items() if v == 1] or [0])

print(l.index(m) + 1 if m != 0 else 'none')
