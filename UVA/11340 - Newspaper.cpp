#include <bits/stdc++.h>

using namespace std;
int t;

int main() {
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    map<char, int> mp;
    while (n--) {
      char a;
      int b;
      cin >> a >> b;
      mp[a] = b;
    }
    int x;
    cin >> x;
    ++x;
    double tot = 0;
    while (x--) {
      string s;
      getline(cin, s);
      for (int i = 0; i < s.length(); ++i) {
        if (mp.find(s[i]) != mp.end()) tot += mp[s[i]];
      }
    }
    printf("%0.2lf$\n", tot / 100);
  }
  return 0;
}
