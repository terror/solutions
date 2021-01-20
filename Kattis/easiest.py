while True:
    N = int(input())
    if N == 0:
        break
    Sum = 0

    for dig in str(N):
        Sum += int(dig)

    m = 0
    for i in range(100000):
        temp = N * i
        ts = 0
        for dig in str(temp):
            ts += int(dig)
        if ts == Sum and i > 10:
            m = i
            break
    print(m)
