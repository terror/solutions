class Solution:
  def solve(self, n):
   terms = [0, 1, 1]

   while terms[-1] < n:
     terms.append(terms[-1] + terms[-2])

   ans, term = 0, len(terms) - 1

   while n > 0:
     ans, n, term = ans + n // terms[term], n % terms[term], term - 1

   return ans
