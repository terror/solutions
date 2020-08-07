#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int t;

int main() {
  cin >> t;
  while (t--) {
    int n, p, a[mxN];
    cin >> n >> p;

    for (int i = 0; i < p; ++i) cin >> a[i];
    int day = 1, ans = 0;
    string s[7] = {"su", "mo", "tu", "we", "th", "fr", "sa"};

    while (day <= n) {
      int x = (day - 1) % 7;
      if (s[x] != "sa" && s[x] != "fr") {
        for (int i = 0; i < p; ++i) {
          if (day % a[i] == 0) {
            ++ans;
            break;
          }
        }
      }
      ++day;
    }
    cout << ans << "\n";
  }
}
