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

int n, m, t, a[mxN], b[mxN], c[mxN];
vi v;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  cin >> n;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    a[i] = x;
    c[i] = x;
  }
  for (int i = 0; i < n; ++i)
    cin >> b[i];
  int diff1 = 0, diff2 = 0, i = 1;
  sort(c, c + n);
  do {
    bool c1 = true, c2 = true;
    for (int i = 0; i < n; ++i)
      if (a[i] != c[i])
        c1 = false;
    for (int i = 0; i < n; ++i)
      if (b[i] != c[i])
        c2 = false;
    if (c1)
      diff1 = i;
    if (c2)
      diff2 = i;
    ++i;
  } while (next_permutation(c, c + n));
  cout << abs(diff1 - diff2);
  return 0;
}
