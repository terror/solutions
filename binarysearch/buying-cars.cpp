int solve(vector<int>& prices, int k) {
  sort(prices.begin(), prices.end());

  int ans = 0;

  for (int i = 0; i < prices.size(); ++i) {
    if (k - prices[i] < 0) break;
    k -= prices[i];
    ++ans;
  }

  return ans;
}
