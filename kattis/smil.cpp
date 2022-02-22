#include <bits/stdc++.h>

using namespace std;

int main() {
  string s; cin >> s;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == ':' or s[i] == ';') {
      // `:)`, `;)`
      if (i + 1 < s.length() and s[i + 1] == ')')
        cout << i << "\n";
      // `:-)`, `;-)`
      if (i + 2 < s.length() and s[i + 1] == '-' and s[i + 2] == ')')
          cout << i << "\n";
    }
  }
}
