a, b = list(map(str, input().split())), [
    list(map(str, input().split())) for i in range(int(input()))]

for _ in range(int(input())):
    s = input()
    b = sorted(b, key=lambda x: x[a.index(s)])
    print(*a)
    for i in b: print(*i)