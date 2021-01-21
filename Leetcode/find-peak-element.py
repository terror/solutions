class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i, v in enumerate(nums):
            if i == n-1:
                if i-1 >= 0 and nums[i-1] < v:
                    return i
            if i == 0:
                if i + 1 < n and nums[i+1] < v:
                    return i
            if nums[i-1] < v > nums[i+1]:
                return i
        return 0
