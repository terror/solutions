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

const int MXN = 2e5 + 10, IINF = 1e9 + 10, INF = 1e18 + IINF + 10,
          MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define F0R(a) for (int i = 0; i < (a); ++i)
#define FORd(i, a, b) for (int i = (b)-1; i >= a; --i)
#define F0Rd(a) for (int i = (a)-1; ~i; --i)
#define trav(a, x) for (auto &a : x)

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

vi adj[MXN];
bool vis[MXN];
vi ans;
bool p = 0;

void dfs(int v) {
  if (p == 1)
    ans.pb(v);
  vis[v] = 1;
  for (auto u : adj[v]) {
    if (!vis[u]) {
      dfs(u);
    }
  }
}

int cc(int n) {
  for (int i = 1; i <= n; ++i)
    vis[i] = 0;
  int ret = 0;
  for (int i = 1; i <= n; ++i) {
    if (!vis[i]) {
      ++ret;
      if (ret > 1)
        p = 1;
      dfs(i);
    }
  }
  return ret;
}

int main() {
  fast();
  cin >> n >> m;
  F0R(m) {
    int u, v;
    cin >> u >> v;
    adj[u].pb(v);
    adj[v].pb(u);
  }
  int x = cc(n);
  if (x == 1) {
    cout << "Connected";
    return 0;
  }
  sort(all(ans));
  for (auto x : ans) {
    cout << x << nl;
  }

  return 0;
}
