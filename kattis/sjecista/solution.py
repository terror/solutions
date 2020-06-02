n = int(input())
print(0 if n <= 3 else n*(n-1)*(n-2)*(n-3)//24)
