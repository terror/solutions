#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int n, m;

void move(char d, int l, int& x, int& y) {
  if (d == 'u') y += l;
  if (d == 'd') y -= l;
  if (d == 'r') x += l;
  if (d == 'l') x -= l;
}

void move2(char d, int l, int& x, int& y) {
  if (d == 'u') y = min(m, y + l);
  if (d == 'd') y = max(0, y - l);
  if (d == 'r') x = min(n, x + l);
  if (d == 'l') x = max(0, x - l);
}

int main() {
  while (cin >> n >> m) {
    if (n == 0 and m == 0) break;
    --n, --m;
    int t, tx = 0, ty = 0, x = 0, y = 0;
    cin >> t;
    while (t--) {
      char dir;
      int l;
      cin >> dir >> l;
      move(dir, l, tx, ty);
      move2(dir, l, x, y);
    }
    cout << "Robot thinks " << tx << " " << ty << "\n";
    cout << "Actually at " << x << " " << y << "\n";
    cout << "\n";
  }
}

