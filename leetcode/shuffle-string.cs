public class Solution {
  public string RestoreString(string s, int[] indices) {
    int n = indices.Length;
    char[] arr = new char[s.Length];
    for (int i = 0; i < n; ++i)
      arr[indices[i]] = s[i];
    return String.Concat(arr);
  }
}
