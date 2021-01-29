class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i, p = 0, pieces
        while i < len(arr):
            f = 0
            curr = arr[i]
            for j in p:
                if j[0] == curr and arr[i:i+len(j)] == j:
                    f = 1
                    i += len(j)
            if not f:
                return 0
        return 1
