#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, a[mxN];

int main() {
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> a[i];
  int ans = 1;
  for (int i = 1; i < n; ++i)
    if (a[i - 1] < a[i]) ++ans;
  cout << ans;
  return 0;
}

