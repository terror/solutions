#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n;

int main() {
  while (cin >> n) {
    int a[mxN];
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    vector<bool> flags(n);
    for (int i = 1; i < n; ++i)
      if (abs(a[i] - a[i - 1]) > 0 && abs(a[i] - a[i - 1]) < n)
        flags[abs(a[i] - a[i - 1])] = true;
    bool ok = true;
    for (int i = 1; i < n; ++i)
      if (flags[i] == false)
        ok = false;
    ok ? cout << "Jolly"
              << "\n"
       : cout << "Not jolly"
              << "\n";
  }
}
