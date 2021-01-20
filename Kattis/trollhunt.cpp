#include <bits/stdc++.h>

using namespace std;
int b, k, g;

int main() {
  cin >> b >> k >> g;
  --b;
  // b%g==0 -> b/groups
  (b) % (k / g) == 0 ? cout << (b) / (k / g) : cout << (b) / (k / g) + 1;
}
