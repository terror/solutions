#include <bits/stdc++.h>

using namespace std;

int main() {
  int n; cin >> n;

  int ans = 0, last = 1;
  while (1) {
    n -= last * last;
    if (n < 0)
      break;
    last += 2;
    ++ans;
  }

  cout << ans << "\n";
}
