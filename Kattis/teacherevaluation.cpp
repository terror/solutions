#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, m;
double s = 0;

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    s += x;
  }
  int ans = 0;
  bool p = true;
  if (s / n != m && m == 100) p = false;
  if (p) {
    while (s / n < m) {
      s += 100;
      ++n, ++ans;
    }
    cout << ans;
  } else
    cout << "impossible";

  return 0;
}
