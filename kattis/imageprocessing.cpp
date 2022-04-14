#include <bits/stdc++.h>

using namespace std;

int main() {
  int h, w, n, m;
  cin >> h >> w >> n >> m;

  int mat[h][w];
  for (int i = 0 ; i < h; ++i)
    for (int j = 0; j < w; ++j)
      cin >> mat[i][j];

  vector<vector<int> > ker;
  for (int i = 0; i < n; ++i) {
    vector<int> row;
    for (int j = 0; j < m; ++j) {
      int x; cin >> x;
      row.push_back(x);
    }
    ker.push_back(row);
  }

  for (int i = 0; i < n; ++i)
    reverse(ker[i].begin(), ker[i].end());

  reverse(ker.begin(), ker.end());

  vector<vector<int> > ans;
  for (int i = 0; i < h - n + 1; ++i) {
    vector<int> row;
    for (int j = 0; j < w - m + 1; ++j) {
      int res = 0;
      for (int k = 0; k < n; ++k)
        for (int l = 0; l < m; ++l)
          res += mat[i + k][j + l] * ker[k][l];
      row.push_back(res);
    }
    ans.push_back(row);
  }

  for(int i = 0; i < ans.size(); ++i) {
    for (int j = 0; j < ans[0].size(); ++j)
      cout << ans[i][j] << ' ';
    cout << '\n';
  }
}
