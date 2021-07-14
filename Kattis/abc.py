nums = list(map(int, input().split()))
l = list(input())
new = []

for i in range(len(l)):
  if l[i] == 'A':
    new.append(min(nums))
  if l[i] == 'B':
    for j in range(len(nums)):
      if nums[j] != max(nums) and nums[j] != min(nums):
        new.append(nums[j])
  if l[i] == 'C':
    new.append(max(nums))

print(*new, sep=' ')
