public class MyQueue {
    private Stack<int> a;
    private Stack<int> b;
    /** Initialize your data structure here. */
    public MyQueue() { a = new Stack<int>(); b = new Stack<int>(); }
        
    /** Push element x to the back of queue. */
    public void Push(int x) {
        while(a.Any()) b.Push(a.Pop());
        a.Push(x);
        while(b.Any()) a.Push(b.Pop());
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int Pop() {
        return a.Pop();
    }
    
    /** Get the front element. */
    public int Peek() {
        return a.Peek();
    }
    
    /** Returns whether the queue is empty. */
    public bool Empty() {
        return !a.Any();
    }
}

/**
 * Your MyQueue object will b instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
