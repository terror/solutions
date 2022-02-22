#include <bits/stdc++.h>

using namespace std;

int main() {
  int N, first;
  cin >> N >> first;

  N -= 1;

  bool reset = 0;

  while (N--) {
    int curr; cin >> curr;

    if (reset) {
      first = curr;
      reset = 0;
      continue;
    }

    if ((curr % first) == 0) {
      cout << curr << "\n";
      reset = 1;
    }
  }

  return 0;
}
