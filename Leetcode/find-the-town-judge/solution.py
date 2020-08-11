class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1: return 1
        if not trust and N>1: return -1
        
        # a -> b
        d, c, ans = collections.Counter(), collections.Counter(), []
        
        for i in range(len(trust)):
            d[trust[i][0]] += 1
            c[trust[i][1]] += 1
            if trust[i][1] not in d: d[trust[i][1]] = 0
        
        for key, val in d.items():
            if val == 0 and c[key] == N-1: ans.append(key)
                
        if not ans or len(ans) > 1: return -1
        
        return ans[0]
        
                