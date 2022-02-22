#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int mxN = 2e5;

#define pb push_back
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int n, m, a, b;
vi adj[mxN], ans;
vector<bool> vis(mxN);

void dfs(int v) {
  vis[v] = true;
  for (auto u : adj[v])
    if (!vis[u])
      dfs(u);
}

vi cc() {
  FOR(i, 1, n) {
    if (!vis[i]) {
      ans.pb(i);
      dfs(i);
    }
  }
  return ans;
}

int main() {
  fast();
  cin >> n >> m;
  FOR(i, 0, m) {
    cin >> a >> b;
    --a, --b;
    adj[a].pb(b);
    adj[b].pb(a);
  }
  dfs(0);
  cc();
  cout << ans.size() << "\n";
  for (auto x : ans)
    cout << x << " " << ++x << "\n";
  return 0;
}
