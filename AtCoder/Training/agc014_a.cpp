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
vi v;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  int a, b, c, ans = 0;
  bool ok = true;
  cin >> a >> b >> c;
  if (a == b && c == b && a == c && a % 2 == 0) {
    ok = false;
    cout << "-1";
  }
  if (a == b && c == b && a == c && a % 2 == 1) {
    ok = false;
    cout << "0";
  }

  if (ok) {
    while (a % 2 == 0 && b % 2 == 0 && c % 2 == 0) {
      int A = a, B = b, C = c;
      a = (A + B) / 2;
      b = (B + C) / 2;
      c = (C + A) / 2;
      ++ans;
    }
    cout << ans;
  }
  return 0;
}
