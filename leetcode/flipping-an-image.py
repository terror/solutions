class Solution:
  def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for i in range(len(A)):
      A[i] = reversed([i ^ 1 for i in A[i]])
    return A
