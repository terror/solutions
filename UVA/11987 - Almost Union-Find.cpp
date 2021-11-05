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

const int MXN = 100010, IINF = 1e9 + 10, INF = 1e18 + IINF + 10,
          MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define F0R(a) for (int i = 0; i < (a); ++i)
#define FORd(i, a, b) for (in i = (b)-1; i >= a; --i)
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

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

class UF {
private:
  int p[MXN], sz[MXN], sum[MXN];
  bool same(int i, int j) { return find(i) == find(j); }
  int find(int i) {
    if (p[i] == i)
      return i;
    return p[i] = find(p[i]); // path compression
  }

public:
  UF(int N) {
    for (int i = 1; i <= N; ++i) {
      p[i] = i + N, p[i + N] = i + N, sum[i + N] = i, sz[i + N] = 1;
    }
  }

  void unionSet(int i, int j) {
    if (same(i, j))
      return;
    int x = find(i), y = find(j);
    sz[y] += sz[x], sum[y] += sum[x];
    p[x] = y;
  }

  void mv(int i, int j) {
    if (same(i, j))
      return;
    int x = find(i), y = find(j);
    --sz[x], ++sz[y], sum[x] -= i, sum[y] += i;
    p[i] = y;
  }

  void ret(int i) {
    int x = find(i);
    cout << sz[x] << " " << sum[x] << nl;
  }
};

int main() {
  int n, m;
  while (scanf("%d%d", &n, &m) != EOF) {
    UF x = UF(n);
    F0R(m) {
      int o, a, b;
      cin >> o;
      if (o == 1) {
        cin >> a >> b;
        x.unionSet(a, b);
      }
      if (o == 2) {
        cin >> a >> b;
        x.mv(a, b);
      }
      if (o == 3) {
        cin >> a;
        x.ret(a);
      }
    }
  }
  return 0;
}
