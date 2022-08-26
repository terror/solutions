class Solution:
  def solve(self, nums0, nums1):
    i = j = 0; new = []
    while i < len(nums0) and j < len(nums1):
      if nums0[i] < nums1[j]: new.append(nums0[i]); i += 1
      else: new.append(nums1[j]); j += 1
    new += nums0[i:]; new += nums1[j:]
    return new[floor(len(new) / 2)]
