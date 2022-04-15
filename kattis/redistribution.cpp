#include <bits/stdc++.h>

using namespace std;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
  return a.second < b.second;
}

int main() {
  int N; cin >> N;

  vector<pair<int, int> > v; int s = 0;
  for (int i = 0; i < N; ++i) {
    int x; cin >> x; s += x;
    v.push_back(make_pair(i + 1, x));
  }

  sort(v.rbegin(), v.rend(), cmp);

  if (s < v[0].second * 2) {
    cout << "impossible" << '\n';
  } else {
    for (auto p : v)
      cout << p.first << ' ';
    cout << '\n';
  }
}
