#include <bits/stdc++.h>

using namespace std;

int main() {
  long long L, N; cin >> L >> N;

  long long ans = 0;
  while ((L % N) != 0) {
    N -= L % N;
    ++ans;
  }

  cout << ans + 1 << "\n";
}
