H, M = list(map(int, input().split()))

minutes = H*60 + M

c = minutes - 45
m = c % 60
c //= 60
if c == -1:
    c = 23

print("{0} {1}".format(c, m))
