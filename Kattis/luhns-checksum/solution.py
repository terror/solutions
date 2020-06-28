n = int(input())
for i in range(n):
    a = list(map(int, str(input())))
    s = 0
    for i in range((len(a)) - 1, -1, -1):
        if((i - len(a)) % 2 == 0):
            a[i] *= 2
            if(a[i] > 9):
                b = list(map(int, str(a[i])))
                a[i] = sum(b)
        s += a[i]

    if(s % 10 == 0):
        print("PASS")
    else:
        print("FAIL")
