#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, m, a[mxN];

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) cin >> a[i];
  int mx = 0;
  for (int i = 0; i < n; ++i) {
    int x = 1, curr = a[i];
    for (int j = i + 1; j < n; ++j)
      if (curr + a[j] <= m) curr += a[j], ++x;
    mx = max(mx, x);
  }
  cout << mx;
}

