#include <bits/stdc++.h>

using namespace std;
int n;

int main() {
  while (cin >> n && n != 0) {
    priority_queue<int, vector<int>, greater<int> > pq;
    for (int i = 0; i < n; ++i) {
      int x;
      cin >> x;
      pq.push(x);
    }

    int cost = 0;
    while (pq.size() != 1) {
      int a = pq.top();
      pq.pop();
      int b = pq.top();
      pq.pop();
      int c = a + b;
      cost += c;
      pq.push(c);
    }
    cout << cost << "\n";
  }
  return 0;
}
