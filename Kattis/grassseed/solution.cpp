#include <bits/stdc++.h>

using namespace std;
double n, x;

int main() {
  cin >> n;
  cin >> x;

  double tot = 0;
  while (x--) {
    double a, b;
    cin >> a >> b;
    tot += a * b;
  }
  printf("%.7lf\n", n * tot);
  return 0;
}
