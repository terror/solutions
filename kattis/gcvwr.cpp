#include <bits/stdc++.h>

using namespace std;

int main() {
  int G, T, n;
  cin >> G >> T >> n;

  int ret = (G - T) * 0.9;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    ret -= x;
  }

  cout << ret << "\n";
}
