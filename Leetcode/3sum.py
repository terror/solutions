class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, i = [], 0
        while i < len(nums):
            targ = -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == targ:
                    v = [-targ, nums[j], nums[k]]
                    if v not in ans:
                        ans.append(v)
                if nums[j] + nums[k] > targ:
                    k -= 1
                else:
                    j += 1
            i += 1
        return ans
