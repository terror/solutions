public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int[] smallerNumberCount = new int[nums.Length];
        int counter = 0;
        for(int i = 0; i < nums.Length; i++) {
            for(int j = 0; j < nums.Length; j++) {
                if(j != i && nums[i] > nums[j]) {
                    counter++;
                }
            }
            smallerNumberCount[i] = counter;
            counter = 0;
        }
        return smallerNumberCount;
    }
}