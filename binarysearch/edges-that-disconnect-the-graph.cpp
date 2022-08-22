vector<bool> vis;
vector<int> tin, low;

int ans = 0, t = 0;

void dfs(int v, auto g, int p = - 1) {
  vis[v] = 1;
  tin[v] = low[v] = t++;
  for (auto u : g[v]) {
    if (u == p)
      continue;
    if (vis[u])
      low[v] = min(low[v], tin[u]);
    else {
      dfs(u, g, v);
      low[v] = min(low[v], low[u]);
      ans += low[u] > tin[v];
    }
  }
}

int solve(vector<vector<int>>& graph) {
  int N = graph.size();

  vis.assign(N, false);
  tin.assign(N, -1);
  low.assign(N, -1);
  ans = t = 0;

  for (int i = 0; i < N; ++i)
    if (!vis[i]) dfs(i, graph);

  return ans;
}
