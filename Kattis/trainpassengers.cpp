#include <bits/stdc++.h>

using namespace std;

int main() {
  int C, n, c = 0;
  cin >> C >> n;
  bool p = true;
  for (int i = 0; i < n; ++i) {
    int a, b, s;
    cin >> a >> b >> s;
    c -= a;
    if (c < 0) p = false;
    c += b;
    if ((c < 0 || c > C) || (c < C && s > 0) || (i == n - 1 && s > 0) ||
        (i == n - 1 && c > 0))
      p = false;
  }
  p ? cout << "possible" : cout << "impossible";
  return 0;
}
