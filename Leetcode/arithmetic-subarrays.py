class Solution:
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    inf, n, ans = float('inf'), len(l), []
    for i in range(n):
      arr, diff, p = sorted(nums[l[i]:r[i] + 1]), inf, 1
      for i in range(1, len(arr)):
        if diff != inf and abs(arr[i] - arr[i - 1]) != diff:
          ans.append(False)
          p = 0
          break
        diff = abs(arr[i] - arr[i - 1])
      if p:
        ans.append(True)
    return ans
