#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<pair<int, int> > v;
  for (int i = 0; i < n; ++i) {
    int a, b;
    cin >> a >> b;
    v.push_back(make_pair(a, b));
  }

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (i != j && v[j].first > v[i].second) {
        cout << "edward is right";
        return 0;
      }
    }
  }

  cout << "gunilla has a point";
  return 0;
}
