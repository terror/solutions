#pragma GCC optimize("O3")
#pragma GCC target("sse4")

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
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

const int MXN = 2e5, IINF = 1e9 + 10, INF = 1e18 + IINF + 10, MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); i++)
#define F0R(i, a) for (int i = 0; i < (a); i++)
#define FORd(i, a, b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i, a) for (int i = (a)-1; i >= 0; i--)
#define trav(a, x) for (auto& a : x)
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

vector<char> adj[MXN];

void dfs(char v, char targ, vector<bool>& vis, set<char>& p) {
  vis[v] = 1;
  for (char u : adj[v]) {
    if (!vis[u]) {
      p.ins(u);
      dfs(u, targ, vis, p);
    }
  }
}

int main() {
  fast();
  cin >> n >> m;
  FOR(i, 0, n) {
    char u, v;
    cin >> u >> v;
    adj[u].pb(v);
  }
  FOR(i, 0, m) {
    string s1, s2;
    cin >> s1 >> s2;
    if (s1.length() != s2.length()) {
      cout << "no" << nl;
      continue;
    }
    bool ok = 1;
    for (int i = 0; i < s1.length(); ++i) {
      vector<bool> vis(MXN);
      set<char> p;
      if (s1[i] == s2[i]) continue;
      dfs(s1[i], s2[i], vis, p);
      if (!p.count(s2[i])) {
        cout << "no" << nl;
        ok = 0;
      }
      if (!ok) break;
    }
    if (ok) cout << "yes" << nl;
  }

  return 0;
}

