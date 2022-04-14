#include <bits/stdc++.h>

using namespace std;

int main() {
  long long a, b, c, d;
  cin >> a >> b >> c >> d;

  if (c == 0 && d == 0) {
    cout << min(a, b) << '\n';
    return 0;
  }

  cout << (c * d) + (a * (d != 0)) + (b * (c != 0)) << '\n';
}
