#include <bits/stdc++.h>

using namespace std;
const int MXN = 2e5;
int n, m, t;

int main() {
  cin >> t;
  while (t--) {
    cin >> n >> m;
    int a[MXN];
    vector<int> idx;
    for (int i = 0; i < n; ++i) cin >> a[i];
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (a[i] == m) {
        int msf = m;
        for (int j = i - 1; ~j; --j)
          if (a[j] > m)
            msf += a[j];
          else
            break;
        for (int j = i + 1; j < n; ++j)
          if (a[j] > m)
            msf += a[j];
          else
            break;
        ans = max(msf, ans);
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
