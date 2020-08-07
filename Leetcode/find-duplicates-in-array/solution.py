class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d, ans = {}, set()

        for i in nums:
            if i in d:
                ans.add(i)
            else:
                d[i] = 1

        return list(ans)
