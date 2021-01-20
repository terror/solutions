#include <bits/stdc++.h>

using namespace std;
int n, a, b;

int main() {
  cin >> n >> a >> b;
  int r = 4, t = 3, rs = 0, ts = 0;
  while (1) {
    if (rs + r >= a) break;
    rs += r++;
  }
  while (1) {
    if (ts + t >= b) break;
    ts += t++;
  }
  int ans = 0;
  while (abs(t - r) > n) {
    ++ans, --a, ++b, r = 4, t = 3, rs = 0, ts = 0;
    while (1) {
      if (rs + r >= a) break;
      rs += r++;
    }
    while (1) {
      if (ts + t >= b) break;
      ts += t++;
    }
  }
  cout << ans;
  return 0;
}
