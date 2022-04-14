#include <bits/stdc++.h>

using namespace std;

int main() {
  string s; cin >> s;

  int cursor = 0;
  vector<char> ret;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == 'L')
      --cursor;
    else if (s[i] == 'R')
      ++cursor;
    else if (s[i] == 'B') {
      --cursor;
      ret.erase(ret.begin() + cursor);
    } else  {
      ret.insert(ret.begin() + cursor, s[i]);
      ++cursor;
    }
  }

  for (int i = 0; i < ret.size(); ++i)
    cout << ret[i];
  cout << '\n';
}
