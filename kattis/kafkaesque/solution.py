p = 0
tot = 1
for i in range(int(input())):
    n = int(input())
    if p > n:
        tot += 1
    p = n
print(tot)
