#include <bits/stdc++.h>

using namespace std;

int main() {
  int a, b, c; cin >> a >> b >> c;

  if (!((a < b && b < c) || (a > b && b > c))) {
    cout << "turned" << '\n';
    return 0;
  }

  if (abs(a - b) == abs(b - c)) {
    cout << "cruised" << '\n';
    return 0;
  }

  if (abs(a - b) > abs(b - c)) {
    cout << "braked" << '\n';
    return 0;
  }

  if (abs(a - b) < abs(b - c)) {
    cout << "accelerated" << '\n';
    return 0;
  }
}
