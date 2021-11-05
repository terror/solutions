#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int h, w, n, a[mxN];

int main() {
  cin >> h >> w >> n;

  for (int i = 0; i < n; ++i)
    cin >> a[i];

  int s = 0;
  bool ok = true;

  for (int i = 0; i < n; ++i) {
    if (h <= 0)
      break;
    s += a[i];
    if (s == w)
      s = 0, --h;
    if (s > w)
      ok = false;
  }

  if (ok)
    cout << "YES";
  else
    cout << "NO";

  return 0;
}