#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> v(n);

  for (auto &x : v)
    cin >> x;
  sort(v.begin(), v.end());

  for (auto x : v)
    cout << x << ' ';
  return 0;
}