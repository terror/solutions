#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  map<int, string> mp;
  mp[1] = "single";
  mp[2] = "double";
  mp[3] = "triple";
  cin >> n;
  vector<int> mul, val;
  for (int i = 1; i <= 20; ++i) {
    for (int j = 1; j <= 3; ++j) {
      if (j * i == n) {
        cout << mp[j] << " " << i;
        return 0;
      }
      mul.push_back(j);
      val.push_back(i);
    }
  }
  for (int i = 0; i < val.size(); ++i) {
    for (int j = 0; j < val.size(); ++j) {
      if (val[i] * mul[i] + val[j] * mul[j] == n) {
        cout << mp[mul[i]] << " " << val[i] << "\n";
        cout << mp[mul[j]] << " " << val[j];
        return 0;
      }
      for (int k = 0; k < val.size(); ++k) {
        if (val[i] * mul[i] + val[j] * mul[j] + val[k] * mul[k] == n) {
          cout << mp[mul[i]] << " " << val[i] << "\n";
          cout << mp[mul[j]] << " " << val[j] << "\n";
          cout << mp[mul[k]] << " " << val[k] << "\n";
          return 0;
        }
      }
    }
  }
  cout << "impossible";
  return 0;
}
