#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  int xs = 0, ys = 0, zs = 0;
  for (int i = 0; i < n; ++i) {
    int x, y, z;
    cin >> x >> y >> z;
    xs += x;
    ys += y;
    zs += z;
  }
  xs == 0 and ys == 0 and zs == 0 ? cout << "YES" : cout << "NO";
}
