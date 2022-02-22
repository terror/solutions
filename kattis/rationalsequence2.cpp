#include <bits/stdc++.h>

using namespace std;
int n, a, b, c;
string p;
char x;

int main() {
  cin >> n;
  while (n--) {
    cin >> a >> b >> x >> c;
    p = "";

    while (b > 1 || c > 1) {
      if (c > b)
        p += "L", c -= b;
      if (b > c)
        p += "R", b -= c;
    }

    int ans = 0;
    // reverse path
    for (int i = p.length() - 1; i >= 0; --i) {
      if (p[i] == 'R')
        ans = (2 * ans) + 2;
      if (p[i] == 'L')
        ans = (2 * ans) + 1;
    }
    cout << a << " " << ans + 1 << "\n";
  }
}
