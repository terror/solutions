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

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }
const int mxV = 10001;

int n, m, u, v;
vi adj[mxV];
bool t[mxV], p[mxV], f = true;

void verify(int curr) {
  if (t[curr]) {
    f = false;
    return;
  }
  if (p[curr])
    return;
  t[curr] = true;
  for (int i = 0; i < adj[curr].size(); ++i)
    verify(adj[curr][i]);
  t[curr] = false, p[curr] = true;
}

int main() {
  fast();
  cin >> n >> m;
  while (m--) {
    cin >> u >> v;
    adj[u].pb(v);
  }

  for (int i = 1; i <= n; ++i) {
    if (!f)
      break;
    verify(i);
  }

  f ? cout << "Y" : cout << "N";

  return 0;
}
