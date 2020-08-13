#include <bits/stdc++.h>

using namespace std;
int n;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  cin >> n;
  char curr;
  set<string> s;
  for (int i = 0; i < n; ++i) {
    string w;
    cin >> w;
    if (s.find(w) != s.end() || (i > 0 && w[0] != curr)) {
      i % 2 == 0 ? cout << "Player 1 lost" : cout << "Player 2 lost";
      return 0;
    }
    s.insert(w);
    curr = w[w.length() - 1];
  }
  cout << "Fair Game";
  return 0;
}
