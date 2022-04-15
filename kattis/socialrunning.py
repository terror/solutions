nums = [int(input()) for _ in range(int(input()))]

ans = int(2e5)
for i, v in enumerate(nums):
  ans = min(ans, v + nums[(i - 2) % len(nums)])

print(ans)
