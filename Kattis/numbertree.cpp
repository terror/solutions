#include <bits/stdc++.h>

using namespace std;
int n;
string s;

int main() {
  cin >> n;
  cin >> s;

  int nodes = pow(2, n + 1) - 1, p = 0;

  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == 'L') p = (p * 2) + 1;
    if (s[i] == 'R') p = (p * 2) + 2;
  }
  cout << nodes - p;
}
