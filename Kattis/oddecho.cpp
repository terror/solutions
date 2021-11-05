#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    string s;
    cin >> s;
    if (i & 1) {
      cout << s << '\n';
    }
  }
  return 0;
}
