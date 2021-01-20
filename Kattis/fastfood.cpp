#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<ll> vl;
#define pb push_back
ll n, a, b, c, x;

int main() {
  cin >> n;
  while (n--) {
    cin >> a >> b;
    vector<vl> amounts(a);
    vl stickers(b), money(a);

    for (int i = 0; i < a; ++i) {
      cin >> c;
      for (int j = 0; j < c; ++j) {
        cin >> x;
        amounts[i].pb(x);
      }
      cin >> money[i];
    }

    for (auto &x : stickers) cin >> x;

    ll ans = 0;
    for (ll i = 0; i < a; ++i) {
      ll mn = 100;
      // ans = min sticker * prize $
      for (auto x : amounts[i]) mn = min(mn, stickers[x - 1]);
      ans += mn * money[i];
    }
    cout << ans << "\n";
  }
  return 0;
}
