#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n, k;
  cin >> n >> k;

  bool prime[n + 1];
  memset(prime, true, sizeof(prime));

  for (int i = 2; i <= n; i++) {
    if (prime[i]) {
      for (int j = i; j <= n; j += i) {
        if (prime[j]) {
          prime[j] = false;
          if (--k == 0) {
            cout << j;
            return 0;
          }
        }
      }
    }
  }
  return 0;
}
