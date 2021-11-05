#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> ii;
typedef map<int, int> MPII;
typedef set<int> SETI;

const int mxN = 2e5;
const ld pi = 4.0 * atanl(1.0);
const int iinf = 1e9 + 10;
const int inf = 1e18 + iinf + 10;
const int mod = 1000000007;
const ld prec = .000001;

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()

int n, m, t, a[mxN];

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  cin >> n >> m;
  vector<ii> v;
  for (int i = 0; i < m; ++i) {
    int a, b;
    cin >> a >> b;
    v.pb(mp(b, a));
  }
  int ans = 0, c = 0;
  sort(v.rbegin(), v.rend());

  for (int i = 0; i < m; ++i) {
    bool full = false;
    for (int j = 0; j < v[i].S; ++j) {
      if (c + 1 > n) {
        full = true;
        break;
      } else {
        ans += v[i].F, ++c;
      }
    }
    if (full)
      break;
  }
  cout << ans;
  return 0;
}
