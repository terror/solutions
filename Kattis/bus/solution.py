n = int(input())
tot = 0
for i in range(n):
    a = int(input())
    if a == 1:
        tot = 1
    else:
        for i in range(a):
            tot += 0.5
            tot *= 2  # reverse half
    print(int(tot))
    tot = 0  # reset
