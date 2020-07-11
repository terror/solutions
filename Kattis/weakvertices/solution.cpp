#include <bits/stdc++.h>

using namespace std;

const int mxV = 1010;
int n, m, t;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  int n;
  while (cin >> n && n != -1) {
    int adj[mxV][mxV];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) cin >> adj[i][j];

    for (int i = 0; i < n; i++) {
      bool w = true;
      for (int j = 0; j < n; j++)
        for (int k = 0; k < n; k++)
          if (adj[i][j] == 1 && adj[i][k] == 1 && adj[j][k] == 1 && i != k &&
              i != j && j != k)
            w = false;
      if (w) cout << i << " ";
    }
    cout << "\n";
  }
  return 0;
}
