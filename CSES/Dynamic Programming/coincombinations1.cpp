#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MXN = 2e5, INF = 1000001, MOD = 1000000007;
int a[MXN];

int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; ++i) cin >> a[i];

  ll dp[INF];
  dp[0] = 1;

  for (int i = 0; i <= m; ++i)
    for (int j = 1; j <= n; ++j)
      if (i - a[j - 1] >= 0) dp[i] += dp[i - a[j - 1]], dp[i] %= MOD;

  cout << dp[m];
  return 0;
}
