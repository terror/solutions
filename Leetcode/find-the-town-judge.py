class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        deg, out = [0]*N, [0]*N
        for i in range(len(trust)):
            a, b = trust[i]
            deg[a-1] += 1
            out[b-1] += 1
        for i in range(N):
            if out[i] == N-1:
                if deg[i] == 0:
                    return i+1
        return -1
