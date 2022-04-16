#include <bits/stdc++.h>

using namespace std;

#define Point pair<int, int>

double dist(Point a, Point b) {
  return sqrt(pow(b.first - a.first, 2) + pow(b.second - a.second, 2));
}

void solve() {
  double s, h; cin >> s >> h;

  vector<Point> points;
  while(h--) {
    int x, y;
    cin >> x >> y;
    points.push_back(make_pair(x, y));
  }

  vector<Point> ans;
  for (int i = 0; i <= s; ++i) {
    for (int j = 0; j <= s; ++j) {
      Point curr = make_pair(i, j);

      if (count(points.begin(), points.end(), curr))
        continue;

      double mx = 0;
      for (auto point : points)
        mx = max(mx, dist(curr, point));

      double x = curr.first, y = curr.second;
      if (mx <= x && mx <= s - x && mx <= y && mx <= s - y)
        ans.push_back(curr);
    }
  }

  sort(ans.begin(), ans.end());

  if (ans.empty())
    cout << "poodle" << '\n';
  else
    cout << ans[0].first << ' ' << ans[0].second << '\n';
}

int main() {
  int T; cin >> T;
  while (T--)
    solve();
}
