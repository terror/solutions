#include <bits/stdc++.h>

using namespace std;

int main() {
  string t, s;
  cin >> t;
  s = t;
  int u = 0, d = 0, x = 0;

  // some case work
  for (int i = 1; i < s.length(); ++i) {
    if (s[i] != s[i - 1])
      ++u, s[i - 1] = s[i];
    if (s[i - 1] != 'U')
      ++u, s[i] = 'U';
  }

  s = t;
  for (int i = 1; i < s.length(); ++i) {
    if (s[i] != s[i - 1])
      ++d, s[i - 1] = s[i];
    if (s[i - 1] != 'D')
      ++d, s[i] = 'D';
  }

  s = t;
  for (int i = 1; i < s.length(); i++)
    if (s[i] != s[i - 1])
      ++x, s[i - 1] = s[i];

  cout << u << "\n" << d << "\n" << x;
}
