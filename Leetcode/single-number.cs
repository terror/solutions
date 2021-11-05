public class Solution {
  public int SingleNumber(int[] nums) {
    for (int i = 0; i < nums.Length; i++) {
      int j;
      for (j = 0; j < nums.Length; j++)
        if (i != j && nums[i] == nums[j])
          break;
      if (j == nums.Length)
        return nums[i];
    }
    return -1;
  }
}