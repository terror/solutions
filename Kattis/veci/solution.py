n = int(input())
i = n
n += 1
ans = 0

while n <= 1000000:
    if sorted(str(i)) == sorted(str(n)):
        ans = n
        break
    n += 1

if ans != 0:
    print(ans)
else:
    print(0)
