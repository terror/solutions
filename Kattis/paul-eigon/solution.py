n, p, q = list(map(int, input().split()))

if((p+q)//n % 2 == 1):
    print("opponent")
else:
    print("paul")
