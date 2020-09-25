#include <bits/stdc++.h>

using namespace std;
int n, m, t;
string s1, s2;

int main() {
  cin >> n >> m;
  cin >> s1 >> s2;
  cin >> t;
  reverse(s1.begin(), s1.end());
  if (t == 0) {
    cout << s1 << s2;
    return 0;
  }
  string x = s1 + s2;
  int c = 0;
  while (1) {
    for (int j = 0; j < x.length() - 1; ++j) {
      if (s1.find(x[j]) != string::npos and s2.find(x[j + 1]) != string::npos)
        swap(x[j], x[j + 1]), ++j;
    }
    if (++c == t) {
      cout << x;
      return 0;
    }
  }
  return 0;
}
