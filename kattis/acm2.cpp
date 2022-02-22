#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define INF (int)1e9
typedef long long ll;
typedef vector<int> vi;
ll n, p;

int main() {
  cin >> n >> p;
  vi v(n);
  for (auto &x : v)
    cin >> x;

  if (v[p] > 300) {
    cout << 0 << ' ' << 0;
    return 0;
  }
  ll np = 1, time = v[p];
  ll pen = v[p];

  v.erase(v.begin() + p);
  sort(v.begin(), v.end());

  for (auto x : v) {
    if (x > 300)
      break;
    if (time + x <= 300)
      pen += time + x, time += x, ++np;
  }

  cout << np << ' ' << pen << "\n";

  return 0;
}