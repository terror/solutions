#include <bits/stdc++.h>

using namespace std;
int a, b, h;

int main() {
  cin >> a >> b >> h;

  int ans = 0, c = 0;
  while (ans < h) {
    ++c;
    ans += a;
    if (ans >= h)
      break;
    ans -= b;
  }
  cout << c;
}
