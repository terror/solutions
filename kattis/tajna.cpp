#include <bits/stdc++.h>

using namespace std;

int main() {
  string s; cin >> s;

  int i = 1, rows = 0;
  while ((s.size() / i) >= i) {
    if (i * (s.size() / i) == s.size())
      rows = max(rows, i);
    ++i;
  }

  for (int i = 0; i < rows; ++i)
    for (int j = 0; j < s.size(); j += rows)
      cout << s[i + j];

  cout << '\n';
}
