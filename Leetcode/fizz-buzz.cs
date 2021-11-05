public class Solution {
  public IList<string> FizzBuzz(int n) {
    var ret = new List<string>();
    for (int i = 1; i <= n; ++i) {
      if (i % 5 == 0 && i % 3 == 0)
        ret.Add("FizzBuzz");
      else if (i % 5 == 0)
        ret.Add("Buzz");
      else if (i % 3 == 0)
        ret.Add("Fizz");
      else
        ret.Add(i.ToString());
    }
    return ret;
  }
}
