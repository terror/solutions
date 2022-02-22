#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, k, a[mxN];
double p;

int main() {
  cin >> n >> p >> k;
  a[0] = 0;
  for (int i = 1; i <= n; ++i)
    cin >> a[i];
  a[n + 1] = k;
  int curr = a[0];
  double ans = 0, speed = 1;

  for (int i = 1; i < n + 2; ++i)
    ans += abs((curr - a[i]) * speed), curr = a[i], speed += p / 100;

  cout << setprecision(2) << fixed << ans << "\n";
  return 0;
}
