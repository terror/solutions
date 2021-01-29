class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s, ans = 0, []

        for i in A:
            if i % 2 == 0:
                s += i

        for v, i in queries:
            # we have added this already
            if A[i] % 2 == 0:
                s -= A[i]
            A[i] += v
            # want it back if even
            if A[i] % 2 == 0:
                s += A[i]
            ans.append(s)

        return ans
