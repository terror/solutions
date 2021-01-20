#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
#define ar array
const int INF = 1e9;

/*
 Greedy solution ~ always chose max digit

int n;

int x(int n) {
  int mx = 0;
  for (char c : to_string(n)) mx = max(mx, c - '0');
  return mx;
}

int main() {
  cin >> n;
  int ans = 0;
  while (n != 0) ++ans, n -= x(n);
  cout << ans;
}

*/

// dp solution,
// ~ try removing each digit

int n;

int main() {
  cin >> n;
  vi dp(n + 1, INF);
  dp[0] = 0;

  for (int i = 0; i <= n; ++i)
    for (char c : to_string(i)) dp[i] = min(dp[i], dp[i - (c - '0')] + 1);

  cout << dp[n];
}
