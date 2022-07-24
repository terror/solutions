class Solution:
  def solve(self, arr):
    arr = list(filter(lambda x: x > 0, arr))
    return ((len(arr) + 1) * (len(arr) + 2)) // 2 - sum(arr)
