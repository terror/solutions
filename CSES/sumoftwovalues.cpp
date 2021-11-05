#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, x;
  cin >> n >> x;
  map<int, int> m;
  vector<int> ans;

  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    if (m.find(num) == m.end()) {
      m[x - num] = i + 1;
    } else {
      ans.push_back(m[num]);
      ans.push_back(i + 1);
    }
  }

  if (!ans.empty()) {
    for (auto x : ans)
      cout << x << ' ';
  } else {
    cout << "IMPOSSIBLE" << endl;
  }

  return 0;
}