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
  string s;
  cin >> s;
  string t = "abcdefghijklmnopqrstuvwxyz";
  sort(s.begin(), s.end());
  char ans = ' ';
  bool ok;
  for (int i = 0; i < t.length(); ++i) {
    ok = true;
    for (int j = 0; j < s.length(); ++j) {
      if (t[i] == s[j]) ok = false;
    }
    if (ok) {
      ans = t[i];
      break;
    }
  }

  if (ok == false)
    cout << "None";
  else
    cout << ans;

  return 0;
}

