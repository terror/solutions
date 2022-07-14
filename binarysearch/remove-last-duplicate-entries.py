class Solution:
  def solve(self, nums):
    d = defaultdict(list)

    for i, num in enumerate(nums):
      d[num].append(i)

    ans = []

    for i, num in enumerate(nums):
      if i == d[num][-1] and len(d[num]) > 1:
        continue
      ans.append(num)

    return ans
