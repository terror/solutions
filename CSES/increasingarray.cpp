#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;

int main() {

  ll n;
  cin >> n;

  ll arr[n];

  for (ll i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  ll t = 0;
  for (ll i = 1; i < n; ++i) {
    if (arr[i] < arr[i - 1]) {
      while (arr[i] != arr[i - 1]) {
        t += 1;
        arr[i] += 1;
      }
    }
  }

  cout << t << endl;

  return 0;
}