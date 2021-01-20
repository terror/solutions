#include <bits/stdc++.h>

using namespace std;

const int MXN = 1e6;
int n, m, dp[MXN], a[MXN];

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) cin >> a[i];

  memset(dp, MXN, sizeof(dp));
  dp[0] = 0;

  for (int i = 1; i <= m; ++i)
    for (int j = 0; j < n; ++j)
      if (a[j] <= i) dp[i] = min(dp[i], dp[i - a[j]] + 1);

  dp[m] > MXN ? cout << -1 : cout << dp[m];
  return 0;
}
