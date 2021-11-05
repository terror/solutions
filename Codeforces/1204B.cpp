#pragma GCC optimize("O3")
#pragma GCC target("sse4")

#include <bits/stdc++.h>

// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

const int MXN = 2e5, IINF = 1e9 + 10, INF = 1e18 + IINF + 10, MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); i++)
#define F0R(i, a) for (int i = 0; i < (a); i++)
#define FORd(i, a, b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i, a) for (int i = (a)-1; i >= 0; i--)
#define trav(a, x) for (auto &a : x)
#define uid(a, b) uniform_int_distribution<int>(a, b)(rng)

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.end(), x.begin()
#define lb lower_bound
#define ub upper_bound
#define sz(x) (int)(x).size()
#define ins insert

int n, m, t, a[MXN];

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

int main() {
  int l, r;
  cin >> n >> l >> r;
  vector<int> arr = {1};
  int x = 1;

  // get min

  int c = 1 * (n - (l - 1));
  int v = l - 1;
  int lol = 1;
  while (v--) {
    c += pow(2, lol);
    lol++;
  }

  if (l == 1)
    c = n;
  cout << c << " ";

  // get max
  for (int i = 1; i <= r; ++i) {
    arr.pb(pow(2, i));
  }

  vector<int> arr2;
  int ss = 0;
  for (int i = 0; i < min(r, n); ++i) {
    arr2.pb(arr[i]);
    ss += arr[i];
  }

  int mx = arr2[arr2.size() - 1];
  if (n > r) {
    cout << ss + ((n - arr2.size()) * mx);
    return 0;
  }
  cout << ss;
  return 0;
}
