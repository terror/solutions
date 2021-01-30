public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        int ret = 0;
        for(int i = 0; i < arr.Length; ++i) {
            int len = 1; int s = arr[i]; ret+=arr[i];
            for(int j = i-1; j>=0; --j) {
                s+=arr[j];
                if (++len%2==1) ret+=s;
            }
        }
        return ret;
    }
}
