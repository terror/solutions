def main():
  nums = []
  for i in range(9):
    n = int(input())
    nums.append(n)
  nums = solve(nums)
  print(*nums, sep='\n')

def solve(nums):
  for i in range(len(nums)):
    s = sum(nums) - nums[i]
    for j in range(i):
      if s - nums[j] == 100:
        nums.remove(nums[j])
        nums.remove(nums[i - 1])
        return nums

main()
