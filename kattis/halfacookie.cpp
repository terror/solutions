#include <bits/stdc++.h>

using namespace std;
const double PI = 4.0 * atanl(1.0);

double area(double r) { return PI * pow(r, 2); }

int main() {
  double r, x, y;
  while (cin >> r >> x >> y) {
    if (!(pow(x, 2) + pow(y, 2) <= pow(r, 2))) {
      cout << "miss"
           << "\n";
      continue;
    }

    double a = area(r), ch = r - sqrt(pow(x, 2) + pow(y, 2));
    double seg =
        pow(r, 2) * acos((r - ch) / r) - (r - ch) * sqrt(2 * r * ch - ch * ch);

    cout << fixed << setprecision(6) << max(a - seg, seg) << " "
         << min(a - seg, seg) << "\n";
  }
  return 0;
}
