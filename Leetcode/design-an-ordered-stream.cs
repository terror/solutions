public class OrderedStream {
  private int ptr;
  private string[] ret;

  public OrderedStream(int n) {
    this.ptr = 0;
    this.ret = new string[n + 1];
  }

  public IList<string> Insert(int id, string value) {
    ret[id - 1] = value;
    var r = new List<string>();
    while (ret[ptr] != null && ptr < ret.Length)
      r.Add(ret[ptr++]);
    return r;
  }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * IList<string> param_1 = obj.Insert(id,value);
 */
