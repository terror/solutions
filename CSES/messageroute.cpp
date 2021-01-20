#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int mxN = 2e5;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)

int n, m, u, v;
vi adj[mxN], ans, d;
vector<bool> vis(mxN);
void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  cin >> n >> m;
  FOR(i, 0, m) {
    cin >> u >> v;
    adj[u].pb(v);
    adj[v].pb(u);
  }
  ans.pb(1);
  d.assign(n, 10000000);
  d[1] = 0;
  set<pair<int, int> > q;
  q.insert({1, 0});
  while (!q.empty()) {
    int v = q.begin()->s;
    q.erase(q.begin());
    for (auto e : adj[v]) {
      if (d[v] < d[e]) {
        q.erase({d[e], e});
        d[e] = d[v];
        q.insert({d[e], e});
      }
    }
  }
  cout << ans.size() << "\n";
  for (auto v : ans) cout << v << " ";

  return 0;
}

