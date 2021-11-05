public class Solution {
  public int MaxSubArray(int[] nums) {
    int maxSoFar = int.MinValue;
    int maxEndingHere = 0;

    for (int i = 0; i < nums.Length; i++) {
      maxEndingHere += nums[i];

      if (maxSoFar < maxEndingHere) {
        maxSoFar = maxEndingHere;
      }

      if (maxEndingHere < 0) {
        maxEndingHere = 0;
      }
    }
    return maxSoFar;
  }
}