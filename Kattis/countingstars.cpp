#include <bits/stdc++.h>

using namespace std;

const int MXN = 101;
int n, m;

// NWES
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int floodfill(int r, int c, char c1, char c2, char adj[MXN][MXN]) {
  if (r < 0 or r >= n or c < 0 or c >= m)
    return 0;
  if (adj[r][c] != c1)
    return 0;
  adj[r][c] = c2;
  for (int d = 0; d < 4; ++d)
    floodfill(r + dr[d], c + dc[d], c1, c2, adj);
  return 1;
}

int main() {
  int x = 1;
  while (cin >> n >> m) {
    char adj[MXN][MXN];
    int ans = 0;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        cin >> adj[i][j];

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        ans += floodfill(i, j, '-', 'x', adj);

    cout << "Case " << x << ": " << ans << "\n";
    ++x;
  }
}
