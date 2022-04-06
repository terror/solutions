(lambda n, k: print(*list(map(lambda x: x[1], filter(lambda x: (x[0] + 1) % k == 0, enumerate(map(int, input().split())))))))(*map(int, input().split()))
