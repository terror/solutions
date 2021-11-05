#include <bits/stdc++.h>

using namespace std;

#define op(S) ((S) & -(S))

typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;

class FenwickTree {
private:
  vll ft;

public:
  FenwickTree(int m) { ft.assign(m + 1, 0); }

  void update(ll i, ll v) {
    for (i++; i < ft.size(); i += op(i))
      ft[i] += v;
  }

  ll rsq(ll i) {
    ll s = 0;
    for (; i > 0; i -= op(i))
      s += ft[i];
    return s;
  }
};

int main() {
  ll n, q;
  scanf("%lld%lld\n", &n, &q);
  FenwickTree ft(n);
  ll a, b;
  while (q--) {
    char c;
    scanf("%c", &c);
    if (c == '+') {
      scanf("%lld%lld\n", &a, &b);
      ft.update(a, b);
    }
    if (c == '?') {
      scanf("%lld\n", &b);
      printf("%lld\n", ft.rsq(b));
    }
  }
  return 0;
}
