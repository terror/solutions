def rev(n):
    r = 0
    while(n > 0):
        rm = n % 10
        r = (r*10) + rm
        n = n//10
    return r


a, b = list(map(int, input().split()))

a = rev(a)
b = rev(b)
if a > b:
    print(a)
else:
    print(b)
