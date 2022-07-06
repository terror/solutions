int solve(vector<string>& ops) {
  stack<int> s;

  for (int i = 0; i < ops.size(); ++i) {
    if (ops[i] == "POP") {
      if (s.size() < 1) return -1;
      s.pop();
    } else if (ops[i] == "DUP") {
      if (s.size() < 1) return -1;
      s.push(s.top());
    } else if (ops[i] == "+") {
      if (s.size() < 2) return -1;
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(a + b);
    } else if (ops[i] == "-") {
      if (s.size() < 2) return -1;
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(a - b);
    } else {
      s.push(stoi(ops[i]));
    }
  }

  return s.top();
}
