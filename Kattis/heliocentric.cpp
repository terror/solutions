#include <bits/stdc++.h>

using namespace std;
int n, m;

int main() {
  int x = 1;
  while (cin >> n >> m) {
    bool ok = false;
    if (n == 0 && m == 0)
      ok = true;
    if (ok)
      cout << "Case " << x << ": " << 0 << "\n";
    else {
      int c = 1;
      while (true) {
        ++n, ++m, ++c;
        if (n == 365)
          n = 0;
        if (m == 687)
          m = 0;
        if (n == 0 && m == 0)
          break;
      }
      cout << "Case " << x << ": " << c - 1 << "\n";
    }
    ++x;
  }
}
