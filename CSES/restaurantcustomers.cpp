#include <bits/stdc++.h>

using namespace std;

const int mxN = 2e5;
#define MP make_pair
#define PB push_back
typedef pair<int, bool> PIB;
typedef vector<PIB> VPIB;
int a, b, n, c = 0, mx = 0;

int main() {
  cin >> n;
  VPIB v;

  while (n--) {
    cin >> a >> b;
    v.PB(MP(a, true)), v.PB(MP(b, false));
  }

  sort(v.begin(), v.end());

  for (int i = 0; i < v.size(); ++i) {
    c += v[i].second ? 1 : -1;
    mx = max(mx, c);
  }

  cout << mx;
}