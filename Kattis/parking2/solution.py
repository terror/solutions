for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print((max(p) - min(p)) + (max(p) - min(p)))
