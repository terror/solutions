from collections import Counter

d = Counter([input() for i in range(int(input()))])
print(max(d, key=d.get))
