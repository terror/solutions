#include <bits/stdc++.h>

using namespace std;
int n, a, b;

int main() {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a >> b;
    bool p = false;
    for (int j = 0; j <= a; ++j) {
      for (int k = 0; k <= a; ++k) {
        if (abs(k - j) == b and j + k == a) {
          cout << k << " " << j << "\n";
          p = true;
          break;
        }
      }
      if (p)
        break;
    }
    if (!p) {
      cout << "impossible"
           << "\n";
    }
  }
}
