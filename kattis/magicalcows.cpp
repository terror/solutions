#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
#define vll vector<ll>
ll c, n, m, x;

int main() {
  cin >> c >> n >> m;
  vector<vll> dp(51, vll(c + 1));
  for (int i = 0; i < n; ++i) {
    cin >> x;
    ++dp[0][x];
  }
  for (int i = 0; i < 50; ++i) {
    for (int j = 1; j <= c; ++j) {
      if (j > c / 2)
        dp[i + 1][j] += dp[i][j] * 2;
      else
        dp[i + 1][j * 2] += dp[i][j];
    }
  }
  for (int i = 0; i < m; ++i) {
    ll ans = 0;
    cin >> x;
    for (int j = 0; j < dp[x].size(); ++j)
      ans += dp[x][j];
    cout << ans << "\n";
  }
  return 0;
}
