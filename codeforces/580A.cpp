#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;

  ll ans = 1;
  ll mx = 0;

  vector<int> v(n);
  for (auto &n : v)
    cin >> n;

  for (int i = 1; i < n; i++) {
    if (v[i] >= v[i - 1])
      ans++;
    else {
      mx = max(mx, ans);
      ans = 1;
    }
  }
  mx = max(mx, ans);
  cout << mx << endl;
  return 0;
}