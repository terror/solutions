(lambda N, x, y: print(*map(lambda a: (a * y) // x, [int(input()) for _ in range(N)]), sep = '\n'))(*map(int, input().split()))
