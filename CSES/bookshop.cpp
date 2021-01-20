#include <bits/stdc++.h>

using namespace std;
const int MXN = 2e5;
typedef vector<int> vi;
typedef vector<vi> vvi;
int n, m, a[MXN], b[MXN];
#define FOR(i, a, b) for (int i = a; i < b; ++i)

int main() {
  cin >> n >> m;
  FOR(i, 0, n) cin >> a[i];
  FOR(i, 0, n) cin >> b[i];

  vvi dp(n + 1, vi(m + 1, 0));
  dp[0][0] = 0;

  FOR(i, 1, n + 1) {
    FOR(j, 0, m + 1) {
      dp[i][j] = dp[i - 1][j];
      if (j - a[i - 1] >= 0)
        dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i - 1]] + b[i - 1]);
    }
  }
  cout << dp[n][m];
  return 0;
}
