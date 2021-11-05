#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<ll> vl;

ll n, t, x = 1;

int main() {
  cin >> t;
  while (t--) {
    cin >> n;
    ll ans = 0;
    vl v1(n), v2(n);

    for (auto &x : v1)
      cin >> x;
    for (auto &x : v2)
      cin >> x;

    sort(v1.begin(), v1.end()), sort(v2.rbegin(), v2.rend());

    for (int i = 0; i < n; ++i)
      ans += v1[i] * v2[i];
    cout << "CASE #" << x << ": " << ans << "\n";
    ++x;
  }
}