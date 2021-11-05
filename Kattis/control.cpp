#pragma GCC optimize("O3")
#pragma GCC target("sse4")

#include <bits/stdc++.h>
using namespace std;

// template {{{

// Types
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

const int MXN = 500001, IINF = 1e9 + 10, INF = 1e18 + IINF + 10,
          MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

// Macros
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.end(), x.begin()
#define lb lower_bound
#define ub upper_bound
#define sz(x) (it)(x).size()
#define ins insert

// Function Macros
#define F0R(i, a, b) for (int i = a; i < (b); ++i)
#define FOR(a) for (int i = 0; i < (a); ++i)
#define F0Rd(i, a, b) for (int i = (b)-1; i >= a; --i)
#define FORd(a) for (int i = (a)-1; ~i; --i)
#define trav(a, x) for (auto &a : x)

template <typename T> void ckmin(T &a, const T &b) { a = min(a, b); }
template <typename T> void ckmax(T &a, const T &b) { a = max(a, b); }
template <typename T> ostream &operator<<(ostream &out, vector<T> iter) {
  out << "[";
  for (auto t : iter) {
    out << t << ", ";
  }
  out << "]";
  return out;
}
inline void setprec(ostream &out, int prec) {
  out << setprecision(prec) << fixed;
}

// I/O
inline void re() {}
inline void print() {}
template <typename F, typename... R> inline void re(F &f, R &...r) {
  cin >> f;
  re(r...);
}
template <typename F> inline void println(F t) { cout << t << '\n'; }
template <typename F, typename... R> inline void println(F f, R... r) {
  cout << f << " ";
  println(r...);
}
template <typename F, typename... R> inline void print(F f, R... r) {
  cout << f;
  print(r...);
}
template <typename T> void printArray(T *arr, int sz) {
  for (int i = 0; i < sz; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";
}

// Debug
#define trace(x) cout << (#x) << ": " << (x);

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }
// }}}

class UF {
private:
  vi p, r, sz;

public:
  UF(int N) {
    p.assign(N + 1, 0), r.assign(N + 1, 0), sz.assign(N + 1, 1);
    for (int i = 1; i <= N; ++i)
      p[i] = i;
  }

  int find(int i) {
    if (p[i] == i)
      return i;
    return p[i] = find(p[i]);
  }

  bool same(int i, int j) { return find(i) == find(j); }

  void merge(int i, int j) {
    if (same(i, j))
      return;
    int x = find(i), y = find(j);
    if (r[x] > r[y])
      swap(x, y);
    p[x] = y;
    if (r[x] == r[y])
      ++r[y];
    sz[y] += sz[x];
  }

  int op(int i) { return sz[find(i)]; }
};

int main() {
  int n, ans = 0;
  re(n);
  UF u = UF(MXN);
  while (n--) {
    int q, a[MXN];
    map<int, int> mp;
    re(q);
    FOR(q) {
      cin >> a[i];
      ++mp[u.find(a[i])];
    }
    bool ok = 1;
    for (auto x : mp) {
      // can't do it
      if (x.s != u.op(x.f)) {
        ok = 0;
        break;
      }
    }
    if (!ok)
      continue;
    // merge all
    ++ans;
    int fst = a[0];
    for (int i = 1; i < q; ++i)
      u.merge(fst, a[i]);
  }
  print(ans);
}
