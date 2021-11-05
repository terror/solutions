#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  ll n;
  cin >> n;
  ll arr[n];

  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  ll b = arr[0];
  ll m = arr[0];

  for (int i = 1; i < n; ++i) {
    b = max(arr[i], arr[i] + b);
    if (b > m)
      m = b;
  }

  cout << m << endl;
  return 0;
}