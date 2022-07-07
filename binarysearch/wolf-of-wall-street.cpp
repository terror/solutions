int solve(vector<int>& prices) {
  int m = 2e5; int ans = 0;
  for (int i = 0; i < prices.size(); ++i) {
    m = min(m, prices[i]);
    ans = max(ans, prices[i] - m);
  }
  return ans;
}
