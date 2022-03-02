#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, s; cin >> n >> s;

  int curr = s, ans = 0;
  while (n--) {
    string o; cin >> o;
    int amt = o[0] - '0' + (o.size() == 2 ? 1 : 0);
    if (curr - amt < 0) {
      curr = s;
      ++ans;
    }
    curr -= amt;
  }

  cout << ans << '\n';
}
