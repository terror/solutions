from functools import reduce

n, V = list(map(int, input().split()))

print(max([reduce(lambda x, y: x * y, list(map(int, input().split()))) for _ in range(n)])-V)
