class Solution:
  def solve(self, nums):
    if not nums:
      return 1

    def pre(L):
      ret = [0, L[0]]
      for i in range(1, len(L)):
        ret.append(ret[i] + L[i])
      return ret

    return 1 - min(pre(nums))
