#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, m;

int main() {
  while (cin >> n >> m && n != 0 && m != 0) {
    int a[mxN], b[mxN], ans = 0;
    bool c = true;
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];
    sort(a, a + n), sort(b, b + m);

    // greedy matching
    for (int i = 0, j = 0; i < n && c; ++i) {
      while (j < m && a[i] > b[j]) ++j;
      if (j == m) c = false;
      ans += b[j];
      ++j;
    }

    if (c)
      cout << ans << "\n";
    else
      cout << "Loowater is doomed!"
           << " \n";
  }
}
