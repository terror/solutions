#include <bits/stdc++.h>

using namespace std;
int b, d, c, l;

int main() {
  cin >> b >> d >> c >> l;
  bool p = false;
  for (int i = 0; i <= l; ++i)
    for (int j = 0; j <= l; ++j)
      for (int k = 0; k <= l; ++k) {
        if ((b * i) + (d * j) + (c * k) == l) {
          p = true;
          cout << i << " " << j << " " << k << "\n";
        }
      }
  p == false ? cout << "impossible" : cout << "";
}
