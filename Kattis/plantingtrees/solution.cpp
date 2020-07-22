#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, d = 1, mx = 0, a[mxN];

int main()
{
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> a[i];
  sort(a, a + n, greater<int>());
  for (int i = 0; i < n; ++i)
    mx = max(mx, a[i] + d), ++d;
  cout << ++mx;
}
