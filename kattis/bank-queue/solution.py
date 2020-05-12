from collections import *

p, t = list(map(int, input().split()))
people = defaultdict(list)
tot = 0
amount = []

# sort by time
for n in range(p, 0, -1):
    a, b = list(map(int, input().split()))
    people[b].append(a)

# longest time -> shortest time
for i in range(t - 1, -1, -1):
    for p in people[i]:
        amount.append(p)
    if len(amount):
        tot += max(amount)
        amount.remove(max(amount))

print(tot)
