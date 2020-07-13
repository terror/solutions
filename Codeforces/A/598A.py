for i in range(int(input())):
    power = 1
    n = int(input())
    Sum = n * (n+1)//2
    while power <= n:
        Sum -= power*2
        power *= 2
    print(Sum)
