#include <bits/stdc++.h>
using namespace std;
#define pb push_back
const int MXV = 10001;

void dfs(int v, vector<int> adj[], vector<bool> &vis, int &ans) {
  if (!vis[v])
    ++ans, vis[v] = true;
  for (auto u : adj[v]) {
    if (!vis[u]) {
      dfs(u, adj, vis, ans);
    }
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, m, l, ans = 0;
    vector<int> adj[MXV];
    vector<bool> vis(MXV);
    cin >> n >> m >> l;
    for (int i = 0; i < m; ++i) {
      int u, v;
      cin >> u >> v;
      adj[u].pb(v);
    }
    for (int i = 0; i < l; ++i) {
      int x;
      cin >> x;
      dfs(x, adj, vis, ans);
    }
    cout << ans << "\n";
  }
  return 0;
}
