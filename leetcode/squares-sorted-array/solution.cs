public class Solution {
    public int[] SortedSquares(int[] A) {
        int[] results = new int[A.Length];
        int result = 0;
        for(int i = 0; i < A.Length; i++) {
            result = Math.Abs(A[i]*A[i]);
            results[i] = result;
        }
        
        Array.Sort(results);
        return results;
    }
}