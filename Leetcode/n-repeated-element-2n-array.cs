public class Solution {
    public int RepeatedNTimes(int[] A) {
        Array.Sort(A);
        for(int i = 0; i < A.Length; i++) {
            if(A[i] == A[i+1]) {
                return A[i];
            }
        }
        return -1;
        
    }
}