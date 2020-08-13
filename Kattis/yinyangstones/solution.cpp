#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;
  cin >> s;
  int b = 0, w = 0;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == 'W')
      ++w;
    else
      ++b;
  }
  b == w ? cout << 1 : cout << 0;
  return 0;
}

