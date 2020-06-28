t = int(input())

for i in range(t):
    n = int(input())
    c = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
        else:
            if (n * 2) % 6 == 0:
                n *= 2
            else:
                c = -1
                break
        c += 1
    print(c)
