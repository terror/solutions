n, V = list(map(int, input().split()))

Max = 0
for i in range(n):
    a, b, c = list(map(int, input().split()))
    if a*b*c > Max:
        Max = a*b*c
print(Max-V)
