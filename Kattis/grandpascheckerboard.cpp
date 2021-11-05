#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n;

int main() {
  cin >> n;
  char a[n][n];
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      cin >> a[i][j];

  bool ok = true;
  for (int i = 0; i < n; ++i) {
    int w = 0, b = 0, c = 1;
    char curr = ' ';
    for (int j = 0; j < n; ++j) {
      if (a[i][j] == 'W') {
        ++w;
        if (curr == 'B')
          c = 1;
        curr = 'W', ++c;
        if (c > 3)
          ok = false;
      }
      if (a[i][j] == 'B') {
        ++b;
        if (curr == 'W')
          c = 1;
        curr = 'B', ++c;
        if (c > 3)
          ok = false;
      }
    }
    if (b != w)
      ok = false;
  }

  if (ok) {
    for (int i = 0; i < n; ++i) {
      int w = 0, b = 0, c = 0;
      char curr = ' ';
      for (int j = 0; j < n; ++j) {
        if (a[j][i] == 'W') {
          ++w;
          if (curr == 'B')
            c = 1;
          curr = 'W', ++c;
          if (c > 3)
            ok = false;
        }
        if (a[j][i] == 'B') {
          ++b;
          if (curr == 'W')
            c = 1;
          curr = 'B', ++c;
          if (c > 3)
            ok = false;
        }
      }
      if (b != w)
        ok = false;
    }
  }
  ok ? cout << 1 : cout << 0;
  return 0;
}
