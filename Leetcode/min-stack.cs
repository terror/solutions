public class MinStack {
    private List<KeyValuePair<int, int>> st;
    private int mn;
    
    /** initialize your data structure here. */
    public MinStack() { this.st = new List<KeyValuePair<int, int>>(); this.mn = int.MaxValue; }
    
    public void Push(int x) {
        // maintain a key (element) -> value (min) pair
        mn = this.st.Count == 0 ? x : Math.Min(x, Go().Value);
        st.Add(new KeyValuePair<int, int>(x, mn));
    }

    // standard pop last element
    public void Pop() { st.RemoveAt(st.Count-1); }

    public int Top() { return Go().Key; }
    public KeyValuePair<int, int> Go() { return st[st.Count-1]; }
    public int GetMin() { return Go().Value; }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int parm_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */

