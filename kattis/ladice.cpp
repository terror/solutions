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

const int MXN = 300000 + 10, IINF = 1e9 + 10, INF = 1e18 + IINF + 10,
          MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define F0R(a) for (int i = 0; i < (a); ++i)
#define FORd(i, a, b) fo(int i = (b)-1; i >= a; --i)
#define F0Rd(a) for (int i = (a)-1; ~i; --i)
#define trav(a, x) for (auto &a : x)

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define lb lower_bound
#define ub upper_bound
#define sz(x) (int)(x).size()
#define ins insert

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

class UF {
private:
  vi p, r, sz, u;

public:
  UF(int N) {
    p.assign(N + 1, 0), r.assign(N + 1, 0), sz.assign(N + 1, 1),
        u.assign(N + 1, 0);
    for (int i = 1; i <= N; ++i)
      p[i] = i;
  }
  bool same(int i, int j) { return find(i) == find(j); }
  int find(int i) { return p[i] == i ? i : (p[i] = find(p[i])); }
  void merge(int i, int j) {
    if (same(i, j))
      return;
    int x = find(i), y = find(j);
    if (r[x] > r[y])
      swap(x, y);
    p[x] = y;
    if (r[x] == r[y])
      ++r[y];
    sz[y] += sz[x], u[y] += u[x];
  }
  bool op(int i) {
    int x = find(i);
    if (u[x] + 1 <= sz[x]) {
      ++u[x];
      return 1;
    }
    return 0;
  }
};

int main() {
  fast();
  int N, M;
  cin >> N >> M;
  UF x = UF(M);
  while (N--) {
    int a, b;
    cin >> a >> b;
    x.merge(a, b);
    cout << (x.op(a) ? "LADICA" : "SMECE") << nl;
  }
}
