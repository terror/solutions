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

const int mxN = 1e5, iinf = 1e9 + 10, inf = 1e18 + iinf + 10, mod = 1000000007;
const ld pi = 4.0 * atanl(1.0), prec = .000001;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)

int n, m, t;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  char x;

  cin >> n >> m >> x;
  char a[n + 1][m + 1];
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j) cin >> a[i][j];

  set<char> s;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (a[i][j] == x) {
        // check all sides
        if (i - 1 >= 0 and i + 1 < n) {
          s.insert(a[i - 1][j]);
          s.insert(a[i + 1][j]);
        } else {
          if (i - 1 >= 0) s.insert(a[i - 1][j]);
          if (i + 1 < n) s.insert(a[i + 1][j]);
        }
        if (j - 1 >= 0 and j + 1 < m) {
          s.insert(a[i][j - 1]);
          s.insert(a[i][j + 1]);
        } else {
          if (j - 1 >= 0) s.insert(a[i][j - 1]);
          if (j + 1 < m) s.insert(a[i][j + 1]);
        }
      }
    }
  }
  int ans = 0;
  for (auto i : s)
    if (i != '.' and i != x) ++ans;
  cout << ans;
  return 0;
}
