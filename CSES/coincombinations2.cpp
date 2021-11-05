#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
const int MXN = 2e5, MOD = 1e9 + 7;

int main() {
  ll n, m, a[MXN];
  cin >> n >> m;

  for (int i = 0; i < n; ++i)
    cin >> a[i];

  vvi dp(n + 1, vi(m + 1));
  dp[0][0] = 1;

  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= m; ++j) {
      dp[i][j] = dp[i - 1][j];
      if (j - a[i - 1] >= 0)
        (dp[i][j] += dp[i][j - a[i - 1]]) %= MOD;
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cout << dp[i][j] << " ";
    }
    cout << "\n";
  }
  cout << "\n";
  cout << dp[n][m];
  return 0;
}
