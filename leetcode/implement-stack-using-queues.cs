public class MyStack {
  private Queue<int> q;

  /** Initialize your data structure here. */
  public MyStack() { q = new Queue<int>(); }

  /** Push element x onto stack. */
  public void Push(int x) {
    Queue<int> t = new Queue<int>();
    t.Enqueue(x);
    while (q.Any())
      t.Enqueue(q.Dequeue());
    q = t;
  }

  /** Removes the element on top of the stack and returns that element. */
  public int Pop() { return q.Dequeue(); }

  /** Get the top element. */
  public int Top() { return q.Peek(); }

  /** Returns whether the stack is empty. */
  public bool Empty() { return !q.Any(); }
}

/**
 * Your MyStack object will be instantiatedand called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */
