int solve(string s) {
  set<int> seen;
  for (int i = 0; i < s.size(); ++i) {
    if (seen.count(s[i]))
      return i;
    seen.insert(s[i]);
  }
  return -1;
}
