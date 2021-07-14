n, h, v = list(map(int, input().split()))
height = max(h, n - h)
length = max(v, n - v)
print(height * length * 4)
