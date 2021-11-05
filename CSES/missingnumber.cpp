#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

  ll n, sum = 0;
  cin >> n;

  for (int i = 1; i < n; i++) {
    int t;
    cin >> t;
    sum += t;
  }

  cout << n * (n + 1) / 2 - sum << endl;
}