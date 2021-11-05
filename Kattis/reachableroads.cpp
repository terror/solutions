#include <bits/stdc++.h>

using namespace std;
#define pb push_back
const int mxV = 1010;
int n, m, r;
vector<int> adj[mxV];
vector<bool> vis(mxV);

void dfs(int v) {
  vis[v] = true;
  for (int i = 0; i < adj[v].size(); ++i)
    if (!vis[adj[v][i]])
      dfs(adj[v][i]);
}

int cc() {
  int ans = 0;
  for (int i = 0; i < m; ++i)
    vis[i] = false;
  for (int i = 0; i < m; ++i) {
    if (!vis[i]) {
      ++ans;
      dfs(i);
    }
  }
  return ans;
}

int main() {
  cin >> n;
  while (n--) {
    cin >> m >> r;
    for (int i = 0; i < r; ++i) {
      int u, v;
      cin >> u >> v;
      adj[u].pb(v);
      adj[v].pb(u);
    }
    dfs(0);
    cout << cc() - 1 << "\n";
    for (auto &v : adj)
      v.clear();
    vis.clear();
  }
}
