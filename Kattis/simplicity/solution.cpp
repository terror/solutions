#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
string s;

int main() {
  cin >> s;
  map<char, int> mp;
  for (int i = 0; i < s.length(); ++i) {
    if (mp.find(s[i]) == mp.end())
      mp[s[i]] = 1;
    else
      mp[s[i]] += 1;
  }
  vector<int> vals(mxN);
  for (auto x : mp) {
    vals.push_back(x.second);
  }
  sort(vals.begin(), vals.end());
  int ans = 0;
  for (int i = 0; i < vals.size() - 2; ++i) {
    ans += vals[i];
  }
  cout << ans;
  return 0;
}
