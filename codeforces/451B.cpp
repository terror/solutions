#include <bits/stdc++.h>

// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

using namespace std;
// using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> pii;
typedef map<int, int> mpii;
typedef set<int> seti;

const int mxN = 2e5, iinf = 1e9 + 10, inf = 1e18 + iinf + 10, mod = 1000000007;
const ld pi = 4.0 * atanl(1.0), prec = .000001;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)

ll n, m, t, a[mxN], b[mxN];

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    b[i] = a[i];
  }
  map<int, int> mp;
  sort(b, b + n);
  for (int i = 0; i < n; i++) {
    mp[b[i]] = i;
  }
  for (int i = 0; i < n; i++) {
    a[i] = mp[a[i]];
  }
  int L = -1;
  for (int i = 0; i < n; i++) {
    if (a[i] != i) {
      L = i;
      break;
    }
  }
  int R = -1;
  for (int i = n - 1; i >= 0; i--) {
    if (a[i] != i) {
      R = i;
      break;
    }
  }
  if (L == -1 || R == -1) {
    cout << "yes" << endl;
    cout << 1 << " " << 1 << endl;
  } else {
    reverse(a + L, a + R + 1);
    int ok = true;
    for (int i = 0; i < n; i++) {
      if (a[i] != i) {
        ok = false;
      }
    }
    if (ok) {
      cout << "yes" << endl;
      cout << L + 1 << " " << R + 1 << endl;
    } else {
      cout << "no" << endl;
    }
  }
  return 0;
}
