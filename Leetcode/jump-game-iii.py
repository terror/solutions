class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    q = [start]
    while q:
      x = q.pop()
      if arr[x] == 0:
        return True
      if arr[x] < 0:
        continue
      # get neighbors
      for i in [x + arr[x], x - arr[x]]:
        if i >= 0 and i < len(arr):
          q.append(i)
      # vis
      arr[x] = -arr[x]
    return False
