t = int(input())
for i in range(t):
    n, num = input(), 0
    while len(n) != 1:
        num = sum([int(i) for i in n])
        n = str(num)
    print(n)
