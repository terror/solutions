t = int(input())
for _ in range(t):
    b = input()
    c = 0
    Ncs, Ne = list(map(int, input().split()))
    cs = list(map(int, input().split()))
    eco = list(map(int, input().split()))

    aCS = sum(cs)/len(cs)
    aECO = sum(eco)/len(eco)

    for i in range(len(cs)):
        if cs[i] < aCS and cs[i] > aECO:
            c += 1
    print(c)
