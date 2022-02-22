#include <bits/stdc++.h>

using namespace std;
int n, p;

int main() {
  cin >> n >> p;
  vector<int> vi;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    vi.push_back(x - p);
  }

  int msf = vi[0], mx = vi[0];
  for (int i = 1; i < n; ++i) {
    msf = max(vi[i], vi[i] + msf);
    mx = max(mx, msf);
  }
  cout << mx << "\n";
}
