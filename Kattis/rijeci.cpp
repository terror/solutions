#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int a = 1, b = 0;

  int n;
  cin >> n;

  while (n--) {
    int t = b;
    b = a;
    a += t;
  }

  cout << a - b << " " << b << endl;

  return 0;
}