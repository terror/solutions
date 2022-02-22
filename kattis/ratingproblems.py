n, k = map(int, input().split())
r = sum([int(input()) for _ in range(k)])
print((-3 * r + (n - k)) / n, (3 * r + (n - k)) / n)
