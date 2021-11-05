public class Solution {
  public int HeightChecker(int[] heights) {
    int counter = 0;
    int[] heightsSorted = new int[heights.Length];

    for (int i = 0; i < heights.Length; i++) {
      heightsSorted[i] = heights[i];
    }

    Array.Sort(heightsSorted);

    for (int i = 0; i < heights.Length; i++) {
      if (heightsSorted[i] != heights[i]) {
        counter++;
      }
    }
    return counter;
  }
}