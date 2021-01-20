#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;
  cin >> s;

  map<char, char> mp;
  mp['R'] = 'S';
  mp['B'] = 'K';
  mp['L'] = 'H';

  int i = 0;
  while (i < s.length()) {
    if (i + 2 < s.length()) {
      set<char> c;
      c.insert(s[i]);
      c.insert(s[i + 1]);
      c.insert(s[i + 2]);
      if (c.size() == 3) {
        cout << "C";
        i += 3;
      } else
        cout << mp[s[i]], ++i;
    } else
      cout << mp[s[i]], ++i;
  }
  return 0;
}

