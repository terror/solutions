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

int A, B, M, x, y, c, a[mxN], b[mxN];

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  cin >> A >> B >> M;
  int mnA = mxN, mnB = mxN;
  for (int i = 0; i < A; ++i) {
    cin >> a[i];
    mnA = min(a[i], mnA);
  }
  for (int i = 0; i < B; ++i) {
    cin >> b[i];
    mnB = min(b[i], mnB);
  }

  int mn = mxN;
  for (int i = 0; i < M; ++i) {
    cin >> x >> y >> c;
    mn = min((a[x - 1] + b[y - 1]) - c, mn);
  }

  if (mnB + mnA < mn)
    cout << mnB + mnA;
  else
    cout << mn;

  return 0;
}

