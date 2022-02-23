#include <bits/stdc++.h>

using namespace std;

const int R = 3;
const int C = 3;

vector<int> pattern[R];

#define pb push_back

struct Position {
  int x;
  int y;

  Position(int x, int y) {
    this->x = x;
    this->y = y;
  }
};

Position pos(int element) {
  for (int i = 0; i < R; ++i)
    for (int j = 0; j < C; ++j)
      if (pattern[i][j] == element)
        return Position(i, j);
  return Position(-1, -1);
}

double dist(int element) {
  Position a = pos(element), b = pos(element + 1);
  return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

int main() {
  for (int i = 0; i < R; ++i) {
    int a, b, c;
    cin >> a >> b >> c;
    pattern[i].pb(a);
    pattern[i].pb(b);
    pattern[i].pb(c);
  }

  double ans = 0;
  for (int i = 1; i <= 8; ++i)
    ans += dist(i);

  cout << setprecision(11) << ans << "\n";
}
