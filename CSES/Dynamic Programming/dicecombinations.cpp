#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vl;
const int MOD = 1000000007;
const char nl = '\n';
int n;

int main() {
  cin >> n;
  vl dp(n + 1);
  dp[0] = 1;

  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= 6; j++)
      if (i - j >= 0) dp[i] += dp[i - j], dp[i] %= MOD;

  cout << dp[n] << nl;
}

