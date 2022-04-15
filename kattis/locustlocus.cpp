#include <bits/stdc++.h>

using namespace std;

const int MXN = 2e5;

int gcd(int a, int b) {
  if (a == b)
    return a;
  if (a > b)
    return gcd(a - b, b);
  return gcd(a, b - a);
}

int lcm(int a, int b) {
  return (a * b) / gcd(a, b);
}

int main() {
  int N; cin >> N;

  int ans = MXN;
  while (N--) {
    int y, a, b; cin >> y >> a >> b;
    ans = min(ans, y + lcm(a, b));
  }

  cout << ans << '\n';
}
